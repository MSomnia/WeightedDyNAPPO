import numpy as np
import re
import math
import random
from typing import List, Tuple, Dict, Optional
import torch
import time
from datetime import datetime
from pathlib import Path
import sys

# file import
from DyNAPPO import DyNAPPO
from LearningRateTracker import LearningMetricsTracker

input_l = 10
input_r = 200
input_b = 32
input_m = "weighted"        # # ['average', 'weighted', 'dynamic']
input_ty = "dynamic"    # threshold mode

time_str = datetime.now().strftime("%Y%m%d%H%M%S")
base_dir = Path("experiments")
dir_path = base_dir / f"{time_str}_r{input_r}_b{input_b}_l{input_l}_{input_m}_{input_ty}"    
dir_path.mkdir(parents=True, exist_ok=True)

sys.stdout = open(dir_path / "output.txt", "w", encoding="utf-8")
sys.stderr = sys.stdout

"""
Generate diverse random sequences for initial training

The warm-up dataset essentially bootstraps the learning process
giving both the policy network and surrogate models enough initial information to make intelligent decisions rather than random guesses
"""
def create_warmup_dataset(oracle_fn, vocab_size: int, max_seq_len: int, n_samples: int = 50):
    sequences = []
    rewards = []
    
    print(f"Generating {n_samples} warm-up samples...")
    
    for _ in range(n_samples):
        # Randomly select which type of pattern to generate
        # This ensures diversity in the initial dataset
        seq_type = random.random()
        
        if seq_type < 0.25: # 25% chance
            # Type 1: Completely random sequence
            # Provides unbiased exploration of the sequence space
            seq = [random.randint(0, vocab_size - 1) for _ in range(max_seq_len)]
        elif seq_type < 0.5: # 25% chance
            # Type 2: High GC content (biased toward G and C bases)
            # For DNA, this explores sequences with stronger binding properties
            # 70% chance of G or C, 30% chance of A or T at each position
            seq = [random.choice([2, 3] if random.random() < 0.7 else [0, 1]) 
                   for _ in range(max_seq_len)]
        elif seq_type < 0.75: # 25% chance
            # Type 3: High AT content (biased toward A and T bases)
            seq = [random.choice([0, 1] if random.random() < 0.7 else [2, 3]) 
                   for _ in range(max_seq_len)]
        else: # 25% chance
            # Type 4: Alternating/repetitive patterns with noise
            # Creates a random 2-base pattern (like "AG" or "TC")
            pattern = [random.randint(0, vocab_size - 1) for _ in range(2)]
            seq = []
            for i in range(max_seq_len):
                seq.append(pattern[i % len(pattern)])
                if random.random() < 0.3:  # Add some noise
                    seq[-1] = random.randint(0, vocab_size - 1)
        
        sequences.append(seq)
        rewards.append(oracle_fn(seq))
    
    return sequences, rewards


