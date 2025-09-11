import numpy as np
import re
import math
import random
from typing import List, Tuple, Dict, Optional

# file import
from DyNAPPO import DyNAPPO
from LearningRateTracker import LearningMetricsTracker


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

    # Initialize tracker
    metrics_tracker = LearningMetricsTracker()

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
        max_model_rounds=M,
        learning_rate=3e-4  # Base learning rate
    )

    """
    Cosine annealing with warm restarts.
    """
    # Learning rate schedule
    def get_learning_rate(round_num: int) -> float:
        
        base_lr = 3e-4
        min_lr = 1e-5
        period = 5  # Restart every 5 rounds
        
        round_in_period = round_num % period
        cos_out = np.cos(np.pi * round_in_period / period)
        lr = min_lr + (base_lr - min_lr) * 0.5 * (1 + cos_out)
        
        return lr
    
    # ALG. 6: for n = 1, 2, ...N do
    for n in range(1, N + 1):
        #Update learning rate
        for param_group in dyna_ppo.optimizer.param_groups:
            current_lr = param_group['lr']
        # current_lr = get_learning_rate(n)
        # for param_group in dyna_ppo.optimizer.param_groups:
        #     param_group['lr'] = current_lr
        
        # Exploration rate schedule
        exploration_rate = max(0.1, 0.5 - (n * 0.05))


        print(f"\n=========== Experiment Round {n}/{N} ===========")
        print(f"Learning Rate: {current_lr:.6f}")
        print(f"Exploration Rate: {exploration_rate:.3f}")
        
        # Execute one round of the algorithm (7-16)
        results = dyna_ppo.train_round_old(oracle_fn, metrics_tracker, n, exploration_rate)

        # Log round-level metrics
        metrics_tracker.log_round_metrics(n, results, current_lr, exploration_rate)
        
        print(f"Round {n} Results:")
        print(f"  Mean Oracle Reward: {results['mean_oracle_reward']:.3f}")
        print(f"  Min Oracle Reward: {results['min_oracle_reward']:.3f}")
        print(f"  Max Oracle Reward: {results['max_oracle_reward']:.3f}")
        print(f"  Standard Dev. Oracle Reward: {results['std_oracle_reward']:.3f}")
        print(f"  Models Used: {results['models_used']}")
        print(f"  Sequence Diversity: {results['sequence_diversity']:.3f}")

        print(f"  Total Sequences Evaluated: {results['total_sequences']}")
    
    print(f"\nDyNA PPO Algorithm Complete!")
    print(f"Total rounds executed: {N}")
    print(f"Total sequences evaluated: {len(dyna_ppo.all_data)}")
    
    # After training, show results
    metrics_tracker.print_summary()
    metrics_tracker.plot_learning_curves(save_path="learning_curves.png")
    metrics_tracker.save_metrics("training_metrics.json")
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
    # Convert numeric sequence [0,1,2,3] to DNA string ['A','T','G','C']
    dna_map = {0: 'A', 1: 'T', 2: 'G', 3: 'C'}
    seq_str = ''.join([dna_map[i] for i in sequence])
    
    score = 0.0  # Initialize total score
    
    # ========== 1. GC CONTENT SCORING ==========
    # Calculate fraction of G and C bases in sequence
    gc_content = (seq_str.count('G') + seq_str.count('C')) / len(seq_str)
    
    # Gaussian penalty: exp(-8(x-0.5)²) creates bell curve peaked at 50% GC
    # At 50% GC: exp(0) = 1.0 (max score)
    # At 0% or 100% GC: exp(-8*0.25) ≈ 0.135 (heavily penalized)
    gc_score = math.exp(-8 * (gc_content - 0.5)**2)
    score += gc_score * 4  # Weight this component by 4
    
    # ========== 2. BIOLOGICAL MOTIF DETECTION ==========
    # Dictionary of important DNA patterns and their rewards
    motifs = {
        'GAATTC': 4.0,   # EcoRI restriction site - very valuable for cloning
        'GGATCC': 3.5,   # BamHI restriction site - another cloning tool
        'GGCC': 2.0,     # Generic 4-cutter restriction site
        'TATA': 2.0,     # TATA box - promoter element
        'ATCG': 1.0,     # Generic motif showing sequence diversity
        'GC': 0.3,       # Simple GC pair - slightly favorable
    }
    
    # Track which positions we've already counted to prevent double-rewarding
    used_positions = set()
    
    # Process motifs from longest to shortest (greedy approach)
    for motif, reward in sorted(motifs.items(), key=lambda x: -len(x[0])):
        start = 0
        while True:
            # Find next occurrence of this motif
            pos = seq_str.find(motif, start)
            if pos == -1:  # No more occurrences
                break
            
            # Check if any position in this motif was already used
            positions = set(range(pos, pos + len(motif)))
            if not positions.intersection(used_positions):
                # New motif found! Add reward and mark positions as used
                score += reward
                used_positions.update(positions)
            start = pos + 1  # Continue searching after this position
    
    # ========== 3. POSITION-DEPENDENT SCORING ==========
    # Different positions in DNA sequence prefer different bases
    for i, base in enumerate(seq_str):
        # Calculate relative position (0=start, 0.5=middle, 1=end)
        position_ratio = i / (len(seq_str) - 1) if len(seq_str) > 1 else 0.5
        
        if base in 'GC':
            # GC bases preferred at ends (0, 1) more than middle (0.5)
            # U-shaped function: high at ends, low in middle
            pos_score = 0.5 * (1 - 4 * (position_ratio - 0.5)**2)
        else:  # AT bases
            # AT bases preferred in middle more than ends
            # Inverted U-shape: high in middle, low at ends
            pos_score = 0.3 * (1 - 4 * (position_ratio - 0.5)**2)
        
        score += pos_score
    
    # ========== 4. REPETITIVE SEQUENCE PENALTY ==========
    def calculate_repeat_penalty(s: str) -> float:
        penalty = 0
        # Check for repeating units of length 1-3
        for length in range(1, 4):  # unit lengths: 1, 2, or 3
            for i in range(len(s) - length):
                if i + 2*length <= len(s):  # Need at least 2 copies
                    unit = s[i:i+length]  # Extract the unit
                    count = 1
                    j = i + length
                    
                    # Count consecutive repetitions of this unit
                    while j + length <= len(s) and s[j:j+length] == unit:
                        count += 1
                        j += length
                    
                    # Penalize if unit repeats 3+ times
                    # e.g., "AAA" (3 A's) gets penalty = (3-2)*1*0.3 = 0.3
                    # e.g., "GCGCGC" (3 GC's) gets penalty = (3-2)*2*0.3 = 0.6
                    if count >= 3:
                        penalty += (count - 2) * length * 0.3
        return penalty
    
    penalty = calculate_repeat_penalty(seq_str)
    score -= penalty  # Subtract penalty from score
    
    # ========== 5. LOCAL COMPLEXITY ANALYSIS ==========
    window_size = 4  # Analyze complexity in 4-base windows
    if len(seq_str) >= window_size:
        complexities = []
        
        # Slide window across sequence
        for i in range(len(seq_str) - window_size + 1):
            window = seq_str[i:i+window_size]
            unique_bases = len(set(window))  # Count unique bases in window
            complexities.append(unique_bases / 4)  # Normalize to [0,1]
        
        # Calculate average complexity and its variance
        avg_complexity = sum(complexities) / len(complexities)
        complexity_variance = sum((c - avg_complexity)**2 for c in complexities) / len(complexities)
        
        score += avg_complexity * 3      # Reward high average complexity
        score -= complexity_variance * 2  # Penalize inconsistent complexity
    
    # ========== 6. DINUCLEOTIDE PREFERENCES ==========
    # Some 2-base combinations are more/less desirable
    dinuc_scores = {
        'CG': 0.2,   # CpG - important for gene regulation
        'GC': 0.2,   # Stable pairing
        'GA': 0.1,   # Purine-purine
        'TC': 0.1,   # Pyrimidine-pyrimidine
        'AA': -0.2,  # Can cause DNA bending
        'TT': -0.2,  # Can cause DNA bending
    }
    
    # Score all consecutive base pairs
    for i in range(len(seq_str) - 1):
        dinuc = seq_str[i:i+2]
        score += dinuc_scores.get(dinuc, 0)  # Add score if in dict, else 0
    
    # ========== 7. MELTING TEMPERATURE ESTIMATION ==========
    # Rough Tm calculation: 4°C per GC pair, 2°C per AT pair
    tm_simple = 4 * (seq_str.count('G') + seq_str.count('C')) + 2 * (seq_str.count('A') + seq_str.count('T'))
    
    # Normalize to approximately [0,1] range
    # For 14-base sequence: min Tm=28 (all AT), max Tm=56 (all GC)
    tm_normalized = (tm_simple - 20) / 40
    score += tm_normalized * 2  # Weight by 2
    
    # ========== 8. EXPERIMENTAL NOISE ==========
    # Add Gaussian noise to simulate real-world measurement variability
    # Mean=0, StdDev=0.15 adds realistic uncertainty
    score += random.gauss(0, 0.15)
    
    # Ensure final score is non-negative
    return max(0, score)



if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING COMPLETE ALGORITHM 1: DyNA PPO")
    print("=" * 60)
    
    trained_dyna_ppo = run_dyna_ppo_algorithm(
        oracle_fn=dna_oracle,
        vocab_size=4,  # DNA: A, T, G, C  
        max_seq_len=8,
        N=10,  # Number of experiment rounds
        M=5,   # Number of model-based training rounds  
        tau=0.1,  # Minimum model score threshold
        batch_size=32
    )
    
    # Generate some final sequences
    print("\nFinal optimized sequences generated (from the policy trained):")
    for i in range(5):
        seq = trained_dyna_ppo.generate_sequence(deterministic=False)
        reward = dna_oracle(seq)
        dna_seq = ''.join(['ATGC'[j] for j in seq])
        print(f"  {dna_seq}: {reward:.3f}")
    
    print("\n" + "=" * 60)