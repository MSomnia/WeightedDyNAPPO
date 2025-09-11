======================================================================
EXPERIMENT ROUND 7/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.190
Total data collected: 242

--- Round 7 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0100
Exploration rate: 0.190

--- Generated Sequences (Diversity: 1.000) ---
  GGGCTCGAAATC
  AGCGTCGACTTA
  ATCGGACTGGCA
  GCGCAGACTTGA
  ATATCGGACTCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.243
  Max reward: 12.396
  With intrinsic bonuses: 10.326

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=1.1324, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0991

=== Surrogate Model Training ===
Total samples: 274

Training on 256 samples (removed 18 outliers)
Reward range: [5.37, 13.37], mean: 9.58
  Created 11 candidate models for data size 256
Current R2 threshold: -0.3
  rf-m: R2 = -0.122 (std: 0.035)
  rf-l: R2 = -0.130 (std: 0.053)
  gb-m: R2 = -0.179 (std: 0.093)
  gb-l: R2 = -0.179 (std: 0.088)
  xgb-m: R2 = -0.277 (std: 0.051)
  knn-m: R2 = -0.247 (std: 0.031)
  knn-tuned: R2 = -0.247 (std: 0.031)
  mlp-m: R2 = -0.509 (std: 0.306)
  svr-rbf: R2 = -0.035 (std: 0.047)
  svr-poly: R2 = -0.035 (std: 0.047)
  ridge: R2 = -0.081 (std: 0.039)

Model-based training with 10 models
Best R2: -0.035, Mean R2: -0.186
Running 2 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.103 rf-l:0.102 gb-m:0.097 gb-l:0.097 xgb-m:0.088 knn-m:0.091 knn-tuned:0.091 svr-rbf:0.112 svr-poly:0.112 ridge:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9712, entropy=1.1400, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.697
    Using performance-based weights
    Model weights: rf-m:0.103 rf-l:0.102 gb-m:0.097 gb-l:0.097 xgb-m:0.088 knn-m:0.091 knn-tuned:0.091 svr-rbf:0.112 svr-poly:0.112 ridge:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9715, entropy=1.1329, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.857

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 7 Results ---
  Mean Oracle Reward: 10.195
  Min Oracle Reward: 7.591
  Max Oracle Reward: 12.540
  Std Oracle Reward: 1.187
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: -0.186, Max: -0.035, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 274

======================================================================
EXPERIMENT ROUND 8/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.080
Total data collected: 274
  Consistent improvement, increasing LR to 0.000132

--- Round 8 Configuration ---
Learning rate: 0.000132
Entropy coefficient: 0.0050
Exploration rate: 0.080

--- Generated Sequences (Diversity: 1.000) ---
  TTAGACCAGGGC
  CGACCAGTTGGA
  GATAGGTCCATC
  TGCACCGGGTAC
  GGTAGCTCAGCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.745
  Max reward: 12.662
  With intrinsic bonuses: 9.793

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9718, entropy=1.0998, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1082

=== Surrogate Model Training ===
Total samples: 306

Training on 283 samples (removed 23 outliers)
Reward range: [5.76, 13.37], mean: 9.68
  Created 11 candidate models for data size 283
Current R2 threshold: -0.3
  rf-m: R2 = -0.034 (std: 0.091)
  rf-l: R2 = -0.031 (std: 0.096)
  gb-m: R2 = -0.128 (std: 0.155)
  gb-l: R2 = -0.138 (std: 0.156)
  xgb-m: R2 = -0.220 (std: 0.157)
  knn-m: R2 = -0.136 (std: 0.138)
  knn-tuned: R2 = -0.136 (std: 0.138)
  mlp-m: R2 = -0.418 (std: 0.262)
  svr-rbf: R2 = 0.006 (std: 0.097)
  svr-poly: R2 = 0.006 (std: 0.097)
  ridge: R2 = -0.060 (std: 0.043)

Model-based training with 10 models
Best R2: 0.006, Mean R2: -0.117
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.105 rf-l:0.105 gb-m:0.096 gb-l:0.095 xgb-m:0.087 knn-m:0.095 knn-tuned:0.095 svr-rbf:0.109 svr-poly:0.109 ridge:0.103
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9741, entropy=1.0909, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1027
  Round 1/3: Mean predicted reward = 9.813
    Using performance-based weights
    Model weights: rf-m:0.105 rf-l:0.105 gb-m:0.096 gb-l:0.095 xgb-m:0.087 knn-m:0.095 knn-tuned:0.095 svr-rbf:0.109 svr-poly:0.109 ridge:0.103
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9711, entropy=1.0807, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1197
  Round 2/3: Mean predicted reward = 9.758
    Using performance-based weights
    Model weights: rf-m:0.105 rf-l:0.105 gb-m:0.096 gb-l:0.095 xgb-m:0.087 knn-m:0.095 knn-tuned:0.095 svr-rbf:0.109 svr-poly:0.109 ridge:0.103
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=1.0806, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1106
  Round 3/3: Mean predicted reward = 9.754

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 8 Results ---
  Mean Oracle Reward: 9.755
  Min Oracle Reward: 4.187
  Max Oracle Reward: 12.381
  Std Oracle Reward: 1.510
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: -0.117, Max: 0.006, Count: 11
  Total Sequences Evaluated: 306

======================================================================
EXPERIMENT ROUND 9/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.065
Total data collected: 306

--- Round 9 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.065

--- Generated Sequences (Diversity: 1.000) ---
  AGTGGGCTACCA
  CATGGACTGGAC
  CCGTGGATCTAA
  ATGCCATCGGAT
  AGTAACCTGCGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.862
  Max reward: 12.226
  With intrinsic bonuses: 9.837

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=1.0727, kl_div=0.0000
    Epoch 1: policy_loss=-0.0004, value_loss=0.9689, entropy=1.0708, kl_div=0.0287

=== Surrogate Model Training ===
Total samples: 338

Training on 314 samples (removed 24 outliers)
Reward range: [5.76, 13.23], mean: 9.68
  Created 14 candidate models for data size 314
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.082 (std: 0.069)
  rf-tuned-xl: R2 = -0.077 (std: 0.075)
  gb-tuned-l: R2 = -0.104 (std: 0.110)
  gb-tuned-xl: R2 = -0.104 (std: 0.110)
  xgb-xl: R2 = -0.289 (std: 0.122)
  xgb-l: R2 = -0.289 (std: 0.122)
  mlp-adaptive-xl: R2 = -0.445 (std: 0.216)
  mlp-l: R2 = -0.568 (std: 0.262)
  svr-rbf-xl: R2 = -0.020 (std: 0.083)
  svr-poly-l: R2 = -0.020 (std: 0.083)
  knn-tuned-sqrt: R2 = -0.189 (std: 0.081)
  knn-tuned-l: R2 = -0.189 (std: 0.081)
  ridge: R2 = -0.081 (std: 0.030)
  gp: R2 = -60.731 (std: 9.145)

Model-based training with 11 models
Best R2: -0.020, Mean R2: -4.513
Running 2 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.095 rf-tuned-xl:0.096 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.077 xgb-l:0.077 svr-rbf-xl:0.101 svr-poly-l:0.101 knn-tuned-sqrt:0.085 knn-tuned-l:0.085 ridge:0.095
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=1.0912, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.834
    Using performance-based weights
    Model weights: rf-tuned-l:0.095 rf-tuned-xl:0.096 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.077 xgb-l:0.077 svr-rbf-xl:0.101 svr-poly-l:0.101 knn-tuned-sqrt:0.085 knn-tuned-l:0.085 ridge:0.095
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=1.0946, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.735

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 9 Results ---
  Mean Oracle Reward: 9.767
  Min Oracle Reward: 7.567
  Max Oracle Reward: 12.063
  Std Oracle Reward: 1.126
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -4.513, Max: -0.020, Count: 14
  Total Sequences Evaluated: 338

======================================================================
EXPERIMENT ROUND 10/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 338

--- Round 10 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGACACGGATGC
  ATCAGGGTCGCC
  CTCAGAGAGTTC
  TTATCAGAGGCC
  CTAACACGGTGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.622
  Max reward: 11.810
  With intrinsic bonuses: 9.616

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=1.0668, kl_div=0.0000
    Epoch 1: policy_loss=-0.0304, value_loss=0.9688, entropy=1.0664, kl_div=0.0262

=== Surrogate Model Training ===
Total samples: 370

Training on 342 samples (removed 28 outliers)
Reward range: [6.13, 12.58], mean: 9.72
  Created 14 candidate models for data size 342
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.039 (std: 0.053)
  rf-tuned-xl: R2 = -0.046 (std: 0.080)
  gb-tuned-l: R2 = -0.148 (std: 0.097)
  gb-tuned-xl: R2 = -0.148 (std: 0.097)
  xgb-xl: R2 = -0.175 (std: 0.179)
  xgb-l: R2 = -0.175 (std: 0.179)
  mlp-adaptive-xl: R2 = -0.464 (std: 0.277)
  mlp-l: R2 = -0.384 (std: 0.267)
  svr-rbf-xl: R2 = 0.002 (std: 0.100)
  svr-poly-l: R2 = 0.002 (std: 0.100)
  knn-tuned-sqrt: R2 = -0.142 (std: 0.086)
  knn-tuned-l: R2 = -0.142 (std: 0.086)
  ridge: R2 = -0.069 (std: 0.032)
  gp: R2 = -66.988 (std: 10.229)

Model-based training with 11 models
Best R2: 0.002, Mean R2: -4.923
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.096 rf-tuned-xl:0.096 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.084 xgb-l:0.084 svr-rbf-xl:0.100 svr-poly-l:0.100 knn-tuned-sqrt:0.087 knn-tuned-l:0.087 ridge:0.093
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9734, entropy=1.0702, kl_div=0.0000
    Epoch 1: policy_loss=-0.0426, value_loss=0.9734, entropy=1.0684, kl_div=0.0488
  Round 1/3: Mean predicted reward = 9.758
    Using performance-based weights
    Model weights: rf-tuned-l:0.096 rf-tuned-xl:0.096 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.084 xgb-l:0.084 svr-rbf-xl:0.100 svr-poly-l:0.100 knn-tuned-sqrt:0.087 knn-tuned-l:0.087 ridge:0.093
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9734, entropy=1.0522, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1939
  Round 2/3: Mean predicted reward = 9.761
    Using performance-based weights
    Model weights: rf-tuned-l:0.096 rf-tuned-xl:0.096 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.084 xgb-l:0.084 svr-rbf-xl:0.100 svr-poly-l:0.100 knn-tuned-sqrt:0.087 knn-tuned-l:0.087 ridge:0.093
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9722, entropy=1.0505, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2079
  Round 3/3: Mean predicted reward = 9.806

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 10 Results ---
  Mean Oracle Reward: 9.576
  Min Oracle Reward: 0.174
  Max Oracle Reward: 11.846
  Std Oracle Reward: 2.007
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -4.923, Max: 0.002, Count: 14
  Total Sequences Evaluated: 370

======================================================================
EXPERIMENT ROUND 11/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 370
  Performance plateaued, reducing LR to 0.000136

--- Round 11 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGAGCCATTGAT
  CCATTGGCCAGG
  GGTCTAGGACCA
  TCAATGGTCGCA
  CAGTAATGCGCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.942
  Max reward: 12.624
  With intrinsic bonuses: 9.889

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9745, entropy=1.0259, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1317

=== Surrogate Model Training ===
Total samples: 402

Training on 376 samples (removed 26 outliers)
Reward range: [5.90, 13.37], mean: 9.76
  Created 14 candidate models for data size 376
Current R2 threshold: -0.29
  rf-tuned-l: R2 = 0.015 (std: 0.089)
  rf-tuned-xl: R2 = 0.021 (std: 0.084)
  gb-tuned-l: R2 = -0.026 (std: 0.093)
  gb-tuned-xl: R2 = -0.026 (std: 0.093)
  xgb-xl: R2 = -0.084 (std: 0.191)
  xgb-l: R2 = -0.084 (std: 0.191)
  mlp-adaptive-xl: R2 = -0.278 (std: 0.174)
  mlp-l: R2 = -0.391 (std: 0.091)
  svr-rbf-xl: R2 = 0.023 (std: 0.116)
  svr-poly-l: R2 = 0.023 (std: 0.116)
  knn-tuned-sqrt: R2 = -0.111 (std: 0.126)
  knn-tuned-l: R2 = -0.111 (std: 0.126)
  ridge: R2 = -0.068 (std: 0.045)
  gp: R2 = -61.606 (std: 9.416)

Model-based training with 12 models
Best R2: 0.023, Mean R2: -4.479
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.089 rf-tuned-xl:0.090 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.081 xgb-l:0.081 mlp-adaptive-xl:0.067 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.079 knn-tuned-l:0.079 ridge:0.082
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=1.0279, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1503
  Round 1/3: Mean predicted reward = 9.863
    Using performance-based weights
    Model weights: rf-tuned-l:0.089 rf-tuned-xl:0.090 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.081 xgb-l:0.081 mlp-adaptive-xl:0.067 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.079 knn-tuned-l:0.079 ridge:0.082
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9706, entropy=1.0107, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1525
  Round 2/3: Mean predicted reward = 9.816
    Using performance-based weights
    Model weights: rf-tuned-l:0.089 rf-tuned-xl:0.090 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.081 xgb-l:0.081 mlp-adaptive-xl:0.067 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.079 knn-tuned-l:0.079 ridge:0.082
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9715, entropy=1.0019, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2077
  Round 3/3: Mean predicted reward = 9.827

  === Progress Analysis ===
  Status: NORMAL

--- Round 11 Results ---
  Mean Oracle Reward: 9.823
  Min Oracle Reward: 4.618
  Max Oracle Reward: 12.383
  Std Oracle Reward: 1.650
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: -4.479, Max: 0.023, Count: 14
  Total Sequences Evaluated: 402

======================================================================
EXPERIMENT ROUND 12/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 402

--- Round 12 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AGTCAATCGCGT
  GCTAATCGCATG
  ACGATCCGGTGC
  CGTGCGTCAACG
  CAGCAGTGCGTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.777
  Max reward: 12.337
  With intrinsic bonuses: 9.793

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9720, entropy=0.9905, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2117

=== Surrogate Model Training ===
Total samples: 434

Training on 406 samples (removed 28 outliers)
Reward range: [5.90, 13.37], mean: 9.78
  Created 14 candidate models for data size 406
Current R2 threshold: -0.27999999999999997
  rf-tuned-l: R2 = -0.010 (std: 0.092)
  rf-tuned-xl: R2 = 0.031 (std: 0.103)
  gb-tuned-l: R2 = -0.013 (std: 0.095)
  gb-tuned-xl: R2 = -0.013 (std: 0.095)
  xgb-xl: R2 = -0.138 (std: 0.198)
  xgb-l: R2 = -0.138 (std: 0.198)
  mlp-adaptive-xl: R2 = -0.307 (std: 0.133)
  mlp-l: R2 = -0.366 (std: 0.120)
  svr-rbf-xl: R2 = 0.033 (std: 0.106)
  svr-poly-l: R2 = 0.033 (std: 0.106)
  knn-tuned-sqrt: R2 = -0.081 (std: 0.161)
  knn-tuned-l: R2 = -0.081 (std: 0.161)
  ridge: R2 = -0.078 (std: 0.060)
  gp: R2 = -59.708 (std: 6.537)

Model-based training with 11 models
Best R2: 0.033, Mean R2: -4.345
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.098 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.082 xgb-l:0.082 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.087 knn-tuned-l:0.087 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9709, entropy=0.9785, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2461
  Round 1/3: Mean predicted reward = 9.896
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.098 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.082 xgb-l:0.082 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.087 knn-tuned-l:0.087 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9725, entropy=0.9575, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2403
  Round 2/3: Mean predicted reward = 9.788
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.098 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.082 xgb-l:0.082 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.087 knn-tuned-l:0.087 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9715, entropy=0.9430, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3308
  Round 3/3: Mean predicted reward = 9.857

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 12 Results ---
  Mean Oracle Reward: 9.835
  Min Oracle Reward: 4.465
  Max Oracle Reward: 12.458
  Std Oracle Reward: 1.806
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -4.345, Max: 0.033, Count: 14
  Total Sequences Evaluated: 434

======================================================================
EXPERIMENT ROUND 13/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 434

--- Round 13 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ATGGTATACCGC
  GACACTGGCAGT
  GAACTGTGGCCA
  GTGGTGCCACAA
  AGTCTCAGGACG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.795
  Max reward: 12.845
  With intrinsic bonuses: 9.799

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9722, entropy=0.9260, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1861

=== Surrogate Model Training ===
Total samples: 466

Training on 438 samples (removed 28 outliers)
Reward range: [5.90, 13.37], mean: 9.79
  Created 14 candidate models for data size 438
Current R2 threshold: -0.27
  rf-tuned-l: R2 = -0.005 (std: 0.127)
  rf-tuned-xl: R2 = 0.000 (std: 0.123)
  gb-tuned-l: R2 = 0.055 (std: 0.099)
  gb-tuned-xl: R2 = 0.055 (std: 0.099)
  xgb-xl: R2 = -0.099 (std: 0.165)
  xgb-l: R2 = -0.099 (std: 0.165)
  mlp-adaptive-xl: R2 = -0.276 (std: 0.166)
  mlp-l: R2 = -0.313 (std: 0.160)
  svr-rbf-xl: R2 = 0.039 (std: 0.127)
  svr-poly-l: R2 = 0.039 (std: 0.127)
  knn-tuned-sqrt: R2 = -0.128 (std: 0.172)
  knn-tuned-l: R2 = -0.128 (std: 0.172)
  ridge: R2 = -0.078 (std: 0.084)
  gp: R2 = -60.068 (std: 12.003)

Model-based training with 11 models
Best R2: 0.055, Mean R2: -4.358
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.093 rf-tuned-xl:0.094 gb-tuned-l:0.099 gb-tuned-xl:0.099 xgb-xl:0.085 xgb-l:0.085 svr-rbf-xl:0.097 svr-poly-l:0.097 knn-tuned-sqrt:0.082 knn-tuned-l:0.082 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9730, entropy=0.9270, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1470
  Round 1/3: Mean predicted reward = 9.830
    Using performance-based weights
    Model weights: rf-tuned-l:0.093 rf-tuned-xl:0.094 gb-tuned-l:0.099 gb-tuned-xl:0.099 xgb-xl:0.085 xgb-l:0.085 svr-rbf-xl:0.097 svr-poly-l:0.097 knn-tuned-sqrt:0.082 knn-tuned-l:0.082 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9702, entropy=0.9074, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1815
  Round 2/3: Mean predicted reward = 9.875
    Using performance-based weights
    Model weights: rf-tuned-l:0.093 rf-tuned-xl:0.094 gb-tuned-l:0.099 gb-tuned-xl:0.099 xgb-xl:0.085 xgb-l:0.085 svr-rbf-xl:0.097 svr-poly-l:0.097 knn-tuned-sqrt:0.082 knn-tuned-l:0.082 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9712, entropy=0.9039, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1731
  Round 3/3: Mean predicted reward = 9.878

  === Progress Analysis ===
  Status: NORMAL

--- Round 13 Results ---
  Mean Oracle Reward: 9.794
  Min Oracle Reward: 6.836
  Max Oracle Reward: 12.769
  Std Oracle Reward: 1.436
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -4.358, Max: 0.055, Count: 14
  Total Sequences Evaluated: 466

======================================================================
EXPERIMENT ROUND 14/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 466
  Performance plateaued, reducing LR to 0.000019

--- Round 14 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTTAGGGATCCA
  GCCGATACTGAT
  GTCAAACGGCTG
  CGGGGACATATC
  GCTGACGATCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.148
  Max reward: 13.903
  With intrinsic bonuses: 10.178

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9670, entropy=0.9045, kl_div=0.0000
    Epoch 1: policy_loss=0.0002, value_loss=0.9670, entropy=0.9032, kl_div=0.0210

=== Surrogate Model Training ===
Total samples: 498

Training on 468 samples (removed 30 outliers)
Reward range: [6.13, 13.37], mean: 9.81
  Created 14 candidate models for data size 468
Current R2 threshold: -0.26
  rf-tuned-l: R2 = 0.014 (std: 0.088)
  rf-tuned-xl: R2 = 0.017 (std: 0.061)
  gb-tuned-l: R2 = -0.015 (std: 0.123)
  gb-tuned-xl: R2 = -0.015 (std: 0.123)
  xgb-xl: R2 = -0.176 (std: 0.129)
  xgb-l: R2 = -0.176 (std: 0.129)
  mlp-adaptive-xl: R2 = -0.292 (std: 0.170)
  mlp-l: R2 = -0.273 (std: 0.180)
  svr-rbf-xl: R2 = 0.031 (std: 0.114)
  svr-poly-l: R2 = 0.031 (std: 0.114)
  knn-tuned-sqrt: R2 = -0.073 (std: 0.091)
  knn-tuned-l: R2 = -0.073 (std: 0.091)
  ridge: R2 = -0.064 (std: 0.074)
  gp: R2 = -59.118 (std: 6.929)

Model-based training with 11 models
Best R2: 0.031, Mean R2: -4.299
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.096 rf-tuned-xl:0.096 gb-tuned-l:0.094 gb-tuned-xl:0.094 xgb-xl:0.080 xgb-l:0.080 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.088 knn-tuned-l:0.088 ridge:0.089
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9728, entropy=0.8823, kl_div=0.0000
    Epoch 1: policy_loss=-0.0104, value_loss=0.9728, entropy=0.8812, kl_div=0.0268
  Round 1/3: Mean predicted reward = 9.798
    Using performance-based weights
    Model weights: rf-tuned-l:0.096 rf-tuned-xl:0.096 gb-tuned-l:0.094 gb-tuned-xl:0.094 xgb-xl:0.080 xgb-l:0.080 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.088 knn-tuned-l:0.088 ridge:0.089
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9685, entropy=0.8836, kl_div=0.0000
    Epoch 1: policy_loss=-0.0018, value_loss=0.9685, entropy=0.8825, kl_div=0.0242
  Round 2/3: Mean predicted reward = 9.866
    Using performance-based weights
    Model weights: rf-tuned-l:0.096 rf-tuned-xl:0.096 gb-tuned-l:0.094 gb-tuned-xl:0.094 xgb-xl:0.080 xgb-l:0.080 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.088 knn-tuned-l:0.088 ridge:0.089
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9712, entropy=0.8870, kl_div=0.0000
    Epoch 1: policy_loss=-0.0038, value_loss=0.9712, entropy=0.8861, kl_div=0.0212
  Round 3/3: Mean predicted reward = 9.963

  === Progress Analysis ===
  Status: NORMAL

--- Round 14 Results ---
  Mean Oracle Reward: 10.142
  Min Oracle Reward: 7.354
  Max Oracle Reward: 13.966
  Std Oracle Reward: 1.423
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -4.299, Max: 0.031, Count: 14
  Total Sequences Evaluated: 498

======================================================================
EXPERIMENT ROUND 15/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 498
  Consistent improvement, increasing LR to 0.000360

--- Round 15 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCTCTCGACGGA
  TCTCAGGTAGCA
  GATAGGCCCGAT
  GTGCCGCCATGA
  ACGTGCATCGGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.303
  Max reward: 12.844
  With intrinsic bonuses: 10.311

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9745, entropy=0.8790, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3916

=== Surrogate Model Training ===
Total samples: 530

Training on 499 samples (removed 31 outliers)
Reward range: [6.13, 13.37], mean: 9.85
  Created 14 candidate models for data size 499
Current R2 threshold: -0.25
  rf-tuned-l: R2 = 0.040 (std: 0.067)
  rf-tuned-xl: R2 = 0.026 (std: 0.087)
  gb-tuned-l: R2 = 0.076 (std: 0.088)
  gb-tuned-xl: R2 = 0.076 (std: 0.088)
  xgb-xl: R2 = -0.165 (std: 0.133)
  xgb-l: R2 = -0.165 (std: 0.133)
  mlp-adaptive-xl: R2 = -0.343 (std: 0.092)
  mlp-l: R2 = -0.203 (std: 0.125)
  svr-rbf-xl: R2 = 0.045 (std: 0.109)
  svr-poly-l: R2 = 0.045 (std: 0.109)
  knn-tuned-sqrt: R2 = -0.088 (std: 0.106)
  knn-tuned-l: R2 = -0.088 (std: 0.106)
  ridge: R2 = -0.064 (std: 0.073)
  gp: R2 = -59.226 (std: 2.480)

Model-based training with 12 models
Best R2: 0.076, Mean R2: -4.288
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.090 rf-tuned-xl:0.088 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.073 xgb-l:0.073 mlp-l:0.070 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.079 knn-tuned-l:0.079 ridge:0.081
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9722, entropy=0.8617, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4221
  Round 1/3: Mean predicted reward = 9.816
    Using performance-based weights
    Model weights: rf-tuned-l:0.090 rf-tuned-xl:0.088 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.073 xgb-l:0.073 mlp-l:0.070 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.079 knn-tuned-l:0.079 ridge:0.081
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.8469, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5632
  Round 2/3: Mean predicted reward = 9.859
    Using performance-based weights
    Model weights: rf-tuned-l:0.090 rf-tuned-xl:0.088 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.073 xgb-l:0.073 mlp-l:0.070 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.079 knn-tuned-l:0.079 ridge:0.081
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.8229, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6746
  Round 3/3: Mean predicted reward = 9.998

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 15 Results ---
  Mean Oracle Reward: 10.356
  Min Oracle Reward: 3.929
  Max Oracle Reward: 12.925
  Std Oracle Reward: 1.499
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: -4.288, Max: 0.076, Count: 14
  New best mean reward!
  Total Sequences Evaluated: 530

======================================================================
EXPERIMENT ROUND 16/100
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
  TTCGGGCTAACA
  AAGTTCAGCTGC
  CCTGCGCAGAGT
  CGACGGGTTCAC
  CATCGACTTGAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.895
  Max reward: 13.052
  With intrinsic bonuses: 9.885

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.7984, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6836

=== Surrogate Model Training ===
Total samples: 562

Training on 530 samples (removed 32 outliers)
Reward range: [6.13, 13.37], mean: 9.86
  Created 13 candidate models for data size 530
Current R2 threshold: -0.24
  rf-tuned-l: R2 = 0.025 (std: 0.053)
  rf-tuned-xl: R2 = 0.026 (std: 0.064)
  gb-tuned-l: R2 = 0.029 (std: 0.082)
  gb-tuned-xl: R2 = 0.027 (std: 0.084)
  xgb-xl: R2 = -0.153 (std: 0.070)
  xgb-l: R2 = -0.153 (std: 0.070)
  mlp-adaptive-xl: R2 = -0.149 (std: 0.115)
  mlp-l: R2 = -0.215 (std: 0.117)
  svr-rbf-xl: R2 = 0.033 (std: 0.098)
  svr-poly-l: R2 = 0.033 (std: 0.098)
  knn-tuned-sqrt: R2 = -0.090 (std: 0.127)
  knn-tuned-l: R2 = -0.090 (std: 0.127)
  ridge: R2 = -0.071 (std: 0.068)

Model-based training with 13 models
Best R2: 0.033, Mean R2: -0.058
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.083 gb-tuned-l:0.084 gb-tuned-xl:0.083 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.070 mlp-l:0.065 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.7885, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7060
  Round 1/3: Mean predicted reward = 9.871
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.083 gb-tuned-l:0.084 gb-tuned-xl:0.083 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.070 mlp-l:0.065 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9676, entropy=0.7618, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6397
  Round 2/3: Mean predicted reward = 9.758
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.083 gb-tuned-l:0.084 gb-tuned-xl:0.083 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.070 mlp-l:0.065 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9675, entropy=0.7589, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4100
  Round 3/3: Mean predicted reward = 9.910

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 16 Results ---
  Mean Oracle Reward: 9.850
  Min Oracle Reward: 5.545
  Max Oracle Reward: 13.086
  Std Oracle Reward: 1.479
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.058, Max: 0.033, Count: 13
  Total Sequences Evaluated: 562

======================================================================
EXPERIMENT ROUND 17/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 562

--- Round 17 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AATGCGATCCGT
  CGAGCGATGATC
  AAATGGCGCTAT
  GTACGTGGACCA
  CAGGTGCGTCAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.150
  Max reward: 11.536
  With intrinsic bonuses: 10.169

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.7465, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2733

=== Surrogate Model Training ===
Total samples: 594

Training on 562 samples (removed 32 outliers)
Reward range: [6.13, 13.37], mean: 9.88
  Created 13 candidate models for data size 562
Current R2 threshold: -0.22999999999999998
  rf-tuned-l: R2 = 0.015 (std: 0.068)
  rf-tuned-xl: R2 = 0.010 (std: 0.078)
  gb-tuned-l: R2 = 0.044 (std: 0.052)
  gb-tuned-xl: R2 = 0.042 (std: 0.054)
  xgb-xl: R2 = -0.133 (std: 0.112)
  xgb-l: R2 = -0.133 (std: 0.112)
  mlp-adaptive-xl: R2 = -0.196 (std: 0.121)
  mlp-l: R2 = -0.183 (std: 0.081)
  svr-rbf-xl: R2 = 0.058 (std: 0.098)
  svr-poly-l: R2 = 0.058 (std: 0.098)
  knn-tuned-sqrt: R2 = -0.076 (std: 0.136)
  knn-tuned-l: R2 = -0.076 (std: 0.136)
  ridge: R2 = -0.067 (std: 0.065)

Model-based training with 13 models
Best R2: 0.058, Mean R2: -0.049
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.066 mlp-l:0.067 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.7362, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1866
  Round 1/3: Mean predicted reward = 9.865
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.066 mlp-l:0.067 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9714, entropy=0.7345, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3217
  Round 2/3: Mean predicted reward = 9.964
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.066 mlp-l:0.067 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.7364, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3058
  Round 3/3: Mean predicted reward = 9.809

  === Progress Analysis ===
  Status: NORMAL

--- Round 17 Results ---
  Mean Oracle Reward: 10.180
  Min Oracle Reward: 7.829
  Max Oracle Reward: 11.804
  Std Oracle Reward: 1.034
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.049, Max: 0.058, Count: 13
  Total Sequences Evaluated: 594

======================================================================
EXPERIMENT ROUND 18/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 594

--- Round 18 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ACAAGGCGCTTG
  GCTTGAGGCCAA
  CCCTGAGTAAGG
  AGGGACCACTTT
  GGCACTCTGAGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.546
  Max reward: 12.328
  With intrinsic bonuses: 9.525

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9707, entropy=0.7036, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2111

=== Surrogate Model Training ===
Total samples: 626

Training on 594 samples (removed 32 outliers)
Reward range: [6.13, 13.37], mean: 9.86
  Created 13 candidate models for data size 594
Current R2 threshold: -0.21999999999999997
  rf-tuned-l: R2 = 0.056 (std: 0.082)
  rf-tuned-xl: R2 = 0.042 (std: 0.077)
  gb-tuned-l: R2 = 0.061 (std: 0.073)
  gb-tuned-xl: R2 = 0.062 (std: 0.073)
  xgb-xl: R2 = -0.143 (std: 0.132)
  xgb-l: R2 = -0.143 (std: 0.132)
  mlp-adaptive-xl: R2 = -0.089 (std: 0.077)
  mlp-l: R2 = -0.154 (std: 0.081)
  svr-rbf-xl: R2 = 0.091 (std: 0.093)
  svr-poly-l: R2 = 0.091 (std: 0.093)
  knn-tuned-sqrt: R2 = -0.079 (std: 0.125)
  knn-tuned-l: R2 = -0.079 (std: 0.125)
  ridge: R2 = -0.052 (std: 0.062)

Model-based training with 13 models
Best R2: 0.091, Mean R2: -0.026
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.082 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.072 mlp-l:0.067 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.7077, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2175
  Round 1/3: Mean predicted reward = 9.825
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.082 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.072 mlp-l:0.067 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9713, entropy=0.7047, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2351
  Round 2/3: Mean predicted reward = 9.816
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.082 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.072 mlp-l:0.067 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9702, entropy=0.7080, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1622
  Round 3/3: Mean predicted reward = 9.943

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 18 Results ---
  Mean Oracle Reward: 9.536
  Min Oracle Reward: 6.212
  Max Oracle Reward: 12.311
  Std Oracle Reward: 1.459
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.026, Max: 0.091, Count: 13
  Total Sequences Evaluated: 626

======================================================================
EXPERIMENT ROUND 19/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 626

--- Round 19 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TTAGCCGCAGGC
  CGGCTGTAGACC
  GTCCATGGTACA
  ACGGGATACCTG
  TGCCGAATCGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.155
  Max reward: 12.860
  With intrinsic bonuses: 10.092

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9726, entropy=0.7000, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1033

=== Surrogate Model Training ===
Total samples: 658

Training on 625 samples (removed 33 outliers)
Reward range: [6.13, 13.37], mean: 9.88
  Created 13 candidate models for data size 625
