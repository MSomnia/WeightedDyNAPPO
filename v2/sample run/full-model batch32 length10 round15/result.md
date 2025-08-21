======================================================================
RUNNING IMPROVED DyNA PPO WITH BETTER SURROGATE LEARNING
======================================================================
======================================================================
IMPROVED DyNA PPO ALGORITHM
======================================================================
Configuration:
  Number of experiment rounds N = 15
  Number of model-based training rounds M = 5
  Minimum model score τ = 0.2
  Batch size B = 32
  Warm-up phase: True
======================================================================

=== WARM-UP PHASE ===
Generating 50 warm-up samples...
Warm-up statistics:
  Mean reward: 6.768
  Std reward: 1.942
  Min/Max: 0.551 / 9.091

======================================================================
EXPERIMENT ROUND 1/15
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.300
Total data collected: 50

--- Round 1 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  CACGTTAG
  ACACGAGC
  CAATTAAG
  ACGCACTA
  GAGTCGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.865
  Max reward: 9.461
  With intrinsic bonuses: 7.932

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9797, entropy=1.3846, kl_div=0.0000
    Epoch 2: policy_loss=-0.1534, value_loss=0.9785, entropy=1.3771, kl_div=-0.0521
    Epoch 4: policy_loss=-0.1803, value_loss=0.9774, entropy=1.3750, kl_div=-0.0957
    Epoch 6: policy_loss=-0.1958, value_loss=0.9763, entropy=1.3754, kl_div=-0.0865

=== Surrogate Model Training ===
Total samples: 82

Training on 81 samples (removed 1 outliers)
Reward range: [2.86, 9.56], mean: 7.30
  Created 8 candidate models for data size 81
  rf-xs: R² = 0.636 (std: 0.159)
  rf-s: R² = 0.634 (std: 0.144)
  knn-xs: R² = 0.284 (std: 0.327)
  knn-s: R² = 0.284 (std: 0.327)
  ridge: R² = 0.744 (std: 0.090)
  gb-xs: R² = 0.740 (std: 0.135)
  gp: R² = -26.701 (std: 14.978)
  svr-rbf-s: R² = 0.448 (std: 0.173)

Model-based training with 7 models
Best R²: 0.744, Mean R²: -2.866
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9711, entropy=1.3736, kl_div=0.0000
    Epoch 1: policy_loss=-0.0470, value_loss=0.9708, entropy=1.3711, kl_div=-0.0022
  Round 1/5: Mean predicted reward = 7.500
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9756, entropy=1.3678, kl_div=0.0000
    Epoch 1: policy_loss=-0.0654, value_loss=0.9752, entropy=1.3609, kl_div=0.0291
  Round 2/5: Mean predicted reward = 7.674
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9760, entropy=1.3529, kl_div=0.0000
    Epoch 1: policy_loss=-0.0601, value_loss=0.9756, entropy=1.3414, kl_div=0.0484
  Round 3/5: Mean predicted reward = 7.783
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9767, entropy=1.3279, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0925
  Round 4/5: Mean predicted reward = 7.719
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9731, entropy=1.3081, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1017
  Round 5/5: Mean predicted reward = 7.629

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 1 Results ---
  Mean Oracle Reward: 7.830
  Min Oracle Reward: 4.310
  Max Oracle Reward: 9.335
  Std Oracle Reward: 1.287
  Sequence Diversity: 1.000
  Models Used: 7
  Model R² - Mean: -2.866, Max: 0.744, Count: 8
  New best mean reward!
  Total Sequences Evaluated: 82

======================================================================
EXPERIMENT ROUND 2/15
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.300
Total data collected: 82

--- Round 2 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  GGAACCAT
  GCCTCGAT
  CGCGAGGC
  GGGGAGCA
  CGATTTGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.511
  Max reward: 9.616
  With intrinsic bonuses: 7.460

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9738, entropy=1.2828, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0951