"""
Run improved DyNA PPO with better exploration and model learning

Args:
    oracle_fn: The true function f(x) to optimize
    vocab_size: Size of vocabulary 
    max_seq_len: Maximum sequence length T
    N: Number of experiment rounds
    M: Number of model-based training rounds
    tau: Minimum model score τ for model-based training
    batch_size: Number of sequences per batch B
    use_warmup: Whether to use warm-up phase for initial data
"""
def run_dyna_ppo_algorithm(dir_path, oracle_fn, vocab_size: int, max_seq_len: int, 
                          N: int = 10, M: int = 5, tau: float = 0.2, 
                          batch_size: int = 32, use_warmup: bool = True, method = "average", 
                          threshold_type = 'fixed', diversity_penalty = 'yes', 
                          purePPO = False):

    start_time = time.time()
    
    # Initialize tracker
    metrics_tracker = LearningMetricsTracker()

    # ALGORITHM INPUTS
    print("=" * 70)
    print("IMPROVED DyNA PPO ALGORITHM")
    print("=" * 70)
    print(f"Configuration:")
    print(f"  Number of experiment rounds N = {N}")
    print(f"  Number of model-based training rounds M = {M}")
    print(f"  Minimum model score τ = {tau}")
    print(f"  Batch size B = {batch_size}")
    print(f"  Warm-up phase: {use_warmup}")
    print(f"  Surrogate model method: {method}")
    print("=" * 70)
    
    # Initialize DyNA PPO with policy π_θ
    # Note: Make sure your DyNAPPO class includes all the improved methods
    dyna_ppo = DyNAPPO(
        vocab_size=vocab_size,
        max_seq_len=max_seq_len,
        batch_size=batch_size,
        model_threshold=tau,
        max_total_rounds = N,
        max_model_rounds=M,
        learning_rate=3e-4,
        diversity_lambda=0.1,  # Increased for better exploration
        method = method, 
        threshold_type = threshold_type,
        diversity_penalty = diversity_penalty,
        use_warmup = use_warmup
    )
    
    # ========== WARM-UP PHASE ==========
    if use_warmup:
        print("\n=== WARM-UP PHASE ===")
        warmup_sequences, warmup_rewards = create_warmup_dataset(
            oracle_fn, vocab_size, max_seq_len, n_samples=50
        )
        
        # Add warm-up data to storage
        for seq, reward in zip(warmup_sequences, warmup_rewards):
            dyna_ppo.all_data.append((seq, reward))
            dyna_ppo.sequence_history.append(seq)
        
        print(f"Warm-up statistics:")
        print(f"  Mean reward: {np.mean(warmup_rewards):.3f}")
        print(f"  Std reward: {np.std(warmup_rewards):.3f}")
        print(f"  Min/Max: {np.min(warmup_rewards):.3f} / {np.max(warmup_rewards):.3f}")
        
        # Pre-train surrogate models if using improved version
        if hasattr(dyna_ppo, 'improved_fit_surrogate_models'):
            print("\nPre-training surrogate models on warm-up data...")
            initial_models, initial_scores = dyna_ppo.improved_fit_surrogate_models(
                warmup_sequences, warmup_rewards, N, round_num=0, threshold_type = threshold_type, tau = tau
            )
            print(f"Initial models trained: {len(initial_models)}")
            if initial_scores:
                print(f"Initial R2 scores - Mean: {np.mean(initial_scores):.3f}, "
                      f"Max: {np.max(initial_scores):.3f}")
    
    """Cosine annealing with warm restarts"""
    # Learning rate schedule with cosine annealing
    def get_learning_rate(round_num: int) -> float:
        
        base_lr = 3e-4
        min_lr = 1e-5
        period = 5  # Restart every 5 rounds
        
        round_in_period = round_num % period
        cos_out = np.cos(np.pi * round_in_period / period)
        lr = min_lr + (base_lr - min_lr) * 0.5 * (1 + cos_out)
        
        return lr
    
    # Track best performance
    best_mean_reward = float('-inf')
    best_round = 0
    
    # ========== MAIN TRAINING LOOP ==========
    for n in range(1, N + 1):
        # Update learning rate
        current_lr = get_learning_rate(n)
        for param_group in dyna_ppo.optimizer.param_groups:
            param_group['lr'] = current_lr
        
        # Adaptive exploration rate schedule
        if n <= 3:
            exploration_rate = 0.3  # High exploration early
        elif n <= 7:
            exploration_rate = max(0.15, 0.4 - (n * 0.03))  # Gradual decay
        else:
            exploration_rate = max(0.05, 0.2 - (n * 0.015))  # Low exploration late
        
        print(f"\n{'=' * 70}")
        print(f"EXPERIMENT ROUND {n}/{N}")
        print(f"{'=' * 70}")
        print(f"Learning Rate: {current_lr:.6f}")
        print(f"Exploration Rate: {exploration_rate:.3f}")
        print(f"Total data collected: {len(dyna_ppo.all_data)}")
        
        # Execute one round of the improved algorithm
        results = dyna_ppo.train_round(oracle_fn, metrics_tracker, N, n, exploration_rate, 
                                       method = method, threshold_type=threshold_type, 
                                       tau = tau, diversity_penalty=diversity_penalty, purePPO = purePPO)
        
        # Log round-level metrics
        #metrics_tracker.log_round_metrics(n, results, current_lr, exploration_rate)
        metrics_tracker.log_round_metrics(n, results, current_lr, exploration_rate, 
                                  threshold=dyna_ppo.threshold_history[-1][1] if dyna_ppo.threshold_history else 0)
        
        # Display round results
        print(f"\n--- Round {n} Results ---")
        print(f"  Mean Oracle Reward: {results['mean_oracle_reward']:.3f}")
        print(f"  Min Oracle Reward: {results['min_oracle_reward']:.3f}")
        print(f"  Max Oracle Reward: {results['max_oracle_reward']:.3f}")
        print(f"  Std Oracle Reward: {results['std_oracle_reward']:.3f}")
        print(f"  Sequence Diversity: {results['sequence_diversity']:.3f}")
        print(f"  Models Used: {results['models_used']}")
        
        # Display model R2 scores if available
        if results.get('model_r2_scores'):
            r2_scores = results['model_r2_scores']
            if r2_scores:
                print(f"  Model R2 - Mean: {np.mean(r2_scores):.3f}, "
                      f"Max: {np.max(r2_scores):.3f}, "
                      f"Count: {len(r2_scores)}")
        
        # Track best performance
        if results['mean_oracle_reward'] > best_mean_reward:
            best_mean_reward = results['mean_oracle_reward']
            best_round = n
            print("  New best mean reward!")
        
        print(f"  Total Sequences Evaluated: {results['total_sequences']}")
        print(f"    Oracle Count: {dyna_ppo.oracle_call_count} {dyna_ppo.oracle_call_history}")
        
        # Optional: Early stopping if converged
        # if n > 5:  # Check after initial exploration
        #     recent_rewards = [metrics_tracker.metrics['oracle_mean_reward'][i] 
        #                     for i in range(-min(3, n), 0)]
        #     if len(recent_rewards) >= 3:
        #         reward_variance = np.var(recent_rewards)
        #         if reward_variance < 0.001 and results['mean_oracle_reward'] > 0:
        #             print(f"\n  Early stopping: Converged at round {n}")
        #             break
    
    end_time = time.time()
    time_used = (round(end_time - start_time, 2))
    # ========== TRAINING COMPLETE ==========
    print(f"\n{'=' * 70}")
    print(f"DyNA PPO ALGORITHM COMPLETE! Time used {time_used} seconds")
    print(f"{'=' * 70}")
    print(f"Total rounds executed: {n}")
    print(f"Total sequences evaluated: {len(dyna_ppo.all_data)}")
    print(f"Best mean reward: {best_mean_reward:.3f} (achieved at round {best_round})")
    
    # Display training summary
    metrics_tracker.print_summary()
    
    # Plot and save results
    print("\nGenerating learning curves...")
    # Create configuration dictionary
    experiment_config = {
        'batch_size': batch_size,
        'max_rounds': N,
        'seq_length': max_seq_len,
        'vocab_size': vocab_size,
        'ensemble_method': method,  # or 'uniform', 'ridge', etc.
        'model_threshold': tau,
        'model_rounds': M,
        'learning_rate': 3e-4,
        'diversity_lambda': dyna_ppo.diversity_lambda,
        'warmup_samples': 50 if use_warmup else 0,
        'time_used': time_used,
        'threshold_type': threshold_type,
        'diversity_penalty': diversity_penalty
    }

    # Pass config when plotting
    metrics_tracker.plot_learning_curves(
        save_path=str(dir_path / "metrices_plot.png"),
        experiment_config=experiment_config
    )
    
    print("Saving training metrics...")
    metrics_tracker.save_metrics(filepath=str(dir_path / "metrices_data.json"), experiment_config=experiment_config)
    
    return dyna_ppo

