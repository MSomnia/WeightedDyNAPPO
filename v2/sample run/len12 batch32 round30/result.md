======================================================================
RUNNING IMPROVED DyNA PPO WITH BETTER SURROGATE LEARNING
======================================================================
======================================================================
IMPROVED DyNA PPO ALGORITHM
======================================================================
Configuration:
  Number of experiment rounds N = 30
  Number of model-based training rounds M = 5
  Minimum model score τ = 0.2
  Batch size B = 32
  Warm-up phase: True
======================================================================

=== WARM-UP PHASE ===
Generating 50 warm-up samples...
Warm-up statistics:
  Mean reward: 7.960
  Std reward: 3.011
  Min/Max: 0.000 / 11.802

======================================================================
EXPERIMENT ROUND 1/30
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.300
Total data collected: 50

--- Round 1 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  TTTCAATAAATC
  TAATGCGAAGAT
  TAAGAGCCGTCC
  GGTGAAACCCAA
  ACCTCTCCATAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.069
  Max reward: 12.298
  With intrinsic bonuses: 9.158

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9823, entropy=1.3841, kl_div=0.0000
    Early stopping at epoch 2: KL divergence = 0.0694

=== Surrogate Model Training ===
Total samples: 82

Training on 73 samples (removed 9 outliers)
Reward range: [4.70, 12.02], mean: 9.19
  Created 8 candidate models for data size 73
  rf-xs: R2 = 0.097 (std: 0.199)
  rf-s: R2 = 0.114 (std: 0.229)
  knn-xs: R2 = 0.004 (std: 0.166)
  knn-s: R2 = 0.004 (std: 0.166)
  ridge: R2 = 0.138 (std: 0.177)
  gb-xs: R2 = -0.080 (std: 0.156)
  gp: R2 = -48.599 (std: 18.167)
  svr-rbf-s: R2 = 0.140 (std: 0.082)

Model-based training with 7 models
Best R2: 0.140, Mean R2: -6.023
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9805, entropy=1.3805, kl_div=0.0000
    Epoch 1: policy_loss=-0.1193, value_loss=0.9800, entropy=1.3749, kl_div=0.0254
  Round 1/3: Mean predicted reward = 9.167
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9922, entropy=1.3677, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0665
  Round 2/3: Mean predicted reward = 9.415
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9784, entropy=1.3597, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1126
  Round 3/3: Mean predicted reward = 9.341

  === Progress Analysis ===
  Status: NORMAL

--- Round 1 Results ---
  Mean Oracle Reward: 9.191
  Min Oracle Reward: 4.473
  Max Oracle Reward: 11.907
  Std Oracle Reward: 1.718
  Sequence Diversity: 1.000
  Models Used: 7
  Model R² - Mean: -6.023, Max: 0.140, Count: 8
  New best mean reward!
  Total Sequences Evaluated: 82

======================================================================
EXPERIMENT ROUND 2/30
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.300
Total data collected: 82

--- Round 2 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  CGAAAGGAGGCG
  CTACTATGCAGT
  TTACATTAATGG
  AGCCAGCCTTTT
  CACTGCATCCTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.686
  Max reward: 11.593
  With intrinsic bonuses: 9.636

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9715, entropy=1.3468, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1016

=== Surrogate Model Training ===
Total samples: 114

Training on 104 samples (removed 10 outliers)
Reward range: [5.17, 12.02], mean: 9.37
  Created 11 candidate models for data size 104
  rf-m: R2 = 0.047 (std: 0.270)
  rf-l: R2 = 0.001 (std: 0.238)
  gb-m: R2 = -0.183 (std: 0.267)
  gb-l: R2 = -0.182 (std: 0.283)
  xgb-m: R2 = -0.047 (std: 0.240)
  knn-m: R2 = 0.015 (std: 0.224)
  knn-tuned: R2 = 0.015 (std: 0.224)
  mlp-m: R2 = -2.761 (std: 1.841)
  svr-rbf: R2 = 0.017 (std: 0.107)
  svr-poly: R2 = 0.017 (std: 0.107)
  ridge: R2 = 0.012 (std: 0.194)

Model-based training with 10 models
Best R2: 0.047, Mean R2: -0.277
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9741, entropy=1.3374, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1063
  Round 1/3: Mean predicted reward = 9.537
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9804, entropy=1.3271, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0595
  Round 2/3: Mean predicted reward = 9.581
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=1.3118, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1287
  Round 3/3: Mean predicted reward = 9.536

  === Progress Analysis ===
  Status: NORMAL

--- Round 2 Results ---
  Mean Oracle Reward: 9.594
  Min Oracle Reward: 5.191
  Max Oracle Reward: 11.448
  Std Oracle Reward: 1.448
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -0.277, Max: 0.047, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 114

======================================================================
EXPERIMENT ROUND 3/30
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.300
Total data collected: 114

--- Round 3 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  GCCAGCTCCTCC
  GCGACCTCTCGC
  CAAGCTGGACCC
  GTGCAGGCATTT
  GCCCAGCCAGGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.559
  Max reward: 11.201
  With intrinsic bonuses: 9.741

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9796, entropy=1.3000, kl_div=0.0000
    Early stopping at epoch 2: KL divergence = 0.1062

=== Surrogate Model Training ===
Total samples: 146

Training on 134 samples (removed 12 outliers)
Reward range: [6.45, 12.02], mean: 9.47
  Created 11 candidate models for data size 134
  rf-m: R2 = 0.053 (std: 0.169)
  rf-l: R2 = 0.063 (std: 0.164)
  gb-m: R2 = -0.093 (std: 0.385)
  gb-l: R2 = -0.103 (std: 0.377)
  xgb-m: R2 = -0.183 (std: 0.407)
  knn-m: R2 = -0.038 (std: 0.123)
  knn-tuned: R2 = -0.038 (std: 0.123)
  mlp-m: R2 = -2.906 (std: 1.382)
  svr-rbf: R2 = -0.015 (std: 0.057)
  svr-poly: R2 = -0.015 (std: 0.057)
  ridge: R2 = -0.014 (std: 0.080)

