import numpy as np
import re
import math
import random
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



# """Example oracle function - optimize for specific patterns."""
# def dna_oracle(sequence: List[int]) -> float:
#     # Convert to string for pattern matching
#     dna_map = {0: 'A', 1: 'T', 2: 'G', 3: 'C'}
#     seq_str = ''.join([dna_map[i] for i in sequence])
    
#     # Scoring component 1: GC content (biological relevance)
#     # High GC content often means stronger DNA binding
#     gc_content = (seq_str.count('G') + seq_str.count('C')) / len(seq_str)

#     # Scoring component 2: Specific motif reward
#     # Rewards sequences containing "ATCG" pattern
#     motif_bonus = seq_str.count('ATCG') * 2  # Bonus for specific motif
    
#     a_content = seq_str.count('A')

#     # Final score with realistic noise
#     return a_content

def dna_oracle(sequence: List[int]) -> float:
    """Advanced oracle with more nuanced scoring."""
    # Convert to string
    dna_map = {0: 'A', 1: 'T', 2: 'G', 3: 'C'}
    seq_str = ''.join([dna_map[i] for i in sequence])
    
    score = 0.0
    
    # 1. GC content with smoother penalty
    gc_content = (seq_str.count('G') + seq_str.count('C')) / len(seq_str)
    # Gaussian-like penalty centered at 0.5
    gc_score = math.exp(-8 * (gc_content - 0.5)**2)
    score += gc_score * 4
    
    # 2. Hierarchical motif rewards (avoid double counting)
    motifs = {
        'GAATTC': 4.0,   # EcoRI site (6bp)
        'GGATCC': 3.5,   # BamHI site
        'GGCC': 2.0,     # Shorter restriction site
        'TATA': 2.0,     # TATA box
        'ATCG': 1.0,     # Generic motif
        'GC': 0.3,       # Simple GC pair
    }
    
    # Mark positions already counted to avoid overlap
    used_positions = set()
    for motif, reward in sorted(motifs.items(), key=lambda x: -len(x[0])):
        start = 0
        while True:
            pos = seq_str.find(motif, start)
            if pos == -1:
                break
            # Check if positions are not already used
            positions = set(range(pos, pos + len(motif)))
            if not positions.intersection(used_positions):
                score += reward
                used_positions.update(positions)
            start = pos + 1
    
    # 3. Progressive position scoring (gradient from start to end)
    for i, base in enumerate(seq_str):
        # Prefer GC at start, AT at middle, GC at end
        position_ratio = i / (len(seq_str) - 1) if len(seq_str) > 1 else 0.5
        
        if base in 'GC':
            # U-shaped preference for GC
            pos_score = 0.5 * (1 - 4 * (position_ratio - 0.5)**2)
        else:  # AT
            # Inverse U-shaped for AT
            pos_score = 0.3 * (1 - 4 * (position_ratio - 0.5)**2)
        
        score += pos_score
    
    # 4. Sophisticated repeat penalty
    def calculate_repeat_penalty(s: str) -> float:
        penalty = 0
        for length in range(1, 4):  # Check 1-3 base repeats
            for i in range(len(s) - length):
                if i + 2*length <= len(s):
                    unit = s[i:i+length]
                    count = 1
                    j = i + length
                    while j + length <= len(s) and s[j:j+length] == unit:
                        count += 1
                        j += length
                    
                    if count >= 3:  # Penalty for 3+ repeats
                        penalty += (count - 2) * length * 0.3
        return penalty
    
    score -= calculate_repeat_penalty(seq_str)
    
    # 5. Local complexity (sliding window)
    window_size = 4
    if len(seq_str) >= window_size:
        complexities = []
        for i in range(len(seq_str) - window_size + 1):
            window = seq_str[i:i+window_size]
            unique_bases = len(set(window))
            complexities.append(unique_bases / 4)
        
        # Reward consistent moderate complexity
        avg_complexity = sum(complexities) / len(complexities)
        complexity_variance = sum((c - avg_complexity)**2 for c in complexities) / len(complexities)
        
        score += avg_complexity * 3  # Reward complexity
        score -= complexity_variance * 2  # Penalize high variance
    
    # 6. Dinucleotide preferences (some are more stable)
    dinuc_scores = {
        'CG': 0.2,   # CpG islands
        'GC': 0.2,
        'GA': 0.1,
        'TC': 0.1,
        'AA': -0.2,  # Poly-A tendency
        'TT': -0.2,  # Poly-T tendency
    }
    
    for i in range(len(seq_str) - 1):
        dinuc = seq_str[i:i+2]
        score += dinuc_scores.get(dinuc, 0)
    
    # 7. Melting temperature approximation
    # Higher Tm often means more stable binding
    tm_simple = 4 * (seq_str.count('G') + seq_str.count('C')) + 2 * (seq_str.count('A') + seq_str.count('T'))
    tm_normalized = (tm_simple - 20) / 40  # Normalize to ~[0,1]
    score += tm_normalized * 2
    
    # 8. Add controlled noise
    score += random.gauss(0, 0.15)

    #***** Oracle Balance
    
    
    return max(0, score)  # Ensure non-negative



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