def dna_oracle(sequence: List[int]) -> float:
    """Complex DNA sequence oracle function"""
    dna_map = {0: 'A', 1: 'T', 2: 'G', 3: 'C'}
    seq_str = ''.join([dna_map[i] for i in sequence])
    
    score = 0.0
    
    # 1. GC content scoring (optimal at 50%)
    gc_content = (seq_str.count('G') + seq_str.count('C')) / len(seq_str)
    gc_score = math.exp(-8 * (gc_content - 0.5)**2)
    score += gc_score * 4
    
    # 2. Biological motifs
    motifs = {
        'GAATTC': 4.0,   # EcoRI restriction site
        'GGATCC': 3.5,   # BamHI restriction site
        'GGCC': 2.0,     # Generic 4-cutter
        'TATA': 2.0,     # TATA box
        'ATCG': 1.0,     # Generic motif
        'GC': 0.3,       # GC pair
    }
    
    used_positions = set()
    for motif, reward in sorted(motifs.items(), key=lambda x: -len(x[0])):
        start = 0
        while True:
            pos = seq_str.find(motif, start)
            if pos == -1:
                break
            positions = set(range(pos, pos + len(motif)))
            if not positions.intersection(used_positions):
                score += reward
                used_positions.update(positions)
            start = pos + 1
    
    # 3. Position-dependent scoring
    for i, base in enumerate(seq_str):
        position_ratio = i / (len(seq_str) - 1) if len(seq_str) > 1 else 0.5
        if base in 'GC':
            pos_score = 0.5 * (1 - 4 * (position_ratio - 0.5)**2)
        else:
            pos_score = 0.3 * (1 - 4 * (position_ratio - 0.5)**2)
        score += pos_score
    
    # 4. Repetitive sequence penalty
    def calculate_repeat_penalty(s: str) -> float:
        penalty = 0
        for length in range(1, 4):
            for i in range(len(s) - length):
                if i + 2*length <= len(s):
                    unit = s[i:i+length]
                    count = 1
                    j = i + length
                    while j + length <= len(s) and s[j:j+length] == unit:
                        count += 1
                        j += length
                    if count >= 3:
                        penalty += (count - 2) * length * 0.3
        return penalty
    
    penalty = calculate_repeat_penalty(seq_str)
    score -= penalty
    
    # 5. Local complexity
    window_size = 4
    if len(seq_str) >= window_size:
        complexities = []
        for i in range(len(seq_str) - window_size + 1):
            window = seq_str[i:i+window_size]
            unique_bases = len(set(window))
            complexities.append(unique_bases / 4)
        avg_complexity = sum(complexities) / len(complexities)
        complexity_variance = sum((c - avg_complexity)**2 for c in complexities) / len(complexities)
        score += avg_complexity * 3
        score -= complexity_variance * 2
    
    # 6. Dinucleotide preferences
    dinuc_scores = {
        'CG': 0.2, 'GC': 0.2, 'GA': 0.1, 'TC': 0.1,
        'AA': -0.2, 'TT': -0.2
    }
    for i in range(len(seq_str) - 1):
        dinuc = seq_str[i:i+2]
        score += dinuc_scores.get(dinuc, 0)
    
    # 7. Melting temperature
    tm_simple = 4 * (seq_str.count('G') + seq_str.count('C')) + 2 * (seq_str.count('A') + seq_str.count('T'))
    tm_normalized = (tm_simple - 20) / 40
    score += tm_normalized * 2
    
    # 8. Experimental noise
    score += random.gauss(0, 0.15)
    
    return max(0, score)