Model-based training with 10 models
Best R2: 0.063, Mean R2: -0.299
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9702, entropy=1.2806, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0700
  Round 1/3: Mean predicted reward = 9.594
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9809, entropy=1.2714, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0594
  Round 2/3: Mean predicted reward = 9.727
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9760, entropy=1.2604, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0688
  Round 3/3: Mean predicted reward = 9.675

  === Progress Analysis ===
  Status: NORMAL

--- Round 3 Results ---
  Mean Oracle Reward: 9.590
  Min Oracle Reward: 7.767
  Max Oracle Reward: 10.936
  Std Oracle Reward: 0.878
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -0.299, Max: 0.063, Count: 11
  Total Sequences Evaluated: 146

======================================================================
EXPERIMENT ROUND 4/30
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.280
Total data collected: 146

--- Round 4 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0100
Exploration rate: 0.280

--- Generated Sequences (Diversity: 1.000) ---
  CCAGGCTATTGA
  GCAGGTCATGCA
  TAGACGAGTGCC
  CGCTAATAGGCG
  ACTGGAACTTCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.261
  Max reward: 14.241
  With intrinsic bonuses: 10.385

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9727, entropy=1.2445, kl_div=0.0000
    Epoch 1: policy_loss=-0.0133, value_loss=0.9726, entropy=1.2403, kl_div=0.0396
    Early stopping at epoch 2: KL divergence = 0.0779

=== Surrogate Model Training ===
Total samples: 178

Training on 165 samples (removed 13 outliers)
Reward range: [6.45, 12.02], mean: 9.61
  Created 11 candidate models for data size 165
  rf-m: R2 = -0.057 (std: 0.133)
  rf-l: R2 = -0.059 (std: 0.174)
  gb-m: R2 = -0.280 (std: 0.183)
  gb-l: R2 = -0.275 (std: 0.171)
  xgb-m: R2 = -0.182 (std: 0.292)
  knn-m: R2 = -0.031 (std: 0.138)
  knn-tuned: R2 = -0.031 (std: 0.138)
  mlp-m: R2 = -2.225 (std: 1.261)
  svr-rbf: R2 = -0.091 (std: 0.035)
  svr-poly: R2 = -0.091 (std: 0.035)
  ridge: R2 = -0.144 (std: 0.059)
  Fallback: Using knn-m with R2 = -0.031

Model-based training with 1 models
Best R2: -0.031, Mean R2: -0.315
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9784, entropy=1.2492, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.816
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9832, entropy=1.2475, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.730

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 4 Results ---
  Mean Oracle Reward: 10.246
  Min Oracle Reward: 6.926
  Max Oracle Reward: 14.027
  Std Oracle Reward: 1.292
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -0.315, Max: -0.031, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 178

======================================================================
EXPERIMENT ROUND 5/30
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.250
Total data collected: 178

--- Round 5 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0100
Exploration rate: 0.250

--- Generated Sequences (Diversity: 1.000) ---
  TCAGGCCTGAGA
  CTAGACGTGACT
  GTTTACCACGGA
  CGTGACGGATAC
  TGCATGACACGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.619
  Max reward: 12.678
  With intrinsic bonuses: 9.726

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9795, entropy=1.2296, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3081

=== Surrogate Model Training ===
Total samples: 210

Training on 196 samples (removed 14 outliers)
Reward range: [6.45, 12.61], mean: 9.63
  Created 11 candidate models for data size 196
  rf-m: R2 = 0.002 (std: 0.167)
  rf-l: R2 = -0.018 (std: 0.147)
  gb-m: R2 = -0.106 (std: 0.212)
  gb-l: R2 = -0.106 (std: 0.200)
  xgb-m: R2 = -0.149 (std: 0.273)
  knn-m: R2 = -0.005 (std: 0.066)
  knn-tuned: R2 = -0.005 (std: 0.066)
  mlp-m: R2 = -1.976 (std: 1.166)
  svr-rbf: R2 = -0.016 (std: 0.102)
  svr-poly: R2 = -0.016 (std: 0.102)
  ridge: R2 = -0.090 (std: 0.111)

Model-based training with 1 models
Best R2: 0.002, Mean R2: -0.226
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9746, entropy=1.2075, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3174
  Round 1/3: Mean predicted reward = 9.617
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9749, entropy=1.1732, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3675
  Round 2/3: Mean predicted reward = 9.634
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=1.1334, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4707
  Round 3/3: Mean predicted reward = 9.649

  === Progress Analysis ===
  Status: NORMAL

--- Round 5 Results ---
  Mean Oracle Reward: 9.602
  Min Oracle Reward: 5.514
  Max Oracle Reward: 12.561
  Std Oracle Reward: 1.289
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -0.226, Max: 0.002, Count: 11
  Total Sequences Evaluated: 210

======================================================================
EXPERIMENT ROUND 6/30
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.220
Total data collected: 210

--- Round 6 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0100
Exploration rate: 0.220

--- Generated Sequences (Diversity: 1.000) ---
  GCTGAATCCGAT
  CTCGTGACATAG
  TTGGCAGCGAAC
  GCCAATGGCGAT
  CGTGAAGGCATC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.570
  Max reward: 12.333
  With intrinsic bonuses: 9.649

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9862, entropy=1.1008, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3844

=== Surrogate Model Training ===
Total samples: 242

