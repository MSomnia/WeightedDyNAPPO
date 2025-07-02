#   FILE: PolicyNetwork.py
#   PROJECT: Optimal Ensemble Weights DyNA PPO
#   AUTHOR: Eric Lin
#   This file contains the reinforcement learning policy gradient network part of the project.


import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List, Tuple, Dict, Optional
import math


"""
Autoregressive policy network for sequence generation.
"""
class PolicyNetwork(nn.Module):
    # vocab_size: the number of unique characters in the vocabulary
    # max_seq_len: the maximum possible length of a sequence
    # context_window: the number of previous characters the model looks at to predct the next one
    # hidden_dim: the number of neurons in the hidden layers of the networks
    # embed_dim: the size of the vector used to represent each character
    def __init__(self, vocab_size: int, max_seq_len: int, context_window: int = 8, 
                 hidden_dim: int = 256, embed_dim: int = 64):
        
        super().__init__()
        self.vocab_size = vocab_size
        self.max_seq_len = max_seq_len
        self.context_window = context_window
        self.embed_dim = embed_dim
        

        # Character embedding
        # Create an embedding layer. This layer is a lookup table that maps each character's integer index to a dense vector of size "embed_dim"
        self.char_embedding = nn.Embedding(vocab_size, embed_dim)
        
        # Positional encoding
        # Generate a tensor that contains information about the position of each character in the sequence.
        self.pos_encoding = self._create_positional_encoding(max_seq_len, embed_dim)
        
        # Input dimension: context_window * embed_dim + embed_dim (for position)
        # Calculate the total size of the input vector that will be fed into the policy and value networks.
        # The sum of the flattened context embedding and the positional encoding vector.
        input_dim = context_window * embed_dim + embed_dim
        
        # Policy network
        # Take the combined context and position input and outputs a score for each possible next character in the vocabulary
        self.policy_net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),   # the first linear layer
            nn.ReLU(),  # a non-linear activation function
            nn.Linear(hidden_dim, hidden_dim),  # the hidden layer
            nn.ReLU(),  # a non-linear activation function
            nn.Linear(hidden_dim, vocab_size)   # the final output layer. It produces one score for each character in the vocabulary
        )
        
        # Value network
        self.value_net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),   # the first linear layer
            nn.ReLU(),  # a non-linear activation function
            nn.Linear(hidden_dim, hidden_dim),  # the hidden layer
            nn.ReLU(),  # a non-linear activation function
            nn.Linear(hidden_dim, 1)    # It produces a single number that estimates the value/goodness of the current state (the sequence so far).
        )
    
    """
    A helper function for generating the sinusoidal positional encoding tensor using sine and cosine functions of different frequencies.
    """
    def _create_positional_encoding(self, max_len: int, embed_dim: int) -> torch.Tensor:
        # Create an empty tensor of shape (max_len, embed_dim) to store the encodings
        pe = torch.zeros(max_len, embed_dim)
        # create a column vector with values from 0 and max_len - 1, representing the positions
        position = torch.arange(0, max_len).unsqueeze(1).float()
        # calculate the divisor term used in the sinusoidal formulas. It creates different wavelengths for the sine and cosine functions
        div_term = torch.exp(torch.arange(0, embed_dim, 2).float() * -(math.log(10000.0) / embed_dim))
        # calculate the sine values for even indices of the embedding dimension
        pe[:, 0::2] = torch.sin(position * div_term)
        # calculate the cosine values for odd indices of the embedding dimension
        pe[:, 1::2] = torch.cos(position * div_term)
        # return the final positional encoding tensor
        return pe
    
    """
    A helper function for preparing the input tensor for the neural networks for a batch of sequences
    """
    def _get_context_input(self, sequences: torch.Tensor, positions: torch.Tensor) -> torch.Tensor:
        batch_size = sequences.size(0)
        context_inputs = []
        
        # loop through each sequence in the input batch
        for i in range(batch_size):
            seq = sequences[i]
            pos = positions[i].item()
            
            # Get context window
            # determine the starting index of the context window
            start_idx = max(0, pos - self.context_window)
            # extract the recent characters from the sequence
            context = seq[start_idx:pos]
            
            # Pad if necessary
            # check if the extracted context is shorter than the required window size
            if len(context) < self.context_window:
                # create a padding tensor of zeros
                padding = torch.zeros(self.context_window - len(context), dtype=torch.long)
                # prepend the padding to the context so it has a consistent length
                context = torch.cat([padding, context])
            
            # Embed characters
            # convert the context characters into their embedding vectors and then flatten them into a single one dimensional vector
            context_embed = self.char_embedding(context).flatten()
            
            # Add positional encoding
            # retrieve the positional encoding vector for the current poisition
            pos_embed = self.pos_encoding[pos]
            
            # Combine
            # concatenate the context embedding and the positional embedding to form the final input vector for this sequence
            input_vec = torch.cat([context_embed, pos_embed])
            context_inputs.append(input_vec)
        
        # stack the input vectors from all sequences in the batch into a single tensor
        return torch.stack(context_inputs)
    

    """
    Define the forward pass
    """
    def forward(self, sequences: torch.Tensor, positions: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        # process the raw sequence and position data into the final input tensor
        context_input = self._get_context_input(sequences, positions)
        
        # Policy output
        # pass the input tensor through the policy network to get the raw output scores for the next character
        policy_logits = self.policy_net(context_input)
        # apply the softmax function to the policy logits. It converts the scores into a probability distribution (all sum to 1).
        # this represents the probability of each character being the next one.
        # *** This computes π_θ(a_t|s_t) for ONE specific s_t
        policy_probs = F.softmax(policy_logits, dim=-1)
        
        # Value output
        # pass the same input tensor through the value network to get the state value.
        # squeeze to remove the last dimension of the output, turning it from a tensor of shape (batch_size, 1) to batch_size
        values = self.value_net(context_input).squeeze(-1)
        
        # return the final calculated probabilities for the next action and the estimated value of the current state.
        # *** returns probability distribution over all possible a_t
        return policy_probs, values