=== Surrogate Model Training ===
Total samples: 114

Training on 109 samples (removed 5 outliers)
Reward range: [3.92, 9.78], mean: 7.52
  Created 11 candidate models for data size 109
  rf-m: R² = 0.676 (std: 0.073)
  rf-l: R² = 0.674 (std: 0.072)
  gb-m: R² = 0.730 (std: 0.094)
  gb-l: R² = 0.737 (std: 0.094)
  xgb-m: R² = 0.579 (std: 0.131)
  knn-m: R² = 0.417 (std: 0.117)
  knn-tuned: R² = 0.417 (std: 0.117)
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
  mlp-m: R² = -0.925 (std: 0.304)
  svr-rbf: R² = 0.565 (std: 0.050)
  svr-poly: R² = 0.565 (std: 0.050)
  ridge: R² = 0.813 (std: 0.050)

Model-based training with 10 models
Best R²: 0.813, Mean R²: 0.477
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9738, entropy=1.2643, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0955
  Round 1/5: Mean predicted reward = 7.493
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9761, entropy=1.2488, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0637
  Round 2/5: Mean predicted reward = 7.725
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9743, entropy=1.2419, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0510
  Round 3/5: Mean predicted reward = 7.620
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=1.2300, kl_div=0.0000
    Epoch 1: policy_loss=-0.0119, value_loss=0.9690, entropy=1.2243, kl_div=0.0313
  Round 4/5: Mean predicted reward = 7.645
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9745, entropy=1.2248, kl_div=0.0000
    Epoch 1: policy_loss=-0.0468, value_loss=0.9744, entropy=1.2263, kl_div=0.0096
  Round 5/5: Mean predicted reward = 7.740

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 2 Results ---
  Mean Oracle Reward: 7.516
  Min Oracle Reward: 4.799
  Max Oracle Reward: 9.693
  Std Oracle Reward: 1.008
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: 0.477, Max: 0.813, Count: 11
  Total Sequences Evaluated: 114

======================================================================
EXPERIMENT ROUND 3/15
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.300
Total data collected: 114

--- Round 3 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  CGCGGAAC
  ATGACGGG
  CGCGCGCC
  AAAGGACT
  CAGCAACT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.424
  Max reward: 9.868
  With intrinsic bonuses: 7.579

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=1.2266, kl_div=0.0000
    Epoch 2: policy_loss=-0.0366, value_loss=0.9683, entropy=1.2283, kl_div=0.0093
    Epoch 4: policy_loss=-0.0958, value_loss=0.9682, entropy=1.2315, kl_div=0.0080
    Epoch 6: policy_loss=-0.1456, value_loss=0.9681, entropy=1.2362, kl_div=-0.0035

=== Surrogate Model Training ===
Total samples: 146

Training on 140 samples (removed 6 outliers)
Reward range: [3.92, 9.88], mean: 7.53
  Created 11 candidate models for data size 140
  rf-m: R² = 0.699 (std: 0.066)
  rf-l: R² = 0.696 (std: 0.048)
  gb-m: R² = 0.825 (std: 0.045)
  gb-l: R² = 0.825 (std: 0.040)
  xgb-m: R² = 0.692 (std: 0.057)
  knn-m: R² = 0.489 (std: 0.048)
  knn-tuned: R² = 0.489 (std: 0.048)
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
  mlp-m: R² = -0.682 (std: 0.494)
  svr-rbf: R² = 0.623 (std: 0.105)
  svr-poly: R² = 0.623 (std: 0.105)
  ridge: R² = 0.857 (std: 0.046)