Current R2 threshold: -0.21
  rf-tuned-l: R2 = 0.060 (std: 0.098)
  rf-tuned-xl: R2 = 0.080 (std: 0.092)
  gb-tuned-l: R2 = 0.073 (std: 0.081)
  gb-tuned-xl: R2 = 0.071 (std: 0.082)
  xgb-xl: R2 = -0.062 (std: 0.183)
  xgb-l: R2 = -0.062 (std: 0.183)
  mlp-adaptive-xl: R2 = -0.119 (std: 0.109)
  mlp-l: R2 = -0.160 (std: 0.106)
  svr-rbf-xl: R2 = 0.104 (std: 0.090)
  svr-poly-l: R2 = 0.104 (std: 0.090)
  knn-tuned-sqrt: R2 = -0.070 (std: 0.127)
  knn-tuned-l: R2 = -0.070 (std: 0.127)
  ridge: R2 = -0.059 (std: 0.076)

Model-based training with 13 models
Best R2: 0.104, Mean R2: -0.009
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.084 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.069 mlp-l:0.066 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.7128, kl_div=0.0000
    Epoch 1: policy_loss=0.0052, value_loss=0.9697, entropy=0.7122, kl_div=0.0470
  Round 1/3: Mean predicted reward = 9.808
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.084 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.069 mlp-l:0.066 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.7119, kl_div=0.0000
    Epoch 1: policy_loss=-0.0098, value_loss=0.9680, entropy=0.7127, kl_div=-0.0086
  Round 2/3: Mean predicted reward = 9.800
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.084 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.069 mlp-l:0.066 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.7080, kl_div=0.0000
    Epoch 1: policy_loss=-0.0182, value_loss=0.9693, entropy=0.7098, kl_div=-0.0480
  Round 3/3: Mean predicted reward = 9.775

  === Progress Analysis ===
  Status: NORMAL

--- Round 19 Results ---
  Mean Oracle Reward: 10.145
  Min Oracle Reward: 5.495
  Max Oracle Reward: 13.033
  Std Oracle Reward: 1.523
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.009, Max: 0.104, Count: 13
  Total Sequences Evaluated: 658

======================================================================
EXPERIMENT ROUND 20/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 658

--- Round 20 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGAAGCGCTCTA
  CGCATTCGGGAA
  ATAGCTCCGGAG
  GTACGTCAGCGC
  AGCTGGCACCTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.325
  Max reward: 12.574
  With intrinsic bonuses: 10.382

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.7226, kl_div=0.0000
    Epoch 1: policy_loss=0.1534, value_loss=0.9699, entropy=0.7392, kl_div=-0.4678

=== Surrogate Model Training ===
Total samples: 690

Training on 656 samples (removed 34 outliers)
Reward range: [6.29, 13.37], mean: 9.91
  Created 13 candidate models for data size 656
Current R2 threshold: -0.19999999999999998
  rf-tuned-l: R2 = 0.069 (std: 0.087)
  rf-tuned-xl: R2 = 0.090 (std: 0.072)
  gb-tuned-l: R2 = 0.085 (std: 0.065)
  gb-tuned-xl: R2 = 0.085 (std: 0.065)
  xgb-xl: R2 = -0.038 (std: 0.143)
  xgb-l: R2 = -0.038 (std: 0.143)
  mlp-adaptive-xl: R2 = -0.131 (std: 0.116)
  mlp-l: R2 = -0.054 (std: 0.071)
  svr-rbf-xl: R2 = 0.109 (std: 0.087)
  svr-poly-l: R2 = 0.109 (std: 0.087)
  knn-tuned-sqrt: R2 = -0.075 (std: 0.151)
  knn-tuned-l: R2 = -0.075 (std: 0.151)
  ridge: R2 = -0.052 (std: 0.064)

Model-based training with 13 models
Best R2: 0.109, Mean R2: 0.007
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.083 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.067 mlp-l:0.072 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.072
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.7259, kl_div=0.0000
    Epoch 1: policy_loss=-0.0261, value_loss=0.9700, entropy=0.7306, kl_div=-0.1505
  Round 1/3: Mean predicted reward = 9.965
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.083 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.067 mlp-l:0.072 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.072
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.7439, kl_div=0.0000
    Epoch 1: policy_loss=-0.0184, value_loss=0.9693, entropy=0.7457, kl_div=-0.1634
  Round 2/3: Mean predicted reward = 9.964
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.083 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.067 mlp-l:0.072 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.072
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9724, entropy=0.7438, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2917
  Round 3/3: Mean predicted reward = 9.930

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 20 Results ---
  Mean Oracle Reward: 10.345
  Min Oracle Reward: 7.488
  Max Oracle Reward: 12.326
  Std Oracle Reward: 1.141
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.007, Max: 0.109, Count: 13
  Total Sequences Evaluated: 690

======================================================================
EXPERIMENT ROUND 21/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 690
  Consistent improvement, increasing LR to 0.000327

--- Round 21 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCGTAGAGCTCA
  ATGCAACCTGGT
  GACGCTGGTACA
  CCTGACAGTGGA
  GAGGACGTCCTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.192
  Max reward: 13.186
  With intrinsic bonuses: 10.186

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.7356, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3622

=== Surrogate Model Training ===
Total samples: 722

Training on 686 samples (removed 36 outliers)
Reward range: [6.29, 13.37], mean: 9.92
  Created 13 candidate models for data size 686
Current R2 threshold: -0.19
  rf-tuned-l: R2 = 0.081 (std: 0.073)
  rf-tuned-xl: R2 = 0.077 (std: 0.060)
  gb-tuned-l: R2 = 0.083 (std: 0.055)
  gb-tuned-xl: R2 = 0.082 (std: 0.055)
  xgb-xl: R2 = -0.076 (std: 0.091)
  xgb-l: R2 = -0.076 (std: 0.091)
  mlp-adaptive-xl: R2 = -0.037 (std: 0.104)
  mlp-l: R2 = -0.027 (std: 0.080)
  svr-rbf-xl: R2 = 0.133 (std: 0.060)
  svr-poly-l: R2 = 0.133 (std: 0.060)
  knn-tuned-sqrt: R2 = -0.034 (std: 0.092)
  knn-tuned-l: R2 = -0.034 (std: 0.092)
  ridge: R2 = -0.047 (std: 0.042)

Model-based training with 13 models
Best R2: 0.133, Mean R2: 0.020
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.072 mlp-l:0.073 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.072
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.7035, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3633
  Round 1/3: Mean predicted reward = 9.863
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.072 mlp-l:0.073 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.072
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9681, entropy=0.7124, kl_div=0.0000
    Epoch 1: policy_loss=0.0035, value_loss=0.9681, entropy=0.7116, kl_div=0.0495
  Round 2/3: Mean predicted reward = 9.946
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.072 mlp-l:0.073 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.072
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.7230, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0701
  Round 3/3: Mean predicted reward = 9.943

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 21 Results ---
  Mean Oracle Reward: 10.211
  Min Oracle Reward: 5.905
  Max Oracle Reward: 13.189
  Std Oracle Reward: 1.318
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.020, Max: 0.133, Count: 13
  Total Sequences Evaluated: 722

======================================================================
EXPERIMENT ROUND 22/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 722
  Performance plateaued, reducing LR to 0.000100

--- Round 22 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTACCCGGTACG
  CCTGGCCAGTGA
  CGGAGCCAGCTT
  ACACCGTGCTGG
  TCTGGCCAGAGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.532
  Max reward: 12.351
  With intrinsic bonuses: 10.563

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.7244, kl_div=0.0000
    Epoch 1: policy_loss=-0.0325, value_loss=0.9688, entropy=0.7256, kl_div=0.0048

=== Surrogate Model Training ===
Total samples: 754

Training on 715 samples (removed 39 outliers)
Reward range: [6.56, 13.23], mean: 9.95
  Created 13 candidate models for data size 715
Current R2 threshold: -0.18
  rf-tuned-l: R2 = 0.041 (std: 0.098)
  rf-tuned-xl: R2 = 0.041 (std: 0.101)
  gb-tuned-l: R2 = 0.046 (std: 0.090)
  gb-tuned-xl: R2 = 0.046 (std: 0.090)
  xgb-xl: R2 = -0.130 (std: 0.099)
  xgb-l: R2 = -0.130 (std: 0.099)
  mlp-adaptive-xl: R2 = -0.091 (std: 0.120)
  mlp-l: R2 = -0.081 (std: 0.168)
  svr-rbf-xl: R2 = 0.102 (std: 0.085)
  svr-poly-l: R2 = 0.102 (std: 0.085)
  knn-tuned-sqrt: R2 = -0.068 (std: 0.157)
  knn-tuned-l: R2 = -0.068 (std: 0.157)
  ridge: R2 = -0.078 (std: 0.077)

Model-based training with 13 models
Best R2: 0.102, Mean R2: -0.021
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.082 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.071 mlp-l:0.072 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.072
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.7195, kl_div=0.0000
    Epoch 1: policy_loss=-0.0441, value_loss=0.9698, entropy=0.7238, kl_div=-0.0850
  Round 1/3: Mean predicted reward = 9.920
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.082 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.071 mlp-l:0.072 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.072
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.7221, kl_div=0.0000
    Epoch 1: policy_loss=-0.0251, value_loss=0.9701, entropy=0.7235, kl_div=-0.0087
  Round 2/3: Mean predicted reward = 9.937
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.082 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.071 mlp-l:0.072 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.072
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.7279, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0547
  Round 3/3: Mean predicted reward = 10.022

  === Progress Analysis ===
  Status: NORMAL

--- Round 22 Results ---
  Mean Oracle Reward: 10.480
  Min Oracle Reward: 8.571
  Max Oracle Reward: 12.300
  Std Oracle Reward: 0.902
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.021, Max: 0.102, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 754

======================================================================
EXPERIMENT ROUND 23/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 754

--- Round 23 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCGCTAGCGTCA
  GGCCTGATGAAC
  CTAGGTCAACGG
  TGCGCACAGCGT
  ACGTTGGACGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.218
  Max reward: 12.950
  With intrinsic bonuses: 10.174

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9715, entropy=0.7226, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1024

=== Surrogate Model Training ===
Total samples: 786

Training on 748 samples (removed 38 outliers)
Reward range: [6.56, 13.37], mean: 9.97
  Created 13 candidate models for data size 748
Current R2 threshold: -0.16999999999999998
  rf-tuned-l: R2 = 0.072 (std: 0.061)
  rf-tuned-xl: R2 = 0.064 (std: 0.047)
  gb-tuned-l: R2 = 0.076 (std: 0.063)
  gb-tuned-xl: R2 = 0.076 (std: 0.063)
  xgb-xl: R2 = -0.083 (std: 0.074)
  xgb-l: R2 = -0.083 (std: 0.074)
  mlp-adaptive-xl: R2 = -0.066 (std: 0.149)
  mlp-l: R2 = -0.094 (std: 0.094)
  svr-rbf-xl: R2 = 0.134 (std: 0.072)
  svr-poly-l: R2 = 0.134 (std: 0.072)
  knn-tuned-sqrt: R2 = -0.041 (std: 0.143)
  knn-tuned-l: R2 = -0.041 (std: 0.143)
  ridge: R2 = -0.073 (std: 0.069)

Model-based training with 13 models
Best R2: 0.134, Mean R2: 0.006
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.071 mlp-l:0.069 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.071
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.7295, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1435
  Round 1/3: Mean predicted reward = 9.918
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.071 mlp-l:0.069 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.071
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.7136, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1563
  Round 2/3: Mean predicted reward = 9.998
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.071 mlp-l:0.069 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.071
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=0.7123, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0954
  Round 3/3: Mean predicted reward = 10.052

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 23 Results ---
  Mean Oracle Reward: 10.243
  Min Oracle Reward: 7.834
  Max Oracle Reward: 13.186
  Std Oracle Reward: 1.345
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.006, Max: 0.134, Count: 13
  Total Sequences Evaluated: 786

======================================================================
EXPERIMENT ROUND 24/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 786

--- Round 24 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGCCGTAACGTG
  ACTGCGCGGTCA
  CACTGTAAGCGT
  ACTCCGGGTGCA
  GCCGAGGTCCAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.752
  Max reward: 13.192
  With intrinsic bonuses: 9.795

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.7135, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0640

=== Surrogate Model Training ===
Total samples: 818

Training on 778 samples (removed 40 outliers)
Reward range: [6.56, 13.37], mean: 9.98
  Created 13 candidate models for data size 778
Current R2 threshold: -0.15999999999999998
  rf-tuned-l: R2 = 0.104 (std: 0.054)
  rf-tuned-xl: R2 = 0.096 (std: 0.079)
  gb-tuned-l: R2 = 0.102 (std: 0.067)
  gb-tuned-xl: R2 = 0.102 (std: 0.067)
  xgb-xl: R2 = -0.013 (std: 0.055)
  xgb-l: R2 = -0.013 (std: 0.055)
  mlp-adaptive-xl: R2 = -0.006 (std: 0.128)
  mlp-l: R2 = -0.015 (std: 0.092)
  svr-rbf-xl: R2 = 0.161 (std: 0.079)
  svr-poly-l: R2 = 0.161 (std: 0.079)
  knn-tuned-sqrt: R2 = -0.032 (std: 0.127)
  knn-tuned-l: R2 = -0.032 (std: 0.127)
  ridge: R2 = -0.062 (std: 0.063)

Model-based training with 13 models
Best R2: 0.161, Mean R2: 0.043
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.073 mlp-l:0.072 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=0.7249, kl_div=0.0000
    Epoch 1: policy_loss=-0.0022, value_loss=0.9678, entropy=0.7247, kl_div=0.0273
  Round 1/3: Mean predicted reward = 9.877
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.073 mlp-l:0.072 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=0.6888, kl_div=0.0000
    Epoch 1: policy_loss=-0.0209, value_loss=0.9709, entropy=0.6887, kl_div=0.0180
  Round 2/3: Mean predicted reward = 10.114
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.073 mlp-l:0.072 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9704, entropy=0.7325, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0691
  Round 3/3: Mean predicted reward = 9.995

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 24 Results ---
  Mean Oracle Reward: 9.823
  Min Oracle Reward: 2.985
  Max Oracle Reward: 13.003
  Std Oracle Reward: 1.841
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.043, Max: 0.161, Count: 13
  Total Sequences Evaluated: 818

======================================================================
EXPERIMENT ROUND 25/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 818

--- Round 25 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCTGTAGCAGGA
  GGTCATAACCGG
  CGGGCCTTAGAA
  GCACAGGCTGTC
  ACGCGTCTAGAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.945
  Max reward: 13.016
  With intrinsic bonuses: 9.914

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9720, entropy=0.6930, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6573

=== Surrogate Model Training ===
Total samples: 850

Training on 807 samples (removed 43 outliers)
Reward range: [6.56, 13.30], mean: 9.98
  Created 13 candidate models for data size 807
Current R2 threshold: -0.15
  rf-tuned-l: R2 = 0.087 (std: 0.070)
  rf-tuned-xl: R2 = 0.080 (std: 0.064)
  gb-tuned-l: R2 = 0.091 (std: 0.073)
  gb-tuned-xl: R2 = 0.091 (std: 0.073)
  xgb-xl: R2 = -0.037 (std: 0.085)
  xgb-l: R2 = -0.037 (std: 0.085)
  mlp-adaptive-xl: R2 = -0.046 (std: 0.093)
  mlp-l: R2 = -0.058 (std: 0.096)
  svr-rbf-xl: R2 = 0.160 (std: 0.086)
  svr-poly-l: R2 = 0.160 (std: 0.086)
  knn-tuned-sqrt: R2 = -0.043 (std: 0.129)
  knn-tuned-l: R2 = -0.043 (std: 0.129)
  ridge: R2 = -0.065 (std: 0.067)

Model-based training with 13 models
Best R2: 0.160, Mean R2: 0.026
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.071 mlp-l:0.070 svr-rbf-xl:0.088 svr-poly-l:0.088 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.7005, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5287
  Round 1/3: Mean predicted reward = 9.912
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.071 mlp-l:0.070 svr-rbf-xl:0.088 svr-poly-l:0.088 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.7048, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7371
  Round 2/3: Mean predicted reward = 10.124
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.071 mlp-l:0.070 svr-rbf-xl:0.088 svr-poly-l:0.088 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.6703, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0166
  Round 3/3: Mean predicted reward = 10.047

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 25 Results ---
  Mean Oracle Reward: 9.930
  Min Oracle Reward: 5.003
  Max Oracle Reward: 13.114
  Std Oracle Reward: 1.543
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.026, Max: 0.160, Count: 13
  Total Sequences Evaluated: 850

======================================================================
EXPERIMENT ROUND 26/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 850

--- Round 26 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GACCGTTGCGCA
  AGTTCGATCAGC
  TAACTCAGGGCG
  CCGTAAGGGCTA
  GAAGGGTTCCAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.777
  Max reward: 12.020
  With intrinsic bonuses: 9.790

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9714, entropy=0.6569, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.2243

=== Surrogate Model Training ===
Total samples: 882

Training on 838 samples (removed 44 outliers)
Reward range: [6.56, 13.37], mean: 9.99
  Created 13 candidate models for data size 838
Current R2 threshold: -0.13999999999999999
  rf-tuned-l: R2 = 0.089 (std: 0.044)
  rf-tuned-xl: R2 = 0.096 (std: 0.062)
  gb-tuned-l: R2 = 0.114 (std: 0.052)
  gb-tuned-xl: R2 = 0.114 (std: 0.052)
  xgb-xl: R2 = -0.011 (std: 0.062)
  xgb-l: R2 = -0.011 (std: 0.062)
  mlp-adaptive-xl: R2 = 0.013 (std: 0.095)
  mlp-l: R2 = 0.059 (std: 0.069)
  svr-rbf-xl: R2 = 0.168 (std: 0.063)
  svr-poly-l: R2 = 0.168 (std: 0.063)
  knn-tuned-sqrt: R2 = -0.024 (std: 0.073)
  knn-tuned-l: R2 = -0.024 (std: 0.073)
  ridge: R2 = -0.053 (std: 0.040)

Model-based training with 13 models
Best R2: 0.168, Mean R2: 0.054
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.074 mlp-l:0.077 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9703, entropy=0.6334, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1941
  Round 1/3: Mean predicted reward = 9.991
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.074 mlp-l:0.077 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.6180, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0413
  Round 2/3: Mean predicted reward = 9.930
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.074 mlp-l:0.077 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.6119, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0486
  Round 3/3: Mean predicted reward = 10.057

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 26 Results ---
  Mean Oracle Reward: 9.759
  Min Oracle Reward: 4.084
  Max Oracle Reward: 12.206
  Std Oracle Reward: 1.680
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.054, Max: 0.168, Count: 13
  Total Sequences Evaluated: 882

======================================================================
EXPERIMENT ROUND 27/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 882
  Performance plateaued, reducing LR to 0.000100

--- Round 27 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ATCCTAGGGTAC
  AATCCGGAGTTC
  GCCGATATGCGA
  ATCTGACGGACG
  TTACACGCCGGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.055
  Max reward: 12.809
  With intrinsic bonuses: 10.115

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.5860, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5493

=== Surrogate Model Training ===
Total samples: 914

Training on 869 samples (removed 45 outliers)
Reward range: [6.56, 13.30], mean: 9.99
  Created 13 candidate models for data size 869
Current R2 threshold: -0.12999999999999998
  rf-tuned-l: R2 = 0.117 (std: 0.079)
  rf-tuned-xl: R2 = 0.115 (std: 0.071)
  gb-tuned-l: R2 = 0.107 (std: 0.067)
  gb-tuned-xl: R2 = 0.107 (std: 0.067)
  xgb-xl: R2 = -0.010 (std: 0.104)
  xgb-l: R2 = -0.010 (std: 0.104)
  mlp-adaptive-xl: R2 = 0.023 (std: 0.087)
  mlp-l: R2 = -0.005 (std: 0.058)
  svr-rbf-xl: R2 = 0.177 (std: 0.081)
  svr-poly-l: R2 = 0.177 (std: 0.081)
  knn-tuned-sqrt: R2 = -0.014 (std: 0.102)
  knn-tuned-l: R2 = -0.014 (std: 0.102)
  ridge: R2 = -0.048 (std: 0.050)

Model-based training with 13 models
Best R2: 0.177, Mean R2: 0.056
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.074 mlp-l:0.072 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.5802, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4835
  Round 1/3: Mean predicted reward = 9.917
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.074 mlp-l:0.072 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.5826, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4467
  Round 2/3: Mean predicted reward = 9.951
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.074 mlp-l:0.072 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.6061, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4290
  Round 3/3: Mean predicted reward = 10.002

  === Progress Analysis ===
  Status: NORMAL

--- Round 27 Results ---
  Mean Oracle Reward: 10.033
  Min Oracle Reward: 6.244
  Max Oracle Reward: 12.750
  Std Oracle Reward: 1.208
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.056, Max: 0.177, Count: 13
  Total Sequences Evaluated: 914

======================================================================
EXPERIMENT ROUND 28/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 914

--- Round 28 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGTGACATGGCC
  AGTGTCCCAAGG
  TACGCGAACTGG
  GGACTCGATACG
  GCCGTACGTCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.144
  Max reward: 12.079
  With intrinsic bonuses: 10.149

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9720, entropy=0.5991, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5927

=== Surrogate Model Training ===
Total samples: 946

Training on 900 samples (removed 46 outliers)
Reward range: [6.56, 13.30], mean: 10.00
  Created 13 candidate models for data size 900
Current R2 threshold: -0.12
  rf-tuned-l: R2 = 0.135 (std: 0.075)
  rf-tuned-xl: R2 = 0.124 (std: 0.078)
  gb-tuned-l: R2 = 0.118 (std: 0.081)
  gb-tuned-xl: R2 = 0.118 (std: 0.081)
  xgb-xl: R2 = 0.000 (std: 0.054)
  xgb-l: R2 = 0.000 (std: 0.054)
  mlp-adaptive-xl: R2 = 0.039 (std: 0.113)
  mlp-l: R2 = 0.007 (std: 0.076)
  svr-rbf-xl: R2 = 0.197 (std: 0.080)
  svr-poly-l: R2 = 0.197 (std: 0.080)
  knn-tuned-sqrt: R2 = -0.012 (std: 0.083)
  knn-tuned-l: R2 = -0.012 (std: 0.083)
  ridge: R2 = -0.049 (std: 0.051)

Model-based training with 13 models
Best R2: 0.197, Mean R2: 0.066
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.075 mlp-l:0.072 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.5897, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6380
  Round 1/3: Mean predicted reward = 10.012
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.075 mlp-l:0.072 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9700, entropy=0.5867, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6609
  Round 2/3: Mean predicted reward = 9.962
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.075 mlp-l:0.072 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.5926, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7343
  Round 3/3: Mean predicted reward = 9.954

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 28 Results ---
  Mean Oracle Reward: 10.168
  Min Oracle Reward: 6.214
  Max Oracle Reward: 12.001
  Std Oracle Reward: 1.325
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.066, Max: 0.197, Count: 13
  Total Sequences Evaluated: 946

======================================================================
EXPERIMENT ROUND 29/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 946
  Consistent improvement, increasing LR to 0.000045

--- Round 29 Configuration ---
Learning rate: 0.000045
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCTCCGGACGGA
  TAGCGTGCCAAG
  CAAGGTGACCGT
  CACTGATCGGCG
  GGTCCCAATGGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.210
  Max reward: 12.731
  With intrinsic bonuses: 10.224

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.5686, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3271

=== Surrogate Model Training ===
Total samples: 978

Training on 930 samples (removed 48 outliers)
Reward range: [6.56, 13.30], mean: 10.01
  Created 13 candidate models for data size 930
Current R2 threshold: -0.10999999999999999
  rf-tuned-l: R2 = 0.128 (std: 0.066)
  rf-tuned-xl: R2 = 0.122 (std: 0.080)
  gb-tuned-l: R2 = 0.133 (std: 0.090)
  gb-tuned-xl: R2 = 0.133 (std: 0.090)
  xgb-xl: R2 = -0.013 (std: 0.061)
  xgb-l: R2 = -0.013 (std: 0.061)
  mlp-adaptive-xl: R2 = 0.022 (std: 0.057)
  mlp-l: R2 = 0.020 (std: 0.038)
  svr-rbf-xl: R2 = 0.197 (std: 0.081)
  svr-poly-l: R2 = 0.197 (std: 0.081)
  knn-tuned-sqrt: R2 = -0.017 (std: 0.073)
  knn-tuned-l: R2 = -0.017 (std: 0.073)
  ridge: R2 = -0.052 (std: 0.058)

Model-based training with 13 models
Best R2: 0.197, Mean R2: 0.064
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.071 xgb-l:0.071 mlp-adaptive-xl:0.073 mlp-l:0.073 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.5896, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2221
  Round 1/3: Mean predicted reward = 9.939
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.071 xgb-l:0.071 mlp-adaptive-xl:0.073 mlp-l:0.073 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.5625, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2364
  Round 2/3: Mean predicted reward = 10.060
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.071 xgb-l:0.071 mlp-adaptive-xl:0.073 mlp-l:0.073 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9730, entropy=0.5607, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3013
  Round 3/3: Mean predicted reward = 10.074

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 29 Results ---
  Mean Oracle Reward: 10.267
  Min Oracle Reward: 5.950
  Max Oracle Reward: 12.704
  Std Oracle Reward: 1.414
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.064, Max: 0.197, Count: 13
  Total Sequences Evaluated: 978

======================================================================
EXPERIMENT ROUND 30/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 978
  Performance plateaued, reducing LR to 0.000150

--- Round 30 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ACCTTCAGGCGG
  CCGATTCGCGAG
  ACAGGTCCGCGT
  TCGGCACTGACG
  GGCTATGCACAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.993
  Max reward: 12.088
  With intrinsic bonuses: 10.024

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9713, entropy=0.5768, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0854

=== Surrogate Model Training ===
Total samples: 1010

Training on 959 samples (removed 51 outliers)
Reward range: [6.59, 13.37], mean: 10.03
  Created 13 candidate models for data size 959
Current R2 threshold: -0.09999999999999998
  rf-tuned-l: R2 = 0.114 (std: 0.060)
  rf-tuned-xl: R2 = 0.116 (std: 0.053)
  gb-tuned-l: R2 = 0.161 (std: 0.075)
  gb-tuned-xl: R2 = 0.161 (std: 0.075)
  xgb-xl: R2 = 0.008 (std: 0.065)
  xgb-l: R2 = 0.008 (std: 0.065)
  mlp-adaptive-xl: R2 = 0.036 (std: 0.057)
  mlp-l: R2 = 0.069 (std: 0.081)
  svr-rbf-xl: R2 = 0.194 (std: 0.057)
  svr-poly-l: R2 = 0.194 (std: 0.057)
  knn-tuned-sqrt: R2 = -0.016 (std: 0.067)
  knn-tuned-l: R2 = -0.016 (std: 0.067)
  ridge: R2 = -0.040 (std: 0.048)

Model-based training with 13 models
Best R2: 0.194, Mean R2: 0.076
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.074 mlp-l:0.076 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.5641, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7978
  Round 1/3: Mean predicted reward = 10.003
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.074 mlp-l:0.076 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.5749, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9004
  Round 2/3: Mean predicted reward = 9.966
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.074 mlp-l:0.076 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.5493, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8474
  Round 3/3: Mean predicted reward = 9.957

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 30 Results ---
  Mean Oracle Reward: 9.972
  Min Oracle Reward: 4.846
  Max Oracle Reward: 11.998
  Std Oracle Reward: 1.713
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.076, Max: 0.194, Count: 13
  Total Sequences Evaluated: 1010

======================================================================
EXPERIMENT ROUND 31/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1010
  Performance plateaued, reducing LR to 0.000136

--- Round 31 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CAAGCGTTCGGC
  GACCGTTCGCAG
  CTCAGGCGAGCT
  TAGGCCGCTCAG
  CCAGGGCGAATT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.674
  Max reward: 12.940
  With intrinsic bonuses: 10.708

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.5753, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7255

=== Surrogate Model Training ===
Total samples: 1042

Training on 990 samples (removed 52 outliers)
Reward range: [6.72, 13.37], mean: 10.06
  Created 13 candidate models for data size 990
Current R2 threshold: -0.09
  rf-tuned-l: R2 = 0.097 (std: 0.037)
  rf-tuned-xl: R2 = 0.094 (std: 0.043)
  gb-tuned-l: R2 = 0.154 (std: 0.065)
  gb-tuned-xl: R2 = 0.154 (std: 0.065)
  xgb-xl: R2 = -0.027 (std: 0.061)
  xgb-l: R2 = -0.027 (std: 0.061)
  mlp-adaptive-xl: R2 = 0.031 (std: 0.086)
  mlp-l: R2 = 0.032 (std: 0.115)
  svr-rbf-xl: R2 = 0.184 (std: 0.064)
  svr-poly-l: R2 = 0.184 (std: 0.064)
  knn-tuned-sqrt: R2 = -0.021 (std: 0.064)
  knn-tuned-l: R2 = -0.021 (std: 0.064)
  ridge: R2 = -0.049 (std: 0.041)

Model-based training with 13 models
Best R2: 0.184, Mean R2: 0.061
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.079 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.074 mlp-l:0.075 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.5653, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5230
  Round 1/3: Mean predicted reward = 9.957
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.079 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.074 mlp-l:0.075 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.5631, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3560
  Round 2/3: Mean predicted reward = 10.067
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.079 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.074 mlp-l:0.075 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=0.5538, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4798
  Round 3/3: Mean predicted reward = 10.108

  === Progress Analysis ===
  Status: NORMAL

--- Round 31 Results ---
  Mean Oracle Reward: 10.688
  Min Oracle Reward: 6.618
  Max Oracle Reward: 12.721
  Std Oracle Reward: 1.263
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.061, Max: 0.184, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 1042

======================================================================
EXPERIMENT ROUND 32/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1042

--- Round 32 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCTGCAACTCGG
  GCCAGGTTCGAC
  GCGCACGACTTG
  TAACGGCGCTAG
  TCAGAGCCGCGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.275
  Max reward: 12.749
  With intrinsic bonuses: 10.325

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9699, entropy=0.5534, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7719

=== Surrogate Model Training ===
Total samples: 1074

Training on 1021 samples (removed 53 outliers)
Reward range: [6.72, 13.30], mean: 10.06
  Created 13 candidate models for data size 1021
Current R2 threshold: -0.07999999999999999
  rf-tuned-l: R2 = 0.092 (std: 0.046)
  rf-tuned-xl: R2 = 0.103 (std: 0.053)
  gb-tuned-l: R2 = 0.165 (std: 0.054)
  gb-tuned-xl: R2 = 0.165 (std: 0.054)
  xgb-xl: R2 = -0.057 (std: 0.076)
  xgb-l: R2 = -0.057 (std: 0.076)
  mlp-adaptive-xl: R2 = 0.075 (std: 0.050)
  mlp-l: R2 = 0.052 (std: 0.067)
  svr-rbf-xl: R2 = 0.187 (std: 0.051)
  svr-poly-l: R2 = 0.187 (std: 0.051)
  knn-tuned-sqrt: R2 = -0.007 (std: 0.074)
  knn-tuned-l: R2 = -0.007 (std: 0.074)
  ridge: R2 = -0.043 (std: 0.062)

Model-based training with 13 models
Best R2: 0.187, Mean R2: 0.066
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.077 mlp-l:0.076 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.5365, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7270
  Round 1/3: Mean predicted reward = 9.991
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.077 mlp-l:0.076 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9702, entropy=0.5525, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9707
  Round 2/3: Mean predicted reward = 9.933
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.077 mlp-l:0.076 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.5208, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0278
  Round 3/3: Mean predicted reward = 10.162

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 32 Results ---
  Mean Oracle Reward: 10.274
  Min Oracle Reward: 7.411
  Max Oracle Reward: 12.816
  Std Oracle Reward: 1.186
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.066, Max: 0.187, Count: 13
  Total Sequences Evaluated: 1074

======================================================================
EXPERIMENT ROUND 33/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1074

--- Round 33 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTAGTGGCCGCA
  GGATCGCGACCT
  ACTGCCGCTAGG
  CCTCCTAGGAGG
  CCGAGATCTCGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.146
  Max reward: 12.496
  With intrinsic bonuses: 10.088

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9716, entropy=0.5016, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7246

=== Surrogate Model Training ===
Total samples: 1106

Training on 1053 samples (removed 53 outliers)
Reward range: [6.72, 13.30], mean: 10.06
  Created 13 candidate models for data size 1053
Current R2 threshold: -0.06999999999999998
  rf-tuned-l: R2 = 0.099 (std: 0.031)
  rf-tuned-xl: R2 = 0.100 (std: 0.054)
  gb-tuned-l: R2 = 0.168 (std: 0.048)
  gb-tuned-xl: R2 = 0.168 (std: 0.048)
  xgb-xl: R2 = -0.032 (std: 0.043)
  xgb-l: R2 = -0.032 (std: 0.043)
  mlp-adaptive-xl: R2 = 0.054 (std: 0.077)
  mlp-l: R2 = 0.077 (std: 0.093)
  svr-rbf-xl: R2 = 0.193 (std: 0.047)
  svr-poly-l: R2 = 0.193 (std: 0.047)
  knn-tuned-sqrt: R2 = 0.030 (std: 0.073)
  knn-tuned-l: R2 = 0.030 (std: 0.073)
  ridge: R2 = -0.034 (std: 0.058)