Training on 227 samples (removed 15 outliers)
Reward range: [6.45, 12.61], mean: 9.65
  Created 11 candidate models for data size 227
  rf-m: R2 = -0.008 (std: 0.094)
  rf-l: R2 = -0.014 (std: 0.131)
  gb-m: R2 = 0.016 (std: 0.112)
  gb-l: R2 = 0.016 (std: 0.117)
  xgb-m: R2 = -0.022 (std: 0.221)
  knn-m: R2 = -0.068 (std: 0.086)
  knn-tuned: R2 = -0.068 (std: 0.086)
  mlp-m: R2 = -1.853 (std: 0.821)
  svr-rbf: R2 = -0.027 (std: 0.088)
  svr-poly: R2 = -0.027 (std: 0.088)
  ridge: R2 = -0.078 (std: 0.115)

Model-based training with 2 models
Best R2: 0.016, Mean R2: -0.194
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9742, entropy=1.0746, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3839
  Round 1/3: Mean predicted reward = 9.665
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9729, entropy=1.0446, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4605
  Round 2/3: Mean predicted reward = 9.657
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9746, entropy=1.0161, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5412
  Round 3/3: Mean predicted reward = 9.628

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 6 Results ---
  Mean Oracle Reward: 9.537
  Min Oracle Reward: 5.973
  Max Oracle Reward: 11.987
  Std Oracle Reward: 1.407
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -0.194, Max: 0.016, Count: 11
  Total Sequences Evaluated: 242

======================================================================
EXPERIMENT ROUND 7/30
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.190
Total data collected: 242

--- Round 7 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0100
Exploration rate: 0.190

--- Generated Sequences (Diversity: 1.000) ---
  GCAGTAGAGCCT
  GACCATGACTTG
  TGCCGGTAACAG
  CGAATCACGGTG
  ATGCAGCCAGTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.908
  Max reward: 11.758
  With intrinsic bonuses: 9.951

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9856, entropy=0.9872, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2616

=== Surrogate Model Training ===
Total samples: 274

Training on 257 samples (removed 17 outliers)
Reward range: [6.50, 12.61], mean: 9.72
  Created 11 candidate models for data size 257
  rf-m: R2 = -0.021 (std: 0.106)
  rf-l: R2 = -0.010 (std: 0.110)
  gb-m: R2 = 0.004 (std: 0.169)
  gb-l: R2 = 0.003 (std: 0.161)
  xgb-m: R2 = -0.108 (std: 0.186)
  knn-m: R2 = -0.024 (std: 0.119)
  knn-tuned: R2 = -0.024 (std: 0.119)
  mlp-m: R2 = -1.129 (std: 0.805)
  svr-rbf: R2 = -0.053 (std: 0.092)
  svr-poly: R2 = -0.053 (std: 0.092)
  ridge: R2 = -0.094 (std: 0.091)

Model-based training with 2 models
Best R2: 0.004, Mean R2: -0.137
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9791, entropy=0.9774, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2628
  Round 1/3: Mean predicted reward = 9.680
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9756, entropy=0.9512, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3306
  Round 2/3: Mean predicted reward = 9.660
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9707, entropy=0.9315, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3864
  Round 3/3: Mean predicted reward = 9.710

  === Progress Analysis ===
  Status: NORMAL

--- Round 7 Results ---
  Mean Oracle Reward: 9.867
  Min Oracle Reward: 4.548
  Max Oracle Reward: 11.441
  Std Oracle Reward: 1.247
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -0.137, Max: 0.004, Count: 11
  Total Sequences Evaluated: 274

======================================================================
EXPERIMENT ROUND 8/30
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.080
Total data collected: 274

--- Round 8 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.080

--- Generated Sequences (Diversity: 1.000) ---
  CACTCATGGTAG
  ACGTGGGAATCC
  AGCCTGAGTCTA
  GGGACCTTCAGA
  TCCCAATAGGGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.482
  Max reward: 11.922
  With intrinsic bonuses: 9.597

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9779, entropy=0.9191, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1711

=== Surrogate Model Training ===
Total samples: 306

Training on 289 samples (removed 17 outliers)
Reward range: [6.45, 12.61], mean: 9.70
  Created 11 candidate models for data size 289
  rf-m: R2 = -0.001 (std: 0.095)
  rf-l: R2 = 0.019 (std: 0.088)
  gb-m: R2 = 0.047 (std: 0.054)
  gb-l: R2 = 0.053 (std: 0.053)
  xgb-m: R2 = -0.059 (std: 0.206)
  knn-m: R2 = -0.069 (std: 0.076)
  knn-tuned: R2 = -0.069 (std: 0.076)
  mlp-m: R2 = -0.878 (std: 0.565)
  svr-rbf: R2 = -0.030 (std: 0.108)
  svr-poly: R2 = -0.030 (std: 0.108)
  ridge: R2 = -0.086 (std: 0.073)

Model-based training with 3 models
Best R2: 0.053, Mean R2: -0.100
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9739, entropy=0.9171, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1727
  Round 1/3: Mean predicted reward = 9.699
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9775, entropy=0.9086, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1621
  Round 2/3: Mean predicted reward = 9.683
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9757, entropy=0.8917, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1303
  Round 3/3: Mean predicted reward = 9.621

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 8 Results ---
  Mean Oracle Reward: 9.487
  Min Oracle Reward: 5.786
  Max Oracle Reward: 11.690
  Std Oracle Reward: 1.249
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: -0.100, Max: 0.053, Count: 11
  Total Sequences Evaluated: 306

======================================================================
EXPERIMENT ROUND 9/30
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.065
Total data collected: 306

--- Round 9 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.065

--- Generated Sequences (Diversity: 1.000) ---
  AGATCCGTGCGA
  CGGACCGTTTAA
  AGATCTGCCGAT
  GCACCGTATAGG
  ACTATCGCGGGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.684
  Max reward: 12.473
  With intrinsic bonuses: 9.694

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9774, entropy=0.8927, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0537