Model-based training with 10 models
Best R²: 0.857, Mean R²: 0.558
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=1.2300, kl_div=0.0000
    Epoch 1: policy_loss=-0.0316, value_loss=0.9687, entropy=1.2273, kl_div=0.0162
  Round 1/5: Mean predicted reward = 7.651
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9752, entropy=1.2293, kl_div=0.0000
    Epoch 1: policy_loss=-0.0313, value_loss=0.9751, entropy=1.2240, kl_div=0.0182
  Round 2/5: Mean predicted reward = 7.795
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9711, entropy=1.2258, kl_div=0.0000
    Epoch 1: policy_loss=-0.0131, value_loss=0.9710, entropy=1.2231, kl_div=0.0040
  Round 3/5: Mean predicted reward = 7.921
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9719, entropy=1.2142, kl_div=0.0000
    Epoch 1: policy_loss=-0.0384, value_loss=0.9718, entropy=1.2113, kl_div=0.0158
  Round 4/5: Mean predicted reward = 7.749
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=1.2010, kl_div=0.0000
    Epoch 1: policy_loss=-0.0315, value_loss=0.9675, entropy=1.1981, kl_div=0.0148
  Round 5/5: Mean predicted reward = 7.788

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 3 Results ---
  Mean Oracle Reward: 7.476
  Min Oracle Reward: 3.940
  Max Oracle Reward: 9.932
  Std Oracle Reward: 1.288
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: 0.558, Max: 0.857, Count: 11
  Total Sequences Evaluated: 146

======================================================================
EXPERIMENT ROUND 4/15
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.280
Total data collected: 146

--- Round 4 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0100
Exploration rate: 0.280

--- Generated Sequences (Diversity: 1.000) ---
  CCTGAGAT
  AGCGTAAT
  AATGTCGC
  GTGGACCA
  GTAAATGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.822
  Max reward: 9.331
  With intrinsic bonuses: 7.932

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9681, entropy=1.1833, kl_div=0.0000
    Epoch 1: policy_loss=-0.0075, value_loss=0.9681, entropy=1.1827, kl_div=0.0057
    Epoch 2: policy_loss=-0.0163, value_loss=0.9681, entropy=1.1819, kl_div=0.0142
    Epoch 3: policy_loss=-0.0260, value_loss=0.9681, entropy=1.1808, kl_div=0.0253

=== Surrogate Model Training ===
Total samples: 178

Training on 170 samples (removed 8 outliers)
Reward range: [4.39, 9.88], mean: 7.63
  Created 11 candidate models for data size 170
  rf-m: R² = 0.732 (std: 0.098)
  rf-l: R² = 0.724 (std: 0.107)
  gb-m: R² = 0.787 (std: 0.113)
  gb-l: R² = 0.787 (std: 0.114)
  xgb-m: R² = 0.757 (std: 0.096)
  knn-m: R² = 0.483 (std: 0.085)
  knn-tuned: R² = 0.483 (std: 0.085)
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
  mlp-m: R² = -0.902 (std: 0.447)
  svr-rbf: R² = 0.658 (std: 0.111)
  svr-poly: R² = 0.658 (std: 0.111)
  ridge: R² = 0.847 (std: 0.027)

Model-based training with 10 models
Best R²: 0.847, Mean R²: 0.547
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9756, entropy=1.1901, kl_div=0.0000
    Epoch 1: policy_loss=-0.0090, value_loss=0.9756, entropy=1.1891, kl_div=0.0037
  Round 1/5: Mean predicted reward = 7.948
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9720, entropy=1.1849, kl_div=0.0000
    Epoch 1: policy_loss=-0.0139, value_loss=0.9720, entropy=1.1838, kl_div=0.0079
  Round 2/5: Mean predicted reward = 7.825
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9708, entropy=1.1788, kl_div=0.0000
    Epoch 1: policy_loss=-0.0024, value_loss=0.9708, entropy=1.1773, kl_div=0.0092
  Round 3/5: Mean predicted reward = 8.001
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9665, entropy=1.1907, kl_div=0.0000
    Epoch 1: policy_loss=-0.0042, value_loss=0.9665, entropy=1.1894, kl_div=0.0066
  Round 4/5: Mean predicted reward = 8.099
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9754, entropy=1.1744, kl_div=0.0000
    Epoch 1: policy_loss=-0.0079, value_loss=0.9754, entropy=1.1726, kl_div=0.0123
  Round 5/5: Mean predicted reward = 7.955

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 4 Results ---
  Mean Oracle Reward: 7.815
  Min Oracle Reward: 5.057
  Max Oracle Reward: 9.308
  Std Oracle Reward: 1.004
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: 0.547, Max: 0.847, Count: 11
  Total Sequences Evaluated: 178