Model-based training with 13 models
Best R2: 0.193, Mean R2: 0.078
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.078 rf-tuned-xl:0.078 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.075 mlp-l:0.077 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.5135, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4663
  Round 1/3: Mean predicted reward = 9.801
    Using performance-based weights
    Model weights: rf-tuned-l:0.078 rf-tuned-xl:0.078 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.075 mlp-l:0.077 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.5121, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3460
  Round 2/3: Mean predicted reward = 9.987
    Using performance-based weights
    Model weights: rf-tuned-l:0.078 rf-tuned-xl:0.078 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.075 mlp-l:0.077 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.4994, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4201
  Round 3/3: Mean predicted reward = 10.127

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 33 Results ---
  Mean Oracle Reward: 10.144
  Min Oracle Reward: 7.356
  Max Oracle Reward: 12.810
  Std Oracle Reward: 1.309
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.078, Max: 0.193, Count: 13
  Total Sequences Evaluated: 1106

======================================================================
EXPERIMENT ROUND 34/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1106

--- Round 34 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGATCCGCATGG
  GGTCGTACCAAG
  TGGCCGTACCAG
  CTATCCAGGGGC
  GATACCTAGGGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.696
  Max reward: 12.112
  With intrinsic bonuses: 9.657

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9715, entropy=0.4777, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1525

=== Surrogate Model Training ===
Total samples: 1138

Training on 1082 samples (removed 56 outliers)
Reward range: [6.79, 13.30], mean: 10.07
  Created 13 candidate models for data size 1082
Current R2 threshold: -0.06
  rf-tuned-l: R2 = 0.125 (std: 0.058)
  rf-tuned-xl: R2 = 0.112 (std: 0.058)
  gb-tuned-l: R2 = 0.158 (std: 0.060)
  gb-tuned-xl: R2 = 0.158 (std: 0.060)
  xgb-xl: R2 = -0.016 (std: 0.049)
  xgb-l: R2 = -0.016 (std: 0.049)
  mlp-adaptive-xl: R2 = 0.096 (std: 0.076)
  mlp-l: R2 = 0.037 (std: 0.058)
  svr-rbf-xl: R2 = 0.193 (std: 0.045)
  svr-poly-l: R2 = 0.193 (std: 0.045)
  knn-tuned-sqrt: R2 = 0.036 (std: 0.074)
  knn-tuned-l: R2 = 0.036 (std: 0.074)
  ridge: R2 = -0.031 (std: 0.059)

Model-based training with 13 models
Best R2: 0.193, Mean R2: 0.083
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.022 gb-tuned-xl:0.000 xgb-xl:0.126 xgb-l:0.447 mlp-adaptive-xl:0.080 mlp-l:0.225 svr-rbf-xl:0.100 svr-poly-l:0.000 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.4801, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1421
  Round 1/3: Mean predicted reward = 9.953
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.022 gb-tuned-xl:0.000 xgb-xl:0.126 xgb-l:0.447 mlp-adaptive-xl:0.080 mlp-l:0.225 svr-rbf-xl:0.100 svr-poly-l:0.000 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9719, entropy=0.4845, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1330
  Round 2/3: Mean predicted reward = 9.942
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.022 gb-tuned-xl:0.000 xgb-xl:0.126 xgb-l:0.447 mlp-adaptive-xl:0.080 mlp-l:0.225 svr-rbf-xl:0.100 svr-poly-l:0.000 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.4594, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2149
  Round 3/3: Mean predicted reward = 9.981

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 34 Results ---
  Mean Oracle Reward: 9.652
  Min Oracle Reward: 1.220
  Max Oracle Reward: 11.704
  Std Oracle Reward: 2.030
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.083, Max: 0.193, Count: 13
  Total Sequences Evaluated: 1138

======================================================================
EXPERIMENT ROUND 35/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1138

--- Round 35 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AGCGTGCTGACC
  CATCCTGGGCAG
  CGTAGAGCGCTC
  GATGCACCTGCG
  ACGCGGAGCTCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.219
  Max reward: 12.972
  With intrinsic bonuses: 10.229

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.5111, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1748

=== Surrogate Model Training ===
Total samples: 1170

Training on 1114 samples (removed 56 outliers)
Reward range: [6.79, 13.30], mean: 10.07
  Created 13 candidate models for data size 1114
Current R2 threshold: -0.04999999999999999
  rf-tuned-l: R2 = 0.140 (std: 0.062)
  rf-tuned-xl: R2 = 0.144 (std: 0.068)
  gb-tuned-l: R2 = 0.176 (std: 0.077)
  gb-tuned-xl: R2 = 0.176 (std: 0.077)
  xgb-xl: R2 = 0.043 (std: 0.024)
  xgb-l: R2 = 0.043 (std: 0.024)
  mlp-adaptive-xl: R2 = 0.096 (std: 0.070)
  mlp-l: R2 = 0.086 (std: 0.075)
  svr-rbf-xl: R2 = 0.209 (std: 0.047)
  svr-poly-l: R2 = 0.209 (std: 0.047)
  knn-tuned-sqrt: R2 = 0.061 (std: 0.062)
  knn-tuned-l: R2 = 0.061 (std: 0.062)
  ridge: R2 = -0.020 (std: 0.056)

Model-based training with 13 models
Best R2: 0.209, Mean R2: 0.109
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.255 gb-tuned-l:0.000 gb-tuned-xl:0.030 xgb-xl:0.486 xgb-l:0.100 mlp-adaptive-xl:0.005 mlp-l:0.061 svr-rbf-xl:0.000 svr-poly-l:0.000 knn-tuned-sqrt:0.063 knn-tuned-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9707, entropy=0.4721, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8552
  Round 1/3: Mean predicted reward = 9.815
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.255 gb-tuned-l:0.000 gb-tuned-xl:0.030 xgb-xl:0.486 xgb-l:0.100 mlp-adaptive-xl:0.005 mlp-l:0.061 svr-rbf-xl:0.000 svr-poly-l:0.000 knn-tuned-sqrt:0.063 knn-tuned-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.4550, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4259
  Round 2/3: Mean predicted reward = 9.948
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.255 gb-tuned-l:0.000 gb-tuned-xl:0.030 xgb-xl:0.486 xgb-l:0.100 mlp-adaptive-xl:0.005 mlp-l:0.061 svr-rbf-xl:0.000 svr-poly-l:0.000 knn-tuned-sqrt:0.063 knn-tuned-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.4687, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1778
  Round 3/3: Mean predicted reward = 10.013

  === Progress Analysis ===
  Status: NORMAL

--- Round 35 Results ---
  Mean Oracle Reward: 10.211
  Min Oracle Reward: 6.810
  Max Oracle Reward: 13.087
  Std Oracle Reward: 1.209
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.109, Max: 0.209, Count: 13
  Total Sequences Evaluated: 1170

======================================================================
EXPERIMENT ROUND 36/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1170

--- Round 36 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGTCCACGTAGC
  AGCCTGTGCCAG
  ACCCGGGATGTC
  TCAACGCTGGCG
  CCGTAGCTGAGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.328
  Max reward: 12.701
  With intrinsic bonuses: 10.381

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9730, entropy=0.4609, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4149

=== Surrogate Model Training ===
Total samples: 1202

Training on 1146 samples (removed 56 outliers)
Reward range: [6.79, 13.30], mean: 10.08
  Created 13 candidate models for data size 1146
Current R2 threshold: -0.03999999999999998
  rf-tuned-l: R2 = 0.149 (std: 0.072)
  rf-tuned-xl: R2 = 0.151 (std: 0.078)
  gb-tuned-l: R2 = 0.191 (std: 0.086)
  gb-tuned-xl: R2 = 0.191 (std: 0.086)
  xgb-xl: R2 = 0.057 (std: 0.043)
  xgb-l: R2 = 0.057 (std: 0.043)
  mlp-adaptive-xl: R2 = 0.127 (std: 0.067)
  mlp-l: R2 = 0.110 (std: 0.094)
  svr-rbf-xl: R2 = 0.215 (std: 0.058)
  svr-poly-l: R2 = 0.215 (std: 0.058)
  knn-tuned-sqrt: R2 = 0.077 (std: 0.072)
  knn-tuned-l: R2 = 0.077 (std: 0.072)
  ridge: R2 = -0.014 (std: 0.059)

Model-based training with 13 models
Best R2: 0.215, Mean R2: 0.123
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.137 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.470 xgb-l:0.086 mlp-adaptive-xl:0.061 mlp-l:0.045 svr-rbf-xl:0.059 svr-poly-l:0.000 knn-tuned-sqrt:0.046 knn-tuned-l:0.000 ridge:0.096
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.4235, kl_div=0.0000
    Epoch 1: policy_loss=-0.0523, value_loss=0.9699, entropy=0.4289, kl_div=-0.0435
  Round 1/3: Mean predicted reward = 9.906
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.137 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.470 xgb-l:0.086 mlp-adaptive-xl:0.061 mlp-l:0.045 svr-rbf-xl:0.059 svr-poly-l:0.000 knn-tuned-sqrt:0.046 knn-tuned-l:0.000 ridge:0.096
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.4575, kl_div=0.0000
    Epoch 1: policy_loss=-0.0013, value_loss=0.9692, entropy=0.4668, kl_div=-0.2816
  Round 2/3: Mean predicted reward = 9.866
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.137 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.470 xgb-l:0.086 mlp-adaptive-xl:0.061 mlp-l:0.045 svr-rbf-xl:0.059 svr-poly-l:0.000 knn-tuned-sqrt:0.046 knn-tuned-l:0.000 ridge:0.096
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9700, entropy=0.4636, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0939
  Round 3/3: Mean predicted reward = 9.990

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 36 Results ---
  Mean Oracle Reward: 10.332
  Min Oracle Reward: 7.180
  Max Oracle Reward: 12.876
  Std Oracle Reward: 1.321
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.123, Max: 0.215, Count: 13
  Total Sequences Evaluated: 1202

======================================================================
EXPERIMENT ROUND 37/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1202
  Consistent improvement, increasing LR to 0.000240

--- Round 37 Configuration ---
Learning rate: 0.000240
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GAGGACCCTGTC
  GCCTTAGGGACC
  TACGGACTCCGG
  GAGCCCAGGCTT
  AGCCCGTTGCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.501
  Max reward: 14.286
  With intrinsic bonuses: 10.495

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.4571, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2724

=== Surrogate Model Training ===
Total samples: 1234

Training on 1177 samples (removed 57 outliers)
Reward range: [6.79, 13.30], mean: 10.09
  Created 13 candidate models for data size 1177
Current R2 threshold: -0.02999999999999997
  rf-tuned-l: R2 = 0.143 (std: 0.067)
  rf-tuned-xl: R2 = 0.136 (std: 0.069)
  gb-tuned-l: R2 = 0.179 (std: 0.074)
  gb-tuned-xl: R2 = 0.179 (std: 0.074)
  xgb-xl: R2 = 0.039 (std: 0.067)
  xgb-l: R2 = 0.039 (std: 0.067)
  mlp-adaptive-xl: R2 = 0.132 (std: 0.077)
  mlp-l: R2 = 0.122 (std: 0.100)
  svr-rbf-xl: R2 = 0.206 (std: 0.058)
  svr-poly-l: R2 = 0.206 (std: 0.058)
  knn-tuned-sqrt: R2 = 0.072 (std: 0.077)
  knn-tuned-l: R2 = 0.072 (std: 0.077)
  ridge: R2 = -0.012 (std: 0.062)

Model-based training with 13 models
Best R2: 0.206, Mean R2: 0.117
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.063 rf-tuned-xl:0.148 gb-tuned-l:0.100 gb-tuned-xl:0.150 xgb-xl:0.342 xgb-l:0.142 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.055
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.4518, kl_div=0.0000
    Epoch 1: policy_loss=-0.0732, value_loss=0.9683, entropy=0.4514, kl_div=-0.0328
  Round 1/3: Mean predicted reward = 9.803
    Using ridge regression weights
    Model weights: rf-tuned-l:0.063 rf-tuned-xl:0.148 gb-tuned-l:0.100 gb-tuned-xl:0.150 xgb-xl:0.342 xgb-l:0.142 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.055
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.4367, kl_div=0.0000
    Epoch 1: policy_loss=-0.0915, value_loss=0.9701, entropy=0.4395, kl_div=-0.0569
  Round 2/3: Mean predicted reward = 10.041
    Using ridge regression weights
    Model weights: rf-tuned-l:0.063 rf-tuned-xl:0.148 gb-tuned-l:0.100 gb-tuned-xl:0.150 xgb-xl:0.342 xgb-l:0.142 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.055
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9707, entropy=0.4305, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0615
  Round 3/3: Mean predicted reward = 10.203

  === Progress Analysis ===
  Status: NORMAL

--- Round 37 Results ---
  Mean Oracle Reward: 10.510
  Min Oracle Reward: 8.197
  Max Oracle Reward: 14.132
  Std Oracle Reward: 1.249
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.117, Max: 0.206, Count: 13
  Total Sequences Evaluated: 1234

======================================================================
EXPERIMENT ROUND 38/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1234
  Consistent improvement, increasing LR to 0.000132

--- Round 38 Configuration ---
Learning rate: 0.000132
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCAGGACGCATG
  GACCTGCTACGG
  GGGACTGTCCAC
  CCCATACGGGGT
  TCAGCCTAGCGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.347
  Max reward: 12.091
  With intrinsic bonuses: 10.352

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9711, entropy=0.4170, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1964

=== Surrogate Model Training ===
Total samples: 1266

Training on 1209 samples (removed 57 outliers)
Reward range: [6.79, 13.30], mean: 10.10
  Created 13 candidate models for data size 1209
Current R2 threshold: -0.019999999999999962
  rf-tuned-l: R2 = 0.148 (std: 0.059)
  rf-tuned-xl: R2 = 0.160 (std: 0.069)
  gb-tuned-l: R2 = 0.203 (std: 0.076)
  gb-tuned-xl: R2 = 0.203 (std: 0.076)
  xgb-xl: R2 = 0.043 (std: 0.069)
  xgb-l: R2 = 0.043 (std: 0.069)
  mlp-adaptive-xl: R2 = 0.126 (std: 0.121)
  mlp-l: R2 = 0.157 (std: 0.106)
  svr-rbf-xl: R2 = 0.228 (std: 0.067)
  svr-poly-l: R2 = 0.228 (std: 0.067)
  knn-tuned-sqrt: R2 = 0.081 (std: 0.084)
  knn-tuned-l: R2 = 0.081 (std: 0.084)
  ridge: R2 = -0.009 (std: 0.074)

Model-based training with 13 models
Best R2: 0.228, Mean R2: 0.130
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.198 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.353 xgb-l:0.119 mlp-adaptive-xl:0.064 mlp-l:0.192 svr-rbf-xl:0.052 svr-poly-l:0.000 knn-tuned-sqrt:0.006 knn-tuned-l:0.000 ridge:0.016
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9708, entropy=0.4278, kl_div=0.0000
    Epoch 1: policy_loss=-0.0631, value_loss=0.9708, entropy=0.4264, kl_div=-0.0116
  Round 1/3: Mean predicted reward = 10.040
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.198 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.353 xgb-l:0.119 mlp-adaptive-xl:0.064 mlp-l:0.192 svr-rbf-xl:0.052 svr-poly-l:0.000 knn-tuned-sqrt:0.006 knn-tuned-l:0.000 ridge:0.016
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.4359, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0792
  Round 2/3: Mean predicted reward = 10.110
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.198 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.353 xgb-l:0.119 mlp-adaptive-xl:0.064 mlp-l:0.192 svr-rbf-xl:0.052 svr-poly-l:0.000 knn-tuned-sqrt:0.006 knn-tuned-l:0.000 ridge:0.016
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9713, entropy=0.4119, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1455
  Round 3/3: Mean predicted reward = 10.079

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 38 Results ---
  Mean Oracle Reward: 10.339
  Min Oracle Reward: 7.373
  Max Oracle Reward: 12.240
  Std Oracle Reward: 1.144
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.130, Max: 0.228, Count: 13
  Total Sequences Evaluated: 1266

======================================================================
EXPERIMENT ROUND 39/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1266
  Performance plateaued, reducing LR to 0.000019

--- Round 39 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCGCAATGGACT
  CGAATGCGTGCC
  ACTCAGCGCGGT
  TCGAGCCAGGCT
  CGGGTCAGACCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.626
  Max reward: 12.265
  With intrinsic bonuses: 10.628

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9715, entropy=0.4254, kl_div=0.0000
    Epoch 1: policy_loss=-0.0268, value_loss=0.9715, entropy=0.4245, kl_div=0.0458

=== Surrogate Model Training ===
Total samples: 1298

Training on 1239 samples (removed 59 outliers)
Reward range: [6.84, 13.30], mean: 10.12
  Created 13 candidate models for data size 1239
Current R2 threshold: -0.010000000000000009
  rf-tuned-l: R2 = 0.161 (std: 0.070)
  rf-tuned-xl: R2 = 0.159 (std: 0.068)
  gb-tuned-l: R2 = 0.208 (std: 0.092)
  gb-tuned-xl: R2 = 0.208 (std: 0.092)
  xgb-xl: R2 = 0.077 (std: 0.097)
  xgb-l: R2 = 0.077 (std: 0.097)
  mlp-adaptive-xl: R2 = 0.145 (std: 0.104)
  mlp-l: R2 = 0.131 (std: 0.093)
  svr-rbf-xl: R2 = 0.237 (std: 0.072)
  svr-poly-l: R2 = 0.237 (std: 0.072)
  knn-tuned-sqrt: R2 = 0.067 (std: 0.075)
  knn-tuned-l: R2 = 0.067 (std: 0.075)
  ridge: R2 = -0.012 (std: 0.079)

Model-based training with 12 models
Best R2: 0.237, Mean R2: 0.135
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.035 rf-tuned-xl:0.191 gb-tuned-l:0.000 gb-tuned-xl:0.049 xgb-xl:0.526 xgb-l:0.153 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000 knn-tuned-sqrt:0.000 knn-tuned-l:0.045
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9715, entropy=0.4035, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0661
  Round 1/3: Mean predicted reward = 10.020
    Using ridge regression weights
    Model weights: rf-tuned-l:0.035 rf-tuned-xl:0.191 gb-tuned-l:0.000 gb-tuned-xl:0.049 xgb-xl:0.526 xgb-l:0.153 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000 knn-tuned-sqrt:0.000 knn-tuned-l:0.045
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.3696, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0569
  Round 2/3: Mean predicted reward = 9.908
    Using ridge regression weights
    Model weights: rf-tuned-l:0.035 rf-tuned-xl:0.191 gb-tuned-l:0.000 gb-tuned-xl:0.049 xgb-xl:0.526 xgb-l:0.153 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000 knn-tuned-sqrt:0.000 knn-tuned-l:0.045
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9711, entropy=0.4095, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0701
  Round 3/3: Mean predicted reward = 10.299

  === Progress Analysis ===
  Status: NORMAL

--- Round 39 Results ---
  Mean Oracle Reward: 10.642
  Min Oracle Reward: 8.337
  Max Oracle Reward: 12.098
  Std Oracle Reward: 0.887
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.135, Max: 0.237, Count: 13
  Total Sequences Evaluated: 1298

======================================================================
EXPERIMENT ROUND 40/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1298

--- Round 40 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCGGATGAGCTC
  ACATTCCGAGGG
  ACGCCGGGTCAT
  GTGCCGGATCAC
  AGGGCCTGCACT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.407
  Max reward: 12.946
  With intrinsic bonuses: 10.511

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9712, entropy=0.4108, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1220

=== Surrogate Model Training ===
Total samples: 1330

Training on 1269 samples (removed 61 outliers)
Reward range: [6.85, 13.30], mean: 10.13
  Created 13 candidate models for data size 1269
Current R2 threshold: 0.0
  rf-tuned-l: R2 = 0.165 (std: 0.068)
  rf-tuned-xl: R2 = 0.154 (std: 0.068)
  gb-tuned-l: R2 = 0.210 (std: 0.085)
  gb-tuned-xl: R2 = 0.210 (std: 0.085)
  xgb-xl: R2 = 0.067 (std: 0.076)
  xgb-l: R2 = 0.067 (std: 0.076)
  mlp-adaptive-xl: R2 = 0.148 (std: 0.120)
  mlp-l: R2 = 0.153 (std: 0.092)
  svr-rbf-xl: R2 = 0.235 (std: 0.068)
  svr-poly-l: R2 = 0.235 (std: 0.068)
  knn-tuned-sqrt: R2 = 0.059 (std: 0.066)
  knn-tuned-l: R2 = 0.059 (std: 0.066)
  ridge: R2 = -0.015 (std: 0.075)

Model-based training with 12 models
Best R2: 0.235, Mean R2: 0.134
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.185 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.215 xgb-l:0.246 mlp-adaptive-xl:0.102 mlp-l:0.027 svr-rbf-xl:0.225 svr-poly-l:0.000 knn-tuned-sqrt:0.000 knn-tuned-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.3606, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0982
  Round 1/3: Mean predicted reward = 9.921
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.185 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.215 xgb-l:0.246 mlp-adaptive-xl:0.102 mlp-l:0.027 svr-rbf-xl:0.225 svr-poly-l:0.000 knn-tuned-sqrt:0.000 knn-tuned-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9699, entropy=0.3471, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.6360
  Round 2/3: Mean predicted reward = 10.135
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.185 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.215 xgb-l:0.246 mlp-adaptive-xl:0.102 mlp-l:0.027 svr-rbf-xl:0.225 svr-poly-l:0.000 knn-tuned-sqrt:0.000 knn-tuned-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.3697, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0781
  Round 3/3: Mean predicted reward = 10.322

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 40 Results ---
  Mean Oracle Reward: 10.429
  Min Oracle Reward: 7.094
  Max Oracle Reward: 12.826
  Std Oracle Reward: 1.255
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.134, Max: 0.235, Count: 13
  Total Sequences Evaluated: 1330

======================================================================
EXPERIMENT ROUND 41/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1330

--- Round 41 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  GCCGTTGACACG
  CGCAGCGGATTA
  ATATCCGGGCAG
  CTGAAGCGTGCC
  GGTCGCAAGTCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.181
  Max reward: 12.908
  With intrinsic bonuses: 10.244

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9700, entropy=0.3333, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3410

=== Surrogate Model Training ===
Total samples: 1362

Training on 1298 samples (removed 64 outliers)
Reward range: [6.90, 13.23], mean: 10.13
  Created 13 candidate models for data size 1298
Current R2 threshold: 0.010000000000000009
  rf-tuned-l: R2 = 0.172 (std: 0.079)
  rf-tuned-xl: R2 = 0.168 (std: 0.074)
  gb-tuned-l: R2 = 0.203 (std: 0.095)
  gb-tuned-xl: R2 = 0.203 (std: 0.095)
  xgb-xl: R2 = 0.092 (std: 0.078)
  xgb-l: R2 = 0.092 (std: 0.078)
  mlp-adaptive-xl: R2 = 0.098 (std: 0.072)
  mlp-l: R2 = 0.132 (std: 0.126)
  svr-rbf-xl: R2 = 0.235 (std: 0.076)
  svr-poly-l: R2 = 0.235 (std: 0.076)
  knn-tuned-sqrt: R2 = 0.064 (std: 0.067)
  knn-tuned-l: R2 = 0.064 (std: 0.067)
  ridge: R2 = -0.010 (std: 0.075)

Model-based training with 12 models
Best R2: 0.235, Mean R2: 0.134
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.019 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.399 xgb-l:0.282 mlp-adaptive-xl:0.133 mlp-l:0.007 svr-rbf-xl:0.131 svr-poly-l:0.000 knn-tuned-sqrt:0.029 knn-tuned-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.3064, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0818
  Round 1/3: Mean predicted reward = 10.252
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.019 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.399 xgb-l:0.282 mlp-adaptive-xl:0.133 mlp-l:0.007 svr-rbf-xl:0.131 svr-poly-l:0.000 knn-tuned-sqrt:0.029 knn-tuned-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.3094, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3412
  Round 2/3: Mean predicted reward = 10.213
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.019 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.399 xgb-l:0.282 mlp-adaptive-xl:0.133 mlp-l:0.007 svr-rbf-xl:0.131 svr-poly-l:0.000 knn-tuned-sqrt:0.029 knn-tuned-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.3038, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6396
  Round 3/3: Mean predicted reward = 10.377

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 41 Results ---
  Mean Oracle Reward: 10.190
  Min Oracle Reward: 6.368
  Max Oracle Reward: 12.712
  Std Oracle Reward: 1.171
  Sequence Diversity: 0.969
  Models Used: 12
  Model R2 - Mean: 0.134, Max: 0.235, Count: 13
  Total Sequences Evaluated: 1362

======================================================================
EXPERIMENT ROUND 42/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1362

--- Round 42 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGTCCAGCTCAG
  GTCAACGTGCGC
  ACACGGTCGGTC
  GCTGACCTAGGC
  TGACGGGTCACC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.121
  Max reward: 12.141
  With intrinsic bonuses: 10.179

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9702, entropy=0.2822, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1899

=== Surrogate Model Training ===
Total samples: 1394

Training on 1329 samples (removed 65 outliers)
Reward range: [6.96, 13.23], mean: 10.14
  Created 13 candidate models for data size 1329
Current R2 threshold: 0.020000000000000018
  rf-tuned-l: R2 = 0.151 (std: 0.078)
  rf-tuned-xl: R2 = 0.160 (std: 0.074)
  gb-tuned-l: R2 = 0.184 (std: 0.089)
  gb-tuned-xl: R2 = 0.184 (std: 0.089)
  xgb-xl: R2 = 0.057 (std: 0.054)
  xgb-l: R2 = 0.057 (std: 0.054)
  mlp-adaptive-xl: R2 = 0.157 (std: 0.108)
  mlp-l: R2 = 0.118 (std: 0.100)
  svr-rbf-xl: R2 = 0.226 (std: 0.075)
  svr-poly-l: R2 = 0.226 (std: 0.075)
  knn-tuned-sqrt: R2 = 0.058 (std: 0.064)
  knn-tuned-l: R2 = 0.058 (std: 0.064)
  ridge: R2 = -0.010 (std: 0.076)

Model-based training with 12 models
Best R2: 0.226, Mean R2: 0.125
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.252 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.526 xgb-l:0.214 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.008 knn-tuned-sqrt:0.000 knn-tuned-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9672, entropy=0.3211, kl_div=0.0000
    Epoch 1: policy_loss=-0.0067, value_loss=0.9673, entropy=0.3239, kl_div=-0.0787
  Round 1/3: Mean predicted reward = 10.124
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.252 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.526 xgb-l:0.214 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.008 knn-tuned-sqrt:0.000 knn-tuned-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.2817, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2686
  Round 2/3: Mean predicted reward = 10.031
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.252 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.526 xgb-l:0.214 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.008 knn-tuned-sqrt:0.000 knn-tuned-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.3289, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5541
  Round 3/3: Mean predicted reward = 10.261

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 42 Results ---
  Mean Oracle Reward: 10.085
  Min Oracle Reward: 8.015
  Max Oracle Reward: 11.923
  Std Oracle Reward: 0.895
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.125, Max: 0.226, Count: 13
  Total Sequences Evaluated: 1394

======================================================================
EXPERIMENT ROUND 43/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1394

--- Round 43 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGCCGGATTCAC
  GATGGACGCCTC
  AGTGGTCCCGAA
  ACGACGTTCGCG
  TGGTGGCCACCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.965
  Max reward: 11.556
  With intrinsic bonuses: 9.957

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9711, entropy=0.2971, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1428

=== Surrogate Model Training ===
Total samples: 1426

Training on 1360 samples (removed 66 outliers)
Reward range: [6.96, 13.23], mean: 10.14
  Created 13 candidate models for data size 1360
Current R2 threshold: 0.030000000000000027
  rf-tuned-l: R2 = 0.182 (std: 0.057)
  rf-tuned-xl: R2 = 0.175 (std: 0.066)
  gb-tuned-l: R2 = 0.197 (std: 0.093)
  gb-tuned-xl: R2 = 0.197 (std: 0.093)
  xgb-xl: R2 = 0.099 (std: 0.030)
  xgb-l: R2 = 0.099 (std: 0.030)
  mlp-adaptive-xl: R2 = 0.137 (std: 0.080)
  mlp-l: R2 = 0.142 (std: 0.100)
  svr-rbf-xl: R2 = 0.238 (std: 0.082)
  svr-poly-l: R2 = 0.238 (std: 0.082)
  knn-tuned-sqrt: R2 = 0.057 (std: 0.085)
  knn-tuned-l: R2 = 0.057 (std: 0.085)
  ridge: R2 = -0.003 (std: 0.080)

Model-based training with 12 models
Best R2: 0.238, Mean R2: 0.140
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.109 gb-tuned-xl:0.000 xgb-xl:0.026 xgb-l:0.272 mlp-adaptive-xl:0.242 mlp-l:0.108 svr-rbf-xl:0.037 svr-poly-l:0.098 knn-tuned-sqrt:0.000 knn-tuned-l:0.108
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.3230, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2527
  Round 1/3: Mean predicted reward = 9.956
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.109 gb-tuned-xl:0.000 xgb-xl:0.026 xgb-l:0.272 mlp-adaptive-xl:0.242 mlp-l:0.108 svr-rbf-xl:0.037 svr-poly-l:0.098 knn-tuned-sqrt:0.000 knn-tuned-l:0.108
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.3013, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4014
  Round 2/3: Mean predicted reward = 10.011
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.109 gb-tuned-xl:0.000 xgb-xl:0.026 xgb-l:0.272 mlp-adaptive-xl:0.242 mlp-l:0.108 svr-rbf-xl:0.037 svr-poly-l:0.098 knn-tuned-sqrt:0.000 knn-tuned-l:0.108
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3009, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2169
  Round 3/3: Mean predicted reward = 10.181

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 43 Results ---
  Mean Oracle Reward: 9.971
  Min Oracle Reward: 3.477
  Max Oracle Reward: 11.708
  Std Oracle Reward: 1.530
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.140, Max: 0.238, Count: 13
  Total Sequences Evaluated: 1426

======================================================================
EXPERIMENT ROUND 44/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1426
  Performance plateaued, reducing LR to 0.000019

--- Round 44 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTCATCAGGGCG
  TGCTGACGACGC
  GGATGTCCGACC
  ATCTGTCGCAAG
  CAGCGTTAGCGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.255
  Max reward: 11.728
  With intrinsic bonuses: 10.284

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9711, entropy=0.2973, kl_div=0.0000
    Epoch 1: policy_loss=-0.0131, value_loss=0.9711, entropy=0.2970, kl_div=0.0424

=== Surrogate Model Training ===
Total samples: 1458

Training on 1390 samples (removed 68 outliers)
Reward range: [6.98, 13.23], mean: 10.14
  Created 13 candidate models for data size 1390
Current R2 threshold: 0.040000000000000036
  rf-tuned-l: R2 = 0.174 (std: 0.053)
  rf-tuned-xl: R2 = 0.175 (std: 0.048)
  gb-tuned-l: R2 = 0.205 (std: 0.081)
  gb-tuned-xl: R2 = 0.205 (std: 0.081)
  xgb-xl: R2 = 0.085 (std: 0.048)
  xgb-l: R2 = 0.085 (std: 0.048)
  mlp-adaptive-xl: R2 = 0.120 (std: 0.085)
  mlp-l: R2 = 0.149 (std: 0.049)
  svr-rbf-xl: R2 = 0.235 (std: 0.068)
  svr-poly-l: R2 = 0.235 (std: 0.068)
  knn-tuned-sqrt: R2 = 0.060 (std: 0.063)
  knn-tuned-l: R2 = 0.060 (std: 0.063)
  ridge: R2 = -0.009 (std: 0.075)

Model-based training with 12 models
Best R2: 0.235, Mean R2: 0.137
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.021 rf-tuned-xl:0.060 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.283 xgb-l:0.054 mlp-adaptive-xl:0.000 mlp-l:0.130 svr-rbf-xl:0.251 svr-poly-l:0.200 knn-tuned-sqrt:0.000 knn-tuned-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2972, kl_div=0.0000
    Epoch 1: policy_loss=0.0054, value_loss=0.9687, entropy=0.2972, kl_div=0.0110
  Round 1/3: Mean predicted reward = 9.818
    Using ridge regression weights
    Model weights: rf-tuned-l:0.021 rf-tuned-xl:0.060 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.283 xgb-l:0.054 mlp-adaptive-xl:0.000 mlp-l:0.130 svr-rbf-xl:0.251 svr-poly-l:0.200 knn-tuned-sqrt:0.000 knn-tuned-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.3175, kl_div=0.0000
    Epoch 1: policy_loss=-0.0087, value_loss=0.9691, entropy=0.3175, kl_div=0.0126
  Round 2/3: Mean predicted reward = 9.976
    Using ridge regression weights
    Model weights: rf-tuned-l:0.021 rf-tuned-xl:0.060 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.283 xgb-l:0.054 mlp-adaptive-xl:0.000 mlp-l:0.130 svr-rbf-xl:0.251 svr-poly-l:0.200 knn-tuned-sqrt:0.000 knn-tuned-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9709, entropy=0.2928, kl_div=0.0000
    Epoch 1: policy_loss=-0.0113, value_loss=0.9709, entropy=0.2927, kl_div=0.0321
  Round 3/3: Mean predicted reward = 10.085

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 44 Results ---
  Mean Oracle Reward: 10.244
  Min Oracle Reward: 6.529
  Max Oracle Reward: 11.595
  Std Oracle Reward: 0.905
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.137, Max: 0.235, Count: 13
  Total Sequences Evaluated: 1458

