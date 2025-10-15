# Adaptive Learning Mechanisms Section - Summary

## Overview
This LaTeX document provides a comprehensive technical description of the adaptive learning mechanisms in DyNAPPO, based on the implementation in `DyNAPPO.py` and `run2.py`.

## Structure

### 1. Learning Rate Scheduling

**Cosine Annealing with Warm Restarts** (Lines 1080-1093 of DyNAPPO.py, Lines 161-171 of run2.py)
- **Implementation**: Uses cosine function with period P=5
- **Formula**: η_scheduled(n) = η_min + (η_base - η_min)/2 * (1 + cos(π*(n mod P)/P))
- **Parameters**:
  - Base LR: 3×10⁻⁴
  - Min LR: 1×10⁻⁵
  - Period: 5 rounds
- **Purpose**: Creates sawtooth pattern with warm restarts to escape local minima
- **Code reference**:
  - `update_learning_rate()` method (lines 1080-1121)
  - `get_learning_rate()` function in run2.py (lines 161-171)

**Performance-Based Adjustment** (Lines 1097-1112 of DyNAPPO.py)
- **Plateau Detection**: If Var(last 3 rewards) < 0.01 → reduce LR by 50%
- **Improvement Detection**: If 3 consecutive increases → increase LR by 20%
- **Formula**:
  - Plateau: η_adjusted = 0.5 * η_scheduled
  - Improvement: η_adjusted = 1.2 * η_scheduled
  - Normal: η_adjusted = η_scheduled
- **Clipping**: Final LR clipped to [η_min, η_base]
- **Code reference**: Lines 1097-1115

### 2. Exploration Scheduling

**Decaying Exploration Rate** (Lines 184-190 of run2.py)
- **Three-stage schedule**:
  - Early (n ≤ 3): ε = 0.3 (30% random exploration)
  - Middle (3 < n ≤ 7): ε = max(0.15, 0.4 - 0.03n) (fast decay)
  - Late (n > 7): ε = max(0.05, 0.2 - 0.015n) (slow decay)
- **Decay rates**: -0.03/round (middle), -0.015/round (late)
- **Floor values**: 0.15 (middle), 0.05 (late)
- **Code reference**: Lines 184-190 of run2.py

**Adaptive Entropy Coefficients** (Lines 1332-1338 of DyNAPPO.py)
- **Schedule**:
  - Early (n ≤ 3): c₂ = 0.02
  - Middle (3 < n ≤ 7): c₂ = 0.01
  - Late (n > 7): c₂ = 0.005
- **Virtual training**: c₂_virtual = 0.5 * c₂ (line 1562)
- **Purpose**: Transitions from high stochasticity (exploration) to low (exploitation)
- **Code reference**: Lines 1332-1338, 1562

**Update Epochs Scheduling** (Lines 1433-1439 of DyNAPPO.py)
- **Schedule**:
  - Early (n ≤ 3): E = 8 epochs
  - Middle (3 < n ≤ 7): E = 4 epochs
  - Late (n > 7): E = 2 epochs
- **Purpose**: More thorough learning early, faster convergence late
- **Code reference**: Lines 1433-1439

### 3. Threshold Management

**Fixed Mode** (Line 1244-1245 of DyNAPPO.py)
- **Formula**: τ_n = τ₀ (constant)
- **Default value**: τ₀ = 0.2
- **Use case**: When oracle complexity is well-understood
- **Code reference**: Lines 1244-1245

**Dynamic Mode** (Lines 1247-1259 of DyNAPPO.py)
- **Piecewise linear schedule**:
  - Warm-up phase (n < n_warmup): τ = -0.3
  - Growth phase (n ≥ n_warmup): τ = min(τ_end, -0.3 + (n - n_warmup) × 0.01)
- **Parameters**:
  - τ_start = -0.3 (initial, accepts poor models)
  - τ_end = τ₀ (user-specified final threshold)
  - n_warmup = ⌊N/10⌋ (10% of total rounds)
  - δ_τ = 0.01 (increment per round)