=== Surrogate Model Training ===
Total samples: 338

Training on 320 samples (removed 18 outliers)
Reward range: [6.45, 12.61], mean: 9.72
  Created 14 candidate models for data size 320
  rf-tuned-l: R2 = 0.043 (std: 0.074)
  rf-tuned-xl: R2 = 0.053 (std: 0.049)
  gb-tuned-l: R2 = 0.009 (std: 0.112)
  gb-tuned-xl: R2 = 0.011 (std: 0.109)
  xgb-xl: R2 = 0.037 (std: 0.058)
  xgb-l: R2 = 0.037 (std: 0.058)
  mlp-adaptive-xl: R2 = -1.087 (std: 0.516)
  mlp-l: R2 = -0.859 (std: 0.528)
  svr-rbf-xl: R2 = -0.011 (std: 0.115)
  svr-poly-l: R2 = -0.011 (std: 0.115)
  knn-tuned-sqrt: R2 = 0.002 (std: 0.125)
  knn-tuned-l: R2 = 0.002 (std: 0.125)
  ridge: R2 = -0.077 (std: 0.080)
  gp: R2 = -71.676 (std: 10.375)

Model-based training with 8 models
Best R2: 0.053, Mean R2: -5.252
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9761, entropy=0.8842, kl_div=0.0000
    Epoch 1: policy_loss=-0.0121, value_loss=0.9761, entropy=0.8836, kl_div=0.0411
  Round 1/3: Mean predicted reward = 9.726
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9808, entropy=0.8968, kl_div=0.0000
    Epoch 1: policy_loss=-0.0024, value_loss=0.9808, entropy=0.8972, kl_div=0.0218
  Round 2/3: Mean predicted reward = 9.581
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9830, entropy=0.8932, kl_div=0.0000
    Epoch 1: policy_loss=-0.0071, value_loss=0.9830, entropy=0.8949, kl_div=-0.0058
  Round 3/3: Mean predicted reward = 9.655

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 9 Results ---
  Mean Oracle Reward: 9.634
  Min Oracle Reward: 3.212
  Max Oracle Reward: 12.291
  Std Oracle Reward: 1.759
  Sequence Diversity: 1.000
  Models Used: 8
  Model R² - Mean: -5.252, Max: 0.053, Count: 14
  Total Sequences Evaluated: 338

======================================================================
EXPERIMENT ROUND 10/30
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 338

--- Round 10 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTGTGACACCTA
  AGGTCTAACGGC
  TCCTGCAAAGGG
  TATGACCGCTGA
  AATTGCGCGCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.257
  Max reward: 12.067
  With intrinsic bonuses: 9.287

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9842, entropy=0.8883, kl_div=0.0000
    Epoch 1: policy_loss=-0.0327, value_loss=0.9840, entropy=0.9066, kl_div=-0.2229

=== Surrogate Model Training ===
Total samples: 370

Training on 350 samples (removed 20 outliers)
Reward range: [6.45, 12.61], mean: 9.72
  Created 14 candidate models for data size 350
  rf-tuned-l: R2 = 0.044 (std: 0.139)
  rf-tuned-xl: R2 = 0.052 (std: 0.124)
  gb-tuned-l: R2 = 0.069 (std: 0.081)
  gb-tuned-xl: R2 = 0.068 (std: 0.083)
  xgb-xl: R2 = -0.038 (std: 0.237)
  xgb-l: R2 = -0.038 (std: 0.237)
  mlp-adaptive-xl: R2 = -0.876 (std: 0.423)
  mlp-l: R2 = -0.907 (std: 0.777)
  svr-rbf-xl: R2 = 0.016 (std: 0.120)
  svr-poly-l: R2 = 0.016 (std: 0.120)
  knn-tuned-sqrt: R2 = 0.014 (std: 0.164)
  knn-tuned-l: R2 = 0.014 (std: 0.164)
  ridge: R2 = -0.070 (std: 0.091)
  gp: R2 = -73.429 (std: 12.871)

Model-based training with 8 models
Best R2: 0.069, Mean R2: -5.362
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9814, entropy=0.9241, kl_div=0.0000
    Epoch 1: policy_loss=-0.0582, value_loss=0.9812, entropy=0.9303, kl_div=-0.0349
  Round 1/3: Mean predicted reward = 9.793
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9780, entropy=0.9335, kl_div=0.0000
    Epoch 1: policy_loss=-0.0568, value_loss=0.9778, entropy=0.9367, kl_div=-0.0703
  Round 2/3: Mean predicted reward = 9.746
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9729, entropy=0.9366, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0617
  Round 3/3: Mean predicted reward = 9.704

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 10 Results ---
  Mean Oracle Reward: 9.305
  Min Oracle Reward: 0.000
  Max Oracle Reward: 12.093
  Std Oracle Reward: 2.108
  Sequence Diversity: 1.000
  Models Used: 8
  Model R² - Mean: -5.362, Max: 0.069, Count: 14
  Total Sequences Evaluated: 370

======================================================================
EXPERIMENT ROUND 11/30
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 370

--- Round 11 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AGTCGAAGGCTC
  AGTGGTCGACAC
  TGGTCGGACACA
  CGGTACCTGAAG
  CTAACCTTAGGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.150
  Max reward: 11.963
  With intrinsic bonuses: 10.211

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9726, entropy=0.9321, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0565

=== Surrogate Model Training ===
Total samples: 402