======================================================================
EXPERIMENT ROUND 45/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1458

--- Round 45 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGCCTGACTACG
  AGACGCGTCCTG
  CGTCATGGACCG
  GACCGCAGTCTG
  TCGCGGCGACTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.082
  Max reward: 11.928
  With intrinsic bonuses: 10.079

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9722, entropy=0.2773, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4534

=== Surrogate Model Training ===
Total samples: 1490

Training on 1419 samples (removed 71 outliers)
Reward range: [7.01, 13.23], mean: 10.15
  Created 13 candidate models for data size 1419
Current R2 threshold: 0.050000000000000044
  rf-tuned-l: R2 = 0.193 (std: 0.062)
  rf-tuned-xl: R2 = 0.189 (std: 0.063)
  gb-tuned-l: R2 = 0.215 (std: 0.074)
  gb-tuned-xl: R2 = 0.215 (std: 0.074)
  xgb-xl: R2 = 0.123 (std: 0.047)
  xgb-l: R2 = 0.123 (std: 0.047)
  mlp-adaptive-xl: R2 = 0.149 (std: 0.050)
  mlp-l: R2 = 0.181 (std: 0.062)
  svr-rbf-xl: R2 = 0.240 (std: 0.060)
  svr-poly-l: R2 = 0.240 (std: 0.060)
  knn-tuned-sqrt: R2 = 0.062 (std: 0.061)
  knn-tuned-l: R2 = 0.062 (std: 0.061)
  ridge: R2 = -0.002 (std: 0.076)

Model-based training with 12 models
Best R2: 0.240, Mean R2: 0.153
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.123 gb-tuned-l:0.042 gb-tuned-xl:0.160 xgb-xl:0.316 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.117 svr-rbf-xl:0.143 svr-poly-l:0.099 knn-tuned-sqrt:0.000 knn-tuned-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.3025, kl_div=0.0000
    Epoch 1: policy_loss=-0.0441, value_loss=0.9688, entropy=0.3031, kl_div=-0.1223
  Round 1/3: Mean predicted reward = 9.805
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.123 gb-tuned-l:0.042 gb-tuned-xl:0.160 xgb-xl:0.316 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.117 svr-rbf-xl:0.143 svr-poly-l:0.099 knn-tuned-sqrt:0.000 knn-tuned-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9710, entropy=0.2950, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2894
  Round 2/3: Mean predicted reward = 9.954
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.123 gb-tuned-l:0.042 gb-tuned-xl:0.160 xgb-xl:0.316 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.117 svr-rbf-xl:0.143 svr-poly-l:0.099 knn-tuned-sqrt:0.000 knn-tuned-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9704, entropy=0.2950, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4501
  Round 3/3: Mean predicted reward = 10.091

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 45 Results ---
  Mean Oracle Reward: 10.103
  Min Oracle Reward: 6.099
  Max Oracle Reward: 12.149
  Std Oracle Reward: 1.455
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.153, Max: 0.240, Count: 13
  Total Sequences Evaluated: 1490

======================================================================
EXPERIMENT ROUND 46/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1490

--- Round 46 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AAGTTCCCGCGG
  CTACGCGAGTCG
  AGGCACTTCCGG
  CCATTGGAGGCC
  CCTCGGAGATCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.290
  Max reward: 13.287
  With intrinsic bonuses: 10.330

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.3019, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3576

=== Surrogate Model Training ===
Total samples: 1522

Training on 1448 samples (removed 74 outliers)
Reward range: [7.01, 13.23], mean: 10.16
  Created 13 candidate models for data size 1448
Current R2 threshold: 0.06
  rf-tuned-l: R2 = 0.193 (std: 0.066)
  rf-tuned-xl: R2 = 0.190 (std: 0.071)
  gb-tuned-l: R2 = 0.206 (std: 0.075)
  gb-tuned-xl: R2 = 0.206 (std: 0.075)
  xgb-xl: R2 = 0.110 (std: 0.058)
  xgb-l: R2 = 0.110 (std: 0.058)
  mlp-adaptive-xl: R2 = 0.128 (std: 0.085)
  mlp-l: R2 = 0.137 (std: 0.073)
  svr-rbf-xl: R2 = 0.231 (std: 0.076)
  svr-poly-l: R2 = 0.231 (std: 0.076)
  knn-tuned-sqrt: R2 = 0.051 (std: 0.067)
  knn-tuned-l: R2 = 0.051 (std: 0.067)
  ridge: R2 = -0.006 (std: 0.081)

Model-based training with 10 models
Best R2: 0.231, Mean R2: 0.141
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.277 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.095 xgb-l:0.117 mlp-adaptive-xl:0.000 mlp-l:0.025 svr-rbf-xl:0.487 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.2723, kl_div=0.0000
    Epoch 1: policy_loss=0.0043, value_loss=0.9693, entropy=0.2693, kl_div=-0.1339
  Round 1/3: Mean predicted reward = 9.767
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.277 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.095 xgb-l:0.117 mlp-adaptive-xl:0.000 mlp-l:0.025 svr-rbf-xl:0.487 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.2518, kl_div=0.0000
    Epoch 1: policy_loss=-0.0617, value_loss=0.9695, entropy=0.2518, kl_div=-0.0574
  Round 2/3: Mean predicted reward = 9.918
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.277 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.095 xgb-l:0.117 mlp-adaptive-xl:0.000 mlp-l:0.025 svr-rbf-xl:0.487 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9702, entropy=0.2696, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9016
  Round 3/3: Mean predicted reward = 10.198

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 46 Results ---
  Mean Oracle Reward: 10.310
  Min Oracle Reward: 6.394
  Max Oracle Reward: 13.276
  Std Oracle Reward: 1.480
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.141, Max: 0.231, Count: 13
  Total Sequences Evaluated: 1522

======================================================================
EXPERIMENT ROUND 47/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1522
  Performance plateaued, reducing LR to 0.000100

--- Round 47 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGTCGCCACGTA
  CTCCGTGCGGAA
  GTCGCGAAGCCT
  CGTGGCCGAATC
  GACTCCGGTAGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.428
  Max reward: 13.355
  With intrinsic bonuses: 10.470

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9717, entropy=0.3080, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2349

=== Surrogate Model Training ===
Total samples: 1554

Training on 1476 samples (removed 78 outliers)
Reward range: [7.01, 13.25], mean: 10.17
  Created 13 candidate models for data size 1476
Current R2 threshold: 0.07
  rf-tuned-l: R2 = 0.182 (std: 0.065)
  rf-tuned-xl: R2 = 0.181 (std: 0.061)
  gb-tuned-l: R2 = 0.197 (std: 0.074)
  gb-tuned-xl: R2 = 0.197 (std: 0.074)
  xgb-xl: R2 = 0.099 (std: 0.065)
  xgb-l: R2 = 0.099 (std: 0.065)
  mlp-adaptive-xl: R2 = 0.165 (std: 0.054)
  mlp-l: R2 = 0.132 (std: 0.067)
  svr-rbf-xl: R2 = 0.233 (std: 0.074)
  svr-poly-l: R2 = 0.233 (std: 0.074)
  knn-tuned-sqrt: R2 = 0.064 (std: 0.065)
  knn-tuned-l: R2 = 0.064 (std: 0.065)
  ridge: R2 = -0.012 (std: 0.084)

Model-based training with 10 models
Best R2: 0.233, Mean R2: 0.141
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.080 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.238 xgb-l:0.000 mlp-adaptive-xl:0.240 mlp-l:0.183 svr-rbf-xl:0.258 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9713, entropy=0.2818, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0840
  Round 1/3: Mean predicted reward = 9.991
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.080 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.238 xgb-l:0.000 mlp-adaptive-xl:0.240 mlp-l:0.183 svr-rbf-xl:0.258 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.2504, kl_div=0.0000
    Epoch 1: policy_loss=-0.0491, value_loss=0.9693, entropy=0.2493, kl_div=-0.0282
  Round 2/3: Mean predicted reward = 10.106
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.080 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.238 xgb-l:0.000 mlp-adaptive-xl:0.240 mlp-l:0.183 svr-rbf-xl:0.258 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9708, entropy=0.2755, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2025
  Round 3/3: Mean predicted reward = 10.186

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 47 Results ---
  Mean Oracle Reward: 10.451
  Min Oracle Reward: 3.421
  Max Oracle Reward: 13.490
  Std Oracle Reward: 2.097
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.141, Max: 0.233, Count: 13
  Total Sequences Evaluated: 1554

======================================================================
EXPERIMENT ROUND 48/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1554
  Consistent improvement, increasing LR to 0.000132

--- Round 48 Configuration ---
Learning rate: 0.000132
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  AGCCTGGTCCGA
  GCGAGTCCCATG
  GGCGACCGTTAA
  GACCCCGGTAGT
  CGCCTCGGTGAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.591
  Max reward: 13.511
  With intrinsic bonuses: 10.592

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.2894, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6479

=== Surrogate Model Training ===
Total samples: 1586

Training on 1502 samples (removed 84 outliers)
Reward range: [7.06, 13.23], mean: 10.18
  Created 13 candidate models for data size 1502
Current R2 threshold: 0.08000000000000002
  rf-tuned-l: R2 = 0.177 (std: 0.071)
  rf-tuned-xl: R2 = 0.181 (std: 0.065)
  gb-tuned-l: R2 = 0.198 (std: 0.083)
  gb-tuned-xl: R2 = 0.198 (std: 0.083)
  xgb-xl: R2 = 0.075 (std: 0.046)
  xgb-l: R2 = 0.075 (std: 0.046)
  mlp-adaptive-xl: R2 = 0.045 (std: 0.104)
  mlp-l: R2 = 0.054 (std: 0.066)
  svr-rbf-xl: R2 = 0.225 (std: 0.078)
  svr-poly-l: R2 = 0.225 (std: 0.078)
  knn-tuned-sqrt: R2 = 0.060 (std: 0.079)
  knn-tuned-l: R2 = 0.060 (std: 0.079)
  ridge: R2 = -0.009 (std: 0.086)

Model-based training with 6 models
Best R2: 0.225, Mean R2: 0.120
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.440 gb-tuned-l:0.000 gb-tuned-xl:0.115 svr-rbf-xl:0.106 svr-poly-l:0.340
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2958, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3054
  Round 1/3: Mean predicted reward = 10.082
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.440 gb-tuned-l:0.000 gb-tuned-xl:0.115 svr-rbf-xl:0.106 svr-poly-l:0.340
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.2793, kl_div=0.0000
    Epoch 1: policy_loss=-0.0293, value_loss=0.9684, entropy=0.2784, kl_div=0.0455
  Round 2/3: Mean predicted reward = 9.806
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.440 gb-tuned-l:0.000 gb-tuned-xl:0.115 svr-rbf-xl:0.106 svr-poly-l:0.340
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.2969, kl_div=0.0000
    Epoch 1: policy_loss=-0.0393, value_loss=0.9700, entropy=0.2946, kl_div=0.0131
  Round 3/3: Mean predicted reward = 10.174

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 48 Results ---
  Mean Oracle Reward: 10.526
  Min Oracle Reward: 8.551
  Max Oracle Reward: 13.285
  Std Oracle Reward: 1.023
  Sequence Diversity: 0.969
  Models Used: 6
  Model R2 - Mean: 0.120, Max: 0.225, Count: 13
  Total Sequences Evaluated: 1586

======================================================================
EXPERIMENT ROUND 49/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1586
  Consistent improvement, increasing LR to 0.000045

--- Round 49 Configuration ---
Learning rate: 0.000045
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTGCCTCAGGGA
  CGGCTTCGAGAC
  GCAGACCTTCGG
  CTGCCTAAGGCG
  GATTCCGGCAGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.332
  Max reward: 12.368
  With intrinsic bonuses: 10.374

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9712, entropy=0.2714, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0793

=== Surrogate Model Training ===
Total samples: 1618

Training on 1532 samples (removed 86 outliers)
Reward range: [7.09, 13.23], mean: 10.19
  Created 13 candidate models for data size 1532
Current R2 threshold: 0.09000000000000002
  rf-tuned-l: R2 = 0.178 (std: 0.058)
  rf-tuned-xl: R2 = 0.181 (std: 0.059)
  gb-tuned-l: R2 = 0.192 (std: 0.069)
  gb-tuned-xl: R2 = 0.192 (std: 0.069)
  xgb-xl: R2 = 0.067 (std: 0.061)
  xgb-l: R2 = 0.067 (std: 0.061)
  mlp-adaptive-xl: R2 = 0.153 (std: 0.068)
  mlp-l: R2 = 0.149 (std: 0.095)
  svr-rbf-xl: R2 = 0.228 (std: 0.067)
  svr-poly-l: R2 = 0.228 (std: 0.067)
  knn-tuned-sqrt: R2 = 0.057 (std: 0.073)
  knn-tuned-l: R2 = 0.057 (std: 0.073)
  ridge: R2 = -0.008 (std: 0.083)

Model-based training with 8 models
Best R2: 0.228, Mean R2: 0.134
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.778 gb-tuned-l:0.000 gb-tuned-xl:0.021 mlp-adaptive-xl:0.060 mlp-l:0.000 svr-rbf-xl:0.141 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.2706, kl_div=0.0000
    Epoch 1: policy_loss=-0.0066, value_loss=0.9692, entropy=0.2702, kl_div=0.0101
  Round 1/3: Mean predicted reward = 9.814
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.778 gb-tuned-l:0.000 gb-tuned-xl:0.021 mlp-adaptive-xl:0.060 mlp-l:0.000 svr-rbf-xl:0.141 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.2694, kl_div=0.0000
    Epoch 1: policy_loss=-0.0232, value_loss=0.9699, entropy=0.2695, kl_div=-0.0255
  Round 2/3: Mean predicted reward = 9.823
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.778 gb-tuned-l:0.000 gb-tuned-xl:0.021 mlp-adaptive-xl:0.060 mlp-l:0.000 svr-rbf-xl:0.141 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.2517, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0537
  Round 3/3: Mean predicted reward = 10.175

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 49 Results ---
  Mean Oracle Reward: 10.373
  Min Oracle Reward: 5.840
  Max Oracle Reward: 12.370
  Std Oracle Reward: 1.499
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: 0.134, Max: 0.228, Count: 13
  Total Sequences Evaluated: 1618

======================================================================
EXPERIMENT ROUND 50/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1618

--- Round 50 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  GTTCCACAGCGG
  GTCGAGCCCTAG
  AGCAGCTGCCTG
  GGCCCAGCTGAT
  GTCGCGTAAACG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.132
  Max reward: 12.109
  With intrinsic bonuses: 10.140

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9707, entropy=0.2913, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1440

=== Surrogate Model Training ===
Total samples: 1650

Training on 1560 samples (removed 90 outliers)
Reward range: [7.11, 13.20], mean: 10.19
  Created 13 candidate models for data size 1560
Current R2 threshold: 0.10000000000000003
  rf-tuned-l: R2 = 0.191 (std: 0.065)
  rf-tuned-xl: R2 = 0.188 (std: 0.066)
  gb-tuned-l: R2 = 0.201 (std: 0.073)
  gb-tuned-xl: R2 = 0.201 (std: 0.073)
  xgb-xl: R2 = 0.093 (std: 0.061)
  xgb-l: R2 = 0.093 (std: 0.061)
  mlp-adaptive-xl: R2 = 0.151 (std: 0.083)
  mlp-l: R2 = 0.131 (std: 0.084)
  svr-rbf-xl: R2 = 0.249 (std: 0.073)
  svr-poly-l: R2 = 0.249 (std: 0.073)
  knn-tuned-sqrt: R2 = 0.075 (std: 0.067)
  knn-tuned-l: R2 = 0.075 (std: 0.067)
  ridge: R2 = 0.000 (std: 0.087)

Model-based training with 8 models
Best R2: 0.249, Mean R2: 0.146
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.531 gb-tuned-l:0.000 gb-tuned-xl:0.027 mlp-adaptive-xl:0.052 mlp-l:0.000 svr-rbf-xl:0.191 svr-poly-l:0.199
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9672, entropy=0.2830, kl_div=0.0000
    Epoch 1: policy_loss=0.0696, value_loss=0.9672, entropy=0.2816, kl_div=-0.3766
  Round 1/3: Mean predicted reward = 9.810
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.531 gb-tuned-l:0.000 gb-tuned-xl:0.027 mlp-adaptive-xl:0.052 mlp-l:0.000 svr-rbf-xl:0.191 svr-poly-l:0.199
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.2445, kl_div=0.0000
    Epoch 1: policy_loss=0.0041, value_loss=0.9701, entropy=0.2419, kl_div=-0.2601
  Round 2/3: Mean predicted reward = 9.988
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.531 gb-tuned-l:0.000 gb-tuned-xl:0.027 mlp-adaptive-xl:0.052 mlp-l:0.000 svr-rbf-xl:0.191 svr-poly-l:0.199
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.2693, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2426
  Round 3/3: Mean predicted reward = 10.275

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 50 Results ---
  Mean Oracle Reward: 10.123
  Min Oracle Reward: 7.207
  Max Oracle Reward: 12.032
  Std Oracle Reward: 1.141
  Sequence Diversity: 0.969
  Models Used: 8
  Model R2 - Mean: 0.146, Max: 0.249, Count: 13
  Total Sequences Evaluated: 1650

======================================================================
EXPERIMENT ROUND 51/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1650

--- Round 51 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  TACCGGGTGACA
  ACCACTGTGCGG
  TTCCAATGGCAG
  GGCTAGCCTCAG
  TCGGACGCGCTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.789
  Max reward: 13.084
  With intrinsic bonuses: 10.794

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.2373, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5146

=== Surrogate Model Training ===
Total samples: 1682

Training on 1594 samples (removed 88 outliers)
Reward range: [7.11, 13.23], mean: 10.21
  Created 13 candidate models for data size 1594
Current R2 threshold: 0.11000000000000004
  rf-tuned-l: R2 = 0.192 (std: 0.065)
  rf-tuned-xl: R2 = 0.183 (std: 0.073)
  gb-tuned-l: R2 = 0.216 (std: 0.084)
  gb-tuned-xl: R2 = 0.216 (std: 0.084)
  xgb-xl: R2 = 0.155 (std: 0.075)
  xgb-l: R2 = 0.155 (std: 0.075)
  mlp-adaptive-xl: R2 = 0.174 (std: 0.084)
  mlp-l: R2 = 0.175 (std: 0.079)
  svr-rbf-xl: R2 = 0.264 (std: 0.084)
  svr-poly-l: R2 = 0.264 (std: 0.084)
  knn-tuned-sqrt: R2 = 0.074 (std: 0.093)
  knn-tuned-l: R2 = 0.074 (std: 0.093)
  ridge: R2 = -0.001 (std: 0.097)

Model-based training with 10 models
Best R2: 0.264, Mean R2: 0.165
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.377 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.404 xgb-l:0.113 mlp-adaptive-xl:0.106 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.2389, kl_div=0.0000
    Epoch 1: policy_loss=-0.0562, value_loss=0.9686, entropy=0.2359, kl_div=0.0346
  Round 1/3: Mean predicted reward = 9.797
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.377 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.404 xgb-l:0.113 mlp-adaptive-xl:0.106 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.2516, kl_div=0.0000
    Epoch 1: policy_loss=0.1800, value_loss=0.9691, entropy=0.2577, kl_div=-0.6142
  Round 2/3: Mean predicted reward = 10.044
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.377 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.404 xgb-l:0.113 mlp-adaptive-xl:0.106 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.2628, kl_div=0.0000
    Epoch 1: policy_loss=-0.0228, value_loss=0.9694, entropy=0.2618, kl_div=-0.0093
  Round 3/3: Mean predicted reward = 10.265

  === Progress Analysis ===
  Status: NORMAL

--- Round 51 Results ---
  Mean Oracle Reward: 10.784
  Min Oracle Reward: 8.161
  Max Oracle Reward: 13.391
  Std Oracle Reward: 1.280
  Sequence Diversity: 0.969
  Models Used: 10
  Model R2 - Mean: 0.165, Max: 0.264, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 1682

======================================================================
EXPERIMENT ROUND 52/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1682

--- Round 52 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.938) ---
  TCAGCAGCTGCG
  TCACGCGGGCAT
  GGCAACCTCGGT
  CAAGTCCTGCGG
  ATCCCGGGTAGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.633
  Max reward: 13.387
  With intrinsic bonuses: 10.591

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9714, entropy=0.2217, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4798

=== Surrogate Model Training ===
Total samples: 1714

Training on 1625 samples (removed 89 outliers)
Reward range: [7.09, 13.25], mean: 10.21
  Created 13 candidate models for data size 1625
Current R2 threshold: 0.12
  rf-tuned-l: R2 = 0.212 (std: 0.092)
  rf-tuned-xl: R2 = 0.211 (std: 0.097)
  gb-tuned-l: R2 = 0.228 (std: 0.098)
  gb-tuned-xl: R2 = 0.228 (std: 0.098)
  xgb-xl: R2 = 0.133 (std: 0.073)
  xgb-l: R2 = 0.133 (std: 0.073)
  mlp-adaptive-xl: R2 = 0.184 (std: 0.070)
  mlp-l: R2 = 0.186 (std: 0.094)
  svr-rbf-xl: R2 = 0.277 (std: 0.095)
  svr-poly-l: R2 = 0.277 (std: 0.095)
  knn-tuned-sqrt: R2 = 0.091 (std: 0.101)
  knn-tuned-l: R2 = 0.091 (std: 0.101)
  ridge: R2 = 0.010 (std: 0.111)

Model-based training with 10 models
Best R2: 0.277, Mean R2: 0.174
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.010 rf-tuned-xl:0.171 gb-tuned-l:0.158 gb-tuned-xl:0.107 xgb-xl:0.000 xgb-l:0.186 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.367 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2413, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1908
  Round 1/3: Mean predicted reward = 9.763
    Using ridge regression weights
    Model weights: rf-tuned-l:0.010 rf-tuned-xl:0.171 gb-tuned-l:0.158 gb-tuned-xl:0.107 xgb-xl:0.000 xgb-l:0.186 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.367 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.1858, kl_div=0.0000
    Epoch 1: policy_loss=-0.0061, value_loss=0.9697, entropy=0.1856, kl_div=-0.0774
  Round 2/3: Mean predicted reward = 9.948
    Using ridge regression weights
    Model weights: rf-tuned-l:0.010 rf-tuned-xl:0.171 gb-tuned-l:0.158 gb-tuned-xl:0.107 xgb-xl:0.000 xgb-l:0.186 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.367 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9709, entropy=0.2352, kl_div=0.0000
    Epoch 1: policy_loss=-0.0341, value_loss=0.9709, entropy=0.2352, kl_div=-0.0825
  Round 3/3: Mean predicted reward = 10.140

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 52 Results ---
  Mean Oracle Reward: 10.654
  Min Oracle Reward: 6.504
  Max Oracle Reward: 13.153
  Std Oracle Reward: 1.675
  Sequence Diversity: 0.938
  Models Used: 10
  Model R2 - Mean: 0.174, Max: 0.277, Count: 13
  Total Sequences Evaluated: 1714

======================================================================
EXPERIMENT ROUND 53/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1714

--- Round 53 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGAACGGCTCGC
  TTCCCCGAGGAG
  TGCGCGCGTACA
  GGCCGTTACGAC
  CGGACGTGCATC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.771
  Max reward: 14.459
  With intrinsic bonuses: 10.760

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.2435, kl_div=0.0000
    Epoch 1: policy_loss=-0.0547, value_loss=0.9698, entropy=0.2433, kl_div=0.0190

=== Surrogate Model Training ===
Total samples: 1746

Training on 1659 samples (removed 87 outliers)
Reward range: [7.07, 13.31], mean: 10.23
  Created 13 candidate models for data size 1659
Current R2 threshold: 0.13
  rf-tuned-l: R2 = 0.199 (std: 0.092)
  rf-tuned-xl: R2 = 0.200 (std: 0.089)
  gb-tuned-l: R2 = 0.221 (std: 0.092)
  gb-tuned-xl: R2 = 0.221 (std: 0.092)
  xgb-xl: R2 = 0.154 (std: 0.072)
  xgb-l: R2 = 0.154 (std: 0.072)
  mlp-adaptive-xl: R2 = 0.203 (std: 0.061)
  mlp-l: R2 = 0.197 (std: 0.088)
  svr-rbf-xl: R2 = 0.272 (std: 0.097)
  svr-poly-l: R2 = 0.272 (std: 0.097)
  knn-tuned-sqrt: R2 = 0.092 (std: 0.105)
  knn-tuned-l: R2 = 0.092 (std: 0.105)
  ridge: R2 = 0.002 (std: 0.122)

Model-based training with 10 models
Best R2: 0.272, Mean R2: 0.175
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.027 gb-tuned-xl:0.074 xgb-xl:0.268 xgb-l:0.325 mlp-adaptive-xl:0.000 mlp-l:0.124 svr-rbf-xl:0.181 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2395, kl_div=0.0000
    Epoch 1: policy_loss=-0.0305, value_loss=0.9687, entropy=0.2411, kl_div=-0.0496
  Round 1/3: Mean predicted reward = 9.605
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.027 gb-tuned-xl:0.074 xgb-xl:0.268 xgb-l:0.325 mlp-adaptive-xl:0.000 mlp-l:0.124 svr-rbf-xl:0.181 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9695, entropy=0.2008, kl_div=0.0000
    Epoch 1: policy_loss=0.0468, value_loss=0.9695, entropy=0.2037, kl_div=-0.2102
  Round 2/3: Mean predicted reward = 9.787
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.027 gb-tuned-xl:0.074 xgb-xl:0.268 xgb-l:0.325 mlp-adaptive-xl:0.000 mlp-l:0.124 svr-rbf-xl:0.181 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.2180, kl_div=0.0000
    Epoch 1: policy_loss=-0.0353, value_loss=0.9705, entropy=0.2178, kl_div=0.0465
  Round 3/3: Mean predicted reward = 10.211

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 53 Results ---
  Mean Oracle Reward: 10.731
  Min Oracle Reward: 6.611
  Max Oracle Reward: 14.515
  Std Oracle Reward: 1.636
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.175, Max: 0.272, Count: 13
  Total Sequences Evaluated: 1746

======================================================================
EXPERIMENT ROUND 54/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1746
  Performance plateaued, reducing LR to 0.000019

--- Round 54 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.938) ---
  TAGGCGCCCTAG
  CGACTCGGTAGC
  GCCTACAGTGCG
  GTACGGCCCTGA
  ACCTGGAGCTCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.948
  Max reward: 13.439
  With intrinsic bonuses: 10.873

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9711, entropy=0.2514, kl_div=0.0000
    Epoch 1: policy_loss=-0.0206, value_loss=0.9711, entropy=0.2511, kl_div=0.0294

=== Surrogate Model Training ===
Total samples: 1778

Training on 1691 samples (removed 87 outliers)
Reward range: [7.07, 13.31], mean: 10.24
  Created 13 candidate models for data size 1691
Current R2 threshold: 0.14
  rf-tuned-l: R2 = 0.205 (std: 0.071)
  rf-tuned-xl: R2 = 0.195 (std: 0.078)
  gb-tuned-l: R2 = 0.220 (std: 0.093)
  gb-tuned-xl: R2 = 0.220 (std: 0.093)
  xgb-xl: R2 = 0.143 (std: 0.056)
  xgb-l: R2 = 0.143 (std: 0.056)
  mlp-adaptive-xl: R2 = 0.197 (std: 0.077)
  mlp-l: R2 = 0.188 (std: 0.096)
  svr-rbf-xl: R2 = 0.265 (std: 0.082)
  svr-poly-l: R2 = 0.265 (std: 0.082)
  knn-tuned-sqrt: R2 = 0.094 (std: 0.106)
  knn-tuned-l: R2 = 0.094 (std: 0.106)
  ridge: R2 = -0.003 (std: 0.121)

Model-based training with 10 models
Best R2: 0.265, Mean R2: 0.171
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.345 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.383 xgb-l:0.158 mlp-adaptive-xl:0.018 mlp-l:0.000 svr-rbf-xl:0.096 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.2453, kl_div=0.0000
    Epoch 1: policy_loss=0.0052, value_loss=0.9680, entropy=0.2452, kl_div=0.0258
  Round 1/3: Mean predicted reward = 9.953
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.345 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.383 xgb-l:0.158 mlp-adaptive-xl:0.018 mlp-l:0.000 svr-rbf-xl:0.096 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=0.2724, kl_div=0.0000
    Epoch 1: policy_loss=-0.0106, value_loss=0.9675, entropy=0.2729, kl_div=-0.0113
  Round 2/3: Mean predicted reward = 10.114
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.345 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.383 xgb-l:0.158 mlp-adaptive-xl:0.018 mlp-l:0.000 svr-rbf-xl:0.096 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.2385, kl_div=0.0000
    Epoch 1: policy_loss=-0.0045, value_loss=0.9701, entropy=0.2390, kl_div=-0.0170
  Round 3/3: Mean predicted reward = 10.380

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 54 Results ---
  Mean Oracle Reward: 10.848
  Min Oracle Reward: 8.256
  Max Oracle Reward: 13.366
  Std Oracle Reward: 1.375
  Sequence Diversity: 0.938
  Models Used: 10
  Model R2 - Mean: 0.171, Max: 0.265, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 1778

======================================================================
EXPERIMENT ROUND 55/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1778
  Consistent improvement, increasing LR to 0.000360

--- Round 55 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  CTCACGGACTGG
  AGGATCGCGCTC
  CGCCGGAAGCTT
  CTCGAGCGAGTC
  CTGGGAAGTACC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 11.079
  Max reward: 13.713
  With intrinsic bonuses: 11.025

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.2281, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4682

=== Surrogate Model Training ===
Total samples: 1810

Training on 1723 samples (removed 87 outliers)
Reward range: [7.06, 13.31], mean: 10.25
  Created 13 candidate models for data size 1723
Current R2 threshold: 0.15000000000000002
  rf-tuned-l: R2 = 0.189 (std: 0.069)
  rf-tuned-xl: R2 = 0.189 (std: 0.059)
  gb-tuned-l: R2 = 0.220 (std: 0.075)
  gb-tuned-xl: R2 = 0.220 (std: 0.075)
  xgb-xl: R2 = 0.151 (std: 0.056)
  xgb-l: R2 = 0.151 (std: 0.056)
  mlp-adaptive-xl: R2 = 0.196 (std: 0.058)
  mlp-l: R2 = 0.188 (std: 0.071)
  svr-rbf-xl: R2 = 0.252 (std: 0.070)
  svr-poly-l: R2 = 0.252 (std: 0.070)
  knn-tuned-sqrt: R2 = 0.079 (std: 0.098)
  knn-tuned-l: R2 = 0.079 (std: 0.098)
  ridge: R2 = -0.003 (std: 0.117)

Model-based training with 10 models
Best R2: 0.252, Mean R2: 0.166
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.283 xgb-l:0.318 mlp-adaptive-xl:0.001 mlp-l:0.022 svr-rbf-xl:0.268 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9685, entropy=0.2438, kl_div=0.0000
    Epoch 1: policy_loss=0.0124, value_loss=0.9685, entropy=0.2491, kl_div=-0.0174
  Round 1/3: Mean predicted reward = 9.662
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.283 xgb-l:0.318 mlp-adaptive-xl:0.001 mlp-l:0.022 svr-rbf-xl:0.268 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.2199, kl_div=0.0000
    Epoch 1: policy_loss=0.0654, value_loss=0.9683, entropy=0.2336, kl_div=-0.6498
  Round 2/3: Mean predicted reward = 9.702
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.283 xgb-l:0.318 mlp-adaptive-xl:0.001 mlp-l:0.022 svr-rbf-xl:0.268 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9704, entropy=0.2750, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3370
  Round 3/3: Mean predicted reward = 10.392

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 55 Results ---
  Mean Oracle Reward: 11.066
  Min Oracle Reward: 8.263
  Max Oracle Reward: 13.721
  Std Oracle Reward: 1.439
  Sequence Diversity: 0.969
  Models Used: 10
  Model R2 - Mean: 0.166, Max: 0.252, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 1810

======================================================================
EXPERIMENT ROUND 56/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1810
  Consistent improvement, increasing LR to 0.000327

--- Round 56 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGCGTGAACAGT
  GCATTCGCAGCG
  CGATCAGCTAGG
  ACCCTGGCTGAG
  ACATCTGGCGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.921
  Max reward: 13.147
  With intrinsic bonuses: 10.936

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9709, entropy=0.2441, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6676

=== Surrogate Model Training ===
Total samples: 1842

Training on 1756 samples (removed 86 outliers)
Reward range: [7.06, 13.37], mean: 10.27
  Created 13 candidate models for data size 1756
Current R2 threshold: 0.16000000000000003
  rf-tuned-l: R2 = 0.198 (std: 0.069)
  rf-tuned-xl: R2 = 0.196 (std: 0.074)
  gb-tuned-l: R2 = 0.221 (std: 0.075)
  gb-tuned-xl: R2 = 0.221 (std: 0.075)
  xgb-xl: R2 = 0.140 (std: 0.051)
  xgb-l: R2 = 0.140 (std: 0.051)
  mlp-adaptive-xl: R2 = 0.183 (std: 0.098)
  mlp-l: R2 = 0.169 (std: 0.090)
  svr-rbf-xl: R2 = 0.258 (std: 0.074)
  svr-poly-l: R2 = 0.258 (std: 0.074)
  knn-tuned-sqrt: R2 = 0.079 (std: 0.099)
  knn-tuned-l: R2 = 0.079 (std: 0.099)
  ridge: R2 = -0.006 (std: 0.117)

