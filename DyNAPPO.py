#   FILE: DyNAPPO.py
#   PROJECT: Optimal Ensemble Weights DyNA PPO
#   AUTHOR: Eric Lin
#   

import numpy as np
import torch.optim as optim
from typing import List, Tuple, Dict, Optional
from SurrogateModel import SurrogateModel
from PolicyNetwork import PolicyNetwork

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


    """
    Create a pool of surrogate models with different complexities
    """
    def create_surrogate_models(self) -> List[SurrogateModel]:
        
        models = []
        
        # Random Forest
        models.append(SurrogateModel('rf', n_estimators=50, max_depth=5))
        models.append(SurrogateModel('rf', n_estimators=100, max_depth=10))
        models.append(SurrogateModel('rf', n_estimators=200, max_depth=None))
        
        # Gradient Boosting
        models.append(SurrogateModel('gb', n_estimators=50, max_depth=3))
        models.append(SurrogateModel('gb', n_estimators=100, max_depth=5))
        
        # Other
        models.append(SurrogateModel('knn', n_neighbors=5))
        models.append(SurrogateModel('knn', n_neighbors=10))
        models.append(SurrogateModel('ridge'))
        
        return models