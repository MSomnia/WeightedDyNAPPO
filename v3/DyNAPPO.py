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
import warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn.model_selection import cross_val_score
import sys

# File import
from SurrogateModel import SurrogateModel
from PolicyNetwork import PolicyNetwork
from SequenceUtils import compute_diversity_penalty, sequence_to_features, edit_distance, compute_sequence_diversity
from LearningRateTracker import LearningMetricsTracker
from OptimalEnsembleWeights import OptimalEnsembleWeights

# SETTINGS
# This will ignore all convergence warnings
warnings.filterwarnings("ignore", category=ConvergenceWarning)


class DyNAPPO:
    
    def __init__(self, vocab_size: int, max_seq_len: int, batch_size: int = 64,
                 learning_rate: float = 3e-4, gamma: float = 0.99, clip_ratio: float = 0.2,
                 model_threshold: float = 0.5, max_total_rounds: int = 10, max_model_rounds: int = 5,
                 diversity_lambda: float = 0.05, diversity_epsilon: int = 3,
                 method = 'average', threshold_type = 'fixed', diversity_penalty = 'yes', use_warmup = True):
        
        self.vocab_size = vocab_size
        self.max_seq_len = max_seq_len
        self.batch_size = batch_size
        self.gamma = gamma
        self.clip_ratio = clip_ratio
        self.model_threshold = model_threshold
        self.max_model_rounds = max_model_rounds
        self.max_total_rounds = max_total_rounds
        self.diversity_lambda = diversity_lambda
        self.diversity_epsilon = diversity_epsilon

        # ['average', 'weighted', 'dynamic']
        self.ensemble_method = method
        self.threshold_type = threshold_type
        self.diversity_penalty = diversity_penalty
        self.use_warmup = use_warmup
        
        # Initialize policy network
        self.policy_net = PolicyNetwork(vocab_size, max_seq_len)
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=learning_rate)
        
        # Surrogate models
        #self.surrogate_models = self.create_smart_surrogate_models()

        # Data storage
        self.all_data = []
        self.sequence_history = []

        self.feature_scaler = StandardScaler()
        self.pca = None  # Will be initialized when enough data
        
        # Track model performance over time
        self.model_performance_history = {}

        # Add threshold tracking
        self.threshold_history = []  # Store (round, threshold) pairs

        # Add weight learner
        self.weight_learner = OptimalEnsembleWeights(method='validation')

        # Add model performance tracking
        self.model_performance_history = {
            'rounds': [],
            'model_names': [],
            'r2_scores': [],
            'weights': [],
            'prediction_errors': []
        }

        # Oracle call tracking
        self.oracle_call_count = 0
        self.oracle_call_history = []  # (round, cumulative_calls, best_reward)

    def track_oracle_call(self, round_num: int, n_calls: int, best_reward: float):
        """Track oracle usage"""
        self.oracle_call_count += n_calls
        self.oracle_call_history.append({
            'round': round_num,
            'cumulative_calls': self.oracle_call_count,
            'new_calls': n_calls,
            'best_reward_so_far': best_reward
        })


    """
    Create models specifically tuned for this problem using SurrogateModel class
    """
    def create_smart_surrogate_models(self, data_size: int) -> List[Tuple[str, SurrogateModel]]:

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
                max_iter=500,
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
                max_iter=1000,
                early_stopping=True,
                validation_fraction=0.15,
                learning_rate='adaptive',
                random_state=42
            )))
            
            models.append(('mlp-l', SurrogateModel('mlp',
                hidden_layer_sizes=(100, 50),
                max_iter=800,
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
        # model_types = {}
        # for model in models:
        #     # model_types[model.model_type] = model_types.get(model.model_type, 0) + 1
        #     print(model[0])
        # print(f"  Model distribution: {model_types}")
        
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




    """
    Generate a sequence of tokens autoregressively using temperature-controlled sampling.
    This method allows for creativity scaling (temperature) and can limit the choices to 
    the top 'k' most likely next tokens to prevent nonsensical outputs.

    temperature:    Controls the randomness of predictions. 
                    Higher values (>1.0) increase diversity 
                    Lower values (<1.0) make the model more confident and deterministic. 
                    A value of 1.0 means no change.
    """
    def generate_sequence_with_temperature(self, temperature: float = 1.0, 
                                    use_top_k: bool = False, k: int = 3) -> List[int]:
        sequence = []
        
        with torch.no_grad():
            for t in range(self.max_seq_len):
                # Prepare input
                # Pad the current sequence with zeros to match the required input length.
                if len(sequence) < self.max_seq_len:
                    padded_seq = sequence + [0] * (self.max_seq_len - len(sequence))
                else:
                    padded_seq = sequence
                
                # Convert the padded sequence and current position into tensors.
                seq_tensor = torch.tensor([padded_seq], dtype=torch.long)
                pos_tensor = torch.tensor([t])
                
                # Get policy probabilities
                policy_probs, _ = self.policy_net(seq_tensor, pos_tensor)
                
                # Apply temperature scaling
                if temperature != 1.0:
                    # Convert probabilities to logits to stabily apply temperature. A small epsilon
                    # (1e-10) is added to prevent log(0), which is undefined.
                    logits = torch.log(policy_probs[0] + 1e-10)
                    # Scale the logits by the temperature. Lower temp -> sharper peaks; Higher temp -> flatter distribution
                    logits = logits / temperature
                    
                    # Optional top-k filtering for more focused generation
                    if use_top_k and k < self.vocab_size:
                        # Get the values and indices of the 'k' highest logits.
                        top_k_values, top_k_indices = torch.topk(logits, k)
                        # Create a new tensor filled with negative infinity.
                        logits_filtered = torch.full_like(logits, float('-inf'))
                        # Keep only the top 'k' logits and set all others to -infinity.
                        # This ensures they will have a probability of 0 after the softmax.
                        logits_filtered.scatter_(0, top_k_indices, top_k_values)
                        # Convert the filtered logits back to a probability distribution
                        policy_probs = F.softmax(logits_filtered, dim=-1).unsqueeze(0)
                    else:
                        # If not using top-k, just convert the temperature-scaled logits back to probabilities
                        policy_probs = F.softmax(logits, dim=-1).unsqueeze(0)
                
                # Sample from distribution
                dist = Categorical(policy_probs[0])
                action = dist.sample().item()
                sequence.append(action)
        
        return sequence



    """
        Generates a batch of sequences using a strategy that balances exploiting known
        successful patterns with exploring new possibilities.

        This method analyzes the best-performing sequences from previous rounds to identify
        desirable traits (like GC content) and then generates new sequences that are either:
        1. Similar to the best ones (exploitation).
        2. Creatively varied using the model (guided exploration).
        3. Completely random (random exploration).
    """
    def guided_sequence_generation(self, batch_size: int, round_num: int):
        
        sequences = []
        
        # Analyze best sequences so far
        if self.all_data:
            # Sort all previously seen sequences by their performance score in descending order
            sorted_data = sorted(self.all_data, key=lambda x: x[1], reverse=True)
            # Select the top 10% of sequences, with a minimum of 5, to analyze
            top_10_percent = sorted_data[:max(5, len(sorted_data)//10)]
            
            # Extract patterns from best sequences
            best_gc_contents = []
            for seq, _ in top_10_percent:
                gc = (seq.count(2) + seq.count(3)) / len(seq)
                best_gc_contents.append(gc)
            
            # Determine the ideal GC content based on the average of the best sequences
            target_gc = np.mean(best_gc_contents) if best_gc_contents else 0.5
            # Calculate the standard deviation to understand the allowable variance
            gc_std = np.std(best_gc_contents) if len(best_gc_contents) > 1 else 0.1
        else:
            # If it's the first round, aim for a neutral GC content.
            target_gc = 0.5
            gc_std = 0.2
        
        # Generate diverse sequences with bias toward good patterns
        for i in range(batch_size):
            # 1. Exploit: Generate near optimal GC content (First 1/3 of the batch)
            if i < batch_size // 3 and round_num > 3:
                # Generate a sequence with a GC content close to the optimal `target_gc`.
                # Sample from a normal distribution centered on the target, with a tighter std dev
                desired_gc = np.clip(np.random.normal(target_gc, gc_std/2), 0.3, 0.7)
                # Calculate the number of GC and AT bases
                n_gc = int(desired_gc * self.max_seq_len)
                n_at = self.max_seq_len - n_gc
                
                # Construct the sequence with the exact number of desired bases and then shuffle
                seq = ([2, 3] * (n_gc // 2 + 1))[:n_gc] + ([0, 1] * (n_at // 2 + 1))[:n_at]
                np.random.shuffle(seq)
                sequences.append(seq[:self.max_seq_len])

            # 2. GUIDED EXPLORATION (Second 1/3 of the batch) 
            # Use the neural network to generate sequences, allowing for creative variations
            elif i < 2 * batch_size // 3:
                # Use a higher temperature in early rounds to encourage more diversity.
                # In later rounds, reduce temperature to refine solutions
                temp = 1.2 if round_num <= 5 else 1.0
                seq = self.generate_sequence_with_temperature(temp)
                sequences.append(seq)

            # 3. RANDOM EXPLORATION (Final 1/3 of the batch)
            # Generate completely random sequences to ensure diversity and avoid getting stuck in a local optimum. 
            # This helps discover entirely new patterns
            else:
                seq = [np.random.randint(0, self.vocab_size) 
                        for _ in range(self.max_seq_len)]
                sequences.append(seq)
        
        return sequences



    """
        Create features for each sequence using context window approach.
        At each position t, encode:
        1. The last W characters (one-hot encoded)
        2. The current position t (sinusoidal positional encoding)
        
        context_window: Size W of the context window
        embed_dim: Dimension of positional encoding

        Better features -> Better predictions -> Better R2 scores

        Outputs a fixed-size vector that represents the last W characters of a sequence plus the sequence's position information
        For each sequence, it outputs a single row of 48 numbers: 32 for the last 8 bases + 16 for position information
    """
    def context_window_encoding(self, sequences: List[List[int]], 
                                   context_window: int = 8,
                                   embed_dim: int = 16) -> np.ndarray:
        
        features = []
        
        for seq in sequences:
            # For each sequence, create features based on the LAST position
            # since we're predicting the full sequence, we use the final context
            t = len(seq)  # Current time step (position after the sequence)
            
            # 1. Extract context window (last W characters)
            if t >= context_window:
                # Full context window available
                context = seq[t - context_window : t]
            else:
                # Pad with zeros if sequence shorter than window
                padding = [0] * (context_window - t)
                context = padding + seq[:t]
            
            # 2. One-hot encode the context window
            context_one_hot = np.zeros(context_window * self.vocab_size)
            for i, token in enumerate(context):
                if token != 0:  # 0 is padding
                    context_one_hot[i * self.vocab_size + token] = 1
            
            # 3. Create sinusoidal positional encoding for position t
            pos_encoding = self.sinusoidal_encoding(t, embed_dim)
            
            # 4. Concatenate context one-hot with positional encoding
            seq_features = np.concatenate([context_one_hot, pos_encoding])
            features.append(seq_features)
        
        return np.array(features)




    """
    Generate sinusoidal positional encoding
    
    Args:
        position: The position/time step t
        embed_dim: Dimension of the positional encoding
    
    Returns:
        Positional encoding vector of size embed_dim
    """
    def sinusoidal_encoding(self, position: int, embed_dim: int) -> np.ndarray:

        encoding = np.zeros(embed_dim)
        
        for i in range(0, embed_dim, 2):
            # Denominator from the paper
            denominator = np.power(10000, 2 * i / embed_dim)
            
            # Apply sin to even indices
            encoding[i] = np.sin(position / denominator)
            
            # Apply cos to odd indices
            if i + 1 < embed_dim:
                encoding[i + 1] = np.cos(position / denominator)
        
        return encoding



    """
    Adaptive policy update with entropy regularization and dynamic hyperparameters
    """
    def adaptive_policy_update(self, sequences: List[List[int]], rewards: List[float], 
                          old_log_probs: List[float], epochs: int = 4, 
                          round_num: int = 0, 
                          metrics_tracker: Optional['LearningMetricsTracker'] = None,
                          entropy_coef: float = 0.01):
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
            
            # ******** Early stopping if KL divergence too large ********
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
            
            # Log metrics
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



    """
        Improved ensemble prediction with uncertainty handling
    """
    def predict_with_improved_ensemble(self, sequences: List[List[int]], 
                                    models: List, total_round, round_num: int = 0, method = 'average') -> List[float]:
        if not models:
            return [0.0] * len(sequences)
        
        print(f"Current Method: {method}")

        # Encoding
        X = self.context_window_encoding(sequences, context_window=8, embed_dim=16)
        #======================== Average Ensemble Method ========================
        if method not in ['average', 'weighted', 'dynamic']:
            print(f'[ERROR] Method {method} does not exist.')
            sys.exit('[ERROR] Method not exist.')
        elif method == 'average':
            predictions = []
            
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
            
            # Simple average of all predictions
            # Average predictions f''(x) = 1/|S'| Σ f'(x)
            #*********** The original algorithm uses mean *********
            predictions = np.array(predictions)
            ensemble_pred = np.mean(predictions, axis=0)
            
            # Add small noise for diversity in early rounds
            if round_num <= 5:
                noise = np.random.normal(0, 0.1, size=ensemble_pred.shape)
                ensemble_pred += noise
            
            #return ensemble_pred.tolist()



        # ================ Weighted Ensemble Method ==============
        else:
            # Get predictions from all models
            predictions = []
            model_names = []
            
            for model_info in models:
                if isinstance(model_info, tuple) and len(model_info) == 3:
                    name, model, score = model_info
                    
                    try:
                        pred = model.predict(X)
                        
                        # Clip predictions
                        if self.all_data:
                            all_rewards = [r for _, r in self.all_data]
                            min_reward = np.percentile(all_rewards, 5)
                            max_reward = np.percentile(all_rewards, 95)
                            pred = np.clip(pred, min_reward, max_reward)
                        
                        predictions.append(pred)
                        model_names.append(name)
                        
                    except Exception as e:
                        print(f"    Prediction error with {name}: {e}")
                        continue
            
            if not predictions:
                # Fallback
                if self.all_data:
                    mean_reward = np.mean([r for _, r in self.all_data])
                    return [mean_reward] * len(sequences)
                else:
                    return [0.0] * len(sequences)
            
            # ============ OPTIMAL WEIGHT LEARNING ============
            predictions = np.array(predictions)
            
            # Initialize weight learner if not exists
            if not hasattr(self, 'weight_learner'):
                self.weight_learner = OptimalEnsembleWeights(method='validation')
            
            # Learn or update weights based on historical data
            if len(self.all_data) > 50 and round_num > 2:
                # Prepare validation data from recent sequences
                val_size = min(30, len(self.all_data) // 3)
                val_data = self.all_data[-val_size:]
                
                X_val_sequences = [data[0] for data in val_data]
                y_val = np.array([data[1] for data in val_data])
                X_val = self.context_window_encoding(X_val_sequences, context_window=8, embed_dim=16)
                

                # OPTION1: R2 Performance-based weights
                if method == 'weighted':
                    weights = self.weight_learner.learn_weights_performance(models)
                    print(f"    Using performance-based weights")

                else:
                    # OPTION 2: Dynamic weight methods
                    # Choose weight learning method based on round
                    if round_num <= (total_round / 3):
                        # Early rounds: use performance-based weights
                        # Simple and fast, based solely on R² scores
                        weights = self.weight_learner.learn_weights_performance(models)
                        print(f"    Using performance-based weights")
                        
                    elif round_num <= (total_round * 2/ 3):
                        # Middle rounds: use ridge regression
                        # Regularized learning, can identify harmful models
                        weights = self.weight_learner.learn_weights_ridge(models, X_val, y_val)
                        print(f"    Using ridge regression weights")
                        
                    else:
                        # Later rounds: use validation-based optimization
                        #  Most accurate but needs validation data
                        weights = self.weight_learner.learn_weights_validation(models, X_val, y_val)
                        print(f"    Using validation-optimized weights")
                    


                # Store weights for analysis
                self.weight_learner.weight_history.append((round_num, weights))
                
                # Print weight distribution
                print(f"    Model weights: ", end="")
                for name, w in zip(model_names, weights):
                    print(f"{name}:{w:.3f} ", end="")
                print()
                
            else:
                # Early rounds or insufficient data: use uniform weights
                weights = np.ones(len(predictions)) / len(predictions)
                print(f"    Using uniform weights (insufficient data)")
            
            # Apply learned weights
            ensemble_pred = np.sum(predictions * weights[:, np.newaxis], axis=0)
            
            # Add small noise for diversity in early rounds
            if round_num <= 5:
                noise = np.random.normal(0, 0.1, size=ensemble_pred.shape)
                ensemble_pred += noise
            
            #return ensemble_pred.tolist()
        
        # Track model performance for this round
        if models and hasattr(self, 'model_performance_history'):
            # Extract model information
            tracked_names = []
            tracked_r2 = []
            tracked_weights = []
            
            for i, model_info in enumerate(models):
                if isinstance(model_info, tuple) and len(model_info) == 3:
                    name, _, score = model_info
                    tracked_names.append(name)
                    tracked_r2.append(score)
                    
                    # Get weight for this model
                    if method == 'average':
                        weight = 1.0 / len(models)
                    else:
                        weight = weights[i] if i < len(weights) else 0
                    tracked_weights.append(weight)
            
            # Store in history
            self.model_performance_history['rounds'].append(round_num)
            self.model_performance_history['model_names'].append(tracked_names)
            self.model_performance_history['r2_scores'].append(tracked_r2)
            self.model_performance_history['weights'].append(tracked_weights)
        return ensemble_pred.tolist()


    def analyze_weight_evolution(self) -> None:
        """
        Analyze how ensemble weights evolved over training.
        """
        if not hasattr(self, 'weight_learner') or not self.weight_learner.weight_history:
            print("No weight history available")
            return
        
        import matplotlib.pyplot as plt
        
        history = self.weight_learner.weight_history
        rounds = [h[0] for h in history]
        weights = np.array([h[1] for h in history])
        
        plt.figure(figsize=(10, 6))
        
        # Plot weight evolution for each model
        n_models = weights.shape[1]
        for i in range(n_models):
            plt.plot(rounds, weights[:, i], marker='o', label=f'Model {i+1}')
        
        plt.xlabel('Round')
        plt.ylabel('Weight')
        plt.title('Evolution of Ensemble Weights')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
        
        # Print final weight statistics
        final_weights = weights[-1]
        print("\nFinal Weight Distribution:")
        print(f"  Max weight: {final_weights.max():.3f}")
        print(f"  Min weight: {final_weights.min():.3f}")
        print(f"  Weight entropy: {-np.sum(final_weights * np.log(final_weights + 1e-10)):.3f}")
        
        # Identify dominant models
        top_indices = np.argsort(final_weights)[-3:][::-1]
        print(f"  Top 3 models: {top_indices.tolist()} with weights {final_weights[top_indices]}")



    """
    Compute intrinsic reward to encourage exploration of under-explored regions
    Encourage to explore new and different solutions rather than getting stuck on the same ones

    In early rounds, this weight is high (close to 1.0), meaning the novelty bonus is fully applied. 
    This strongly encourages the algorithm to explore widely at the beginning.

    In later rounds, the weight drops towards 0. 
    This gradually turns off the exploration bonus, encouraging the algorithm to focus on refining the best solutions it has already found rather than just searching for new things.
    """
    def compute_intrinsic_reward(self, sequence: List[int], round_num: int) -> float:
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
        # exploration_weight that decreases as the round_num increases
        novelty_reward = min(1.0, avg_distance / self.max_seq_len) * 0.5
        
        # Exploration bonus based on round
        exploration_weight = max(0, 1 - round_num / 10)
        
        return novelty_reward * exploration_weight



    """
    Adapts the learning rate based on a combination of a cyclical schedule and recent model performance.
    """
    def update_learning_rate(self, round_num: int, performance_trend: Optional[List[float]] = None):

        base_lr = 3e-4
        min_lr = 1e-5
        
        # --- Section 1: Cyclical Learning Rate Scheduling (Cosine Annealing) ---
        # This section implements a cosine annealing schedule with a warm restart every `period` rounds.
        # It's designed to help the model escape local minima by periodically increasing the learning rate.
        period = 5
        round_in_period = round_num % period
        # Calculate the cosine value, which will oscillate between 1 and -1.
        cos_out = np.cos(np.pi * round_in_period / period)
        # Scale the cosine output to create a learning rate that varies between min_lr and base_lr.
        scheduled_lr = min_lr + (base_lr - min_lr) * 0.5 * (1 + cos_out)
        
        # --- Section 2: Performance-Based Adjustment ---
        # This section fine-tunes the learning rate based on the recent performance trend.
        if performance_trend and len(performance_trend) >= 3:
            # Get the three most recent performance values to analyze the trend.
            recent_trend = performance_trend[-3:]
            # Calculate the variance to check for a performance plateau.
            variance = np.var(recent_trend)
            
            # A low variance indicates the performance has plateaued
            if variance < 0.01:
                # If performance is stable, reduce the learning rate to encourage convergence
                scheduled_lr *= 0.5
                print(f"  Performance plateaued, reducing LR to {scheduled_lr:.6f}")
            elif all(recent_trend[i] > recent_trend[i-1] for i in range(1, len(recent_trend))):
                # A consistent increase in performance suggests the model is still learning quickly.
                # In this case, slightly increase the learning rate to accelerate training
                scheduled_lr *= 1.2
                print(f"  Consistent improvement, increasing LR to {scheduled_lr:.6f}")
        
        # Clip to reasonable range
        final_lr = np.clip(scheduled_lr, min_lr, base_lr)
        
        # Update the learning rate in the optimizer for each parameter group.
        for param_group in self.optimizer.param_groups:
            param_group['lr'] = final_lr
        
        return final_lr




    """
    Analyze training progress and provide insights
    """
    def analyze_and_report_progress(self, round_num: int, results: Dict) -> Dict:

        analysis = {
            'round': round_num,
            'status': 'normal',
            'recommendations': []
        }
        
        # Check R2 scores
        if 'model_r2_scores' in results and results['model_r2_scores']:
            max_r2 = np.max(results['model_r2_scores'])
            mean_r2 = np.mean(results['model_r2_scores'])
            
            if max_r2 < -0.5:
                analysis['status'] = 'critical'
                analysis['recommendations'].append(
                    "R2 scores very poor. Consider: "
                    "1) Increasing warm-up samples, "
                    "2) Simplifying oracle function, "
                    "3) Using different feature engineering"
                )
            elif max_r2 < 0:
                analysis['status'] = 'warning'
                analysis['recommendations'].append(
                    "R2 scores negative. Models struggling to learn. "
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


    """
    Calculate dynamic R² threshold with smooth linear progression.
    
    Threshold increases linearly from -0.3 to 0.3 over training.
    """
    # Smooth linear progression of threshold
    def get_dynamic_threshold1(round_num: int, total_rounds: int) -> float:

        start_threshold = -0.3  # Beginning threshold
        end_threshold = 0.3     # Final threshold
        
        # Linear interpolation based on progress
        progress = (round_num - 1) / max(1, total_rounds - 1)
        threshold = start_threshold + (end_threshold - start_threshold) * progress
        
        return threshold
    

    """
    Completely revised model fitting with better strategies
    """
    def improved_fit_surrogate_models(self, sequences: List[List[int]], 
                                        rewards: List[float], total_rounds: int, round_num: int, threshold_type, tau):

        if len(sequences) < 30:  # Need more data before trying models
            return [], []
        
        # Encoding
        X = self.context_window_encoding(sequences, context_window=8, embed_dim=16)
        y = np.array(rewards)
        
        
        # *** Remove outliers for more stable training ***
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

        # Set a dynamic R2 threshold for model acceptance. In early rounds,
        # a negative R2 is acceptable as a starting point.
        #threshold = -0.2 if round_num <= 3 else 0.0
        #threshold = get_dynamic_threshold1(round_num, total_rounds)
        if threshold_type == 'fixed': 
            threshold = tau

        else:
            start_threshold = -0.3  # Beginning threshold
            end_threshold = tau     # Final threshold
            start_round = round(total_rounds / 10)
            threshold_increase_constant = 0.01
            # Linear interpolation based on progress
            if round_num < start_round:
                threshold = start_threshold
            else:
                progress = (round_num - 1) / (max(1, total_rounds - 1))
                threshold = min(end_threshold, start_threshold + (round_num - start_round) * threshold_increase_constant)
                #threshold = start_threshold + (end_threshold - start_threshold) * progress
            
        print(f"Current R2 threshold: {threshold}")

        # Store the threshold
        self.threshold_history.append((round_num, threshold))
    
        for name, model in model_candidates:
            try:
                # Use cross-validation to get a robust estimate of the model's R2 score.
                # A smaller number of folds is used for smaller datasets to prevent errors.
                cv_folds = min(5, len(y_clean) // 10)
                
                scores = cross_val_score(model, X_clean, y_clean, 
                                        cv=cv_folds, scoring='r2')
                mean_score = scores.mean()
                
                print(f"  {name}: R2 = {mean_score:.3f} (std: {scores.std():.3f})")
                
                r2_scores.append(mean_score)
                
                
                
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
                print(f"  Fallback: Using {name} with R2 = {r2_scores[best_idx]:.3f}")
        
        return reliable_models, r2_scores



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
    def train_round(self, oracle_fn, metrics_tracker: LearningMetricsTracker, total_rounds: int, 
                round_num: int = 0, exploration_rate: float = 0, method = 'average', threshold_type = 'fixed', 
                tau = '0.2', diversity_penalty = "yes", purePPO = False) -> Dict:
        
        print(f"[{round_num}/{total_rounds}] New Round running", file=sys.__stdout__)
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
        # COUNT ORACLE CALLS HERE
        oracle_calls_this_round = 0
        


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
            oracle_calls_this_round += 1  # <-- COUNT EACH CALL
        
        # Track the calls
        current_best = max([r for _, r in self.all_data]) if self.all_data else 0
        self.track_oracle_call(round_num, oracle_calls_this_round, current_best)

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
        
        # # ========== PHASE 6: IMPROVED SURROGATE MODEL TRAINING ==========
        if purePPO == False:
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
                    all_sequences, all_rewards, total_rounds, round_num, threshold_type = threshold_type, tau = tau
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
                    print(f"Best R2: {best_r2:.3f}, Mean R2: {mean_r2:.3f}")
                    
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
                            virtual_sequences, reliable_models, total_rounds, round_num, method = method
                        )
                        
                        # Only apply diversity penalty if models are good
                        if best_r2 > 0 and diversity_penalty == 'yes':
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
                        

                        # After getting predicted_rewards, calculate accuracy
                        if reliable_models and virtual_sequences:
                            # Get actual rewards for accuracy calculation
                            actual_rewards = [oracle_fn(seq) for seq in virtual_sequences[:10]]  # Sample
                            predicted_sample = predicted_rewards[:10]
                            
                            # Calculate prediction errors
                            errors = [abs(a - p) for a, p in zip(actual_rewards, predicted_sample)]
                            mean_error = np.mean(errors)
                            
                            # Add to tracking
                            if hasattr(self, 'model_performance_history'):
                                if 'prediction_errors' in self.model_performance_history:
                                    self.model_performance_history['prediction_errors'].append(mean_error)
                
                else:
                    print(f"\nNo reliable models found. Skipping model-based training.")
            
            else:
                print(f"\nInsufficient data ({len(self.all_data)} < {min_data_for_models}). "
                    f"Skipping surrogate models.")
        
        # ========== PHASE 8: ANALYZE PROGRESS ==========
        # Re-evaluate with oracle for accurate statistics
        oracle_rewards_clean = [oracle_fn(seq) for seq in sequences]
        if purePPO == True:
            model_rewards = []
            models_used = []
            model_r2_scores = []

        
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
    

    def plot_model_weight_evolution(self, save_path: Optional[str] = None):
        """Create stacked area chart showing weight distribution over time"""
        
        if not hasattr(self, 'model_performance_history'):
            print("No model performance history available")
            return
        
        history = self.model_performance_history
        if not history['rounds']:
            print("No tracking data available")
            return
        
        import matplotlib.pyplot as plt
        import numpy as np
        from collections import defaultdict, OrderedDict
        
        # Get all unique rounds and model types
        all_model_types = set()
        rounds_data = OrderedDict()
        
        for i, round_num in enumerate(history['rounds']):
            if round_num not in rounds_data:
                rounds_data[round_num] = defaultdict(float)
            
            names = history['model_names'][i]
            weights = history['weights'][i]
            
            for name, weight in zip(names, weights):
                model_type = name.split('-')[0]
                all_model_types.add(model_type)
                rounds_data[round_num][model_type] += weight
        
        # Convert to consistent arrays
        unique_rounds = sorted(rounds_data.keys())
        model_types = sorted(list(all_model_types))
        
        # Create weight matrix with zeros for missing values
        weights_matrix = []
        for model_type in model_types:
            model_weights = []
            for round_num in unique_rounds:
                weight = rounds_data[round_num].get(model_type, 0.0)
                model_weights.append(weight)
            weights_matrix.append(model_weights)
        
        # Convert to numpy array
        weights_array = np.array(weights_matrix)
        
        # Create plots
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))
        
        # 1. Stacked area chart of weights
        colors = plt.cm.Set3(np.linspace(0, 1, len(model_types)))
        ax1.stackplot(unique_rounds, weights_array, labels=model_types, colors=colors, alpha=0.8)
        ax1.set_xlabel('Round')
        ax1.set_ylabel('Weight Distribution')
        ax1.set_title('Model Weight Evolution (Stacked Area)')
        ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim(0, 1.1)
        
        # 2. Individual model R² scores over time
        for i, round_num in enumerate(history['rounds']):
            r2_scores = history['r2_scores'][i] if i < len(history['r2_scores']) else []
            names = history['model_names'][i] if i < len(history['model_names']) else []
            
            for name, score in zip(names, r2_scores):
                model_type = name.split('-')[0]
                try:
                    color_idx = model_types.index(model_type)
                    ax2.scatter(round_num, score, color=colors[color_idx], alpha=0.6, s=30)
                except (ValueError, IndexError):
                    continue
        
        ax2.axhline(y=0, color='red', linestyle='--', alpha=0.5)
        ax2.set_xlabel('Round')
        ax2.set_ylabel('R² Score')
        ax2.set_title('Individual Model R² Scores')
        ax2.grid(True, alpha=0.3)
        ax2.set_ylim(-1, 1)
        
        # 3. FIX: Handle prediction errors properly
        if 'prediction_errors' in history and history['prediction_errors']:
            # Match the length of rounds with errors
            error_data = history['prediction_errors']
            
            # If prediction_errors is longer than unique_rounds, truncate it
            if len(error_data) > len(unique_rounds):
                error_data = error_data[:len(unique_rounds)]
            
            # If prediction_errors is shorter, only use corresponding rounds
            rounds_with_errors = unique_rounds[:len(error_data)]
            
            # Now both arrays have the same length
            ax3.plot(rounds_with_errors, error_data, 
                    'b-', linewidth=2, marker='o', markersize=6, label='Prediction Error')
            ax3.set_xlabel('Round')
            ax3.set_ylabel('Mean Absolute Error')
            ax3.set_title('Prediction Accuracy Over Time')
            ax3.grid(True, alpha=0.3)
            ax3.legend()
            # Note: Not inverting y-axis as lower error is visually intuitive at bottom
        else:
            # Alternative: Show individual model type weights over time
            for i, model_type in enumerate(model_types):
                model_weights_line = []
                for round_num in unique_rounds:
                    weight = rounds_data[round_num].get(model_type, 0.0)
                    model_weights_line.append(weight)
                ax3.plot(unique_rounds, model_weights_line, 
                        color=colors[i], linewidth=2, label=model_type, 
                        marker='o', markersize=4, alpha=0.7)
            ax3.set_xlabel('Round')
            ax3.set_ylabel('Model Weight')
            ax3.set_title('Individual Model Type Weights Over Time')
            ax3.legend(loc='best', fontsize=8, ncol=2)
            ax3.grid(True, alpha=0.3)
            ax3.set_ylim(-0.05, 1.05)
        

        # Create detailed configuration text
        config_text = "Experiment Configuration:\n"
        config_text += "─" * 25 + "\n"
        
        # Core parameters
        config_text += f"• Batch Size: {self.batch_size}\n"
        config_text += f"• Max Rounds: {self.max_total_rounds}\n"
        config_text += f"• Sequence Length: {self.max_seq_len}\n"
        config_text += f"• Vocab Size: {self.vocab_size}\n"
        config_text += f"• Model Threshold: {self.model_threshold}\n"
        config_text += f"• Diversity λ: {self.diversity_lambda}\n"
        config_text += f"• Warmup Samples: {self.use_warmup}\n"

        # other parameters
        config_text += f"• Threshold Type: {self.threshold_type}\n"
        config_text += f"• Diversity Penalty: {self.diversity_penalty}\n"


        # Place text box in bottom right corner
        fig.text(0.98, 0.02, config_text, 
                transform=fig.transFigure,
                fontsize=9,
                verticalalignment='bottom',
                horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
                fontfamily='monospace')
        plt.tight_layout()
        
        if save_path:
            save_path = save_path.replace('.png', f'_r{self.max_total_rounds}_b{self.batch_size}_l{self.max_seq_len}.png')
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Model evolution plot saved to {save_path}")
        else:
            plt.show()
        
        # Print summary statistics
        print("\n=== Model Performance Summary ===")
        
        # Final round statistics
        if unique_rounds:
            final_round = unique_rounds[-1]
            final_weights = rounds_data[final_round]
            
            print(f"\nFinal weight distribution (Round {final_round}):")
            for mt in sorted(final_weights.keys(), key=lambda x: -final_weights[x]):
                if final_weights[mt] > 0:
                    print(f"  {mt}: {final_weights[mt]:.3f}")
            
            # Most dominant model types across all rounds
            total_dominance = defaultdict(float)
            for round_data in rounds_data.values():
                for model_type, weight in round_data.items():
                    total_dominance[model_type] += weight
            
            print("\nOverall model importance (average weight across all rounds):")
            for mt in sorted(total_dominance.keys(), key=lambda x: -total_dominance[x]):
                avg_weight = total_dominance[mt] / len(unique_rounds)
                if avg_weight > 0.01:  # Only show models with >1% average weight
                    print(f"  {mt}: {avg_weight:.3f}")
    

        



    