Model-based training with 8 models
Best R2: 0.258, Mean R2: 0.164
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.624 gb-tuned-l:0.000 gb-tuned-xl:0.020 mlp-adaptive-xl:0.107 mlp-l:0.057 svr-rbf-xl:0.192 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2351, kl_div=0.0000
    Epoch 1: policy_loss=0.0052, value_loss=0.9688, entropy=0.2435, kl_div=-0.0226
  Round 1/3: Mean predicted reward = 9.788
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.624 gb-tuned-l:0.000 gb-tuned-xl:0.020 mlp-adaptive-xl:0.107 mlp-l:0.057 svr-rbf-xl:0.192 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.3088, kl_div=0.0000
    Epoch 1: policy_loss=-0.0365, value_loss=0.9696, entropy=0.3145, kl_div=-0.1604
  Round 2/3: Mean predicted reward = 10.061
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.624 gb-tuned-l:0.000 gb-tuned-xl:0.020 mlp-adaptive-xl:0.107 mlp-l:0.057 svr-rbf-xl:0.192 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.2606, kl_div=0.0000
    Epoch 1: policy_loss=-0.0125, value_loss=0.9694, entropy=0.2621, kl_div=-0.2770
  Round 3/3: Mean predicted reward = 10.135

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 56 Results ---
  Mean Oracle Reward: 10.962
  Min Oracle Reward: 7.227
  Max Oracle Reward: 13.195
  Std Oracle Reward: 1.374
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: 0.164, Max: 0.258, Count: 13
  Total Sequences Evaluated: 1842

======================================================================
EXPERIMENT ROUND 57/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1842
  Performance plateaued, reducing LR to 0.000100

--- Round 57 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTCGAAGGTCGC
  ACGGCCTTAGGC
  GTGACAAGGCTC
  TCGCGACTGAGC
  GATGCCGGTCCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 11.016
  Max reward: 13.130
  With intrinsic bonuses: 10.988

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.2904, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1945

=== Surrogate Model Training ===
Total samples: 1874

Training on 1792 samples (removed 82 outliers)
Reward range: [7.03, 13.42], mean: 10.28
  Created 13 candidate models for data size 1792
Current R2 threshold: 0.17000000000000004
  rf-tuned-l: R2 = 0.187 (std: 0.060)
  rf-tuned-xl: R2 = 0.196 (std: 0.062)
  gb-tuned-l: R2 = 0.220 (std: 0.072)
  gb-tuned-xl: R2 = 0.220 (std: 0.072)
  xgb-xl: R2 = 0.126 (std: 0.054)
  xgb-l: R2 = 0.126 (std: 0.054)
  mlp-adaptive-xl: R2 = 0.191 (std: 0.052)
  mlp-l: R2 = 0.182 (std: 0.053)
  svr-rbf-xl: R2 = 0.260 (std: 0.062)
  svr-poly-l: R2 = 0.260 (std: 0.062)
  knn-tuned-sqrt: R2 = 0.088 (std: 0.090)
  knn-tuned-l: R2 = 0.088 (std: 0.090)
  ridge: R2 = -0.020 (std: 0.127)

Model-based training with 8 models
Best R2: 0.260, Mean R2: 0.163
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.588 gb-tuned-l:0.000 gb-tuned-xl:0.015 mlp-adaptive-xl:0.072 mlp-l:0.000 svr-rbf-xl:0.159 svr-poly-l:0.165
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.2665, kl_div=0.0000
    Epoch 1: policy_loss=-0.0039, value_loss=0.9690, entropy=0.2660, kl_div=0.0133
  Round 1/3: Mean predicted reward = 9.993
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.588 gb-tuned-l:0.000 gb-tuned-xl:0.015 mlp-adaptive-xl:0.072 mlp-l:0.000 svr-rbf-xl:0.159 svr-poly-l:0.165
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9695, entropy=0.2470, kl_div=0.0000
    Epoch 1: policy_loss=-0.0158, value_loss=0.9695, entropy=0.2466, kl_div=-0.0730
  Round 2/3: Mean predicted reward = 10.115
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.588 gb-tuned-l:0.000 gb-tuned-xl:0.015 mlp-adaptive-xl:0.072 mlp-l:0.000 svr-rbf-xl:0.159 svr-poly-l:0.165
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.2786, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1707
  Round 3/3: Mean predicted reward = 10.240

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 57 Results ---
  Mean Oracle Reward: 10.963
  Min Oracle Reward: 7.780
  Max Oracle Reward: 13.265
  Std Oracle Reward: 1.311
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: 0.163, Max: 0.260, Count: 13
  Total Sequences Evaluated: 1874

======================================================================
EXPERIMENT ROUND 58/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1874
  Performance plateaued, reducing LR to 0.000055

--- Round 58 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCTTCCGCAAGG
  CTCCGGCAAGGT
  CGCGATCGTAGC
  ACCGGCAGCGTT
  GGGGCTCTACCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.554
  Max reward: 13.353
  With intrinsic bonuses: 10.534

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.2634, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1243

=== Surrogate Model Training ===
Total samples: 1906

Training on 1826 samples (removed 80 outliers)
Reward range: [7.01, 13.42], mean: 10.28
  Created 13 candidate models for data size 1826
Current R2 threshold: 0.18
  rf-tuned-l: R2 = 0.194 (std: 0.065)
  rf-tuned-xl: R2 = 0.200 (std: 0.062)
  gb-tuned-l: R2 = 0.227 (std: 0.083)
  gb-tuned-xl: R2 = 0.227 (std: 0.083)
  xgb-xl: R2 = 0.131 (std: 0.056)
  xgb-l: R2 = 0.131 (std: 0.056)
  mlp-adaptive-xl: R2 = 0.210 (std: 0.053)
  mlp-l: R2 = 0.217 (std: 0.076)
  svr-rbf-xl: R2 = 0.273 (std: 0.064)
  svr-poly-l: R2 = 0.273 (std: 0.064)
  knn-tuned-sqrt: R2 = 0.092 (std: 0.090)
  knn-tuned-l: R2 = 0.092 (std: 0.090)
  ridge: R2 = -0.019 (std: 0.138)

Model-based training with 8 models
Best R2: 0.273, Mean R2: 0.173
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.666 gb-tuned-l:0.000 gb-tuned-xl:0.009 mlp-adaptive-xl:0.000 mlp-l:0.103 svr-rbf-xl:0.222 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.2606, kl_div=0.0000
    Epoch 1: policy_loss=-0.0083, value_loss=0.9692, entropy=0.2593, kl_div=0.0203
  Round 1/3: Mean predicted reward = 9.849
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.666 gb-tuned-l:0.000 gb-tuned-xl:0.009 mlp-adaptive-xl:0.000 mlp-l:0.103 svr-rbf-xl:0.222 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.2791, kl_div=0.0000
    Epoch 1: policy_loss=-0.0232, value_loss=0.9697, entropy=0.2786, kl_div=-0.1180
  Round 2/3: Mean predicted reward = 10.279
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.666 gb-tuned-l:0.000 gb-tuned-xl:0.009 mlp-adaptive-xl:0.000 mlp-l:0.103 svr-rbf-xl:0.222 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.2732, kl_div=0.0000
    Epoch 1: policy_loss=-0.0371, value_loss=0.9696, entropy=0.2721, kl_div=0.0076
  Round 3/3: Mean predicted reward = 10.188

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 58 Results ---
  Mean Oracle Reward: 10.517
  Min Oracle Reward: 6.902
  Max Oracle Reward: 12.808
  Std Oracle Reward: 1.495
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: 0.173, Max: 0.273, Count: 13
  Total Sequences Evaluated: 1906

======================================================================
EXPERIMENT ROUND 59/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1906

--- Round 59 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  TCCCACGGGTGA
  CCCAGTGTCAGG
  TACGAGTACGCG
  GGGCGCATCCTA
  CGTGGACTACCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.784
  Max reward: 13.451
  With intrinsic bonuses: 10.749

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.2677, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0922

=== Surrogate Model Training ===
Total samples: 1938

Training on 1858 samples (removed 80 outliers)
Reward range: [7.01, 13.42], mean: 10.29
  Created 13 candidate models for data size 1858
Current R2 threshold: 0.19
  rf-tuned-l: R2 = 0.219 (std: 0.093)
  rf-tuned-xl: R2 = 0.227 (std: 0.086)
  gb-tuned-l: R2 = 0.248 (std: 0.081)
  gb-tuned-xl: R2 = 0.248 (std: 0.081)
  xgb-xl: R2 = 0.167 (std: 0.097)
  xgb-l: R2 = 0.167 (std: 0.097)
  mlp-adaptive-xl: R2 = 0.242 (std: 0.078)
  mlp-l: R2 = 0.216 (std: 0.060)
  svr-rbf-xl: R2 = 0.289 (std: 0.077)
  svr-poly-l: R2 = 0.289 (std: 0.077)
  knn-tuned-sqrt: R2 = 0.117 (std: 0.107)
  knn-tuned-l: R2 = 0.117 (std: 0.107)
  ridge: R2 = -0.011 (std: 0.136)

Model-based training with 8 models
Best R2: 0.289, Mean R2: 0.195
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.574 gb-tuned-l:0.000 gb-tuned-xl:0.001 mlp-adaptive-xl:0.125 mlp-l:0.056 svr-rbf-xl:0.243 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2938, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0523
  Round 1/3: Mean predicted reward = 9.694
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.574 gb-tuned-l:0.000 gb-tuned-xl:0.001 mlp-adaptive-xl:0.125 mlp-l:0.056 svr-rbf-xl:0.243 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.2301, kl_div=0.0000
    Epoch 1: policy_loss=-0.0167, value_loss=0.9690, entropy=0.2299, kl_div=-0.0082
  Round 2/3: Mean predicted reward = 10.022
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.574 gb-tuned-l:0.000 gb-tuned-xl:0.001 mlp-adaptive-xl:0.125 mlp-l:0.056 svr-rbf-xl:0.243 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.2847, kl_div=0.0000
    Epoch 1: policy_loss=-0.0199, value_loss=0.9701, entropy=0.2841, kl_div=-0.0042
  Round 3/3: Mean predicted reward = 10.285

  === Progress Analysis ===
  Status: NORMAL

--- Round 59 Results ---
  Mean Oracle Reward: 10.772
  Min Oracle Reward: 7.342
  Max Oracle Reward: 13.234
  Std Oracle Reward: 1.407
  Sequence Diversity: 0.969
  Models Used: 8
  Model R2 - Mean: 0.195, Max: 0.289, Count: 13
  Total Sequences Evaluated: 1938

======================================================================
EXPERIMENT ROUND 60/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1938

--- Round 60 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AAGCGTCGTCGC
  CCTTCGGGGAAC
  GGTTGCCCCAGA
  AAGGCAGCTGTC
  AGTGACGCCTCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.701
  Max reward: 13.369
  With intrinsic bonuses: 10.743

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.2378, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5458

=== Surrogate Model Training ===
Total samples: 1970

Training on 1890 samples (removed 80 outliers)
Reward range: [7.01, 13.42], mean: 10.30
  Created 13 candidate models for data size 1890
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.230 (std: 0.097)
  rf-tuned-xl: R2 = 0.238 (std: 0.087)
  gb-tuned-l: R2 = 0.256 (std: 0.090)
  gb-tuned-xl: R2 = 0.256 (std: 0.090)
  xgb-xl: R2 = 0.153 (std: 0.115)
  xgb-l: R2 = 0.153 (std: 0.115)
  mlp-adaptive-xl: R2 = 0.235 (std: 0.087)
  mlp-l: R2 = 0.247 (std: 0.078)
  svr-rbf-xl: R2 = 0.293 (std: 0.088)
  svr-poly-l: R2 = 0.293 (std: 0.088)
  knn-tuned-sqrt: R2 = 0.112 (std: 0.112)
  knn-tuned-l: R2 = 0.112 (std: 0.112)
  ridge: R2 = -0.010 (std: 0.140)

Model-based training with 8 models
Best R2: 0.293, Mean R2: 0.197
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.475 gb-tuned-l:0.000 gb-tuned-xl:0.098 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.326 svr-poly-l:0.101
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.2601, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1231
  Round 1/3: Mean predicted reward = 9.297
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.475 gb-tuned-l:0.000 gb-tuned-xl:0.098 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.326 svr-poly-l:0.101
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.2217, kl_div=0.0000
    Epoch 1: policy_loss=-0.0152, value_loss=0.9684, entropy=0.2239, kl_div=-0.3210
  Round 2/3: Mean predicted reward = 9.539
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.475 gb-tuned-l:0.000 gb-tuned-xl:0.098 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.326 svr-poly-l:0.101
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2269, kl_div=0.0000
    Epoch 1: policy_loss=0.0070, value_loss=0.9690, entropy=0.2298, kl_div=-0.0432
  Round 3/3: Mean predicted reward = 10.200

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 60 Results ---
  Mean Oracle Reward: 10.753
  Min Oracle Reward: 8.198
  Max Oracle Reward: 13.179
  Std Oracle Reward: 1.534
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: 0.197, Max: 0.293, Count: 13
  Total Sequences Evaluated: 1970

======================================================================
EXPERIMENT ROUND 61/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1970
  Performance plateaued, reducing LR to 0.000136

--- Round 61 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  AGTAGCCTCCGG
  GTGACCACGCGT
  ATCGCGCCGAGT
  TCGGTCCGGCAA
  TTCCCCGAGAGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.722
  Max reward: 13.331
  With intrinsic bonuses: 10.703

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9713, entropy=0.2663, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2104

=== Surrogate Model Training ===
Total samples: 2002

Training on 1921 samples (removed 81 outliers)
Reward range: [7.01, 13.42], mean: 10.31
  Created 13 candidate models for data size 1921
Current R2 threshold: 0.21000000000000002
  rf-tuned-l: R2 = 0.233 (std: 0.103)
  rf-tuned-xl: R2 = 0.242 (std: 0.099)
  gb-tuned-l: R2 = 0.261 (std: 0.086)
  gb-tuned-xl: R2 = 0.261 (std: 0.086)
  xgb-xl: R2 = 0.190 (std: 0.106)
  xgb-l: R2 = 0.190 (std: 0.106)
  mlp-adaptive-xl: R2 = 0.246 (std: 0.079)
  mlp-l: R2 = 0.241 (std: 0.072)
  svr-rbf-xl: R2 = 0.306 (std: 0.088)
  svr-poly-l: R2 = 0.306 (std: 0.088)
  knn-tuned-sqrt: R2 = 0.120 (std: 0.123)
  knn-tuned-l: R2 = 0.120 (std: 0.123)
  ridge: R2 = -0.008 (std: 0.131)

Model-based training with 8 models
Best R2: 0.306, Mean R2: 0.208
Running 5 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.261 gb-tuned-l:0.129 gb-tuned-xl:0.166 mlp-adaptive-xl:0.357 mlp-l:0.000 svr-rbf-xl:0.087 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.2318, kl_div=0.0000
    Epoch 1: policy_loss=-0.0199, value_loss=0.9686, entropy=0.2315, kl_div=0.0317
  Round 1/5: Mean predicted reward = 9.796
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.261 gb-tuned-l:0.129 gb-tuned-xl:0.166 mlp-adaptive-xl:0.357 mlp-l:0.000 svr-rbf-xl:0.087 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.2419, kl_div=0.0000
    Epoch 1: policy_loss=-0.0482, value_loss=0.9692, entropy=0.2444, kl_div=-0.1279
  Round 2/5: Mean predicted reward = 10.033
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.261 gb-tuned-l:0.129 gb-tuned-xl:0.166 mlp-adaptive-xl:0.357 mlp-l:0.000 svr-rbf-xl:0.087 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.2371, kl_div=0.0000
    Epoch 1: policy_loss=-0.0212, value_loss=0.9696, entropy=0.2396, kl_div=-0.2841
  Round 3/5: Mean predicted reward = 10.044
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.261 gb-tuned-l:0.129 gb-tuned-xl:0.166 mlp-adaptive-xl:0.357 mlp-l:0.000 svr-rbf-xl:0.087 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.2481, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0893
  Round 4/5: Mean predicted reward = 10.300
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.261 gb-tuned-l:0.129 gb-tuned-xl:0.166 mlp-adaptive-xl:0.357 mlp-l:0.000 svr-rbf-xl:0.087 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9702, entropy=0.2323, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3191
  Round 5/5: Mean predicted reward = 10.626

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 61 Results ---
  Mean Oracle Reward: 10.712
  Min Oracle Reward: 4.502
  Max Oracle Reward: 13.318
  Std Oracle Reward: 1.882
  Sequence Diversity: 0.969
  Models Used: 8
  Model R2 - Mean: 0.208, Max: 0.306, Count: 13
  Total Sequences Evaluated: 2002

======================================================================
EXPERIMENT ROUND 62/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2002
  Performance plateaued, reducing LR to 0.000100

--- Round 62 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  CATCAGGCTGCG
  CCAGCTTCAGGG
  TCCGGAGATCCG
  ATGGACCTCGGC
  CACGTGCATCGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.916
  Max reward: 13.147
  With intrinsic bonuses: 10.856

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9702, entropy=0.2331, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2320

=== Surrogate Model Training ===
Total samples: 2034

Training on 1952 samples (removed 82 outliers)
Reward range: [7.02, 13.42], mean: 10.32
  Created 13 candidate models for data size 1952
Current R2 threshold: 0.22000000000000003
  rf-tuned-l: R2 = 0.248 (std: 0.099)
  rf-tuned-xl: R2 = 0.238 (std: 0.108)
  gb-tuned-l: R2 = 0.257 (std: 0.090)
  gb-tuned-xl: R2 = 0.257 (std: 0.090)
  xgb-xl: R2 = 0.207 (std: 0.123)
  xgb-l: R2 = 0.207 (std: 0.123)
  mlp-adaptive-xl: R2 = 0.248 (std: 0.107)
  mlp-l: R2 = 0.246 (std: 0.067)
  svr-rbf-xl: R2 = 0.308 (std: 0.087)
  svr-poly-l: R2 = 0.308 (std: 0.087)
  knn-tuned-sqrt: R2 = 0.126 (std: 0.131)
  knn-tuned-l: R2 = 0.126 (std: 0.131)
  ridge: R2 = -0.017 (std: 0.135)

Model-based training with 8 models
Best R2: 0.308, Mean R2: 0.212
Running 5 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.651 gb-tuned-l:0.000 gb-tuned-xl:0.079 mlp-adaptive-xl:0.018 mlp-l:0.094 svr-rbf-xl:0.158 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.2234, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1224
  Round 1/5: Mean predicted reward = 9.534
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.651 gb-tuned-l:0.000 gb-tuned-xl:0.079 mlp-adaptive-xl:0.018 mlp-l:0.094 svr-rbf-xl:0.158 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.2103, kl_div=0.0000
    Epoch 1: policy_loss=-0.0201, value_loss=0.9686, entropy=0.2102, kl_div=0.0011
  Round 2/5: Mean predicted reward = 9.743
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.651 gb-tuned-l:0.000 gb-tuned-xl:0.079 mlp-adaptive-xl:0.018 mlp-l:0.094 svr-rbf-xl:0.158 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2139, kl_div=0.0000
    Epoch 1: policy_loss=0.0425, value_loss=0.9690, entropy=0.2163, kl_div=-0.2650
  Round 3/5: Mean predicted reward = 10.044
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.651 gb-tuned-l:0.000 gb-tuned-xl:0.079 mlp-adaptive-xl:0.018 mlp-l:0.094 svr-rbf-xl:0.158 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.2370, kl_div=0.0000
    Epoch 1: policy_loss=-0.0266, value_loss=0.9699, entropy=0.2376, kl_div=-0.0665
  Round 4/5: Mean predicted reward = 10.096
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.651 gb-tuned-l:0.000 gb-tuned-xl:0.079 mlp-adaptive-xl:0.018 mlp-l:0.094 svr-rbf-xl:0.158 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.2223, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1592
  Round 5/5: Mean predicted reward = 10.456

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 62 Results ---
  Mean Oracle Reward: 10.944
  Min Oracle Reward: 8.252
  Max Oracle Reward: 13.077
  Std Oracle Reward: 1.253
  Sequence Diversity: 0.969
  Models Used: 8
  Model R2 - Mean: 0.212, Max: 0.308, Count: 13
  Total Sequences Evaluated: 2034

======================================================================
EXPERIMENT ROUND 63/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2034
  Performance plateaued, reducing LR to 0.000055

--- Round 63 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  TCGCTGGCAACG
  CACTGTCACGGG
  TCCGCCGAGGAT
  GCGCCGCAATGT
  GGGTGCCTACCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.634
  Max reward: 13.381
  With intrinsic bonuses: 10.581

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.2481, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1036

=== Surrogate Model Training ===
Total samples: 2066

Training on 1984 samples (removed 82 outliers)
Reward range: [7.02, 13.54], mean: 10.33
  Created 13 candidate models for data size 1984
Current R2 threshold: 0.23000000000000004
  rf-tuned-l: R2 = 0.245 (std: 0.100)
  rf-tuned-xl: R2 = 0.243 (std: 0.097)
  gb-tuned-l: R2 = 0.271 (std: 0.091)
  gb-tuned-xl: R2 = 0.271 (std: 0.091)
  xgb-xl: R2 = 0.224 (std: 0.120)
  xgb-l: R2 = 0.224 (std: 0.120)
  mlp-adaptive-xl: R2 = 0.226 (std: 0.102)
  mlp-l: R2 = 0.240 (std: 0.099)
  svr-rbf-xl: R2 = 0.314 (std: 0.083)
  svr-poly-l: R2 = 0.314 (std: 0.083)
  knn-tuned-sqrt: R2 = 0.130 (std: 0.126)
  knn-tuned-l: R2 = 0.130 (std: 0.126)
  ridge: R2 = -0.023 (std: 0.144)

Model-based training with 7 models
Best R2: 0.314, Mean R2: 0.216
Running 5 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.410 gb-tuned-l:0.022 gb-tuned-xl:0.046 mlp-l:0.000 svr-rbf-xl:0.347 svr-poly-l:0.175
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.2279, kl_div=0.0000
    Epoch 1: policy_loss=0.0059, value_loss=0.9695, entropy=0.2270, kl_div=0.0369
  Round 1/5: Mean predicted reward = 9.517
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.410 gb-tuned-l:0.022 gb-tuned-xl:0.046 mlp-l:0.000 svr-rbf-xl:0.347 svr-poly-l:0.175
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.2184, kl_div=0.0000
    Epoch 1: policy_loss=-0.0369, value_loss=0.9691, entropy=0.2193, kl_div=-0.0788
  Round 2/5: Mean predicted reward = 9.890
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.410 gb-tuned-l:0.022 gb-tuned-xl:0.046 mlp-l:0.000 svr-rbf-xl:0.347 svr-poly-l:0.175
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2086, kl_div=0.0000
    Epoch 1: policy_loss=-0.0182, value_loss=0.9687, entropy=0.2102, kl_div=-0.1729
  Round 3/5: Mean predicted reward = 10.092
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.410 gb-tuned-l:0.022 gb-tuned-xl:0.046 mlp-l:0.000 svr-rbf-xl:0.347 svr-poly-l:0.175
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.2252, kl_div=0.0000
    Epoch 1: policy_loss=-0.0148, value_loss=0.9699, entropy=0.2261, kl_div=-0.0559
  Round 4/5: Mean predicted reward = 10.208
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.410 gb-tuned-l:0.022 gb-tuned-xl:0.046 mlp-l:0.000 svr-rbf-xl:0.347 svr-poly-l:0.175
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2253, kl_div=0.0000
    Epoch 1: policy_loss=-0.0136, value_loss=0.9690, entropy=0.2253, kl_div=-0.0255
  Round 5/5: Mean predicted reward = 10.484

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 63 Results ---
  Mean Oracle Reward: 10.543
  Min Oracle Reward: 5.438
  Max Oracle Reward: 13.204
  Std Oracle Reward: 1.789
  Sequence Diversity: 0.969
  Models Used: 7
  Model R2 - Mean: 0.216, Max: 0.314, Count: 13
  Total Sequences Evaluated: 2066

======================================================================
EXPERIMENT ROUND 64/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2066

--- Round 64 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  TTCACGGCACGG
  GCACGTGTCCGA
  GGTGTCAGCCCA
  GTCCGTCGCAAG
  CTGCGAGCCGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.953
  Max reward: 13.306
  With intrinsic bonuses: 10.974

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.2541, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0776

=== Surrogate Model Training ===
Total samples: 2098

Training on 2014 samples (removed 84 outliers)
Reward range: [7.03, 13.54], mean: 10.34
  Created 13 candidate models for data size 2014
Current R2 threshold: 0.24000000000000005
  rf-tuned-l: R2 = 0.252 (std: 0.105)
  rf-tuned-xl: R2 = 0.252 (std: 0.105)
  gb-tuned-l: R2 = 0.273 (std: 0.085)
  gb-tuned-xl: R2 = 0.273 (std: 0.085)
  xgb-xl: R2 = 0.220 (std: 0.119)
  xgb-l: R2 = 0.220 (std: 0.119)
  mlp-adaptive-xl: R2 = 0.261 (std: 0.073)
  mlp-l: R2 = 0.257 (std: 0.092)
  svr-rbf-xl: R2 = 0.318 (std: 0.087)
  svr-poly-l: R2 = 0.318 (std: 0.087)
  knn-tuned-sqrt: R2 = 0.132 (std: 0.126)
  knn-tuned-l: R2 = 0.132 (std: 0.126)
  ridge: R2 = -0.035 (std: 0.147)

Model-based training with 8 models
Best R2: 0.318, Mean R2: 0.221
Running 5 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.012 rf-tuned-xl:0.789 gb-tuned-l:0.000 gb-tuned-xl:0.000 mlp-adaptive-xl:0.000 mlp-l:0.021 svr-rbf-xl:0.120 svr-poly-l:0.058
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2485, kl_div=0.0000
    Epoch 1: policy_loss=-0.0024, value_loss=0.9689, entropy=0.2485, kl_div=0.0160
  Round 1/5: Mean predicted reward = 9.391
    Using ridge regression weights
    Model weights: rf-tuned-l:0.012 rf-tuned-xl:0.789 gb-tuned-l:0.000 gb-tuned-xl:0.000 mlp-adaptive-xl:0.000 mlp-l:0.021 svr-rbf-xl:0.120 svr-poly-l:0.058
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2181, kl_div=0.0000
    Epoch 1: policy_loss=-0.0440, value_loss=0.9687, entropy=0.2193, kl_div=-0.0498
  Round 2/5: Mean predicted reward = 9.647
    Using ridge regression weights
    Model weights: rf-tuned-l:0.012 rf-tuned-xl:0.789 gb-tuned-l:0.000 gb-tuned-xl:0.000 mlp-adaptive-xl:0.000 mlp-l:0.021 svr-rbf-xl:0.120 svr-poly-l:0.058
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2291, kl_div=0.0000
    Epoch 1: policy_loss=-0.0204, value_loss=0.9689, entropy=0.2316, kl_div=-0.1458
  Round 3/5: Mean predicted reward = 9.889
    Using ridge regression weights
    Model weights: rf-tuned-l:0.012 rf-tuned-xl:0.789 gb-tuned-l:0.000 gb-tuned-xl:0.000 mlp-adaptive-xl:0.000 mlp-l:0.021 svr-rbf-xl:0.120 svr-poly-l:0.058
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.2403, kl_div=0.0000
    Epoch 1: policy_loss=-0.0045, value_loss=0.9694, entropy=0.2412, kl_div=-0.0697
  Round 4/5: Mean predicted reward = 10.428
    Using ridge regression weights
    Model weights: rf-tuned-l:0.012 rf-tuned-xl:0.789 gb-tuned-l:0.000 gb-tuned-xl:0.000 mlp-adaptive-xl:0.000 mlp-l:0.021 svr-rbf-xl:0.120 svr-poly-l:0.058
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2354, kl_div=0.0000
    Epoch 1: policy_loss=-0.0147, value_loss=0.9690, entropy=0.2346, kl_div=0.0343
  Round 5/5: Mean predicted reward = 10.204

  === Progress Analysis ===
  Status: NORMAL

--- Round 64 Results ---
  Mean Oracle Reward: 10.938
  Min Oracle Reward: 7.406
  Max Oracle Reward: 13.280
  Std Oracle Reward: 1.219
  Sequence Diversity: 0.969
  Models Used: 8
  Model R2 - Mean: 0.221, Max: 0.318, Count: 13
  Total Sequences Evaluated: 2098

======================================================================
EXPERIMENT ROUND 65/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2098

--- Round 65 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.875) ---
  CACGGGATTGCC
  GAGGATCCACGT
  CTGTGGCAGACC
  CCCTGGGACAGT
  GGCAATGTCGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 11.006
  Max reward: 14.039
  With intrinsic bonuses: 11.048

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9700, entropy=0.2624, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7184

=== Surrogate Model Training ===
Total samples: 2130

Training on 2047 samples (removed 83 outliers)
Reward range: [7.02, 13.55], mean: 10.35
  Created 13 candidate models for data size 2047
Current R2 threshold: 0.25000000000000006
  rf-tuned-l: R2 = 0.281 (std: 0.110)
  rf-tuned-xl: R2 = 0.286 (std: 0.108)
  gb-tuned-l: R2 = 0.274 (std: 0.101)
  gb-tuned-xl: R2 = 0.274 (std: 0.101)
  xgb-xl: R2 = 0.270 (std: 0.133)
  xgb-l: R2 = 0.270 (std: 0.133)
  mlp-adaptive-xl: R2 = 0.299 (std: 0.093)
  mlp-l: R2 = 0.286 (std: 0.102)
  svr-rbf-xl: R2 = 0.340 (std: 0.105)
  svr-poly-l: R2 = 0.340 (std: 0.105)
  knn-tuned-sqrt: R2 = 0.160 (std: 0.140)
  knn-tuned-l: R2 = 0.160 (std: 0.140)
  ridge: R2 = -0.041 (std: 0.155)

Model-based training with 10 models
Best R2: 0.340, Mean R2: 0.246
Running 5 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.046 gb-tuned-l:0.000 gb-tuned-xl:0.007 xgb-xl:0.353 xgb-l:0.274 mlp-adaptive-xl:0.000 mlp-l:0.137 svr-rbf-xl:0.182 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.2358, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3994
  Round 1/5: Mean predicted reward = 9.422
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.046 gb-tuned-l:0.000 gb-tuned-xl:0.007 xgb-xl:0.353 xgb-l:0.274 mlp-adaptive-xl:0.000 mlp-l:0.137 svr-rbf-xl:0.182 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.2109, kl_div=0.0000
    Epoch 1: policy_loss=-0.0148, value_loss=0.9682, entropy=0.2082, kl_div=0.0011
  Round 2/5: Mean predicted reward = 9.975
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.046 gb-tuned-l:0.000 gb-tuned-xl:0.007 xgb-xl:0.353 xgb-l:0.274 mlp-adaptive-xl:0.000 mlp-l:0.137 svr-rbf-xl:0.182 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.1940, kl_div=0.0000
    Epoch 1: policy_loss=0.3144, value_loss=0.9689, entropy=0.2037, kl_div=-0.5889
  Round 3/5: Mean predicted reward = 10.015
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.046 gb-tuned-l:0.000 gb-tuned-xl:0.007 xgb-xl:0.353 xgb-l:0.274 mlp-adaptive-xl:0.000 mlp-l:0.137 svr-rbf-xl:0.182 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2434, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1396
  Round 4/5: Mean predicted reward = 10.255
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.046 gb-tuned-l:0.000 gb-tuned-xl:0.007 xgb-xl:0.353 xgb-l:0.274 mlp-adaptive-xl:0.000 mlp-l:0.137 svr-rbf-xl:0.182 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9685, entropy=0.2297, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5090
  Round 5/5: Mean predicted reward = 10.450

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 65 Results ---
  Mean Oracle Reward: 11.092
  Min Oracle Reward: 5.814
  Max Oracle Reward: 13.881
  Std Oracle Reward: 1.681
  Sequence Diversity: 0.875
  Models Used: 10
  Model R2 - Mean: 0.246, Max: 0.340, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 2130

======================================================================
EXPERIMENT ROUND 66/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2130
  Consistent improvement, increasing LR to 0.000327

--- Round 66 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  ATCCAGCGGGCT
  TCTGAGAGCCCG
  TTCGAGCCCGAG
  ACCAGTGCGATG
  CCGAGAGGCTTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.616
  Max reward: 13.635
  With intrinsic bonuses: 10.633

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.2399, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5672

=== Surrogate Model Training ===
Total samples: 2162

Training on 2078 samples (removed 84 outliers)
Reward range: [7.02, 13.55], mean: 10.36
  Created 13 candidate models for data size 2078