Training on 381 samples (removed 21 outliers)
Reward range: [6.50, 12.61], mean: 9.77
  Created 14 candidate models for data size 381
  rf-tuned-l: R2 = 0.070 (std: 0.046)
  rf-tuned-xl: R2 = 0.066 (std: 0.060)
  gb-tuned-l: R2 = 0.067 (std: 0.068)
  gb-tuned-xl: R2 = 0.067 (std: 0.068)
  xgb-xl: R2 = 0.003 (std: 0.142)
  xgb-l: R2 = 0.003 (std: 0.142)
  mlp-adaptive-xl: R2 = -0.804 (std: 0.307)
  mlp-l: R2 = -0.753 (std: 0.227)
  svr-rbf-xl: R2 = 0.038 (std: 0.082)
  svr-poly-l: R2 = 0.038 (std: 0.082)
  knn-tuned-sqrt: R2 = -0.034 (std: 0.081)
  knn-tuned-l: R2 = -0.034 (std: 0.081)
  ridge: R2 = -0.046 (std: 0.064)
  gp: R2 = -74.878 (std: 12.836)

Model-based training with 8 models
Best R2: 0.070, Mean R2: -5.443
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.9278, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1998
  Round 1/3: Mean predicted reward = 9.881
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.9118, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2355
  Round 2/3: Mean predicted reward = 9.932
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9736, entropy=0.8940, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3976
  Round 3/3: Mean predicted reward = 9.792

  === Progress Analysis ===
  Status: NORMAL

--- Round 11 Results ---
  Mean Oracle Reward: 10.148
  Min Oracle Reward: 7.906
  Max Oracle Reward: 11.752
  Std Oracle Reward: 1.002
  Sequence Diversity: 1.000
  Models Used: 8
  Model R² - Mean: -5.443, Max: 0.070, Count: 14
  Total Sequences Evaluated: 402

======================================================================
EXPERIMENT ROUND 12/30
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 402

--- Round 12 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CATAGGGCTTCA
  ACGTTCGGTAAC
  GCGCATGAACTG
  GCTGGCATACAG
  AACCGGTTGAGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.868
  Max reward: 12.949
  With intrinsic bonuses: 9.819

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9801, entropy=0.8716, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1876

=== Surrogate Model Training ===
Total samples: 434

Training on 411 samples (removed 23 outliers)
Reward range: [6.50, 12.61], mean: 9.80
  Created 14 candidate models for data size 411
  rf-tuned-l: R2 = 0.062 (std: 0.055)
  rf-tuned-xl: R2 = 0.070 (std: 0.058)
  gb-tuned-l: R2 = 0.064 (std: 0.057)
  gb-tuned-xl: R2 = 0.065 (std: 0.058)
  xgb-xl: R2 = 0.029 (std: 0.108)
  xgb-l: R2 = 0.029 (std: 0.108)
  mlp-adaptive-xl: R2 = -0.742 (std: 0.223)
  mlp-l: R2 = -0.755 (std: 0.177)
  svr-rbf-xl: R2 = 0.053 (std: 0.085)
  svr-poly-l: R2 = 0.053 (std: 0.085)
  knn-tuned-sqrt: R2 = 0.001 (std: 0.119)
  knn-tuned-l: R2 = 0.001 (std: 0.119)
  ridge: R2 = -0.039 (std: 0.036)
  gp: R2 = -74.268 (std: 10.647)

Model-based training with 10 models
Best R2: 0.070, Mean R2: -5.384
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9736, entropy=0.8645, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2764
  Round 1/3: Mean predicted reward = 9.828
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9712, entropy=0.8530, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3379
  Round 2/3: Mean predicted reward = 9.918
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9760, entropy=0.8432, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3698
  Round 3/3: Mean predicted reward = 9.868

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 12 Results ---
  Mean Oracle Reward: 9.853
  Min Oracle Reward: 4.083
  Max Oracle Reward: 12.635
  Std Oracle Reward: 1.759
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -5.384, Max: 0.070, Count: 14
  Total Sequences Evaluated: 434

======================================================================
EXPERIMENT ROUND 13/30
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 434

--- Round 13 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCGCAAGCTTCG
  GCCCCAGGATTG
  TTAGCCAGGCGA
  TGTGGCACCACG
  ACTCGAGGGTAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.240
  Max reward: 12.108
  With intrinsic bonuses: 9.208

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9768, entropy=0.8092, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1790

=== Surrogate Model Training ===
Total samples: 466

Training on 441 samples (removed 25 outliers)
Reward range: [6.50, 12.61], mean: 9.79
  Created 14 candidate models for data size 441
  rf-tuned-l: R2 = 0.087 (std: 0.056)
  rf-tuned-xl: R2 = 0.086 (std: 0.052)
  gb-tuned-l: R2 = 0.130 (std: 0.079)
  gb-tuned-xl: R2 = 0.131 (std: 0.080)
  xgb-xl: R2 = 0.058 (std: 0.109)
  xgb-l: R2 = 0.058 (std: 0.109)
  mlp-adaptive-xl: R2 = -0.637 (std: 0.368)
  mlp-l: R2 = -0.586 (std: 0.288)
  svr-rbf-xl: R2 = 0.064 (std: 0.072)
  svr-poly-l: R2 = 0.064 (std: 0.072)
  knn-tuned-sqrt: R2 = 0.039 (std: 0.131)
  knn-tuned-l: R2 = 0.039 (std: 0.131)
  ridge: R2 = -0.033 (std: 0.032)
  gp: R2 = -74.302 (std: 12.674)

Model-based training with 10 models
Best R2: 0.131, Mean R2: -5.343
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9732, entropy=0.8152, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2027
  Round 1/3: Mean predicted reward = 9.826
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9753, entropy=0.8126, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1942
  Round 2/3: Mean predicted reward = 9.870
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9764, entropy=0.7941, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1868
  Round 3/3: Mean predicted reward = 9.812

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 13 Results ---
  Mean Oracle Reward: 9.217
  Min Oracle Reward: 0.000
  Max Oracle Reward: 11.756
  Std Oracle Reward: 2.176
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -5.343, Max: 0.131, Count: 14
  Total Sequences Evaluated: 466

