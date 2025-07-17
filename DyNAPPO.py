#   FILE: DyNAPPO.py
#   PROJECT: Optimal Ensemble Weights DyNA PPO
#   AUTHOR: Eric Lin
#   

import numpy as np
import torch.optim as optim
from typing import List, Tuple, Dict, Optional
import torch
import torch.nn.functional as F
from torch.distributions import Categorical

# File import
from SurrogateModel import SurrogateModel
from PolicyNetwork import PolicyNetwork
from SequenceUtils import compute_diversity_penalty, sequence_to_features, edit_distance

class DyNAPPO:
    
    def __init__(self, vocab_size: int, max_seq_len: int, batch_size: int = 64,
                 learning_rate: float = 3e-4, gamma: float = 0.99, clip_ratio: float = 0.2,
                 model_threshold: float = 0.5, max_model_rounds: int = 10,
                 diversity_lambda: float = 0.1, diversity_epsilon: int = 2):
        
        self.vocab_size = vocab_size
        self.max_seq_len = max_seq_len
        self.batch_size = batch_size
        self.gamma = gamma
        self.clip_ratio = clip_ratio
        self.model_threshold = model_threshold
        self.max_model_rounds = max_model_rounds
        self.diversity_lambda = diversity_lambda
        self.diversity_epsilon = diversity_epsilon
        
        # Initialize policy network
        self.policy_net = PolicyNetwork(vocab_size, max_seq_len)
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=learning_rate)
        
        # Surrogate models
        self.surrogate_models = self.create_surrogate_models()

        # Data storage
        self.all_data = []
        self.sequence_history = []


    """
    Create a pool of surrogate models with different complexities
    """
    def create_surrogate_models(self, data_size: int = 0) -> List[SurrogateModel]:
        
        models = []
        
        # Scale parameters based on data size
        base_estimators = max(100, min(500, data_size // 10))
        max_depth = max(10, min(20, data_size // 50))

        # Random Forest
        models.append(SurrogateModel('rf', n_estimators=50, max_depth=5))
        models.append(SurrogateModel('rf', n_estimators=100, max_depth=10))
        models.append(SurrogateModel('rf', n_estimators=200, max_depth=None))
        models.append(SurrogateModel('rf', n_estimators=base_estimators, max_depth=max_depth))
        models.append(SurrogateModel('rf', n_estimators=base_estimators*2, max_depth=None))
        
        # Gradient Boosting
        models.append(SurrogateModel('gb', n_estimators=50, max_depth=3))
        models.append(SurrogateModel('gb', n_estimators=100, max_depth=5))
        gb_estimators = max(50, min(300, data_size // 20))
        models.append(SurrogateModel('gb', n_estimators=gb_estimators, max_depth=max_depth//2))
        
        # Other
        models.append(SurrogateModel('knn', n_neighbors=5))
        models.append(SurrogateModel('knn', n_neighbors=10))
        k_neighbors = max(5, min(50, int(np.sqrt(data_size))))
        models.append(SurrogateModel('knn', n_neighbors=k_neighbors))
        models.append(SurrogateModel('ridge'))
        models.append(SurrogateModel('xgb', n_estimators=200, max_depth=8, learning_rate=0.1))
        models.append(SurrogateModel('mlp', hidden_layer_sizes=(128, 64, 32), max_iter=500))
        models.append(SurrogateModel('svr', kernel='rbf', C=1.0, gamma='scale'))
        
        return models
    
    """
    Generate a single sequence using the current policy.

    ***
    For each position t in the sequence:
        - get policy probabilities π_θ(a_t|s_t) from PolicyNetwork
        - samples action a_t from this distribution, or takes argmax if deterministic
        - appends the sampled token to the sequence
    
    Sum over a_t: implemented by sampling actions from the policy
    Implements the sampling of trajectories needed to approximate the expectation E[R(s_{1:T})|s_0, θ]

    ***
    DNA Example: Building "GGCGTACC" one base at a time
    Position 0: Choose G (from A,T,G,C)
    Position 1: Choose G (given we have "G")
    Position 2: Choose C (given we have "GG")
    ... and so on
    """
    def generate_sequence(self, deterministic: bool = False) -> List[int]:
        # This samples actions a_t from π_θ(a_t|s_t) at each step

        sequence = []

        # Disable gradient computation for inference
        with torch.no_grad():
            # Build sequence position by position (8 bases for our DNA)
            for t in range(self.max_seq_len):   # t = 0,1,2...7
                # Current sequence as tensor
                # Prepare current sequence state for the neural network
                'Example at t=3: sequence=[2,2,1] (GGC), pad with zeros: [2,2,1,0,0,0,0,0]'
                seq_tensor = torch.tensor([sequence + [0] * (self.max_seq_len - len(sequence))], dtype=torch.long)
                # Current position in sequence
                pos_tensor = torch.tensor([t])
                
                # Get policy probabilities
                # *** Get π_θ(a_t|s_t) from PolicyNetwork
                'Ask PolicyNetwork: Given GGC at position 3, what base should come next?'
                'Returns probability distribution, e.g., [0.1, 0.15, 0.6, 0.15] for [A,T,G,C]'
                policy_probs, _ = self.policy_net(seq_tensor, pos_tensor)
                
                # Choose the next base
                # *** SAMPLE a_t from π_θ(a_t|s_t) - this approximates the sum over a_t
                if deterministic:
                    # Always pick highest probability base
                    'Example: argmax([0.1, 0.15, 0.6, 0.15]) = 2 (G)'
                    action = torch.argmax(policy_probs[0]).item()
                else:
                    # Sample from probability distribution (exploration)
                    'Example: might pick G (60% chance), but could pick C (15% chance)'
                    dist = Categorical(policy_probs[0])
                    action = dist.sample().item()   # Sample one a_t
                
                # Add chosen base to sequence
                'Example: sequence goes from [2,2,1] to [2,2,1,2] (GGC → GGCG)'
                sequence.append(action)
        
        return sequence
    

    """
    Generate a batch of sequences.

    *** 
    Each sequence represents a different trajectory, helping approximate the sum over different states s_t in the expectation
    Sum over s_t: implemented by generating multiple sequences

    ***
    DNA Example: Generate 32 different DNA sequences for lab testing
    Each represents a different "trajectory" through sequence space
    """
    def generate_batch(self, batch_size: int) -> List[List[int]]:
        # This samples different trajectories, covering different s_t states
        '''
            Example output for batch_size=4:
            [
            [2,2,1,2,1,0,1,1],  GGCGTACC
            [1,0,1,2,1,0,1,2],  TACGTACG
            [2,1,1,2,1,0,1,1],  GTCGTACC
            [0,2,1,2,1,0,1,1],  AGCGTACC
            ]
        '''
        return [self.generate_sequence() for _ in range(batch_size)]
    

    """
    Compute rewards for sequences
    Evaluates sequences using the oracle function f(x) and applies diversity penalty

    ***
        - get base rewards from oracle function
        - if diversity is enabled, substracts a penalty based on how similar the sequence is to previously generated sequences
        - final reward = f(x) - λ·penalty

    ***
    DNA Example: Lab tests each sequence for binding affinity, then applies diversity bonus to encourage variety
    """
    def compute_rewards(self, sequences: List[List[int]], oracle_fn, use_diversity: bool = True) -> List[float]:
        rewards = []
        for seq in sequences:
            # Get actual binding affinity from wet lab
            'Example: oracle_fn([2,2,1,2,1,0,1,1]) = 0.85 (strong binding)'
            base_reward = oracle_fn(seq)
            
            if use_diversity:
                # Check how similar this sequence is to previous ones
                '''
                Example: If we already tested 5 sequences very similar to GGCGTACC:
                    - Edit distance to "GGCGTACC" = 0 → high penalty
                    - Edit distance to "GGCGTACG" = 1 → medium penalty  
                    - Edit distance to "TACGTACG" = 4 → no penalty
                '''
                diversity_penalty = compute_diversity_penalty(seq, 
                                                              self.sequence_history, # All previously generated sequences
                                                              self.diversity_lambda, # Penalty strength
                                                              self.diversity_epsilon # Similarity threshold
                                                              )
                # Final reward encourages both high binding AND novelty
                'Example: 0.85 - 0.05 = 0.80 (good binding, but similar to others)'
                reward = base_reward - diversity_penalty
            else:
                reward = base_reward
            
            rewards.append(reward)
        
        return rewards
    


    """
    Update policy using PPO
    Uses sampled trajectories to approximate gradient of expectation

    *** 
    In PPO update, we use the sampled trajectories to estimate gradients

        - computes current log probabilities for each sequence
        - calculates advantages: rewards - baseline values
        - computes PPO loss with clipping to prevent large updates
        - updates both policy and value networds
    
    *** Example
    Round 1 Update:
        Sequence: ATCGATCG, Reward: -1.2 (bad)
        → Policy learns: "Avoid starting with A"
        → Value learns: "AT... patterns predict low binding"

        Sequence: GGCGTACC, Reward: 1.0 (good)  
        → Policy learns: "GGC start is promising"
        → Value learns: "GGC... patterns predict high binding"

    Round 5 Update (more sophisticated):
        The policy now understands complex patterns:
        - "After GG, always choose C"
        - "Position 4 should be G when preceded by C"
        - "Avoid more than 2 consecutive identical bases"
    
    """
    def update_policy(self, sequences: List[List[int]], rewards: List[float], old_log_probs: List[float], epochs: int = 4):
        
        # Convert lists to tensors for gradient computation
        rewards_tensor = torch.tensor(rewards, dtype=torch.float32)
        old_log_probs_tensor = torch.tensor(old_log_probs, dtype=torch.float32)
        
        # Normalize rewards to stabilize training
        # help the network learn equally from good and bad examples
        rewards_tensor = (rewards_tensor - rewards_tensor.mean()) / (rewards_tensor.std() + 1e-8)
        
        # multiple training passes over the same data
        for _ in range(epochs):
            # Recompute probabilities with current policy parameters
            current_log_probs = []
            values = []
            
            # process each DNA sequence
            for seq in sequences:   # ***Each seq represents one sample of the trajectory eg. seq = [2,2,1,2,1,0,1,1] (GGCGTACC)
                log_prob = 0    # accumulate log probability of entire sequence
                seq_values = [] # value estimates at each position
                
                # Compute probability of generating this exact sequence
                # *** Each step in the trajectory
                for t in range(len(seq)):   # t = 0,1,2...7 for 8-base DNA
                    seq_tensor = torch.tensor([seq], dtype=torch.long)
                    pos_tensor = torch.tensor([t])
                    
                    # *** Get π_θ(a_t|s_t) from PolicyNetwork - get policy's current opinion
                    'Example at t=3 with seq[:3]=[2,2,1] (GGC): policy_probs might be [0.1, 0.15, 0.6, 0.15] for [A,T,G,C]'
                    policy_probs, value = self.policy_net(seq_tensor, pos_tensor)

                    # *** Compute log π_θ(a_t|s_t) for the actual action taken
                    # what's the probability of the actual choice made?
                    dist = Categorical(policy_probs[0])

                    # *** This log_prob represents log π_θ(trajectory) = Σ_t log π_θ(a_t|s_t) for this specific trajectory
                    'Example: seq[3]=2 (G), so log(0.6) = -0.51'
                    log_prob += dist.log_prob(torch.tensor(seq[t]))

                    # Value estimates how good this partial sequence is
                    seq_values.append(value.item())

                    # *** PPO loss uses these samples to approximate the policy gradient, which is the gradient of E[R(s_{1:T})|s_0, θ]
                
                # Total log probability of generating this exact DNA sequence
                'Example: log(P(GGCGTACC)) = sum of 8 log probabilities'
                current_log_probs.append(log_prob)

                # Average value across the sequence
                values.append(np.mean(seq_values))
            
            # Stack all sequences' probabilities and values
            current_log_probs = torch.stack(current_log_probs)
            values = torch.tensor(values, dtype=torch.float32)
            
            # Compute advantages
            # How much better was this sequence than expected?
            'Example: If GGCGTACC got reward 1.0 but value predicted 0.6, advantage = 0.4'
            advantages = rewards_tensor - values
            
            # PPO loss - limit how much the policy can change
            # ratio = P_new(sequence) / P_old(sequence)
            ratio = torch.exp(current_log_probs - old_log_probs_tensor)

            # Two surrogate objectives
            surr1 = ratio * advantages
            # Clipped version prevents ratio from going beyond boundries
            surr2 = torch.clamp(ratio, 1 - self.clip_ratio, 1 + self.clip_ratio) * advantages
            
            # Use the more conservative update
            policy_loss = -torch.min(surr1, surr2).mean()

            # train value network to better predict rewards
            value_loss = F.mse_loss(values, rewards_tensor)
            
            # Combined loss
            total_loss = policy_loss + 0.5 * value_loss
            
            # Backpropagation: update neural network weights
            self.optimizer.zero_grad()
            total_loss.backward()
            self.optimizer.step()


    """
    Fit surrogate models and return reliable ones
    ALG. 9: Fit candidate models f' ∈ S on ∪ᵢ₌₁ⁿ Dᵢ and compute score by cross-validation
    ALG. 10: Select subset of models S' ⊆ S with score ≥ τ

    ***
    Example: After testing 100+ sequences, build models that can predict binding affinity without going to the lab.
    
    Round 2 (64 sequences):
        Models attempted:
        - KNN (k=5): R2 = 0.65 - good "Sequences similar to GGCGTACC bind well"
        - Random Forest: R2 = 0.45 - not good (not enough data)
        - Neural Network: R2 = 0.20 - not good (needs more data)
        Reliable models: 1 (KNN only)

    Round 5 (160 sequences):
        Models attempted:
        - KNN (k=5): R2 = 0.68 - good 
        - Random Forest: R2 = 0.78 - good "GC at positions 3-5 is key"
        - Gradient Boost: R2 = 0.75 - good "Complex position interactions"
        - Neural Network: R2 = 0.52 - gppd  (finally working!)
        Reliable models: 4 (ensemble is powerful)
    """
    def fit_surrogate_models(self, sequences: List[List[int]], rewards: List[float]) -> List[SurrogateModel]:
        # Need minimum data for meaningful patterns
        if len(sequences) < 10:
            return []
        
        # self.surrogate_models = self.create_surrogate_models(len(sequences))

        # Convert sequences to features - 32-dimensional vector (8 positions × 4 bases)
        'DNA [2,2,1,2,1,0,1,1] → one-hot: [0,0,1,0, 0,0,1,0, 0,1,0,0, ...]'
        X = sequence_to_features(sequences, self.vocab_size)
        y = np.array(rewards)
        
        reliable_models = []
        
        # for each candiate model
        for model in self.surrogate_models:
            try:
                # computes r2 score using cross validation
                score = model.score(X, y)
                print(f"Model {model.model_type}: {score:.3f}")
                # if score >= threshold, fits the model and adds to reliable models list
                if score >= self.model_threshold:
                    model.fit(X, y)
                    reliable_models.append(model)
                    print(f"Model {model.model_type} is reliable with R2 score: {score:.3f}")

            except Exception as e:
                print(f"Error fitting model {model.model_type}: {e}")
                continue
        
        return reliable_models



    """
    Make predictions using ensemble of models
    ALG. 13: Compute f''(x) = 1/|S'| Σ f'∈S' f'(x)

    ***
    Instead of testing 1000 sequences in the lab, use our trained models to predict which ones will bind well.
    """
    def predict_with_ensemble(self, sequences: List[List[int]], models: List[SurrogateModel]) -> List[float]:
        # Convert sequences to same feature format used in training
        X = sequence_to_features(sequences, self.vocab_size)
        
        predictions = []

        # get prediction from all reliable models
        for model in models:
            pred = model.predict(X)
            predictions.append(pred)
        
        # Average predictions f''(x) = 1/|S'| Σ f'(x)
        ensemble_pred = np.mean(predictions, axis=0)    #*********** The original algorithm uses mean *********
        return ensemble_pred.tolist()
    

    """
    Execute one training round of DyNA PPO - corresponds to ALG. 6-17.
    Reinforcement Learning
    
    *** 
    The full expectation E[R(s_{1:T})|s_0, θ] is approximated in training

    One complete cycle of:
        1. Generate DNA sequences
        2. Test in lab (expensive)
        3. Learn from results
        4. Use models for virtual testing (cheap)
        5. Learn more from virtual results
    """
    def train_round(self, oracle_fn, round_num: int = 0) -> Dict:
        # *** This approximates the full expectation through Monte Carlo sampling

        # ========== PHASE 1: REAL LAB EXPERIMENTS ==========
        # ALG. 7: Collect samples D_n = {x, f(x)} using policy π_θ
        # Round 1: generate random batch of sequences - this samples multiple trajectories
        # *** Each trajectory represents one realization of the sum over s_t, a_t
        # Round 5: Generates sophisticated sequences
        sequences = self.generate_batch(self.batch_size)    # Multiple samples
        
        # Store current policy's probability of generating each sequence
        # Compute old log probabilities for PPO
        old_log_probs = []
        for seq in sequences:
            log_prob = 0

            # Calculate P(sequence|current policy)
            for t in range(len(seq)):
                seq_tensor = torch.tensor([seq], dtype=torch.long)
                pos_tensor = torch.tensor([t])
                
                with torch.no_grad():
                    # Get probability distribution at position t
                    policy_probs, _ = self.policy_net(seq_tensor, pos_tensor)
                    dist = Categorical(policy_probs[0])
                    # Add log probability of actual choice
                    log_prob += dist.log_prob(torch.tensor(seq[t]))
            
            old_log_probs.append(log_prob.item())
        
        # Send sequences to wet lab for testing
        # Evaluate with oracle - this gives us f(x) values
        # *** Compute rewards for each trajectory
        oracle_rewards = self.compute_rewards(sequences, oracle_fn)
        
        # Store data for cumulative dataset ∪ᵢ₌₁ⁿ Dᵢ
        for seq, reward in zip(sequences, oracle_rewards):
            self.all_data.append((seq, reward))
            self.sequence_history.append(seq)
        
        # ALG. 8: Train policy π_θ on D_n
        # Learn from this round's lab results
        # *** Update policy using these samples - this approximates the gradient of the expectation
        'GGCGTACC got 0.8 binding - reinforce this pattern!'
        'AAAATTTT got 0.1 binding - avoid poly-A stretches!'
        self.update_policy(sequences, oracle_rewards, old_log_probs)
        

        # ========== PHASE 2: VIRTUAL MODEL-BASED TRAINING - ALG. 9 - 16 ==========
        model_rewards = oracle_rewards.copy()   # Start with real rewards
        models_used = 0
        
        # Only attempt model-based training if we have enough data
        if len(self.all_data) > 20:  # Need sufficient data
            # Prepare all historical data
            all_sequences = [data[0] for data in self.all_data]
            all_rewards = [data[1] for data in self.all_data]
            
            # ALG. 9: Fit candidate models f' ∈ S on ∪ᵢ₌₁ⁿ Dᵢ and compute score by cross-validation
            # Try to build simulators that can predict binding without lab tests
            'Models learn patterns like GC-rich centers bind well'
            reliable_models = self.fit_surrogate_models(all_sequences, all_rewards)
            
            # Use models only if they're reliable
            # ALG. 10: Select subset of models S' ⊆ S with score ≥ τ
            # ALG. 11: if S' ≠ ∅ then
            if reliable_models:
                print(f"Round {round_num}: Using {len(reliable_models)} reliable models")
                models_used = len(reliable_models)
                
                # ALG. 12 - Multiple rounds of virtual training: for m = 1, 2, ...M do
                for m in range(self.max_model_rounds):
                    # ALG. 13: Generate virtual sequences and predict
                    # Sample batch of sequences x from π_θ and observe reward f''(x) = 1/|S'| Σ f'∈S' f'(x)
                    model_sequences = self.generate_batch(self.batch_size)
                    
                    # Use ensemble to predict binding, no lab needed
                    # Predict rewards with ensemble - this is f''(x)
                    predicted_rewards = self.predict_with_ensemble(model_sequences, reliable_models)
                    
                    # Apply diversity penalty to virtual sequences
                    final_rewards = []
                    for seq, pred_reward in zip(model_sequences, predicted_rewards):
                        # Penalize if too similar to previous sequences
                        diversity_penalty = compute_diversity_penalty(
                            seq, 
                            self.sequence_history, # All sequences ever generated
                            self.diversity_lambda, 
                            self.diversity_epsilon
                        )
                        'Example: GGCGTACC predicted 0.85, but we have 5 similar ones. Final reward: 0.85 - 0.05 = 0.80'
                        final_rewards.append(pred_reward - diversity_penalty)
                    
                    # Calculate policy probabilities for virtual sequences
                    # Compute old log probabilities for PPO
                    model_old_log_probs = []
                    for seq in model_sequences:
                        log_prob = 0
                        # Calculate P(sequence|current policy)
                        for t in range(len(seq)):
                            seq_tensor = torch.tensor([seq], dtype=torch.long)
                            pos_tensor = torch.tensor([t])
                            
                            with torch.no_grad():
                                # Get probability distribution at position t
                                policy_probs, _ = self.policy_net(seq_tensor, pos_tensor)
                                dist = Categorical(policy_probs[0])
                                # Add log probability of actual choice
                                log_prob += dist.log_prob(torch.tensor(seq[t]))
                        
                        model_old_log_probs.append(log_prob.item())
                    
                    # ALG. 14: Update policy with virtual data - Learn from model predictions without lab costs
                    # Update π_θ on {x, f''(x)}
                    self.update_policy(model_sequences, final_rewards, model_old_log_probs)
                    
                    # Track virtual sequences for diversity
                    self.sequence_history.extend(model_sequences)

                    # Collect all rewards for reporting
                    model_rewards.extend(final_rewards)

                # ALG. 15: end for - model rounds
            # ALG. 16: end if - reliable models exist
        
        # Return statistics
        return {
            'oracle_rewards': oracle_rewards,   # Real lab results
            'model_rewards': model_rewards,     # All rewards (real + virtual)
            'models_used': models_used,         # Number of reliable models
            'mean_oracle_reward': np.mean(oracle_rewards),  # Average binding this round
            'max_oracle_reward': np.max(oracle_rewards),    # Best binding this round
            'total_sequences': len(self.all_data)           # Cumulative sequences tested
        }


    