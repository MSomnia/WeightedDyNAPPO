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
import random
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel, Matern
from sklearn.ensemble import VotingRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

# File import
from SurrogateModel import SurrogateModel
from PolicyNetwork import PolicyNetwork
from SequenceUtils import compute_diversity_penalty, sequence_to_features, edit_distance, compute_sequence_diversity
from LearningRateTracker import LearningMetricsTracker

class DyNAPPO:
    
    def __init__(self, vocab_size: int, max_seq_len: int, batch_size: int = 64,
                 learning_rate: float = 3e-4, gamma: float = 0.99, clip_ratio: float = 0.2,
                 model_threshold: float = 0.5, max_model_rounds: int = 10,
                 diversity_lambda: float = 0.05, diversity_epsilon: int = 3):
        
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

        self.feature_scaler = StandardScaler()
        self.pca = None  # Will be initialized when enough data
        
        # Track model performance over time
        self.model_performance_history = {}


    """
    Create a pool of surrogate models with different complexities
    """
    def create_surrogate_models(self, data_size: int = 0) -> List[SurrogateModel]:
        
        models = []
        
        # Scale parameters based on data size
        base_estimators = max(100, min(500, data_size // 10))
        max_depth = max(10, min(20, data_size // 50))

        # Random Forest
        models.append(SurrogateModel('rf', n_estimators=100, max_depth=5))
        models.append(SurrogateModel('rf', n_estimators=300, max_depth=10))
        models.append(SurrogateModel('rf', n_estimators=500, max_depth=None))
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
        models.append(SurrogateModel('knn', n_neighbors=15))
        k_neighbors = max(5, min(50, int(np.sqrt(data_size))))
        models.append(SurrogateModel('knn', n_neighbors=k_neighbors))
        models.append(SurrogateModel('ridge'))
        models.append(SurrogateModel('xgb', n_estimators=200, max_depth=8, learning_rate=0.1))
        models.append(SurrogateModel('mlp', hidden_layer_sizes=(128, 64, 32), max_iter=500))
        models.append(SurrogateModel('svr', kernel='rbf', C=1.0, gamma='scale'))
        
        return models
    
    #******************************** NEW ****************************************
    def create_adaptive_surrogate_models(self, data_size: int) -> List[SurrogateModel]:
        """Create models appropriate for current data size"""
        models = []
        
        # Early rounds (< 50 samples): Simple models only
        if data_size < 50:
            models.append(SurrogateModel('knn', n_neighbors=min(3, data_size//3)))
            models.append(SurrogateModel('knn', n_neighbors=min(5, data_size//2)))
            models.append(SurrogateModel('ridge'))
            # Simple Random Forest with limited depth
            models.append(SurrogateModel('rf', n_estimators=50, max_depth=3, min_samples_split=5))
            
        # Medium data (50-150 samples): Add moderate complexity
        elif data_size < 150:
            # KNN with adaptive neighbors
            k_values = [3, 5, int(np.sqrt(data_size))]
            for k in k_values:
                models.append(SurrogateModel('knn', n_neighbors=k))
            
            # Random Forest with different complexities
            models.append(SurrogateModel('rf', n_estimators=50, max_depth=3))
            models.append(SurrogateModel('rf', n_estimators=100, max_depth=5))
            
            # Light gradient boosting
            models.append(SurrogateModel('gb', n_estimators=30, max_depth=3, learning_rate=0.1))
            
            # Ridge regression
            models.append(SurrogateModel('ridge'))
            
        # Sufficient data (>= 150 samples): Full model suite
        else:
            # Scaled parameters based on data size
            base_estimators = min(200, data_size // 2)
            max_depth = min(10, data_size // 20)
            
            # KNN variants
            for k in [5, 10, int(np.sqrt(data_size))]:
                models.append(SurrogateModel('knn', n_neighbors=k))
            
            # Random Forest variants
            models.append(SurrogateModel('rf', n_estimators=base_estimators, max_depth=max_depth))
            models.append(SurrogateModel('rf', n_estimators=base_estimators*2, max_depth=None))
            
            # Gradient Boosting
            models.append(SurrogateModel('gb', n_estimators=min(100, base_estimators), 
                                        max_depth=max_depth//2))
            
            # Add complex models only with enough data
            if data_size > 200:
                models.append(SurrogateModel('xgb', n_estimators=100, max_depth=5, learning_rate=0.1))
                models.append(SurrogateModel('mlp', hidden_layer_sizes=(64, 32), max_iter=300))
            
            models.append(SurrogateModel('ridge'))
            models.append(SurrogateModel('svr', kernel='rbf', C=1.0))
        
        return models
    #********************************************** END **********************************************

    #********************************************** NEW **********************************************
    """Create richer feature representations"""
    def create_enhanced_features(self, sequences: List[List[int]]) -> np.ndarray:
        features = []
        
        for seq in sequences:
            seq_features = []
            
            # 1. One-hot encoding (original)
            one_hot = np.zeros(len(seq) * self.vocab_size)
            for i, token in enumerate(seq):
                one_hot[i * self.vocab_size + token] = 1
            
            # 2. Position-independent features
            # Token frequency
            token_counts = np.zeros(self.vocab_size)
            for token in seq:
                token_counts[token] += 1
            token_freq = token_counts / len(seq)
            
            # 3. Bigram features (consecutive pairs)
            bigram_counts = np.zeros(self.vocab_size * self.vocab_size)
            for i in range(len(seq) - 1):
                bigram_idx = seq[i] * self.vocab_size + seq[i+1]
                bigram_counts[bigram_idx] += 1
            if len(seq) > 1:
                bigram_freq = bigram_counts / (len(seq) - 1)
            else:
                bigram_freq = bigram_counts
            
            # 4. Local complexity features
            window_size = min(4, len(seq))
            if window_size > 1:
                complexities = []
                for i in range(len(seq) - window_size + 1):
                    window = seq[i:i+window_size]
                    unique_tokens = len(set(window))
                    complexities.append(unique_tokens / window_size)
                
                complexity_mean = np.mean(complexities)
                complexity_std = np.std(complexities)
            else:
                complexity_mean = 1.0
                complexity_std = 0.0
            
            # 5. Run-length encoding features (repetition patterns)
            max_run_length = 0
            avg_run_length = 0
            if len(seq) > 0:
                run_lengths = []
                current_run = 1
                for i in range(1, len(seq)):
                    if seq[i] == seq[i-1]:
                        current_run += 1
                    else:
                        run_lengths.append(current_run)
                        current_run = 1
                run_lengths.append(current_run)
                max_run_length = max(run_lengths)
                avg_run_length = np.mean(run_lengths)
            
            # 6. GC content for DNA (tokens 2 and 3)
            gc_content = (seq.count(2) + seq.count(3)) / len(seq) if len(seq) > 0 else 0
            
            # Combine all features
            seq_features = np.concatenate([
                one_hot,
                token_freq,
                bigram_freq[:16],  # Limit bigram features to prevent explosion
                [complexity_mean, complexity_std],
                [max_run_length / len(seq), avg_run_length / len(seq)],
                [gc_content]
            ])
            
            features.append(seq_features)
        
        features = np.array(features)
        
        # Apply PCA if we have enough samples
        if len(features) > 50 and features.shape[0] > features.shape[1] // 2:
            if self.pca is None:
                # Initialize PCA to retain 95% variance
                n_components = min(features.shape[0] - 1, features.shape[1], 50)
                self.pca = PCA(n_components=n_components, random_state=42)
                features_reduced = self.pca.fit_transform(features)
            else:
                features_reduced = self.pca.transform(features)
            
            # Add back some original features that are important
            important_original = features[:, :self.vocab_size*2]  # First two positions
            features = np.hstack([features_reduced, important_original])
        
        return features
    #********************************************** END **********************************************

    
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
    def generate_sequence(self, deterministic: bool = False, epsilon: float = 0.0) -> List[int]:
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
                    # Epsilon-greedy exploration
                    if random.random() < epsilon:
                        action = random.randint(0, self.vocab_size - 1)
                    else:
                        # Sample from probability distribution (exploration)
                        'Example: might pick G (60% chance), but could pick C (15% chance)'
                        dist = Categorical(policy_probs[0])
                        action = dist.sample().item()   # Sample one a_t
                
                # Add chosen base to sequence
                'Example: sequence goes from [2,2,1] to [2,2,1,2] (GGC → GGCG)'
                sequence.append(action)
        
        return sequence
    
    #********************************************** NEW **********************************************
    """Generate sequence with temperature-controlled sampling"""
    def generate_sequence_with_temperature(self, temperature: float = 1.0) -> List[int]:
        sequence = []
        
        with torch.no_grad():
            for t in range(self.max_seq_len):
                seq_tensor = torch.tensor([sequence + [0] * (self.max_seq_len - len(sequence))], 
                                         dtype=torch.long)
                pos_tensor = torch.tensor([t])
                
                policy_probs, _ = self.policy_net(seq_tensor, pos_tensor)
                
                # Apply temperature
                if temperature != 1.0:
                    logits = torch.log(policy_probs[0] + 1e-10)
                    logits = logits / temperature
                    policy_probs = F.softmax(logits, dim=-1)
                    policy_probs = policy_probs.unsqueeze(0)
                
                dist = Categorical(policy_probs[0])
                action = dist.sample().item()
                sequence.append(action)
        
        return sequence
    
    """Generate batch with enforced diversity"""
    def generate_diverse_batch(self, batch_size: int, temperature: float = 1.0) -> List[List[int]]:
        sequences = []
        attempts = 0
        max_attempts = batch_size * 3
        
        while len(sequences) < batch_size and attempts < max_attempts:
            # Generate with temperature-controlled randomness
            seq = self.generate_sequence_with_temperature(temperature)
            
            # Check minimum diversity from existing sequences
            min_distance = float('inf')
            for existing_seq in sequences:
                dist = edit_distance(seq, existing_seq)
                min_distance = min(min_distance, dist)
            
            # Accept if sufficiently different or first sequence
            if len(sequences) == 0 or min_distance >= 2:
                sequences.append(seq)
            
            attempts += 1
        
        # Fill remaining with random if needed
        while len(sequences) < batch_size:
            seq = [random.randint(0, self.vocab_size - 1) for _ in range(self.max_seq_len)]
            sequences.append(seq)
        
        return sequences
    #********************************************** END **********************************************
    

    """
    Generate a batch of sequences.

    *** 
    Each sequence represents a different trajectory, helping approximate the sum over different states s_t in the expectation
    Sum over s_t: implemented by generating multiple sequences

    ***
    DNA Example: Generate 32 different DNA sequences for lab testing
    Each represents a different "trajectory" through sequence space
    """
    def generate_batch(self, batch_size: int, epsilon: float = 0.0) -> List[List[int]]:
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
        return [self.generate_sequence(epsilon = epsilon) for _ in range(batch_size)]
    

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
    def update_policy(self, sequences: List[List[int]], rewards: List[float], old_log_probs: List[float], epochs: int = 4, round_num: int = 0, metrics_tracker: Optional[LearningMetricsTracker] = None):
        
        # Convert lists to tensors for gradient computation
        rewards_tensor = torch.tensor(rewards, dtype=torch.float32)
        old_log_probs_tensor = torch.tensor(old_log_probs, dtype=torch.float32)
        
        # Normalize rewards to stabilize training
        # help the network learn equally from good and bad examples
        rewards_tensor = (rewards_tensor - rewards_tensor.mean()) / (rewards_tensor.std() + 1e-8)

        update_idx = 0
        
        # multiple training passes over the same data
        for epoch in range(epochs):
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
            
            # ====================== PPO =====================
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
            
            # Compute KL divergence
            kl_div = (old_log_probs_tensor - current_log_probs).mean().item()

            # Combined loss
            #total_loss = policy_loss + 0.5 * value_loss

            # **** L2 Regularization
            l2_lambda = 0.001
            l2_norm = sum(p.pow(2.0).sum() for p in self.policy_net.parameters())
            total_loss = policy_loss + 0.5 * value_loss + l2_lambda * l2_norm
            
            # Backpropagation: update neural network weights
            self.optimizer.zero_grad()
            total_loss.backward()

            # Compute gradient norm before clipping
            total_norm = 0
            for p in self.policy_net.parameters():
                if p.grad is not None:
                    param_norm = p.grad.data.norm(2)
                    total_norm += param_norm.item() ** 2
            total_norm = total_norm ** 0.5


            self.optimizer.step()

            # Log metrics if tracker provided
            if metrics_tracker:
                metrics_tracker.log_update_metrics(
                    round_num=round_num,
                    update_idx=update_idx,
                    policy_loss=policy_loss.item(),
                    value_loss=value_loss.item(),
                    total_loss=total_loss.item(),
                    gradient_norm=total_norm,
                    kl_divergence=kl_div
                )
            
            update_idx += 1


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
    def fit_surrogate_models(self, sequences: List[List[int]], rewards: List[float], round_num: int = 0) -> List[SurrogateModel]:

        # Need minimum data for meaningful patterns
        if len(sequences) < 10:
            return [], []
        
        # recreate the model pool in each round to adapt to the current data distribution:
        #self.surrogate_models = self.create_surrogate_models(len(sequences))

        # Convert sequences to features - 32-dimensional vector (8 positions × 4 bases)
        'DNA [2,2,1,2,1,0,1,1] → one-hot: [0,0,1,0, 0,0,1,0, 0,1,0,0, ...]'
        X = sequence_to_features(sequences, self.vocab_size)
        y = np.array(rewards)
        
        # **** Adaptive threshold based on round and data quality
        # Adaptive threshold based on round and data quality
        base_threshold = self.model_threshold

        # Determine threshold based on training round
        if round_num <= 2:
            # Early rounds: very lenient, accept any positive R²
            threshold = 0.0
            print(f"Round {round_num}: Using lenient threshold (R2 > 0.0)")
        elif round_num <= 5:
            # Middle rounds: moderately lenient
            threshold = base_threshold * 0.5
            print(f"Round {round_num}: Using moderate threshold (R2 > {threshold:.3f})")
        else:
            # Later rounds: use full threshold
            threshold = base_threshold
            print(f"Round {round_num}: Using full threshold (R2 > {threshold:.3f})")

        # Track all model scores for fallback selection
        model_scores = []
        reliable_models = []
        all_r2_scores = []  # Collect all R2 scores
        
        # for each candiate model
        for model in self.surrogate_models:
            try:
                # Compute R2 score using cross-validation
                score = model.score(X, y)
                all_r2_scores.append(score)  # Store the score
                model_scores.append((score, model))
                print(f"Model {model.model_type}: R2 = {score:.3f}")
                
                # Check if model meets adaptive threshold
                if score >= threshold:
                    model.fit(X, y)
                    reliable_models.append(model)
                    print(f"Model {model.model_type} selected (R2 = {score:.3f} >= {threshold:.3f})")
                    
            except Exception as e:
                print(f"Error fitting model {model.model_type}: {e}")
                continue
        
        # Fallback strategy if no models meet threshold
        if not reliable_models and model_scores:
            print("\nNo models met threshold. Using fallback selection...")
            
            # Sort models by score (best first)
            model_scores.sort(key=lambda x: x[0], reverse=True)
            
            # Strategy 1: Take top N models with positive scores
            n_fallback = min(3, len(model_scores))
            fallback_count = 0
            
            for score, model in model_scores:
                if score > 0 and fallback_count < n_fallback:
                    try:
                        model.fit(X, y)
                        reliable_models.append(model)
                        print(f"Fallback: Using {model.model_type} with R2 = {score:.3f}")
                        fallback_count += 1
                    except:
                        continue
            
            # Strategy 2: If still no models, take the single best one
            if not reliable_models and model_scores[0][0] > -0.5:
                best_score, best_model = model_scores[0]
                try:
                    best_model.fit(X, y)
                    reliable_models.append(best_model)
                    print(f"Last resort: Using best model {best_model.model_type} with R2 = {best_score:.3f}")
                except:
                    pass
        
        # Summary
        print(f"\nSelected {len(reliable_models)} reliable models for round {round_num}")
        if reliable_models:
            selected_types = [m.model_type for m in reliable_models]
            print(f"Model types: {', '.join(selected_types)}")
        
        return reliable_models, all_r2_scores


    #********************************************** NEW **********************************************
    """Improved surrogate model fitting with better strategies"""
    def fit_surrogate_models_improved(self, sequences: List[List[int]], rewards: List[float], 
                                     round_num: int = 0) -> Tuple[List[SurrogateModel], List[float]]:
        
        if len(sequences) < 10:
            print(f"Not enough data ({len(sequences)} samples) for surrogate models")
            return [], []
        
        # Create adaptive model pool based on data size
        surrogate_models = self.create_adaptive_surrogate_models(len(sequences))
        
        # Use enhanced features
        X = self.create_enhanced_features(sequences)
        y = np.array(rewards)
        
        # Normalize targets for better learning
        y_mean, y_std = y.mean(), y.std()
        if y_std > 0:
            y_normalized = (y - y_mean) / y_std
        else:
            y_normalized = y
        
        # Progressive threshold strategy
        if round_num <= 2:
            threshold = -0.5  # Accept any model that's better than random
            min_models = 1    # Need at least 1 model
        elif round_num <= 5:
            threshold = 0.0   # Accept any positive correlation
            min_models = 2
        else:
            threshold = min(0.3, self.model_threshold * (round_num / 10))
            min_models = 3
        
        print(f"\nRound {round_num}: Evaluating {len(surrogate_models)} models")
        print(f"Data size: {len(sequences)}, Feature dim: {X.shape[1]}")
        print(f"Threshold: R² > {threshold:.3f}, Min models: {min_models}")
        
        model_scores = []
        reliable_models = []
        all_r2_scores = []
        
        # Evaluate each model
        for model in surrogate_models:
            try:
                # Use normalized targets for scoring
                score = model.score(X, y_normalized)
                all_r2_scores.append(score)
                model_scores.append((score, model))
                
                # Track performance history
                model_key = f"{model.model_type}_{round_num}"
                self.model_performance_history[model_key] = score
                
                print(f"  {model.model_type}: R² = {score:.3f}")
                
                if score >= threshold:
                    # Fit on original scale targets
                    model.fit(X, y)
                    reliable_models.append(model)
                    
            except Exception as e:
                print(f"  Error with {model.model_type}: {e}")
                continue
        
        # Intelligent fallback strategy
        if len(reliable_models) < min_models and model_scores:
            print(f"\nOnly {len(reliable_models)} models met threshold. Using fallback...")
            
            # Sort by score
            model_scores.sort(key=lambda x: x[0], reverse=True)
            
            # Take best models up to min_models
            for score, model in model_scores:
                if len(reliable_models) >= min_models:
                    break
                if model not in reliable_models and score > -1.0:  # Not completely terrible
                    try:
                        model.fit(X, y)
                        reliable_models.append(model)
                        print(f"  Fallback added: {model.model_type} (R² = {score:.3f})")
                    except:
                        continue
        
        print(f"\nSelected {len(reliable_models)} models for ensemble")
        if reliable_models:
            selected_types = [m.model_type for m in reliable_models]
            selected_scores = [s for s, m in model_scores if m in reliable_models]
            print(f"Models: {selected_types}")
            print(f"Scores: {[f'{s:.3f}' for s in selected_scores]}")
        
        return reliable_models, all_r2_scores
    #********************************************** END **********************************************



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
    
    #********************************************** NEW **********************************************
    def predict_with_average_ensemble(self, sequences: List[List[int]], 
                                  models: List[SurrogateModel], 
                                  model_scores: Optional[List[float]] = None) -> List[float]:
        """Simple ensemble prediction using mean of all models"""
        
        X = self.create_enhanced_features(sequences)
        predictions = []
        
        # Get predictions from each model
        for model in models:
            try:
                pred = model.predict(X)
                predictions.append(pred)
            except:
                # Skip failed models instead of adding zeros
                continue
        
        # If no models succeeded, return zeros
        if not predictions:
            return [0.0] * len(sequences)
        
        # Simple mean of all predictions
        ensemble_pred = np.mean(predictions, axis=0)
        return ensemble_pred.tolist()
    
    
    def predict_with_weighted_ensemble(self, sequences: List[List[int]], 
                                      models: List[SurrogateModel], 
                                      model_scores: Optional[List[float]] = None) -> List[float]:
        """Weighted ensemble prediction based on model performance"""
        
        X = self.create_enhanced_features(sequences)
        predictions = []
        weights = []
        
        # Calculate weights based on R² scores if available
        if model_scores:
            # Convert R² scores to weights (only positive contributions)
            weights = [max(0, score) for score in model_scores]
            weight_sum = sum(weights)
            if weight_sum > 0:
                weights = [w / weight_sum for w in weights]
            else:
                weights = [1.0 / len(models)] * len(models)
        else:
            weights = [1.0 / len(models)] * len(models)
        
        # Get weighted predictions
        for model, weight in zip(models, weights):
            try:
                pred = model.predict(X)
                predictions.append(pred * weight)
            except:
                predictions.append(np.zeros(len(sequences)))
        
        # Weighted average
        ensemble_pred = np.sum(predictions, axis=0)
        return ensemble_pred.tolist()
    #********************************************** END **********************************************

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
    def train_round_old(self, oracle_fn, metrics_tracker: LearningMetricsTracker, round_num: int = 0, exploration_rate: float = 0) -> Dict:
        # *** This approximates the full expectation through Monte Carlo sampling
        # ========== PHASE 1: REAL LAB EXPERIMENTS ==========
        # ALG. 7: Collect samples D_n = {x, f(x)} using policy π_θ
        # Round 1: generate random batch of sequences - this samples multiple trajectories
        # *** Each trajectory represents one realization of the sum over s_t, a_t
        # Round 5: Generates sophisticated sequences
        #sequences = self.generate_batch(self.batch_size)    # Multiple samples
        sequences = self.generate_batch(self.batch_size, epsilon=exploration_rate)

        # Compute diversity
        diversity = compute_sequence_diversity(sequences)

        # Quick sequence preview
        print(f"\n--- Round {round_num} Generated Sequences ---:\n", end="")
        dna_map = {0: 'A', 1: 'T', 2: 'G', 3: 'C'}
        for i in range(min(20, len(sequences))):
            dna_str = ''.join([dna_map[b] for b in sequences[i]])
            print(f"{dna_str} ", end="")
        print(f"... ({len(sequences)} total)")
        
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
        
        # **** Highly encourage diversity
        for reward in oracle_rewards:
            reward = reward + diversity * 2
        
        # Store data for cumulative dataset ∪ᵢ₌₁ⁿ Dᵢ
        for seq, reward in zip(sequences, oracle_rewards):
            self.all_data.append((seq, reward))
            self.sequence_history.append(seq)
        
        # ALG. 8: Train policy π_θ on D_n
        # Learn from this round's lab results
        # *** Update policy using these samples - this approximates the gradient of the expectation
        'GGCGTACC got 0.8 binding - reinforce this pattern'
        'AAAATTTT got 0.1 binding - avoid poly-A stretches'
        self.update_policy(sequences, oracle_rewards, old_log_probs, epochs = 4, round_num=round_num, metrics_tracker=metrics_tracker)
        

        # ========== PHASE 2: VIRTUAL MODEL-BASED TRAINING - ALG. 9 - 16 ==========
        model_rewards = oracle_rewards.copy()   # Start with real rewards
        models_used = 0
        model_r2_scores = []
        
        # Only attempt model-based training if we have enough data
        if len(self.all_data) > 20:  # Need sufficient data
            # Prepare all historical data
            all_sequences = [data[0] for data in self.all_data]
            all_rewards = [data[1] for data in self.all_data]
            
            # ALG. 9: Fit candidate models f' ∈ S on ∪ᵢ₌₁ⁿ Dᵢ and compute score by cross-validation
            # Try to build simulators that can predict binding without lab tests
            'Models learn patterns like GC-rich centers bind well'
            #reliable_models = self.fit_surrogate_models(all_sequences, all_rewards)
            reliable_models, all_r2_scores = self.fit_surrogate_models(all_sequences, all_rewards, round_num)
            model_r2_scores = all_r2_scores  # Store for metrics
            
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
                    # final_rewards = []
                    # for seq, pred_reward in zip(model_sequences, predicted_rewards):
                    #     # Penalize if too similar to previous sequences
                    #     diversity_penalty = compute_diversity_penalty(
                    #         seq, 
                    #         self.sequence_history, # All sequences ever generated
                    #         self.diversity_lambda, 
                    #         self.diversity_epsilon
                    #     )
                    #     'Example: GGCGTACC predicted 0.85, but we have 5 similar ones. Final reward: 0.85 - 0.05 = 0.80'
                    #     final_rewards.append(pred_reward - diversity_penalty)
                    
                    # ****** gradually reduce diversity penalty
                    diversity_weight = max(0, 1 - m / self.max_model_rounds)  # Linear decay
                    final_rewards = []
                    for seq, pred_reward in zip(model_sequences, predicted_rewards):
                        diversity_penalty = compute_diversity_penalty(
                            seq, 
                            self.sequence_history,
                            self.diversity_lambda * diversity_weight,
                            self.diversity_epsilon
                        )
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
                    self.update_policy(model_sequences, final_rewards, model_old_log_probs, epochs = 2, round_num=round_num, metrics_tracker=metrics_tracker)
                    
                    # Track virtual sequences for diversity
                    self.sequence_history.extend(model_sequences)

                    # Collect all rewards for reporting
                    model_rewards.extend(final_rewards)

                    # print(model_sequences)

                # ALG. 15: end for - model rounds
            # ALG. 16: end if - reliable models exist
        
        # Collect oracle rewards statistics
        oracle_rewards = self.compute_rewards(sequences, oracle_fn)

        # Return statistics
        return {
            'oracle_rewards': oracle_rewards,   # Real lab results
            'model_rewards': model_rewards,     # All rewards (real + virtual)
            'models_used': models_used,         # Number of reliable models
            'mean_oracle_reward': np.mean(oracle_rewards),  # Average binding this round
            'min_oracle_reward': np.min(oracle_rewards),
            'max_oracle_reward': np.max(oracle_rewards),    # Best binding this round
            'std_oracle_reward': np.std(oracle_rewards),
            'sequence_diversity': diversity,
            'model_r2_scores': model_r2_scores,
            'total_sequences': len(self.all_data)           # Cumulative sequences tested
        }
    

    #********************************************** NEW **********************************************
    def train_roundv2(self, oracle_fn, metrics_tracker: LearningMetricsTracker, 
                round_num: int = 0, exploration_rate: float = 0) -> Dict:
        """
        Improved training round with better surrogate model learning
        """
        
        # ========== PHASE 1: ADAPTIVE SEQUENCE GENERATION ==========
        # Use temperature-based sampling for better exploration
        if round_num <= 3:
            temperature = 1.5  # High temperature for exploration
            use_diverse_generation = True
        elif round_num <= 7:
            temperature = 1.2
            use_diverse_generation = True
        else:
            temperature = 1.0
            use_diverse_generation = False
        
        # Generate sequences with adaptive strategy
        if use_diverse_generation:
            # Use diverse batch generation in early rounds
            sequences = self.generate_diverse_batch(self.batch_size, temperature)
        else:
            # Mix exploration and exploitation
            sequences = []
            for _ in range(self.batch_size):
                if random.random() < exploration_rate:
                    # Pure random exploration
                    seq = [random.randint(0, self.vocab_size - 1) for _ in range(self.max_seq_len)]
                else:
                    # Temperature-controlled policy sampling
                    seq = self.generate_sequence_with_temperature(temperature)
                sequences.append(seq)
        
        # Compute diversity metrics
        diversity = compute_sequence_diversity(sequences)
        
        # Quick sequence preview
        print(f"\n--- Round {round_num} Generated Sequences ---")
        print(f"Temperature: {temperature:.2f}, Diversity: {diversity:.3f}")
        dna_map = {0: 'A', 1: 'T', 2: 'G', 3: 'C'}
        for i in range(min(10, len(sequences))):
            dna_str = ''.join([dna_map[b] for b in sequences[i]])
            print(f"{dna_str} ", end="")
        print(f"... ({len(sequences)} total)")
        
        # ========== PHASE 2: COMPUTE OLD LOG PROBABILITIES ==========
        old_log_probs = []
        for seq in sequences:
            log_prob = 0
            for t in range(len(seq)):
                seq_tensor = torch.tensor([seq], dtype=torch.long)
                pos_tensor = torch.tensor([t])
                
                with torch.no_grad():
                    policy_probs, _ = self.policy_net(seq_tensor, pos_tensor)
                    dist = Categorical(policy_probs[0])
                    log_prob += dist.log_prob(torch.tensor(seq[t]))
            
            old_log_probs.append(log_prob.item())
        
        # ========== PHASE 3: ORACLE EVALUATION ==========
        oracle_rewards = self.compute_rewards(sequences, oracle_fn, use_diversity=True)
        
        # Boost diversity in early rounds
        if round_num <= 5:
            diversity_boost = diversity * 2.0
            oracle_rewards = [r + diversity_boost for r in oracle_rewards]
        
        # Store data with enhanced tracking
        for seq, reward in zip(sequences, oracle_rewards):
            self.all_data.append((seq, reward))
            self.sequence_history.append(seq)
        
        # ========== PHASE 4: UPDATE POLICY WITH REAL DATA ==========
        # More epochs in early rounds when data is limited
        update_epochs = 6 if round_num <= 3 else 4
        
        self.update_policy(sequences, oracle_rewards, old_log_probs, 
                        epochs=update_epochs, round_num=round_num, 
                        metrics_tracker=metrics_tracker)
        
        # ========== PHASE 5: IMPROVED SURROGATE MODEL TRAINING ==========
        model_rewards = oracle_rewards.copy()
        models_used = 0
        model_r2_scores = []
        reliable_models = []
        
        # Only attempt model-based training if we have sufficient diverse data
        min_data_for_models = 30 if round_num <= 3 else 20
        
        if len(self.all_data) >= min_data_for_models:
            # Prepare all historical data
            all_sequences = [data[0] for data in self.all_data]
            all_rewards = [data[1] for data in self.all_data]
            
            print(f"\n=== Surrogate Model Training (Round {round_num}) ===")
            print(f"Total training samples: {len(all_sequences)}")
            
            # Use improved model fitting
            reliable_models, all_r2_scores = self.fit_surrogate_models_improved(
                all_sequences, all_rewards, round_num
            )
            model_r2_scores = all_r2_scores
            
            # ========== PHASE 6: MODEL-BASED TRAINING ==========
            if reliable_models:
                models_used = len(reliable_models)
                
                # Extract model scores for weighted ensemble
                model_scores = []
                for model in reliable_models:
                    # Find the score for this model from all_r2_scores
                    # (In practice, you'd track this mapping in fit_surrogate_models_improved)
                    model_scores.append(max(0, np.mean(all_r2_scores)))  # Simplified
                
                # Adaptive number of model rounds based on model quality
                if np.max(all_r2_scores) > 0.5:
                    adaptive_model_rounds = self.max_model_rounds
                elif np.max(all_r2_scores) > 0.2:
                    adaptive_model_rounds = max(2, self.max_model_rounds // 2)
                else:
                    adaptive_model_rounds = 2  # Minimal virtual training with poor models
                
                print(f"\nModel-based training: {adaptive_model_rounds} rounds with {models_used} models")
                print(f"Best model R²: {np.max(all_r2_scores):.3f}")
                
                for m in range(adaptive_model_rounds):
                    # Generate virtual sequences with controlled diversity
                    if m == 0:
                        # First round: explore around current policy
                        virtual_temp = max(1.0, temperature - 0.2)
                    else:
                        # Later rounds: more exploitation
                        virtual_temp = max(0.8, temperature - 0.4)
                    
                    # Use diverse generation for virtual sequences too
                    if round_num <= 5:
                        model_sequences = self.generate_diverse_batch(
                            self.batch_size, virtual_temp
                        )
                    else:
                        model_sequences = []
                        for _ in range(self.batch_size):
                            seq = self.generate_sequence_with_temperature(virtual_temp)
                            model_sequences.append(seq)
                    
                    # Use weighted ensemble prediction
                    # predicted_rewards = self.predict_with_weighted_ensemble(
                    #     model_sequences, reliable_models, model_scores
                    # )

                    predicted_rewards = self.predict_with_average_ensemble(
                        model_sequences, reliable_models, model_scores
                    )
                    
                    # Apply diversity penalty with decay
                    diversity_weight = max(0.2, 1 - m / adaptive_model_rounds)
                    final_rewards = []
                    
                    for seq, pred_reward in zip(model_sequences, predicted_rewards):
                        # Only apply diversity penalty if we have good models
                        if np.max(all_r2_scores) > 0.3:
                            diversity_penalty = compute_diversity_penalty(
                                seq, 
                                self.sequence_history,
                                self.diversity_lambda * diversity_weight,
                                self.diversity_epsilon
                            )
                            final_rewards.append(pred_reward - diversity_penalty)
                        else:
                            # With poor models, don't apply diversity penalty
                            final_rewards.append(pred_reward)
                    
                    # Compute old log probabilities for virtual sequences
                    model_old_log_probs = []
                    for seq in model_sequences:
                        log_prob = 0
                        for t in range(len(seq)):
                            seq_tensor = torch.tensor([seq], dtype=torch.long)
                            pos_tensor = torch.tensor([t])
                            
                            with torch.no_grad():
                                policy_probs, _ = self.policy_net(seq_tensor, pos_tensor)
                                dist = Categorical(policy_probs[0])
                                log_prob += dist.log_prob(torch.tensor(seq[t]))
                        
                        model_old_log_probs.append(log_prob.item())
                    
                    # Update with virtual data (fewer epochs to prevent overfitting)
                    virtual_epochs = 2 if np.max(all_r2_scores) > 0.3 else 1
                    
                    self.update_policy(model_sequences, final_rewards, model_old_log_probs, 
                                    epochs=virtual_epochs, round_num=round_num, 
                                    metrics_tracker=metrics_tracker)
                    
                    # Track virtual sequences for diversity
                    self.sequence_history.extend(model_sequences)
                    model_rewards.extend(final_rewards)
                    
                    if m % 2 == 0:  # Print every other round
                        print(f"  Virtual round {m+1}/{adaptive_model_rounds}: "
                            f"Mean predicted reward = {np.mean(final_rewards):.3f}")
            
            else:
                print(f"\nNo reliable models found (best R² = {np.max(all_r2_scores):.3f})")
                print("Skipping model-based training this round")
        
        else:
            print(f"\nInsufficient data for surrogate models ({len(self.all_data)} < {min_data_for_models})")
        
        # ========== PHASE 7: COMPUTE FINAL STATISTICS ==========
        # Re-evaluate oracle rewards without diversity boost for accurate reporting
        oracle_rewards_clean = [oracle_fn(seq) for seq in sequences]
        
        # Return comprehensive statistics
        return {
            'oracle_rewards': oracle_rewards_clean,
            'model_rewards': model_rewards,
            'models_used': models_used,
            'mean_oracle_reward': np.mean(oracle_rewards_clean),
            'min_oracle_reward': np.min(oracle_rewards_clean),
            'max_oracle_reward': np.max(oracle_rewards_clean),
            'std_oracle_reward': np.std(oracle_rewards_clean),
            'sequence_diversity': diversity,
            'model_r2_scores': model_r2_scores,
            'total_sequences': len(self.all_data),
            'temperature': temperature,
            'best_model_r2': np.max(model_r2_scores) if model_r2_scores else 0,
            'mean_model_r2': np.mean(model_r2_scores) if model_r2_scores else 0,
            'reliable_models': [m.model_type for m in reliable_models] if reliable_models else []
        }
    #********************************************** END **********************************************



    def train_round(self, oracle_fn, metrics_tracker: LearningMetricsTracker, 
                round_num: int = 0, exploration_rate: float = 0) -> Dict:
        """
        Comprehensive improved training round integrating all enhancements
        """
        
        # ========== PHASE 1: ANALYZE PROGRESS & ADAPT PARAMETERS ==========
        # Track performance trend for adaptive learning
        performance_trend = []
        if hasattr(self, 'round_rewards_history'):
            performance_trend = self.round_rewards_history[-5:]
        else:
            self.round_rewards_history = []
        
        # Update learning rate based on performance
        current_lr = self.update_learning_rate(round_num, performance_trend)
        
        # Set entropy coefficient for exploration
        if round_num <= 3:
            entropy_coef = 0.02  # High exploration early
        elif round_num <= 7:
            entropy_coef = 0.01
        else:
            entropy_coef = 0.005  # Low exploration late
        
        print(f"\n--- Round {round_num} Configuration ---")
        print(f"Learning rate: {current_lr:.6f}")
        print(f"Entropy coefficient: {entropy_coef:.4f}")
        print(f"Exploration rate: {exploration_rate:.3f}")
        
        # ========== PHASE 2: GUIDED SEQUENCE GENERATION ==========
        # Use guided generation that learns from best sequences
        if round_num <= 2:
            # Early rounds: more random exploration
            sequences = []
            for _ in range(self.batch_size):
                if random.random() < 0.5:
                    # Random sequence
                    seq = [random.randint(0, self.vocab_size - 1) 
                        for _ in range(self.max_seq_len)]
                else:
                    # Temperature-based generation
                    seq = self.generate_sequence_with_temperature(
                        temperature=1.5, use_top_k=False
                    )
                sequences.append(seq)
        else:
            # Later rounds: use guided generation
            sequences = self.guided_sequence_generation(self.batch_size, round_num)
        
        # Compute diversity metrics
        diversity = compute_sequence_diversity(sequences)
        
        # Display sample sequences
        print(f"\n--- Generated Sequences (Diversity: {diversity:.3f}) ---")
        dna_map = {0: 'A', 1: 'T', 2: 'G', 3: 'C'}
        for i in range(min(5, len(sequences))):
            dna_str = ''.join([dna_map[b] for b in sequences[i]])
            print(f"  {dna_str}")
        print(f"  ... ({len(sequences)} total)")
        
        # ========== PHASE 3: COMPUTE OLD LOG PROBABILITIES ==========
        old_log_probs = []
        with torch.no_grad():
            for seq in sequences:
                log_prob = 0
                for t in range(len(seq)):
                    seq_tensor = torch.tensor([seq], dtype=torch.long)
                    pos_tensor = torch.tensor([t])
                    
                    policy_probs, _ = self.policy_net(seq_tensor, pos_tensor)
                    dist = Categorical(policy_probs[0])
                    log_prob += dist.log_prob(torch.tensor(seq[t]))
                
                old_log_probs.append(log_prob.item())
        
        # ========== PHASE 4: ORACLE EVALUATION WITH INTRINSIC REWARDS ==========
        oracle_rewards = []
        for seq in sequences:
            # Get oracle reward
            base_reward = oracle_fn(seq)
            
            # Add intrinsic reward for exploration
            intrinsic_reward = self.compute_intrinsic_reward(seq, round_num)
            
            # Combine rewards
            total_reward = base_reward + intrinsic_reward
            oracle_rewards.append(total_reward)
        
        # Store data
        for seq, reward in zip(sequences, oracle_rewards):
            # Store original oracle reward without intrinsic bonus
            original_reward = oracle_fn(seq)
            self.all_data.append((seq, original_reward))
            self.sequence_history.append(seq)
        
        # Track round performance
        mean_reward = np.mean([oracle_fn(seq) for seq in sequences])
        self.round_rewards_history.append(mean_reward)
        
        print(f"\nOracle Evaluation:")
        print(f"  Mean reward: {mean_reward:.3f}")
        print(f"  Max reward: {np.max([oracle_fn(seq) for seq in sequences]):.3f}")
        print(f"  With intrinsic bonuses: {np.mean(oracle_rewards):.3f}")
        
        # ========== PHASE 5: ADAPTIVE POLICY UPDATE ==========
        print(f"\nPolicy Update:")
        
        # Determine number of epochs based on round and data quality
        if round_num <= 3:
            update_epochs = 8
        elif round_num <= 7:
            update_epochs = 4
        else:
            update_epochs = 2
        
        # Use adaptive policy update with entropy regularization
        self.adaptive_policy_update(
            sequences, 
            oracle_rewards, 
            old_log_probs,
            epochs=update_epochs,
            round_num=round_num,
            metrics_tracker=metrics_tracker,
            entropy_coef=entropy_coef
        )
        
        # ========== PHASE 6: IMPROVED SURROGATE MODEL TRAINING ==========
        model_rewards = oracle_rewards.copy()
        models_used = 0
        model_r2_scores = []
        reliable_models = []
        
        # Minimum data requirements
        min_data_for_models = 30
        
        if len(self.all_data) >= min_data_for_models:
            print(f"\n=== Surrogate Model Training ===")
            print(f"Total samples: {len(self.all_data)}")
            
            # Prepare all historical data
            all_sequences = [data[0] for data in self.all_data]
            all_rewards = [data[1] for data in self.all_data]
            
            # Use improved model fitting with oracle-aligned features
            reliable_models, model_r2_scores = self.improved_fit_surrogate_models(
                all_sequences, all_rewards, round_num
            )
            
            models_used = len(reliable_models)
            
            # ========== PHASE 7: MODEL-BASED TRAINING ==========
            if reliable_models:
                # Determine quality of models
                if model_r2_scores:
                    best_r2 = np.max(model_r2_scores)
                    mean_r2 = np.mean([s for s in model_r2_scores if s > -999])
                else:
                    best_r2 = -1
                    mean_r2 = -1
                
                print(f"\nModel-based training with {models_used} models")
                print(f"Best R²: {best_r2:.3f}, Mean R²: {mean_r2:.3f}")
                
                # Adaptive number of virtual rounds based on model quality
                if best_r2 > 0.3:
                    virtual_rounds = min(self.max_model_rounds, 5)
                elif best_r2 > 0:
                    virtual_rounds = min(self.max_model_rounds, 3)
                elif best_r2 > -0.3:
                    virtual_rounds = 2
                else:
                    virtual_rounds = 1  # Minimal virtual training with poor models
                
                print(f"Running {virtual_rounds} virtual training rounds")
                
                for m in range(virtual_rounds):
                    # Generate virtual sequences with appropriate strategy
                    if best_r2 > 0:
                        # Models are decent - use guided generation
                        virtual_sequences = self.guided_sequence_generation(
                            self.batch_size, round_num
                        )
                    else:
                        # Models are poor - use more exploration
                        virtual_sequences = []
                        for _ in range(self.batch_size):
                            temp = 1.3 - (m * 0.1)  # Decrease temperature each round
                            seq = self.generate_sequence_with_temperature(
                                temperature=temp, use_top_k=True, k=3
                            )
                            virtual_sequences.append(seq)
                    
                    # Predict rewards using improved ensemble
                    predicted_rewards = self.predict_with_improved_ensemble(
                        virtual_sequences, reliable_models, round_num
                    )
                    
                    # Only apply diversity penalty if models are good
                    if best_r2 > 0:
                        diversity_weight = max(0.2, 1 - m / virtual_rounds)
                        final_rewards = []
                        for seq, pred_reward in zip(virtual_sequences, predicted_rewards):
                            diversity_penalty = compute_diversity_penalty(
                                seq, 
                                self.sequence_history,
                                self.diversity_lambda * diversity_weight,
                                self.diversity_epsilon
                            )
                            final_rewards.append(pred_reward - diversity_penalty)
                    else:
                        # Poor models - use predictions as-is
                        final_rewards = predicted_rewards
                    
                    # Skip update if predictions are all zeros or invalid
                    if all(r == 0 for r in final_rewards) or np.std(final_rewards) < 1e-6:
                        print(f"  Round {m+1}: Skipping update (invalid predictions)")
                        continue
                    
                    # Compute old log probabilities for virtual sequences
                    virtual_old_log_probs = []
                    with torch.no_grad():
                        for seq in virtual_sequences:
                            log_prob = 0
                            for t in range(len(seq)):
                                seq_tensor = torch.tensor([seq], dtype=torch.long)
                                pos_tensor = torch.tensor([t])
                                
                                policy_probs, _ = self.policy_net(seq_tensor, pos_tensor)
                                dist = Categorical(policy_probs[0])
                                log_prob += dist.log_prob(torch.tensor(seq[t]))
                            
                            virtual_old_log_probs.append(log_prob.item())
                    
                    # Update with virtual data (fewer epochs, less entropy)
                    virtual_epochs = 2 if best_r2 > 0 else 1
                    virtual_entropy = entropy_coef * 0.5  # Less exploration with virtual data
                    
                    self.adaptive_policy_update(
                        virtual_sequences, 
                        final_rewards, 
                        virtual_old_log_probs,
                        epochs=virtual_epochs,
                        round_num=round_num,
                        metrics_tracker=metrics_tracker,
                        entropy_coef=virtual_entropy
                    )
                    
                    # Track virtual sequences
                    self.sequence_history.extend(virtual_sequences)
                    model_rewards.extend(final_rewards)
                    
                    print(f"  Round {m+1}/{virtual_rounds}: "
                        f"Mean predicted reward = {np.mean(final_rewards):.3f}")
            
            else:
                print(f"\nNo reliable models found. Skipping model-based training.")
        
        else:
            print(f"\nInsufficient data ({len(self.all_data)} < {min_data_for_models}). "
                f"Skipping surrogate models.")
        
        # ========== PHASE 8: ANALYZE PROGRESS ==========
        # Re-evaluate with oracle for accurate statistics
        oracle_rewards_clean = [oracle_fn(seq) for seq in sequences]
        
        results = {
            'oracle_rewards': oracle_rewards_clean,
            'model_rewards': model_rewards,
            'models_used': models_used,
            'mean_oracle_reward': np.mean(oracle_rewards_clean),
            'min_oracle_reward': np.min(oracle_rewards_clean),
            'max_oracle_reward': np.max(oracle_rewards_clean),
            'std_oracle_reward': np.std(oracle_rewards_clean),
            'sequence_diversity': diversity,
            'model_r2_scores': model_r2_scores,
            'total_sequences': len(self.all_data),
            'best_model_r2': np.max(model_r2_scores) if model_r2_scores else -999,
            'mean_model_r2': np.mean([s for s in model_r2_scores if s > -999]) if model_r2_scores else -999
        }
        
        # Analyze and provide recommendations
        analysis = self.analyze_and_report_progress(round_num, results)
        
        return results





    def adaptive_policy_update(self, sequences: List[List[int]], rewards: List[float], 
                          old_log_probs: List[float], epochs: int = 4, 
                          round_num: int = 0, 
                          metrics_tracker: Optional['LearningMetricsTracker'] = None,
                          entropy_coef: float = 0.01):
        """
        Adaptive policy update with entropy regularization and dynamic hyperparameters
        """
        # Convert to tensors
        rewards_tensor = torch.tensor(rewards, dtype=torch.float32)
        old_log_probs_tensor = torch.tensor(old_log_probs, dtype=torch.float32)
        
        # Analyze reward distribution for adaptive normalization
        reward_mean = rewards_tensor.mean()
        reward_std = rewards_tensor.std()
        
        # Adaptive reward normalization based on distribution
        if reward_std > 1e-8:
            if reward_std > 3.0:  # High variance - use robust normalization
                # Use median and MAD for robustness
                reward_median = torch.median(rewards_tensor)
                mad = torch.median(torch.abs(rewards_tensor - reward_median))
                rewards_normalized = (rewards_tensor - reward_median) / (mad + 1e-8)
            else:
                # Standard normalization
                rewards_normalized = (rewards_tensor - reward_mean) / (reward_std + 1e-8)
        else:
            rewards_normalized = rewards_tensor
        
        # Adaptive clipping based on training progress and reward variance
        if round_num <= 3:
            clip_ratio = 0.3  # More exploration early
        elif reward_std > 2.0:
            clip_ratio = 0.1  # Conservative with high variance
        else:
            clip_ratio = 0.2  # Standard clipping
        
        print(f"  Adaptive update: clip_ratio={clip_ratio:.2f}, entropy_coef={entropy_coef:.3f}")
        
        update_idx = 0
        best_policy_loss = float('inf')
        
        for epoch in range(epochs):
            # Recompute probabilities with current policy
            current_log_probs = []
            values = []
            entropies = []
            
            for seq in sequences:
                log_prob = 0
                seq_values = []
                seq_entropy = 0
                
                for t in range(len(seq)):
                    seq_tensor = torch.tensor([seq], dtype=torch.long)
                    pos_tensor = torch.tensor([t])
                    
                    policy_probs, value = self.policy_net(seq_tensor, pos_tensor)
                    
                    # Calculate log probability and entropy
                    dist = Categorical(policy_probs[0])
                    action_log_prob = dist.log_prob(torch.tensor(seq[t]))
                    log_prob += action_log_prob
                    
                    # Entropy for exploration bonus
                    seq_entropy += dist.entropy()
                    
                    seq_values.append(value.item())
                
                current_log_probs.append(log_prob)
                values.append(np.mean(seq_values))
                entropies.append(seq_entropy / len(seq))  # Average entropy per position
            
            # Stack tensors
            current_log_probs = torch.stack(current_log_probs)
            values = torch.tensor(values, dtype=torch.float32)
            entropies = torch.stack(entropies)
            
            # Compute advantages with baseline
            advantages = rewards_normalized - values
            
            # Normalize advantages for stability
            if advantages.std() > 1e-8:
                advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)
            
            # PPO objective with adaptive clipping
            ratio = torch.exp(current_log_probs - old_log_probs_tensor)
            
            # Compute both surrogate objectives
            surr1 = ratio * advantages
            surr2 = torch.clamp(ratio, 1 - clip_ratio, 1 + clip_ratio) * advantages
            
            # Policy loss with entropy bonus
            policy_loss = -torch.min(surr1, surr2).mean()
            entropy_loss = -entropies.mean()  # Negative because we want to maximize entropy
            
            # Value function loss with clipping
            value_loss = F.mse_loss(values, rewards_normalized)
            
            # Adaptive loss weighting
            if round_num <= 5:
                # Early training: emphasize exploration
                total_loss = policy_loss + 0.5 * value_loss + entropy_coef * entropy_loss
            else:
                # Later training: focus on exploitation
                total_loss = policy_loss + 0.5 * value_loss + (entropy_coef * 0.5) * entropy_loss
            
            # Add small L2 regularization
            l2_lambda = 0.0001
            l2_norm = sum(p.pow(2.0).sum() for p in self.policy_net.parameters())
            total_loss = total_loss + l2_lambda * l2_norm
            
            # Compute KL divergence for monitoring
            kl_div = (old_log_probs_tensor - current_log_probs).mean().item()
            
            # Early stopping if KL divergence too large
            if kl_div > 0.05 and epoch > 0:
                print(f"    Early stopping at epoch {epoch}: KL divergence = {kl_div:.4f}")
                break
            
            # Gradient computation and clipping
            self.optimizer.zero_grad()
            total_loss.backward()
            
            # Compute gradient norm before clipping
            total_norm = 0
            for p in self.policy_net.parameters():
                if p.grad is not None:
                    param_norm = p.grad.data.norm(2)
                    total_norm += param_norm.item() ** 2
            total_norm = total_norm ** 0.5
            
            # Adaptive gradient clipping
            max_grad_norm = 1.0 if round_num <= 3 else 0.5
            torch.nn.utils.clip_grad_norm_(self.policy_net.parameters(), max_grad_norm)
            
            # Update parameters
            self.optimizer.step()
            
            # Track best policy loss for potential rollback
            if policy_loss.item() < best_policy_loss:
                best_policy_loss = policy_loss.item()
            
            # Log metrics if tracker provided
            if metrics_tracker:
                metrics_tracker.log_update_metrics(
                    round_num=round_num,
                    update_idx=update_idx,
                    policy_loss=policy_loss.item(),
                    value_loss=value_loss.item(),
                    total_loss=total_loss.item(),
                    gradient_norm=total_norm,
                    kl_divergence=kl_div
                )
            
            update_idx += 1
            
            # Print progress for important epochs
            if epoch % max(1, epochs // 4) == 0:
                print(f"    Epoch {epoch}: policy_loss={policy_loss.item():.4f}, "
                    f"value_loss={value_loss.item():.4f}, "
                    f"entropy={entropies.mean().item():.4f}, "
                    f"kl_div={kl_div:.4f}")


    def generate_sequence_with_temperature(self, temperature: float = 1.0, 
                                        use_top_k: bool = False, k: int = 3) -> List[int]:
        """
        Generate sequence with temperature-controlled sampling and optional top-k filtering
        """
        sequence = []
        
        with torch.no_grad():
            for t in range(self.max_seq_len):
                # Prepare input
                if len(sequence) < self.max_seq_len:
                    padded_seq = sequence + [0] * (self.max_seq_len - len(sequence))
                else:
                    padded_seq = sequence
                
                seq_tensor = torch.tensor([padded_seq], dtype=torch.long)
                pos_tensor = torch.tensor([t])
                
                # Get policy probabilities
                policy_probs, _ = self.policy_net(seq_tensor, pos_tensor)
                
                # Apply temperature scaling
                if temperature != 1.0:
                    # Convert to logits, apply temperature, then back to probabilities
                    logits = torch.log(policy_probs[0] + 1e-10)
                    logits = logits / temperature
                    
                    # Optional top-k filtering for more focused generation
                    if use_top_k and k < self.vocab_size:
                        top_k_values, top_k_indices = torch.topk(logits, k)
                        logits_filtered = torch.full_like(logits, float('-inf'))
                        logits_filtered.scatter_(0, top_k_indices, top_k_values)
                        policy_probs = F.softmax(logits_filtered, dim=-1).unsqueeze(0)
                    else:
                        policy_probs = F.softmax(logits, dim=-1).unsqueeze(0)
                
                # Sample from distribution
                dist = Categorical(policy_probs[0])
                action = dist.sample().item()
                sequence.append(action)
        
        return sequence


    def predict_with_improved_ensemble(self, sequences: List[List[int]], 
                                    models: List, round_num: int = 0) -> List[float]:
        """
        Improved ensemble prediction with uncertainty handling
        """
        if not models:
            # Return neutral predictions if no models
            return [0.0] * len(sequences)
        
        # Use oracle-aligned features
        X = self.create_oracle_aligned_features(sequences)
        
        predictions = []
        weights = []
        
        # Extract model info (name, model, score) tuples
        for model_info in models:
            if isinstance(model_info, tuple) and len(model_info) == 3:
                name, model, score = model_info
                
                try:
                    # Make predictions
                    pred = model.predict(X)
                    
                    # Clip predictions to reasonable range based on observed rewards
                    if self.all_data:
                        all_rewards = [r for _, r in self.all_data]
                        min_reward = np.percentile(all_rewards, 5)
                        max_reward = np.percentile(all_rewards, 95)
                        pred = np.clip(pred, min_reward, max_reward)
                    
                    predictions.append(pred)
                    
                    # Weight based on R² score (only positive contributions)
                    weight = max(0, score + 0.5)  # Even negative R² gets some weight
                    weights.append(weight)
                    
                except Exception as e:
                    print(f"    Prediction error with {name}: {e}")
                    continue
        
        if not predictions:
            # Fallback to mean reward if all predictions fail
            if self.all_data:
                mean_reward = np.mean([r for _, r in self.all_data])
                return [mean_reward] * len(sequences)
            else:
                return [0.0] * len(sequences)
        
        # Weighted ensemble prediction
        predictions = np.array(predictions)
        weights = np.array(weights)
        
        # Normalize weights
        if weights.sum() > 0:
            weights = weights / weights.sum()
        else:
            weights = np.ones(len(weights)) / len(weights)
        
        # Compute weighted average
        ensemble_pred = np.average(predictions, axis=0, weights=weights)
        
        # Add small noise for diversity in early rounds
        if round_num <= 5:
            noise = np.random.normal(0, 0.1, size=ensemble_pred.shape)
            ensemble_pred += noise
        
        return ensemble_pred.tolist()


    def compute_intrinsic_reward(self, sequence: List[int], round_num: int) -> float:
        """
        Compute intrinsic reward to encourage exploration of under-explored regions
        """
        if not self.sequence_history or round_num <= 2:
            return 0.0
        
        # Compute novelty based on distance to nearest neighbors
        min_distances = []
        for hist_seq in self.sequence_history[-100:]:  # Check last 100 sequences
            dist = edit_distance(sequence, hist_seq)
            min_distances.append(dist)
        
        # Sort and take k-nearest
        min_distances.sort()
        k = min(5, len(min_distances))
        avg_distance = np.mean(min_distances[:k])
        
        # Novelty bonus (higher for more different sequences)
        novelty_reward = min(1.0, avg_distance / self.max_seq_len) * 0.5
        
        # Exploration bonus based on round
        exploration_weight = max(0, 1 - round_num / 10)
        
        return novelty_reward * exploration_weight


    def update_learning_rate(self, round_num: int, performance_trend: Optional[List[float]] = None):
        """
        Adaptive learning rate scheduling based on performance
        """
        base_lr = 3e-4
        min_lr = 1e-5
        
        # Cosine annealing with warm restarts
        period = 5
        round_in_period = round_num % period
        cos_out = np.cos(np.pi * round_in_period / period)
        scheduled_lr = min_lr + (base_lr - min_lr) * 0.5 * (1 + cos_out)
        
        # Performance-based adjustment
        if performance_trend and len(performance_trend) >= 3:
            # Check if performance is plateauing
            recent_trend = performance_trend[-3:]
            variance = np.var(recent_trend)
            
            if variance < 0.01:  # Plateaued
                # Reduce learning rate
                scheduled_lr *= 0.5
                print(f"  Performance plateaued, reducing LR to {scheduled_lr:.6f}")
            elif all(recent_trend[i] > recent_trend[i-1] for i in range(1, len(recent_trend))):
                # Consistent improvement
                scheduled_lr *= 1.2
                print(f"  Consistent improvement, increasing LR to {scheduled_lr:.6f}")
        
        # Clip to reasonable range
        final_lr = np.clip(scheduled_lr, min_lr, base_lr)
        
        # Update optimizer
        for param_group in self.optimizer.param_groups:
            param_group['lr'] = final_lr
        
        return final_lr


    def analyze_and_report_progress(self, round_num: int, results: Dict) -> Dict:
        """
        Analyze training progress and provide insights
        """
        analysis = {
            'round': round_num,
            'status': 'normal',
            'recommendations': []
        }
        
        # Check R² scores
        if 'model_r2_scores' in results and results['model_r2_scores']:
            max_r2 = np.max(results['model_r2_scores'])
            mean_r2 = np.mean(results['model_r2_scores'])
            
            if max_r2 < -0.5:
                analysis['status'] = 'critical'
                analysis['recommendations'].append(
                    "R² scores very poor. Consider: "
                    "1) Increasing warm-up samples, "
                    "2) Simplifying oracle function, "
                    "3) Using different feature engineering"
                )
            elif max_r2 < 0:
                analysis['status'] = 'warning'
                analysis['recommendations'].append(
                    "R² scores negative. Models struggling to learn. "
                    "Try collecting more diverse data."
                )
            elif max_r2 > 0.5:
                analysis['status'] = 'excellent'
                analysis['recommendations'].append(
                    "Models learning well. Can increase model-based training."
                )
        
        # Check diversity
        if results.get('sequence_diversity', 0) < 0.5:
            analysis['recommendations'].append(
                "Low sequence diversity. Increase exploration or temperature."
            )
        
        # Check reward progression
        if round_num > 5:
            recent_rewards = [self.all_data[i][1] for i in range(-50, 0) if -i <= len(self.all_data)]
            if recent_rewards:
                trend = np.polyfit(range(len(recent_rewards)), recent_rewards, 1)[0]
                if trend < 0:
                    analysis['recommendations'].append(
                        "Reward trend declining. Consider resetting exploration parameters."
                    )
        
        # Print analysis
        print(f"\n  === Progress Analysis ===")
        print(f"  Status: {analysis['status'].upper()}")
        for rec in analysis['recommendations']:
            print(f"  • {rec}")
        
        return analysis





    def create_oracle_aligned_features(self, sequences: List[List[int]]) -> np.ndarray:
        """
        Create features that directly align with oracle function components
        This is CRITICAL for improving R² scores
        """
        features = []
        
        for seq in sequences:
            seq_features = []
            
            # Map to DNA string for easier feature extraction
            dna_map = {0: 'A', 1: 'T', 2: 'G', 3: 'C'}
            seq_str = ''.join([dna_map[b] for b in seq])
            
            # ========== ORACLE-ALIGNED FEATURES ==========
            
            # 1. GC Content (critical for oracle)
            gc_content = (seq.count(2) + seq.count(3)) / len(seq)
            seq_features.append(gc_content)
            
            # 2. GC Content deviation from optimal (0.5)
            gc_deviation = abs(gc_content - 0.5)
            seq_features.append(gc_deviation)
            
            # 3. GC Content squared (captures the Gaussian penalty)
            seq_features.append(gc_content ** 2)
            
            # 4. Motif counts (directly from oracle)
            motifs = ['GAATTC', 'GGATCC', 'GGCC', 'TATA', 'ATCG', 'GC']
            for motif in motifs:
                count = seq_str.count(motif)
                seq_features.append(count)
            
            # 5. Position-specific GC preference
            for i in range(min(4, len(seq))):  # First 4 positions
                seq_features.append(1 if seq[i] in [2, 3] else 0)
            
            for i in range(max(0, len(seq)-4), len(seq)):  # Last 4 positions
                seq_features.append(1 if seq[i] in [2, 3] else 0)
            
            # 6. Dinucleotide frequencies (from oracle)
            important_dinucs = ['CG', 'GC', 'AA', 'TT', 'GA', 'TC']
            for dinuc in important_dinucs:
                count = sum(1 for i in range(len(seq_str)-1) 
                            if seq_str[i:i+2] == dinuc)
                seq_features.append(count / max(1, len(seq_str)-1))
            
            # 7. Repeat penalty features
            max_repeat = 0
            current_repeat = 1
            for i in range(1, len(seq)):
                if seq[i] == seq[i-1]:
                    current_repeat += 1
                    max_repeat = max(max_repeat, current_repeat)
                else:
                    current_repeat = 1
            seq_features.append(max_repeat / len(seq))
            
            # 8. Complexity measures
            unique_in_windows = []
            window_size = 4
            for i in range(len(seq) - window_size + 1):
                window = seq[i:i+window_size]
                unique_in_windows.append(len(set(window)))
            
            if unique_in_windows:
                seq_features.append(np.mean(unique_in_windows) / 4)
                seq_features.append(np.std(unique_in_windows))
            else:
                seq_features.append(1.0)
                seq_features.append(0.0)
            
            # 9. Melting temperature proxy
            tm_proxy = (4 * gc_content + 2 * (1 - gc_content)) / 6
            seq_features.append(tm_proxy)
            
            # 10. Base frequencies (individual)
            for base in range(4):
                freq = seq.count(base) / len(seq)
                seq_features.append(freq)
            
            # 11. Positional encoding (simplified)
            for pos in [0, len(seq)//4, len(seq)//2, 3*len(seq)//4, len(seq)-1]:
                if pos < len(seq):
                    seq_features.extend([1 if seq[pos] == b else 0 for b in range(4)])
                else:
                    seq_features.extend([0] * 4)
            
            features.append(seq_features)
        
        return np.array(features)

    # def create_smart_surrogate_models(self, data_size: int) -> List:
    #     """
    #     Create models specifically tuned for this problem
    #     """
    #     models = []
        
    #     if data_size < 100:
    #         # For small data: Simple, robust models
            
    #         # 1. Simple Random Forest with regularization
    #         models.append(('rf_simple', RandomForestRegressor(
    #             n_estimators=50,
    #             max_depth=3,
    #             min_samples_split=10,
    #             min_samples_leaf=5,
    #             max_features='sqrt',
    #             random_state=42
    #         )))
            
    #         # 2. Gaussian Process with proper kernel
    #         kernel = ConstantKernel(1.0) * RBF(length_scale=1.0)
    #         models.append(('gp', GaussianProcessRegressor(
    #             kernel=kernel,
    #             alpha=0.1,  # Noise level
    #             random_state=42
    #         )))
            
    #         # 3. Ridge with polynomial features
    #         from sklearn.linear_model import Ridge
    #         models.append(('poly_ridge', Pipeline([
    #             ('poly', PolynomialFeatures(degree=2, include_bias=False)),
    #             ('ridge', Ridge(alpha=1.0))
    #         ])))
            
    #     else:
    #         # For larger data: More complex models
            
    #         # 1. Tuned Random Forest
    #         models.append(('rf_tuned', RandomForestRegressor(
    #             n_estimators=min(200, data_size),
    #             max_depth=min(10, data_size // 30),
    #             min_samples_split=5,
    #             min_samples_leaf=2,
    #             max_features='sqrt',
    #             random_state=42
    #         )))
            
    #         # 2. Gradient Boosting with careful regularization
    #         models.append(('gb_tuned', GradientBoostingRegressor(
    #             n_estimators=min(100, data_size // 2),
    #             max_depth=4,
    #             learning_rate=0.05,
    #             subsample=0.8,
    #             random_state=42
    #         )))
            
    #         # 3. Ensemble of simple models
    #         ensemble = VotingRegressor([
    #             ('rf1', RandomForestRegressor(n_estimators=50, max_depth=5)),
    #             ('rf2', RandomForestRegressor(n_estimators=100, max_depth=3)),
    #             ('gb', GradientBoostingRegressor(n_estimators=50, max_depth=3))
    #         ])
    #         models.append(('ensemble', ensemble))
        
    #     return models
    
    def create_smart_surrogate_models(self, data_size: int) -> List[Tuple[str, SurrogateModel]]:
        """
        Create models specifically tuned for this problem using SurrogateModel class
        """
        models = []
        
        if data_size < 100:
            # ========== For small data: Simple, robust models ==========
            
            # Random Forest variants (regularized for small data)
            models.append(('rf-xs',SurrogateModel('rf', 
                n_estimators=30,
                max_depth=3,
                min_samples_split=10,
                min_samples_leaf=5,
                max_features='sqrt',
                random_state=42
            )))
            
            models.append(('rf-s',SurrogateModel('rf',
                n_estimators=50,
                max_depth=4,
                min_samples_split=8,
                min_samples_leaf=4,
                random_state=42
            )))
            
            # KNN with different neighbors (adaptive to data size)
            models.append(('knn-xs',SurrogateModel('knn', n_neighbors=min(3, data_size//10))))
            models.append(('knn-s',SurrogateModel('knn', n_neighbors=min(5, data_size//5))))
            
            # Ridge regression (good for small data)
            models.append(('ridge',SurrogateModel('ridge')))
            
            # Light Gradient Boosting
            models.append(('gb-xs',SurrogateModel('gb',
                n_estimators=30,
                max_depth=3,
                learning_rate=0.1,
                subsample=0.8,
                random_state=42
            )))
            
            # Gaussian Process (excellent for small data)
            kernel = ConstantKernel(1.0) * RBF(length_scale=1.0)
            models.append(('gp',SurrogateModel('gp',
                kernel=kernel,
                alpha=0.1,  # Noise level
                random_state=42
            )))
            
            # SVR for non-linear patterns
            models.append(('svr-rbf-s',SurrogateModel('svr',
                kernel='rbf',
                C=1.0,
                gamma='scale',
                epsilon=0.1
            )))
            
        elif data_size < 300:
            # ========== For medium data: Balanced complexity ==========
            
            # Random Forest variants
            models.append(('rf-m',SurrogateModel('rf',
                n_estimators=100,
                max_depth=5,
                min_samples_split=5,
                min_samples_leaf=2,
                random_state=42
            )))
            
            models.append(('rf-l',SurrogateModel('rf',
                n_estimators=150,
                max_depth=7,
                min_samples_split=4,
                random_state=42
            )))
            
            # Gradient Boosting
            models.append(('gb-m',SurrogateModel('gb',
                n_estimators=50,
                max_depth=4,
                learning_rate=0.05,
                subsample=0.8,
                random_state=42
            )))
            
            models.append(('gb-l',SurrogateModel('gb',
                n_estimators=75,
                max_depth=5,
                learning_rate=0.03,
                random_state=42
            )))
            
            # XGBoost (starts to work with medium data)
            models.append(('xgb-m', SurrogateModel('xgb',
                n_estimators=100,
                max_depth=5,
                learning_rate=0.05,
                subsample=0.8,
                colsample_bytree=0.8,
                random_state=42
            )))
            
            # KNN variants
            models.append(('knn-m',SurrogateModel('knn', n_neighbors=5)))
            models.append(('knn-tuned',SurrogateModel('knn', n_neighbors=int(np.sqrt(data_size)))))
            
            # Neural Network (simple architecture)
            models.append(('mlp-m', SurrogateModel('mlp',
                hidden_layer_sizes=(50, 25),
                max_iter=300,
                early_stopping=True,
                validation_fraction=0.2,
                random_state=42
            )))
            
            # SVR variants
            models.append(('svr-rbf', SurrogateModel('svr', kernel='rbf', C=1.0)))
            models.append(('svr-poly', SurrogateModel('svr', kernel='poly', degree=2, C=1.0)))
            
            # Ridge
            models.append(('ridge', SurrogateModel('ridge')))
            
        else:
            # ========== For large data: Complex models ==========
            
            # Random Forest variants (can handle complexity)
            models.append(('rf-tuned-l', SurrogateModel('rf',
                n_estimators=min(200, data_size//2),
                max_depth=min(10, data_size//30),
                min_samples_split=5,
                min_samples_leaf=2,
                max_features='sqrt',
                random_state=42
            )))
            
            models.append(('rf-tuned-xl', SurrogateModel('rf',
                n_estimators=min(300, data_size),
                max_depth=min(15, data_size//20),
                min_samples_split=3,
                random_state=42
            )))
            
            # Gradient Boosting variants
            models.append(('gb-tuned-l', SurrogateModel('gb',
                n_estimators=min(100, data_size//3),
                max_depth=5,
                learning_rate=0.05,
                subsample=0.8,
                random_state=42
            )))
            
            models.append(('gb-tuned-xl', SurrogateModel('gb',
                n_estimators=min(150, data_size//2),
                max_depth=6,
                learning_rate=0.03,
                subsample=0.7,
                random_state=42
            )))
            
            # XGBoost variants (powerful for large data)
            models.append(('xgb-xl', SurrogateModel('xgb',
                n_estimators=200,
                max_depth=8,
                learning_rate=0.05,
                subsample=0.8,
                colsample_bytree=0.8,
                reg_alpha=0.1,
                reg_lambda=1.0,
                random_state=42
            )))
            
            models.append(('xgb-l', SurrogateModel('xgb',
                n_estimators=150,
                max_depth=6,
                learning_rate=0.1,
                subsample=0.7,
                random_state=42
            )))
            
            # Neural Network variants (can learn complex patterns)
            models.append(('mlp-adaptive-xl', SurrogateModel('mlp',
                hidden_layer_sizes=(128, 64, 32),
                max_iter=500,
                early_stopping=True,
                validation_fraction=0.15,
                learning_rate='adaptive',
                random_state=42
            )))
            
            models.append(('mlp-l', SurrogateModel('mlp',
                hidden_layer_sizes=(100, 50),
                max_iter=400,
                early_stopping=True,
                activation='tanh',
                random_state=42
            )))
            
            # SVR variants
            models.append(('svr-rbf-xl', SurrogateModel('svr', 
                kernel='rbf', 
                C=10.0, 
                gamma='auto',
                epsilon=0.01
            )))
            
            models.append(('svr-poly-l', SurrogateModel('svr',
                kernel='poly',
                degree=3,
                C=1.0,
                epsilon=0.1
            )))
            
            # KNN (with optimal k)
            models.append(('knn-tuned-sqrt', SurrogateModel('knn', n_neighbors=int(np.sqrt(data_size)))))
            models.append(('knn-tuned-l', SurrogateModel('knn', n_neighbors=min(20, data_size//20))))
            
            # Ridge (always good as baseline)
            models.append(('ridge', SurrogateModel('ridge')))
            
            # Gaussian Process (if data not too large)
            if data_size < 500:
                kernel = Matern(length_scale=1.0, nu=1.5)
                models.append(('gp', SurrogateModel('gp',
                    kernel=kernel,
                    alpha=0.1,
                    random_state=42
                )))
        
        print(f"  Created {len(models)} candidate models for data size {data_size}")
        model_types = {}
        for model in models:
            # model_types[model.model_type] = model_types.get(model.model_type, 0) + 1
            print(model[0])
        print(f"  Model distribution: {model_types}")
        
        return models

    def improved_fit_surrogate_models(self, sequences: List[List[int]], 
                                        rewards: List[float], round_num: int):
        """
        Completely revised model fitting with better strategies
        """
        if len(sequences) < 30:  # Need more data before trying models
            return [], []
        
        # Use oracle-aligned features
        X = self.create_oracle_aligned_features(sequences)
        y = np.array(rewards)
        
        # CRITICAL: Don't normalize rewards for tree-based models!
        # Tree-based models handle different scales well
        
        # Remove outliers for more stable training
        q1, q3 = np.percentile(y, [25, 75])
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        mask = (y >= lower_bound) & (y <= upper_bound)
        
        if mask.sum() < 20:  # If too many outliers, use all data
            X_clean, y_clean = X, y
        else:
            X_clean, y_clean = X[mask], y[mask]
        
        print(f"\nTraining on {len(y_clean)} samples (removed {len(y)-len(y_clean)} outliers)")
        print(f"Reward range: [{y_clean.min():.2f}, {y_clean.max():.2f}], mean: {y_clean.mean():.2f}")
        
        # Get appropriate models
        model_candidates = self.create_smart_surrogate_models(len(y_clean))
        
        reliable_models = []
        r2_scores = []
        
        for name, model in model_candidates:
            try:
                # Use fewer CV folds for small datasets
                cv_folds = min(5, len(y_clean) // 10)
                
                from sklearn.model_selection import cross_val_score
                scores = cross_val_score(model, X_clean, y_clean, 
                                        cv=cv_folds, scoring='r2')
                mean_score = scores.mean()
                
                print(f"  {name}: R² = {mean_score:.3f} (std: {scores.std():.3f})")
                
                r2_scores.append(mean_score)
                
                # Accept ANY positive R² in early rounds
                threshold = -0.2 if round_num <= 3 else 0.0
                
                if mean_score > threshold:
                    model.fit(X_clean, y_clean)
                    reliable_models.append((name, model, mean_score))
                    
            except Exception as e:
                print(f"  {name}: Failed - {e}")
                r2_scores.append(-999)
        
        # If no good models, use the best one anyway
        if not reliable_models and r2_scores:
            best_idx = np.argmax(r2_scores)
            if r2_scores[best_idx] > -0.5:
                name, model = model_candidates[best_idx]
                model.fit(X_clean, y_clean)
                reliable_models.append((name, model, r2_scores[best_idx]))
                print(f"  Fallback: Using {name} with R² = {r2_scores[best_idx]:.3f}")
        
        return reliable_models, r2_scores

    def guided_sequence_generation(self, batch_size: int, round_num: int):
        """
        Generate sequences with guided exploration based on what works
        """
        sequences = []
        
        # Analyze best sequences so far
        if self.all_data:
            sorted_data = sorted(self.all_data, key=lambda x: x[1], reverse=True)
            top_10_percent = sorted_data[:max(5, len(sorted_data)//10)]
            
            # Extract patterns from best sequences
            best_gc_contents = []
            for seq, _ in top_10_percent:
                gc = (seq.count(2) + seq.count(3)) / len(seq)
                best_gc_contents.append(gc)
            
            target_gc = np.mean(best_gc_contents) if best_gc_contents else 0.5
            gc_std = np.std(best_gc_contents) if len(best_gc_contents) > 1 else 0.1
        else:
            target_gc = 0.5
            gc_std = 0.2
        
        # Generate diverse sequences with bias toward good patterns
        for i in range(batch_size):
            if i < batch_size // 3 and round_num > 3:
                # Exploit: Generate near optimal GC content
                desired_gc = np.clip(np.random.normal(target_gc, gc_std/2), 0.3, 0.7)
                n_gc = int(desired_gc * self.max_seq_len)
                n_at = self.max_seq_len - n_gc
                
                seq = ([2, 3] * (n_gc // 2 + 1))[:n_gc] + \
                        ([0, 1] * (n_at // 2 + 1))[:n_at]
                np.random.shuffle(seq)
                sequences.append(seq[:self.max_seq_len])
                
            elif i < 2 * batch_size // 3:
                # Explore with temperature
                temp = 1.2 if round_num <= 5 else 1.0
                seq = self.generate_sequence_with_temperature(temp)
                sequences.append(seq)
                
            else:
                # Random exploration
                seq = [np.random.randint(0, self.vocab_size) 
                        for _ in range(self.max_seq_len)]
                sequences.append(seq)
        
        return sequences


    