======================================================================
EXPERIMENT ROUND 5/15
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.250
Total data collected: 178

--- Round 5 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0100
Exploration rate: 0.250

--- Generated Sequences (Diversity: 1.000) ---
  CTCAGTGA
  GTGTCACA
  CTCAAGGT
  GGTCATAC
  TACCGGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.044
  Max reward: 11.669
  With intrinsic bonuses: 8.139

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9731, entropy=1.1786, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1170

=== Surrogate Model Training ===
Total samples: 210

Training on 199 samples (removed 11 outliers)
Reward range: [4.50, 10.02], mean: 7.72
  Created 11 candidate models for data size 199
  rf-m: R² = 0.728 (std: 0.045)
  rf-l: R² = 0.723 (std: 0.047)
  gb-m: R² = 0.834 (std: 0.054)
  gb-l: R² = 0.836 (std: 0.058)
  xgb-m: R² = 0.770 (std: 0.089)
  knn-m: R² = 0.498 (std: 0.137)
  knn-tuned: R² = 0.498 (std: 0.137)
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
  mlp-m: R² = -0.488 (std: 0.264)
  svr-rbf: R² = 0.677 (std: 0.138)
  svr-poly: R² = 0.677 (std: 0.138)
  ridge: R² = 0.859 (std: 0.062)

Model-based training with 10 models
Best R²: 0.859, Mean R²: 0.601
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9638, entropy=1.1671, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0699
  Round 1/5: Mean predicted reward = 7.897
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9679, entropy=1.1603, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0604
  Round 2/5: Mean predicted reward = 7.978
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=1.1260, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1254
  Round 3/5: Mean predicted reward = 7.788
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=1.1022, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1575
  Round 4/5: Mean predicted reward = 7.920
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9759, entropy=1.1105, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1461
  Round 5/5: Mean predicted reward = 7.902

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 5 Results ---
  Mean Oracle Reward: 8.037
  Min Oracle Reward: 4.201
  Max Oracle Reward: 11.858
  Std Oracle Reward: 1.351
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: 0.601, Max: 0.859, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 210

======================================================================
EXPERIMENT ROUND 6/15
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.220
Total data collected: 210
  Consistent improvement, increasing LR to 0.000327

--- Round 6 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0100
Exploration rate: 0.220

--- Generated Sequences (Diversity: 1.000) ---
  TTCGAGAC
  CGATTCGA
  GAGTCACT
  CAGTGCAT
  AAGTTCGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.421
  Max reward: 10.163
  With intrinsic bonuses: 8.461

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=1.0920, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1212

=== Surrogate Model Training ===
Total samples: 242

Training on 227 samples (removed 15 outliers)
Reward range: [5.14, 10.03], mean: 7.86
  Created 11 candidate models for data size 227
  rf-m: R² = 0.725 (std: 0.056)
  rf-l: R² = 0.726 (std: 0.075)
  gb-m: R² = 0.826 (std: 0.042)
  gb-l: R² = 0.825 (std: 0.043)
  xgb-m: R² = 0.743 (std: 0.101)
  knn-m: R² = 0.437 (std: 0.179)
  knn-tuned: R² = 0.437 (std: 0.179)
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
  mlp-m: R² = -0.788 (std: 0.313)
  svr-rbf: R² = 0.683 (std: 0.126)
  svr-poly: R² = 0.683 (std: 0.126)
  ridge: R² = 0.890 (std: 0.033)