Current R2 threshold: 0.26000000000000006
  rf-tuned-l: R2 = 0.280 (std: 0.122)
  rf-tuned-xl: R2 = 0.284 (std: 0.123)
  gb-tuned-l: R2 = 0.286 (std: 0.103)
  gb-tuned-xl: R2 = 0.286 (std: 0.103)
  xgb-xl: R2 = 0.273 (std: 0.163)
  xgb-l: R2 = 0.273 (std: 0.163)
  mlp-adaptive-xl: R2 = 0.282 (std: 0.095)
  mlp-l: R2 = 0.308 (std: 0.103)
  svr-rbf-xl: R2 = 0.350 (std: 0.112)
  svr-poly-l: R2 = 0.350 (std: 0.112)
  knn-tuned-sqrt: R2 = 0.167 (std: 0.147)
  knn-tuned-l: R2 = 0.167 (std: 0.147)
  ridge: R2 = -0.045 (std: 0.161)

Model-based training with 10 models
Best R2: 0.350, Mean R2: 0.251
Running 5 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.023 gb-tuned-xl:0.175 xgb-xl:0.152 xgb-l:0.298 mlp-adaptive-xl:0.081 mlp-l:0.000 svr-rbf-xl:0.269 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.2230, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1352
  Round 1/5: Mean predicted reward = 9.299
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.023 gb-tuned-xl:0.175 xgb-xl:0.152 xgb-l:0.298 mlp-adaptive-xl:0.081 mlp-l:0.000 svr-rbf-xl:0.269 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.2518, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2154
  Round 2/5: Mean predicted reward = 9.905
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.023 gb-tuned-xl:0.175 xgb-xl:0.152 xgb-l:0.298 mlp-adaptive-xl:0.081 mlp-l:0.000 svr-rbf-xl:0.269 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.2208, kl_div=0.0000
    Epoch 1: policy_loss=0.1970, value_loss=0.9684, entropy=0.2105, kl_div=-0.0728
  Round 3/5: Mean predicted reward = 10.082
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.023 gb-tuned-xl:0.175 xgb-xl:0.152 xgb-l:0.298 mlp-adaptive-xl:0.081 mlp-l:0.000 svr-rbf-xl:0.269 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.2222, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2826
  Round 4/5: Mean predicted reward = 10.191
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.023 gb-tuned-xl:0.175 xgb-xl:0.152 xgb-l:0.298 mlp-adaptive-xl:0.081 mlp-l:0.000 svr-rbf-xl:0.269 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9695, entropy=0.2456, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5440
  Round 5/5: Mean predicted reward = 10.543

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 66 Results ---
  Mean Oracle Reward: 10.622
  Min Oracle Reward: 1.334
  Max Oracle Reward: 13.294
  Std Oracle Reward: 2.022
  Sequence Diversity: 0.969
  Models Used: 10
  Model R2 - Mean: 0.251, Max: 0.350, Count: 13
  Total Sequences Evaluated: 2162

======================================================================
EXPERIMENT ROUND 67/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2162

--- Round 67 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  CCAGCCTGGTAG
  GCCGCTAGGATC
  GGCACATCTGCG
  CAATGGCGCCTG
  CGGACCGATCTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.282
  Max reward: 11.670
  With intrinsic bonuses: 10.238

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.2205, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3517

=== Surrogate Model Training ===
Total samples: 2194

Training on 2110 samples (removed 84 outliers)
Reward range: [7.02, 13.55], mean: 10.36
  Created 13 candidate models for data size 2110
Current R2 threshold: 0.2700000000000001
  rf-tuned-l: R2 = 0.288 (std: 0.128)
  rf-tuned-xl: R2 = 0.294 (std: 0.123)
  gb-tuned-l: R2 = 0.283 (std: 0.106)
  gb-tuned-xl: R2 = 0.283 (std: 0.106)
  xgb-xl: R2 = 0.279 (std: 0.155)
  xgb-l: R2 = 0.279 (std: 0.155)
  mlp-adaptive-xl: R2 = 0.295 (std: 0.113)
  mlp-l: R2 = 0.298 (std: 0.105)
  svr-rbf-xl: R2 = 0.351 (std: 0.119)
  svr-poly-l: R2 = 0.351 (std: 0.119)
  knn-tuned-sqrt: R2 = 0.183 (std: 0.149)
  knn-tuned-l: R2 = 0.183 (std: 0.149)
  ridge: R2 = -0.042 (std: 0.158)

Model-based training with 10 models
Best R2: 0.351, Mean R2: 0.256
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:1.000 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.2418, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2876
  Round 1/5: Mean predicted reward = 10.066
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:1.000 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.2251, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0581
  Round 2/5: Mean predicted reward = 10.126
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:1.000 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2575, kl_div=0.0000
    Epoch 1: policy_loss=-0.0436, value_loss=0.9687, entropy=0.2587, kl_div=-0.1167
  Round 3/5: Mean predicted reward = 10.130
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:1.000 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2207, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1144
  Round 4/5: Mean predicted reward = 9.995
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:1.000 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.2102, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1477
  Round 5/5: Mean predicted reward = 10.449

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 67 Results ---
  Mean Oracle Reward: 10.271
  Min Oracle Reward: 8.457
  Max Oracle Reward: 11.918
  Std Oracle Reward: 0.788
  Sequence Diversity: 0.969
  Models Used: 10
  Model R2 - Mean: 0.256, Max: 0.351, Count: 13
  Total Sequences Evaluated: 2194

======================================================================
EXPERIMENT ROUND 68/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2194

--- Round 68 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TAGCGGCCCAGT
  GCTCGGGCCATA
  GCTCGCTCGGAA
  AGGCTGACACGT
  CCTCGAGCGAGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.723
  Max reward: 12.723
  With intrinsic bonuses: 10.750

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.2438, kl_div=0.0000
    Epoch 1: policy_loss=-0.0498, value_loss=0.9690, entropy=0.2455, kl_div=-0.0730

=== Surrogate Model Training ===
Total samples: 2226

Training on 2139 samples (removed 87 outliers)
Reward range: [7.04, 13.55], mean: 10.37
  Created 13 candidate models for data size 2139
Current R2 threshold: 0.27999999999999997
  rf-tuned-l: R2 = 0.296 (std: 0.128)
  rf-tuned-xl: R2 = 0.290 (std: 0.128)
  gb-tuned-l: R2 = 0.276 (std: 0.100)
  gb-tuned-xl: R2 = 0.276 (std: 0.100)
  xgb-xl: R2 = 0.292 (std: 0.131)
  xgb-l: R2 = 0.292 (std: 0.131)
  mlp-adaptive-xl: R2 = 0.290 (std: 0.109)
  mlp-l: R2 = 0.297 (std: 0.113)
  svr-rbf-xl: R2 = 0.346 (std: 0.119)
  svr-poly-l: R2 = 0.346 (std: 0.119)
  knn-tuned-sqrt: R2 = 0.182 (std: 0.154)
  knn-tuned-l: R2 = 0.182 (std: 0.154)
  ridge: R2 = -0.047 (std: 0.147)

Model-based training with 8 models
Best R2: 0.346, Mean R2: 0.255
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.203 xgb-xl:0.797 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2408, kl_div=0.0000
    Epoch 1: policy_loss=-0.0410, value_loss=0.9689, entropy=0.2429, kl_div=-0.1335
  Round 1/5: Mean predicted reward = 9.943
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.203 xgb-xl:0.797 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.1938, kl_div=0.0000
    Epoch 1: policy_loss=-0.0384, value_loss=0.9686, entropy=0.1946, kl_div=-0.1110
  Round 2/5: Mean predicted reward = 9.996
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.203 xgb-xl:0.797 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.2145, kl_div=0.0000
    Epoch 1: policy_loss=-0.0286, value_loss=0.9692, entropy=0.2150, kl_div=0.0242
  Round 3/5: Mean predicted reward = 10.069
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.203 xgb-xl:0.797 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.2111, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1293
  Round 4/5: Mean predicted reward = 10.107
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.203 xgb-xl:0.797 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9699, entropy=0.2110, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1509
  Round 5/5: Mean predicted reward = 10.236

  === Progress Analysis ===
  Status: NORMAL

--- Round 68 Results ---
  Mean Oracle Reward: 10.746
  Min Oracle Reward: 8.417
  Max Oracle Reward: 13.056
  Std Oracle Reward: 1.021
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: 0.255, Max: 0.346, Count: 13
  Total Sequences Evaluated: 2226

======================================================================
EXPERIMENT ROUND 69/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2226

--- Round 69 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  CAGTGCCGCGTA
  GGTCACCCGATG
  GCCGCGTATCGA
  GCGTGCACTGCA
  TGCCGCAACGGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.388
  Max reward: 13.359
  With intrinsic bonuses: 10.400

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.2383, kl_div=0.0000
    Epoch 1: policy_loss=-0.0270, value_loss=0.9693, entropy=0.2383, kl_div=-0.0286

=== Surrogate Model Training ===
Total samples: 2258

Training on 2168 samples (removed 90 outliers)
Reward range: [7.06, 13.55], mean: 10.38
  Created 13 candidate models for data size 2168
Current R2 threshold: 0.29
  rf-tuned-l: R2 = 0.291 (std: 0.128)
  rf-tuned-xl: R2 = 0.301 (std: 0.129)
  gb-tuned-l: R2 = 0.280 (std: 0.095)
  gb-tuned-xl: R2 = 0.280 (std: 0.095)
  xgb-xl: R2 = 0.298 (std: 0.165)
  xgb-l: R2 = 0.298 (std: 0.165)
  mlp-adaptive-xl: R2 = 0.297 (std: 0.125)
  mlp-l: R2 = 0.286 (std: 0.117)
  svr-rbf-xl: R2 = 0.349 (std: 0.128)
  svr-poly-l: R2 = 0.349 (std: 0.128)
  knn-tuned-sqrt: R2 = 0.184 (std: 0.161)
  knn-tuned-l: R2 = 0.184 (std: 0.161)
  ridge: R2 = -0.051 (std: 0.150)

Model-based training with 7 models
Best R2: 0.349, Mean R2: 0.257
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 xgb-xl:1.000 xgb-l:0.000 mlp-adaptive-xl:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.2249, kl_div=0.0000
    Epoch 1: policy_loss=-0.0329, value_loss=0.9686, entropy=0.2248, kl_div=-0.0485
  Round 1/5: Mean predicted reward = 9.414
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 xgb-xl:1.000 xgb-l:0.000 mlp-adaptive-xl:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.2257, kl_div=0.0000
    Epoch 1: policy_loss=-0.0228, value_loss=0.9696, entropy=0.2270, kl_div=-0.1385
  Round 2/5: Mean predicted reward = 10.177
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 xgb-xl:1.000 xgb-l:0.000 mlp-adaptive-xl:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.2107, kl_div=0.0000
    Epoch 1: policy_loss=-0.0390, value_loss=0.9684, entropy=0.2109, kl_div=-0.0941
  Round 3/5: Mean predicted reward = 10.156
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 xgb-xl:1.000 xgb-l:0.000 mlp-adaptive-xl:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2163, kl_div=0.0000
    Epoch 1: policy_loss=-0.0170, value_loss=0.9689, entropy=0.2166, kl_div=-0.0191
  Round 4/5: Mean predicted reward = 10.404
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 xgb-xl:1.000 xgb-l:0.000 mlp-adaptive-xl:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.2424, kl_div=0.0000
    Epoch 1: policy_loss=-0.0089, value_loss=0.9694, entropy=0.2420, kl_div=0.0214
  Round 5/5: Mean predicted reward = 10.401

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 69 Results ---
  Mean Oracle Reward: 10.431
  Min Oracle Reward: 5.307
  Max Oracle Reward: 13.286
  Std Oracle Reward: 1.574
  Sequence Diversity: 0.969
  Models Used: 7
  Model R2 - Mean: 0.257, Max: 0.349, Count: 13
  Total Sequences Evaluated: 2258

======================================================================
EXPERIMENT ROUND 70/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2258

--- Round 70 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  TCCGACAGTGGC
  ACCGATGCGCGT
  TGTACAGCCGCG
  GTCCTGAGGCAC
  CCTCCATAGGGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.288
  Max reward: 13.331
  With intrinsic bonuses: 10.256

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.2161, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0975

=== Surrogate Model Training ===
Total samples: 2290

Training on 2198 samples (removed 92 outliers)
Reward range: [7.07, 13.55], mean: 10.38
  Created 13 candidate models for data size 2198
Current R2 threshold: 0.3
  rf-tuned-l: R2 = 0.309 (std: 0.128)
  rf-tuned-xl: R2 = 0.305 (std: 0.138)
  gb-tuned-l: R2 = 0.275 (std: 0.095)
  gb-tuned-xl: R2 = 0.275 (std: 0.095)
  xgb-xl: R2 = 0.312 (std: 0.161)
  xgb-l: R2 = 0.312 (std: 0.161)
  mlp-adaptive-xl: R2 = 0.303 (std: 0.122)
  mlp-l: R2 = 0.307 (std: 0.109)
  svr-rbf-xl: R2 = 0.340 (std: 0.125)
  svr-poly-l: R2 = 0.340 (std: 0.125)
  knn-tuned-sqrt: R2 = 0.184 (std: 0.158)
  knn-tuned-l: R2 = 0.184 (std: 0.158)
  ridge: R2 = -0.061 (std: 0.148)

Model-based training with 8 models
Best R2: 0.340, Mean R2: 0.260
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 xgb-xl:0.000 xgb-l:0.852 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.148 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2156, kl_div=0.0000
    Epoch 1: policy_loss=0.1853, value_loss=0.9689, entropy=0.2171, kl_div=-0.3030
  Round 1/5: Mean predicted reward = 9.354
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 xgb-xl:0.000 xgb-l:0.852 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.148 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.2172, kl_div=0.0000
    Epoch 1: policy_loss=0.0388, value_loss=0.9688, entropy=0.2215, kl_div=-0.2168
  Round 2/5: Mean predicted reward = 10.065
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 xgb-xl:0.000 xgb-l:0.852 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.148 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.2338, kl_div=0.0000
    Epoch 1: policy_loss=-0.0512, value_loss=0.9686, entropy=0.2362, kl_div=-0.0854
  Round 3/5: Mean predicted reward = 9.865
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 xgb-xl:0.000 xgb-l:0.852 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.148 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9695, entropy=0.2501, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2371
  Round 4/5: Mean predicted reward = 10.203
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 xgb-xl:0.000 xgb-l:0.852 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.148 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.2362, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0944
  Round 5/5: Mean predicted reward = 10.436

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 70 Results ---
  Mean Oracle Reward: 10.278
  Min Oracle Reward: 4.624
  Max Oracle Reward: 13.337
  Std Oracle Reward: 1.605
  Sequence Diversity: 0.969
  Models Used: 8
  Model R2 - Mean: 0.260, Max: 0.340, Count: 13
  Total Sequences Evaluated: 2290

======================================================================
EXPERIMENT ROUND 71/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2290

--- Round 71 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.938) ---
  CAGCTAGTGCGC
  TCGCATCAGGGC
  TCCCGGCGAGAT
  GTGCCAGCTGAC
  CCTGGGCGCTAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.948
  Max reward: 11.680
  With intrinsic bonuses: 9.920

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.2204, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3477

=== Surrogate Model Training ===
Total samples: 2322

Training on 2230 samples (removed 92 outliers)
Reward range: [7.04, 13.55], mean: 10.37
  Created 13 candidate models for data size 2230
Current R2 threshold: 0.31
  rf-tuned-l: R2 = 0.332 (std: 0.139)
  rf-tuned-xl: R2 = 0.320 (std: 0.139)
  gb-tuned-l: R2 = 0.286 (std: 0.095)
  gb-tuned-xl: R2 = 0.286 (std: 0.095)
  xgb-xl: R2 = 0.317 (std: 0.157)
  xgb-l: R2 = 0.317 (std: 0.157)
  mlp-adaptive-xl: R2 = 0.316 (std: 0.134)
  mlp-l: R2 = 0.297 (std: 0.138)
  svr-rbf-xl: R2 = 0.348 (std: 0.127)
  svr-poly-l: R2 = 0.348 (std: 0.127)
  knn-tuned-sqrt: R2 = 0.191 (std: 0.160)
  knn-tuned-l: R2 = 0.191 (std: 0.160)
  ridge: R2 = -0.056 (std: 0.136)

Model-based training with 7 models
Best R2: 0.348, Mean R2: 0.269
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.184 xgb-xl:0.816 xgb-l:0.000 mlp-adaptive-xl:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.1949, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1212
  Round 1/5: Mean predicted reward = 9.961
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.184 xgb-xl:0.816 xgb-l:0.000 mlp-adaptive-xl:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.2008, kl_div=0.0000
    Epoch 1: policy_loss=-0.0586, value_loss=0.9692, entropy=0.1972, kl_div=0.0012
  Round 2/5: Mean predicted reward = 10.112
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.184 xgb-xl:0.816 xgb-l:0.000 mlp-adaptive-xl:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.1935, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0886
  Round 3/5: Mean predicted reward = 10.002
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.184 xgb-xl:0.816 xgb-l:0.000 mlp-adaptive-xl:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.1735, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1749
  Round 4/5: Mean predicted reward = 10.408
    Using validation-optimized weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.184 xgb-xl:0.816 xgb-l:0.000 mlp-adaptive-xl:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.1971, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3676
  Round 5/5: Mean predicted reward = 10.391

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 71 Results ---
  Mean Oracle Reward: 9.922
  Min Oracle Reward: 5.104
  Max Oracle Reward: 11.686
  Std Oracle Reward: 1.626
  Sequence Diversity: 0.938
  Models Used: 7
  Model R2 - Mean: 0.269, Max: 0.348, Count: 13
  Total Sequences Evaluated: 2322

======================================================================
EXPERIMENT ROUND 72/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2322

--- Round 72 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.938) ---
  CATGTCACGGCG
  ACGAGCGTGACT
  AACCGTGCTGCG
  AGGGTCCCATCG
  GGTCAGATCCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.709
  Max reward: 12.672
  With intrinsic bonuses: 10.722

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2238, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1978

=== Surrogate Model Training ===
Total samples: 2354

Training on 2260 samples (removed 94 outliers)
Reward range: [7.07, 13.55], mean: 10.38
  Created 13 candidate models for data size 2260
Current R2 threshold: 0.32
  rf-tuned-l: R2 = 0.309 (std: 0.138)
  rf-tuned-xl: R2 = 0.312 (std: 0.136)
  gb-tuned-l: R2 = 0.270 (std: 0.096)
  gb-tuned-xl: R2 = 0.270 (std: 0.096)
  xgb-xl: R2 = 0.295 (std: 0.152)
  xgb-l: R2 = 0.295 (std: 0.152)
  mlp-adaptive-xl: R2 = 0.273 (std: 0.093)
  mlp-l: R2 = 0.292 (std: 0.125)
  svr-rbf-xl: R2 = 0.335 (std: 0.115)
  svr-poly-l: R2 = 0.335 (std: 0.115)
  knn-tuned-sqrt: R2 = 0.186 (std: 0.156)
  knn-tuned-l: R2 = 0.186 (std: 0.156)
  ridge: R2 = -0.059 (std: 0.135)

Model-based training with 2 models
Best R2: 0.335, Mean R2: 0.254
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.2128, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3144
  Round 1/5: Mean predicted reward = 9.562
    Using validation-optimized weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.2041, kl_div=0.0000
    Epoch 1: policy_loss=-0.0324, value_loss=0.9690, entropy=0.2049, kl_div=0.0070
  Round 2/5: Mean predicted reward = 9.914
    Using validation-optimized weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.2337, kl_div=0.0000
    Epoch 1: policy_loss=0.0912, value_loss=0.9691, entropy=0.2321, kl_div=-0.3624
  Round 3/5: Mean predicted reward = 10.408
    Using validation-optimized weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2070, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1050
  Round 4/5: Mean predicted reward = 10.026
    Using validation-optimized weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.1884, kl_div=0.0000
    Epoch 1: policy_loss=-0.0122, value_loss=0.9696, entropy=0.1923, kl_div=-0.0933
  Round 5/5: Mean predicted reward = 10.272

  === Progress Analysis ===
  Status: NORMAL

--- Round 72 Results ---
  Mean Oracle Reward: 10.693
  Min Oracle Reward: 8.054
  Max Oracle Reward: 12.756
  Std Oracle Reward: 0.935
  Sequence Diversity: 0.938
  Models Used: 2
  Model R2 - Mean: 0.254, Max: 0.335, Count: 13
  Total Sequences Evaluated: 2354

======================================================================
EXPERIMENT ROUND 73/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2354

--- Round 73 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  TCCACGGAGTGC
  CGTGTAAGGACC
  GTCGTCCCAAGG
  GTGTAACCCGCG
  GCACCAGGCTTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.418
  Max reward: 12.683
  With intrinsic bonuses: 10.419

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.2050, kl_div=0.0000
    Epoch 1: policy_loss=-0.0187, value_loss=0.9682, entropy=0.2059, kl_div=-0.1243

=== Surrogate Model Training ===
Total samples: 2386

Training on 2290 samples (removed 96 outliers)
Reward range: [7.09, 13.55], mean: 10.38
  Created 13 candidate models for data size 2290
Current R2 threshold: 0.33
  rf-tuned-l: R2 = 0.327 (std: 0.134)
  rf-tuned-xl: R2 = 0.321 (std: 0.130)
  gb-tuned-l: R2 = 0.270 (std: 0.098)
  gb-tuned-xl: R2 = 0.270 (std: 0.098)
  xgb-xl: R2 = 0.309 (std: 0.156)
  xgb-l: R2 = 0.309 (std: 0.156)
  mlp-adaptive-xl: R2 = 0.280 (std: 0.126)
  mlp-l: R2 = 0.309 (std: 0.130)
  svr-rbf-xl: R2 = 0.339 (std: 0.116)
  svr-poly-l: R2 = 0.339 (std: 0.116)
  knn-tuned-sqrt: R2 = 0.179 (std: 0.165)
  knn-tuned-l: R2 = 0.179 (std: 0.165)
  ridge: R2 = -0.058 (std: 0.135)

Model-based training with 2 models
Best R2: 0.339, Mean R2: 0.259
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2165, kl_div=0.0000
    Epoch 1: policy_loss=-0.0441, value_loss=0.9690, entropy=0.2169, kl_div=-0.0626
  Round 1/5: Mean predicted reward = 10.049
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2317, kl_div=0.0000
    Epoch 1: policy_loss=-0.0822, value_loss=0.9689, entropy=0.2339, kl_div=-0.0771
  Round 2/5: Mean predicted reward = 9.793
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.2161, kl_div=0.0000
    Epoch 1: policy_loss=0.0321, value_loss=0.9694, entropy=0.2207, kl_div=-0.0837
  Round 3/5: Mean predicted reward = 10.058
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.2289, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0616
  Round 4/5: Mean predicted reward = 10.194
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2664, kl_div=0.0000
    Epoch 1: policy_loss=-0.0466, value_loss=0.9690, entropy=0.2656, kl_div=0.0291
  Round 5/5: Mean predicted reward = 10.325

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 73 Results ---
  Mean Oracle Reward: 10.443
  Min Oracle Reward: 7.627
  Max Oracle Reward: 13.166
  Std Oracle Reward: 1.027
  Sequence Diversity: 0.969
  Models Used: 2
  Model R2 - Mean: 0.259, Max: 0.339, Count: 13
  Total Sequences Evaluated: 2386

======================================================================
EXPERIMENT ROUND 74/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2386

--- Round 74 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  CCGGCTAACGTG
  CTCAGGACCGTG
  CCTCCTGAAGGG
  GATGACTCCGGC
  TCCCTCAGGAGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.133
  Max reward: 12.206
  With intrinsic bonuses: 10.101

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.2268, kl_div=0.0000
    Epoch 1: policy_loss=-0.0229, value_loss=0.9692, entropy=0.2263, kl_div=0.0138

=== Surrogate Model Training ===
Total samples: 2418

Training on 2320 samples (removed 98 outliers)
Reward range: [7.09, 13.55], mean: 10.38
  Created 13 candidate models for data size 2320
Current R2 threshold: 0.34
  rf-tuned-l: R2 = 0.304 (std: 0.123)
  rf-tuned-xl: R2 = 0.311 (std: 0.124)
  gb-tuned-l: R2 = 0.270 (std: 0.081)
  gb-tuned-xl: R2 = 0.270 (std: 0.081)
  xgb-xl: R2 = 0.298 (std: 0.146)
  xgb-l: R2 = 0.298 (std: 0.146)
  mlp-adaptive-xl: R2 = 0.257 (std: 0.123)
  mlp-l: R2 = 0.298 (std: 0.104)
  svr-rbf-xl: R2 = 0.325 (std: 0.101)
  svr-poly-l: R2 = 0.325 (std: 0.101)
  knn-tuned-sqrt: R2 = 0.170 (std: 0.151)
  knn-tuned-l: R2 = 0.170 (std: 0.151)
  ridge: R2 = -0.059 (std: 0.126)
  Fallback: Using svr-rbf-xl with R2 = 0.325

Model-based training with 1 models
Best R2: 0.325, Mean R2: 0.249
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.2466, kl_div=0.0000
    Epoch 1: policy_loss=-0.0227, value_loss=0.9685, entropy=0.2462, kl_div=-0.0622
  Round 1/5: Mean predicted reward = 9.642
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.2462, kl_div=0.0000
    Epoch 1: policy_loss=-0.0388, value_loss=0.9684, entropy=0.2477, kl_div=-0.0527
  Round 2/5: Mean predicted reward = 10.008
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2310, kl_div=0.0000
    Epoch 1: policy_loss=-0.0258, value_loss=0.9689, entropy=0.2331, kl_div=-0.0714
  Round 3/5: Mean predicted reward = 10.139
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.2131, kl_div=0.0000
    Epoch 1: policy_loss=-0.0417, value_loss=0.9691, entropy=0.2151, kl_div=0.0209
  Round 4/5: Mean predicted reward = 10.046
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.2607, kl_div=0.0000
    Epoch 1: policy_loss=-0.0104, value_loss=0.9688, entropy=0.2614, kl_div=-0.0263
  Round 5/5: Mean predicted reward = 10.334

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 74 Results ---
  Mean Oracle Reward: 10.102
  Min Oracle Reward: 6.607
  Max Oracle Reward: 12.037
  Std Oracle Reward: 1.385
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.249, Max: 0.325, Count: 13
  Total Sequences Evaluated: 2418

======================================================================
EXPERIMENT ROUND 75/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2418

--- Round 75 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.938) ---
  TCCCGAATGCGG
  CGAGTCGTCCAG
  AAGCCTGGGCCT
  AGCTGGCACGCT
  CAAACCGTTGGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.524
  Max reward: 12.547
  With intrinsic bonuses: 10.551

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.2796, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1298

=== Surrogate Model Training ===
Total samples: 2450

Training on 2349 samples (removed 101 outliers)
Reward range: [7.11, 13.54], mean: 10.39
  Created 13 candidate models for data size 2349
Current R2 threshold: 0.35000000000000003
  rf-tuned-l: R2 = 0.300 (std: 0.119)
  rf-tuned-xl: R2 = 0.289 (std: 0.120)
  gb-tuned-l: R2 = 0.262 (std: 0.073)
  gb-tuned-xl: R2 = 0.262 (std: 0.073)
  xgb-xl: R2 = 0.278 (std: 0.139)
  xgb-l: R2 = 0.278 (std: 0.139)
  mlp-adaptive-xl: R2 = 0.276 (std: 0.124)
  mlp-l: R2 = 0.298 (std: 0.122)
  svr-rbf-xl: R2 = 0.318 (std: 0.090)
  svr-poly-l: R2 = 0.318 (std: 0.090)
  knn-tuned-sqrt: R2 = 0.149 (std: 0.141)
  knn-tuned-l: R2 = 0.149 (std: 0.141)
  ridge: R2 = -0.065 (std: 0.130)
  Fallback: Using svr-rbf-xl with R2 = 0.318

Model-based training with 1 models
Best R2: 0.318, Mean R2: 0.239
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.2212, kl_div=0.0000
    Epoch 1: policy_loss=0.1295, value_loss=0.9695, entropy=0.2264, kl_div=-0.1273
  Round 1/5: Mean predicted reward = 9.930
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.2317, kl_div=0.0000
    Epoch 1: policy_loss=-0.0241, value_loss=0.9695, entropy=0.2303, kl_div=0.0434
  Round 2/5: Mean predicted reward = 10.102
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.2584, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3038
  Round 3/5: Mean predicted reward = 10.423
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.2397, kl_div=0.0000
    Epoch 1: policy_loss=0.0019, value_loss=0.9691, entropy=0.2383, kl_div=-0.0310
  Round 4/5: Mean predicted reward = 10.319
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.2596, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1384
  Round 5/5: Mean predicted reward = 10.471

  === Progress Analysis ===
  Status: NORMAL

--- Round 75 Results ---
  Mean Oracle Reward: 10.552
  Min Oracle Reward: 7.541
  Max Oracle Reward: 12.608
  Std Oracle Reward: 1.258
  Sequence Diversity: 0.938
  Models Used: 1
  Model R2 - Mean: 0.239, Max: 0.318, Count: 13
  Total Sequences Evaluated: 2450

======================================================================
EXPERIMENT ROUND 76/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2450

--- Round 76 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.938) ---
  CGGCTTGGACCA
  GGCAGTCCCGAT
  ACAGACTGGTCG
  CCGATCGCAGGT
  TGGACGGCACCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.587
  Max reward: 12.321
  With intrinsic bonuses: 10.542

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2343, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4465

=== Surrogate Model Training ===
Total samples: 2482

Training on 2377 samples (removed 105 outliers)
Reward range: [7.15, 13.48], mean: 10.39
  Created 13 candidate models for data size 2377
Current R2 threshold: 0.36000000000000004
  rf-tuned-l: R2 = 0.277 (std: 0.100)
  rf-tuned-xl: R2 = 0.291 (std: 0.097)
  gb-tuned-l: R2 = 0.259 (std: 0.074)
  gb-tuned-xl: R2 = 0.259 (std: 0.074)
  xgb-xl: R2 = 0.287 (std: 0.099)
  xgb-l: R2 = 0.287 (std: 0.099)
  mlp-adaptive-xl: R2 = 0.277 (std: 0.090)
  mlp-l: R2 = 0.273 (std: 0.107)
  svr-rbf-xl: R2 = 0.313 (std: 0.078)
  svr-poly-l: R2 = 0.313 (std: 0.078)
  knn-tuned-sqrt: R2 = 0.155 (std: 0.125)
  knn-tuned-l: R2 = 0.155 (std: 0.125)
  ridge: R2 = -0.069 (std: 0.133)
  Fallback: Using svr-rbf-xl with R2 = 0.313

Model-based training with 1 models
Best R2: 0.313, Mean R2: 0.237
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.2517, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1460
  Round 1/5: Mean predicted reward = 10.016
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2200, kl_div=0.0000
    Epoch 1: policy_loss=0.2631, value_loss=0.9689, entropy=0.2251, kl_div=-0.5810
  Round 2/5: Mean predicted reward = 10.239
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.2246, kl_div=0.0000
    Epoch 1: policy_loss=0.0292, value_loss=0.9691, entropy=0.2246, kl_div=-0.2067
  Round 3/5: Mean predicted reward = 9.824
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.2242, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1422
  Round 4/5: Mean predicted reward = 9.908
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.2492, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4317
  Round 5/5: Mean predicted reward = 10.569

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 76 Results ---
  Mean Oracle Reward: 10.551
  Min Oracle Reward: 6.743
  Max Oracle Reward: 12.238
  Std Oracle Reward: 1.072
  Sequence Diversity: 0.938
  Models Used: 1
  Model R2 - Mean: 0.237, Max: 0.313, Count: 13
  Total Sequences Evaluated: 2482

======================================================================
EXPERIMENT ROUND 77/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2482
  Consistent improvement, increasing LR to 0.000240

--- Round 77 Configuration ---
Learning rate: 0.000240
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CAGCGTTGAGCC
  TCCCACGGGATG
  GACCGGACTCGT
  ACGTCCAGGGTC
  ACAGGGTGCCTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.168
  Max reward: 12.364
  With intrinsic bonuses: 10.161

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.2453, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4462

=== Surrogate Model Training ===
Total samples: 2514

Training on 2410 samples (removed 104 outliers)
Reward range: [7.12, 13.48], mean: 10.39
  Created 13 candidate models for data size 2410
Current R2 threshold: 0.37000000000000005
  rf-tuned-l: R2 = 0.284 (std: 0.097)
  rf-tuned-xl: R2 = 0.282 (std: 0.093)
  gb-tuned-l: R2 = 0.265 (std: 0.076)
  gb-tuned-xl: R2 = 0.265 (std: 0.076)
  xgb-xl: R2 = 0.267 (std: 0.104)
  xgb-l: R2 = 0.267 (std: 0.104)
  mlp-adaptive-xl: R2 = 0.278 (std: 0.095)
  mlp-l: R2 = 0.257 (std: 0.109)
  svr-rbf-xl: R2 = 0.320 (std: 0.078)
  svr-poly-l: R2 = 0.320 (std: 0.078)
  knn-tuned-sqrt: R2 = 0.164 (std: 0.127)
  knn-tuned-l: R2 = 0.164 (std: 0.127)
  ridge: R2 = -0.058 (std: 0.132)
  Fallback: Using svr-rbf-xl with R2 = 0.320