- **Rationale**:
  - Early: Accept poor models (limited data)
  - Late: Require good models (sufficient data)
- **Code reference**: Lines 1247-1259

**Threshold History Tracking** (Line 1263 of DyNAPPO.py)
- **Storage**: `self.threshold_history.append((round_num, threshold))`
- **Purpose**: Enable post-hoc analysis and hyperparameter tuning
- **Code reference**: Line 1263

## Mathematical Formulations

All equations are derived directly from implementation:

### Learning Rate Equations
- **Eq. (1)**: Cosine annealing formula (lines 1088-1093)
- **Eq. (2)**: Performance-based adjustment (lines 1104-1111)
- **Eq. (3)**: Learning rate clipping (line 1115)

### Exploration Equations
- **Eq. (4)**: Exploration rate schedule (lines 185-190 of run2.py)
- **Eq. (5)**: Entropy coefficient schedule (lines 1332-1338)
- **Eq. (6)**: Virtual entropy scaling (line 1562)
- **Eq. (7)**: Update epochs schedule (lines 1433-1439)

### Threshold Equations
- **Eq. (8)**: Fixed threshold (line 1245)
- **Eq. (9)**: Dynamic threshold (lines 1248-1258)
- **Eq. (10)**: Threshold history (line 1263)

## Key Design Decisions

### 1. Three-Phase Training Strategy
All adaptive mechanisms follow a consistent three-phase pattern:
- **Phase 1 (Early)**: High exploration, high learning rates, lenient thresholds
- **Phase 2 (Middle)**: Balanced exploration/exploitation, moderate rates
- **Phase 3 (Late)**: Low exploration, fine-tuning rates, strict thresholds

### 2. Coordination of Mechanisms
The mechanisms work together:
- Learning rate restarts align with exploration phases
- Entropy coefficient decreases coordinate with exploration rate
- Threshold increases match data accumulation

### 3. Floor and Ceiling Values
All schedules include:
- **Floor values**: Prevent complete elimination of exploration/learning
- **Ceiling values**: Prevent excessive values that destabilize training
- **Clipping**: Ensures parameters stay in valid ranges

## Integration with Other Components

### Policy Optimization
- Learning rate updates affect gradient descent steps
- Entropy coefficients control policy stochasticity
- Update epochs determine optimization thoroughness

### Surrogate Modeling
- Threshold management controls model selection
- Dynamic thresholds adapt to data availability
- Affects number of model-based training rounds (lines 1490-1499)

### Performance Tracking
- Learning rate adjustments use performance history
- Threshold history enables analysis
- All schedules logged to metrics tracker

## Code References Summary

### Primary Functions:
1. `update_learning_rate()` - Lines 1080-1121 of DyNAPPO.py
2. `get_learning_rate()` - Lines 161-171 of run2.py
3. `train_round()` - Lines 1316-1631 of DyNAPPO.py (coordination of all mechanisms)
4. `improved_fit_surrogate_models()` - Lines 1208-1298 (threshold management)

### Key Configuration Locations:
- **Learning rates**: Lines 1082-1083 (base_lr, min_lr)
- **Exploration rates**: Lines 185-190 of run2.py
- **Entropy coefficients**: Lines 1332-1338
- **Threshold parameters**: Lines 1248-1251
- **Update epochs**: Lines 1433-1439

## Usage Notes

This LaTeX section can be integrated directly after the Policy Optimization section in your report. It provides the "how" (adaptive mechanisms) that complements the "what" (PPO algorithm) of the previous section.

### Recommended Position:
- After Policy Optimization subsection
- Before Ensemble Methods or Surrogate Modeling sections
- Part of the broader "Methodology" or "Algorithm" section

### Cross-References:
The document references concepts from Policy Optimization (entropy regularization) and sets up concepts for Surrogate Modeling (threshold management), creating a cohesive narrative flow.