======================================================================
EXPERIMENT ROUND 14/30
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 466

--- Round 14 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGGCCATGATCC
  GCACGACGTAGT
  CAGTTTCGCAGA
  TCCGGGAATGCC
  GGCTAGTATCCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.532
  Max reward: 12.286
  With intrinsic bonuses: 9.569

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9775, entropy=0.7858, kl_div=0.0000
    Epoch 1: policy_loss=-0.0012, value_loss=0.9774, entropy=0.7842, kl_div=0.0417

=== Surrogate Model Training ===
Total samples: 498

Training on 471 samples (removed 27 outliers)
Reward range: [6.50, 12.61], mean: 9.79
  Created 14 candidate models for data size 471
  rf-tuned-l: R2 = 0.116 (std: 0.067)
  rf-tuned-xl: R2 = 0.097 (std: 0.063)
  gb-tuned-l: R2 = 0.106 (std: 0.056)
  gb-tuned-xl: R2 = 0.107 (std: 0.057)
  xgb-xl: R2 = 0.069 (std: 0.108)
  xgb-l: R2 = 0.069 (std: 0.108)
  mlp-adaptive-xl: R2 = -0.653 (std: 0.208)
  mlp-l: R2 = -0.664 (std: 0.274)
  svr-rbf-xl: R2 = 0.087 (std: 0.095)
  svr-poly-l: R2 = 0.087 (std: 0.095)
  knn-tuned-sqrt: R2 = 0.039 (std: 0.094)
  knn-tuned-l: R2 = 0.039 (std: 0.094)
  ridge: R2 = -0.041 (std: 0.038)
  gp: R2 = -72.422 (std: 9.349)

Model-based training with 10 models
Best R2: 0.116, Mean R2: -5.212
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9753, entropy=0.7891, kl_div=0.0000
    Epoch 1: policy_loss=-0.0049, value_loss=0.9753, entropy=0.7898, kl_div=-0.0004
  Round 1/3: Mean predicted reward = 9.793
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.7809, kl_div=0.0000
    Epoch 1: policy_loss=-0.0087, value_loss=0.9693, entropy=0.7820, kl_div=-0.0061
  Round 2/3: Mean predicted reward = 9.772
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9746, entropy=0.7684, kl_div=0.0000
    Epoch 1: policy_loss=-0.0134, value_loss=0.9746, entropy=0.7683, kl_div=0.0264
  Round 3/3: Mean predicted reward = 9.781

  === Progress Analysis ===
  Status: NORMAL

--- Round 14 Results ---
  Mean Oracle Reward: 9.542
  Min Oracle Reward: 4.899
  Max Oracle Reward: 12.364
  Std Oracle Reward: 1.611
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -5.212, Max: 0.116, Count: 14
  Total Sequences Evaluated: 498

======================================================================
EXPERIMENT ROUND 15/30
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 498

--- Round 15 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGAGAGATTCCC
  CAAAGTCTGCGT
  TGACTGGAACGC
  CACCGGATTGCG
  TAACTGGACCGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.653
  Max reward: 12.136
  With intrinsic bonuses: 9.589

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9760, entropy=0.7853, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2536

=== Surrogate Model Training ===
Total samples: 530

Training on 498 samples (removed 32 outliers)
Reward range: [6.60, 12.61], mean: 9.82
  Created 14 candidate models for data size 498
  rf-tuned-l: R2 = 0.075 (std: 0.055)
  rf-tuned-xl: R2 = 0.056 (std: 0.070)
  gb-tuned-l: R2 = 0.040 (std: 0.118)
  gb-tuned-xl: R2 = 0.042 (std: 0.120)
  xgb-xl: R2 = 0.014 (std: 0.136)
  xgb-l: R2 = 0.014 (std: 0.136)
  mlp-adaptive-xl: R2 = -0.719 (std: 0.399)
  mlp-l: R2 = -0.575 (std: 0.194)
  svr-rbf-xl: R2 = 0.063 (std: 0.107)
  svr-poly-l: R2 = 0.063 (std: 0.107)
  knn-tuned-sqrt: R2 = 0.008 (std: 0.090)
  knn-tuned-l: R2 = 0.008 (std: 0.090)
  ridge: R2 = -0.047 (std: 0.035)
  gp: R2 = -77.882 (std: 8.283)

Model-based training with 10 models
Best R2: 0.075, Mean R2: -5.631
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9748, entropy=0.7912, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1901
  Round 1/3: Mean predicted reward = 9.868
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9791, entropy=0.8004, kl_div=0.0000
    Epoch 1: policy_loss=-0.0434, value_loss=0.9789, entropy=0.8080, kl_div=0.0311
  Round 2/3: Mean predicted reward = 9.628
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9737, entropy=0.8073, kl_div=0.0000
    Epoch 1: policy_loss=-0.0367, value_loss=0.9736, entropy=0.8205, kl_div=-0.1414
  Round 3/3: Mean predicted reward = 9.855

  === Progress Analysis ===
  Status: NORMAL

--- Round 15 Results ---
  Mean Oracle Reward: 9.636
  Min Oracle Reward: 4.194
  Max Oracle Reward: 12.019
  Std Oracle Reward: 1.392
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -5.631, Max: 0.075, Count: 14
  Total Sequences Evaluated: 530

======================================================================
EXPERIMENT ROUND 16/30
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 530
  Consistent improvement, increasing LR to 0.000327

--- Round 16 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGCTAGCGTCAC
  GGACCATTCGAG
  TCCAATGCGGTA
  GTGAGAGCCCCT
  GAAAGGCTCGCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.700
  Max reward: 11.811
  With intrinsic bonuses: 9.678

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9740, entropy=0.8300, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1653