Model-based training with 1 models
Best R2: 0.320, Mean R2: 0.236
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.2245, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4774
  Round 1/5: Mean predicted reward = 10.014
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.2321, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2515
  Round 2/5: Mean predicted reward = 10.100
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2167, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1175
  Round 3/5: Mean predicted reward = 10.143
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.2127, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2090
  Round 4/5: Mean predicted reward = 10.010
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.2084, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3722
  Round 5/5: Mean predicted reward = 10.189

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 77 Results ---
  Mean Oracle Reward: 10.210
  Min Oracle Reward: 8.167
  Max Oracle Reward: 12.289
  Std Oracle Reward: 1.122
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.236, Max: 0.320, Count: 13
  Total Sequences Evaluated: 2514

======================================================================
EXPERIMENT ROUND 78/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2514

--- Round 78 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AGCCCGTTGGCA
  AAGGCGCTCGCT
  TCTGCCGGACGA
  CTAGCGCCTGAG
  CTATGGGGACCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.627
  Max reward: 12.420
  With intrinsic bonuses: 10.605

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9695, entropy=0.2342, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1874

=== Surrogate Model Training ===
Total samples: 2546

Training on 2440 samples (removed 106 outliers)
Reward range: [7.15, 13.48], mean: 10.39
  Created 13 candidate models for data size 2440
Current R2 threshold: 0.38000000000000006
  rf-tuned-l: R2 = 0.300 (std: 0.106)
  rf-tuned-xl: R2 = 0.298 (std: 0.110)
  gb-tuned-l: R2 = 0.278 (std: 0.087)
  gb-tuned-xl: R2 = 0.278 (std: 0.087)
  xgb-xl: R2 = 0.290 (std: 0.101)
  xgb-l: R2 = 0.290 (std: 0.101)
  mlp-adaptive-xl: R2 = 0.290 (std: 0.115)
  mlp-l: R2 = 0.289 (std: 0.101)
  svr-rbf-xl: R2 = 0.337 (std: 0.089)
  svr-poly-l: R2 = 0.337 (std: 0.089)
  knn-tuned-sqrt: R2 = 0.175 (std: 0.127)
  knn-tuned-l: R2 = 0.175 (std: 0.127)
  ridge: R2 = -0.042 (std: 0.134)
  Fallback: Using svr-rbf-xl with R2 = 0.337

Model-based training with 1 models
Best R2: 0.337, Mean R2: 0.253
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.2142, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0578
  Round 1/5: Mean predicted reward = 9.292
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.2133, kl_div=0.0000
    Epoch 1: policy_loss=-0.0846, value_loss=0.9690, entropy=0.2154, kl_div=-0.0016
  Round 2/5: Mean predicted reward = 9.913
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.2131, kl_div=0.0000
    Epoch 1: policy_loss=-0.0434, value_loss=0.9694, entropy=0.2145, kl_div=-0.0981
  Round 3/5: Mean predicted reward = 9.708
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.2402, kl_div=0.0000
    Epoch 1: policy_loss=-0.0289, value_loss=0.9688, entropy=0.2395, kl_div=-0.0383
  Round 4/5: Mean predicted reward = 10.255
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.2354, kl_div=0.0000
    Epoch 1: policy_loss=-0.0158, value_loss=0.9692, entropy=0.2359, kl_div=-0.0254
  Round 5/5: Mean predicted reward = 10.550

  === Progress Analysis ===
  Status: NORMAL

--- Round 78 Results ---
  Mean Oracle Reward: 10.666
  Min Oracle Reward: 7.148
  Max Oracle Reward: 12.238
  Std Oracle Reward: 1.033
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.253, Max: 0.337, Count: 13
  Total Sequences Evaluated: 2546

======================================================================
EXPERIMENT ROUND 79/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2546

--- Round 79 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.906) ---
  CGGCTCTACAGG
  GCTCTGGCAAGC
  CTGGGTGCACAC
  AGCGCGCTATCG
  GCACCGAGTCGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.452
  Max reward: 12.370
  With intrinsic bonuses: 10.432

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.2086, kl_div=0.0000
    Epoch 1: policy_loss=-0.0205, value_loss=0.9693, entropy=0.2089, kl_div=-0.0327

=== Surrogate Model Training ===
Total samples: 2578

Training on 2471 samples (removed 107 outliers)
Reward range: [7.15, 13.54], mean: 10.40
  Created 13 candidate models for data size 2471
Current R2 threshold: 0.39000000000000007
  rf-tuned-l: R2 = 0.298 (std: 0.105)
  rf-tuned-xl: R2 = 0.294 (std: 0.106)
  gb-tuned-l: R2 = 0.270 (std: 0.083)
  gb-tuned-xl: R2 = 0.270 (std: 0.083)
  xgb-xl: R2 = 0.279 (std: 0.113)
  xgb-l: R2 = 0.279 (std: 0.113)
  mlp-adaptive-xl: R2 = 0.298 (std: 0.111)
  mlp-l: R2 = 0.287 (std: 0.115)
  svr-rbf-xl: R2 = 0.339 (std: 0.086)
  svr-poly-l: R2 = 0.339 (std: 0.086)
  knn-tuned-sqrt: R2 = 0.169 (std: 0.124)
  knn-tuned-l: R2 = 0.169 (std: 0.124)
  ridge: R2 = -0.038 (std: 0.136)
  Fallback: Using svr-rbf-xl with R2 = 0.339

Model-based training with 1 models
Best R2: 0.339, Mean R2: 0.250
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.1981, kl_div=0.0000
    Epoch 1: policy_loss=-0.0744, value_loss=0.9687, entropy=0.1996, kl_div=-0.0964
  Round 1/5: Mean predicted reward = 9.547
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.2361, kl_div=0.0000
    Epoch 1: policy_loss=-0.0300, value_loss=0.9691, entropy=0.2373, kl_div=-0.0950
  Round 2/5: Mean predicted reward = 10.001
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2286, kl_div=0.0000
    Epoch 1: policy_loss=-0.0295, value_loss=0.9687, entropy=0.2309, kl_div=-0.1009
  Round 3/5: Mean predicted reward = 9.999
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2195, kl_div=0.0000
    Epoch 1: policy_loss=-0.0234, value_loss=0.9689, entropy=0.2212, kl_div=-0.1071
  Round 4/5: Mean predicted reward = 10.394
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.2571, kl_div=0.0000
    Epoch 1: policy_loss=-0.0118, value_loss=0.9691, entropy=0.2578, kl_div=-0.0001
  Round 5/5: Mean predicted reward = 10.261

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 79 Results ---
  Mean Oracle Reward: 10.453
  Min Oracle Reward: 6.822
  Max Oracle Reward: 12.434
  Std Oracle Reward: 1.293
  Sequence Diversity: 0.906
  Models Used: 1
  Model R2 - Mean: 0.250, Max: 0.339, Count: 13
  Total Sequences Evaluated: 2578

======================================================================
EXPERIMENT ROUND 80/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2578

--- Round 80 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.938) ---
  TCCGGCGACGAT
  GCCGGCGTATAC
  GTCCCTACGAGG
  ACTGCGCACTGG
  TGACCGCCGTGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.319
  Max reward: 12.579
  With intrinsic bonuses: 10.327

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.2599, kl_div=0.0000
    Epoch 1: policy_loss=0.0207, value_loss=0.9694, entropy=0.2683, kl_div=-0.3215

=== Surrogate Model Training ===
Total samples: 2610

Training on 2501 samples (removed 109 outliers)
Reward range: [7.15, 13.54], mean: 10.40
  Created 13 candidate models for data size 2501
Current R2 threshold: 0.4000000000000001
  rf-tuned-l: R2 = 0.286 (std: 0.115)
  rf-tuned-xl: R2 = 0.290 (std: 0.118)
  gb-tuned-l: R2 = 0.280 (std: 0.091)
  gb-tuned-xl: R2 = 0.280 (std: 0.091)
  xgb-xl: R2 = 0.289 (std: 0.108)
  xgb-l: R2 = 0.289 (std: 0.108)
  mlp-adaptive-xl: R2 = 0.260 (std: 0.100)
  mlp-l: R2 = 0.276 (std: 0.109)
  svr-rbf-xl: R2 = 0.341 (std: 0.088)
  svr-poly-l: R2 = 0.341 (std: 0.088)
  knn-tuned-sqrt: R2 = 0.157 (std: 0.123)
  knn-tuned-l: R2 = 0.157 (std: 0.123)
  ridge: R2 = -0.037 (std: 0.140)
  Fallback: Using svr-rbf-xl with R2 = 0.341

Model-based training with 1 models
Best R2: 0.341, Mean R2: 0.247
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2585, kl_div=0.0000
    Epoch 1: policy_loss=-0.0688, value_loss=0.9689, entropy=0.2639, kl_div=-0.3556
  Round 1/5: Mean predicted reward = 9.267
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2604, kl_div=0.0000
    Epoch 1: policy_loss=-0.0619, value_loss=0.9687, entropy=0.2669, kl_div=-0.1812
  Round 2/5: Mean predicted reward = 9.581
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.2456, kl_div=0.0000
    Epoch 1: policy_loss=0.6283, value_loss=0.9688, entropy=0.2496, kl_div=-0.5901
  Round 3/5: Mean predicted reward = 10.059
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2341, kl_div=0.0000
    Epoch 1: policy_loss=0.4707, value_loss=0.9690, entropy=0.2393, kl_div=-0.4631
  Round 4/5: Mean predicted reward = 10.204
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2543, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1288
  Round 5/5: Mean predicted reward = 10.417

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 80 Results ---
  Mean Oracle Reward: 10.351
  Min Oracle Reward: 6.082
  Max Oracle Reward: 12.429
  Std Oracle Reward: 1.493
  Sequence Diversity: 0.938
  Models Used: 1
  Model R2 - Mean: 0.247, Max: 0.341, Count: 13
  Total Sequences Evaluated: 2610

======================================================================
EXPERIMENT ROUND 81/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2610

--- Round 81 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCTCTGGCGAAC
  GCTACGTCACGG
  GCACACGTGCTG
  GGCGTGTCCACA
  ACCTGGACTCGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.299
  Max reward: 12.519
  With intrinsic bonuses: 10.301

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2202, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3352

=== Surrogate Model Training ===
Total samples: 2642

Training on 2529 samples (removed 113 outliers)
Reward range: [7.18, 13.48], mean: 10.40
  Created 13 candidate models for data size 2529
Current R2 threshold: 0.41
  rf-tuned-l: R2 = 0.284 (std: 0.116)
  rf-tuned-xl: R2 = 0.280 (std: 0.114)
  gb-tuned-l: R2 = 0.280 (std: 0.095)
  gb-tuned-xl: R2 = 0.280 (std: 0.095)
  xgb-xl: R2 = 0.275 (std: 0.112)
  xgb-l: R2 = 0.275 (std: 0.112)
  mlp-adaptive-xl: R2 = 0.265 (std: 0.116)
  mlp-l: R2 = 0.271 (std: 0.110)
  svr-rbf-xl: R2 = 0.340 (std: 0.091)
  svr-poly-l: R2 = 0.340 (std: 0.091)
  knn-tuned-sqrt: R2 = 0.146 (std: 0.121)
  knn-tuned-l: R2 = 0.146 (std: 0.121)
  ridge: R2 = -0.027 (std: 0.148)
  Fallback: Using svr-rbf-xl with R2 = 0.340

Model-based training with 1 models
Best R2: 0.340, Mean R2: 0.243
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.2325, kl_div=0.0000
    Epoch 1: policy_loss=0.0460, value_loss=0.9691, entropy=0.2348, kl_div=-0.0663
  Round 1/5: Mean predicted reward = 10.122
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2076, kl_div=0.0000
    Epoch 1: policy_loss=-0.0281, value_loss=0.9689, entropy=0.2102, kl_div=-0.4038
  Round 2/5: Mean predicted reward = 9.679
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2417, kl_div=0.0000
    Epoch 1: policy_loss=-0.0377, value_loss=0.9688, entropy=0.2456, kl_div=-0.3908
  Round 3/5: Mean predicted reward = 9.954
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2719, kl_div=0.0000
    Epoch 1: policy_loss=-0.0704, value_loss=0.9688, entropy=0.2728, kl_div=-0.1340
  Round 4/5: Mean predicted reward = 10.396
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.2655, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2386
  Round 5/5: Mean predicted reward = 10.208

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 81 Results ---
  Mean Oracle Reward: 10.290
  Min Oracle Reward: 6.967
  Max Oracle Reward: 12.240
  Std Oracle Reward: 1.094
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.243, Max: 0.340, Count: 13
  Total Sequences Evaluated: 2642

======================================================================
EXPERIMENT ROUND 82/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2642
  Performance plateaued, reducing LR to 0.000100

--- Round 82 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  GCTCCGGGATAC
  AGGACTTCCGCG
  CATAGGGTCCGC
  GGACATCGCTGC
  GCTCAAGGCCGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.506
  Max reward: 12.616
  With intrinsic bonuses: 10.538

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.2274, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1387

=== Surrogate Model Training ===
Total samples: 2674

Training on 2558 samples (removed 116 outliers)
Reward range: [7.19, 13.48], mean: 10.41
  Created 13 candidate models for data size 2558
Current R2 threshold: 0.42
  rf-tuned-l: R2 = 0.295 (std: 0.121)
  rf-tuned-xl: R2 = 0.288 (std: 0.122)
  gb-tuned-l: R2 = 0.290 (std: 0.099)
  gb-tuned-xl: R2 = 0.290 (std: 0.099)
  xgb-xl: R2 = 0.276 (std: 0.109)
  xgb-l: R2 = 0.276 (std: 0.109)
  mlp-adaptive-xl: R2 = 0.304 (std: 0.094)
  mlp-l: R2 = 0.292 (std: 0.093)
  svr-rbf-xl: R2 = 0.348 (std: 0.095)
  svr-poly-l: R2 = 0.348 (std: 0.095)
  knn-tuned-sqrt: R2 = 0.152 (std: 0.118)
  knn-tuned-l: R2 = 0.152 (std: 0.118)
  ridge: R2 = -0.034 (std: 0.147)
  Fallback: Using svr-rbf-xl with R2 = 0.348

Model-based training with 1 models
Best R2: 0.348, Mean R2: 0.252
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9685, entropy=0.2374, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0570
  Round 1/5: Mean predicted reward = 9.463
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2629, kl_div=0.0000
    Epoch 1: policy_loss=0.0052, value_loss=0.9690, entropy=0.2635, kl_div=-0.0151
  Round 2/5: Mean predicted reward = 9.646
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.2549, kl_div=0.0000
    Epoch 1: policy_loss=-0.0497, value_loss=0.9691, entropy=0.2567, kl_div=-0.0768
  Round 3/5: Mean predicted reward = 10.064
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.2702, kl_div=0.0000
    Epoch 1: policy_loss=-0.0534, value_loss=0.9688, entropy=0.2699, kl_div=0.0228
  Round 4/5: Mean predicted reward = 10.045
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2402, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1417
  Round 5/5: Mean predicted reward = 10.229

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 82 Results ---
  Mean Oracle Reward: 10.510
  Min Oracle Reward: 6.798
  Max Oracle Reward: 12.687
  Std Oracle Reward: 1.362
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.252, Max: 0.348, Count: 13
  Total Sequences Evaluated: 2674

======================================================================
EXPERIMENT ROUND 83/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2674
  Performance plateaued, reducing LR to 0.000055

--- Round 83 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGGAGTGCTCAC
  ACGGTCCGGTCA
  GTCCTGACGAGC
  CTCGCGAATCGG
  CTCCAAGTGGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.887
  Max reward: 14.090
  With intrinsic bonuses: 10.883

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.2396, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1510

=== Surrogate Model Training ===
Total samples: 2706

Training on 2587 samples (removed 119 outliers)
Reward range: [7.21, 13.48], mean: 10.42
  Created 13 candidate models for data size 2587
Current R2 threshold: 0.43
  rf-tuned-l: R2 = 0.293 (std: 0.115)
  rf-tuned-xl: R2 = 0.289 (std: 0.124)
  gb-tuned-l: R2 = 0.288 (std: 0.102)
  gb-tuned-xl: R2 = 0.288 (std: 0.102)
  xgb-xl: R2 = 0.302 (std: 0.115)
  xgb-l: R2 = 0.302 (std: 0.115)
  mlp-adaptive-xl: R2 = 0.291 (std: 0.107)
  mlp-l: R2 = 0.308 (std: 0.090)
  svr-rbf-xl: R2 = 0.355 (std: 0.096)
  svr-poly-l: R2 = 0.355 (std: 0.096)
  knn-tuned-sqrt: R2 = 0.144 (std: 0.117)
  knn-tuned-l: R2 = 0.144 (std: 0.117)
  ridge: R2 = -0.034 (std: 0.144)
  Fallback: Using svr-rbf-xl with R2 = 0.355

Model-based training with 1 models
Best R2: 0.355, Mean R2: 0.256
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2382, kl_div=0.0000
    Epoch 1: policy_loss=0.0174, value_loss=0.9687, entropy=0.2376, kl_div=0.0382
  Round 1/5: Mean predicted reward = 9.271
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.2685, kl_div=0.0000
    Epoch 1: policy_loss=-0.0450, value_loss=0.9686, entropy=0.2698, kl_div=-0.0681
  Round 2/5: Mean predicted reward = 9.507
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2666, kl_div=0.0000
    Epoch 1: policy_loss=-0.0526, value_loss=0.9687, entropy=0.2693, kl_div=-0.1123
  Round 3/5: Mean predicted reward = 10.028
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2466, kl_div=0.0000
    Epoch 1: policy_loss=-0.0314, value_loss=0.9689, entropy=0.2496, kl_div=-0.1516
  Round 4/5: Mean predicted reward = 10.168
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2159, kl_div=0.0000
    Epoch 1: policy_loss=0.0109, value_loss=0.9687, entropy=0.2169, kl_div=-0.0554
  Round 5/5: Mean predicted reward = 10.091

  === Progress Analysis ===
  Status: NORMAL

--- Round 83 Results ---
  Mean Oracle Reward: 10.868
  Min Oracle Reward: 8.026
  Max Oracle Reward: 13.931
  Std Oracle Reward: 1.240
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.256, Max: 0.355, Count: 13
  Total Sequences Evaluated: 2706

======================================================================
EXPERIMENT ROUND 84/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2706
  Consistent improvement, increasing LR to 0.000045

--- Round 84 Configuration ---
Learning rate: 0.000045
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GACCCTGGCTAG
  TCAGCGCGGTAC
  CTGACATCCGGG
  CAGGCACGTTGC
  GCCTCAAGTGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.439
  Max reward: 12.488
  With intrinsic bonuses: 10.426

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.2436, kl_div=0.0000
    Epoch 1: policy_loss=-0.0124, value_loss=0.9692, entropy=0.2440, kl_div=0.0025

=== Surrogate Model Training ===
Total samples: 2738

Training on 2619 samples (removed 119 outliers)
Reward range: [7.21, 13.48], mean: 10.42
  Created 13 candidate models for data size 2619
Current R2 threshold: 0.44
  rf-tuned-l: R2 = 0.297 (std: 0.116)
  rf-tuned-xl: R2 = 0.298 (std: 0.123)
  gb-tuned-l: R2 = 0.288 (std: 0.106)
  gb-tuned-xl: R2 = 0.288 (std: 0.106)
  xgb-xl: R2 = 0.304 (std: 0.106)
  xgb-l: R2 = 0.304 (std: 0.106)
  mlp-adaptive-xl: R2 = 0.305 (std: 0.110)
  mlp-l: R2 = 0.336 (std: 0.097)
  svr-rbf-xl: R2 = 0.360 (std: 0.095)
  svr-poly-l: R2 = 0.360 (std: 0.095)
  knn-tuned-sqrt: R2 = 0.147 (std: 0.110)
  knn-tuned-l: R2 = 0.147 (std: 0.110)
  ridge: R2 = -0.035 (std: 0.146)
  Fallback: Using svr-rbf-xl with R2 = 0.360

Model-based training with 1 models
Best R2: 0.360, Mean R2: 0.261
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9685, entropy=0.2338, kl_div=0.0000
    Epoch 1: policy_loss=-0.0514, value_loss=0.9685, entropy=0.2351, kl_div=-0.0904
  Round 1/5: Mean predicted reward = 8.995
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.2638, kl_div=0.0000
    Epoch 1: policy_loss=-0.0295, value_loss=0.9685, entropy=0.2658, kl_div=-0.0620
  Round 2/5: Mean predicted reward = 9.379
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.2487, kl_div=0.0000
    Epoch 1: policy_loss=-0.0422, value_loss=0.9686, entropy=0.2507, kl_div=-0.1077
  Round 3/5: Mean predicted reward = 9.695
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2671, kl_div=0.0000
    Epoch 1: policy_loss=-0.0376, value_loss=0.9687, entropy=0.2692, kl_div=-0.1419
  Round 4/5: Mean predicted reward = 10.130
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.2719, kl_div=0.0000
    Epoch 1: policy_loss=0.0077, value_loss=0.9693, entropy=0.2726, kl_div=-0.0935
  Round 5/5: Mean predicted reward = 10.368

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 84 Results ---
  Mean Oracle Reward: 10.460
  Min Oracle Reward: 6.353
  Max Oracle Reward: 12.632
  Std Oracle Reward: 1.518
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.261, Max: 0.360, Count: 13
  Total Sequences Evaluated: 2738

======================================================================
EXPERIMENT ROUND 85/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2738

--- Round 85 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCGCCGCGTAGA
  TCCGGGCAACTG
  TCGAGCCATCGG
  CGTGCGGCCATA
  CCGGTCAGCTAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.435
  Max reward: 12.626
  With intrinsic bonuses: 10.383

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.2708, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1757

=== Surrogate Model Training ===
Total samples: 2770

Training on 2649 samples (removed 121 outliers)
Reward range: [7.21, 13.48], mean: 10.42
  Created 13 candidate models for data size 2649
Current R2 threshold: 0.45
  rf-tuned-l: R2 = 0.310 (std: 0.131)
  rf-tuned-xl: R2 = 0.309 (std: 0.133)
  gb-tuned-l: R2 = 0.310 (std: 0.115)
  gb-tuned-xl: R2 = 0.310 (std: 0.115)
  xgb-xl: R2 = 0.310 (std: 0.122)
  xgb-l: R2 = 0.310 (std: 0.122)
  mlp-adaptive-xl: R2 = 0.332 (std: 0.124)
  mlp-l: R2 = 0.320 (std: 0.113)
  svr-rbf-xl: R2 = 0.379 (std: 0.105)
  svr-poly-l: R2 = 0.379 (std: 0.105)
  knn-tuned-sqrt: R2 = 0.165 (std: 0.125)
  knn-tuned-l: R2 = 0.165 (std: 0.125)
  ridge: R2 = -0.031 (std: 0.154)
  Fallback: Using svr-rbf-xl with R2 = 0.379

Model-based training with 1 models
Best R2: 0.379, Mean R2: 0.274
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.2680, kl_div=0.0000
    Epoch 1: policy_loss=-0.0742, value_loss=0.9686, entropy=0.2688, kl_div=-0.1156
  Round 1/5: Mean predicted reward = 8.987
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.2695, kl_div=0.0000
    Epoch 1: policy_loss=0.0290, value_loss=0.9686, entropy=0.2765, kl_div=-0.4043
  Round 2/5: Mean predicted reward = 9.447
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.2832, kl_div=0.0000
    Epoch 1: policy_loss=-0.0205, value_loss=0.9686, entropy=0.2844, kl_div=-0.3227
  Round 3/5: Mean predicted reward = 9.955
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2960, kl_div=0.0000
    Epoch 1: policy_loss=-0.0500, value_loss=0.9689, entropy=0.2893, kl_div=-0.1675
  Round 4/5: Mean predicted reward = 10.047
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3060, kl_div=0.0000
    Epoch 1: policy_loss=-0.0814, value_loss=0.9689, entropy=0.2994, kl_div=-0.0135
  Round 5/5: Mean predicted reward = 10.310

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 85 Results ---
  Mean Oracle Reward: 10.429
  Min Oracle Reward: 6.146
  Max Oracle Reward: 12.686
  Std Oracle Reward: 1.578
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.274, Max: 0.379, Count: 13
  Total Sequences Evaluated: 2770

======================================================================
EXPERIMENT ROUND 86/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2770

--- Round 86 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGGGTGAACCCC
  ACGTCAGGGTCC
  TGCAACGTGCCG
  CCCGGTAGACTG
  GACCGCGTCTAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.173
  Max reward: 13.133
  With intrinsic bonuses: 10.131

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2692, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2767

=== Surrogate Model Training ===
Total samples: 2802

Training on 2680 samples (removed 122 outliers)
Reward range: [7.21, 13.48], mean: 10.42
  Created 13 candidate models for data size 2680
Current R2 threshold: 0.46
  rf-tuned-l: R2 = 0.317 (std: 0.127)
  rf-tuned-xl: R2 = 0.322 (std: 0.126)
  gb-tuned-l: R2 = 0.315 (std: 0.117)
  gb-tuned-xl: R2 = 0.315 (std: 0.117)
  xgb-xl: R2 = 0.320 (std: 0.125)
  xgb-l: R2 = 0.320 (std: 0.125)
  mlp-adaptive-xl: R2 = 0.347 (std: 0.119)
  mlp-l: R2 = 0.338 (std: 0.119)
  svr-rbf-xl: R2 = 0.384 (std: 0.110)
  svr-poly-l: R2 = 0.384 (std: 0.110)
  knn-tuned-sqrt: R2 = 0.175 (std: 0.130)
  knn-tuned-l: R2 = 0.175 (std: 0.130)
  ridge: R2 = -0.028 (std: 0.157)
  Fallback: Using svr-rbf-xl with R2 = 0.384

Model-based training with 1 models
Best R2: 0.384, Mean R2: 0.283
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2679, kl_div=0.0000
    Epoch 1: policy_loss=-0.0196, value_loss=0.9687, entropy=0.2676, kl_div=-0.0946
  Round 1/5: Mean predicted reward = 9.071
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2889, kl_div=0.0000
    Epoch 1: policy_loss=-0.0685, value_loss=0.9689, entropy=0.2912, kl_div=-0.2052
  Round 2/5: Mean predicted reward = 9.783
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2783, kl_div=0.0000
    Epoch 1: policy_loss=-0.0295, value_loss=0.9689, entropy=0.2842, kl_div=-0.2925
  Round 3/5: Mean predicted reward = 10.002
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2715, kl_div=0.0000
    Epoch 1: policy_loss=-0.0778, value_loss=0.9689, entropy=0.2745, kl_div=-0.0855
  Round 4/5: Mean predicted reward = 10.073
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2687, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4262
  Round 5/5: Mean predicted reward = 10.227

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 86 Results ---
  Mean Oracle Reward: 10.188
  Min Oracle Reward: 6.328
  Max Oracle Reward: 12.896
  Std Oracle Reward: 1.439
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.283, Max: 0.384, Count: 13
  Total Sequences Evaluated: 2802

======================================================================
EXPERIMENT ROUND 87/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2802

--- Round 87 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  ACGGCGACTGCT
  GCCCCTGGAATG
  CCAGGCAGTCGT
  TGGAACCTGCAG
  AATTGCGCGCGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.461
  Max reward: 12.247
  With intrinsic bonuses: 10.438

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3073, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2547

=== Surrogate Model Training ===
Total samples: 2834

Training on 2712 samples (removed 122 outliers)
Reward range: [7.21, 13.48], mean: 10.42
  Created 13 candidate models for data size 2712
Current R2 threshold: 0.47000000000000003
  rf-tuned-l: R2 = 0.322 (std: 0.116)
  rf-tuned-xl: R2 = 0.319 (std: 0.121)
  gb-tuned-l: R2 = 0.313 (std: 0.107)
  gb-tuned-xl: R2 = 0.313 (std: 0.107)
  xgb-xl: R2 = 0.312 (std: 0.098)
  xgb-l: R2 = 0.312 (std: 0.098)
  mlp-adaptive-xl: R2 = 0.330 (std: 0.101)
  mlp-l: R2 = 0.327 (std: 0.110)
  svr-rbf-xl: R2 = 0.385 (std: 0.105)
  svr-poly-l: R2 = 0.385 (std: 0.105)
  knn-tuned-sqrt: R2 = 0.177 (std: 0.126)
  knn-tuned-l: R2 = 0.177 (std: 0.126)
  ridge: R2 = -0.031 (std: 0.162)
  Fallback: Using svr-rbf-xl with R2 = 0.385

Model-based training with 1 models
Best R2: 0.385, Mean R2: 0.280
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.3063, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1553
  Round 1/5: Mean predicted reward = 9.562
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2907, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1091
  Round 2/5: Mean predicted reward = 9.917
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3126, kl_div=0.0000
    Epoch 1: policy_loss=-0.0441, value_loss=0.9689, entropy=0.3132, kl_div=0.0070
  Round 3/5: Mean predicted reward = 9.724
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.3007, kl_div=0.0000
    Epoch 1: policy_loss=-0.0488, value_loss=0.9688, entropy=0.3045, kl_div=-0.0732
  Round 4/5: Mean predicted reward = 10.014
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2735, kl_div=0.0000
    Epoch 1: policy_loss=-0.0419, value_loss=0.9688, entropy=0.2772, kl_div=-0.0280
  Round 5/5: Mean predicted reward = 10.219

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 87 Results ---
  Mean Oracle Reward: 10.467
  Min Oracle Reward: 7.211
  Max Oracle Reward: 12.165
  Std Oracle Reward: 1.183
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.280, Max: 0.385, Count: 13
  Total Sequences Evaluated: 2834

======================================================================
EXPERIMENT ROUND 88/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2834

--- Round 88 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ATCGCCAGGTGC
  GTCGGCCGAATC
  CAGTGGGCACTC
  ACAGTTCGCAGG
  TGGAGACCGCCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.260
  Max reward: 13.389
  With intrinsic bonuses: 10.187

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.3082, kl_div=0.0000
    Epoch 1: policy_loss=-0.0628, value_loss=0.9690, entropy=0.3097, kl_div=0.0490

=== Surrogate Model Training ===
Total samples: 2866

Training on 2740 samples (removed 126 outliers)
Reward range: [7.21, 13.48], mean: 10.42
  Created 13 candidate models for data size 2740
Current R2 threshold: 0.48000000000000004
  rf-tuned-l: R2 = 0.315 (std: 0.117)
  rf-tuned-xl: R2 = 0.323 (std: 0.122)
  gb-tuned-l: R2 = 0.313 (std: 0.114)
  gb-tuned-xl: R2 = 0.313 (std: 0.114)
  xgb-xl: R2 = 0.322 (std: 0.095)
  xgb-l: R2 = 0.322 (std: 0.095)
  mlp-adaptive-xl: R2 = 0.332 (std: 0.133)
  mlp-l: R2 = 0.332 (std: 0.115)
  svr-rbf-xl: R2 = 0.389 (std: 0.106)
  svr-poly-l: R2 = 0.389 (std: 0.106)
  knn-tuned-sqrt: R2 = 0.182 (std: 0.129)
  knn-tuned-l: R2 = 0.182 (std: 0.129)
  ridge: R2 = -0.025 (std: 0.157)
  Fallback: Using svr-rbf-xl with R2 = 0.389

Model-based training with 1 models
Best R2: 0.389, Mean R2: 0.284
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3179, kl_div=0.0000
    Epoch 1: policy_loss=-0.0712, value_loss=0.9688, entropy=0.3193, kl_div=-0.0288
  Round 1/5: Mean predicted reward = 9.623
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.3029, kl_div=0.0000
    Epoch 1: policy_loss=-0.0440, value_loss=0.9687, entropy=0.3065, kl_div=-0.0935
  Round 2/5: Mean predicted reward = 10.056
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3011, kl_div=0.0000
    Epoch 1: policy_loss=-0.0413, value_loss=0.9689, entropy=0.3017, kl_div=0.0071
  Round 3/5: Mean predicted reward = 10.202
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.3195, kl_div=0.0000
    Epoch 1: policy_loss=-0.0091, value_loss=0.9687, entropy=0.3189, kl_div=-0.0213
  Round 4/5: Mean predicted reward = 10.344
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.2934, kl_div=0.0000
    Epoch 1: policy_loss=-0.0218, value_loss=0.9688, entropy=0.2921, kl_div=-0.0408
  Round 5/5: Mean predicted reward = 10.231

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 88 Results ---
  Mean Oracle Reward: 10.237
  Min Oracle Reward: 4.933
  Max Oracle Reward: 13.435
  Std Oracle Reward: 1.833
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.284, Max: 0.389, Count: 13
  Total Sequences Evaluated: 2866

======================================================================
EXPERIMENT ROUND 89/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2866

--- Round 89 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCAGTCGCGACG
  CAGTCCTGCGGA
  CGATCGGCCGTA
  ATCGCGGCTACG
  GCACGGTTCCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.246
  Max reward: 12.769
  With intrinsic bonuses: 10.239

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3472, kl_div=0.0000
    Epoch 1: policy_loss=-0.0353, value_loss=0.9688, entropy=0.3464, kl_div=0.0479

=== Surrogate Model Training ===
Total samples: 2898

Training on 2769 samples (removed 129 outliers)
Reward range: [7.25, 13.48], mean: 10.42
  Created 13 candidate models for data size 2769
