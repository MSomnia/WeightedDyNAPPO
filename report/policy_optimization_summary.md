# Policy Optimization Section - Summary

## Overview
This LaTeX document provides a comprehensive technical description of the policy optimization mechanisms in DyNAPPO, based on the implementation in `DyNAPPO.py` and `run2.py`.

## Structure

### 1. PPO Loss Function
**Key Components Documented:**
- **Clipped Surrogate Objective**: Lines 719-728 of DyNAPPO.py
  - Implements the ratio-based clipping mechanism
  - Uses advantages computed with value function baseline

- **Value Function Loss**: Lines 731 of DyNAPPO.py
  - MSE loss between predicted values and normalized rewards
  - Coefficient c₁ = 0.5

- **Entropy Regularization**: Lines 694-699, 728-729 of DyNAPPO.py
  - Computed per-position and averaged across sequence
  - Encourages exploration through policy entropy maximization

- **Total Loss**: Lines 734-744 of DyNAPPO.py
  - Combines policy, value, entropy, and L2 regularization terms
  - Adaptive loss weighting based on training round

### 2. Adaptive Mechanisms
**Key Features Documented:**

- **Dynamic Clip Ratio**: Lines 663-669 of DyNAPPO.py
  - Early rounds (n ≤ 3): ε = 0.3
  - High variance (σ > 2.0): ε = 0.1
  - Standard: ε = 0.2

- **KL Divergence Early Stopping**: Lines 746-752 of DyNAPPO.py
  - Monitors KL divergence between old and new policies
  - Stops if KL > 0.05 after epoch 0

- **Gradient Clipping**: Lines 754-768 of DyNAPPO.py
  - Adaptive max gradient norm: 1.0 (early) → 0.5 (late)

- **Adaptive Entropy Coefficient**: Lines 1332-1338 of DyNAPPO.py
  - Decreases from 0.02 → 0.01 → 0.005 over training
  - Reduced by 50% for virtual training rounds

- **Adaptive Reward Normalization**: Lines 646-661 of DyNAPPO.py
  - High variance: Robust normalization with MAD
  - Standard: Z-score normalization

### 3. Reward Engineering
**Key Strategies Documented:**

- **Intrinsic Rewards**: Lines 1051-1073 of DyNAPPO.py
  - k-nearest neighbor (k=5) edit distance computation
  - Novelty bonus normalized by sequence length
  - Exploration weight decays from 1.0 to 0 over 10 rounds

- **Diversity Penalties**: Lines 66-79 of SequenceUtils.py
  - Linear decay weight function with threshold ε = 3
  - Applied during model-based training only
  - Decaying weight across virtual rounds (lines 1526-1535)

- **Reward Combination**:
  - Oracle training: Lines 1397-1407 (oracle + intrinsic)
  - Virtual training: Lines 1519-1539 (predicted - diversity penalty)

## Code References

### Primary Functions:
1. `adaptive_policy_update()` - Lines 635-797 of DyNAPPO.py
2. `compute_intrinsic_reward()` - Lines 1051-1073 of DyNAPPO.py
3. `compute_diversity_penalty()` - Lines 66-79 of SequenceUtils.py
4. `train_round()` - Lines 1316-1631 of DyNAPPO.py

### Key Parameters:
- Batch size: 32 (configurable)
- Clip ratio: Dynamic (0.1-0.3)
- Entropy coefficients: 0.005-0.02
- Value function coefficient: 0.5
- L2 regularization: 0.0001
- Diversity lambda: 0.1
- Diversity epsilon: 3
- KL threshold: 0.05

## Mathematical Formulations
All equations are derived directly from the implementation:
- Equation (1): Probability ratio computation (line 720)
- Equation (2): Clipped objective (lines 723-726)
- Equation (3): Value function loss (line 731)
- Equation (4): Entropy loss (lines 698-699, 728)
- Equation (5): Total loss (lines 734-744)
- Equations (6-7): Dynamic clip ratio (lines 663-669)
- Equation (8): KL divergence (line 747)
- Equations (9-10): Gradient clipping (lines 766-768)
- Equation (11): Entropy coefficient schedule (lines 1332-1338)
- Equations (12-13): Reward normalization (lines 650-661)
- Equations (14-15): Intrinsic reward (lines 1056-1071)
- Equations (16-18): Diversity penalty (SequenceUtils.py lines 66-79)

## Usage Notes
This LaTeX section can be directly integrated into your report. It uses standard LaTeX equation environments and should compile with most document classes (article, IEEEtran, etc.).

### Dependencies:
- Standard LaTeX math packages (amsmath, amssymb)
- No special packages required

### Integration:
Place this section under "Section G" as specified in your outline, or integrate it into your existing methodology section.