=== Surrogate Model Training ===
Total samples: 562

Training on 529 samples (removed 33 outliers)
Reward range: [6.60, 12.61], mean: 9.82
  Created 13 candidate models for data size 529
  rf-tuned-l: R2 = 0.104 (std: 0.033)
  rf-tuned-xl: R2 = 0.083 (std: 0.045)
  gb-tuned-l: R2 = 0.097 (std: 0.074)
  gb-tuned-xl: R2 = 0.097 (std: 0.074)
  xgb-xl: R2 = 0.100 (std: 0.073)
  xgb-l: R2 = 0.100 (std: 0.073)
  mlp-adaptive-xl: R2 = -0.548 (std: 0.173)
  mlp-l: R2 = -0.591 (std: 0.189)
  svr-rbf-xl: R2 = 0.102 (std: 0.098)
  svr-poly-l: R2 = 0.102 (std: 0.098)
  knn-tuned-sqrt: R2 = 0.020 (std: 0.080)
  knn-tuned-l: R2 = 0.020 (std: 0.080)
  ridge: R2 = -0.037 (std: 0.023)

Model-based training with 10 models
Best R2: 0.104, Mean R2: -0.027
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9814, entropy=0.8354, kl_div=0.0000
    Epoch 1: policy_loss=-0.0111, value_loss=0.9812, entropy=0.8388, kl_div=0.0296
  Round 1/3: Mean predicted reward = 9.723
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9764, entropy=0.8307, kl_div=0.0000
    Epoch 1: policy_loss=-0.0222, value_loss=0.9763, entropy=0.8350, kl_div=-0.1467
  Round 2/3: Mean predicted reward = 9.745
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=0.8417, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0797
  Round 3/3: Mean predicted reward = 9.824

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 16 Results ---
  Mean Oracle Reward: 9.763
  Min Oracle Reward: 4.526
  Max Oracle Reward: 12.001
  Std Oracle Reward: 1.517
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -0.027, Max: 0.104, Count: 13
  Total Sequences Evaluated: 562

======================================================================
EXPERIMENT ROUND 17/30
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 562
  Performance plateaued, reducing LR to 0.000100

--- Round 17 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTCACTAGCGGC
  CCGACGGATCTG
  GCACGTATTCGA
  TGGCGACTCAGC
  TGCGCATACTGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.932
  Max reward: 11.159
  With intrinsic bonuses: 9.920

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9719, entropy=0.8448, kl_div=0.0000
    Epoch 1: policy_loss=-0.0262, value_loss=0.9719, entropy=0.8428, kl_div=0.0481

=== Surrogate Model Training ===
Total samples: 594

Training on 557 samples (removed 37 outliers)
Reward range: [6.68, 12.61], mean: 9.86
  Created 13 candidate models for data size 557
  rf-tuned-l: R2 = 0.072 (std: 0.027)
  rf-tuned-xl: R2 = 0.079 (std: 0.021)
  gb-tuned-l: R2 = 0.064 (std: 0.077)
  gb-tuned-xl: R2 = 0.065 (std: 0.079)
  xgb-xl: R2 = 0.088 (std: 0.073)
  xgb-l: R2 = 0.088 (std: 0.073)
  mlp-adaptive-xl: R2 = -0.510 (std: 0.142)
  mlp-l: R2 = -0.468 (std: 0.188)
  svr-rbf-xl: R2 = 0.092 (std: 0.077)
  svr-poly-l: R2 = 0.092 (std: 0.077)
  knn-tuned-sqrt: R2 = 0.026 (std: 0.062)
  knn-tuned-l: R2 = 0.026 (std: 0.062)
  ridge: R2 = -0.026 (std: 0.024)

Model-based training with 10 models
Best R2: 0.092, Mean R2: -0.024
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9733, entropy=0.8325, kl_div=0.0000
    Epoch 1: policy_loss=-0.0259, value_loss=0.9733, entropy=0.8336, kl_div=-0.0350
  Round 1/3: Mean predicted reward = 9.760
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9761, entropy=0.8277, kl_div=0.0000
    Epoch 1: policy_loss=-0.0133, value_loss=0.9760, entropy=0.8285, kl_div=-0.0474
  Round 2/3: Mean predicted reward = 9.840
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9740, entropy=0.8340, kl_div=0.0000
    Epoch 1: policy_loss=-0.0223, value_loss=0.9740, entropy=0.8325, kl_div=0.0251
  Round 3/3: Mean predicted reward = 9.788

  === Progress Analysis ===
  Status: NORMAL

--- Round 17 Results ---
  Mean Oracle Reward: 9.945
  Min Oracle Reward: 5.649
  Max Oracle Reward: 11.298
  Std Oracle Reward: 1.167
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -0.024, Max: 0.092, Count: 13
  Total Sequences Evaluated: 594

======================================================================
EXPERIMENT ROUND 18/30
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 594
  Consistent improvement, increasing LR to 0.000132

--- Round 18 Configuration ---
Learning rate: 0.000132
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGATCACGCGTA
  ACGCCTAGGCTG
  CCAGTAGATGCG
  CGGCTATATACG
  GATGCGCCATAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.004
  Max reward: 12.564
  With intrinsic bonuses: 9.958

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=0.8313, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1308

=== Surrogate Model Training ===
Total samples: 626