Model-based training with 10 models
Best R²: 0.890, Mean R²: 0.562
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9739, entropy=1.0742, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0756
  Round 1/5: Mean predicted reward = 7.923
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=1.0682, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0826
  Round 2/5: Mean predicted reward = 7.952
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9708, entropy=1.0542, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0990
  Round 3/5: Mean predicted reward = 7.956
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9716, entropy=1.0232, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2159
  Round 4/5: Mean predicted reward = 7.761
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9719, entropy=1.0397, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2053
  Round 5/5: Mean predicted reward = 7.740

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 6 Results ---
  Mean Oracle Reward: 8.428
  Min Oracle Reward: 6.479
  Max Oracle Reward: 10.192
  Std Oracle Reward: 0.736
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: 0.562, Max: 0.890, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 242

======================================================================
EXPERIMENT ROUND 7/15
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.190
Total data collected: 242
  Consistent improvement, increasing LR to 0.000240

--- Round 7 Configuration ---
Learning rate: 0.000240
Entropy coefficient: 0.0100
Exploration rate: 0.190

--- Generated Sequences (Diversity: 1.000) ---
  CTGTAACG
  ACGTTACG
  CGCATGAT
  ATCATGGC
  TAATGCGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.711
  Max reward: 10.052
  With intrinsic bonuses: 7.783

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9713, entropy=1.0018, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2235

=== Surrogate Model Training ===
Total samples: 274

Training on 256 samples (removed 18 outliers)
Reward range: [5.14, 10.03], mean: 7.91
  Created 11 candidate models for data size 256
  rf-m: R² = 0.762 (std: 0.060)
  rf-l: R² = 0.761 (std: 0.051)
  gb-m: R² = 0.856 (std: 0.034)
  gb-l: R² = 0.852 (std: 0.034)
  xgb-m: R² = 0.799 (std: 0.058)
  knn-m: R² = 0.448 (std: 0.100)
  knn-tuned: R² = 0.448 (std: 0.100)
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
  mlp-m: R² = -0.268 (std: 0.227)
  svr-rbf: R² = 0.729 (std: 0.082)
  svr-poly: R² = 0.729 (std: 0.082)
  ridge: R² = 0.898 (std: 0.039)

Model-based training with 10 models
Best R²: 0.898, Mean R²: 0.637
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9716, entropy=0.9982, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2119
  Round 1/5: Mean predicted reward = 7.771
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9671, entropy=0.9710, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2834
  Round 2/5: Mean predicted reward = 7.905
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.9613, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3315
  Round 3/5: Mean predicted reward = 8.067
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.9447, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2944
  Round 4/5: Mean predicted reward = 7.879
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9722, entropy=0.8936, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4478
  Round 5/5: Mean predicted reward = 8.058

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 7 Results ---
  Mean Oracle Reward: 7.827
  Min Oracle Reward: 0.000
  Max Oracle Reward: 9.731
  Std Oracle Reward: 2.060
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: 0.637, Max: 0.898, Count: 11
  Total Sequences Evaluated: 274

======================================================================
EXPERIMENT ROUND 8/15
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.080
Total data collected: 274

--- Round 8 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.080

--- Generated Sequences (Diversity: 1.000) ---
  TCAATCGG
  GTCGCAAG
  CGTATAGC
  TAAGCCGT
  CGCATGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.150
  Max reward: 10.690
  With intrinsic bonuses: 8.239

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9658, entropy=0.9187, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1466

=== Surrogate Model Training ===
Total samples: 306

Training on 287 samples (removed 19 outliers)
Reward range: [5.14, 10.72], mean: 7.95
  Created 11 candidate models for data size 287
  rf-m: R² = 0.798 (std: 0.035)
  rf-l: R² = 0.803 (std: 0.027)
  gb-m: R² = 0.870 (std: 0.029)
  gb-l: R² = 0.869 (std: 0.029)
  xgb-m: R² = 0.800 (std: 0.043)
  knn-m: R² = 0.481 (std: 0.125)
  knn-tuned: R² = 0.481 (std: 0.125)
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
  mlp-m: R² = -0.160 (std: 0.210)
  svr-rbf: R² = 0.737 (std: 0.072)
  svr-poly: R² = 0.737 (std: 0.072)
  ridge: R² = 0.909 (std: 0.034)

