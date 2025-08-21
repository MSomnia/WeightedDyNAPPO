#   FILE: SequenceUtils.py
#   PROJECT: Optimal Ensemble Weights DyNA PPO
#   AUTHOR: Eric Lin
#   

import numpy as np
from typing import List, Tuple, Dict, Optional

"""
Convert sequences to feature vectors for surrogate models
"""
def sequence_to_features(sequences: List[List[int]], vocab_size: int) -> np.ndarray:
    features = []

    for seq in sequences:
        # ----- One-hot encoding -----
        # Create a zero-filled array with size: sequence_length * vocabulary_size
        feature = np.zeros(len(seq) * vocab_size)
        # Loop through each token in the current sequence
        for i, token in enumerate(seq):
            # Set the appropriate position to 1 for one-hot encoding
            # Position calculated as: token_position * vocab_size + token_value
            feature[i * vocab_size + token] = 1
        features.append(feature)
    return np.array(features)


"""
Compute edit distance between two sequences
counting the minimum number of changes needed to transform one into the other
"""
def edit_distance(seq1: List[int], seq2: List[int]) -> int:
    m, n = len(seq1), len(seq2)

    # dp[i][j] will store edit distance between first i chars of seq1 and first j chars of seq2
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first column: distance from empty string to seq1 prefixes
    # This represents inserting i characters
    for i in range(m + 1):
        dp[i][0] = i
    # Initialize first row: distance from empty string to seq2 prefixes
    # This represents inserting j characters
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match, no operation needed - take diagonal value
            if seq1[i-1] == seq2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Characters don't match - take minimum of three operations + 1
                # dp[i-1][j] + 1: deletion from seq1
                # dp[i][j-1] + 1: insertion into seq1
                # dp[i-1][j-1] + 1: substitution
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[m][n]


"""
Compute diversity penalty based on sequence history
Discourages generating sequences that are too similar to ones already created.
"""
def compute_diversity_penalty(sequence: List[int], history: List[List[int]], lambda_penalty: float = 0.1, epsilon: int = 2) -> float:
    penalty = 0.0

    # Loop through each previously generated sequence in history
    for hist_seq in history:
        # Calculate how different the current sequence is from this historical one
        distance = edit_distance(sequence, hist_seq)
        if distance <= epsilon:
            # Calculate penalty weight using linear decay
            # Weight decreases as distance increases, reaching 0 when distance = epsilon
            weight = max(0, 1 - distance / epsilon)  # Linear decay
            # Add weighted penalty to total
            penalty += weight
    return lambda_penalty * penalty

"""
Compute diversity ratio of sequences.
Helper function to compute sequence diversity
"""
def compute_sequence_diversity(sequences: List[List[int]]) -> float:
    if not sequences:
        return 0.0
    unique_sequences = len(set(tuple(seq) for seq in sequences))
    return unique_sequences / len(sequences)