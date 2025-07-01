#   FILE: PolicyNetwork.py
#   PROJECT: Optimal Ensemble Weights DyNA PPO
#   AUTHOR: Eric Lin
#   This file contains the reinforcement learning policy gradient network part of the project.


import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List, Tuple, Dict, Optional
import math

class PolicyNetwork(nn.Module):
    """Autoregressive policy network for sequence generation."""
    
    def __init__(self, vocab_size: int, max_seq_len: int, context_window: int = 8, 
                 hidden_dim: int = 256, embed_dim: int = 64):
        super().__init__()
        self.vocab_size = vocab_size
        self.max_seq_len = max_seq_len
        self.context_window = context_window
        self.embed_dim = embed_dim
        
        # Character embedding
        self.char_embedding = nn.Embedding(vocab_size, embed_dim)
        
        # Positional encoding
        self.pos_encoding = self._create_positional_encoding(max_seq_len, embed_dim)
        
        # Input dimension: context_window * embed_dim + embed_dim (for position)
        input_dim = context_window * embed_dim + embed_dim
        
        # Policy network
        self.policy_net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, vocab_size)
        )
        
        # Value network
        self.value_net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1)
        )
    
    def _create_positional_encoding(self, max_len: int, embed_dim: int) -> torch.Tensor:
        """Create sinusoidal positional encoding."""
        pe = torch.zeros(max_len, embed_dim)
        position = torch.arange(0, max_len).unsqueeze(1).float()
        div_term = torch.exp(torch.arange(0, embed_dim, 2).float() * 
                           -(math.log(10000.0) / embed_dim))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        return pe
    
    def _get_context_input(self, sequences: torch.Tensor, positions: torch.Tensor) -> torch.Tensor:
        """Get context input for the network."""
        batch_size = sequences.size(0)
        context_inputs = []
        
        for i in range(batch_size):
            seq = sequences[i]
            pos = positions[i].item()
            
            # Get context window
            start_idx = max(0, pos - self.context_window)
            context = seq[start_idx:pos]
            
            # Pad if necessary
            if len(context) < self.context_window:
                padding = torch.zeros(self.context_window - len(context), dtype=torch.long)
                context = torch.cat([padding, context])
            
            # Embed characters
            context_embed = self.char_embedding(context).flatten()
            
            # Add positional encoding
            pos_embed = self.pos_encoding[pos]
            
            # Combine
            input_vec = torch.cat([context_embed, pos_embed])
            context_inputs.append(input_vec)
        
        return torch.stack(context_inputs)
    
    def forward(self, sequences: torch.Tensor, positions: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Forward pass."""
        context_input = self._get_context_input(sequences, positions)
        
        # Policy output
        policy_logits = self.policy_net(context_input)
        policy_probs = F.softmax(policy_logits, dim=-1)
        
        # Value output
        values = self.value_net(context_input).squeeze(-1)
        
        return policy_probs, values