if __name__ == "__main__":
    print("=" * 70)
    print("RUNNING IMPROVED DyNA PPO WITH BETTER SURROGATE LEARNING")
    print("=" * 70)

    # input_l = 6
    # input_r = 10
    # input_b = 32
    # input_m = "weighted"
    # input_ty = "dynamic"

    # time_str = datetime.now().strftime("%Y%m%d%H%M%S")
    # base_dir = Path("experiments")
    # dir_path = base_dir / f"{time_str}_r{input_r}_b{input_b}_l{input_l}_{input_m}_{input_ty}"    
    # dir_path.mkdir(parents=True, exist_ok=True)
    

    # Run with improved configuration
    trained_dyna_ppo = run_dyna_ppo_algorithm(
        dir_path = dir_path,
        oracle_fn=dna_oracle,
        vocab_size=4,      # DNA: A, T, G, C  
        max_seq_len=input_l,    # 12-base sequences
        N=input_r,              # More rounds for better learning
        M=5,               # Model-based training rounds
        tau=0.2,           # Lower threshold for early rounds
        batch_size=input_b,     # Larger batch for more diversity
        use_warmup=True,    # Enable warm-up phase
        method = input_m,
        threshold_type = input_ty,
        diversity_penalty = 'yes',
        purePPO = False
        
    )

    
    # print("\n=== Ensemble Weight Analysis ===")
    # trained_dyna_ppo.analyze_weight_evolution()

    # Generate and evaluate final optimized sequences
    print("\n" + "=" * 70)
    print("FINAL OPTIMIZED SEQUENCES")
    print("=" * 70)
    
    final_sequences = []
    final_rewards = []
    
    # Generate multiple sequences with different strategies
    print("\nDeterministic (Exploitation):")
    for i in range(5):
        seq = trained_dyna_ppo.generate_sequence(deterministic=True)
        reward = dna_oracle(seq)
        dna_seq = ''.join(['ATGC'[j] for j in seq])
        print(f"  {dna_seq}: {reward:.3f}")
        final_sequences.append(seq)
        final_rewards.append(reward)
    
    print("\nStochastic (Exploration):")
    for i in range(5):
        seq = trained_dyna_ppo.generate_sequence(deterministic=False)
        reward = dna_oracle(seq)
        dna_seq = ''.join(['ATGC'[j] for j in seq])
        print(f"  {dna_seq}: {reward:.3f}")
        final_sequences.append(seq)
        final_rewards.append(reward)
    
    # Statistics
    print(f"\nFinal Performance:")
    print(f"  Mean reward: {np.mean(final_rewards):.3f}")
    print(f"  Max reward: {np.max(final_rewards):.3f}")
    print(f"  Std reward: {np.std(final_rewards):.3f}")
    
    # Find best sequence
    best_idx = np.argmax(final_rewards)
    best_seq = ''.join(['ATGC'[j] for j in final_sequences[best_idx]])
    print(f"\nBest sequence found: {best_seq}")
    print(f"   Reward: {final_rewards[best_idx]:.3f}")
    
    print("\n" + "=" * 70)
    print("Training complete! Check 'learning_curves.png' and 'training_metrics.json'")
    print("=" * 70)


    # Generate model evolution plot
    print("\n=== Model Weight Evolution Analysis ===")
    trained_dyna_ppo.plot_model_weight_evolution(save_path=str(dir_path / "model_evolution.png"))

    # Generate detailed report
    if hasattr(trained_dyna_ppo, 'model_performance_history'):
        history = trained_dyna_ppo.model_performance_history
        
        # Export to CSV for further analysis
        import pandas as pd
        
        # Create DataFrame for each round
        data_rows = []
        for i in range(len(history['rounds'])):
            round_num = history['rounds'][i]
            for j, name in enumerate(history['model_names'][i]):
                data_rows.append({
                    'round': round_num,
                    'model': name,
                    'r2_score': history['r2_scores'][i][j],
                    'weight': history['weights'][i][j]
                })
        
        df = pd.DataFrame(data_rows)
        df.to_csv(dir_path / 'model_performance_details.csv', index=False)
        print("Detailed performance data saved to model_performance_details.csv")