Training on 588 samples (removed 38 outliers)
Reward range: [6.65, 12.73], mean: 9.86
  Created 13 candidate models for data size 588
  rf-tuned-l: R2 = 0.062 (std: 0.034)
  rf-tuned-xl: R2 = 0.096 (std: 0.013)
  gb-tuned-l: R2 = 0.054 (std: 0.080)
  gb-tuned-xl: R2 = 0.054 (std: 0.080)
  xgb-xl: R2 = 0.052 (std: 0.097)
  xgb-l: R2 = 0.052 (std: 0.097)
  mlp-adaptive-xl: R2 = -0.441 (std: 0.167)
  mlp-l: R2 = -0.488 (std: 0.147)
  svr-rbf-xl: R2 = 0.089 (std: 0.081)
  svr-poly-l: R2 = 0.089 (std: 0.081)
  knn-tuned-sqrt: R2 = -0.006 (std: 0.094)
  knn-tuned-l: R2 = -0.006 (std: 0.094)
  ridge: R2 = -0.031 (std: 0.031)

Model-based training with 8 models
Best R2: 0.096, Mean R2: -0.033
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9751, entropy=0.8385, kl_div=0.0000
    Epoch 1: policy_loss=-0.0092, value_loss=0.9750, entropy=0.8365, kl_div=0.0416
  Round 1/3: Mean predicted reward = 9.836
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9744, entropy=0.8321, kl_div=0.0000
    Epoch 1: policy_loss=-0.0388, value_loss=0.9744, entropy=0.8306, kl_div=0.0358
  Round 2/3: Mean predicted reward = 9.809
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9734, entropy=0.8404, kl_div=0.0000
    Epoch 1: policy_loss=-0.0366, value_loss=0.9733, entropy=0.8418, kl_div=-0.0780
  Round 3/3: Mean predicted reward = 9.930

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 18 Results ---
  Mean Oracle Reward: 9.973
  Min Oracle Reward: 2.763
  Max Oracle Reward: 12.879
  Std Oracle Reward: 1.851
  Sequence Diversity: 1.000
  Models Used: 8
  Model R² - Mean: -0.033, Max: 0.096, Count: 13
  Total Sequences Evaluated: 626

======================================================================
EXPERIMENT ROUND 19/30
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 626
  Consistent improvement, increasing LR to 0.000045

--- Round 19 Configuration ---
Learning rate: 0.000045
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCCGCAAGTGGA
  GTCACCTGACGG
  GGACGCCTTAGA
  GTTCGCGCAAGC
  TCCACGGATCGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.864
  Max reward: 11.264
  With intrinsic bonuses: 9.895

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9732, entropy=0.8424, kl_div=0.0000
    Epoch 1: policy_loss=-0.0140, value_loss=0.9732, entropy=0.8430, kl_div=-0.0198

=== Surrogate Model Training ===
Total samples: 658

Training on 622 samples (removed 36 outliers)
Reward range: [6.60, 13.02], mean: 9.87
  Created 13 candidate models for data size 622
  rf-tuned-l: R2 = 0.081 (std: 0.036)
  rf-tuned-xl: R2 = 0.093 (std: 0.052)
  gb-tuned-l: R2 = 0.075 (std: 0.053)
  gb-tuned-xl: R2 = 0.076 (std: 0.054)
  xgb-xl: R2 = 0.075 (std: 0.096)
  xgb-l: R2 = 0.075 (std: 0.096)
  mlp-adaptive-xl: R2 = -0.429 (std: 0.099)
  mlp-l: R2 = -0.450 (std: 0.122)
  svr-rbf-xl: R2 = 0.105 (std: 0.089)
  svr-poly-l: R2 = 0.105 (std: 0.089)
  knn-tuned-sqrt: R2 = 0.032 (std: 0.084)
  knn-tuned-l: R2 = 0.032 (std: 0.084)
  ridge: R2 = -0.035 (std: 0.039)

Model-based training with 10 models
Best R2: 0.105, Mean R2: -0.013
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9730, entropy=0.8404, kl_div=0.0000
    Epoch 1: policy_loss=-0.0129, value_loss=0.9730, entropy=0.8405, kl_div=-0.0061
  Round 1/3: Mean predicted reward = 9.943
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9722, entropy=0.8122, kl_div=0.0000
    Epoch 1: policy_loss=-0.0074, value_loss=0.9722, entropy=0.8116, kl_div=0.0158
  Round 2/3: Mean predicted reward = 9.889
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9712, entropy=0.8360, kl_div=0.0000
    Epoch 1: policy_loss=-0.0185, value_loss=0.9712, entropy=0.8350, kl_div=0.0344
  Round 3/3: Mean predicted reward = 9.823

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 19 Results ---
  Mean Oracle Reward: 9.946
  Min Oracle Reward: 6.677
  Max Oracle Reward: 11.354
  Std Oracle Reward: 1.273
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -0.013, Max: 0.105, Count: 13
  Total Sequences Evaluated: 658

  Early stopping: Converged at round 19

======================================================================
DyNA PPO ALGORITHM COMPLETE!
======================================================================
Total rounds executed: 19
Total sequences evaluated: 658
Best mean reward: 10.246 (achieved at round 4)

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 19
Final Mean Reward: 9.9456
Best Mean Reward: 10.2461
Best Max Reward: 14.0275
Initial Lr: 0.0003
Final Lr: 0.0000
Total Updates: 104
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
  GGCCGGCCCGGC: 12.180
  GGCCGGCCCGGC: 12.058
  GGCCGGCCCGGC: 12.326
  GGCCGGCCCGGC: 11.987
  GGCCGGCCCGGC: 12.289

Stochastic (Exploration):
  GCGGCGCGTCTG: 10.147
  CGAGAGGCGCGC: 9.337
  GGACGGGGACGC: 8.230
  GGCCGTGGTCCC: 10.108
  CGGGCCGCCCGG: 9.799

Final Performance:
  Mean reward: 10.846
  Max reward: 12.326
  Std reward: 1.417

Best sequence found: GGCCGGCCCGGC
   Reward: 12.326

======================================================================
Training complete! Check 'learning_curves.png' and 'training_metrics.json'
======================================================================