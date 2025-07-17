import numpy as np
from typing import List, Tuple, Dict, Optional

# file import
from DyNAPPO import DyNAPPO

"""
Run DyNA PPO

Args:
    oracle_fn: The true function f(x) to optimize
    vocab_size: Size of vocabulary 
    max_seq_len: Maximum sequence length T
    N: Number of experiment rounds (alg. 1)
    M: Number of model-based training rounds (alg. 2)
    tau: Minimum model score τ for model-based training (alg. 4)
    batch_size: Number of sequences per batch B
"""
def run_dyna_ppo_algorithm(oracle_fn, vocab_size: int, max_seq_len: int, N: int = 10, M: int = 10, tau: float = 0.5, batch_size: int = 32):

    # ALGORITHM INPUTS (1-5)
    print(f"Algorithm 1: DyNA PPO")
    print(f"Input: Number of experiment rounds N = {N}")
    print(f"Input: Number of model-based training rounds M = {M}")
    print(f"Input: Minimum model score τ = {tau}")
    print(f"Input: Batch size B = {batch_size}")
    
    # Initialize DyNA PPO with policy π_θ
    dyna_ppo = DyNAPPO(
        vocab_size=vocab_size,
        max_seq_len=max_seq_len,
        batch_size=batch_size,
        model_threshold=tau,
        max_model_rounds=M
    )
    
    # ALG. 6: for n = 1, 2, ...N do
    for n in range(1, N + 1):
        print(f"\n=== Experiment Round {n}/{N} ===")
        
        # Execute one round of the algorithm (7-16)
        results = dyna_ppo.train_round(oracle_fn, n)
        
        print(f"Round {n} Results:")
        print(f"  Mean Oracle Reward: {results['mean_oracle_reward']:.3f}")
        print(f"  Max Oracle Reward: {results['max_oracle_reward']:.3f}")
        print(f"  Models Used: {results['models_used']}")
        print(f"  Total Sequences Evaluated: {results['total_sequences']}")
    
    print(f"\nDyNA PPO Algorithm Complete!")
    print(f"Total rounds executed: {N}")
    print(f"Total sequences evaluated: {len(dyna_ppo.all_data)}")
    
    return dyna_ppo



"""Example oracle function - optimize for specific patterns."""
def dna_oracle(sequence: List[int]) -> float:
    # Convert to string for pattern matching
    dna_map = {0: 'A', 1: 'T', 2: 'G', 3: 'C'}
    seq_str = ''.join([dna_map[i] for i in sequence])
    
    # Scoring component 1: GC content (biological relevance)
    # High GC content often means stronger DNA binding
    gc_content = (seq_str.count('G') + seq_str.count('C')) / len(seq_str)

    # Scoring component 2: Specific motif reward
    # Rewards sequences containing "ATCG" pattern
    motif_bonus = seq_str.count('ATCG') * 2  # Bonus for specific motif
    
    a_content = seq_str.count('A')

    # Final score with realistic noise
    return a_content




if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING COMPLETE ALGORITHM 1: DyNA PPO")
    print("=" * 60)
    
    trained_dyna_ppo = run_dyna_ppo_algorithm(
        oracle_fn=dna_oracle,
        vocab_size=4,  # DNA: A, T, G, C  
        max_seq_len=14,
        N=10,  # Number of experiment rounds
        M=5,   # Number of model-based training rounds  
        tau=0.1,  # Minimum model score threshold
        batch_size=128
    )
    
    # Generate some final sequences
    print("\nFinal optimized sequences:")
    for i in range(5):
        seq = trained_dyna_ppo.generate_sequence(deterministic=True)
        reward = dna_oracle(seq)
        dna_seq = ''.join(['ATGC'[j] for j in seq])
        print(f"  {dna_seq}: {reward:.3f}")
    
    print("\n" + "=" * 60)