Current R2 threshold: 0.49000000000000005
  rf-tuned-l: R2 = 0.320 (std: 0.119)
  rf-tuned-xl: R2 = 0.318 (std: 0.120)
  gb-tuned-l: R2 = 0.314 (std: 0.109)
  gb-tuned-xl: R2 = 0.314 (std: 0.109)
  xgb-xl: R2 = 0.339 (std: 0.113)
  xgb-l: R2 = 0.339 (std: 0.113)
  mlp-adaptive-xl: R2 = 0.342 (std: 0.101)
  mlp-l: R2 = 0.328 (std: 0.121)
  svr-rbf-xl: R2 = 0.388 (std: 0.107)
  svr-poly-l: R2 = 0.388 (std: 0.107)
  knn-tuned-sqrt: R2 = 0.176 (std: 0.135)
  knn-tuned-l: R2 = 0.176 (std: 0.135)
  ridge: R2 = -0.027 (std: 0.155)
  Fallback: Using svr-rbf-xl with R2 = 0.388

Model-based training with 1 models
Best R2: 0.388, Mean R2: 0.286
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.3073, kl_div=0.0000
    Epoch 1: policy_loss=-0.0038, value_loss=0.9687, entropy=0.3069, kl_div=0.0481
  Round 1/5: Mean predicted reward = 9.796
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3195, kl_div=0.0000
    Epoch 1: policy_loss=-0.0402, value_loss=0.9688, entropy=0.3193, kl_div=-0.0137
  Round 2/5: Mean predicted reward = 9.888
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3230, kl_div=0.0000
    Epoch 1: policy_loss=-0.0256, value_loss=0.9688, entropy=0.3237, kl_div=-0.0514
  Round 3/5: Mean predicted reward = 10.274
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.3067, kl_div=0.0000
    Epoch 1: policy_loss=-0.0476, value_loss=0.9691, entropy=0.3059, kl_div=-0.0472
  Round 4/5: Mean predicted reward = 10.164
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.3101, kl_div=0.0000
    Epoch 1: policy_loss=-0.0089, value_loss=0.9688, entropy=0.3098, kl_div=-0.0060
  Round 5/5: Mean predicted reward = 10.218

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 89 Results ---
  Mean Oracle Reward: 10.239
  Min Oracle Reward: 6.329
  Max Oracle Reward: 12.725
  Std Oracle Reward: 1.296
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.286, Max: 0.388, Count: 13
  Total Sequences Evaluated: 2898

======================================================================
EXPERIMENT ROUND 90/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2898
  Performance plateaued, reducing LR to 0.000150

--- Round 90 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AGGCCGGCATCT
  GCGCGTCACGTA
  CCCAGTAGTCGG
  TGGTGAAGCCCA
  AATCGGGCCTCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.574
  Max reward: 12.734
  With intrinsic bonuses: 10.558

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2928, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3737

=== Surrogate Model Training ===
Total samples: 2930

Training on 2800 samples (removed 130 outliers)
Reward range: [7.25, 13.48], mean: 10.43
  Created 13 candidate models for data size 2800
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.316 (std: 0.125)
  rf-tuned-xl: R2 = 0.321 (std: 0.133)
  gb-tuned-l: R2 = 0.313 (std: 0.118)
  gb-tuned-xl: R2 = 0.313 (std: 0.118)
  xgb-xl: R2 = 0.331 (std: 0.106)
  xgb-l: R2 = 0.331 (std: 0.106)
  mlp-adaptive-xl: R2 = 0.328 (std: 0.113)
  mlp-l: R2 = 0.352 (std: 0.127)
  svr-rbf-xl: R2 = 0.390 (std: 0.113)
  svr-poly-l: R2 = 0.390 (std: 0.113)
  knn-tuned-sqrt: R2 = 0.178 (std: 0.138)
  knn-tuned-l: R2 = 0.178 (std: 0.138)
  ridge: R2 = -0.028 (std: 0.168)
  Fallback: Using svr-rbf-xl with R2 = 0.390

Model-based training with 1 models
Best R2: 0.390, Mean R2: 0.286
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.3471, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0635
  Round 1/5: Mean predicted reward = 9.708
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.3174, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0839
  Round 2/5: Mean predicted reward = 9.720
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3192, kl_div=0.0000
    Epoch 1: policy_loss=-0.0422, value_loss=0.9688, entropy=0.3227, kl_div=-0.0299
  Round 3/5: Mean predicted reward = 10.160
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3288, kl_div=0.0000
    Epoch 1: policy_loss=0.0613, value_loss=0.9689, entropy=0.3363, kl_div=-0.3180
  Round 4/5: Mean predicted reward = 10.346
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.3251, kl_div=0.0000
    Epoch 1: policy_loss=-0.0551, value_loss=0.9687, entropy=0.3317, kl_div=-0.1187
  Round 5/5: Mean predicted reward = 10.655

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 90 Results ---
  Mean Oracle Reward: 10.640
  Min Oracle Reward: 7.406
  Max Oracle Reward: 12.961
  Std Oracle Reward: 1.172
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.286, Max: 0.390, Count: 13
  Total Sequences Evaluated: 2930

======================================================================
EXPERIMENT ROUND 91/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2930

--- Round 91 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTGGGACGCCTA
  CACACTTGGGCG
  CTAGGTCGCAGC
  TCACTCCAGGGG
  CGGCAGTGTCAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.361
  Max reward: 13.040
  With intrinsic bonuses: 10.334

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3347, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1980

=== Surrogate Model Training ===
Total samples: 2962

Training on 2832 samples (removed 130 outliers)
Reward range: [7.24, 13.48], mean: 10.42
  Created 13 candidate models for data size 2832
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.326 (std: 0.133)
  rf-tuned-xl: R2 = 0.330 (std: 0.131)
  gb-tuned-l: R2 = 0.317 (std: 0.126)
  gb-tuned-xl: R2 = 0.317 (std: 0.126)
  xgb-xl: R2 = 0.345 (std: 0.122)
  xgb-l: R2 = 0.345 (std: 0.122)
  mlp-adaptive-xl: R2 = 0.333 (std: 0.114)
  mlp-l: R2 = 0.349 (std: 0.124)
  svr-rbf-xl: R2 = 0.394 (std: 0.122)
  svr-poly-l: R2 = 0.394 (std: 0.122)
  knn-tuned-sqrt: R2 = 0.182 (std: 0.160)
  knn-tuned-l: R2 = 0.182 (std: 0.160)
  ridge: R2 = -0.032 (std: 0.176)
  Fallback: Using svr-rbf-xl with R2 = 0.394

Model-based training with 1 models
Best R2: 0.394, Mean R2: 0.291
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.3524, kl_div=0.0000
    Epoch 1: policy_loss=-0.0265, value_loss=0.9689, entropy=0.3565, kl_div=-0.1381
  Round 1/5: Mean predicted reward = 10.139
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.3460, kl_div=0.0000
    Epoch 1: policy_loss=-0.0820, value_loss=0.9688, entropy=0.3502, kl_div=0.0373
  Round 2/5: Mean predicted reward = 10.079
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.3496, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2047
  Round 3/5: Mean predicted reward = 10.002
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.3402, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2867
  Round 4/5: Mean predicted reward = 10.245
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3012, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4798
  Round 5/5: Mean predicted reward = 10.133

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 91 Results ---
  Mean Oracle Reward: 10.341
  Min Oracle Reward: 7.248
  Max Oracle Reward: 12.972
  Std Oracle Reward: 1.237
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.291, Max: 0.394, Count: 13
  Total Sequences Evaluated: 2962

======================================================================
EXPERIMENT ROUND 92/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2962

--- Round 92 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTCAGCGACGGT
  ACAGGCTCGTGC
  GCGCTCGCAGTA
  ACTGTCCGACGG
  GGAGTCGCCATC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.062
  Max reward: 12.538
  With intrinsic bonuses: 10.056

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.3096, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3700

=== Surrogate Model Training ===
Total samples: 2994

Training on 2862 samples (removed 132 outliers)
Reward range: [7.25, 13.48], mean: 10.42
  Created 13 candidate models for data size 2862
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.324 (std: 0.132)
  rf-tuned-xl: R2 = 0.332 (std: 0.137)
  gb-tuned-l: R2 = 0.322 (std: 0.132)
  gb-tuned-xl: R2 = 0.322 (std: 0.132)
  xgb-xl: R2 = 0.336 (std: 0.132)
  xgb-l: R2 = 0.336 (std: 0.132)
  mlp-adaptive-xl: R2 = 0.338 (std: 0.109)
  mlp-l: R2 = 0.326 (std: 0.118)
  svr-rbf-xl: R2 = 0.392 (std: 0.125)
  svr-poly-l: R2 = 0.392 (std: 0.125)
  knn-tuned-sqrt: R2 = 0.184 (std: 0.167)
  knn-tuned-l: R2 = 0.184 (std: 0.167)
  ridge: R2 = -0.029 (std: 0.177)
  Fallback: Using svr-rbf-xl with R2 = 0.392

Model-based training with 1 models
Best R2: 0.392, Mean R2: 0.289
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3003, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2903
  Round 1/5: Mean predicted reward = 9.811
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.3486, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0544
  Round 2/5: Mean predicted reward = 9.949
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2934, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2372
  Round 3/5: Mean predicted reward = 10.099
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.3047, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3898
  Round 4/5: Mean predicted reward = 10.142
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.2982, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2761
  Round 5/5: Mean predicted reward = 10.338

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 92 Results ---
  Mean Oracle Reward: 10.039
  Min Oracle Reward: 6.763
  Max Oracle Reward: 12.523
  Std Oracle Reward: 1.327
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.289, Max: 0.392, Count: 13
  Total Sequences Evaluated: 2994

======================================================================
EXPERIMENT ROUND 93/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2994

--- Round 93 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  GCTTGCAACGGC
  CAGTTCGGGCAC
  GCTGGCATAGCC
  TGAGGCTCAGCC
  CCCATGTGGAAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.159
  Max reward: 12.202
  With intrinsic bonuses: 10.074

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2609, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0674

=== Surrogate Model Training ===
Total samples: 3026

Training on 2891 samples (removed 135 outliers)
Reward range: [7.26, 13.42], mean: 10.42
  Created 13 candidate models for data size 2891
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.326 (std: 0.145)
  rf-tuned-xl: R2 = 0.323 (std: 0.139)
  gb-tuned-l: R2 = 0.313 (std: 0.138)
  gb-tuned-xl: R2 = 0.313 (std: 0.138)
  xgb-xl: R2 = 0.334 (std: 0.136)
  xgb-l: R2 = 0.334 (std: 0.136)
  mlp-adaptive-xl: R2 = 0.338 (std: 0.116)
  mlp-l: R2 = 0.329 (std: 0.131)
  svr-rbf-xl: R2 = 0.389 (std: 0.121)
  svr-poly-l: R2 = 0.389 (std: 0.121)
  knn-tuned-sqrt: R2 = 0.180 (std: 0.171)
  knn-tuned-l: R2 = 0.180 (std: 0.171)
  ridge: R2 = -0.026 (std: 0.166)
  Fallback: Using svr-rbf-xl with R2 = 0.389

Model-based training with 1 models
Best R2: 0.389, Mean R2: 0.286
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.2607, kl_div=0.0000
    Epoch 1: policy_loss=-0.0124, value_loss=0.9686, entropy=0.2601, kl_div=0.0108
  Round 1/5: Mean predicted reward = 9.418
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2590, kl_div=0.0000
    Epoch 1: policy_loss=-0.0411, value_loss=0.9687, entropy=0.2601, kl_div=-0.0733
  Round 2/5: Mean predicted reward = 9.715
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2913, kl_div=0.0000
    Epoch 1: policy_loss=-0.0223, value_loss=0.9688, entropy=0.2922, kl_div=-0.1014
  Round 3/5: Mean predicted reward = 9.951
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2650, kl_div=0.0000
    Epoch 1: policy_loss=-0.0357, value_loss=0.9688, entropy=0.2664, kl_div=-0.0875
  Round 4/5: Mean predicted reward = 9.956
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.3256, kl_div=0.0000
    Epoch 1: policy_loss=-0.0430, value_loss=0.9689, entropy=0.3260, kl_div=0.0088
  Round 5/5: Mean predicted reward = 10.523

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 93 Results ---
  Mean Oracle Reward: 10.107
  Min Oracle Reward: 6.445
  Max Oracle Reward: 12.076
  Std Oracle Reward: 1.181
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.286, Max: 0.389, Count: 13
  Total Sequences Evaluated: 3026

======================================================================
EXPERIMENT ROUND 94/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 3026

--- Round 94 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTCGAAGCGTCG
  GACAGCTCTCGG
  CTCACCGGGATG
  TGGCCCGGATAC
  TGTAGCAGCCGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.234
  Max reward: 11.703
  With intrinsic bonuses: 10.221

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2928, kl_div=0.0000
    Epoch 1: policy_loss=-0.0244, value_loss=0.9688, entropy=0.2920, kl_div=0.0331

=== Surrogate Model Training ===
Total samples: 3058

Training on 2922 samples (removed 136 outliers)
Reward range: [7.26, 13.42], mean: 10.42
  Created 13 candidate models for data size 2922
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.330 (std: 0.147)
  rf-tuned-xl: R2 = 0.324 (std: 0.147)
  gb-tuned-l: R2 = 0.310 (std: 0.124)
  gb-tuned-xl: R2 = 0.310 (std: 0.124)
  xgb-xl: R2 = 0.339 (std: 0.128)
  xgb-l: R2 = 0.339 (std: 0.128)
  mlp-adaptive-xl: R2 = 0.340 (std: 0.121)
  mlp-l: R2 = 0.343 (std: 0.121)
  svr-rbf-xl: R2 = 0.391 (std: 0.122)
  svr-poly-l: R2 = 0.391 (std: 0.122)
  knn-tuned-sqrt: R2 = 0.181 (std: 0.166)
  knn-tuned-l: R2 = 0.181 (std: 0.166)
  ridge: R2 = -0.025 (std: 0.170)
  Fallback: Using svr-rbf-xl with R2 = 0.391

Model-based training with 1 models
Best R2: 0.391, Mean R2: 0.289
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2581, kl_div=0.0000
    Epoch 1: policy_loss=-0.0164, value_loss=0.9687, entropy=0.2581, kl_div=-0.0035
  Round 1/5: Mean predicted reward = 9.396
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2856, kl_div=0.0000
    Epoch 1: policy_loss=-0.0338, value_loss=0.9687, entropy=0.2872, kl_div=-0.0622
  Round 2/5: Mean predicted reward = 10.225
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2924, kl_div=0.0000
    Epoch 1: policy_loss=-0.0238, value_loss=0.9687, entropy=0.2935, kl_div=-0.0353
  Round 3/5: Mean predicted reward = 9.915
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2839, kl_div=0.0000
    Epoch 1: policy_loss=-0.0190, value_loss=0.9688, entropy=0.2847, kl_div=-0.0336
  Round 4/5: Mean predicted reward = 10.260
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2910, kl_div=0.0000
    Epoch 1: policy_loss=-0.0064, value_loss=0.9689, entropy=0.2914, kl_div=-0.0096
  Round 5/5: Mean predicted reward = 10.333

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 94 Results ---
  Mean Oracle Reward: 10.247
  Min Oracle Reward: 5.467
  Max Oracle Reward: 11.696
  Std Oracle Reward: 1.137
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.289, Max: 0.391, Count: 13
  Total Sequences Evaluated: 3058

======================================================================
EXPERIMENT ROUND 95/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 3058
  Performance plateaued, reducing LR to 0.000150

--- Round 95 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGGTGGCACCTA
  GCCAATTGCCGG
  TGGCACGTGACC
  GGACTGACCGTA
  TGCAGCCCGGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.246
  Max reward: 12.306
  With intrinsic bonuses: 10.200

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2818, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1668

=== Surrogate Model Training ===
Total samples: 3090

Training on 2949 samples (removed 141 outliers)
Reward range: [7.27, 13.42], mean: 10.42
  Created 13 candidate models for data size 2949
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.335 (std: 0.149)
  rf-tuned-xl: R2 = 0.327 (std: 0.169)
  gb-tuned-l: R2 = 0.312 (std: 0.130)
  gb-tuned-xl: R2 = 0.312 (std: 0.130)
  xgb-xl: R2 = 0.354 (std: 0.124)
  xgb-l: R2 = 0.354 (std: 0.124)
  mlp-adaptive-xl: R2 = 0.341 (std: 0.125)
  mlp-l: R2 = 0.320 (std: 0.126)
  svr-rbf-xl: R2 = 0.396 (std: 0.126)
  svr-poly-l: R2 = 0.396 (std: 0.126)
  knn-tuned-sqrt: R2 = 0.180 (std: 0.173)
  knn-tuned-l: R2 = 0.180 (std: 0.173)
  ridge: R2 = -0.023 (std: 0.166)
  Fallback: Using svr-rbf-xl with R2 = 0.396

Model-based training with 1 models
Best R2: 0.396, Mean R2: 0.291
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2906, kl_div=0.0000
    Epoch 1: policy_loss=-0.0450, value_loss=0.9687, entropy=0.2918, kl_div=-0.0003
  Round 1/5: Mean predicted reward = 9.909
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3077, kl_div=0.0000
    Epoch 1: policy_loss=-0.0582, value_loss=0.9688, entropy=0.3133, kl_div=-0.0986
  Round 2/5: Mean predicted reward = 9.846
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.3106, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0653
  Round 3/5: Mean predicted reward = 10.121
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2990, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0694
  Round 4/5: Mean predicted reward = 10.243
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2986, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0916
  Round 5/5: Mean predicted reward = 10.228

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 95 Results ---
  Mean Oracle Reward: 10.221
  Min Oracle Reward: 7.501
  Max Oracle Reward: 12.308
  Std Oracle Reward: 1.102
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.291, Max: 0.396, Count: 13
  Total Sequences Evaluated: 3090

======================================================================
EXPERIMENT ROUND 96/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 3090
  Performance plateaued, reducing LR to 0.000136

--- Round 96 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CATAGCCGTAGG
  AGGAGCCCCTTG
  TTGGCCACCGAG
  ATCTGCACCGGG
  TCGGATCCCGGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.281
  Max reward: 13.329
  With intrinsic bonuses: 10.240

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.3130, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1787

=== Surrogate Model Training ===
Total samples: 3122

Training on 2978 samples (removed 144 outliers)
Reward range: [7.28, 13.42], mean: 10.42
  Created 13 candidate models for data size 2978
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.337 (std: 0.143)
  rf-tuned-xl: R2 = 0.334 (std: 0.144)
  gb-tuned-l: R2 = 0.315 (std: 0.125)
  gb-tuned-xl: R2 = 0.315 (std: 0.125)
  xgb-xl: R2 = 0.342 (std: 0.127)
  xgb-l: R2 = 0.342 (std: 0.127)
  mlp-adaptive-xl: R2 = 0.343 (std: 0.117)
  mlp-l: R2 = 0.317 (std: 0.133)
  svr-rbf-xl: R2 = 0.397 (std: 0.121)
  svr-poly-l: R2 = 0.397 (std: 0.121)
  knn-tuned-sqrt: R2 = 0.184 (std: 0.167)
  knn-tuned-l: R2 = 0.184 (std: 0.167)
  ridge: R2 = -0.021 (std: 0.156)
  Fallback: Using svr-rbf-xl with R2 = 0.397

Model-based training with 1 models
Best R2: 0.397, Mean R2: 0.291
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2891, kl_div=0.0000
    Epoch 1: policy_loss=0.0134, value_loss=0.9689, entropy=0.2886, kl_div=-0.0606
  Round 1/5: Mean predicted reward = 9.788
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2983, kl_div=0.0000
    Epoch 1: policy_loss=-0.0489, value_loss=0.9688, entropy=0.3007, kl_div=-0.1086
  Round 2/5: Mean predicted reward = 9.935
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.2966, kl_div=0.0000
    Epoch 1: policy_loss=-0.0498, value_loss=0.9688, entropy=0.2982, kl_div=-0.1033
  Round 3/5: Mean predicted reward = 10.128
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3005, kl_div=0.0000
    Epoch 1: policy_loss=-0.0644, value_loss=0.9689, entropy=0.3012, kl_div=-0.0504
  Round 4/5: Mean predicted reward = 10.048
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2736, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1218
  Round 5/5: Mean predicted reward = 10.139

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 96 Results ---
  Mean Oracle Reward: 10.294
  Min Oracle Reward: 8.173
  Max Oracle Reward: 13.241
  Std Oracle Reward: 1.123
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.291, Max: 0.397, Count: 13
  Total Sequences Evaluated: 3122

======================================================================
EXPERIMENT ROUND 97/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 3122
  Performance plateaued, reducing LR to 0.000100

--- Round 97 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCGGATATCGCG
  GGGCCAGCTACT
  GTGGACCGCTCA
  CGATACCGTGGC
  TCCCGGACAGTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.147
  Max reward: 12.594
  With intrinsic bonuses: 10.154

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.3151, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0975

=== Surrogate Model Training ===
Total samples: 3154

Training on 3010 samples (removed 144 outliers)
Reward range: [7.28, 13.42], mean: 10.42
  Created 13 candidate models for data size 3010
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.343 (std: 0.141)
  rf-tuned-xl: R2 = 0.340 (std: 0.144)
  gb-tuned-l: R2 = 0.321 (std: 0.127)
  gb-tuned-xl: R2 = 0.321 (std: 0.127)
  xgb-xl: R2 = 0.346 (std: 0.149)
  xgb-l: R2 = 0.346 (std: 0.149)
  mlp-adaptive-xl: R2 = 0.325 (std: 0.130)
  mlp-l: R2 = 0.335 (std: 0.127)
  svr-rbf-xl: R2 = 0.404 (std: 0.128)
  svr-poly-l: R2 = 0.404 (std: 0.128)
  knn-tuned-sqrt: R2 = 0.185 (std: 0.174)
  knn-tuned-l: R2 = 0.185 (std: 0.174)
  ridge: R2 = -0.014 (std: 0.156)
  Fallback: Using svr-rbf-xl with R2 = 0.404

Model-based training with 1 models
Best R2: 0.404, Mean R2: 0.295
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3383, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0760
  Round 1/5: Mean predicted reward = 9.866
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3118, kl_div=0.0000
    Epoch 1: policy_loss=-0.0486, value_loss=0.9688, entropy=0.3115, kl_div=0.0455
  Round 2/5: Mean predicted reward = 9.914
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.3091, kl_div=0.0000
    Epoch 1: policy_loss=-0.0572, value_loss=0.9687, entropy=0.3119, kl_div=-0.0627
  Round 3/5: Mean predicted reward = 10.033
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.3051, kl_div=0.0000
    Epoch 1: policy_loss=-0.0419, value_loss=0.9687, entropy=0.3041, kl_div=0.0227
  Round 4/5: Mean predicted reward = 10.343
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.3106, kl_div=0.0000
    Epoch 1: policy_loss=-0.0219, value_loss=0.9688, entropy=0.3081, kl_div=0.0403
  Round 5/5: Mean predicted reward = 10.340

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 97 Results ---
  Mean Oracle Reward: 10.123
  Min Oracle Reward: 5.750
  Max Oracle Reward: 12.704
  Std Oracle Reward: 1.386
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.295, Max: 0.404, Count: 13
  Total Sequences Evaluated: 3154

======================================================================
EXPERIMENT ROUND 98/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 3154
  Performance plateaued, reducing LR to 0.000055

--- Round 98 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  GGCTACGGTCAC
  CGTTGCGCAAGC
  CCGTATGCGGCA
  TGCCTAACGCGG
  CGCTAGACGTCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.285
  Max reward: 11.561
  With intrinsic bonuses: 10.248

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2764, kl_div=0.0000
    Epoch 1: policy_loss=-0.0067, value_loss=0.9688, entropy=0.2759, kl_div=0.0254

=== Surrogate Model Training ===
Total samples: 3186

Training on 3038 samples (removed 148 outliers)
Reward range: [7.29, 13.42], mean: 10.42
  Created 13 candidate models for data size 3038
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.354 (std: 0.147)
  rf-tuned-xl: R2 = 0.354 (std: 0.139)
  gb-tuned-l: R2 = 0.318 (std: 0.121)
  gb-tuned-xl: R2 = 0.318 (std: 0.121)
  xgb-xl: R2 = 0.359 (std: 0.136)
  xgb-l: R2 = 0.359 (std: 0.136)
  mlp-adaptive-xl: R2 = 0.332 (std: 0.136)
  mlp-l: R2 = 0.327 (std: 0.135)
  svr-rbf-xl: R2 = 0.402 (std: 0.126)
  svr-poly-l: R2 = 0.402 (std: 0.126)
  knn-tuned-sqrt: R2 = 0.194 (std: 0.169)
  knn-tuned-l: R2 = 0.194 (std: 0.169)
  ridge: R2 = -0.015 (std: 0.149)
  Fallback: Using svr-rbf-xl with R2 = 0.402

Model-based training with 1 models
Best R2: 0.402, Mean R2: 0.300
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.3284, kl_div=0.0000
    Epoch 1: policy_loss=-0.0213, value_loss=0.9688, entropy=0.3297, kl_div=-0.0369
  Round 1/5: Mean predicted reward = 9.764
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2951, kl_div=0.0000
    Epoch 1: policy_loss=-0.0290, value_loss=0.9688, entropy=0.2965, kl_div=-0.0928
  Round 2/5: Mean predicted reward = 10.206
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3018, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0532
  Round 3/5: Mean predicted reward = 9.976
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2844, kl_div=0.0000
    Epoch 1: policy_loss=-0.0240, value_loss=0.9688, entropy=0.2848, kl_div=-0.0291
  Round 4/5: Mean predicted reward = 10.088
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3099, kl_div=0.0000
    Epoch 1: policy_loss=-0.0097, value_loss=0.9688, entropy=0.3097, kl_div=0.0253
  Round 5/5: Mean predicted reward = 10.089

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 98 Results ---
  Mean Oracle Reward: 10.217
  Min Oracle Reward: 4.181
  Max Oracle Reward: 11.726
  Std Oracle Reward: 1.444
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.300, Max: 0.402, Count: 13
  Total Sequences Evaluated: 3186

======================================================================
EXPERIMENT ROUND 99/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 3186
  Performance plateaued, reducing LR to 0.000019

--- Round 99 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  CAAGGCCCGGTT
  GCTCACCGAGGT
  ACGACGGGTACT
  GGTCACCCGGAT
  GACGGCTTCAAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.053
  Max reward: 11.993
  With intrinsic bonuses: 10.041

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2726, kl_div=0.0000
    Epoch 1: policy_loss=-0.0093, value_loss=0.9687, entropy=0.2728, kl_div=0.0012

=== Surrogate Model Training ===
Total samples: 3218

Training on 3063 samples (removed 155 outliers)
Reward range: [7.30, 13.40], mean: 10.42
  Created 13 candidate models for data size 3063
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.349 (std: 0.143)
  rf-tuned-xl: R2 = 0.347 (std: 0.143)
  gb-tuned-l: R2 = 0.316 (std: 0.124)
  gb-tuned-xl: R2 = 0.316 (std: 0.124)
  xgb-xl: R2 = 0.349 (std: 0.138)
  xgb-l: R2 = 0.349 (std: 0.138)
  mlp-adaptive-xl: R2 = 0.327 (std: 0.133)
  mlp-l: R2 = 0.331 (std: 0.130)
  svr-rbf-xl: R2 = 0.398 (std: 0.125)
  svr-poly-l: R2 = 0.398 (std: 0.125)
  knn-tuned-sqrt: R2 = 0.182 (std: 0.171)
  knn-tuned-l: R2 = 0.182 (std: 0.171)
  ridge: R2 = -0.015 (std: 0.151)
  Fallback: Using svr-rbf-xl with R2 = 0.398

Model-based training with 1 models
Best R2: 0.398, Mean R2: 0.295
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2949, kl_div=0.0000
    Epoch 1: policy_loss=-0.0139, value_loss=0.9687, entropy=0.2956, kl_div=-0.0145
  Round 1/5: Mean predicted reward = 9.904
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2836, kl_div=0.0000
    Epoch 1: policy_loss=-0.0111, value_loss=0.9688, entropy=0.2846, kl_div=-0.0347
  Round 2/5: Mean predicted reward = 9.673
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2848, kl_div=0.0000
    Epoch 1: policy_loss=-0.0193, value_loss=0.9689, entropy=0.2858, kl_div=-0.0208
  Round 3/5: Mean predicted reward = 9.911
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2992, kl_div=0.0000
    Epoch 1: policy_loss=0.0033, value_loss=0.9689, entropy=0.3002, kl_div=-0.0231
  Round 4/5: Mean predicted reward = 9.996
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.3124, kl_div=0.0000
    Epoch 1: policy_loss=-0.0153, value_loss=0.9687, entropy=0.3130, kl_div=-0.0050
  Round 5/5: Mean predicted reward = 10.354

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 99 Results ---
  Mean Oracle Reward: 10.083
  Min Oracle Reward: 4.601
  Max Oracle Reward: 11.786
  Std Oracle Reward: 1.498
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.295, Max: 0.398, Count: 13
  Total Sequences Evaluated: 3218

======================================================================
EXPERIMENT ROUND 100/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 3218
  Performance plateaued, reducing LR to 0.000150

--- Round 100 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TAGGCCATCGCG
  ACATTCGCGCGG
  TACCCGGGGCTA
  CGCGGTAGTCCA
  GTGCCCACGTGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.978
  Max reward: 13.521
  With intrinsic bonuses: 9.953

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2851, kl_div=0.0000
    Epoch 1: policy_loss=0.0087, value_loss=0.9689, entropy=0.2896, kl_div=-0.0154

=== Surrogate Model Training ===
Total samples: 3250

Training on 3091 samples (removed 159 outliers)
Reward range: [7.30, 13.40], mean: 10.43
  Created 13 candidate models for data size 3091
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.348 (std: 0.135)
  rf-tuned-xl: R2 = 0.348 (std: 0.136)
  gb-tuned-l: R2 = 0.311 (std: 0.119)
  gb-tuned-xl: R2 = 0.311 (std: 0.119)
  xgb-xl: R2 = 0.350 (std: 0.138)
  xgb-l: R2 = 0.350 (std: 0.138)
  mlp-adaptive-xl: R2 = 0.328 (std: 0.147)
  mlp-l: R2 = 0.332 (std: 0.136)
  svr-rbf-xl: R2 = 0.395 (std: 0.118)
  svr-poly-l: R2 = 0.395 (std: 0.118)
  knn-tuned-sqrt: R2 = 0.182 (std: 0.158)
  knn-tuned-l: R2 = 0.182 (std: 0.158)
  ridge: R2 = -0.018 (std: 0.151)
  Fallback: Using svr-rbf-xl with R2 = 0.395

Model-based training with 1 models
Best R2: 0.395, Mean R2: 0.293
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.3064, kl_div=0.0000
    Epoch 1: policy_loss=0.0189, value_loss=0.9687, entropy=0.3107, kl_div=-0.1988
  Round 1/5: Mean predicted reward = 9.882
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.3047, kl_div=0.0000
    Epoch 1: policy_loss=-0.0169, value_loss=0.9688, entropy=0.3094, kl_div=-0.1965
  Round 2/5: Mean predicted reward = 10.090
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3291, kl_div=0.0000
    Epoch 1: policy_loss=-0.0332, value_loss=0.9688, entropy=0.3325, kl_div=-0.0680
  Round 3/5: Mean predicted reward = 9.924
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.3249, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0977
  Round 4/5: Mean predicted reward = 10.120
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3222, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0797
  Round 5/5: Mean predicted reward = 10.258

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 100 Results ---
  Mean Oracle Reward: 10.028
  Min Oracle Reward: 4.081
  Max Oracle Reward: 13.737
  Std Oracle Reward: 1.864
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.293, Max: 0.395, Count: 13
  Total Sequences Evaluated: 3250

======================================================================
DyNA PPO ALGORITHM COMPLETE!
======================================================================
Total rounds executed: 100
Total sequences evaluated: 3250
Best mean reward: 11.092 (achieved at round 65)

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 100
Final Mean Reward: 10.0285
Best Mean Reward: 11.0921
Best Max Reward: 14.5146
Initial Lr: 0.0003
Final Lr: 0.0003
Total Updates: 698
Final Diversity: 1.0000
Convergence Round: 9
==================================================

Generating learning curves...
Learning curves saved to learning_curves.png
Saving training metrics...
Metrics saved to training_metrics.json

======================================================================
FINAL OPTIMIZED SEQUENCES
======================================================================

Deterministic (Exploitation):
  GCGAGCTAGCCG: 11.030
  GCGAGCTAGCCG: 11.135
  GCGAGCTAGCCG: 10.973
  GCGAGCTAGCCG: 11.172
  GCGAGCTAGCCG: 11.195

Stochastic (Exploration):
  GCGACGGCTAGC: 11.174
  GCGATGCAGCTG: 11.678
  GCGACGAACGAT: 11.258
  GCCGATGCATGC: 11.335
  GCGTCGATCGCA: 12.322

Final Performance:
  Mean reward: 11.327
  Max reward: 12.322
  Std reward: 0.379

Best sequence found: GCGTCGATCGCA
   Reward: 12.322

======================================================================
Training complete! Check 'learning_curves.png' and 'training_metrics.json'
======================================================================