Model-based training with 10 models
Best R²: 0.909, Mean R²: 0.666
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9674, entropy=0.8778, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2052
  Round 1/5: Mean predicted reward = 7.790
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.8907, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1506
  Round 2/5: Mean predicted reward = 7.845
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9718, entropy=0.8943, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1666
  Round 3/5: Mean predicted reward = 7.636
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9660, entropy=0.8495, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1953
  Round 4/5: Mean predicted reward = 7.852
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9656, entropy=0.8716, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1905
  Round 5/5: Mean predicted reward = 8.136

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 8 Results ---
  Mean Oracle Reward: 8.123
  Min Oracle Reward: 4.238
  Max Oracle Reward: 10.795
  Std Oracle Reward: 1.351
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: 0.666, Max: 0.909, Count: 11
  Total Sequences Evaluated: 306

======================================================================
EXPERIMENT ROUND 9/15
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.065
Total data collected: 306

--- Round 9 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.065

--- Generated Sequences (Diversity: 1.000) ---
  TCGAGGCA
  GTGCAGCA
  AAGCTTAG
  GCTAATCG
  GGTTACAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.088
  Max reward: 10.196
  With intrinsic bonuses: 8.111

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9717, entropy=0.8556, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0661

=== Surrogate Model Training ===
Total samples: 338

Training on 317 samples (removed 21 outliers)
Reward range: [5.21, 10.72], mean: 7.98
  Created 14 candidate models for data size 317
  rf-tuned-l: R² = 0.806 (std: 0.038)
  rf-tuned-xl: R² = 0.802 (std: 0.037)
  gb-tuned-l: R² = 0.876 (std: 0.042)
  gb-tuned-xl: R² = 0.876 (std: 0.041)
  xgb-xl: R² = 0.817 (std: 0.035)
  xgb-l: R² = 0.817 (std: 0.035)
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
  mlp-adaptive-xl: R² = -0.045 (std: 0.302)
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
  mlp-l: R² = -0.169 (std: 0.268)
  svr-rbf-xl: R² = 0.737 (std: 0.078)
  svr-poly-l: R² = 0.737 (std: 0.078)
  knn-tuned-sqrt: R² = 0.479 (std: 0.131)
  knn-tuned-l: R² = 0.479 (std: 0.131)
  ridge: R² = 0.907 (std: 0.023)
  gp: R² = -61.876 (std: 14.033)

Model-based training with 11 models
Best R²: 0.907, Mean R²: -3.840
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9731, entropy=0.8364, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0644
  Round 1/5: Mean predicted reward = 7.532
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.8457, kl_div=0.0000
    Epoch 1: policy_loss=0.0063, value_loss=0.9689, entropy=0.8438, kl_div=0.0382
  Round 2/5: Mean predicted reward = 7.732
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9721, entropy=0.8197, kl_div=0.0000
    Epoch 1: policy_loss=-0.0246, value_loss=0.9721, entropy=0.8185, kl_div=0.0385
  Round 3/5: Mean predicted reward = 7.627
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.8220, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0516
  Round 4/5: Mean predicted reward = 8.015
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.8384, kl_div=0.0000
    Epoch 1: policy_loss=-0.0163, value_loss=0.9701, entropy=0.8364, kl_div=0.0447
  Round 5/5: Mean predicted reward = 8.135

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 9 Results ---
  Mean Oracle Reward: 8.078
  Min Oracle Reward: 4.355
  Max Oracle Reward: 10.062
  Std Oracle Reward: 1.186
  Sequence Diversity: 1.000
  Models Used: 11
  Model R² - Mean: -3.840, Max: 0.907, Count: 14
  Total Sequences Evaluated: 338

