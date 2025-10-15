# DyNAPPO Report Sections - Documentation

This directory contains LaTeX sections for the DyNAPPO project report, generated from the actual implementation code.

## 📁 Files Generated

### Main LaTeX Documents
1. **`policy_optimization_section.tex`** - Policy Optimization subsection (Section G.1)
2. **`adaptive_learning_section.tex`** - Adaptive Learning Mechanisms subsection (Section G.2)

### Supporting Documentation
3. **`policy_optimization_summary.md`** - Detailed guide for policy optimization section
4. **`adaptive_learning_summary.md`** - Detailed guide for adaptive learning section
5. **`README_report_sections.md`** - This file

## 📊 Section Overview

### Section G.1: Policy Optimization
**Based on**: `DyNAPPO.py` (lines 635-1631), `SequenceUtils.py`, `OptimalEnsembleWeights.py`

**Content**:
1. **PPO Loss Function**
   - Clipped surrogate objective
   - Value function loss
   - Entropy regularization
   - Combined loss formulation

2. **Adaptive Mechanisms**
   - Dynamic clip ratio (0.1-0.3)
   - KL divergence early stopping (threshold: 0.05)
   - Gradient clipping (1.0 → 0.5)
   - Adaptive entropy coefficients (0.02 → 0.005)
   - Robust reward normalization (MAD/z-score)

3. **Reward Engineering**
   - k-NN intrinsic rewards (k=5, edit distance)
   - Diversity penalties (λ=0.1, ε=3)
   - Reward combination strategies

**Equations**: 18 numbered equations
**Length**: ~165 lines

---

### Section G.2: Adaptive Learning Mechanisms
**Based on**: `DyNAPPO.py` (lines 1080-1298), `run2.py` (lines 161-203)

**Content**:
1. **Learning Rate Scheduling**
   - Cosine annealing with warm restarts (period=5)
   - Performance-based adjustments (plateau/improvement detection)
   - Learning rate bounds (1e-5 to 3e-4)

2. **Exploration Scheduling**
   - Three-phase exploration rate decay (0.3 → 0.05)
   - Adaptive entropy coefficients (0.02 → 0.005)
   - Update epochs scheduling (8 → 4 → 2)

3. **Threshold Management**
   - Fixed mode (constant τ)
   - Dynamic mode (linear interpolation)
   - Warm-up phase and growth phase
   - Threshold history tracking

**Equations**: 16 numbered equations
**Length**: ~180 lines

---

## 🔗 Section Interconnections

```
Policy Optimization (G.1)
    ├─ Defines: PPO algorithm, loss functions, entropy
    └─ Used by: Adaptive Learning Mechanisms

Adaptive Learning Mechanisms (G.2)
    ├─ Uses: Entropy coefficients from G.1
    ├─ Controls: Learning rate, exploration, thresholds
    └─ Affects: Policy updates, model selection

Surrogate Modeling (G.3 - future)
    ├─ Uses: Threshold management from G.2
    └─ Provides: Model predictions for policy training
```

## 📐 Mathematical Notation

### Consistent Notation Used:
- **θ**: Policy network parameters
- **π_θ**: Policy distribution
- **n**: Training round number
- **N**: Total number of rounds
- **ε**: Exploration rate OR clip ratio (context-dependent)
- **η**: Learning rate
- **τ**: R² threshold for surrogate models
- **c₁, c₂**: Loss coefficients
- **λ**: Regularization coefficients
- **s, a**: State, action
- **R**: Reward
- **V**: Value function
- **A**: Advantage function

## 🎯 Key Hyperparameters Reference

| Parameter | Value | Location | Description |
|-----------|-------|----------|-------------|
| Base LR | 3×10⁻⁴ | DyNAPPO.py:1082 | Maximum learning rate |
| Min LR | 1×10⁻⁵ | DyNAPPO.py:1083 | Minimum learning rate |
| LR Period | 5 | DyNAPPO.py:1088 | Cosine annealing period |
| Initial ε | 0.3 | run2.py:186 | Early exploration rate |
| Final ε | 0.05 | run2.py:190 | Late exploration rate |
| Clip ratio | 0.1-0.3 | DyNAPPO.py:664-669 | PPO clip range |
| KL threshold | 0.05 | DyNAPPO.py:750 | Early stopping criterion |
| Gradient norm | 0.5-1.0 | DyNAPPO.py:767-768 | Gradient clipping |
| c₁ (value) | 0.5 | DyNAPPO.py:736 | Value loss coefficient |
| c₂ (entropy) | 0.005-0.02 | DyNAPPO.py:1333-1337 | Entropy coefficient |
| λ_div | 0.1 | DyNAPPO.py:54, 124 | Diversity penalty |
| ε_div | 3 | DyNAPPO.py:55 | Edit distance threshold |
| τ_start | -0.3 | DyNAPPO.py:1248 | Initial R² threshold |
| δ_τ | 0.01 | DyNAPPO.py:1251 | Threshold increment |

## 📝 Integration Instructions

### To integrate into your main report:

1. **Add to preamble** (if not already present):
```latex
\usepackage{amsmath}
\usepackage{amssymb}
```

2. **Include the sections**:
```latex
\section{Methodology}  % Or your main section

% ... other content ...

\subsection{Policy Optimization}
\input{policy_optimization_section.tex}

\subsection{Adaptive Learning Mechanisms}
\input{adaptive_learning_section.tex}

% ... continue with other sections ...
```

3. **Alternative** (direct copy):
Simply copy the contents of the `.tex` files directly into your main document.

### Equation Numbering
- Equations are numbered sequentially within each subsection
- To reset numbering per section, add to preamble:
```latex
\numberwithin{equation}{section}
```

### Cross-Referencing
To reference equations across sections:
```latex
% In the .tex file, label important equations:
\begin{equation}
\label{eq:ppo_clip}
L^{\text{CLIP}}(\theta) = ...
\end{equation}

% Reference from another section:
As shown in Eq.~\ref{eq:ppo_clip}, the clipped objective...
```

## 🔍 Verification

### Code Coverage
Both sections are based on actual implementation:
- ✅ Every equation maps to specific code lines
- ✅ All hyperparameters match implementation
- ✅ Mathematical formulations verified against code
- ✅ Design decisions documented from comments

### Cross-Validation
To verify accuracy:
1. Check equation numbers against code line references in summary files
2. Verify hyperparameter values in `DyNAPPO.py` and `run2.py`
3. Trace execution flow in `train_round()` method (lines 1316-1631)

## 📚 Related Sections (Future Work)

### Suggested Additional Sections:
1. **Surrogate Modeling** - Ensemble methods, optimal weights
2. **Sequence Generation** - Temperature sampling, guided generation
3. **Feature Engineering** - Context window encoding, positional embeddings
4. **Experimental Setup** - Oracle function, evaluation metrics

### Code Files for Future Sections:
- `OptimalEnsembleWeights.py` - For ensemble methods section
- `PolicyNetwork.py` - For neural architecture section
- `SequenceUtils.py` - For feature engineering section
- `LearningRateTracker.py` - For evaluation metrics section

## 📧 Notes

- All equations are self-contained and can be understood independently
- Mathematical notation is consistent across both sections
- Figures and tables can be added separately
- Code listings can be added using `listings` package if desired

---

**Generated from**: WeightedDyNAPPO v3 implementation
**Date**: 2025
**Author**: Based on code by Eric Lin
**Purpose**: Academic report documentation