======================================================================
EXPERIMENT ROUND 10/15
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 338

--- Round 10 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TACACGGT
  CCGTAATG
  CAGCTGTA
  GATTCGAC
  TAATGCGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.232
  Max reward: 10.503
  With intrinsic bonuses: 8.152

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.8156, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5183

=== Surrogate Model Training ===
Total samples: 370

Training on 349 samples (removed 21 outliers)
Reward range: [5.21, 10.72], mean: 8.00
  Created 14 candidate models for data size 349
  rf-tuned-l: R² = 0.820 (std: 0.036)
  rf-tuned-xl: R² = 0.810 (std: 0.043)
  gb-tuned-l: R² = 0.887 (std: 0.036)
  gb-tuned-xl: R² = 0.888 (std: 0.036)
  xgb-xl: R² = 0.831 (std: 0.030)
  xgb-l: R² = 0.831 (std: 0.030)
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
  mlp-adaptive-xl: R² = -0.061 (std: 0.223)
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\neural_network\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
  mlp-l: R² = 0.050 (std: 0.229)
  svr-rbf-xl: R² = 0.767 (std: 0.059)
  svr-poly-l: R² = 0.767 (std: 0.059)
  knn-tuned-sqrt: R² = 0.529 (std: 0.148)
  knn-tuned-l: R² = 0.529 (std: 0.148)
  ridge: R² = 0.921 (std: 0.028)
  gp: R² = -58.449 (std: 7.828)

Model-based training with 12 models
Best R²: 0.921, Mean R²: -3.563
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9654, entropy=0.8499, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2400
  Round 1/5: Mean predicted reward = 7.459
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=0.7884, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4586
  Round 2/5: Mean predicted reward = 7.418
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.7763, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4102
  Round 3/5: Mean predicted reward = 7.522
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9728, entropy=0.8090, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2034
  Round 4/5: Mean predicted reward = 7.873
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=0.7397, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4109
  Round 5/5: Mean predicted reward = 7.974

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 10 Results ---
  Mean Oracle Reward: 8.153
  Min Oracle Reward: 5.749
  Max Oracle Reward: 10.849
  Std Oracle Reward: 1.088
  Sequence Diversity: 1.000
  Models Used: 12
  Model R² - Mean: -3.563, Max: 0.921, Count: 14
  Total Sequences Evaluated: 370

  Early stopping: Converged at round 10

======================================================================
DyNA PPO ALGORITHM COMPLETE!
======================================================================
Total rounds executed: 10
Total sequences evaluated: 370
Best mean reward: 8.428 (achieved at round 6)

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 10
Final Mean Reward: 8.1534
Best Mean Reward: 8.4281
Best Max Reward: 11.8583
Initial Lr: 0.0003
Final Lr: 0.0003
Total Updates: 95
Final Diversity: 1.0000
Convergence Round: 3
==================================================

Generating learning curves...
Learning curves saved to learning_curves.png
Saving training metrics...
Metrics saved to training_metrics.json

======================================================================
FINAL OPTIMIZED SEQUENCES
======================================================================

Deterministic (Exploitation):
  GGCGATAG: 8.662
  GGCGATAG: 8.868
  GGCGATAG: 8.697
  GGCGATAG: 8.829
  GGCGATAG: 8.614

Stochastic (Exploration):
  GCGACTGC: 8.625
  GGGTCAGC: 7.488
  GGGCTTTC: 7.030
  GGGCAGTT: 8.188
  GGCGACGT: 7.968

Final Performance:
  Mean reward: 8.297
  Max reward: 8.868
  Std reward: 0.591

Best sequence found: GGCGATAG
   Reward: 8.868

======================================================================
Training complete! Check 'learning_curves.png' and 'training_metrics.json'
======================================================================