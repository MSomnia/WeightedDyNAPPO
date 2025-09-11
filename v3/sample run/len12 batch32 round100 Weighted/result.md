======================================================================
RUNNING IMPROVED DyNA PPO WITH BETTER SURROGATE LEARNING
======================================================================
======================================================================
IMPROVED DyNA PPO ALGORITHM
======================================================================
Configuration:
  Number of experiment rounds N = 100
  Number of model-based training rounds M = 5
  Minimum model score τ = 0.2
  Batch size B = 32
  Warm-up phase: True
======================================================================

=== WARM-UP PHASE ===
Generating 50 warm-up samples...
Warm-up statistics:
  Mean reward: 8.560
  Std reward: 2.650
  Min/Max: 0.000 / 12.367

Pre-training surrogate models on warm-up data...

Training on 46 samples (removed 4 outliers)
Reward range: [5.33, 12.37], mean: 9.21
  Created 8 candidate models for data size 46
Current R2 threshold: -0.3
  rf-xs: R2 = -0.195 (std: 0.605)
  rf-s: R2 = -0.161 (std: 0.564)
  knn-xs: R2 = -0.244 (std: 0.624)
  knn-s: R2 = -0.244 (std: 0.624)
  ridge: R2 = -0.428 (std: 0.583)
  gb-xs: R2 = -0.207 (std: 0.636)
  gp: R2 = -50.863 (std: 14.096)
  svr-rbf-s: R2 = -0.283 (std: 0.312)
Initial models trained: 6
Initial R2 scores - Mean: -6.578, Max: -0.161

======================================================================
EXPERIMENT ROUND 1/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.300
Total data collected: 50

--- Round 1 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  TTGGCCTAGCAT
  GTGACAAGGGTC
  ACGTGCAGTTGA
  GACAGGATTAAT
  GGTCTTGCACTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.703
  Max reward: 12.452
  With intrinsic bonuses: 9.710

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9791, entropy=1.3820, kl_div=0.0000
    Epoch 2: policy_loss=-0.2044, value_loss=0.9787, entropy=1.3844, kl_div=-0.0911
    Epoch 4: policy_loss=-0.2288, value_loss=0.9783, entropy=1.3824, kl_div=-0.0185
    Early stopping at epoch 6: KL divergence = 0.0851

=== Surrogate Model Training ===
Total samples: 82

Training on 78 samples (removed 4 outliers)
Reward range: [5.33, 12.40], mean: 9.42
  Created 8 candidate models for data size 78
Current R2 threshold: -0.3
  rf-xs: R2 = -0.103 (std: 0.172)
  rf-s: R2 = -0.058 (std: 0.072)
  knn-xs: R2 = -0.021 (std: 0.162)
  knn-s: R2 = -0.021 (std: 0.162)
  ridge: R2 = -0.191 (std: 0.111)
  gb-xs: R2 = -0.244 (std: 0.139)
  gp: R2 = -43.369 (std: 9.654)
  svr-rbf-s: R2 = -0.040 (std: 0.071)

Model-based training with 7 models
Best R2: -0.021, Mean R2: -5.506
Running 2 virtual training rounds
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9550, entropy=1.3824, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.184
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9724, entropy=1.3826, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.126

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 1 Results ---
  Mean Oracle Reward: 9.727
  Min Oracle Reward: 6.212
  Max Oracle Reward: 12.826
  Std Oracle Reward: 1.556
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: -5.506, Max: -0.021, Count: 8
  New best mean reward!
  Total Sequences Evaluated: 82

======================================================================
EXPERIMENT ROUND 2/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.300
Total data collected: 82

--- Round 2 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  AGCATAGTGGTA
  ATCCGGCATAAT
  ATAATATCCCAC
  TTTGTAGCAAAT
  CCCGTAATGCAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.169
  Max reward: 11.709
  With intrinsic bonuses: 9.192

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9646, entropy=1.3815, kl_div=0.0000
    Epoch 2: policy_loss=-0.1268, value_loss=0.9648, entropy=1.3812, kl_div=0.0186
    Early stopping at epoch 4: KL divergence = 0.0599

=== Surrogate Model Training ===
Total samples: 114

Training on 110 samples (removed 4 outliers)
Reward range: [5.33, 12.40], mean: 9.33
  Created 11 candidate models for data size 110
Current R2 threshold: -0.3
  rf-m: R2 = 0.034 (std: 0.092)
  rf-l: R2 = 0.011 (std: 0.065)
  gb-m: R2 = -0.115 (std: 0.205)
  gb-l: R2 = -0.126 (std: 0.201)
  xgb-m: R2 = -0.040 (std: 0.186)
  knn-m: R2 = 0.070 (std: 0.129)
  knn-tuned: R2 = 0.070 (std: 0.129)
  mlp-m: R2 = -0.971 (std: 0.363)
  svr-rbf: R2 = 0.043 (std: 0.079)
  svr-poly: R2 = 0.043 (std: 0.079)
  ridge: R2 = -0.024 (std: 0.060)

Model-based training with 10 models
Best R2: 0.070, Mean R2: -0.091
Running 3 virtual training rounds
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9568, entropy=1.3790, kl_div=0.0000
    Epoch 1: policy_loss=-0.0739, value_loss=0.9570, entropy=1.3766, kl_div=0.0161
  Round 1/3: Mean predicted reward = 9.246
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9577, entropy=1.3721, kl_div=0.0000
    Epoch 1: policy_loss=-0.0575, value_loss=0.9578, entropy=1.3675, kl_div=0.0317
  Round 2/3: Mean predicted reward = 9.445
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9666, entropy=1.3618, kl_div=0.0000
    Epoch 1: policy_loss=-0.0534, value_loss=0.9667, entropy=1.3553, kl_div=0.0246
  Round 3/3: Mean predicted reward = 9.392

  === Progress Analysis ===
  Status: NORMAL

--- Round 2 Results ---
  Mean Oracle Reward: 9.155
  Min Oracle Reward: 5.687
  Max Oracle Reward: 11.579
  Std Oracle Reward: 1.562
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: -0.091, Max: 0.070, Count: 11
  Total Sequences Evaluated: 114

======================================================================
EXPERIMENT ROUND 3/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.300
Total data collected: 114

--- Round 3 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  GCCGGTTACCTT
  GACCGGAGTGGT
  CCACATGCCTGG
  TCATGTACGCTA
  AGCTTGTTTTTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.555
  Max reward: 11.180
  With intrinsic bonuses: 9.731

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9603, entropy=1.3485, kl_div=0.0000
    Epoch 2: policy_loss=-0.0642, value_loss=0.9604, entropy=1.3381, kl_div=0.0383
    Early stopping at epoch 3: KL divergence = 0.0677

=== Surrogate Model Training ===
Total samples: 146

Training on 140 samples (removed 6 outliers)
Reward range: [5.73, 12.40], mean: 9.45
  Created 11 candidate models for data size 140
Current R2 threshold: -0.3
  rf-m: R2 = 0.015 (std: 0.096)
  rf-l: R2 = 0.027 (std: 0.155)
  gb-m: R2 = -0.113 (std: 0.339)
  gb-l: R2 = -0.130 (std: 0.353)
  xgb-m: R2 = -0.109 (std: 0.251)
  knn-m: R2 = -0.059 (std: 0.226)
  knn-tuned: R2 = -0.059 (std: 0.226)
  mlp-m: R2 = -0.938 (std: 0.485)
  svr-rbf: R2 = 0.059 (std: 0.116)
  svr-poly: R2 = 0.059 (std: 0.116)
  ridge: R2 = -0.015 (std: 0.079)

Model-based training with 10 models
Best R2: 0.059, Mean R2: -0.115
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.105 rf-l:0.106 gb-m:0.092 gb-l:0.090 xgb-m:0.092 knn-m:0.097 knn-tuned:0.097 svr-rbf:0.109 svr-poly:0.109 ridge:0.102
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9646, entropy=1.3322, kl_div=0.0000
    Epoch 1: policy_loss=-0.0450, value_loss=0.9646, entropy=1.3256, kl_div=0.0282
  Round 1/3: Mean predicted reward = 9.511
    Using performance-based weights
    Model weights: rf-m:0.105 rf-l:0.106 gb-m:0.092 gb-l:0.090 xgb-m:0.092 knn-m:0.097 knn-tuned:0.097 svr-rbf:0.109 svr-poly:0.109 ridge:0.102
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9637, entropy=1.3220, kl_div=0.0000
    Epoch 1: policy_loss=-0.0449, value_loss=0.9638, entropy=1.3143, kl_div=0.0225
  Round 2/3: Mean predicted reward = 9.646
    Using performance-based weights
    Model weights: rf-m:0.105 rf-l:0.106 gb-m:0.092 gb-l:0.090 xgb-m:0.092 knn-m:0.097 knn-tuned:0.097 svr-rbf:0.109 svr-poly:0.109 ridge:0.102
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9624, entropy=1.3020, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0636
  Round 3/3: Mean predicted reward = 9.411

  === Progress Analysis ===
  Status: NORMAL

--- Round 3 Results ---
  Mean Oracle Reward: 9.593
  Min Oracle Reward: 4.918
  Max Oracle Reward: 11.583
  Std Oracle Reward: 1.405
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: -0.115, Max: 0.059, Count: 11
  Total Sequences Evaluated: 146

======================================================================
EXPERIMENT ROUND 4/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.280
Total data collected: 146

--- Round 4 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0100
Exploration rate: 0.280

--- Generated Sequences (Diversity: 1.000) ---
  GAGTAATCGCCG
  ATGGCATAGCCG
  CCATTGAGACGG
  AGGGCTCTGCAC
  AGATCCGCGAGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.850
  Max reward: 12.392
  With intrinsic bonuses: 9.940

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9647, entropy=1.2918, kl_div=0.0000
    Epoch 1: policy_loss=-0.0110, value_loss=0.9647, entropy=1.2885, kl_div=0.0189
    Epoch 2: policy_loss=-0.0227, value_loss=0.9647, entropy=1.2853, kl_div=0.0386
    Early stopping at epoch 3: KL divergence = 0.0588

=== Surrogate Model Training ===
Total samples: 178

Training on 169 samples (removed 9 outliers)
Reward range: [5.97, 12.40], mean: 9.59
  Created 11 candidate models for data size 169
Current R2 threshold: -0.3
  rf-m: R2 = -0.142 (std: 0.130)
  rf-l: R2 = -0.148 (std: 0.118)
  gb-m: R2 = -0.352 (std: 0.281)
  gb-l: R2 = -0.358 (std: 0.291)
  xgb-m: R2 = -0.369 (std: 0.287)
  knn-m: R2 = -0.197 (std: 0.242)
  knn-tuned: R2 = -0.197 (std: 0.242)
  mlp-m: R2 = -1.503 (std: 1.125)
  svr-rbf: R2 = -0.019 (std: 0.130)
  svr-poly: R2 = -0.019 (std: 0.130)
  ridge: R2 = -0.097 (std: 0.159)

Model-based training with 7 models
Best R2: -0.019, Mean R2: -0.309
Running 2 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.139 rf-l:0.138 knn-m:0.132 knn-tuned:0.132 svr-rbf:0.157 svr-poly:0.157 ridge:0.145
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9648, entropy=1.2906, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.883
    Using performance-based weights
    Model weights: rf-m:0.139 rf-l:0.138 knn-m:0.132 knn-tuned:0.132 svr-rbf:0.157 svr-poly:0.157 ridge:0.145
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9738, entropy=1.2884, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.880

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 4 Results ---
  Mean Oracle Reward: 9.816
  Min Oracle Reward: 4.646
  Max Oracle Reward: 12.471
  Std Oracle Reward: 1.442
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: -0.309, Max: -0.019, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 178

======================================================================
EXPERIMENT ROUND 5/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.250
Total data collected: 178
  Consistent improvement, increasing LR to 0.000360

--- Round 5 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0100
Exploration rate: 0.250

--- Generated Sequences (Diversity: 1.000) ---
  AGAGCCATGTCG
  GGCAGTCGCACT
  GGCGATCACGTA
  GGAATCCGACGT
  GTCGGGAACACT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.871
  Max reward: 11.411
  With intrinsic bonuses: 10.016

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9755, entropy=1.2781, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1295

=== Surrogate Model Training ===
Total samples: 210

Training on 201 samples (removed 9 outliers)
Reward range: [5.96, 12.40], mean: 9.65
  Created 11 candidate models for data size 201
Current R2 threshold: -0.3
  rf-m: R2 = -0.016 (std: 0.128)
  rf-l: R2 = -0.051 (std: 0.090)
  gb-m: R2 = -0.170 (std: 0.239)
  gb-l: R2 = -0.159 (std: 0.220)
  xgb-m: R2 = -0.154 (std: 0.184)
  knn-m: R2 = -0.116 (std: 0.151)
  knn-tuned: R2 = -0.116 (std: 0.151)
  mlp-m: R2 = -1.352 (std: 0.773)
  svr-rbf: R2 = 0.062 (std: 0.067)
  svr-poly: R2 = 0.062 (std: 0.067)
  ridge: R2 = -0.040 (std: 0.076)

Model-based training with 10 models
Best R2: 0.062, Mean R2: -0.186
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.105 rf-l:0.102 gb-m:0.090 gb-l:0.091 xgb-m:0.092 knn-m:0.095 knn-tuned:0.095 svr-rbf:0.114 svr-poly:0.114 ridge:0.103
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9672, entropy=1.2559, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1808
  Round 1/3: Mean predicted reward = 9.702
    Using performance-based weights
    Model weights: rf-m:0.105 rf-l:0.102 gb-m:0.090 gb-l:0.091 xgb-m:0.092 knn-m:0.095 knn-tuned:0.095 svr-rbf:0.114 svr-poly:0.114 ridge:0.103
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9652, entropy=1.2356, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2237
  Round 2/3: Mean predicted reward = 9.602
    Using performance-based weights
    Model weights: rf-m:0.105 rf-l:0.102 gb-m:0.090 gb-l:0.091 xgb-m:0.092 knn-m:0.095 knn-tuned:0.095 svr-rbf:0.114 svr-poly:0.114 ridge:0.103
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9666, entropy=1.2097, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2135
  Round 3/3: Mean predicted reward = 9.883

  === Progress Analysis ===
  Status: NORMAL

--- Round 5 Results ---
  Mean Oracle Reward: 9.919
  Min Oracle Reward: 6.189
  Max Oracle Reward: 11.379
  Std Oracle Reward: 1.220
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: -0.186, Max: 0.062, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 210

======================================================================
EXPERIMENT ROUND 6/100
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
  CCTAAGATGGGC
  CGAACGCTCGTG
  CGAACGTGCAGT
  GGCCAATAGCGT
  GTTGAACCAGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.951
  Max reward: 12.265
  With intrinsic bonuses: 10.027

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=1.1818, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2430

=== Surrogate Model Training ===
Total samples: 242

Training on 230 samples (removed 12 outliers)
Reward range: [6.21, 12.40], mean: 9.74
  Created 11 candidate models for data size 230
Current R2 threshold: -0.3
  rf-m: R2 = -0.070 (std: 0.137)
  rf-l: R2 = -0.044 (std: 0.148)
  gb-m: R2 = -0.109 (std: 0.185)
  gb-l: R2 = -0.105 (std: 0.183)
  xgb-m: R2 = -0.150 (std: 0.180)
  knn-m: R2 = -0.089 (std: 0.113)
  knn-tuned: R2 = -0.089 (std: 0.113)
  mlp-m: R2 = -1.588 (std: 0.883)
  svr-rbf: R2 = 0.007 (std: 0.072)
  svr-poly: R2 = 0.007 (std: 0.072)
  ridge: R2 = -0.119 (std: 0.125)

Model-based training with 10 models
Best R2: 0.007, Mean R2: -0.214
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.101 rf-l:0.103 gb-m:0.097 gb-l:0.097 xgb-m:0.093 knn-m:0.099 knn-tuned:0.099 svr-rbf:0.109 svr-poly:0.109 ridge:0.096
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=1.1623, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2068
  Round 1/3: Mean predicted reward = 9.823
    Using performance-based weights
    Model weights: rf-m:0.101 rf-l:0.103 gb-m:0.097 gb-l:0.097 xgb-m:0.093 knn-m:0.099 knn-tuned:0.099 svr-rbf:0.109 svr-poly:0.109 ridge:0.096
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9621, entropy=1.1370, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2964
  Round 2/3: Mean predicted reward = 9.874
    Using performance-based weights
    Model weights: rf-m:0.101 rf-l:0.103 gb-m:0.097 gb-l:0.097 xgb-m:0.093 knn-m:0.099 knn-tuned:0.099 svr-rbf:0.109 svr-poly:0.109 ridge:0.096
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9639, entropy=1.1069, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3289
  Round 3/3: Mean predicted reward = 9.744

  === Progress Analysis ===
  Status: NORMAL

--- Round 6 Results ---
  Mean Oracle Reward: 9.941
  Min Oracle Reward: 7.267
  Max Oracle Reward: 12.375
  Std Oracle Reward: 1.260
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: -0.214, Max: 0.007, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 242

======================================================================
EXPERIMENT ROUND 7/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.190
Total data collected: 242
  Performance plateaued, reducing LR to 0.000100

--- Round 7 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0100
Exploration rate: 0.190

--- Generated Sequences (Diversity: 1.000) ---
  CGACTGACAGGT
  GGCGTTCAGCAC
  TGTACCCAGGCG
  CCGAGAGGTATC
  CTGATGCGGACC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.730
  Max reward: 11.241
  With intrinsic bonuses: 9.740

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9747, entropy=1.0853, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0811

=== Surrogate Model Training ===
Total samples: 274

Training on 261 samples (removed 13 outliers)
Reward range: [6.21, 12.40], mean: 9.76
  Created 11 candidate models for data size 261
Current R2 threshold: -0.3
  rf-m: R2 = -0.019 (std: 0.111)
  rf-l: R2 = -0.023 (std: 0.090)
  gb-m: R2 = -0.070 (std: 0.104)
  gb-l: R2 = -0.073 (std: 0.104)
  xgb-m: R2 = -0.221 (std: 0.163)
  knn-m: R2 = -0.150 (std: 0.157)
  knn-tuned: R2 = -0.150 (std: 0.157)
  mlp-m: R2 = -0.804 (std: 0.570)
  svr-rbf: R2 = 0.017 (std: 0.051)
  svr-poly: R2 = 0.017 (std: 0.051)
  ridge: R2 = -0.101 (std: 0.059)

Model-based training with 10 models
Best R2: 0.017, Mean R2: -0.143
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.106 rf-l:0.105 gb-m:0.100 gb-l:0.100 xgb-m:0.086 knn-m:0.093 knn-tuned:0.093 svr-rbf:0.110 svr-poly:0.110 ridge:0.097
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9649, entropy=1.0706, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1020
  Round 1/3: Mean predicted reward = 9.756
    Using performance-based weights
    Model weights: rf-m:0.106 rf-l:0.105 gb-m:0.100 gb-l:0.100 xgb-m:0.086 knn-m:0.093 knn-tuned:0.093 svr-rbf:0.110 svr-poly:0.110 ridge:0.097
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=1.0671, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1092
  Round 2/3: Mean predicted reward = 9.809
    Using performance-based weights
    Model weights: rf-m:0.106 rf-l:0.105 gb-m:0.100 gb-l:0.100 xgb-m:0.086 knn-m:0.093 knn-tuned:0.093 svr-rbf:0.110 svr-poly:0.110 ridge:0.097
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9657, entropy=1.0577, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1009
  Round 3/3: Mean predicted reward = 9.914

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 7 Results ---
  Mean Oracle Reward: 9.707
  Min Oracle Reward: 5.260
  Max Oracle Reward: 11.043
  Std Oracle Reward: 1.254
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: -0.143, Max: 0.017, Count: 11
  Total Sequences Evaluated: 274

======================================================================
EXPERIMENT ROUND 8/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.080
Total data collected: 274
  Performance plateaued, reducing LR to 0.000055

--- Round 8 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.080

--- Generated Sequences (Diversity: 1.000) ---
  GCTAGGAATCGC
  CCCAAGGGATTG
  GAACTCCTAGTG
  AGGACCTACGGT
  AACGGCCTTAGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.142
  Max reward: 12.280
  With intrinsic bonuses: 10.226

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9652, entropy=1.0459, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0699

=== Surrogate Model Training ===
Total samples: 306

Training on 293 samples (removed 13 outliers)
Reward range: [6.21, 12.40], mean: 9.80
  Created 11 candidate models for data size 293
Current R2 threshold: -0.3
  rf-m: R2 = 0.020 (std: 0.071)
  rf-l: R2 = 0.025 (std: 0.061)
  gb-m: R2 = -0.053 (std: 0.145)
  gb-l: R2 = -0.053 (std: 0.146)
  xgb-m: R2 = -0.110 (std: 0.220)
  knn-m: R2 = -0.045 (std: 0.123)
  knn-tuned: R2 = -0.045 (std: 0.123)
  mlp-m: R2 = -0.545 (std: 0.294)
  svr-rbf: R2 = 0.030 (std: 0.059)
  svr-poly: R2 = 0.030 (std: 0.059)
  ridge: R2 = -0.070 (std: 0.023)

Model-based training with 10 models
Best R2: 0.030, Mean R2: -0.074
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.105 rf-l:0.105 gb-m:0.097 gb-l:0.097 xgb-m:0.092 knn-m:0.098 knn-tuned:0.098 svr-rbf:0.106 svr-poly:0.106 ridge:0.096
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9633, entropy=1.0485, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0746
  Round 1/3: Mean predicted reward = 9.912
    Using performance-based weights
    Model weights: rf-m:0.105 rf-l:0.105 gb-m:0.097 gb-l:0.097 xgb-m:0.092 knn-m:0.098 knn-tuned:0.098 svr-rbf:0.106 svr-poly:0.106 ridge:0.096
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9632, entropy=1.0462, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0799
  Round 2/3: Mean predicted reward = 9.868
    Using performance-based weights
    Model weights: rf-m:0.105 rf-l:0.105 gb-m:0.097 gb-l:0.097 xgb-m:0.092 knn-m:0.098 knn-tuned:0.098 svr-rbf:0.106 svr-poly:0.106 ridge:0.096
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9655, entropy=1.0357, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0770
  Round 3/3: Mean predicted reward = 9.951

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 8 Results ---
  Mean Oracle Reward: 10.169
  Min Oracle Reward: 7.853
  Max Oracle Reward: 12.547
  Std Oracle Reward: 1.164
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: -0.074, Max: 0.030, Count: 11
  New best mean reward!
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
  AGCCGAGTGTCA
  CGCCATGAGTGC
  ACTGGATCGCCG
  GAGACGCATTCG
  GTCGCGCCATAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.966
  Max reward: 12.163
  With intrinsic bonuses: 10.007

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9665, entropy=1.0272, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0537

=== Surrogate Model Training ===
Total samples: 338

Training on 324 samples (removed 14 outliers)
Reward range: [6.21, 12.40], mean: 9.84
  Created 14 candidate models for data size 324
Current R2 threshold: -0.3
  rf-tuned-l: R2 = 0.055 (std: 0.061)
  rf-tuned-xl: R2 = 0.039 (std: 0.046)
  gb-tuned-l: R2 = -0.041 (std: 0.105)
  gb-tuned-xl: R2 = -0.040 (std: 0.105)
  xgb-xl: R2 = -0.119 (std: 0.167)
  xgb-l: R2 = -0.119 (std: 0.167)
  mlp-adaptive-xl: R2 = -0.391 (std: 0.346)
  mlp-l: R2 = -0.521 (std: 0.308)
  svr-rbf-xl: R2 = 0.066 (std: 0.032)
  svr-poly-l: R2 = 0.066 (std: 0.032)
  knn-tuned-sqrt: R2 = -0.034 (std: 0.062)
  knn-tuned-l: R2 = -0.034 (std: 0.062)
  ridge: R2 = -0.066 (std: 0.029)
  gp: R2 = -67.925 (std: 17.341)

Model-based training with 11 models
Best R2: 0.066, Mean R2: -4.933
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.096 gb-tuned-l:0.089 gb-tuned-xl:0.089 xgb-xl:0.082 xgb-l:0.082 svr-rbf-xl:0.099 svr-poly-l:0.099 knn-tuned-sqrt:0.090 knn-tuned-l:0.090 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9639, entropy=1.0202, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0616
  Round 1/3: Mean predicted reward = 10.033
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.096 gb-tuned-l:0.089 gb-tuned-xl:0.089 xgb-xl:0.082 xgb-l:0.082 svr-rbf-xl:0.099 svr-poly-l:0.099 knn-tuned-sqrt:0.090 knn-tuned-l:0.090 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9730, entropy=1.0217, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0525
  Round 2/3: Mean predicted reward = 9.950
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.096 gb-tuned-l:0.089 gb-tuned-xl:0.089 xgb-xl:0.082 xgb-l:0.082 svr-rbf-xl:0.099 svr-poly-l:0.099 knn-tuned-sqrt:0.090 knn-tuned-l:0.090 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9637, entropy=1.0167, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0567
  Round 3/3: Mean predicted reward = 10.020

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 9 Results ---
  Mean Oracle Reward: 10.046
  Min Oracle Reward: 5.090
  Max Oracle Reward: 12.461
  Std Oracle Reward: 1.688
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -4.933, Max: 0.066, Count: 14
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
  TCCCGTAAGTGA
  AGTGGACCCTAG
  CACGTCGCGATG
  TGAGAGCGATCC
  GTACCTAGCGAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.939
  Max reward: 12.274
  With intrinsic bonuses: 9.902

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9663, entropy=1.0130, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4185

=== Surrogate Model Training ===
Total samples: 370

Training on 355 samples (removed 15 outliers)
Reward range: [6.48, 12.40], mean: 9.86
  Created 14 candidate models for data size 355
Current R2 threshold: -0.3
  rf-tuned-l: R2 = 0.075 (std: 0.112)
  rf-tuned-xl: R2 = 0.088 (std: 0.082)
  gb-tuned-l: R2 = 0.034 (std: 0.074)
  gb-tuned-xl: R2 = 0.035 (std: 0.074)
  xgb-xl: R2 = -0.137 (std: 0.264)
  xgb-l: R2 = -0.137 (std: 0.264)
  mlp-adaptive-xl: R2 = -0.462 (std: 0.375)
  mlp-l: R2 = -0.409 (std: 0.336)
  svr-rbf-xl: R2 = 0.104 (std: 0.088)
  svr-poly-l: R2 = 0.104 (std: 0.088)
  knn-tuned-sqrt: R2 = 0.021 (std: 0.146)
  knn-tuned-l: R2 = 0.021 (std: 0.146)
  ridge: R2 = -0.043 (std: 0.052)
  gp: R2 = -67.775 (std: 14.962)

Model-based training with 11 models
Best R2: 0.104, Mean R2: -4.891
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.096 rf-tuned-xl:0.097 gb-tuned-l:0.092 gb-tuned-xl:0.092 xgb-xl:0.078 xgb-l:0.078 svr-rbf-xl:0.099 svr-poly-l:0.099 knn-tuned-sqrt:0.091 knn-tuned-l:0.091 ridge:0.086
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9611, entropy=0.9839, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4658
  Round 1/3: Mean predicted reward = 10.015
    Using performance-based weights
    Model weights: rf-tuned-l:0.096 rf-tuned-xl:0.097 gb-tuned-l:0.092 gb-tuned-xl:0.092 xgb-xl:0.078 xgb-l:0.078 svr-rbf-xl:0.099 svr-poly-l:0.099 knn-tuned-sqrt:0.091 knn-tuned-l:0.091 ridge:0.086
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9646, entropy=0.9374, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5699
  Round 2/3: Mean predicted reward = 9.858
    Using performance-based weights
    Model weights: rf-tuned-l:0.096 rf-tuned-xl:0.097 gb-tuned-l:0.092 gb-tuned-xl:0.092 xgb-xl:0.078 xgb-l:0.078 svr-rbf-xl:0.099 svr-poly-l:0.099 knn-tuned-sqrt:0.091 knn-tuned-l:0.091 ridge:0.086
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9568, entropy=0.9124, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6218
  Round 3/3: Mean predicted reward = 10.005

  === Progress Analysis ===
  Status: NORMAL

--- Round 10 Results ---
  Mean Oracle Reward: 9.951
  Min Oracle Reward: 7.280
  Max Oracle Reward: 12.143
  Std Oracle Reward: 1.158
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -4.891, Max: 0.104, Count: 14
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
  GAACCGGATGTC
  CTTCGACGCAGG
  TTAGCAAGGCGC
  GAAGTCACTGCG
  CGCCCAGTGTGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.169
  Max reward: 12.450
  With intrinsic bonuses: 10.084

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.8719, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3259

=== Surrogate Model Training ===
Total samples: 402

Training on 386 samples (removed 16 outliers)
Reward range: [6.72, 12.51], mean: 9.89
  Created 14 candidate models for data size 386
Current R2 threshold: -0.29
  rf-tuned-l: R2 = 0.073 (std: 0.058)
  rf-tuned-xl: R2 = 0.096 (std: 0.049)
  gb-tuned-l: R2 = 0.007 (std: 0.032)
  gb-tuned-xl: R2 = 0.007 (std: 0.032)
  xgb-xl: R2 = -0.052 (std: 0.116)
  xgb-l: R2 = -0.052 (std: 0.116)
  mlp-adaptive-xl: R2 = -0.504 (std: 0.298)
  mlp-l: R2 = -0.223 (std: 0.344)
  svr-rbf-xl: R2 = 0.078 (std: 0.043)
  svr-poly-l: R2 = 0.078 (std: 0.043)
  knn-tuned-sqrt: R2 = -0.021 (std: 0.085)
  knn-tuned-l: R2 = -0.021 (std: 0.085)
  ridge: R2 = -0.038 (std: 0.043)
  gp: R2 = -72.519 (std: 15.356)

Model-based training with 12 models
Best R2: 0.096, Mean R2: -5.221
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.090 rf-tuned-xl:0.092 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.079 xgb-l:0.079 mlp-l:0.067 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.082 knn-tuned-l:0.082 ridge:0.080
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9656, entropy=0.8603, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3635
  Round 1/3: Mean predicted reward = 9.980
    Using performance-based weights
    Model weights: rf-tuned-l:0.090 rf-tuned-xl:0.092 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.079 xgb-l:0.079 mlp-l:0.067 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.082 knn-tuned-l:0.082 ridge:0.080
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9667, entropy=0.8484, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4051
  Round 2/3: Mean predicted reward = 9.928
    Using performance-based weights
    Model weights: rf-tuned-l:0.090 rf-tuned-xl:0.092 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.079 xgb-l:0.079 mlp-l:0.067 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.082 knn-tuned-l:0.082 ridge:0.080
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9630, entropy=0.8323, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4507
  Round 3/3: Mean predicted reward = 9.884

  === Progress Analysis ===
  Status: NORMAL

--- Round 11 Results ---
  Mean Oracle Reward: 10.131
  Min Oracle Reward: 7.792
  Max Oracle Reward: 12.590
  Std Oracle Reward: 0.995
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: -5.221, Max: 0.096, Count: 14
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
  TGCCCGCGTAAG
  AGCGGTCCTGAA
  ATGCAGCAGTGC
  CTGCTAGGAGCC
  CAGTACCCTGGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.808
  Max reward: 12.397
  With intrinsic bonuses: 9.845

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9623, entropy=0.8237, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5902

=== Surrogate Model Training ===
Total samples: 434

Training on 415 samples (removed 19 outliers)
Reward range: [6.80, 12.51], mean: 9.91
  Created 14 candidate models for data size 415
Current R2 threshold: -0.27999999999999997
  rf-tuned-l: R2 = 0.057 (std: 0.058)
  rf-tuned-xl: R2 = 0.058 (std: 0.042)
  gb-tuned-l: R2 = 0.023 (std: 0.087)
  gb-tuned-xl: R2 = 0.024 (std: 0.088)
  xgb-xl: R2 = -0.086 (std: 0.150)
  xgb-l: R2 = -0.086 (std: 0.150)
  mlp-adaptive-xl: R2 = -0.410 (std: 0.433)
  mlp-l: R2 = -0.439 (std: 0.183)
  svr-rbf-xl: R2 = 0.054 (std: 0.068)
  svr-poly-l: R2 = 0.054 (std: 0.068)
  knn-tuned-sqrt: R2 = -0.053 (std: 0.114)
  knn-tuned-l: R2 = -0.053 (std: 0.114)
  ridge: R2 = -0.054 (std: 0.058)
  gp: R2 = -75.304 (std: 14.697)

Model-based training with 11 models
Best R2: 0.058, Mean R2: -5.444
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.097 rf-tuned-xl:0.097 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.084 xgb-l:0.084 svr-rbf-xl:0.096 svr-poly-l:0.096 knn-tuned-sqrt:0.087 knn-tuned-l:0.087 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.7944, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6829
  Round 1/3: Mean predicted reward = 10.059
    Using performance-based weights
    Model weights: rf-tuned-l:0.097 rf-tuned-xl:0.097 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.084 xgb-l:0.084 svr-rbf-xl:0.096 svr-poly-l:0.096 knn-tuned-sqrt:0.087 knn-tuned-l:0.087 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.7762, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7582
  Round 2/3: Mean predicted reward = 9.893
    Using performance-based weights
    Model weights: rf-tuned-l:0.097 rf-tuned-xl:0.097 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.084 xgb-l:0.084 svr-rbf-xl:0.096 svr-poly-l:0.096 knn-tuned-sqrt:0.087 knn-tuned-l:0.087 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9629, entropy=0.7493, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7054
  Round 3/3: Mean predicted reward = 9.874

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 12 Results ---
  Mean Oracle Reward: 9.818
  Min Oracle Reward: 4.070
  Max Oracle Reward: 12.217
  Std Oracle Reward: 1.514
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -5.444, Max: 0.058, Count: 14
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
  CCCACGTGTGGA
  TGCCAGTGAACG
  TGCACAGCAGGT
  ACTCGGCGAGAT
  GGGTATCACCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.373
  Max reward: 12.402
  With intrinsic bonuses: 9.408

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9700, entropy=0.7286, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3136

=== Surrogate Model Training ===
Total samples: 466

Training on 449 samples (removed 17 outliers)
Reward range: [6.48, 12.51], mean: 9.86
  Created 14 candidate models for data size 449
Current R2 threshold: -0.27
  rf-tuned-l: R2 = 0.020 (std: 0.090)
  rf-tuned-xl: R2 = 0.041 (std: 0.062)
  gb-tuned-l: R2 = 0.010 (std: 0.104)
  gb-tuned-xl: R2 = 0.009 (std: 0.104)
  xgb-xl: R2 = -0.157 (std: 0.192)
  xgb-l: R2 = -0.157 (std: 0.192)
  mlp-adaptive-xl: R2 = -0.558 (std: 0.182)
  mlp-l: R2 = -0.378 (std: 0.180)
  svr-rbf-xl: R2 = 0.008 (std: 0.074)
  svr-poly-l: R2 = 0.008 (std: 0.074)
  knn-tuned-sqrt: R2 = -0.063 (std: 0.092)
  knn-tuned-l: R2 = -0.063 (std: 0.092)
  ridge: R2 = -0.071 (std: 0.035)
  gp: R2 = -68.538 (std: 19.393)

Model-based training with 11 models
Best R2: 0.041, Mean R2: -4.992
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.096 rf-tuned-xl:0.098 gb-tuned-l:0.095 gb-tuned-xl:0.095 xgb-xl:0.081 xgb-l:0.081 svr-rbf-xl:0.095 svr-poly-l:0.095 knn-tuned-sqrt:0.088 knn-tuned-l:0.088 ridge:0.088
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9660, entropy=0.7157, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2911
  Round 1/3: Mean predicted reward = 9.570
    Using performance-based weights
    Model weights: rf-tuned-l:0.096 rf-tuned-xl:0.098 gb-tuned-l:0.095 gb-tuned-xl:0.095 xgb-xl:0.081 xgb-l:0.081 svr-rbf-xl:0.095 svr-poly-l:0.095 knn-tuned-sqrt:0.088 knn-tuned-l:0.088 ridge:0.088
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.7128, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2266
  Round 2/3: Mean predicted reward = 9.800
    Using performance-based weights
    Model weights: rf-tuned-l:0.096 rf-tuned-xl:0.098 gb-tuned-l:0.095 gb-tuned-xl:0.095 xgb-xl:0.081 xgb-l:0.081 svr-rbf-xl:0.095 svr-poly-l:0.095 knn-tuned-sqrt:0.088 knn-tuned-l:0.088 ridge:0.088
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9649, entropy=0.7037, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2860
  Round 3/3: Mean predicted reward = 9.921

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 13 Results ---
  Mean Oracle Reward: 9.316
  Min Oracle Reward: 6.140
  Max Oracle Reward: 12.160
  Std Oracle Reward: 1.573
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -4.992, Max: 0.041, Count: 14
  Total Sequences Evaluated: 466

======================================================================
EXPERIMENT ROUND 14/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 466

--- Round 14 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGGCAGTTGCAC
  GGTCCCTCAAGG
  CGCCCGGAATTG
  TCGCAAGTCATG
  AGGCTACGCCTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.898
  Max reward: 12.204
  With intrinsic bonuses: 9.943

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9646, entropy=0.7182, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0550

=== Surrogate Model Training ===
Total samples: 498

Training on 479 samples (removed 19 outliers)
Reward range: [6.72, 12.54], mean: 9.87
  Created 14 candidate models for data size 479
Current R2 threshold: -0.26
  rf-tuned-l: R2 = 0.015 (std: 0.113)
  rf-tuned-xl: R2 = 0.004 (std: 0.131)
  gb-tuned-l: R2 = -0.012 (std: 0.127)
  gb-tuned-xl: R2 = -0.014 (std: 0.126)
  xgb-xl: R2 = -0.229 (std: 0.281)
  xgb-l: R2 = -0.229 (std: 0.281)
  mlp-adaptive-xl: R2 = -0.573 (std: 0.305)
  mlp-l: R2 = -0.368 (std: 0.192)
  svr-rbf-xl: R2 = 0.029 (std: 0.108)
  svr-poly-l: R2 = 0.029 (std: 0.108)
  knn-tuned-sqrt: R2 = -0.120 (std: 0.152)
  knn-tuned-l: R2 = -0.120 (std: 0.152)
  ridge: R2 = -0.056 (std: 0.035)
  gp: R2 = -72.554 (std: 21.713)

Model-based training with 11 models
Best R2: 0.029, Mean R2: -5.300
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.097 gb-tuned-l:0.095 gb-tuned-xl:0.095 xgb-xl:0.077 xgb-l:0.077 svr-rbf-xl:0.099 svr-poly-l:0.099 knn-tuned-sqrt:0.086 knn-tuned-l:0.086 ridge:0.091
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9702, entropy=0.7122, kl_div=0.0000
    Epoch 1: policy_loss=0.0020, value_loss=0.9702, entropy=0.7126, kl_div=0.0270
  Round 1/3: Mean predicted reward = 9.829
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.097 gb-tuned-l:0.095 gb-tuned-xl:0.095 xgb-xl:0.077 xgb-l:0.077 svr-rbf-xl:0.099 svr-poly-l:0.099 knn-tuned-sqrt:0.086 knn-tuned-l:0.086 ridge:0.091
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.7158, kl_div=0.0000
    Epoch 1: policy_loss=-0.0105, value_loss=0.9692, entropy=0.7172, kl_div=-0.0099
  Round 2/3: Mean predicted reward = 9.944
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.097 gb-tuned-l:0.095 gb-tuned-xl:0.095 xgb-xl:0.077 xgb-l:0.077 svr-rbf-xl:0.099 svr-poly-l:0.099 knn-tuned-sqrt:0.086 knn-tuned-l:0.086 ridge:0.091
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9651, entropy=0.7055, kl_div=0.0000
    Epoch 1: policy_loss=-0.0083, value_loss=0.9651, entropy=0.7066, kl_div=-0.0093
  Round 3/3: Mean predicted reward = 9.879

  === Progress Analysis ===
  Status: NORMAL

--- Round 14 Results ---
  Mean Oracle Reward: 9.976
  Min Oracle Reward: 8.178
  Max Oracle Reward: 12.427
  Std Oracle Reward: 0.935
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -5.300, Max: 0.029, Count: 14
  Total Sequences Evaluated: 498

======================================================================
EXPERIMENT ROUND 15/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 498

--- Round 15 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCGGAGCCATGA
  ATCCGTAGGCGC
  CAGACTTCGAGG
  AGCGGACGCCTT
  ATCGCGGCATCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.144
  Max reward: 13.289
  With intrinsic bonuses: 10.153

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9632, entropy=0.7243, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0968

=== Surrogate Model Training ===
Total samples: 530

Training on 509 samples (removed 21 outliers)
Reward range: [6.72, 12.54], mean: 9.89
  Created 13 candidate models for data size 509
Current R2 threshold: -0.25
  rf-tuned-l: R2 = 0.038 (std: 0.120)
  rf-tuned-xl: R2 = 0.021 (std: 0.106)
  gb-tuned-l: R2 = 0.057 (std: 0.113)
  gb-tuned-xl: R2 = 0.057 (std: 0.113)
  xgb-xl: R2 = -0.103 (std: 0.203)
  xgb-l: R2 = -0.103 (std: 0.203)
  mlp-adaptive-xl: R2 = -0.296 (std: 0.149)
  mlp-l: R2 = -0.404 (std: 0.153)
  svr-rbf-xl: R2 = 0.056 (std: 0.089)
  svr-poly-l: R2 = 0.056 (std: 0.089)
  knn-tuned-sqrt: R2 = -0.087 (std: 0.119)
  knn-tuned-l: R2 = -0.087 (std: 0.119)
  ridge: R2 = -0.050 (std: 0.033)

Model-based training with 11 models
Best R2: 0.057, Mean R2: -0.065
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.095 rf-tuned-xl:0.094 gb-tuned-l:0.097 gb-tuned-xl:0.097 xgb-xl:0.083 xgb-l:0.083 svr-rbf-xl:0.097 svr-poly-l:0.097 knn-tuned-sqrt:0.084 knn-tuned-l:0.084 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.7217, kl_div=0.0000
    Epoch 1: policy_loss=-0.0288, value_loss=0.9685, entropy=0.7265, kl_div=0.0306
  Round 1/3: Mean predicted reward = 9.837
    Using performance-based weights
    Model weights: rf-tuned-l:0.095 rf-tuned-xl:0.094 gb-tuned-l:0.097 gb-tuned-xl:0.097 xgb-xl:0.083 xgb-l:0.083 svr-rbf-xl:0.097 svr-poly-l:0.097 knn-tuned-sqrt:0.084 knn-tuned-l:0.084 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9663, entropy=0.7313, kl_div=0.0000
    Epoch 1: policy_loss=0.0105, value_loss=0.9663, entropy=0.7326, kl_div=-0.1890
  Round 2/3: Mean predicted reward = 9.824
    Using performance-based weights
    Model weights: rf-tuned-l:0.095 rf-tuned-xl:0.094 gb-tuned-l:0.097 gb-tuned-xl:0.097 xgb-xl:0.083 xgb-l:0.083 svr-rbf-xl:0.097 svr-poly-l:0.097 knn-tuned-sqrt:0.084 knn-tuned-l:0.084 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.7280, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1636
  Round 3/3: Mean predicted reward = 10.087

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 15 Results ---
  Mean Oracle Reward: 10.107
  Min Oracle Reward: 4.446
  Max Oracle Reward: 13.153
  Std Oracle Reward: 1.534
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -0.065, Max: 0.057, Count: 13
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
  ATAAGGGTGCCC
  GCGACCCGTAGT
  ATCCGGCAGTCG
  GACGGCTCGTAC
  TAATCGGGGCCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.853
  Max reward: 11.601
  With intrinsic bonuses: 9.803

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9743, entropy=0.7240, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1161

=== Surrogate Model Training ===
Total samples: 562

Training on 540 samples (removed 22 outliers)
Reward range: [6.72, 12.54], mean: 9.90
  Created 13 candidate models for data size 540
Current R2 threshold: -0.24
  rf-tuned-l: R2 = 0.050 (std: 0.062)
  rf-tuned-xl: R2 = 0.066 (std: 0.084)
  gb-tuned-l: R2 = 0.081 (std: 0.077)
  gb-tuned-xl: R2 = 0.081 (std: 0.077)
  xgb-xl: R2 = -0.153 (std: 0.200)
  xgb-l: R2 = -0.153 (std: 0.200)
  mlp-adaptive-xl: R2 = -0.189 (std: 0.121)
  mlp-l: R2 = -0.235 (std: 0.230)
  svr-rbf-xl: R2 = 0.068 (std: 0.070)
  svr-poly-l: R2 = 0.068 (std: 0.070)
  knn-tuned-sqrt: R2 = -0.057 (std: 0.116)
  knn-tuned-l: R2 = -0.057 (std: 0.116)
  ridge: R2 = -0.033 (std: 0.039)

Model-based training with 13 models
Best R2: 0.081, Mean R2: -0.035
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.085 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.066 mlp-l:0.063 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.077
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9666, entropy=0.7162, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2541
  Round 1/3: Mean predicted reward = 9.822
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.085 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.066 mlp-l:0.063 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.077
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9717, entropy=0.7288, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2214
  Round 2/3: Mean predicted reward = 9.882
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.085 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.066 mlp-l:0.063 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.077
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9634, entropy=0.7103, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1880
  Round 3/3: Mean predicted reward = 9.889

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 16 Results ---
  Mean Oracle Reward: 9.839
  Min Oracle Reward: 2.569
  Max Oracle Reward: 11.687
  Std Oracle Reward: 1.680
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.035, Max: 0.081, Count: 13
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
  GGCTTAGGACCC
  ACGGCTCAGTGC
  CCCTTGCGAAGG
  CCTACAGGGGCT
  TAGATCGCGCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.741
  Max reward: 11.928
  With intrinsic bonuses: 9.752

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9734, entropy=0.6858, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1521

=== Surrogate Model Training ===
Total samples: 594

Training on 571 samples (removed 23 outliers)
Reward range: [6.72, 12.54], mean: 9.90
  Created 13 candidate models for data size 571
Current R2 threshold: -0.22999999999999998
  rf-tuned-l: R2 = 0.066 (std: 0.079)
  rf-tuned-xl: R2 = 0.051 (std: 0.101)
  gb-tuned-l: R2 = 0.048 (std: 0.092)
  gb-tuned-xl: R2 = 0.048 (std: 0.092)
  xgb-xl: R2 = -0.124 (std: 0.179)
  xgb-l: R2 = -0.124 (std: 0.179)
  mlp-adaptive-xl: R2 = -0.176 (std: 0.165)
  mlp-l: R2 = -0.168 (std: 0.160)
  svr-rbf-xl: R2 = 0.053 (std: 0.053)
  svr-poly-l: R2 = 0.053 (std: 0.053)
  knn-tuned-sqrt: R2 = -0.020 (std: 0.097)
  knn-tuned-l: R2 = -0.020 (std: 0.097)
  ridge: R2 = -0.037 (std: 0.035)

Model-based training with 13 models
Best R2: 0.066, Mean R2: -0.027
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.084 rf-tuned-xl:0.083 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.066 mlp-l:0.067 svr-rbf-xl:0.083 svr-poly-l:0.083 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9664, entropy=0.6866, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2533
  Round 1/3: Mean predicted reward = 9.981
    Using performance-based weights
    Model weights: rf-tuned-l:0.084 rf-tuned-xl:0.083 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.066 mlp-l:0.067 svr-rbf-xl:0.083 svr-poly-l:0.083 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.6923, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2996
  Round 2/3: Mean predicted reward = 9.841
    Using performance-based weights
    Model weights: rf-tuned-l:0.084 rf-tuned-xl:0.083 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.066 mlp-l:0.067 svr-rbf-xl:0.083 svr-poly-l:0.083 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.6922, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4736
  Round 3/3: Mean predicted reward = 9.853

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 17 Results ---
  Mean Oracle Reward: 9.761
  Min Oracle Reward: 6.406
  Max Oracle Reward: 11.668
  Std Oracle Reward: 1.410
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.027, Max: 0.066, Count: 13
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
  GTCGCCAGCGTA
  AGTGGCTCCCGA
  GGATCCACCGGT
  AGGCGGCTCTAC
  AACTGCGCTGGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.791
  Max reward: 13.452
  With intrinsic bonuses: 9.770

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9776, entropy=0.6924, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1361

=== Surrogate Model Training ===
Total samples: 626

Training on 602 samples (removed 24 outliers)
Reward range: [6.72, 13.22], mean: 9.92
  Created 13 candidate models for data size 602
Current R2 threshold: -0.21999999999999997
  rf-tuned-l: R2 = 0.022 (std: 0.026)
  rf-tuned-xl: R2 = 0.008 (std: 0.034)
  gb-tuned-l: R2 = 0.043 (std: 0.081)
  gb-tuned-xl: R2 = 0.043 (std: 0.081)
  xgb-xl: R2 = -0.125 (std: 0.080)
  xgb-l: R2 = -0.125 (std: 0.080)
  mlp-adaptive-xl: R2 = -0.216 (std: 0.165)
  mlp-l: R2 = -0.241 (std: 0.279)
  svr-rbf-xl: R2 = 0.030 (std: 0.079)
  svr-poly-l: R2 = 0.030 (std: 0.079)
  knn-tuned-sqrt: R2 = -0.106 (std: 0.083)
  knn-tuned-l: R2 = -0.106 (std: 0.083)
  ridge: R2 = -0.061 (std: 0.043)

Model-based training with 12 models
Best R2: 0.043, Mean R2: -0.062
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.089 rf-tuned-xl:0.088 gb-tuned-l:0.091 gb-tuned-xl:0.091 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.070 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.082
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.6795, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0680
  Round 1/3: Mean predicted reward = 9.880
    Using performance-based weights
    Model weights: rf-tuned-l:0.089 rf-tuned-xl:0.088 gb-tuned-l:0.091 gb-tuned-xl:0.091 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.070 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.082
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.6741, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1098
  Round 2/3: Mean predicted reward = 9.824
    Using performance-based weights
    Model weights: rf-tuned-l:0.089 rf-tuned-xl:0.088 gb-tuned-l:0.091 gb-tuned-xl:0.091 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.070 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.082
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.6770, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1200
  Round 3/3: Mean predicted reward = 9.817

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 18 Results ---
  Mean Oracle Reward: 9.812
  Min Oracle Reward: 3.404
  Max Oracle Reward: 13.502
  Std Oracle Reward: 1.861
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: -0.062, Max: 0.043, Count: 13
  Total Sequences Evaluated: 626

======================================================================
EXPERIMENT ROUND 19/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 626
  Performance plateaued, reducing LR to 0.000019

--- Round 19 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCGGTACACGCG
  CCGAGATGGCCT
  AGTGAGGCCTCC
  CACGCTGAGGTC
  ACTGAGGATGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.869
  Max reward: 12.169
  With intrinsic bonuses: 9.919

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9724, entropy=0.6742, kl_div=0.0000
    Epoch 1: policy_loss=-0.0068, value_loss=0.9724, entropy=0.6746, kl_div=0.0174

=== Surrogate Model Training ===
Total samples: 658

Training on 633 samples (removed 25 outliers)
Reward range: [6.72, 13.22], mean: 9.92
  Created 13 candidate models for data size 633
Current R2 threshold: -0.21
  rf-tuned-l: R2 = 0.019 (std: 0.056)
  rf-tuned-xl: R2 = 0.053 (std: 0.060)
  gb-tuned-l: R2 = 0.048 (std: 0.101)
  gb-tuned-xl: R2 = 0.048 (std: 0.101)
  xgb-xl: R2 = -0.157 (std: 0.065)
  xgb-l: R2 = -0.157 (std: 0.065)
  mlp-adaptive-xl: R2 = -0.206 (std: 0.205)
  mlp-l: R2 = -0.244 (std: 0.175)
  svr-rbf-xl: R2 = 0.067 (std: 0.064)
  svr-poly-l: R2 = 0.067 (std: 0.064)
  knn-tuned-sqrt: R2 = -0.058 (std: 0.029)
  knn-tuned-l: R2 = -0.058 (std: 0.029)
  ridge: R2 = -0.053 (std: 0.037)

Model-based training with 12 models
Best R2: 0.067, Mean R2: -0.049
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.087 rf-tuned-xl:0.090 gb-tuned-l:0.090 gb-tuned-xl:0.090 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.070 svr-rbf-xl:0.092 svr-poly-l:0.092 knn-tuned-sqrt:0.081 knn-tuned-l:0.081 ridge:0.081
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.6929, kl_div=0.0000
    Epoch 1: policy_loss=-0.0123, value_loss=0.9690, entropy=0.6938, kl_div=0.0124
  Round 1/3: Mean predicted reward = 9.821
    Using performance-based weights
    Model weights: rf-tuned-l:0.087 rf-tuned-xl:0.090 gb-tuned-l:0.090 gb-tuned-xl:0.090 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.070 svr-rbf-xl:0.092 svr-poly-l:0.092 knn-tuned-sqrt:0.081 knn-tuned-l:0.081 ridge:0.081
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9604, entropy=0.6726, kl_div=0.0000
    Epoch 1: policy_loss=-0.0063, value_loss=0.9604, entropy=0.6734, kl_div=0.0100
  Round 2/3: Mean predicted reward = 9.809
    Using performance-based weights
    Model weights: rf-tuned-l:0.087 rf-tuned-xl:0.090 gb-tuned-l:0.090 gb-tuned-xl:0.090 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.070 svr-rbf-xl:0.092 svr-poly-l:0.092 knn-tuned-sqrt:0.081 knn-tuned-l:0.081 ridge:0.081
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.6710, kl_div=0.0000
    Epoch 1: policy_loss=-0.0222, value_loss=0.9698, entropy=0.6711, kl_div=0.0356
  Round 3/3: Mean predicted reward = 9.955

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 19 Results ---
  Mean Oracle Reward: 9.910
  Min Oracle Reward: 5.020
  Max Oracle Reward: 12.431
  Std Oracle Reward: 1.568
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: -0.049, Max: 0.067, Count: 13
  Total Sequences Evaluated: 658

======================================================================
EXPERIMENT ROUND 20/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 658
  Performance plateaued, reducing LR to 0.000150

--- Round 20 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGCGGACAGCCT
  CAGTACCGTGCG
  AGACCTCGGTGC
  GGACACCTCGGT
  AAGCTGCTGGCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.829
  Max reward: 11.466
  With intrinsic bonuses: 9.832

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9719, entropy=0.6685, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3187

=== Surrogate Model Training ===
Total samples: 690

Training on 664 samples (removed 26 outliers)
Reward range: [6.72, 13.22], mean: 9.93
  Created 13 candidate models for data size 664
Current R2 threshold: -0.19999999999999998
  rf-tuned-l: R2 = 0.043 (std: 0.066)
  rf-tuned-xl: R2 = 0.045 (std: 0.071)
  gb-tuned-l: R2 = 0.070 (std: 0.108)
  gb-tuned-xl: R2 = 0.070 (std: 0.108)
  xgb-xl: R2 = -0.075 (std: 0.103)
  xgb-l: R2 = -0.075 (std: 0.103)
  mlp-adaptive-xl: R2 = -0.191 (std: 0.227)
  mlp-l: R2 = -0.196 (std: 0.201)
  svr-rbf-xl: R2 = 0.066 (std: 0.074)
  svr-poly-l: R2 = 0.066 (std: 0.074)
  knn-tuned-sqrt: R2 = -0.058 (std: 0.037)
  knn-tuned-l: R2 = -0.058 (std: 0.037)
  ridge: R2 = -0.045 (std: 0.035)

Model-based training with 13 models
Best R2: 0.070, Mean R2: -0.026
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.082 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.065 mlp-l:0.065 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9741, entropy=0.6777, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2331
  Round 1/3: Mean predicted reward = 9.764
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.082 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.065 mlp-l:0.065 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9635, entropy=0.6981, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2363
  Round 2/3: Mean predicted reward = 9.951
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.082 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.065 mlp-l:0.065 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.6996, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3449
  Round 3/3: Mean predicted reward = 9.857

  === Progress Analysis ===
  Status: NORMAL

--- Round 20 Results ---
  Mean Oracle Reward: 9.845
  Min Oracle Reward: 6.108
  Max Oracle Reward: 11.345
  Std Oracle Reward: 1.241
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.026, Max: 0.070, Count: 13
  Total Sequences Evaluated: 690

======================================================================
EXPERIMENT ROUND 21/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 690
  Performance plateaued, reducing LR to 0.000136

--- Round 21 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ATCGCGGAGATC
  CCGCGATGGTAC
  ACCCGGGTCGAT
  TCCGGAGAGATC
  GTCACGATGACG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.109
  Max reward: 11.733
  With intrinsic bonuses: 10.118

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9713, entropy=0.6881, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2101

=== Surrogate Model Training ===
Total samples: 722

Training on 696 samples (removed 26 outliers)
Reward range: [6.72, 13.22], mean: 9.93
  Created 13 candidate models for data size 696
Current R2 threshold: -0.19
  rf-tuned-l: R2 = 0.069 (std: 0.100)
  rf-tuned-xl: R2 = 0.042 (std: 0.091)
  gb-tuned-l: R2 = 0.078 (std: 0.084)
  gb-tuned-xl: R2 = 0.079 (std: 0.082)
  xgb-xl: R2 = -0.109 (std: 0.147)
  xgb-l: R2 = -0.109 (std: 0.147)
  mlp-adaptive-xl: R2 = -0.122 (std: 0.225)
  mlp-l: R2 = -0.224 (std: 0.197)
  svr-rbf-xl: R2 = 0.084 (std: 0.068)
  svr-poly-l: R2 = 0.084 (std: 0.068)
  knn-tuned-sqrt: R2 = -0.043 (std: 0.065)
  knn-tuned-l: R2 = -0.043 (std: 0.065)
  ridge: R2 = -0.038 (std: 0.034)

Model-based training with 12 models
Best R2: 0.084, Mean R2: -0.019
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.089 rf-tuned-xl:0.087 gb-tuned-l:0.090 gb-tuned-xl:0.090 xgb-xl:0.075 xgb-l:0.075 mlp-adaptive-xl:0.074 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.080 knn-tuned-l:0.080 ridge:0.080
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.6802, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2902
  Round 1/3: Mean predicted reward = 9.563
    Using performance-based weights
    Model weights: rf-tuned-l:0.089 rf-tuned-xl:0.087 gb-tuned-l:0.090 gb-tuned-xl:0.090 xgb-xl:0.075 xgb-l:0.075 mlp-adaptive-xl:0.074 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.080 knn-tuned-l:0.080 ridge:0.080
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9714, entropy=0.6825, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3144
  Round 2/3: Mean predicted reward = 10.016
    Using performance-based weights
    Model weights: rf-tuned-l:0.089 rf-tuned-xl:0.087 gb-tuned-l:0.090 gb-tuned-xl:0.090 xgb-xl:0.075 xgb-l:0.075 mlp-adaptive-xl:0.074 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.080 knn-tuned-l:0.080 ridge:0.080
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.6944, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2178
  Round 3/3: Mean predicted reward = 10.015

  === Progress Analysis ===
  Status: NORMAL

--- Round 21 Results ---
  Mean Oracle Reward: 10.104
  Min Oracle Reward: 6.920
  Max Oracle Reward: 11.641
  Std Oracle Reward: 1.062
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: -0.019, Max: 0.084, Count: 13
  Total Sequences Evaluated: 722

======================================================================
EXPERIMENT ROUND 22/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 722

--- Round 22 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TAGCGGTCAAGC
  AGTTACGCGGCC
  CCCGAAGTTGGC
  GCGCATCGCATG
  TAGATGCGCCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.360
  Max reward: 12.719
  With intrinsic bonuses: 10.396

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9681, entropy=0.6972, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4108

=== Surrogate Model Training ===
Total samples: 754

Training on 727 samples (removed 27 outliers)
Reward range: [6.72, 13.14], mean: 9.95
  Created 13 candidate models for data size 727
Current R2 threshold: -0.18
  rf-tuned-l: R2 = 0.066 (std: 0.081)
  rf-tuned-xl: R2 = 0.076 (std: 0.063)
  gb-tuned-l: R2 = 0.109 (std: 0.059)
  gb-tuned-xl: R2 = 0.110 (std: 0.059)
  xgb-xl: R2 = -0.058 (std: 0.133)
  xgb-l: R2 = -0.058 (std: 0.133)
  mlp-adaptive-xl: R2 = -0.060 (std: 0.179)
  mlp-l: R2 = -0.116 (std: 0.121)
  svr-rbf-xl: R2 = 0.099 (std: 0.031)
  svr-poly-l: R2 = 0.099 (std: 0.031)
  knn-tuned-sqrt: R2 = 0.015 (std: 0.040)
  knn-tuned-l: R2 = 0.015 (std: 0.040)
  ridge: R2 = -0.026 (std: 0.023)

Model-based training with 13 models
Best R2: 0.110, Mean R2: 0.021
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.081 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.071 xgb-l:0.071 mlp-adaptive-xl:0.071 mlp-l:0.067 svr-rbf-xl:0.083 svr-poly-l:0.083 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9746, entropy=0.6854, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4072
  Round 1/3: Mean predicted reward = 9.798
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.081 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.071 xgb-l:0.071 mlp-adaptive-xl:0.071 mlp-l:0.067 svr-rbf-xl:0.083 svr-poly-l:0.083 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9720, entropy=0.6944, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4961
  Round 2/3: Mean predicted reward = 9.861
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.081 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.071 xgb-l:0.071 mlp-adaptive-xl:0.071 mlp-l:0.067 svr-rbf-xl:0.083 svr-poly-l:0.083 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.6906, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5490
  Round 3/3: Mean predicted reward = 9.936

  === Progress Analysis ===
  Status: NORMAL

--- Round 22 Results ---
  Mean Oracle Reward: 10.378
  Min Oracle Reward: 8.427
  Max Oracle Reward: 12.400
  Std Oracle Reward: 1.219
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.021, Max: 0.110, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 754

======================================================================
EXPERIMENT ROUND 23/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 754
  Consistent improvement, increasing LR to 0.000132

--- Round 23 Configuration ---
Learning rate: 0.000132
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGTACGCCGTGA
  ACGCCGTTGACG
  GCTGAGTCGCCA
  CCAAGCGTTGCG
  CGTACTGCAGGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.237
  Max reward: 12.529
  With intrinsic bonuses: 10.236

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9657, entropy=0.6880, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2243

=== Surrogate Model Training ===
Total samples: 786

Training on 756 samples (removed 30 outliers)
Reward range: [6.80, 13.10], mean: 9.97
  Created 13 candidate models for data size 756
Current R2 threshold: -0.16999999999999998
  rf-tuned-l: R2 = 0.121 (std: 0.086)
  rf-tuned-xl: R2 = 0.108 (std: 0.091)
  gb-tuned-l: R2 = 0.118 (std: 0.051)
  gb-tuned-xl: R2 = 0.118 (std: 0.051)
  xgb-xl: R2 = 0.006 (std: 0.103)
  xgb-l: R2 = 0.006 (std: 0.103)
  mlp-adaptive-xl: R2 = -0.082 (std: 0.101)
  mlp-l: R2 = -0.149 (std: 0.132)
  svr-rbf-xl: R2 = 0.125 (std: 0.033)
  svr-poly-l: R2 = 0.125 (std: 0.033)
  knn-tuned-sqrt: R2 = 0.057 (std: 0.057)
  knn-tuned-l: R2 = 0.057 (std: 0.057)
  ridge: R2 = -0.028 (std: 0.025)

Model-based training with 13 models
Best R2: 0.125, Mean R2: 0.045
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.082 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.074 xgb-l:0.074 mlp-adaptive-xl:0.068 mlp-l:0.063 svr-rbf-xl:0.083 svr-poly-l:0.083 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.071
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.6806, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1995
  Round 1/3: Mean predicted reward = 9.688
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.082 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.074 xgb-l:0.074 mlp-adaptive-xl:0.068 mlp-l:0.063 svr-rbf-xl:0.083 svr-poly-l:0.083 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.071
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9647, entropy=0.6808, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2235
  Round 2/3: Mean predicted reward = 9.864
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.082 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.074 xgb-l:0.074 mlp-adaptive-xl:0.068 mlp-l:0.063 svr-rbf-xl:0.083 svr-poly-l:0.083 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.071
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.6867, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1306
  Round 3/3: Mean predicted reward = 10.029

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 23 Results ---
  Mean Oracle Reward: 10.218
  Min Oracle Reward: 7.074
  Max Oracle Reward: 12.179
  Std Oracle Reward: 0.903
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.045, Max: 0.125, Count: 13
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
  TCACCCGGATGG
  CGTACCGATGCG
  GGCTATCAAGAT
  TAGGGAACCTCG
  TTGCGCGGACAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.146
  Max reward: 12.513
  With intrinsic bonuses: 10.177

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.6779, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0644

=== Surrogate Model Training ===
Total samples: 818

Training on 787 samples (removed 31 outliers)
Reward range: [6.80, 13.14], mean: 9.99
  Created 13 candidate models for data size 787
Current R2 threshold: -0.15999999999999998
  rf-tuned-l: R2 = 0.091 (std: 0.077)
  rf-tuned-xl: R2 = 0.089 (std: 0.081)
  gb-tuned-l: R2 = 0.115 (std: 0.039)
  gb-tuned-xl: R2 = 0.115 (std: 0.039)
  xgb-xl: R2 = -0.018 (std: 0.070)
  xgb-l: R2 = -0.018 (std: 0.070)
  mlp-adaptive-xl: R2 = -0.062 (std: 0.106)
  mlp-l: R2 = -0.059 (std: 0.131)
  svr-rbf-xl: R2 = 0.112 (std: 0.061)
  svr-poly-l: R2 = 0.112 (std: 0.061)
  knn-tuned-sqrt: R2 = 0.024 (std: 0.049)
  knn-tuned-l: R2 = 0.024 (std: 0.049)
  ridge: R2 = -0.047 (std: 0.037)

Model-based training with 13 models
Best R2: 0.115, Mean R2: 0.037
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.070 mlp-l:0.070 svr-rbf-xl:0.083 svr-poly-l:0.083 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.071
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9742, entropy=0.6579, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0820
  Round 1/3: Mean predicted reward = 9.940
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.070 mlp-l:0.070 svr-rbf-xl:0.083 svr-poly-l:0.083 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.071
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9669, entropy=0.6829, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0926
  Round 2/3: Mean predicted reward = 9.938
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.070 mlp-l:0.070 svr-rbf-xl:0.083 svr-poly-l:0.083 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.071
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.6889, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0603
  Round 3/3: Mean predicted reward = 9.858

  === Progress Analysis ===
  Status: NORMAL

--- Round 24 Results ---
  Mean Oracle Reward: 10.195
  Min Oracle Reward: 6.304
  Max Oracle Reward: 12.691
  Std Oracle Reward: 1.305
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.037, Max: 0.115, Count: 13
  Total Sequences Evaluated: 818

======================================================================
EXPERIMENT ROUND 25/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 818
  Performance plateaued, reducing LR to 0.000150

--- Round 25 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GATTATCCAGGC
  GCCCGAGCTATG
  CCACTGGTAGGC
  GCAAGGGCTCCT
  ACTGCACTCGGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.140
  Max reward: 11.655
  With intrinsic bonuses: 10.109

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9660, entropy=0.6857, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1329

=== Surrogate Model Training ===
Total samples: 850

Training on 816 samples (removed 34 outliers)
Reward range: [6.88, 13.10], mean: 10.00
  Created 13 candidate models for data size 816
Current R2 threshold: -0.15
  rf-tuned-l: R2 = 0.109 (std: 0.048)
  rf-tuned-xl: R2 = 0.090 (std: 0.052)
  gb-tuned-l: R2 = 0.080 (std: 0.062)
  gb-tuned-xl: R2 = 0.080 (std: 0.062)
  xgb-xl: R2 = -0.022 (std: 0.092)
  xgb-l: R2 = -0.022 (std: 0.092)
  mlp-adaptive-xl: R2 = -0.008 (std: 0.100)
  mlp-l: R2 = -0.055 (std: 0.162)
  svr-rbf-xl: R2 = 0.115 (std: 0.065)
  svr-poly-l: R2 = 0.115 (std: 0.065)
  knn-tuned-sqrt: R2 = 0.021 (std: 0.051)
  knn-tuned-l: R2 = 0.021 (std: 0.051)
  ridge: R2 = -0.049 (std: 0.044)

Model-based training with 13 models
Best R2: 0.115, Mean R2: 0.037
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.081 gb-tuned-l:0.080 gb-tuned-xl:0.080 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.073 mlp-l:0.070 svr-rbf-xl:0.083 svr-poly-l:0.083 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.6887, kl_div=0.0000
    Epoch 1: policy_loss=-0.0276, value_loss=0.9701, entropy=0.6912, kl_div=-0.0207
  Round 1/3: Mean predicted reward = 9.762
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.081 gb-tuned-l:0.080 gb-tuned-xl:0.080 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.073 mlp-l:0.070 svr-rbf-xl:0.083 svr-poly-l:0.083 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9679, entropy=0.7026, kl_div=0.0000
    Epoch 1: policy_loss=-0.0884, value_loss=0.9679, entropy=0.7057, kl_div=-0.1157
  Round 2/3: Mean predicted reward = 9.737
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.081 gb-tuned-l:0.080 gb-tuned-xl:0.080 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.073 mlp-l:0.070 svr-rbf-xl:0.083 svr-poly-l:0.083 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.7063, kl_div=0.0000
    Epoch 1: policy_loss=-0.0251, value_loss=0.9696, entropy=0.7087, kl_div=0.0042
  Round 3/3: Mean predicted reward = 10.022

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 25 Results ---
  Mean Oracle Reward: 10.082
  Min Oracle Reward: 6.448
  Max Oracle Reward: 11.685
  Std Oracle Reward: 1.009
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.037, Max: 0.115, Count: 13
  Total Sequences Evaluated: 850

======================================================================
EXPERIMENT ROUND 26/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 850
  Performance plateaued, reducing LR to 0.000136

--- Round 26 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCGCTGCAGATA
  GTGGTCGACACC
  GAGGCCGTATCC
  GGAGCTAGCATC
  TAGGAGGTCCCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.212
  Max reward: 11.983
  With intrinsic bonuses: 10.272

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9671, entropy=0.6940, kl_div=0.0000
    Epoch 1: policy_loss=-0.0538, value_loss=0.9671, entropy=0.6942, kl_div=0.0343

=== Surrogate Model Training ===
Total samples: 882

Training on 847 samples (removed 35 outliers)
Reward range: [6.88, 13.10], mean: 10.01
  Created 13 candidate models for data size 847
Current R2 threshold: -0.13999999999999999
  rf-tuned-l: R2 = 0.119 (std: 0.040)
  rf-tuned-xl: R2 = 0.117 (std: 0.041)
  gb-tuned-l: R2 = 0.098 (std: 0.033)
  gb-tuned-xl: R2 = 0.099 (std: 0.033)
  xgb-xl: R2 = 0.042 (std: 0.077)
  xgb-l: R2 = 0.042 (std: 0.077)
  mlp-adaptive-xl: R2 = -0.083 (std: 0.093)
  mlp-l: R2 = -0.041 (std: 0.077)
  svr-rbf-xl: R2 = 0.142 (std: 0.033)
  svr-poly-l: R2 = 0.142 (std: 0.033)
  knn-tuned-sqrt: R2 = 0.014 (std: 0.022)
  knn-tuned-l: R2 = 0.014 (std: 0.022)
  ridge: R2 = -0.042 (std: 0.042)

Model-based training with 13 models
Best R2: 0.142, Mean R2: 0.051
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.082 gb-tuned-l:0.080 gb-tuned-xl:0.080 xgb-xl:0.076 xgb-l:0.076 mlp-adaptive-xl:0.067 mlp-l:0.070 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9723, entropy=0.6953, kl_div=0.0000
    Epoch 1: policy_loss=-0.0070, value_loss=0.9723, entropy=0.6958, kl_div=0.0053
  Round 1/3: Mean predicted reward = 9.855
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.082 gb-tuned-l:0.080 gb-tuned-xl:0.080 xgb-xl:0.076 xgb-l:0.076 mlp-adaptive-xl:0.067 mlp-l:0.070 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9703, entropy=0.7018, kl_div=0.0000
    Epoch 1: policy_loss=-0.0484, value_loss=0.9703, entropy=0.7032, kl_div=-0.0436
  Round 2/3: Mean predicted reward = 10.024
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.082 gb-tuned-l:0.080 gb-tuned-xl:0.080 xgb-xl:0.076 xgb-l:0.076 mlp-adaptive-xl:0.067 mlp-l:0.070 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9704, entropy=0.6881, kl_div=0.0000
    Epoch 1: policy_loss=-0.0365, value_loss=0.9704, entropy=0.6901, kl_div=-0.0364
  Round 3/3: Mean predicted reward = 9.969

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 26 Results ---
  Mean Oracle Reward: 10.232
  Min Oracle Reward: 6.609
  Max Oracle Reward: 12.266
  Std Oracle Reward: 1.256
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.051, Max: 0.142, Count: 13
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
  GAACCGGCTCTG
  CCGGTTCGAACG
  CCCGGGTGACTA
  TCAAAGGCGTGC
  CTAAACTGGGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.942
  Max reward: 11.783
  With intrinsic bonuses: 9.920

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.6868, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0752

=== Surrogate Model Training ===
Total samples: 914

Training on 879 samples (removed 35 outliers)
Reward range: [6.88, 13.10], mean: 10.01
  Created 13 candidate models for data size 879
Current R2 threshold: -0.12999999999999998
  rf-tuned-l: R2 = 0.129 (std: 0.032)
  rf-tuned-xl: R2 = 0.115 (std: 0.025)
  gb-tuned-l: R2 = 0.129 (std: 0.025)
  gb-tuned-xl: R2 = 0.129 (std: 0.025)
  xgb-xl: R2 = 0.019 (std: 0.045)
  xgb-l: R2 = 0.019 (std: 0.045)
  mlp-adaptive-xl: R2 = -0.018 (std: 0.088)
  mlp-l: R2 = -0.041 (std: 0.078)
  svr-rbf-xl: R2 = 0.153 (std: 0.049)
  svr-poly-l: R2 = 0.153 (std: 0.049)
  knn-tuned-sqrt: R2 = 0.033 (std: 0.030)
  knn-tuned-l: R2 = 0.033 (std: 0.030)
  ridge: R2 = -0.032 (std: 0.029)

Model-based training with 13 models
Best R2: 0.153, Mean R2: 0.063
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.071 mlp-l:0.069 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9713, entropy=0.6918, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1354
  Round 1/3: Mean predicted reward = 9.982
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.071 mlp-l:0.069 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9713, entropy=0.6935, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1768
  Round 2/3: Mean predicted reward = 10.012
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.071 mlp-l:0.069 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9670, entropy=0.6987, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2774
  Round 3/3: Mean predicted reward = 10.023

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 27 Results ---
  Mean Oracle Reward: 9.899
  Min Oracle Reward: 7.549
  Max Oracle Reward: 11.920
  Std Oracle Reward: 1.054
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.063, Max: 0.153, Count: 13
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
  CAGGCACTGGTC
  TCCGGGACTGAA
  GGGGACCACTCT
  GGGAGATCCTAC
  CGTACAGGCTGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.008
  Max reward: 12.411
  With intrinsic bonuses: 9.956

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9648, entropy=0.7032, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2263

=== Surrogate Model Training ===
Total samples: 946

Training on 908 samples (removed 38 outliers)
Reward range: [6.94, 12.67], mean: 10.01
  Created 13 candidate models for data size 908
Current R2 threshold: -0.12
  rf-tuned-l: R2 = 0.126 (std: 0.026)
  rf-tuned-xl: R2 = 0.135 (std: 0.019)
  gb-tuned-l: R2 = 0.125 (std: 0.023)
  gb-tuned-xl: R2 = 0.125 (std: 0.023)
  xgb-xl: R2 = 0.019 (std: 0.064)
  xgb-l: R2 = 0.019 (std: 0.064)
  mlp-adaptive-xl: R2 = 0.016 (std: 0.050)
  mlp-l: R2 = -0.023 (std: 0.085)
  svr-rbf-xl: R2 = 0.162 (std: 0.051)
  svr-poly-l: R2 = 0.162 (std: 0.051)
  knn-tuned-sqrt: R2 = 0.023 (std: 0.031)
  knn-tuned-l: R2 = 0.023 (std: 0.031)
  ridge: R2 = -0.028 (std: 0.021)

Model-based training with 13 models
Best R2: 0.162, Mean R2: 0.068
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.082 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.073 mlp-l:0.070 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9755, entropy=0.7039, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3670
  Round 1/3: Mean predicted reward = 9.968
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.082 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.073 mlp-l:0.070 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=0.6805, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3384
  Round 2/3: Mean predicted reward = 9.916
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.082 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.073 mlp-l:0.070 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9670, entropy=0.7041, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2799
  Round 3/3: Mean predicted reward = 10.012

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 28 Results ---
  Mean Oracle Reward: 9.969
  Min Oracle Reward: 7.633
  Max Oracle Reward: 12.622
  Std Oracle Reward: 1.088
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.068, Max: 0.162, Count: 13
  Total Sequences Evaluated: 946

======================================================================
EXPERIMENT ROUND 29/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 946

--- Round 29 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TACGCGTGCAGC
  TAGGACGCGCCT
  GGCTTACAAGCG
  ATGCTGGCCAGC
  GGCCCCGAGTTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.489
  Max reward: 13.005
  With intrinsic bonuses: 10.439

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.6962, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1499

=== Surrogate Model Training ===
Total samples: 978

Training on 941 samples (removed 37 outliers)
Reward range: [6.92, 13.10], mean: 10.03
  Created 13 candidate models for data size 941
Current R2 threshold: -0.10999999999999999
  rf-tuned-l: R2 = 0.132 (std: 0.018)
  rf-tuned-xl: R2 = 0.146 (std: 0.024)
  gb-tuned-l: R2 = 0.141 (std: 0.036)
  gb-tuned-xl: R2 = 0.141 (std: 0.036)
  xgb-xl: R2 = 0.001 (std: 0.058)
  xgb-l: R2 = 0.001 (std: 0.058)
  mlp-adaptive-xl: R2 = -0.021 (std: 0.041)
  mlp-l: R2 = 0.004 (std: 0.043)
  svr-rbf-xl: R2 = 0.173 (std: 0.051)
  svr-poly-l: R2 = 0.173 (std: 0.051)
  knn-tuned-sqrt: R2 = 0.017 (std: 0.059)
  knn-tuned-l: R2 = 0.017 (std: 0.059)
  ridge: R2 = -0.028 (std: 0.025)

Model-based training with 13 models
Best R2: 0.173, Mean R2: 0.069
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.083 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.070 mlp-l:0.072 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9617, entropy=0.6922, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1359
  Round 1/3: Mean predicted reward = 9.800
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.083 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.070 mlp-l:0.072 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9655, entropy=0.6982, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1449
  Round 2/3: Mean predicted reward = 10.013
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.083 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.070 mlp-l:0.072 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9655, entropy=0.6947, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1707
  Round 3/3: Mean predicted reward = 10.204

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 29 Results ---
  Mean Oracle Reward: 10.496
  Min Oracle Reward: 7.034
  Max Oracle Reward: 13.036
  Std Oracle Reward: 1.311
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.069, Max: 0.173, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 978

======================================================================
EXPERIMENT ROUND 30/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 978
  Consistent improvement, increasing LR to 0.000360

--- Round 30 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCCGTCGGCAGA
  GAGCGCGACTCT
  CGTGAGCTAGAC
  GTGATGACCTCA
  GTACGCTATACG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.159
  Max reward: 12.834
  With intrinsic bonuses: 10.149

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9752, entropy=0.7016, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9864

=== Surrogate Model Training ===
Total samples: 1010

Training on 968 samples (removed 42 outliers)
Reward range: [6.99, 12.98], mean: 10.04
  Created 13 candidate models for data size 968
Current R2 threshold: -0.09999999999999998
  rf-tuned-l: R2 = 0.134 (std: 0.041)
  rf-tuned-xl: R2 = 0.125 (std: 0.060)
  gb-tuned-l: R2 = 0.137 (std: 0.047)
  gb-tuned-xl: R2 = 0.137 (std: 0.047)
  xgb-xl: R2 = 0.011 (std: 0.061)
  xgb-l: R2 = 0.011 (std: 0.061)
  mlp-adaptive-xl: R2 = -0.009 (std: 0.073)
  mlp-l: R2 = -0.016 (std: 0.086)
  svr-rbf-xl: R2 = 0.151 (std: 0.091)
  svr-poly-l: R2 = 0.151 (std: 0.091)
  knn-tuned-sqrt: R2 = -0.002 (std: 0.059)
  knn-tuned-l: R2 = -0.002 (std: 0.059)
  ridge: R2 = -0.036 (std: 0.033)

Model-based training with 13 models
Best R2: 0.151, Mean R2: 0.061
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.082 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.072 mlp-l:0.071 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9731, entropy=0.6786, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.2024
  Round 1/3: Mean predicted reward = 9.956
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.082 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.072 mlp-l:0.071 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9702, entropy=0.6888, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.3935
  Round 2/3: Mean predicted reward = 9.921
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.082 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.072 mlp-l:0.071 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9663, entropy=0.6887, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.6032
  Round 3/3: Mean predicted reward = 10.009

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 30 Results ---
  Mean Oracle Reward: 10.103
  Min Oracle Reward: 5.017
  Max Oracle Reward: 13.128
  Std Oracle Reward: 1.505
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.061, Max: 0.151, Count: 13
  Total Sequences Evaluated: 1010

======================================================================
EXPERIMENT ROUND 31/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1010

--- Round 31 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGGGCTACGATC
  GACGGGCTATAC
  CCCAGAGTGCGT
  ATCGGCCCAGGT
  GTTCCGCAGCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.176
  Max reward: 12.116
  With intrinsic bonuses: 10.142

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9714, entropy=0.6825, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0766

=== Surrogate Model Training ===
Total samples: 1042

Training on 999 samples (removed 43 outliers)
Reward range: [6.99, 12.98], mean: 10.05
  Created 13 candidate models for data size 999
Current R2 threshold: -0.09
  rf-tuned-l: R2 = 0.125 (std: 0.041)
  rf-tuned-xl: R2 = 0.120 (std: 0.044)
  gb-tuned-l: R2 = 0.150 (std: 0.040)
  gb-tuned-xl: R2 = 0.150 (std: 0.040)
  xgb-xl: R2 = 0.001 (std: 0.071)
  xgb-l: R2 = 0.001 (std: 0.071)
  mlp-adaptive-xl: R2 = 0.004 (std: 0.131)
  mlp-l: R2 = 0.029 (std: 0.088)
  svr-rbf-xl: R2 = 0.162 (std: 0.051)
  svr-poly-l: R2 = 0.162 (std: 0.051)
  knn-tuned-sqrt: R2 = 0.012 (std: 0.039)
  knn-tuned-l: R2 = 0.012 (std: 0.039)
  ridge: R2 = -0.027 (std: 0.026)

Model-based training with 13 models
Best R2: 0.162, Mean R2: 0.069
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.072 mlp-l:0.074 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.6597, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6984
  Round 1/3: Mean predicted reward = 9.904
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.072 mlp-l:0.074 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9658, entropy=0.6686, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7669
  Round 2/3: Mean predicted reward = 10.172
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.072 mlp-l:0.074 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.070
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9657, entropy=0.6513, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0331
  Round 3/3: Mean predicted reward = 9.969

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 31 Results ---
  Mean Oracle Reward: 10.147
  Min Oracle Reward: 6.168
  Max Oracle Reward: 12.147
  Std Oracle Reward: 1.225
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.069, Max: 0.162, Count: 13
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
  GCGCACCAGTGT
  GACCTGTCAGGA
  TTCCCGACGGAG
  GGGCCTTACAGC
  GAGGGACTCCTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.165
  Max reward: 12.762
  With intrinsic bonuses: 10.175

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9643, entropy=0.6488, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8324

=== Surrogate Model Training ===
Total samples: 1074

Training on 1030 samples (removed 44 outliers)
Reward range: [6.99, 12.98], mean: 10.05
  Created 13 candidate models for data size 1030
Current R2 threshold: -0.07999999999999999
  rf-tuned-l: R2 = 0.134 (std: 0.028)
  rf-tuned-xl: R2 = 0.129 (std: 0.030)
  gb-tuned-l: R2 = 0.133 (std: 0.038)
  gb-tuned-xl: R2 = 0.133 (std: 0.038)
  xgb-xl: R2 = 0.017 (std: 0.088)
  xgb-l: R2 = 0.017 (std: 0.088)
  mlp-adaptive-xl: R2 = 0.040 (std: 0.034)
  mlp-l: R2 = 0.040 (std: 0.022)
  svr-rbf-xl: R2 = 0.168 (std: 0.041)
  svr-poly-l: R2 = 0.168 (std: 0.041)
  knn-tuned-sqrt: R2 = 0.016 (std: 0.046)
  knn-tuned-l: R2 = 0.016 (std: 0.046)
  ridge: R2 = -0.024 (std: 0.028)

Model-based training with 13 models
Best R2: 0.168, Mean R2: 0.076
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.074 mlp-l:0.074 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9711, entropy=0.6487, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5919
  Round 1/3: Mean predicted reward = 10.046
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.074 mlp-l:0.074 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9715, entropy=0.6322, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4861
  Round 2/3: Mean predicted reward = 10.093
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.072 xgb-l:0.072 mlp-adaptive-xl:0.074 mlp-l:0.074 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9649, entropy=0.6457, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5849
  Round 3/3: Mean predicted reward = 9.959

  === Progress Analysis ===
  Status: NORMAL

--- Round 32 Results ---
  Mean Oracle Reward: 10.180
  Min Oracle Reward: 7.875
  Max Oracle Reward: 12.909
  Std Oracle Reward: 1.013
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.076, Max: 0.168, Count: 13
  Total Sequences Evaluated: 1074

======================================================================
EXPERIMENT ROUND 33/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1074
  Performance plateaued, reducing LR to 0.000055

--- Round 33 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CAACATGGGGTC
  GGACATGTCGCC
  CCGTACTGAGGC
  CGAGGTAACTCG
  CGTCTAAGGCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.141
  Max reward: 12.344
  With intrinsic bonuses: 10.124

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9651, entropy=0.6223, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2079

=== Surrogate Model Training ===
Total samples: 1106

Training on 1062 samples (removed 44 outliers)
Reward range: [6.99, 12.98], mean: 10.05
  Created 13 candidate models for data size 1062
Current R2 threshold: -0.06999999999999998
  rf-tuned-l: R2 = 0.144 (std: 0.050)
  rf-tuned-xl: R2 = 0.146 (std: 0.043)
  gb-tuned-l: R2 = 0.146 (std: 0.025)
  gb-tuned-xl: R2 = 0.146 (std: 0.025)
  xgb-xl: R2 = 0.036 (std: 0.060)
  xgb-l: R2 = 0.036 (std: 0.060)
  mlp-adaptive-xl: R2 = 0.071 (std: 0.046)
  mlp-l: R2 = 0.063 (std: 0.064)
  svr-rbf-xl: R2 = 0.180 (std: 0.043)
  svr-poly-l: R2 = 0.180 (std: 0.043)
  knn-tuned-sqrt: R2 = 0.003 (std: 0.057)
  knn-tuned-l: R2 = 0.003 (std: 0.057)
  ridge: R2 = -0.015 (std: 0.023)

Model-based training with 13 models
Best R2: 0.180, Mean R2: 0.088
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.075 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.6073, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1107
  Round 1/3: Mean predicted reward = 9.799
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.075 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=0.6209, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1767
  Round 2/3: Mean predicted reward = 10.015
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.075 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.069
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.6434, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1388
  Round 3/3: Mean predicted reward = 10.137

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 33 Results ---
  Mean Oracle Reward: 10.101
  Min Oracle Reward: 7.989
  Max Oracle Reward: 11.882
  Std Oracle Reward: 1.077
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.088, Max: 0.180, Count: 13
  Total Sequences Evaluated: 1106

======================================================================
EXPERIMENT ROUND 34/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1106
  Performance plateaued, reducing LR to 0.000019

--- Round 34 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGAGTCACCCGG
  GTGACCATCGGC
  TCGACTGCCGAG
  CTCTGACGGGAC
  GGTGCCGAACAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.978
  Max reward: 13.061
  With intrinsic bonuses: 9.958

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9652, entropy=0.6215, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0603

=== Surrogate Model Training ===
Total samples: 1138

Training on 1096 samples (removed 42 outliers)
Reward range: [6.94, 13.10], mean: 10.05
  Created 13 candidate models for data size 1096
Current R2 threshold: -0.06
  rf-tuned-l: R2 = 0.189 (std: 0.047)
  rf-tuned-xl: R2 = 0.178 (std: 0.052)
  gb-tuned-l: R2 = 0.171 (std: 0.027)
  gb-tuned-xl: R2 = 0.171 (std: 0.027)
  xgb-xl: R2 = 0.099 (std: 0.066)
  xgb-l: R2 = 0.099 (std: 0.066)
  mlp-adaptive-xl: R2 = 0.101 (std: 0.023)
  mlp-l: R2 = 0.101 (std: 0.028)
  svr-rbf-xl: R2 = 0.207 (std: 0.037)
  svr-poly-l: R2 = 0.207 (std: 0.037)
  knn-tuned-sqrt: R2 = 0.030 (std: 0.056)
  knn-tuned-l: R2 = 0.030 (std: 0.056)
  ridge: R2 = -0.012 (std: 0.019)

Model-based training with 13 models
Best R2: 0.207, Mean R2: 0.121
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.075 xgb-l:0.075 mlp-adaptive-xl:0.075 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.067
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9639, entropy=0.6390, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0525
  Round 1/3: Mean predicted reward = 9.996
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.075 xgb-l:0.075 mlp-adaptive-xl:0.075 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.067
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9715, entropy=0.6338, kl_div=0.0000
    Epoch 1: policy_loss=-0.0006, value_loss=0.9715, entropy=0.6331, kl_div=0.0453
  Round 2/3: Mean predicted reward = 10.064
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.075 xgb-l:0.075 mlp-adaptive-xl:0.075 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.067
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9666, entropy=0.6206, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0527
  Round 3/3: Mean predicted reward = 10.027

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 34 Results ---
  Mean Oracle Reward: 9.971
  Min Oracle Reward: 6.136
  Max Oracle Reward: 12.835
  Std Oracle Reward: 1.381
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.121, Max: 0.207, Count: 13
  Total Sequences Evaluated: 1138

======================================================================
EXPERIMENT ROUND 35/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1138
  Performance plateaued, reducing LR to 0.000150

--- Round 35 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGCAGTGAACCT
  GTACCCGTGGAA
  GAGACGCGCTCT
  GATACTGCGGCC
  CCAGGGCTGACT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.283
  Max reward: 12.471
  With intrinsic bonuses: 10.245

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9664, entropy=0.6195, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4558

=== Surrogate Model Training ===
Total samples: 1170

Training on 1126 samples (removed 44 outliers)
Reward range: [6.98, 13.10], mean: 10.06
  Created 13 candidate models for data size 1126
Current R2 threshold: -0.04999999999999999
  rf-tuned-l: R2 = 0.162 (std: 0.039)
  rf-tuned-xl: R2 = 0.171 (std: 0.046)
  gb-tuned-l: R2 = 0.176 (std: 0.021)
  gb-tuned-xl: R2 = 0.176 (std: 0.021)
  xgb-xl: R2 = 0.081 (std: 0.086)
  xgb-l: R2 = 0.081 (std: 0.086)
  mlp-adaptive-xl: R2 = 0.081 (std: 0.063)
  mlp-l: R2 = 0.070 (std: 0.045)
  svr-rbf-xl: R2 = 0.216 (std: 0.045)
  svr-poly-l: R2 = 0.216 (std: 0.045)
  knn-tuned-sqrt: R2 = 0.024 (std: 0.026)
  knn-tuned-l: R2 = 0.024 (std: 0.026)
  ridge: R2 = -0.013 (std: 0.016)

Model-based training with 13 models
Best R2: 0.216, Mean R2: 0.113
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.074 xgb-l:0.074 mlp-adaptive-xl:0.074 mlp-l:0.074 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.6182, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3137
  Round 1/3: Mean predicted reward = 9.919
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.074 xgb-l:0.074 mlp-adaptive-xl:0.074 mlp-l:0.074 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9651, entropy=0.6023, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4462
  Round 2/3: Mean predicted reward = 9.988
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.074 xgb-l:0.074 mlp-adaptive-xl:0.074 mlp-l:0.074 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9677, entropy=0.6195, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4389
  Round 3/3: Mean predicted reward = 9.954

  === Progress Analysis ===
  Status: NORMAL

--- Round 35 Results ---
  Mean Oracle Reward: 10.309
  Min Oracle Reward: 6.933
  Max Oracle Reward: 12.590
  Std Oracle Reward: 1.257
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.113, Max: 0.216, Count: 13
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
  CTGAACGGTGAC
  CGAGCCCTTGGA
  CGAGTCTGAGCC
  GCGACAGGCTCT
  AGACGTTGGCCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.000
  Max reward: 12.299
  With intrinsic bonuses: 9.987

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9673, entropy=0.5986, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8995

=== Surrogate Model Training ===
Total samples: 1202

Training on 1156 samples (removed 46 outliers)
Reward range: [6.98, 13.10], mean: 10.07
  Created 13 candidate models for data size 1156
Current R2 threshold: -0.03999999999999998
  rf-tuned-l: R2 = 0.165 (std: 0.050)
  rf-tuned-xl: R2 = 0.164 (std: 0.057)
  gb-tuned-l: R2 = 0.167 (std: 0.031)
  gb-tuned-xl: R2 = 0.167 (std: 0.031)
  xgb-xl: R2 = 0.086 (std: 0.102)
  xgb-l: R2 = 0.086 (std: 0.102)
  mlp-adaptive-xl: R2 = 0.075 (std: 0.082)
  mlp-l: R2 = 0.056 (std: 0.068)
  svr-rbf-xl: R2 = 0.221 (std: 0.052)
  svr-poly-l: R2 = 0.221 (std: 0.052)
  knn-tuned-sqrt: R2 = 0.027 (std: 0.042)
  knn-tuned-l: R2 = 0.027 (std: 0.042)
  ridge: R2 = -0.015 (std: 0.022)

Model-based training with 13 models
Best R2: 0.221, Mean R2: 0.111
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.075 xgb-l:0.075 mlp-adaptive-xl:0.074 mlp-l:0.073 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.5840, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4584
  Round 1/3: Mean predicted reward = 9.916
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.075 xgb-l:0.075 mlp-adaptive-xl:0.074 mlp-l:0.073 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9673, entropy=0.6230, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2388
  Round 2/3: Mean predicted reward = 9.961
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.075 xgb-l:0.075 mlp-adaptive-xl:0.074 mlp-l:0.073 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9642, entropy=0.6080, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1884
  Round 3/3: Mean predicted reward = 9.989

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 36 Results ---
  Mean Oracle Reward: 10.006
  Min Oracle Reward: 5.814
  Max Oracle Reward: 12.440
  Std Oracle Reward: 1.422
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.111, Max: 0.221, Count: 13
  Total Sequences Evaluated: 1202

======================================================================
EXPERIMENT ROUND 37/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1202

--- Round 37 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ATGACGTGGCAC
  CCTGTGAAGGCA
  GGGCCGTACACT
  GGCGCCTCTGAA
  TCGACTGGGCCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.106
  Max reward: 12.956
  With intrinsic bonuses: 10.076

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9768, entropy=0.5752, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1930

=== Surrogate Model Training ===
Total samples: 1234

Training on 1190 samples (removed 44 outliers)
Reward range: [6.94, 13.14], mean: 10.08
  Created 13 candidate models for data size 1190
Current R2 threshold: -0.02999999999999997
  rf-tuned-l: R2 = 0.166 (std: 0.063)
  rf-tuned-xl: R2 = 0.173 (std: 0.068)
  gb-tuned-l: R2 = 0.168 (std: 0.025)
  gb-tuned-xl: R2 = 0.168 (std: 0.025)
  xgb-xl: R2 = 0.108 (std: 0.116)
  xgb-l: R2 = 0.108 (std: 0.116)
  mlp-adaptive-xl: R2 = 0.139 (std: 0.081)
  mlp-l: R2 = 0.106 (std: 0.067)
  svr-rbf-xl: R2 = 0.226 (std: 0.061)
  svr-poly-l: R2 = 0.226 (std: 0.061)
  knn-tuned-sqrt: R2 = 0.021 (std: 0.056)
  knn-tuned-l: R2 = 0.021 (std: 0.056)
  ridge: R2 = -0.015 (std: 0.028)

Model-based training with 13 models
Best R2: 0.226, Mean R2: 0.124
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.081 gb-tuned-l:0.080 gb-tuned-xl:0.080 xgb-xl:0.075 xgb-l:0.075 mlp-adaptive-xl:0.078 mlp-l:0.075 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.069 knn-tuned-l:0.069 ridge:0.067
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9664, entropy=0.6128, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0990
  Round 1/3: Mean predicted reward = 9.872
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.081 gb-tuned-l:0.080 gb-tuned-xl:0.080 xgb-xl:0.075 xgb-l:0.075 mlp-adaptive-xl:0.078 mlp-l:0.075 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.069 knn-tuned-l:0.069 ridge:0.067
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9628, entropy=0.6119, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3214
  Round 2/3: Mean predicted reward = 10.018
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.081 gb-tuned-l:0.080 gb-tuned-xl:0.080 xgb-xl:0.075 xgb-l:0.075 mlp-adaptive-xl:0.078 mlp-l:0.075 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.069 knn-tuned-l:0.069 ridge:0.067
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9647, entropy=0.6085, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3229
  Round 3/3: Mean predicted reward = 9.974

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 37 Results ---
  Mean Oracle Reward: 10.091
  Min Oracle Reward: 0.000
  Max Oracle Reward: 13.017
  Std Oracle Reward: 2.315
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.124, Max: 0.226, Count: 13
  Total Sequences Evaluated: 1234

======================================================================
EXPERIMENT ROUND 38/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1234

--- Round 38 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCGTCGCACTGA
  GACGGACTGCTC
  ATCGGTCAACGG
  GGTCGCAACTGC
  AAGTCCTGGCGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.780
  Max reward: 12.631
  With intrinsic bonuses: 9.785

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9709, entropy=0.5829, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0541

=== Surrogate Model Training ===
Total samples: 1266

Training on 1219 samples (removed 47 outliers)
Reward range: [6.94, 13.14], mean: 10.09
  Created 13 candidate models for data size 1219
Current R2 threshold: -0.019999999999999962
  rf-tuned-l: R2 = 0.165 (std: 0.065)
  rf-tuned-xl: R2 = 0.149 (std: 0.073)
  gb-tuned-l: R2 = 0.168 (std: 0.027)
  gb-tuned-xl: R2 = 0.168 (std: 0.027)
  xgb-xl: R2 = 0.049 (std: 0.097)
  xgb-l: R2 = 0.049 (std: 0.097)
  mlp-adaptive-xl: R2 = 0.094 (std: 0.096)
  mlp-l: R2 = 0.070 (std: 0.089)
  svr-rbf-xl: R2 = 0.213 (std: 0.055)
  svr-poly-l: R2 = 0.213 (std: 0.055)
  knn-tuned-sqrt: R2 = 0.009 (std: 0.050)
  knn-tuned-l: R2 = 0.009 (std: 0.050)
  ridge: R2 = -0.019 (std: 0.021)

Model-based training with 13 models
Best R2: 0.213, Mean R2: 0.103
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.076 mlp-l:0.074 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9744, entropy=0.6045, kl_div=0.0000
    Epoch 1: policy_loss=-0.0262, value_loss=0.9744, entropy=0.6066, kl_div=-0.0390
  Round 1/3: Mean predicted reward = 9.892
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.076 mlp-l:0.074 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9650, entropy=0.6171, kl_div=0.0000
    Epoch 1: policy_loss=-0.0459, value_loss=0.9650, entropy=0.6209, kl_div=-0.1164
  Round 2/3: Mean predicted reward = 10.052
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.073 xgb-l:0.073 mlp-adaptive-xl:0.076 mlp-l:0.074 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9639, entropy=0.6181, kl_div=0.0000
    Epoch 1: policy_loss=-0.0520, value_loss=0.9639, entropy=0.6211, kl_div=-0.1016
  Round 3/3: Mean predicted reward = 10.039

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 38 Results ---
  Mean Oracle Reward: 9.808
  Min Oracle Reward: 0.336
  Max Oracle Reward: 12.511
  Std Oracle Reward: 2.316
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.103, Max: 0.213, Count: 13
  Total Sequences Evaluated: 1266

======================================================================
EXPERIMENT ROUND 39/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1266

--- Round 39 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTACTGACACGG
  CCAGAGCTGGTC
  AACCGTGTCGGC
  CTGGTGCCGCAA
  CAGCATCGTGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.221
  Max reward: 12.478
  With intrinsic bonuses: 10.210

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=0.6102, kl_div=0.0000
    Epoch 1: policy_loss=-0.0163, value_loss=0.9675, entropy=0.6105, kl_div=-0.0023

=== Surrogate Model Training ===
Total samples: 1298

Training on 1249 samples (removed 49 outliers)
Reward range: [6.98, 13.14], mean: 10.09
  Created 13 candidate models for data size 1249
Current R2 threshold: -0.010000000000000009
  rf-tuned-l: R2 = 0.160 (std: 0.084)
  rf-tuned-xl: R2 = 0.158 (std: 0.065)
  gb-tuned-l: R2 = 0.192 (std: 0.027)
  gb-tuned-xl: R2 = 0.192 (std: 0.027)
  xgb-xl: R2 = 0.070 (std: 0.076)
  xgb-l: R2 = 0.070 (std: 0.076)
  mlp-adaptive-xl: R2 = 0.130 (std: 0.070)
  mlp-l: R2 = 0.083 (std: 0.087)
  svr-rbf-xl: R2 = 0.216 (std: 0.052)
  svr-poly-l: R2 = 0.216 (std: 0.052)
  knn-tuned-sqrt: R2 = 0.016 (std: 0.064)
  knn-tuned-l: R2 = 0.016 (std: 0.064)
  ridge: R2 = -0.019 (std: 0.023)

Model-based training with 12 models
Best R2: 0.216, Mean R2: 0.116
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.089 gb-tuned-xl:0.089 xgb-xl:0.079 xgb-l:0.079 mlp-adaptive-xl:0.083 mlp-l:0.080 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.074 knn-tuned-l:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.5950, kl_div=0.0000
    Epoch 1: policy_loss=-0.0084, value_loss=0.9694, entropy=0.5948, kl_div=-0.0003
  Round 1/3: Mean predicted reward = 10.000
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.089 gb-tuned-xl:0.089 xgb-xl:0.079 xgb-l:0.079 mlp-adaptive-xl:0.083 mlp-l:0.080 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.074 knn-tuned-l:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9664, entropy=0.5996, kl_div=0.0000
    Epoch 1: policy_loss=-0.0261, value_loss=0.9664, entropy=0.5985, kl_div=0.0279
  Round 2/3: Mean predicted reward = 10.109
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.089 gb-tuned-xl:0.089 xgb-xl:0.079 xgb-l:0.079 mlp-adaptive-xl:0.083 mlp-l:0.080 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.074 knn-tuned-l:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.6364, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0601
  Round 3/3: Mean predicted reward = 10.196

  === Progress Analysis ===
  Status: NORMAL

--- Round 39 Results ---
  Mean Oracle Reward: 10.215
  Min Oracle Reward: 7.441
  Max Oracle Reward: 12.677
  Std Oracle Reward: 1.041
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.116, Max: 0.216, Count: 13
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
  CTATGCGGGCAC
  TGACCGGAGCCT
  TTCCAAGCGAGG
  GTCCGACGACTG
  CATCCGAGAGGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.283
  Max reward: 12.830
  With intrinsic bonuses: 10.318

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9672, entropy=0.5989, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6607

=== Surrogate Model Training ===
Total samples: 1330

Training on 1280 samples (removed 50 outliers)
Reward range: [6.98, 13.14], mean: 10.10
  Created 13 candidate models for data size 1280
Current R2 threshold: 0.0
  rf-tuned-l: R2 = 0.176 (std: 0.068)
  rf-tuned-xl: R2 = 0.170 (std: 0.069)
  gb-tuned-l: R2 = 0.190 (std: 0.027)
  gb-tuned-xl: R2 = 0.190 (std: 0.027)
  xgb-xl: R2 = 0.060 (std: 0.098)
  xgb-l: R2 = 0.060 (std: 0.098)
  mlp-adaptive-xl: R2 = 0.097 (std: 0.043)
  mlp-l: R2 = 0.140 (std: 0.056)
  svr-rbf-xl: R2 = 0.225 (std: 0.058)
  svr-poly-l: R2 = 0.225 (std: 0.058)
  knn-tuned-sqrt: R2 = 0.023 (std: 0.068)
  knn-tuned-l: R2 = 0.023 (std: 0.068)
  ridge: R2 = -0.017 (std: 0.025)

Model-based training with 12 models
Best R2: 0.225, Mean R2: 0.120
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.087 rf-tuned-xl:0.086 gb-tuned-l:0.088 gb-tuned-xl:0.088 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.080 mlp-l:0.084 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.075 knn-tuned-l:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.5880, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3651
  Round 1/3: Mean predicted reward = 9.841
    Using performance-based weights
    Model weights: rf-tuned-l:0.087 rf-tuned-xl:0.086 gb-tuned-l:0.088 gb-tuned-xl:0.088 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.080 mlp-l:0.084 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.075 knn-tuned-l:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9660, entropy=0.5511, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3101
  Round 2/3: Mean predicted reward = 9.965
    Using performance-based weights
    Model weights: rf-tuned-l:0.087 rf-tuned-xl:0.086 gb-tuned-l:0.088 gb-tuned-xl:0.088 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.080 mlp-l:0.084 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.075 knn-tuned-l:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9672, entropy=0.5567, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4587
  Round 3/3: Mean predicted reward = 10.087

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 40 Results ---
  Mean Oracle Reward: 10.318
  Min Oracle Reward: 6.623
  Max Oracle Reward: 12.802
  Std Oracle Reward: 1.112
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.120, Max: 0.225, Count: 13
  Total Sequences Evaluated: 1330

======================================================================
EXPERIMENT ROUND 41/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1330
  Consistent improvement, increasing LR to 0.000327

--- Round 41 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AGGGCTCACGTC
  CGGGACTGCTAC
  GGACCGACTTGC
  CTGCCAATGGGC
  CGCCAAGTCGTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.350
  Max reward: 11.955
  With intrinsic bonuses: 10.409

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.5288, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7173

=== Surrogate Model Training ===
Total samples: 1362

Training on 1310 samples (removed 52 outliers)
Reward range: [7.00, 13.14], mean: 10.11
  Created 13 candidate models for data size 1310
Current R2 threshold: 0.010000000000000009
  rf-tuned-l: R2 = 0.161 (std: 0.086)
  rf-tuned-xl: R2 = 0.169 (std: 0.079)
  gb-tuned-l: R2 = 0.181 (std: 0.020)
  gb-tuned-xl: R2 = 0.181 (std: 0.020)
  xgb-xl: R2 = 0.108 (std: 0.051)
  xgb-l: R2 = 0.108 (std: 0.051)
  mlp-adaptive-xl: R2 = 0.069 (std: 0.067)
  mlp-l: R2 = 0.110 (std: 0.055)
  svr-rbf-xl: R2 = 0.228 (std: 0.055)
  svr-poly-l: R2 = 0.228 (std: 0.055)
  knn-tuned-sqrt: R2 = 0.026 (std: 0.070)
  knn-tuned-l: R2 = 0.026 (std: 0.070)
  ridge: R2 = -0.018 (std: 0.031)

Model-based training with 12 models
Best R2: 0.228, Mean R2: 0.121
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.081 xgb-l:0.081 mlp-adaptive-xl:0.078 mlp-l:0.081 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.075 knn-tuned-l:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.4996, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3730
  Round 1/3: Mean predicted reward = 9.898
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.081 xgb-l:0.081 mlp-adaptive-xl:0.078 mlp-l:0.081 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.075 knn-tuned-l:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=0.4882, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3538
  Round 2/3: Mean predicted reward = 10.028
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.081 xgb-l:0.081 mlp-adaptive-xl:0.078 mlp-l:0.081 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.075 knn-tuned-l:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9700, entropy=0.4915, kl_div=0.0000
    Epoch 1: policy_loss=-0.0189, value_loss=0.9700, entropy=0.4918, kl_div=0.0185
  Round 3/3: Mean predicted reward = 9.996

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 41 Results ---
  Mean Oracle Reward: 10.365
  Min Oracle Reward: 8.792
  Max Oracle Reward: 12.070
  Std Oracle Reward: 0.794
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.121, Max: 0.228, Count: 13
  Total Sequences Evaluated: 1362

======================================================================
EXPERIMENT ROUND 42/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1362
  Performance plateaued, reducing LR to 0.000100

--- Round 42 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGCGGACGACTT
  TACCCCGGGATG
  GGACCATGTGAC
  GCGCACGAGTTC
  TCCGCGGTCAAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.117
  Max reward: 12.064
  With intrinsic bonuses: 10.126

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=0.4886, kl_div=0.0000
    Epoch 1: policy_loss=-0.0398, value_loss=0.9678, entropy=0.4945, kl_div=-0.1484

=== Surrogate Model Training ===
Total samples: 1394

Training on 1341 samples (removed 53 outliers)
Reward range: [7.01, 13.14], mean: 10.12
  Created 13 candidate models for data size 1341
Current R2 threshold: 0.020000000000000018
  rf-tuned-l: R2 = 0.172 (std: 0.069)
  rf-tuned-xl: R2 = 0.170 (std: 0.072)
  gb-tuned-l: R2 = 0.170 (std: 0.038)
  gb-tuned-xl: R2 = 0.170 (std: 0.038)
  xgb-xl: R2 = 0.088 (std: 0.042)
  xgb-l: R2 = 0.088 (std: 0.042)
  mlp-adaptive-xl: R2 = 0.134 (std: 0.068)
  mlp-l: R2 = 0.160 (std: 0.062)
  svr-rbf-xl: R2 = 0.229 (std: 0.056)
  svr-poly-l: R2 = 0.229 (std: 0.056)
  knn-tuned-sqrt: R2 = 0.031 (std: 0.046)
  knn-tuned-l: R2 = 0.031 (std: 0.046)
  ridge: R2 = -0.016 (std: 0.029)

Model-based training with 12 models
Best R2: 0.229, Mean R2: 0.127
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.079 xgb-l:0.079 mlp-adaptive-xl:0.083 mlp-l:0.085 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.075 knn-tuned-l:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9635, entropy=0.4884, kl_div=0.0000
    Epoch 1: policy_loss=-0.0332, value_loss=0.9635, entropy=0.4926, kl_div=-0.0732
  Round 1/3: Mean predicted reward = 10.194
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.079 xgb-l:0.079 mlp-adaptive-xl:0.083 mlp-l:0.085 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.075 knn-tuned-l:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.4840, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1717
  Round 2/3: Mean predicted reward = 10.086
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.079 xgb-l:0.079 mlp-adaptive-xl:0.083 mlp-l:0.085 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.075 knn-tuned-l:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9676, entropy=0.5489, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1919
  Round 3/3: Mean predicted reward = 10.192

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 42 Results ---
  Mean Oracle Reward: 10.095
  Min Oracle Reward: 7.035
  Max Oracle Reward: 12.035
  Std Oracle Reward: 1.221
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.127, Max: 0.229, Count: 13
  Total Sequences Evaluated: 1394

======================================================================
EXPERIMENT ROUND 43/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1394
  Performance plateaued, reducing LR to 0.000055

--- Round 43 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCCCATAGGGTG
  CGACCCGATGTG
  ACTGGCCTCGAG
  ACCGAGGCTTGA
  GAGCGCGCTCAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.216
  Max reward: 12.322
  With intrinsic bonuses: 10.183

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9663, entropy=0.5103, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1316

=== Surrogate Model Training ===
Total samples: 1426

Training on 1373 samples (removed 53 outliers)
Reward range: [7.01, 13.14], mean: 10.12
  Created 13 candidate models for data size 1373
Current R2 threshold: 0.030000000000000027
  rf-tuned-l: R2 = 0.168 (std: 0.068)
  rf-tuned-xl: R2 = 0.171 (std: 0.066)
  gb-tuned-l: R2 = 0.198 (std: 0.026)
  gb-tuned-xl: R2 = 0.198 (std: 0.026)
  xgb-xl: R2 = 0.071 (std: 0.068)
  xgb-l: R2 = 0.071 (std: 0.068)
  mlp-adaptive-xl: R2 = 0.127 (std: 0.080)
  mlp-l: R2 = 0.131 (std: 0.056)
  svr-rbf-xl: R2 = 0.239 (std: 0.066)
  svr-poly-l: R2 = 0.239 (std: 0.066)
  knn-tuned-sqrt: R2 = 0.038 (std: 0.037)
  knn-tuned-l: R2 = 0.038 (std: 0.037)
  ridge: R2 = -0.011 (std: 0.040)

Model-based training with 12 models
Best R2: 0.239, Mean R2: 0.129
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.085 rf-tuned-xl:0.086 gb-tuned-l:0.088 gb-tuned-xl:0.088 xgb-xl:0.078 xgb-l:0.078 mlp-adaptive-xl:0.082 mlp-l:0.082 svr-rbf-xl:0.092 svr-poly-l:0.092 knn-tuned-sqrt:0.075 knn-tuned-l:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.5231, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1572
  Round 1/3: Mean predicted reward = 9.979
    Using performance-based weights
    Model weights: rf-tuned-l:0.085 rf-tuned-xl:0.086 gb-tuned-l:0.088 gb-tuned-xl:0.088 xgb-xl:0.078 xgb-l:0.078 mlp-adaptive-xl:0.082 mlp-l:0.082 svr-rbf-xl:0.092 svr-poly-l:0.092 knn-tuned-sqrt:0.075 knn-tuned-l:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=0.5152, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0873
  Round 2/3: Mean predicted reward = 10.155
    Using performance-based weights
    Model weights: rf-tuned-l:0.085 rf-tuned-xl:0.086 gb-tuned-l:0.088 gb-tuned-xl:0.088 xgb-xl:0.078 xgb-l:0.078 mlp-adaptive-xl:0.082 mlp-l:0.082 svr-rbf-xl:0.092 svr-poly-l:0.092 knn-tuned-sqrt:0.075 knn-tuned-l:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9717, entropy=0.4943, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0593
  Round 3/3: Mean predicted reward = 10.013

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 43 Results ---
  Mean Oracle Reward: 10.156
  Min Oracle Reward: 7.677
  Max Oracle Reward: 12.099
  Std Oracle Reward: 1.132
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.129, Max: 0.239, Count: 13
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
  CTTTCGGCAGAA
  AGTATTGACCCG
  AAGCGGCCGCTT
  AGCAGGTCGCCT
  CGCTTGCGGAAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.507
  Max reward: 13.006
  With intrinsic bonuses: 10.498

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9664, entropy=0.5062, kl_div=0.0000
    Epoch 1: policy_loss=-0.0108, value_loss=0.9664, entropy=0.5063, kl_div=0.0153

=== Surrogate Model Training ===
Total samples: 1458

Training on 1403 samples (removed 55 outliers)
Reward range: [7.06, 13.14], mean: 10.13
  Created 13 candidate models for data size 1403
Current R2 threshold: 0.040000000000000036
  rf-tuned-l: R2 = 0.183 (std: 0.067)
  rf-tuned-xl: R2 = 0.176 (std: 0.078)
  gb-tuned-l: R2 = 0.186 (std: 0.050)
  gb-tuned-xl: R2 = 0.186 (std: 0.050)
  xgb-xl: R2 = 0.091 (std: 0.078)
  xgb-l: R2 = 0.091 (std: 0.078)
  mlp-adaptive-xl: R2 = 0.103 (std: 0.082)
  mlp-l: R2 = 0.154 (std: 0.057)
  svr-rbf-xl: R2 = 0.237 (std: 0.069)
  svr-poly-l: R2 = 0.237 (std: 0.069)
  knn-tuned-sqrt: R2 = 0.040 (std: 0.048)
  knn-tuned-l: R2 = 0.040 (std: 0.048)
  ridge: R2 = -0.013 (std: 0.042)

Model-based training with 10 models
Best R2: 0.237, Mean R2: 0.132
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.102 rf-tuned-xl:0.101 gb-tuned-l:0.102 gb-tuned-xl:0.102 xgb-xl:0.093 xgb-l:0.093 mlp-adaptive-xl:0.094 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.5186, kl_div=0.0000
    Epoch 1: policy_loss=-0.0094, value_loss=0.9698, entropy=0.5190, kl_div=0.0023
  Round 1/3: Mean predicted reward = 10.164
    Using performance-based weights
    Model weights: rf-tuned-l:0.102 rf-tuned-xl:0.101 gb-tuned-l:0.102 gb-tuned-xl:0.102 xgb-xl:0.093 xgb-l:0.093 mlp-adaptive-xl:0.094 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.5015, kl_div=0.0000
    Epoch 1: policy_loss=-0.0140, value_loss=0.9690, entropy=0.5027, kl_div=-0.0300
  Round 2/3: Mean predicted reward = 10.084
    Using performance-based weights
    Model weights: rf-tuned-l:0.102 rf-tuned-xl:0.101 gb-tuned-l:0.102 gb-tuned-xl:0.102 xgb-xl:0.093 xgb-l:0.093 mlp-adaptive-xl:0.094 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9719, entropy=0.4929, kl_div=0.0000
    Epoch 1: policy_loss=0.0115, value_loss=0.9719, entropy=0.4941, kl_div=-0.0417
  Round 3/3: Mean predicted reward = 9.970

  === Progress Analysis ===
  Status: NORMAL

--- Round 44 Results ---
  Mean Oracle Reward: 10.461
  Min Oracle Reward: 6.475
  Max Oracle Reward: 12.806
  Std Oracle Reward: 1.169
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.132, Max: 0.237, Count: 13
  Total Sequences Evaluated: 1458

======================================================================
EXPERIMENT ROUND 45/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1458
  Consistent improvement, increasing LR to 0.000360

--- Round 45 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CACCGGCGTAGT
  GTCGGCACGACT
  CCGCAGGGTATC
  CGGTAGTACGCC
  CATTGCAGGGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.201
  Max reward: 11.895
  With intrinsic bonuses: 10.255

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.5083, kl_div=0.0000
    Epoch 1: policy_loss=-0.0481, value_loss=0.9682, entropy=0.5074, kl_div=-0.0100

=== Surrogate Model Training ===
Total samples: 1490

Training on 1435 samples (removed 55 outliers)
Reward range: [7.06, 13.14], mean: 10.14
  Created 13 candidate models for data size 1435
Current R2 threshold: 0.050000000000000044
  rf-tuned-l: R2 = 0.185 (std: 0.072)
  rf-tuned-xl: R2 = 0.185 (std: 0.070)
  gb-tuned-l: R2 = 0.194 (std: 0.047)
  gb-tuned-xl: R2 = 0.194 (std: 0.047)
  xgb-xl: R2 = 0.111 (std: 0.055)
  xgb-l: R2 = 0.111 (std: 0.055)
  mlp-adaptive-xl: R2 = 0.163 (std: 0.093)
  mlp-l: R2 = 0.154 (std: 0.091)
  svr-rbf-xl: R2 = 0.249 (std: 0.071)
  svr-poly-l: R2 = 0.249 (std: 0.071)
  knn-tuned-sqrt: R2 = 0.062 (std: 0.041)
  knn-tuned-l: R2 = 0.062 (std: 0.041)
  ridge: R2 = -0.006 (std: 0.039)

Model-based training with 12 models
Best R2: 0.249, Mean R2: 0.147
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.085 rf-tuned-xl:0.085 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.079 xgb-l:0.079 mlp-adaptive-xl:0.083 mlp-l:0.083 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.075 knn-tuned-l:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9740, entropy=0.4714, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3715
  Round 1/3: Mean predicted reward = 9.859
    Using performance-based weights
    Model weights: rf-tuned-l:0.085 rf-tuned-xl:0.085 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.079 xgb-l:0.079 mlp-adaptive-xl:0.083 mlp-l:0.083 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.075 knn-tuned-l:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9671, entropy=0.4788, kl_div=0.0000
    Epoch 1: policy_loss=-0.0577, value_loss=0.9671, entropy=0.4788, kl_div=-0.0250
  Round 2/3: Mean predicted reward = 10.177
    Using performance-based weights
    Model weights: rf-tuned-l:0.085 rf-tuned-xl:0.085 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.079 xgb-l:0.079 mlp-adaptive-xl:0.083 mlp-l:0.083 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.075 knn-tuned-l:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9670, entropy=0.4842, kl_div=0.0000
    Epoch 1: policy_loss=0.0333, value_loss=0.9670, entropy=0.4868, kl_div=-0.0248
  Round 3/3: Mean predicted reward = 10.015

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 45 Results ---
  Mean Oracle Reward: 10.233
  Min Oracle Reward: 7.587
  Max Oracle Reward: 11.869
  Std Oracle Reward: 1.030
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.147, Max: 0.249, Count: 13
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
  GCCCGATCATGG
  CGGGTGACACTC
  ATCGAGGCTCGC
  CCTGCTGGAGCA
  CGGGGATCACTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.059
  Max reward: 12.376
  With intrinsic bonuses: 10.059

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9722, entropy=0.4865, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3910

=== Surrogate Model Training ===
Total samples: 1522

Training on 1466 samples (removed 56 outliers)
Reward range: [7.06, 13.13], mean: 10.13
  Created 13 candidate models for data size 1466
Current R2 threshold: 0.06
  rf-tuned-l: R2 = 0.186 (std: 0.066)
  rf-tuned-xl: R2 = 0.189 (std: 0.069)
  gb-tuned-l: R2 = 0.190 (std: 0.041)
  gb-tuned-xl: R2 = 0.190 (std: 0.041)
  xgb-xl: R2 = 0.128 (std: 0.067)
  xgb-l: R2 = 0.128 (std: 0.067)
  mlp-adaptive-xl: R2 = 0.132 (std: 0.081)
  mlp-l: R2 = 0.147 (std: 0.075)
  svr-rbf-xl: R2 = 0.248 (std: 0.074)
  svr-poly-l: R2 = 0.248 (std: 0.074)
  knn-tuned-sqrt: R2 = 0.063 (std: 0.038)
  knn-tuned-l: R2 = 0.063 (std: 0.038)
  ridge: R2 = -0.003 (std: 0.047)

Model-based training with 12 models
Best R2: 0.248, Mean R2: 0.147
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.085 rf-tuned-xl:0.086 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.081 xgb-l:0.081 mlp-adaptive-xl:0.081 mlp-l:0.082 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.076 knn-tuned-l:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.5114, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1302
  Round 1/3: Mean predicted reward = 10.030
    Using performance-based weights
    Model weights: rf-tuned-l:0.085 rf-tuned-xl:0.086 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.081 xgb-l:0.081 mlp-adaptive-xl:0.081 mlp-l:0.082 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.076 knn-tuned-l:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9714, entropy=0.4728, kl_div=0.0000
    Epoch 1: policy_loss=-0.0334, value_loss=0.9714, entropy=0.4741, kl_div=-0.0643
  Round 2/3: Mean predicted reward = 9.957
    Using performance-based weights
    Model weights: rf-tuned-l:0.085 rf-tuned-xl:0.086 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.081 xgb-l:0.081 mlp-adaptive-xl:0.081 mlp-l:0.082 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.076 knn-tuned-l:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9654, entropy=0.4644, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1702
  Round 3/3: Mean predicted reward = 9.933

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 46 Results ---
  Mean Oracle Reward: 10.037
  Min Oracle Reward: 7.235
  Max Oracle Reward: 12.632
  Std Oracle Reward: 1.051
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.147, Max: 0.248, Count: 13
  Total Sequences Evaluated: 1522

======================================================================
EXPERIMENT ROUND 47/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1522

--- Round 47 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AGCTGGGACTAC
  GAGAACTCGCTG
  GGGTTACACGCA
  CTGCGAGACGTC
  ATGCCCGAGGCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.384
  Max reward: 12.372
  With intrinsic bonuses: 10.409

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.4900, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1640

=== Surrogate Model Training ===
Total samples: 1554

Training on 1498 samples (removed 56 outliers)
Reward range: [7.06, 13.13], mean: 10.14
  Created 13 candidate models for data size 1498
Current R2 threshold: 0.07
  rf-tuned-l: R2 = 0.192 (std: 0.063)
  rf-tuned-xl: R2 = 0.190 (std: 0.056)
  gb-tuned-l: R2 = 0.198 (std: 0.036)
  gb-tuned-xl: R2 = 0.198 (std: 0.036)
  xgb-xl: R2 = 0.093 (std: 0.049)
  xgb-l: R2 = 0.093 (std: 0.049)
  mlp-adaptive-xl: R2 = 0.154 (std: 0.046)
  mlp-l: R2 = 0.149 (std: 0.101)
  svr-rbf-xl: R2 = 0.254 (std: 0.069)
  svr-poly-l: R2 = 0.254 (std: 0.069)
  knn-tuned-sqrt: R2 = 0.071 (std: 0.047)
  knn-tuned-l: R2 = 0.071 (std: 0.047)
  ridge: R2 = -0.000 (std: 0.049)

Model-based training with 12 models
Best R2: 0.254, Mean R2: 0.147
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.078 xgb-l:0.078 mlp-adaptive-xl:0.083 mlp-l:0.082 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.076 knn-tuned-l:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.4746, kl_div=0.0000
    Epoch 1: policy_loss=-0.0352, value_loss=0.9694, entropy=0.4752, kl_div=-0.0620
  Round 1/3: Mean predicted reward = 9.903
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.078 xgb-l:0.078 mlp-adaptive-xl:0.083 mlp-l:0.082 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.076 knn-tuned-l:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9719, entropy=0.4622, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1123
  Round 2/3: Mean predicted reward = 10.055
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.078 xgb-l:0.078 mlp-adaptive-xl:0.083 mlp-l:0.082 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.076 knn-tuned-l:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.4886, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2278
  Round 3/3: Mean predicted reward = 10.143

  === Progress Analysis ===
  Status: NORMAL

--- Round 47 Results ---
  Mean Oracle Reward: 10.377
  Min Oracle Reward: 8.821
  Max Oracle Reward: 12.872
  Std Oracle Reward: 1.004
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.147, Max: 0.254, Count: 13
  Total Sequences Evaluated: 1554

======================================================================
EXPERIMENT ROUND 48/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1554

--- Round 48 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCATCGACTGGG
  GCTGGGACCTCA
  GGCACCGAGTAT
  ACGGCGGCACTT
  AGAGTTCACCGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.777
  Max reward: 12.781
  With intrinsic bonuses: 9.803

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=0.4511, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2330

=== Surrogate Model Training ===
Total samples: 1586

Training on 1526 samples (removed 60 outliers)
Reward range: [7.07, 13.10], mean: 10.13
  Created 13 candidate models for data size 1526
Current R2 threshold: 0.08000000000000002
  rf-tuned-l: R2 = 0.200 (std: 0.062)
  rf-tuned-xl: R2 = 0.202 (std: 0.071)
  gb-tuned-l: R2 = 0.198 (std: 0.052)
  gb-tuned-xl: R2 = 0.198 (std: 0.052)
  xgb-xl: R2 = 0.114 (std: 0.080)
  xgb-l: R2 = 0.114 (std: 0.080)
  mlp-adaptive-xl: R2 = 0.150 (std: 0.060)
  mlp-l: R2 = 0.137 (std: 0.090)
  svr-rbf-xl: R2 = 0.261 (std: 0.074)
  svr-poly-l: R2 = 0.261 (std: 0.074)
  knn-tuned-sqrt: R2 = 0.075 (std: 0.070)
  knn-tuned-l: R2 = 0.075 (std: 0.070)
  ridge: R2 = 0.008 (std: 0.063)

Model-based training with 10 models
Best R2: 0.261, Mean R2: 0.153
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.102 rf-tuned-xl:0.102 gb-tuned-l:0.101 gb-tuned-xl:0.101 xgb-xl:0.093 xgb-l:0.093 mlp-adaptive-xl:0.097 mlp-l:0.095 svr-rbf-xl:0.108 svr-poly-l:0.108
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.4700, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0541
  Round 1/3: Mean predicted reward = 9.845
    Using performance-based weights
    Model weights: rf-tuned-l:0.102 rf-tuned-xl:0.102 gb-tuned-l:0.101 gb-tuned-xl:0.101 xgb-xl:0.093 xgb-l:0.093 mlp-adaptive-xl:0.097 mlp-l:0.095 svr-rbf-xl:0.108 svr-poly-l:0.108
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9699, entropy=0.4570, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1553
  Round 2/3: Mean predicted reward = 10.157
    Using performance-based weights
    Model weights: rf-tuned-l:0.102 rf-tuned-xl:0.102 gb-tuned-l:0.101 gb-tuned-xl:0.101 xgb-xl:0.093 xgb-l:0.093 mlp-adaptive-xl:0.097 mlp-l:0.095 svr-rbf-xl:0.108 svr-poly-l:0.108
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.4463, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1652
  Round 3/3: Mean predicted reward = 10.007

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 48 Results ---
  Mean Oracle Reward: 9.816
  Min Oracle Reward: 5.710
  Max Oracle Reward: 12.619
  Std Oracle Reward: 1.475
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.153, Max: 0.261, Count: 13
  Total Sequences Evaluated: 1586

======================================================================
EXPERIMENT ROUND 49/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1586

--- Round 49 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCAGCTCGAGCG
  CGATTGGCCACG
  ATCAGGTCCAGG
  GAAGGTCACTCG
  TGCCGGAGACTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.137
  Max reward: 11.893
  With intrinsic bonuses: 10.180

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9647, entropy=0.4474, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0732

=== Surrogate Model Training ===
Total samples: 1618

Training on 1556 samples (removed 62 outliers)
Reward range: [7.10, 13.10], mean: 10.14
  Created 13 candidate models for data size 1556
Current R2 threshold: 0.09000000000000002
  rf-tuned-l: R2 = 0.210 (std: 0.052)
  rf-tuned-xl: R2 = 0.189 (std: 0.049)
  gb-tuned-l: R2 = 0.206 (std: 0.043)
  gb-tuned-xl: R2 = 0.206 (std: 0.043)
  xgb-xl: R2 = 0.143 (std: 0.069)
  xgb-l: R2 = 0.143 (std: 0.069)
  mlp-adaptive-xl: R2 = 0.160 (std: 0.057)
  mlp-l: R2 = 0.165 (std: 0.080)
  svr-rbf-xl: R2 = 0.269 (std: 0.059)
  svr-poly-l: R2 = 0.269 (std: 0.059)
  knn-tuned-sqrt: R2 = 0.083 (std: 0.050)
  knn-tuned-l: R2 = 0.083 (std: 0.050)
  ridge: R2 = 0.014 (std: 0.048)

Model-based training with 10 models
Best R2: 0.269, Mean R2: 0.165
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.099 gb-tuned-l:0.101 gb-tuned-xl:0.101 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.096 mlp-l:0.097 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.4175, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0696
  Round 1/3: Mean predicted reward = 9.897
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.099 gb-tuned-l:0.101 gb-tuned-xl:0.101 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.096 mlp-l:0.097 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9618, entropy=0.4345, kl_div=0.0000
    Epoch 1: policy_loss=0.0009, value_loss=0.9618, entropy=0.4333, kl_div=0.0228
  Round 2/3: Mean predicted reward = 10.042
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.099 gb-tuned-l:0.101 gb-tuned-xl:0.101 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.096 mlp-l:0.097 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9651, entropy=0.4479, kl_div=0.0000
    Epoch 1: policy_loss=-0.0139, value_loss=0.9651, entropy=0.4480, kl_div=-0.0229
  Round 3/3: Mean predicted reward = 10.168

  === Progress Analysis ===
  Status: NORMAL

--- Round 49 Results ---
  Mean Oracle Reward: 10.191
  Min Oracle Reward: 7.656
  Max Oracle Reward: 11.857
  Std Oracle Reward: 1.031
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.165, Max: 0.269, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  CGCCCGTGTAGA
  GCGCAGGCTTAA
  ATACCTCGGAGG
  GACTCCTGGCAG
  TGCGCCCAGGTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.832
  Max reward: 11.522
  With intrinsic bonuses: 9.783

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.4465, kl_div=0.0000
    Epoch 1: policy_loss=0.0147, value_loss=0.9687, entropy=0.4467, kl_div=-0.1798

=== Surrogate Model Training ===
Total samples: 1650

Training on 1587 samples (removed 63 outliers)
Reward range: [7.10, 12.98], mean: 10.13
  Created 13 candidate models for data size 1587
Current R2 threshold: 0.10000000000000003
  rf-tuned-l: R2 = 0.215 (std: 0.062)
  rf-tuned-xl: R2 = 0.217 (std: 0.058)
  gb-tuned-l: R2 = 0.207 (std: 0.063)
  gb-tuned-xl: R2 = 0.207 (std: 0.063)
  xgb-xl: R2 = 0.154 (std: 0.033)
  xgb-l: R2 = 0.154 (std: 0.033)
  mlp-adaptive-xl: R2 = 0.170 (std: 0.064)
  mlp-l: R2 = 0.171 (std: 0.010)
  svr-rbf-xl: R2 = 0.271 (std: 0.065)
  svr-poly-l: R2 = 0.271 (std: 0.065)
  knn-tuned-sqrt: R2 = 0.081 (std: 0.054)
  knn-tuned-l: R2 = 0.081 (std: 0.054)
  ridge: R2 = 0.012 (std: 0.063)

Model-based training with 10 models
Best R2: 0.271, Mean R2: 0.170
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.101 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.097 mlp-l:0.097 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.4465, kl_div=0.0000
    Epoch 1: policy_loss=-0.0732, value_loss=0.9692, entropy=0.4456, kl_div=0.0398
  Round 1/3: Mean predicted reward = 10.034
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.101 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.097 mlp-l:0.097 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.4508, kl_div=0.0000
    Epoch 1: policy_loss=-0.0479, value_loss=0.9696, entropy=0.4500, kl_div=-0.0192
  Round 2/3: Mean predicted reward = 10.110
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.101 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.097 mlp-l:0.097 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9655, entropy=0.4243, kl_div=0.0000
    Epoch 1: policy_loss=-0.0190, value_loss=0.9655, entropy=0.4294, kl_div=-0.1319
  Round 3/3: Mean predicted reward = 10.158

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 50 Results ---
  Mean Oracle Reward: 9.798
  Min Oracle Reward: 6.996
  Max Oracle Reward: 11.213
  Std Oracle Reward: 0.941
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.170, Max: 0.271, Count: 13
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
  CCTGGTCAAGAG
  CGCGCCGTTAGA
  GTCGCCGGCAAT
  CCTGAGTAGCCG
  AGTCACGCGGTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.099
  Max reward: 11.841
  With intrinsic bonuses: 10.087

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9672, entropy=0.4437, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2528

=== Surrogate Model Training ===
Total samples: 1682

Training on 1616 samples (removed 66 outliers)
Reward range: [7.14, 12.98], mean: 10.14
  Created 13 candidate models for data size 1616
Current R2 threshold: 0.11000000000000004
  rf-tuned-l: R2 = 0.215 (std: 0.065)
  rf-tuned-xl: R2 = 0.222 (std: 0.058)
  gb-tuned-l: R2 = 0.202 (std: 0.060)
  gb-tuned-xl: R2 = 0.202 (std: 0.060)
  xgb-xl: R2 = 0.152 (std: 0.052)
  xgb-l: R2 = 0.152 (std: 0.052)
  mlp-adaptive-xl: R2 = 0.159 (std: 0.070)
  mlp-l: R2 = 0.198 (std: 0.043)
  svr-rbf-xl: R2 = 0.269 (std: 0.062)
  svr-poly-l: R2 = 0.269 (std: 0.062)
  knn-tuned-sqrt: R2 = 0.086 (std: 0.052)
  knn-tuned-l: R2 = 0.086 (std: 0.052)
  ridge: R2 = 0.014 (std: 0.054)

Model-based training with 10 models
Best R2: 0.269, Mean R2: 0.171
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.102 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.096 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.4028, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1409
  Round 1/3: Mean predicted reward = 9.917
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.102 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.096 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9739, entropy=0.4098, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1353
  Round 2/3: Mean predicted reward = 9.964
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.102 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.096 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.4001, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4898
  Round 3/3: Mean predicted reward = 10.263

  === Progress Analysis ===
  Status: NORMAL

--- Round 51 Results ---
  Mean Oracle Reward: 10.050
  Min Oracle Reward: 6.002
  Max Oracle Reward: 11.506
  Std Oracle Reward: 1.045
  Sequence Diversity: 0.969
  Models Used: 10
  Model R2 - Mean: 0.171, Max: 0.269, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  CAGGCAGCTGCT
  GGAGCCCCTGAT
  ACCGTTGAGCCG
  TCTAGGGGACCC
  GGCGTATCACCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.988
  Max reward: 12.946
  With intrinsic bonuses: 9.970

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9736, entropy=0.4021, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1757

=== Surrogate Model Training ===
Total samples: 1714

Training on 1645 samples (removed 69 outliers)
Reward range: [7.17, 12.98], mean: 10.14
  Created 13 candidate models for data size 1645
Current R2 threshold: 0.12
  rf-tuned-l: R2 = 0.214 (std: 0.065)
  rf-tuned-xl: R2 = 0.219 (std: 0.076)
  gb-tuned-l: R2 = 0.198 (std: 0.060)
  gb-tuned-xl: R2 = 0.198 (std: 0.060)
  xgb-xl: R2 = 0.154 (std: 0.068)
  xgb-l: R2 = 0.154 (std: 0.068)
  mlp-adaptive-xl: R2 = 0.199 (std: 0.060)
  mlp-l: R2 = 0.176 (std: 0.039)
  svr-rbf-xl: R2 = 0.272 (std: 0.071)
  svr-poly-l: R2 = 0.272 (std: 0.071)
  knn-tuned-sqrt: R2 = 0.085 (std: 0.046)
  knn-tuned-l: R2 = 0.085 (std: 0.046)
  ridge: R2 = 0.012 (std: 0.054)

Model-based training with 10 models
Best R2: 0.272, Mean R2: 0.172
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.101 gb-tuned-l:0.099 gb-tuned-xl:0.099 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.099 mlp-l:0.097 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.4151, kl_div=0.0000
    Epoch 1: policy_loss=-0.0185, value_loss=0.9685, entropy=0.4162, kl_div=-0.0453
  Round 1/3: Mean predicted reward = 9.892
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.101 gb-tuned-l:0.099 gb-tuned-xl:0.099 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.099 mlp-l:0.097 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9656, entropy=0.3965, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1667
  Round 2/3: Mean predicted reward = 10.049
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.101 gb-tuned-l:0.099 gb-tuned-xl:0.099 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.099 mlp-l:0.097 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9661, entropy=0.4213, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2870
  Round 3/3: Mean predicted reward = 10.212

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 52 Results ---
  Mean Oracle Reward: 9.969
  Min Oracle Reward: 1.524
  Max Oracle Reward: 12.515
  Std Oracle Reward: 1.730
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.172, Max: 0.272, Count: 13
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
  AGCCTTGCGGAC
  TCCGTCGAGAGC
  TACGGCTGACCG
  GCCCGCGAATGT
  GACGATCTAGGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.734
  Max reward: 11.650
  With intrinsic bonuses: 9.678

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9708, entropy=0.3581, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1363

=== Surrogate Model Training ===
Total samples: 1746

Training on 1677 samples (removed 69 outliers)
Reward range: [7.14, 12.98], mean: 10.13
  Created 13 candidate models for data size 1677
Current R2 threshold: 0.13
  rf-tuned-l: R2 = 0.222 (std: 0.064)
  rf-tuned-xl: R2 = 0.226 (std: 0.065)
  gb-tuned-l: R2 = 0.213 (std: 0.060)
  gb-tuned-xl: R2 = 0.213 (std: 0.060)
  xgb-xl: R2 = 0.165 (std: 0.057)
  xgb-l: R2 = 0.165 (std: 0.057)
  mlp-adaptive-xl: R2 = 0.192 (std: 0.046)
  mlp-l: R2 = 0.204 (std: 0.052)
  svr-rbf-xl: R2 = 0.280 (std: 0.060)
  svr-poly-l: R2 = 0.280 (std: 0.060)
  knn-tuned-sqrt: R2 = 0.100 (std: 0.057)
  knn-tuned-l: R2 = 0.100 (std: 0.057)
  ridge: R2 = 0.020 (std: 0.057)

Model-based training with 10 models
Best R2: 0.280, Mean R2: 0.183
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.100 rf-tuned-xl:0.101 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.098 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.3880, kl_div=0.0000
    Epoch 1: policy_loss=-0.0221, value_loss=0.9680, entropy=0.3874, kl_div=0.0333
  Round 1/3: Mean predicted reward = 10.068
    Using performance-based weights
    Model weights: rf-tuned-l:0.100 rf-tuned-xl:0.101 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.098 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9644, entropy=0.3769, kl_div=0.0000
    Epoch 1: policy_loss=-0.0412, value_loss=0.9644, entropy=0.3784, kl_div=-0.1610
  Round 2/3: Mean predicted reward = 9.959
    Using performance-based weights
    Model weights: rf-tuned-l:0.100 rf-tuned-xl:0.101 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.098 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.3772, kl_div=0.0000
    Epoch 1: policy_loss=-0.0385, value_loss=0.9701, entropy=0.3769, kl_div=-0.0060
  Round 3/3: Mean predicted reward = 10.136

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 53 Results ---
  Mean Oracle Reward: 9.733
  Min Oracle Reward: 2.764
  Max Oracle Reward: 11.587
  Std Oracle Reward: 1.698
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.183, Max: 0.280, Count: 13
  Total Sequences Evaluated: 1746

======================================================================
EXPERIMENT ROUND 54/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1746

--- Round 54 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TTACCGCGGGCA
  ATGTCGCAGCCG
  TAGCCTGGGCAA
  TCCGGGCGCTAA
  GCATGCTGACGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.031
  Max reward: 11.895
  With intrinsic bonuses: 9.979

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9725, entropy=0.3882, kl_div=0.0000
    Epoch 1: policy_loss=-0.0327, value_loss=0.9725, entropy=0.3875, kl_div=0.0342

=== Surrogate Model Training ===
Total samples: 1778

Training on 1706 samples (removed 72 outliers)
Reward range: [7.17, 12.98], mean: 10.14
  Created 13 candidate models for data size 1706
Current R2 threshold: 0.14
  rf-tuned-l: R2 = 0.225 (std: 0.053)
  rf-tuned-xl: R2 = 0.219 (std: 0.043)
  gb-tuned-l: R2 = 0.218 (std: 0.054)
  gb-tuned-xl: R2 = 0.218 (std: 0.054)
  xgb-xl: R2 = 0.181 (std: 0.053)
  xgb-l: R2 = 0.181 (std: 0.053)
  mlp-adaptive-xl: R2 = 0.191 (std: 0.041)
  mlp-l: R2 = 0.182 (std: 0.052)
  svr-rbf-xl: R2 = 0.284 (std: 0.057)
  svr-poly-l: R2 = 0.284 (std: 0.057)
  knn-tuned-sqrt: R2 = 0.087 (std: 0.042)
  knn-tuned-l: R2 = 0.087 (std: 0.042)
  ridge: R2 = 0.022 (std: 0.061)

Model-based training with 10 models
Best R2: 0.284, Mean R2: 0.183
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.100 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.096 xgb-l:0.096 mlp-adaptive-xl:0.097 mlp-l:0.096 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9644, entropy=0.3405, kl_div=0.0000
    Epoch 1: policy_loss=-0.0148, value_loss=0.9644, entropy=0.3407, kl_div=-0.0211
  Round 1/3: Mean predicted reward = 9.650
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.100 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.096 xgb-l:0.096 mlp-adaptive-xl:0.097 mlp-l:0.096 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=0.3871, kl_div=0.0000
    Epoch 1: policy_loss=-0.0168, value_loss=0.9675, entropy=0.3879, kl_div=-0.0585
  Round 2/3: Mean predicted reward = 9.916
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.100 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.096 xgb-l:0.096 mlp-adaptive-xl:0.097 mlp-l:0.096 svr-rbf-xl:0.107 svr-poly-l:0.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.3817, kl_div=0.0000
    Epoch 1: policy_loss=-0.0143, value_loss=0.9691, entropy=0.3809, kl_div=0.0326
  Round 3/3: Mean predicted reward = 10.183

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 54 Results ---
  Mean Oracle Reward: 10.025
  Min Oracle Reward: 2.795
  Max Oracle Reward: 11.887
  Std Oracle Reward: 1.535
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.183, Max: 0.284, Count: 13
  Total Sequences Evaluated: 1778

======================================================================
EXPERIMENT ROUND 55/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1778

--- Round 55 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CAGCTGCGCAGT
  CGCCTAGATGCG
  CAGGTGACCCGT
  AGCGGGTCCCTA
  GGTGTCCACGAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.059
  Max reward: 11.752
  With intrinsic bonuses: 10.005

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9664, entropy=0.3851, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5688

=== Surrogate Model Training ===
Total samples: 1810

Training on 1734 samples (removed 76 outliers)
Reward range: [7.18, 12.98], mean: 10.15
  Created 13 candidate models for data size 1734
Current R2 threshold: 0.15000000000000002
  rf-tuned-l: R2 = 0.223 (std: 0.053)
  rf-tuned-xl: R2 = 0.219 (std: 0.058)
  gb-tuned-l: R2 = 0.219 (std: 0.062)
  gb-tuned-xl: R2 = 0.219 (std: 0.062)
  xgb-xl: R2 = 0.162 (std: 0.051)
  xgb-l: R2 = 0.162 (std: 0.051)
  mlp-adaptive-xl: R2 = 0.191 (std: 0.071)
  mlp-l: R2 = 0.182 (std: 0.036)
  svr-rbf-xl: R2 = 0.291 (std: 0.064)
  svr-poly-l: R2 = 0.291 (std: 0.064)
  knn-tuned-sqrt: R2 = 0.088 (std: 0.057)
  knn-tuned-l: R2 = 0.088 (std: 0.057)
  ridge: R2 = 0.027 (std: 0.058)

Model-based training with 10 models
Best R2: 0.291, Mean R2: 0.182
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.100 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.097 mlp-l:0.097 svr-rbf-xl:0.108 svr-poly-l:0.108
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9707, entropy=0.3880, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6572
  Round 1/3: Mean predicted reward = 9.935
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.100 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.097 mlp-l:0.097 svr-rbf-xl:0.108 svr-poly-l:0.108
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9670, entropy=0.3581, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1155
  Round 2/3: Mean predicted reward = 9.926
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.100 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.097 mlp-l:0.097 svr-rbf-xl:0.108 svr-poly-l:0.108
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9672, entropy=0.3513, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6499
  Round 3/3: Mean predicted reward = 10.102

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 55 Results ---
  Mean Oracle Reward: 9.985
  Min Oracle Reward: 4.661
  Max Oracle Reward: 11.693
  Std Oracle Reward: 1.429
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.182, Max: 0.291, Count: 13
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
  GAACCGCCGGTT
  CCGGGTCTCAGA
  TGGCACGCGATC
  CGGCAACTCTGG
  GCCTTCGAAGGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.016
  Max reward: 11.986
  With intrinsic bonuses: 9.985

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.4006, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3654

=== Surrogate Model Training ===
Total samples: 1842

Training on 1762 samples (removed 80 outliers)
Reward range: [7.22, 12.98], mean: 10.15
  Created 13 candidate models for data size 1762
Current R2 threshold: 0.16000000000000003
  rf-tuned-l: R2 = 0.222 (std: 0.058)
  rf-tuned-xl: R2 = 0.217 (std: 0.051)
  gb-tuned-l: R2 = 0.207 (std: 0.049)
  gb-tuned-xl: R2 = 0.207 (std: 0.049)
  xgb-xl: R2 = 0.167 (std: 0.040)
  xgb-l: R2 = 0.167 (std: 0.040)
  mlp-adaptive-xl: R2 = 0.164 (std: 0.010)
  mlp-l: R2 = 0.177 (std: 0.048)
  svr-rbf-xl: R2 = 0.285 (std: 0.048)
  svr-poly-l: R2 = 0.285 (std: 0.048)
  knn-tuned-sqrt: R2 = 0.082 (std: 0.053)
  knn-tuned-l: R2 = 0.082 (std: 0.053)
  ridge: R2 = 0.024 (std: 0.053)

Model-based training with 10 models
Best R2: 0.285, Mean R2: 0.176
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.101 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.096 xgb-l:0.096 mlp-adaptive-xl:0.095 mlp-l:0.097 svr-rbf-xl:0.108 svr-poly-l:0.108
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.3627, kl_div=0.0000
    Epoch 1: policy_loss=-0.0341, value_loss=0.9691, entropy=0.3568, kl_div=0.0038
  Round 1/3: Mean predicted reward = 9.787
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.101 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.096 xgb-l:0.096 mlp-adaptive-xl:0.095 mlp-l:0.097 svr-rbf-xl:0.108 svr-poly-l:0.108
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.3641, kl_div=0.0000
    Epoch 1: policy_loss=-0.0543, value_loss=0.9689, entropy=0.3642, kl_div=-0.1083
  Round 2/3: Mean predicted reward = 9.963
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.101 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.096 xgb-l:0.096 mlp-adaptive-xl:0.095 mlp-l:0.097 svr-rbf-xl:0.108 svr-poly-l:0.108
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9718, entropy=0.3449, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4800
  Round 3/3: Mean predicted reward = 9.921

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 56 Results ---
  Mean Oracle Reward: 9.999
  Min Oracle Reward: 6.934
  Max Oracle Reward: 12.096
  Std Oracle Reward: 1.066
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.176, Max: 0.285, Count: 13
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
  GGACCTACTGGC
  AGACCCGTTGGC
  GTCCCAGGCGAT
  ACTTAGCGCGCG
  GCAGTAGTCGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.091
  Max reward: 11.747
  With intrinsic bonuses: 10.116

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9685, entropy=0.3496, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1546

=== Surrogate Model Training ===
Total samples: 1874

Training on 1790 samples (removed 84 outliers)
Reward range: [7.25, 12.88], mean: 10.15
  Created 13 candidate models for data size 1790
Current R2 threshold: 0.17000000000000004
  rf-tuned-l: R2 = 0.208 (std: 0.037)
  rf-tuned-xl: R2 = 0.206 (std: 0.030)
  gb-tuned-l: R2 = 0.206 (std: 0.040)
  gb-tuned-xl: R2 = 0.206 (std: 0.040)
  xgb-xl: R2 = 0.156 (std: 0.057)
  xgb-l: R2 = 0.156 (std: 0.057)
  mlp-adaptive-xl: R2 = 0.170 (std: 0.061)
  mlp-l: R2 = 0.200 (std: 0.054)
  svr-rbf-xl: R2 = 0.280 (std: 0.040)
  svr-poly-l: R2 = 0.280 (std: 0.040)
  knn-tuned-sqrt: R2 = 0.063 (std: 0.038)
  knn-tuned-l: R2 = 0.063 (std: 0.038)
  ridge: R2 = 0.030 (std: 0.048)

Model-based training with 7 models
Best R2: 0.280, Mean R2: 0.171
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.140 rf-tuned-xl:0.140 gb-tuned-l:0.140 gb-tuned-xl:0.140 mlp-l:0.139 svr-rbf-xl:0.151 svr-poly-l:0.151
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9676, entropy=0.3099, kl_div=0.0000
    Epoch 1: policy_loss=-0.0061, value_loss=0.9676, entropy=0.3104, kl_div=0.0036
  Round 1/3: Mean predicted reward = 9.873
    Using performance-based weights
    Model weights: rf-tuned-l:0.140 rf-tuned-xl:0.140 gb-tuned-l:0.140 gb-tuned-xl:0.140 mlp-l:0.139 svr-rbf-xl:0.151 svr-poly-l:0.151
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9649, entropy=0.3779, kl_div=0.0000
    Epoch 1: policy_loss=0.0148, value_loss=0.9649, entropy=0.3798, kl_div=-0.2339
  Round 2/3: Mean predicted reward = 9.993
    Using performance-based weights
    Model weights: rf-tuned-l:0.140 rf-tuned-xl:0.140 gb-tuned-l:0.140 gb-tuned-xl:0.140 mlp-l:0.139 svr-rbf-xl:0.151 svr-poly-l:0.151
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9722, entropy=0.3616, kl_div=0.0000
    Epoch 1: policy_loss=-0.0643, value_loss=0.9722, entropy=0.3632, kl_div=-0.0070
  Round 3/3: Mean predicted reward = 10.068

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 57 Results ---
  Mean Oracle Reward: 10.031
  Min Oracle Reward: 7.346
  Max Oracle Reward: 11.402
  Std Oracle Reward: 0.886
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: 0.171, Max: 0.280, Count: 13
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
  CTCAGCGGCGTA
  TCACGGCATGCG
  TCCGCGCGAGTA
  GGATGCCTACGC
  ACAGCGGCTTCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.071
  Max reward: 12.432
  With intrinsic bonuses: 10.122

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9673, entropy=0.3476, kl_div=0.0000
    Epoch 1: policy_loss=-0.0209, value_loss=0.9673, entropy=0.3493, kl_div=-0.0841

=== Surrogate Model Training ===
Total samples: 1906

Training on 1819 samples (removed 87 outliers)
Reward range: [7.26, 12.88], mean: 10.16
  Created 13 candidate models for data size 1819
Current R2 threshold: 0.18
  rf-tuned-l: R2 = 0.198 (std: 0.040)
  rf-tuned-xl: R2 = 0.212 (std: 0.033)
  gb-tuned-l: R2 = 0.209 (std: 0.048)
  gb-tuned-xl: R2 = 0.209 (std: 0.048)
  xgb-xl: R2 = 0.135 (std: 0.041)
  xgb-l: R2 = 0.135 (std: 0.041)
  mlp-adaptive-xl: R2 = 0.211 (std: 0.028)
  mlp-l: R2 = 0.188 (std: 0.049)
  svr-rbf-xl: R2 = 0.278 (std: 0.038)
  svr-poly-l: R2 = 0.278 (std: 0.038)
  knn-tuned-sqrt: R2 = 0.078 (std: 0.031)
  knn-tuned-l: R2 = 0.078 (std: 0.031)
  ridge: R2 = 0.033 (std: 0.048)

Model-based training with 8 models
Best R2: 0.278, Mean R2: 0.172
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.122 rf-tuned-xl:0.124 gb-tuned-l:0.123 gb-tuned-xl:0.123 mlp-adaptive-xl:0.123 mlp-l:0.121 svr-rbf-xl:0.132 svr-poly-l:0.132
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.3284, kl_div=0.0000
    Epoch 1: policy_loss=-0.0301, value_loss=0.9684, entropy=0.3306, kl_div=-0.0642
  Round 1/3: Mean predicted reward = 9.757
    Using performance-based weights
    Model weights: rf-tuned-l:0.122 rf-tuned-xl:0.124 gb-tuned-l:0.123 gb-tuned-xl:0.123 mlp-adaptive-xl:0.123 mlp-l:0.121 svr-rbf-xl:0.132 svr-poly-l:0.132
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.3446, kl_div=0.0000
    Epoch 1: policy_loss=-0.0434, value_loss=0.9701, entropy=0.3469, kl_div=-0.1766
  Round 2/3: Mean predicted reward = 9.793
    Using performance-based weights
    Model weights: rf-tuned-l:0.122 rf-tuned-xl:0.124 gb-tuned-l:0.123 gb-tuned-xl:0.123 mlp-adaptive-xl:0.123 mlp-l:0.121 svr-rbf-xl:0.132 svr-poly-l:0.132
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3412, kl_div=0.0000
    Epoch 1: policy_loss=-0.0313, value_loss=0.9689, entropy=0.3425, kl_div=-0.1535
  Round 3/3: Mean predicted reward = 10.035

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 58 Results ---
  Mean Oracle Reward: 10.088
  Min Oracle Reward: 4.808
  Max Oracle Reward: 12.559
  Std Oracle Reward: 1.290
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: 0.172, Max: 0.278, Count: 13
  Total Sequences Evaluated: 1906

======================================================================
EXPERIMENT ROUND 59/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1906
  Performance plateaued, reducing LR to 0.000019

--- Round 59 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ACGCCGAGTGTC
  CAGCGTCGACGT
  GATATCCCGGAG
  TCGCGTCAGCAG
  AGCTGCGCTAGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.956
  Max reward: 12.813
  With intrinsic bonuses: 9.935

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.3254, kl_div=0.0000
    Epoch 1: policy_loss=-0.0143, value_loss=0.9684, entropy=0.3258, kl_div=-0.0205

=== Surrogate Model Training ===
Total samples: 1938

Training on 1850 samples (removed 88 outliers)
Reward range: [7.25, 12.88], mean: 10.15
  Created 13 candidate models for data size 1850
Current R2 threshold: 0.19
  rf-tuned-l: R2 = 0.203 (std: 0.045)
  rf-tuned-xl: R2 = 0.207 (std: 0.038)
  gb-tuned-l: R2 = 0.208 (std: 0.051)
  gb-tuned-xl: R2 = 0.208 (std: 0.051)
  xgb-xl: R2 = 0.150 (std: 0.056)
  xgb-l: R2 = 0.150 (std: 0.056)
  mlp-adaptive-xl: R2 = 0.169 (std: 0.070)
  mlp-l: R2 = 0.217 (std: 0.052)
  svr-rbf-xl: R2 = 0.280 (std: 0.045)
  svr-poly-l: R2 = 0.280 (std: 0.045)
  knn-tuned-sqrt: R2 = 0.071 (std: 0.033)
  knn-tuned-l: R2 = 0.071 (std: 0.033)
  ridge: R2 = 0.032 (std: 0.050)

Model-based training with 7 models
Best R2: 0.280, Mean R2: 0.173
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.139 rf-tuned-xl:0.140 gb-tuned-l:0.140 gb-tuned-xl:0.140 mlp-l:0.141 svr-rbf-xl:0.150 svr-poly-l:0.150
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.3398, kl_div=0.0000
    Epoch 1: policy_loss=-0.0326, value_loss=0.9680, entropy=0.3403, kl_div=-0.0440
  Round 1/3: Mean predicted reward = 9.600
    Using performance-based weights
    Model weights: rf-tuned-l:0.139 rf-tuned-xl:0.140 gb-tuned-l:0.140 gb-tuned-xl:0.140 mlp-l:0.141 svr-rbf-xl:0.150 svr-poly-l:0.150
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=0.3432, kl_div=0.0000
    Epoch 1: policy_loss=-0.0133, value_loss=0.9678, entropy=0.3439, kl_div=-0.0871
  Round 2/3: Mean predicted reward = 9.928
    Using performance-based weights
    Model weights: rf-tuned-l:0.139 rf-tuned-xl:0.140 gb-tuned-l:0.140 gb-tuned-xl:0.140 mlp-l:0.141 svr-rbf-xl:0.150 svr-poly-l:0.150
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.3458, kl_div=0.0000
    Epoch 1: policy_loss=-0.0117, value_loss=0.9690, entropy=0.3465, kl_div=-0.0595
  Round 3/3: Mean predicted reward = 9.997

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 59 Results ---
  Mean Oracle Reward: 9.973
  Min Oracle Reward: 6.997
  Max Oracle Reward: 12.917
  Std Oracle Reward: 1.231
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: 0.173, Max: 0.280, Count: 13
  Total Sequences Evaluated: 1938

======================================================================
EXPERIMENT ROUND 60/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1938
  Performance plateaued, reducing LR to 0.000150

--- Round 60 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGTAGTCGCGCA
  CGACGTGCACTG
  GTGTCCGGAACC
  GGCACCATAGGT
  AGAACCTGGCTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.036
  Max reward: 12.562
  With intrinsic bonuses: 9.959

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.3126, kl_div=0.0000
    Epoch 1: policy_loss=0.0875, value_loss=0.9685, entropy=0.3172, kl_div=-0.3194

=== Surrogate Model Training ===
Total samples: 1970

Training on 1881 samples (removed 89 outliers)
Reward range: [7.26, 12.88], mean: 10.15
  Created 13 candidate models for data size 1881
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.213 (std: 0.049)
  rf-tuned-xl: R2 = 0.214 (std: 0.057)
  gb-tuned-l: R2 = 0.213 (std: 0.043)
  gb-tuned-xl: R2 = 0.213 (std: 0.043)
  xgb-xl: R2 = 0.132 (std: 0.065)
  xgb-l: R2 = 0.132 (std: 0.065)
  mlp-adaptive-xl: R2 = 0.200 (std: 0.092)
  mlp-l: R2 = 0.198 (std: 0.064)
  svr-rbf-xl: R2 = 0.287 (std: 0.048)
  svr-poly-l: R2 = 0.287 (std: 0.048)
  knn-tuned-sqrt: R2 = 0.078 (std: 0.039)
  knn-tuned-l: R2 = 0.078 (std: 0.039)
  ridge: R2 = 0.035 (std: 0.053)

Model-based training with 6 models
Best R2: 0.287, Mean R2: 0.175
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.163 rf-tuned-xl:0.163 gb-tuned-l:0.162 gb-tuned-xl:0.162 svr-rbf-xl:0.175 svr-poly-l:0.175
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=0.3600, kl_div=0.0000
    Epoch 1: policy_loss=0.0390, value_loss=0.9678, entropy=0.3626, kl_div=-0.2761
  Round 1/3: Mean predicted reward = 9.927
    Using performance-based weights
    Model weights: rf-tuned-l:0.163 rf-tuned-xl:0.163 gb-tuned-l:0.162 gb-tuned-xl:0.162 svr-rbf-xl:0.175 svr-poly-l:0.175
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9670, entropy=0.3921, kl_div=0.0000
    Epoch 1: policy_loss=-0.0210, value_loss=0.9670, entropy=0.3958, kl_div=-0.2339
  Round 2/3: Mean predicted reward = 9.943
    Using performance-based weights
    Model weights: rf-tuned-l:0.163 rf-tuned-xl:0.163 gb-tuned-l:0.162 gb-tuned-xl:0.162 svr-rbf-xl:0.175 svr-poly-l:0.175
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=0.3575, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0756
  Round 3/3: Mean predicted reward = 10.095

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 60 Results ---
  Mean Oracle Reward: 10.070
  Min Oracle Reward: 8.180
  Max Oracle Reward: 12.453
  Std Oracle Reward: 0.952
  Sequence Diversity: 1.000
  Models Used: 6
  Model R2 - Mean: 0.175, Max: 0.287, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  GTGAACCGTCGC
  AGGGAGATTCCC
  CAGACGATCGTG
  CGGGTCACGCTA
  CGCAGCATGGCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.216
  Max reward: 12.100
  With intrinsic bonuses: 10.299

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9702, entropy=0.3324, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2434

=== Surrogate Model Training ===
Total samples: 2002

Training on 1913 samples (removed 89 outliers)
Reward range: [7.26, 12.88], mean: 10.16
  Created 13 candidate models for data size 1913
Current R2 threshold: 0.21000000000000002
  rf-tuned-l: R2 = 0.211 (std: 0.043)
  rf-tuned-xl: R2 = 0.205 (std: 0.056)
  gb-tuned-l: R2 = 0.212 (std: 0.053)
  gb-tuned-xl: R2 = 0.212 (std: 0.053)
  xgb-xl: R2 = 0.155 (std: 0.049)
  xgb-l: R2 = 0.155 (std: 0.049)
  mlp-adaptive-xl: R2 = 0.196 (std: 0.056)
  mlp-l: R2 = 0.207 (std: 0.054)
  svr-rbf-xl: R2 = 0.292 (std: 0.042)
  svr-poly-l: R2 = 0.292 (std: 0.042)
  knn-tuned-sqrt: R2 = 0.085 (std: 0.042)
  knn-tuned-l: R2 = 0.085 (std: 0.042)
  ridge: R2 = 0.036 (std: 0.048)

Model-based training with 5 models
Best R2: 0.292, Mean R2: 0.180
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.193 gb-tuned-l:0.194 gb-tuned-xl:0.194 svr-rbf-xl:0.210 svr-poly-l:0.210
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9632, entropy=0.3423, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0818
  Round 1/3: Mean predicted reward = 9.727
    Using performance-based weights
    Model weights: rf-tuned-l:0.193 gb-tuned-l:0.194 gb-tuned-xl:0.194 svr-rbf-xl:0.210 svr-poly-l:0.210
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.3706, kl_div=0.0000
    Epoch 1: policy_loss=-0.0312, value_loss=0.9685, entropy=0.3714, kl_div=-0.0968
  Round 2/3: Mean predicted reward = 10.008
    Using performance-based weights
    Model weights: rf-tuned-l:0.193 gb-tuned-l:0.194 gb-tuned-xl:0.194 svr-rbf-xl:0.210 svr-poly-l:0.210
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9664, entropy=0.3472, kl_div=0.0000
    Epoch 1: policy_loss=-0.0645, value_loss=0.9664, entropy=0.3481, kl_div=-0.0390
  Round 3/3: Mean predicted reward = 10.151

  === Progress Analysis ===
  Status: NORMAL

--- Round 61 Results ---
  Mean Oracle Reward: 10.244
  Min Oracle Reward: 8.167
  Max Oracle Reward: 11.963
  Std Oracle Reward: 0.955
  Sequence Diversity: 1.000
  Models Used: 5
  Model R2 - Mean: 0.180, Max: 0.292, Count: 13
  Total Sequences Evaluated: 2002

======================================================================
EXPERIMENT ROUND 62/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2002
  Consistent improvement, increasing LR to 0.000240

--- Round 62 Configuration ---
Learning rate: 0.000240
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGCCGGGCATAC
  CGCAGGTACTGC
  CCGGATCGACGT
  GGCCAAGCTTGC
  GCCTGGACATCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.542
  Max reward: 12.119
  With intrinsic bonuses: 10.474

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.3284, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2232

=== Surrogate Model Training ===
Total samples: 2034

Training on 1945 samples (removed 89 outliers)
Reward range: [7.26, 12.88], mean: 10.16
  Created 13 candidate models for data size 1945
Current R2 threshold: 0.22000000000000003
  rf-tuned-l: R2 = 0.216 (std: 0.059)
  rf-tuned-xl: R2 = 0.213 (std: 0.058)
  gb-tuned-l: R2 = 0.218 (std: 0.045)
  gb-tuned-xl: R2 = 0.218 (std: 0.045)
  xgb-xl: R2 = 0.134 (std: 0.073)
  xgb-l: R2 = 0.134 (std: 0.073)
  mlp-adaptive-xl: R2 = 0.194 (std: 0.059)
  mlp-l: R2 = 0.181 (std: 0.031)
  svr-rbf-xl: R2 = 0.297 (std: 0.040)
  svr-poly-l: R2 = 0.297 (std: 0.040)
  knn-tuned-sqrt: R2 = 0.093 (std: 0.053)
  knn-tuned-l: R2 = 0.093 (std: 0.053)
  ridge: R2 = 0.035 (std: 0.044)

Model-based training with 2 models
Best R2: 0.297, Mean R2: 0.179
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.3323, kl_div=0.0000
    Epoch 1: policy_loss=-0.0257, value_loss=0.9691, entropy=0.3364, kl_div=-0.1153
  Round 1/3: Mean predicted reward = 9.807
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9675, entropy=0.3356, kl_div=0.0000
    Epoch 1: policy_loss=0.0564, value_loss=0.9675, entropy=0.3432, kl_div=-0.5276
  Round 2/3: Mean predicted reward = 10.007
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9631, entropy=0.3520, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0559
  Round 3/3: Mean predicted reward = 10.172

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 62 Results ---
  Mean Oracle Reward: 10.507
  Min Oracle Reward: 8.349
  Max Oracle Reward: 11.994
  Std Oracle Reward: 0.899
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.179, Max: 0.297, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 2034

======================================================================
EXPERIMENT ROUND 63/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2034
  Consistent improvement, increasing LR to 0.000132

--- Round 63 Configuration ---
Learning rate: 0.000132
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CATTAGCGGCGC
  GCGATATCGACG
  GAGTCCCCAGGT
  GGCTACTCGGAC
  AGGATCGTCGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.023
  Max reward: 12.228
  With intrinsic bonuses: 10.045

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9712, entropy=0.3491, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0990

=== Surrogate Model Training ===
Total samples: 2066

Training on 1974 samples (removed 92 outliers)
Reward range: [7.29, 12.88], mean: 10.16
  Created 13 candidate models for data size 1974
Current R2 threshold: 0.23000000000000004
  rf-tuned-l: R2 = 0.221 (std: 0.058)
  rf-tuned-xl: R2 = 0.215 (std: 0.054)
  gb-tuned-l: R2 = 0.217 (std: 0.049)
  gb-tuned-xl: R2 = 0.217 (std: 0.049)
  xgb-xl: R2 = 0.165 (std: 0.065)
  xgb-l: R2 = 0.165 (std: 0.065)
  mlp-adaptive-xl: R2 = 0.180 (std: 0.039)
  mlp-l: R2 = 0.204 (std: 0.049)
  svr-rbf-xl: R2 = 0.294 (std: 0.046)
  svr-poly-l: R2 = 0.294 (std: 0.046)
  knn-tuned-sqrt: R2 = 0.089 (std: 0.062)
  knn-tuned-l: R2 = 0.089 (std: 0.062)
  ridge: R2 = 0.036 (std: 0.044)

Model-based training with 2 models
Best R2: 0.294, Mean R2: 0.184
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.3391, kl_div=0.0000
    Epoch 1: policy_loss=-0.0406, value_loss=0.9705, entropy=0.3394, kl_div=-0.0107
  Round 1/3: Mean predicted reward = 9.955
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.3689, kl_div=0.0000
    Epoch 1: policy_loss=-0.0150, value_loss=0.9692, entropy=0.3736, kl_div=-0.2439
  Round 2/3: Mean predicted reward = 10.110
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9695, entropy=0.3646, kl_div=0.0000
    Epoch 1: policy_loss=-0.0320, value_loss=0.9695, entropy=0.3681, kl_div=-0.1247
  Round 3/3: Mean predicted reward = 10.068

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 63 Results ---
  Mean Oracle Reward: 9.953
  Min Oracle Reward: 3.800
  Max Oracle Reward: 12.255
  Std Oracle Reward: 1.465
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.184, Max: 0.294, Count: 13
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
  CGCTCGGCAAGT
  CGGCGTGCCATA
  CGTTGGGACCAC
  CTCCCTGAGGAG
  TGCGTCCAAGGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.977
  Max reward: 11.897
  With intrinsic bonuses: 9.975

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9666, entropy=0.3535, kl_div=0.0000
    Epoch 1: policy_loss=-0.0098, value_loss=0.9666, entropy=0.3534, kl_div=0.0128

=== Surrogate Model Training ===
Total samples: 2098

Training on 2004 samples (removed 94 outliers)
Reward range: [7.30, 12.88], mean: 10.16
  Created 13 candidate models for data size 2004
Current R2 threshold: 0.24000000000000005
  rf-tuned-l: R2 = 0.220 (std: 0.058)
  rf-tuned-xl: R2 = 0.223 (std: 0.056)
  gb-tuned-l: R2 = 0.213 (std: 0.052)
  gb-tuned-xl: R2 = 0.213 (std: 0.052)
  xgb-xl: R2 = 0.162 (std: 0.079)
  xgb-l: R2 = 0.162 (std: 0.079)
  mlp-adaptive-xl: R2 = 0.152 (std: 0.039)
  mlp-l: R2 = 0.159 (std: 0.045)
  svr-rbf-xl: R2 = 0.287 (std: 0.044)
  svr-poly-l: R2 = 0.287 (std: 0.044)
  knn-tuned-sqrt: R2 = 0.092 (std: 0.045)
  knn-tuned-l: R2 = 0.092 (std: 0.045)
  ridge: R2 = 0.039 (std: 0.052)

Model-based training with 2 models
Best R2: 0.287, Mean R2: 0.177
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9670, entropy=0.3496, kl_div=0.0000
    Epoch 1: policy_loss=-0.0047, value_loss=0.9670, entropy=0.3496, kl_div=-0.0040
  Round 1/3: Mean predicted reward = 9.598
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9668, entropy=0.3628, kl_div=0.0000
    Epoch 1: policy_loss=-0.0195, value_loss=0.9668, entropy=0.3635, kl_div=-0.0388
  Round 2/3: Mean predicted reward = 9.953
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9661, entropy=0.3598, kl_div=0.0000
    Epoch 1: policy_loss=-0.0186, value_loss=0.9661, entropy=0.3597, kl_div=0.0387
  Round 3/3: Mean predicted reward = 10.353

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 64 Results ---
  Mean Oracle Reward: 9.947
  Min Oracle Reward: 7.564
  Max Oracle Reward: 11.833
  Std Oracle Reward: 0.950
  Sequence Diversity: 0.969
  Models Used: 2
  Model R2 - Mean: 0.177, Max: 0.287, Count: 13
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

--- Generated Sequences (Diversity: 0.969) ---
  CGGTGGCCCTAA
  CTCCAGCGGATG
  CAGATACTGGCG
  GGTCGAACCGTC
  AGCGCGATCCTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.169
  Max reward: 12.124
  With intrinsic bonuses: 10.243

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.3568, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2881

=== Surrogate Model Training ===
Total samples: 2130

Training on 2034 samples (removed 96 outliers)
Reward range: [7.36, 12.88], mean: 10.17
  Created 13 candidate models for data size 2034
Current R2 threshold: 0.25000000000000006
  rf-tuned-l: R2 = 0.215 (std: 0.061)
  rf-tuned-xl: R2 = 0.210 (std: 0.063)
  gb-tuned-l: R2 = 0.216 (std: 0.039)
  gb-tuned-xl: R2 = 0.216 (std: 0.039)
  xgb-xl: R2 = 0.143 (std: 0.069)
  xgb-l: R2 = 0.143 (std: 0.069)
  mlp-adaptive-xl: R2 = 0.193 (std: 0.043)
  mlp-l: R2 = 0.198 (std: 0.051)
  svr-rbf-xl: R2 = 0.290 (std: 0.049)
  svr-poly-l: R2 = 0.290 (std: 0.049)
  knn-tuned-sqrt: R2 = 0.093 (std: 0.058)
  knn-tuned-l: R2 = 0.093 (std: 0.058)
  ridge: R2 = 0.036 (std: 0.046)

Model-based training with 2 models
Best R2: 0.290, Mean R2: 0.180
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.3456, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0849
  Round 1/3: Mean predicted reward = 9.942
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=0.3406, kl_div=0.0000
    Epoch 1: policy_loss=-0.0225, value_loss=0.9704, entropy=0.3433, kl_div=0.0336
  Round 2/3: Mean predicted reward = 10.067
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.3807, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1786
  Round 3/3: Mean predicted reward = 10.070

  === Progress Analysis ===
  Status: NORMAL

--- Round 65 Results ---
  Mean Oracle Reward: 10.217
  Min Oracle Reward: 5.589
  Max Oracle Reward: 12.277
  Std Oracle Reward: 1.228
  Sequence Diversity: 0.969
  Models Used: 2
  Model R2 - Mean: 0.180, Max: 0.290, Count: 13
  Total Sequences Evaluated: 2130

======================================================================
EXPERIMENT ROUND 66/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2130
  Performance plateaued, reducing LR to 0.000136

--- Round 66 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTCCTGGAAACG
  TGCGCCACGGTA
  CTGGGGCTAACC
  CCCCGGTGTAGA
  GCACTCGAGTGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.226
  Max reward: 12.992
  With intrinsic bonuses: 10.174

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.3393, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2432

=== Surrogate Model Training ===
Total samples: 2162

Training on 2067 samples (removed 95 outliers)
Reward range: [7.29, 12.95], mean: 10.17
  Created 13 candidate models for data size 2067
Current R2 threshold: 0.26000000000000006
  rf-tuned-l: R2 = 0.213 (std: 0.051)
  rf-tuned-xl: R2 = 0.202 (std: 0.053)
  gb-tuned-l: R2 = 0.218 (std: 0.028)
  gb-tuned-xl: R2 = 0.218 (std: 0.028)
  xgb-xl: R2 = 0.158 (std: 0.053)
  xgb-l: R2 = 0.158 (std: 0.053)
  mlp-adaptive-xl: R2 = 0.203 (std: 0.034)
  mlp-l: R2 = 0.169 (std: 0.078)
  svr-rbf-xl: R2 = 0.293 (std: 0.041)
  svr-poly-l: R2 = 0.293 (std: 0.041)
  knn-tuned-sqrt: R2 = 0.089 (std: 0.054)
  knn-tuned-l: R2 = 0.089 (std: 0.054)
  ridge: R2 = 0.033 (std: 0.037)

Model-based training with 2 models
Best R2: 0.293, Mean R2: 0.180
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9670, entropy=0.3575, kl_div=0.0000
    Epoch 1: policy_loss=-0.0282, value_loss=0.9670, entropy=0.3583, kl_div=0.0010
  Round 1/3: Mean predicted reward = 9.783
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9685, entropy=0.3486, kl_div=0.0000
    Epoch 1: policy_loss=0.0088, value_loss=0.9685, entropy=0.3507, kl_div=-0.1660
  Round 2/3: Mean predicted reward = 9.926
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9675, entropy=0.3249, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1463
  Round 3/3: Mean predicted reward = 10.132

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 66 Results ---
  Mean Oracle Reward: 10.194
  Min Oracle Reward: 5.741
  Max Oracle Reward: 13.045
  Std Oracle Reward: 1.449
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.180, Max: 0.293, Count: 13
  Total Sequences Evaluated: 2162

======================================================================
EXPERIMENT ROUND 67/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2162
  Consistent improvement, increasing LR to 0.000240

--- Round 67 Configuration ---
Learning rate: 0.000240
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCCCGAACGGTT
  CCTCTAGAGCGG
  CCCAGACTTGGG
  AATGCCCGGTCG
  CCGCGGTAGATC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.111
  Max reward: 12.062
  With intrinsic bonuses: 10.142

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9667, entropy=0.3793, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5121

=== Surrogate Model Training ===
Total samples: 2194

Training on 2094 samples (removed 100 outliers)
Reward range: [7.36, 12.88], mean: 10.17
  Created 13 candidate models for data size 2094
Current R2 threshold: 0.2700000000000001
  rf-tuned-l: R2 = 0.222 (std: 0.045)
  rf-tuned-xl: R2 = 0.221 (std: 0.052)
  gb-tuned-l: R2 = 0.214 (std: 0.038)
  gb-tuned-xl: R2 = 0.214 (std: 0.038)
  xgb-xl: R2 = 0.158 (std: 0.083)
  xgb-l: R2 = 0.158 (std: 0.083)
  mlp-adaptive-xl: R2 = 0.206 (std: 0.047)
  mlp-l: R2 = 0.190 (std: 0.059)
  svr-rbf-xl: R2 = 0.298 (std: 0.047)
  svr-poly-l: R2 = 0.298 (std: 0.047)
  knn-tuned-sqrt: R2 = 0.086 (std: 0.050)
  knn-tuned-l: R2 = 0.086 (std: 0.050)
  ridge: R2 = 0.035 (std: 0.036)

Model-based training with 2 models
Best R2: 0.298, Mean R2: 0.184
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9669, entropy=0.3625, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1242
  Round 1/3: Mean predicted reward = 9.725
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.3296, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3978
  Round 2/3: Mean predicted reward = 10.162
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.3283, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3267
  Round 3/3: Mean predicted reward = 10.028

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 67 Results ---
  Mean Oracle Reward: 10.083
  Min Oracle Reward: 5.170
  Max Oracle Reward: 12.027
  Std Oracle Reward: 1.156
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.184, Max: 0.298, Count: 13
  Total Sequences Evaluated: 2194

======================================================================
EXPERIMENT ROUND 68/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2194
  Performance plateaued, reducing LR to 0.000055

--- Round 68 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GACCTGGCACGT
  GTGACAGGCCCT
  ACAGCTGGGCCT
  TGGCCTGACCGA
  GTCTGCCAGGCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.561
  Max reward: 13.221
  With intrinsic bonuses: 10.539

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.3608, kl_div=0.0000
    Epoch 1: policy_loss=-0.0472, value_loss=0.9690, entropy=0.3579, kl_div=0.0340

=== Surrogate Model Training ===
Total samples: 2226

Training on 2124 samples (removed 102 outliers)
Reward range: [7.36, 12.88], mean: 10.18
  Created 13 candidate models for data size 2124
Current R2 threshold: 0.27999999999999997
  rf-tuned-l: R2 = 0.232 (std: 0.053)
  rf-tuned-xl: R2 = 0.233 (std: 0.049)
  gb-tuned-l: R2 = 0.215 (std: 0.039)
  gb-tuned-xl: R2 = 0.215 (std: 0.039)
  xgb-xl: R2 = 0.163 (std: 0.076)
  xgb-l: R2 = 0.163 (std: 0.076)
  mlp-adaptive-xl: R2 = 0.191 (std: 0.060)
  mlp-l: R2 = 0.193 (std: 0.053)
  svr-rbf-xl: R2 = 0.297 (std: 0.049)
  svr-poly-l: R2 = 0.297 (std: 0.049)
  knn-tuned-sqrt: R2 = 0.099 (std: 0.050)
  knn-tuned-l: R2 = 0.099 (std: 0.050)
  ridge: R2 = 0.033 (std: 0.042)

Model-based training with 2 models
Best R2: 0.297, Mean R2: 0.187
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.3509, kl_div=0.0000
    Epoch 1: policy_loss=0.0103, value_loss=0.9696, entropy=0.3489, kl_div=0.0155
  Round 1/3: Mean predicted reward = 9.882
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9712, entropy=0.3183, kl_div=0.0000
    Epoch 1: policy_loss=-0.0248, value_loss=0.9712, entropy=0.3179, kl_div=-0.0395
  Round 2/3: Mean predicted reward = 9.997
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9682, entropy=0.3015, kl_div=0.0000
    Epoch 1: policy_loss=-0.0242, value_loss=0.9682, entropy=0.3015, kl_div=-0.0490
  Round 3/3: Mean predicted reward = 10.011

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 68 Results ---
  Mean Oracle Reward: 10.534
  Min Oracle Reward: 6.631
  Max Oracle Reward: 13.419
  Std Oracle Reward: 1.283
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.187, Max: 0.297, Count: 13
  New best mean reward!
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

--- Generated Sequences (Diversity: 1.000) ---
  GATTGGCGCCCA
  GCGGACCATCGT
  ATCACGTGGGCC
  ACTGCGAGCTCG
  GTCTCAGCGACG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.421
  Max reward: 11.777
  With intrinsic bonuses: 10.417

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9672, entropy=0.3463, kl_div=0.0000
    Epoch 1: policy_loss=-0.0143, value_loss=0.9672, entropy=0.3466, kl_div=-0.0218

=== Surrogate Model Training ===
Total samples: 2258

Training on 2156 samples (removed 102 outliers)
Reward range: [7.36, 12.88], mean: 10.18
  Created 13 candidate models for data size 2156
Current R2 threshold: 0.29
  rf-tuned-l: R2 = 0.233 (std: 0.052)
  rf-tuned-xl: R2 = 0.233 (std: 0.049)
  gb-tuned-l: R2 = 0.210 (std: 0.050)
  gb-tuned-xl: R2 = 0.210 (std: 0.050)
  xgb-xl: R2 = 0.162 (std: 0.083)
  xgb-l: R2 = 0.162 (std: 0.083)
  mlp-adaptive-xl: R2 = 0.216 (std: 0.064)
  mlp-l: R2 = 0.186 (std: 0.058)
  svr-rbf-xl: R2 = 0.301 (std: 0.046)
  svr-poly-l: R2 = 0.301 (std: 0.046)
  knn-tuned-sqrt: R2 = 0.097 (std: 0.061)
  knn-tuned-l: R2 = 0.097 (std: 0.061)
  ridge: R2 = 0.033 (std: 0.043)

Model-based training with 2 models
Best R2: 0.301, Mean R2: 0.188
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9708, entropy=0.2863, kl_div=0.0000
    Epoch 1: policy_loss=-0.0222, value_loss=0.9708, entropy=0.2871, kl_div=-0.0417
  Round 1/5: Mean predicted reward = 9.750
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.3243, kl_div=0.0000
    Epoch 1: policy_loss=-0.0494, value_loss=0.9698, entropy=0.3266, kl_div=-0.1017
  Round 2/5: Mean predicted reward = 9.919
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3151, kl_div=0.0000
    Epoch 1: policy_loss=-0.0050, value_loss=0.9689, entropy=0.3169, kl_div=-0.1561
  Round 3/5: Mean predicted reward = 10.080
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.3737, kl_div=0.0000
    Epoch 1: policy_loss=-0.0135, value_loss=0.9692, entropy=0.3747, kl_div=-0.0213
  Round 4/5: Mean predicted reward = 10.168
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9661, entropy=0.3421, kl_div=0.0000
    Epoch 1: policy_loss=-0.0262, value_loss=0.9661, entropy=0.3430, kl_div=0.0315
  Round 5/5: Mean predicted reward = 10.181

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 69 Results ---
  Mean Oracle Reward: 10.412
  Min Oracle Reward: 7.951
  Max Oracle Reward: 11.868
  Std Oracle Reward: 0.912
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.188, Max: 0.301, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  ACCGGAGCCTGT
  CCGGGACCTATG
  GTACGCGTACAG
  CGCGTCGCAGAT
  TATCGCGGCCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.217
  Max reward: 13.566
  With intrinsic bonuses: 10.258

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.3255, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6504

=== Surrogate Model Training ===
Total samples: 2290

Training on 2187 samples (removed 103 outliers)
Reward range: [7.36, 12.88], mean: 10.18
  Created 13 candidate models for data size 2187
Current R2 threshold: 0.3
  rf-tuned-l: R2 = 0.245 (std: 0.052)
  rf-tuned-xl: R2 = 0.241 (std: 0.052)
  gb-tuned-l: R2 = 0.213 (std: 0.057)
  gb-tuned-xl: R2 = 0.213 (std: 0.057)
  xgb-xl: R2 = 0.171 (std: 0.064)
  xgb-l: R2 = 0.171 (std: 0.064)
  mlp-adaptive-xl: R2 = 0.199 (std: 0.042)
  mlp-l: R2 = 0.223 (std: 0.045)
  svr-rbf-xl: R2 = 0.307 (std: 0.044)
  svr-poly-l: R2 = 0.307 (std: 0.044)
  knn-tuned-sqrt: R2 = 0.108 (std: 0.057)
  knn-tuned-l: R2 = 0.108 (std: 0.057)
  ridge: R2 = 0.033 (std: 0.044)

Model-based training with 2 models
Best R2: 0.307, Mean R2: 0.195
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9670, entropy=0.3274, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1490
  Round 1/5: Mean predicted reward = 9.781
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.3610, kl_div=0.0000
    Epoch 1: policy_loss=-0.0504, value_loss=0.9689, entropy=0.3652, kl_div=-0.0683
  Round 2/5: Mean predicted reward = 9.773
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9677, entropy=0.3427, kl_div=0.0000
    Epoch 1: policy_loss=0.8104, value_loss=0.9678, entropy=0.3524, kl_div=-0.8702
  Round 3/5: Mean predicted reward = 10.052
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9678, entropy=0.3571, kl_div=0.0000
    Epoch 1: policy_loss=-0.0377, value_loss=0.9678, entropy=0.3578, kl_div=0.0308
  Round 4/5: Mean predicted reward = 9.984
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9652, entropy=0.3415, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6136
  Round 5/5: Mean predicted reward = 10.115

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 70 Results ---
  Mean Oracle Reward: 10.253
  Min Oracle Reward: 7.309
  Max Oracle Reward: 13.459
  Std Oracle Reward: 1.300
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.195, Max: 0.307, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  CGCTGTCAGACG
  AGTCTCGGCACG
  TGCTCAGCAGGC
  GTCCGCGACAGT
  AGAGGCCGTCCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.331
  Max reward: 12.106
  With intrinsic bonuses: 10.331

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9674, entropy=0.3487, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6878

=== Surrogate Model Training ===
Total samples: 2322

Training on 2219 samples (removed 103 outliers)
Reward range: [7.36, 12.95], mean: 10.19
  Created 13 candidate models for data size 2219
Current R2 threshold: 0.31
  rf-tuned-l: R2 = 0.241 (std: 0.055)
  rf-tuned-xl: R2 = 0.233 (std: 0.056)
  gb-tuned-l: R2 = 0.226 (std: 0.041)
  gb-tuned-xl: R2 = 0.226 (std: 0.041)
  xgb-xl: R2 = 0.180 (std: 0.054)
  xgb-l: R2 = 0.180 (std: 0.054)
  mlp-adaptive-xl: R2 = 0.205 (std: 0.024)
  mlp-l: R2 = 0.219 (std: 0.040)
  svr-rbf-xl: R2 = 0.311 (std: 0.044)
  svr-poly-l: R2 = 0.311 (std: 0.044)
  knn-tuned-sqrt: R2 = 0.115 (std: 0.055)
  knn-tuned-l: R2 = 0.115 (std: 0.055)
  ridge: R2 = 0.033 (std: 0.043)

Model-based training with 2 models
Best R2: 0.311, Mean R2: 0.200
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.3798, kl_div=0.0000
    Epoch 1: policy_loss=0.0432, value_loss=0.9685, entropy=0.3761, kl_div=0.0130
  Round 1/5: Mean predicted reward = 9.910
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.3434, kl_div=0.0000
    Epoch 1: policy_loss=-0.0384, value_loss=0.9684, entropy=0.3414, kl_div=-0.0555
  Round 2/5: Mean predicted reward = 10.105
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.3144, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2677
  Round 3/5: Mean predicted reward = 10.236
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.3174, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3362
  Round 4/5: Mean predicted reward = 10.098
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.3171, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5913
  Round 5/5: Mean predicted reward = 10.000

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 71 Results ---
  Mean Oracle Reward: 10.361
  Min Oracle Reward: 5.829
  Max Oracle Reward: 11.933
  Std Oracle Reward: 1.180
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.200, Max: 0.311, Count: 13
  Total Sequences Evaluated: 2322

======================================================================
EXPERIMENT ROUND 72/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2322
  Performance plateaued, reducing LR to 0.000100

--- Round 72 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTCGCAGCCATG
  GCCGGAATTGCC
  GAACCCGCTGTG
  CGTTGGACCAGC
  TCGAGAAGCTCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.326
  Max reward: 12.628
  With intrinsic bonuses: 10.405

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9671, entropy=0.3412, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1791

=== Surrogate Model Training ===
Total samples: 2354

Training on 2250 samples (removed 104 outliers)
Reward range: [7.36, 12.95], mean: 10.19
  Created 13 candidate models for data size 2250
Current R2 threshold: 0.32
  rf-tuned-l: R2 = 0.236 (std: 0.051)
  rf-tuned-xl: R2 = 0.233 (std: 0.048)
  gb-tuned-l: R2 = 0.215 (std: 0.046)
  gb-tuned-xl: R2 = 0.215 (std: 0.046)
  xgb-xl: R2 = 0.198 (std: 0.052)
  xgb-l: R2 = 0.198 (std: 0.052)
  mlp-adaptive-xl: R2 = 0.221 (std: 0.032)
  mlp-l: R2 = 0.215 (std: 0.056)
  svr-rbf-xl: R2 = 0.307 (std: 0.042)
  svr-poly-l: R2 = 0.307 (std: 0.042)
  knn-tuned-sqrt: R2 = 0.106 (std: 0.052)
  knn-tuned-l: R2 = 0.106 (std: 0.052)
  ridge: R2 = 0.030 (std: 0.047)
  Fallback: Using svr-rbf-xl with R2 = 0.307

Model-based training with 1 models
Best R2: 0.307, Mean R2: 0.199
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9674, entropy=0.3184, kl_div=0.0000
    Epoch 1: policy_loss=-0.0053, value_loss=0.9675, entropy=0.3180, kl_div=0.0392
  Round 1/5: Mean predicted reward = 9.677
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9685, entropy=0.3132, kl_div=0.0000
    Epoch 1: policy_loss=-0.0320, value_loss=0.9685, entropy=0.3124, kl_div=-0.1590
  Round 2/5: Mean predicted reward = 9.725
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=0.3319, kl_div=0.0000
    Epoch 1: policy_loss=-0.0337, value_loss=0.9709, entropy=0.3309, kl_div=-0.0686
  Round 3/5: Mean predicted reward = 9.947
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.3052, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1115
  Round 4/5: Mean predicted reward = 10.177
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=0.3259, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0955
  Round 5/5: Mean predicted reward = 10.155

  === Progress Analysis ===
  Status: NORMAL

--- Round 72 Results ---
  Mean Oracle Reward: 10.393
  Min Oracle Reward: 3.498
  Max Oracle Reward: 12.551
  Std Oracle Reward: 1.512
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.199, Max: 0.307, Count: 13
  Total Sequences Evaluated: 2354

======================================================================
EXPERIMENT ROUND 73/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2354
  Performance plateaued, reducing LR to 0.000055

--- Round 73 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGAGCCATGGCT
  GGTCCAGATCGA
  ATGGGCATCCGA
  GATGCGACTGCC
  GCCATCGGATGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.277
  Max reward: 11.931
  With intrinsic bonuses: 10.296

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9660, entropy=0.2943, kl_div=0.0000
    Epoch 1: policy_loss=-0.0250, value_loss=0.9660, entropy=0.2937, kl_div=-0.0419

=== Surrogate Model Training ===
Total samples: 2386

Training on 2281 samples (removed 105 outliers)
Reward range: [7.36, 12.95], mean: 10.20
  Created 13 candidate models for data size 2281
Current R2 threshold: 0.33
  rf-tuned-l: R2 = 0.231 (std: 0.054)
  rf-tuned-xl: R2 = 0.232 (std: 0.054)
  gb-tuned-l: R2 = 0.216 (std: 0.049)
  gb-tuned-xl: R2 = 0.216 (std: 0.049)
  xgb-xl: R2 = 0.175 (std: 0.056)
  xgb-l: R2 = 0.175 (std: 0.056)
  mlp-adaptive-xl: R2 = 0.222 (std: 0.037)
  mlp-l: R2 = 0.202 (std: 0.046)
  svr-rbf-xl: R2 = 0.308 (std: 0.042)
  svr-poly-l: R2 = 0.308 (std: 0.042)
  knn-tuned-sqrt: R2 = 0.106 (std: 0.052)
  knn-tuned-l: R2 = 0.106 (std: 0.052)
  ridge: R2 = 0.027 (std: 0.049)
  Fallback: Using svr-rbf-xl with R2 = 0.308

Model-based training with 1 models
Best R2: 0.308, Mean R2: 0.194
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9702, entropy=0.3107, kl_div=0.0000
    Epoch 1: policy_loss=-0.0272, value_loss=0.9702, entropy=0.3111, kl_div=-0.1091
  Round 1/5: Mean predicted reward = 10.100
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9682, entropy=0.3439, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0609
  Round 2/5: Mean predicted reward = 10.161
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.3357, kl_div=0.0000
    Epoch 1: policy_loss=-0.0320, value_loss=0.9690, entropy=0.3368, kl_div=-0.0235
  Round 3/5: Mean predicted reward = 10.180
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.3333, kl_div=0.0000
    Epoch 1: policy_loss=-0.0161, value_loss=0.9684, entropy=0.3334, kl_div=0.0020
  Round 4/5: Mean predicted reward = 10.283
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.3383, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0955
  Round 5/5: Mean predicted reward = 10.391

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 73 Results ---
  Mean Oracle Reward: 10.297
  Min Oracle Reward: 2.514
  Max Oracle Reward: 12.078
  Std Oracle Reward: 1.623
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.194, Max: 0.308, Count: 13
  Total Sequences Evaluated: 2386

======================================================================
EXPERIMENT ROUND 74/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2386
  Performance plateaued, reducing LR to 0.000019

--- Round 74 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCGGATCGGCTA
  CCAGCTGGGCAT
  GTCCGTGAACCG
  ATAGCCGAGGCT
  ACCCAGCGTTGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.356
  Max reward: 13.035
  With intrinsic bonuses: 10.278

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.3210, kl_div=0.0000
    Epoch 1: policy_loss=-0.0210, value_loss=0.9683, entropy=0.3205, kl_div=0.0281

=== Surrogate Model Training ===
Total samples: 2418

Training on 2312 samples (removed 106 outliers)
Reward range: [7.36, 12.95], mean: 10.20
  Created 13 candidate models for data size 2312
Current R2 threshold: 0.34
  rf-tuned-l: R2 = 0.236 (std: 0.062)
  rf-tuned-xl: R2 = 0.235 (std: 0.056)
  gb-tuned-l: R2 = 0.214 (std: 0.039)
  gb-tuned-xl: R2 = 0.214 (std: 0.039)
  xgb-xl: R2 = 0.190 (std: 0.046)
  xgb-l: R2 = 0.190 (std: 0.046)
  mlp-adaptive-xl: R2 = 0.194 (std: 0.042)
  mlp-l: R2 = 0.222 (std: 0.049)
  svr-rbf-xl: R2 = 0.309 (std: 0.042)
  svr-poly-l: R2 = 0.309 (std: 0.042)
  knn-tuned-sqrt: R2 = 0.102 (std: 0.052)
  knn-tuned-l: R2 = 0.102 (std: 0.052)
  ridge: R2 = 0.024 (std: 0.047)
  Fallback: Using svr-rbf-xl with R2 = 0.309

Model-based training with 1 models
Best R2: 0.309, Mean R2: 0.196
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.3024, kl_div=0.0000
    Epoch 1: policy_loss=-0.0113, value_loss=0.9692, entropy=0.3020, kl_div=-0.0124
  Round 1/5: Mean predicted reward = 9.403
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.3348, kl_div=0.0000
    Epoch 1: policy_loss=-0.0197, value_loss=0.9679, entropy=0.3348, kl_div=-0.0512
  Round 2/5: Mean predicted reward = 10.004
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.3290, kl_div=0.0000
    Epoch 1: policy_loss=-0.0096, value_loss=0.9690, entropy=0.3291, kl_div=-0.0091
  Round 3/5: Mean predicted reward = 10.137
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.3293, kl_div=0.0000
    Epoch 1: policy_loss=-0.0073, value_loss=0.9683, entropy=0.3293, kl_div=0.0075
  Round 4/5: Mean predicted reward = 10.267
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.3060, kl_div=0.0000
    Epoch 1: policy_loss=-0.0132, value_loss=0.9684, entropy=0.3057, kl_div=0.0081
  Round 5/5: Mean predicted reward = 10.113

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 74 Results ---
  Mean Oracle Reward: 10.325
  Min Oracle Reward: 7.538
  Max Oracle Reward: 13.122
  Std Oracle Reward: 1.200
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.196, Max: 0.309, Count: 13
  Total Sequences Evaluated: 2418

======================================================================
EXPERIMENT ROUND 75/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2418
  Performance plateaued, reducing LR to 0.000150

--- Round 75 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  GACGGATGCTCC
  GCACGGTCTGAA
  CCTAGAGCGGCT
  GTCCAGTAGCCG
  CCGGGATAGTCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.478
  Max reward: 14.605
  With intrinsic bonuses: 10.496

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.3090, kl_div=0.0000
    Epoch 1: policy_loss=0.0217, value_loss=0.9688, entropy=0.3055, kl_div=-0.0795

=== Surrogate Model Training ===
Total samples: 2450

Training on 2341 samples (removed 109 outliers)
Reward range: [7.36, 12.95], mean: 10.20
  Created 13 candidate models for data size 2341
Current R2 threshold: 0.35000000000000003
  rf-tuned-l: R2 = 0.229 (std: 0.057)
  rf-tuned-xl: R2 = 0.231 (std: 0.051)
  gb-tuned-l: R2 = 0.207 (std: 0.041)
  gb-tuned-xl: R2 = 0.207 (std: 0.041)
  xgb-xl: R2 = 0.203 (std: 0.061)
  xgb-l: R2 = 0.203 (std: 0.061)
  mlp-adaptive-xl: R2 = 0.217 (std: 0.050)
  mlp-l: R2 = 0.218 (std: 0.045)
  svr-rbf-xl: R2 = 0.304 (std: 0.040)
  svr-poly-l: R2 = 0.304 (std: 0.040)
  knn-tuned-sqrt: R2 = 0.096 (std: 0.050)
  knn-tuned-l: R2 = 0.096 (std: 0.050)
  ridge: R2 = 0.021 (std: 0.050)
  Fallback: Using svr-rbf-xl with R2 = 0.304

Model-based training with 1 models
Best R2: 0.304, Mean R2: 0.195
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.2934, kl_div=0.0000
    Epoch 1: policy_loss=-0.0107, value_loss=0.9698, entropy=0.2942, kl_div=-0.0867
  Round 1/5: Mean predicted reward = 9.757
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9679, entropy=0.2946, kl_div=0.0000
    Epoch 1: policy_loss=-0.0260, value_loss=0.9679, entropy=0.2971, kl_div=-0.1258
  Round 2/5: Mean predicted reward = 9.878
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.3017, kl_div=0.0000
    Epoch 1: policy_loss=-0.0459, value_loss=0.9686, entropy=0.3028, kl_div=-0.0504
  Round 3/5: Mean predicted reward = 9.890
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9656, entropy=0.3204, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1096
  Round 4/5: Mean predicted reward = 10.103
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9674, entropy=0.3073, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3109
  Round 5/5: Mean predicted reward = 9.893

  === Progress Analysis ===
  Status: NORMAL

--- Round 75 Results ---
  Mean Oracle Reward: 10.518
  Min Oracle Reward: 6.257
  Max Oracle Reward: 14.408
  Std Oracle Reward: 1.397
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.195, Max: 0.304, Count: 13
  Total Sequences Evaluated: 2450

======================================================================
EXPERIMENT ROUND 76/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2450
  Performance plateaued, reducing LR to 0.000136

--- Round 76 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTACACGGGCAT
  CCGTGGGCATCA
  TCGACGGTGCCA
  TGGCCTCGCAAG
  AGGCTTACCGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.366
  Max reward: 12.488
  With intrinsic bonuses: 10.406

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9674, entropy=0.2981, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1676

=== Surrogate Model Training ===
Total samples: 2482

Training on 2371 samples (removed 111 outliers)
Reward range: [7.36, 12.95], mean: 10.21
  Created 13 candidate models for data size 2371
Current R2 threshold: 0.36000000000000004
  rf-tuned-l: R2 = 0.233 (std: 0.050)
  rf-tuned-xl: R2 = 0.233 (std: 0.046)
  gb-tuned-l: R2 = 0.210 (std: 0.043)
  gb-tuned-xl: R2 = 0.210 (std: 0.043)
  xgb-xl: R2 = 0.200 (std: 0.044)
  xgb-l: R2 = 0.200 (std: 0.044)
  mlp-adaptive-xl: R2 = 0.215 (std: 0.038)
  mlp-l: R2 = 0.195 (std: 0.032)
  svr-rbf-xl: R2 = 0.306 (std: 0.035)
  svr-poly-l: R2 = 0.306 (std: 0.035)
  knn-tuned-sqrt: R2 = 0.093 (std: 0.047)
  knn-tuned-l: R2 = 0.093 (std: 0.047)
  ridge: R2 = 0.020 (std: 0.047)
  Fallback: Using svr-rbf-xl with R2 = 0.306

Model-based training with 1 models
Best R2: 0.306, Mean R2: 0.193
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.2992, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2131
  Round 1/5: Mean predicted reward = 9.638
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.3142, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0570
  Round 2/5: Mean predicted reward = 9.909
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.3039, kl_div=0.0000
    Epoch 1: policy_loss=-0.0309, value_loss=0.9688, entropy=0.3065, kl_div=-0.0523
  Round 3/5: Mean predicted reward = 9.870
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9707, entropy=0.3169, kl_div=0.0000
    Epoch 1: policy_loss=-0.0329, value_loss=0.9707, entropy=0.3194, kl_div=-0.1015
  Round 4/5: Mean predicted reward = 10.046
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.3026, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1858
  Round 5/5: Mean predicted reward = 10.050

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 76 Results ---
  Mean Oracle Reward: 10.353
  Min Oracle Reward: 6.686
  Max Oracle Reward: 12.430
  Std Oracle Reward: 1.226
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.193, Max: 0.306, Count: 13
  Total Sequences Evaluated: 2482

======================================================================
EXPERIMENT ROUND 77/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2482
  Performance plateaued, reducing LR to 0.000100

--- Round 77 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGAGGTCACATC
  TCCGAGGTCGAC
  CATGTGACCGCG
  AACTTGGAGTCC
  CAACGGGGCTTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.427
  Max reward: 13.025
  With intrinsic bonuses: 10.457

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.3065, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2492

=== Surrogate Model Training ===
Total samples: 2514

Training on 2401 samples (removed 113 outliers)
Reward range: [7.39, 12.95], mean: 10.21
  Created 13 candidate models for data size 2401
Current R2 threshold: 0.37000000000000005
  rf-tuned-l: R2 = 0.230 (std: 0.043)
  rf-tuned-xl: R2 = 0.234 (std: 0.050)
  gb-tuned-l: R2 = 0.210 (std: 0.048)
  gb-tuned-xl: R2 = 0.210 (std: 0.048)
  xgb-xl: R2 = 0.191 (std: 0.048)
  xgb-l: R2 = 0.191 (std: 0.048)
  mlp-adaptive-xl: R2 = 0.222 (std: 0.022)
  mlp-l: R2 = 0.204 (std: 0.048)
  svr-rbf-xl: R2 = 0.305 (std: 0.029)
  svr-poly-l: R2 = 0.305 (std: 0.029)
  knn-tuned-sqrt: R2 = 0.110 (std: 0.045)
  knn-tuned-l: R2 = 0.110 (std: 0.045)
  ridge: R2 = 0.017 (std: 0.055)
  Fallback: Using svr-rbf-xl with R2 = 0.305

Model-based training with 1 models
Best R2: 0.305, Mean R2: 0.195
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9678, entropy=0.3264, kl_div=0.0000
    Epoch 1: policy_loss=0.0224, value_loss=0.9678, entropy=0.3271, kl_div=-0.0282
  Round 1/5: Mean predicted reward = 9.619
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9673, entropy=0.3022, kl_div=0.0000
    Epoch 1: policy_loss=-0.0310, value_loss=0.9673, entropy=0.3038, kl_div=-0.0980
  Round 2/5: Mean predicted reward = 9.976
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9670, entropy=0.2937, kl_div=0.0000
    Epoch 1: policy_loss=-0.0431, value_loss=0.9670, entropy=0.2945, kl_div=-0.0359
  Round 3/5: Mean predicted reward = 9.889
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.3075, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1354
  Round 4/5: Mean predicted reward = 10.048
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9676, entropy=0.3244, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0661
  Round 5/5: Mean predicted reward = 10.440

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 77 Results ---
  Mean Oracle Reward: 10.456
  Min Oracle Reward: 5.685
  Max Oracle Reward: 12.854
  Std Oracle Reward: 1.345
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.195, Max: 0.305, Count: 13
  Total Sequences Evaluated: 2514

======================================================================
EXPERIMENT ROUND 78/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2514
  Performance plateaued, reducing LR to 0.000055

--- Round 78 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTTGAGGCCCAG
  CTCCTGAACGGG
  ACAGTCCGATGG
  GAGTGCCACGCT
  TACGCCTGGGAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.308
  Max reward: 12.426
  With intrinsic bonuses: 10.343

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9672, entropy=0.2933, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1062

=== Surrogate Model Training ===
Total samples: 2546

Training on 2429 samples (removed 117 outliers)
Reward range: [7.40, 12.88], mean: 10.22
  Created 13 candidate models for data size 2429
Current R2 threshold: 0.38000000000000006
  rf-tuned-l: R2 = 0.228 (std: 0.041)
  rf-tuned-xl: R2 = 0.228 (std: 0.055)
  gb-tuned-l: R2 = 0.222 (std: 0.052)
  gb-tuned-xl: R2 = 0.222 (std: 0.052)
  xgb-xl: R2 = 0.175 (std: 0.040)
  xgb-l: R2 = 0.175 (std: 0.040)
  mlp-adaptive-xl: R2 = 0.226 (std: 0.040)
  mlp-l: R2 = 0.220 (std: 0.033)
  svr-rbf-xl: R2 = 0.306 (std: 0.039)
  svr-poly-l: R2 = 0.306 (std: 0.039)
  knn-tuned-sqrt: R2 = 0.114 (std: 0.046)
  knn-tuned-l: R2 = 0.114 (std: 0.046)
  ridge: R2 = 0.018 (std: 0.053)
  Fallback: Using svr-rbf-xl with R2 = 0.306

Model-based training with 1 models
Best R2: 0.306, Mean R2: 0.197
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.3156, kl_div=0.0000
    Epoch 1: policy_loss=-0.0161, value_loss=0.9693, entropy=0.3161, kl_div=0.0025
  Round 1/5: Mean predicted reward = 9.812
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.3122, kl_div=0.0000
    Epoch 1: policy_loss=-0.0459, value_loss=0.9684, entropy=0.3138, kl_div=-0.1322
  Round 2/5: Mean predicted reward = 9.799
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9669, entropy=0.3201, kl_div=0.0000
    Epoch 1: policy_loss=-0.0174, value_loss=0.9669, entropy=0.3220, kl_div=-0.0572
  Round 3/5: Mean predicted reward = 9.947
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.3091, kl_div=0.0000
    Epoch 1: policy_loss=-0.0281, value_loss=0.9694, entropy=0.3085, kl_div=0.0241
  Round 4/5: Mean predicted reward = 10.020
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9669, entropy=0.2816, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1366
  Round 5/5: Mean predicted reward = 10.253

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 78 Results ---
  Mean Oracle Reward: 10.406
  Min Oracle Reward: 6.544
  Max Oracle Reward: 12.747
  Std Oracle Reward: 1.288
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.197, Max: 0.306, Count: 13
  Total Sequences Evaluated: 2546

======================================================================
EXPERIMENT ROUND 79/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2546
  Performance plateaued, reducing LR to 0.000019

--- Round 79 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTCGACGGGTCA
  CTCATCGAGGCG
  CTTGAAGCGGCC
  CGCCGTAGGCTA
  CTGGCGATCACG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.404
  Max reward: 12.544
  With intrinsic bonuses: 10.454

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9668, entropy=0.2821, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0582

=== Surrogate Model Training ===
Total samples: 2578

Training on 2458 samples (removed 120 outliers)
Reward range: [7.43, 12.88], mean: 10.22
  Created 13 candidate models for data size 2458
Current R2 threshold: 0.39000000000000007
  rf-tuned-l: R2 = 0.233 (std: 0.047)
  rf-tuned-xl: R2 = 0.235 (std: 0.048)
  gb-tuned-l: R2 = 0.223 (std: 0.047)
  gb-tuned-xl: R2 = 0.223 (std: 0.047)
  xgb-xl: R2 = 0.189 (std: 0.057)
  xgb-l: R2 = 0.189 (std: 0.057)
  mlp-adaptive-xl: R2 = 0.208 (std: 0.042)
  mlp-l: R2 = 0.222 (std: 0.030)
  svr-rbf-xl: R2 = 0.308 (std: 0.045)
  svr-poly-l: R2 = 0.308 (std: 0.045)
  knn-tuned-sqrt: R2 = 0.119 (std: 0.056)
  knn-tuned-l: R2 = 0.119 (std: 0.056)
  ridge: R2 = 0.011 (std: 0.054)
  Fallback: Using svr-rbf-xl with R2 = 0.308

Model-based training with 1 models
Best R2: 0.308, Mean R2: 0.199
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.3364, kl_div=0.0000
    Epoch 1: policy_loss=-0.0080, value_loss=0.9693, entropy=0.3360, kl_div=0.0199
  Round 1/5: Mean predicted reward = 9.637
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.2767, kl_div=0.0000
    Epoch 1: policy_loss=-0.0158, value_loss=0.9699, entropy=0.2764, kl_div=0.0310
  Round 2/5: Mean predicted reward = 9.966
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.3025, kl_div=0.0000
    Epoch 1: policy_loss=-0.0098, value_loss=0.9683, entropy=0.3023, kl_div=0.0486
  Round 3/5: Mean predicted reward = 10.097
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.3351, kl_div=0.0000
    Epoch 1: policy_loss=-0.0097, value_loss=0.9696, entropy=0.3350, kl_div=0.0104
  Round 4/5: Mean predicted reward = 10.272
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9685, entropy=0.2882, kl_div=0.0000
    Epoch 1: policy_loss=-0.0139, value_loss=0.9685, entropy=0.2882, kl_div=0.0107
  Round 5/5: Mean predicted reward = 10.215

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 79 Results ---
  Mean Oracle Reward: 10.444
  Min Oracle Reward: 6.711
  Max Oracle Reward: 12.533
  Std Oracle Reward: 1.326
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.199, Max: 0.308, Count: 13
  Total Sequences Evaluated: 2578

======================================================================
EXPERIMENT ROUND 80/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2578
  Performance plateaued, reducing LR to 0.000150

--- Round 80 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGCGCTGAACGT
  CAGCCGTGAGTC
  ACCATGGTGGCC
  CTCTGCGGGCAA
  GCTCCGTAAGGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.137
  Max reward: 13.831
  With intrinsic bonuses: 10.096

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.2999, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0607

=== Surrogate Model Training ===
Total samples: 2610

Training on 2485 samples (removed 125 outliers)
Reward range: [7.43, 12.88], mean: 10.22
  Created 13 candidate models for data size 2485
Current R2 threshold: 0.4000000000000001
  rf-tuned-l: R2 = 0.237 (std: 0.050)
  rf-tuned-xl: R2 = 0.240 (std: 0.046)
  gb-tuned-l: R2 = 0.221 (std: 0.053)
  gb-tuned-xl: R2 = 0.221 (std: 0.053)
  xgb-xl: R2 = 0.200 (std: 0.052)
  xgb-l: R2 = 0.200 (std: 0.052)
  mlp-adaptive-xl: R2 = 0.214 (std: 0.054)
  mlp-l: R2 = 0.200 (std: 0.059)
  svr-rbf-xl: R2 = 0.312 (std: 0.047)
  svr-poly-l: R2 = 0.312 (std: 0.047)
  knn-tuned-sqrt: R2 = 0.121 (std: 0.059)
  knn-tuned-l: R2 = 0.121 (std: 0.059)
  ridge: R2 = 0.008 (std: 0.052)
  Fallback: Using svr-rbf-xl with R2 = 0.312

Model-based training with 1 models
Best R2: 0.312, Mean R2: 0.201
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.3170, kl_div=0.0000
    Epoch 1: policy_loss=-0.0721, value_loss=0.9703, entropy=0.3190, kl_div=-0.0719
  Round 1/5: Mean predicted reward = 9.632
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9676, entropy=0.3092, kl_div=0.0000
    Epoch 1: policy_loss=0.0174, value_loss=0.9676, entropy=0.3136, kl_div=-0.3154
  Round 2/5: Mean predicted reward = 9.876
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3310, kl_div=0.0000
    Epoch 1: policy_loss=0.0703, value_loss=0.9689, entropy=0.3373, kl_div=-0.0390
  Round 3/5: Mean predicted reward = 10.074
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.3481, kl_div=0.0000
    Epoch 1: policy_loss=-0.0401, value_loss=0.9679, entropy=0.3506, kl_div=-0.0859
  Round 4/5: Mean predicted reward = 10.446
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9717, entropy=0.3492, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2697
  Round 5/5: Mean predicted reward = 10.391

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 80 Results ---
  Mean Oracle Reward: 10.131
  Min Oracle Reward: 4.683
  Max Oracle Reward: 13.603
  Std Oracle Reward: 1.837
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.201, Max: 0.312, Count: 13
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
  CGGTAGCCATGC
  GTGCACAGGCTC
  ATCGTCAGGCGC
  GTGACAGCTGCC
  AATCACGGTGGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.766
  Max reward: 12.643
  With intrinsic bonuses: 10.801

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9676, entropy=0.3433, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.2813

=== Surrogate Model Training ===
Total samples: 2642

Training on 2518 samples (removed 124 outliers)
Reward range: [7.43, 12.95], mean: 10.23
  Created 13 candidate models for data size 2518
Current R2 threshold: 0.41
  rf-tuned-l: R2 = 0.242 (std: 0.046)
  rf-tuned-xl: R2 = 0.240 (std: 0.050)
  gb-tuned-l: R2 = 0.218 (std: 0.046)
  gb-tuned-xl: R2 = 0.218 (std: 0.046)
  xgb-xl: R2 = 0.211 (std: 0.095)
  xgb-l: R2 = 0.211 (std: 0.095)
  mlp-adaptive-xl: R2 = 0.228 (std: 0.043)
  mlp-l: R2 = 0.223 (std: 0.060)
  svr-rbf-xl: R2 = 0.314 (std: 0.049)
  svr-poly-l: R2 = 0.314 (std: 0.049)
  knn-tuned-sqrt: R2 = 0.126 (std: 0.059)
  knn-tuned-l: R2 = 0.126 (std: 0.059)
  ridge: R2 = 0.002 (std: 0.057)
  Fallback: Using svr-rbf-xl with R2 = 0.314

Model-based training with 1 models
Best R2: 0.314, Mean R2: 0.205
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.3134, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4751
  Round 1/5: Mean predicted reward = 9.831
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9667, entropy=0.2756, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1964
  Round 2/5: Mean predicted reward = 9.877
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.2678, kl_div=0.0000
    Epoch 1: policy_loss=-0.0729, value_loss=0.9701, entropy=0.2669, kl_div=-0.0296
  Round 3/5: Mean predicted reward = 9.996
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.2892, kl_div=0.0000
    Epoch 1: policy_loss=-0.0032, value_loss=0.9680, entropy=0.2885, kl_div=-0.0617
  Round 4/5: Mean predicted reward = 9.937
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9718, entropy=0.3077, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5582
  Round 5/5: Mean predicted reward = 10.435

  === Progress Analysis ===
  Status: NORMAL

--- Round 81 Results ---
  Mean Oracle Reward: 10.814
  Min Oracle Reward: 8.829
  Max Oracle Reward: 12.403
  Std Oracle Reward: 0.917
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.205, Max: 0.314, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 2642

======================================================================
EXPERIMENT ROUND 82/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2642

--- Round 82 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AATCGGTCCAGG
  ATCGGCGGCCTA
  CGGAGTTCCGAA
  GCACGTGGACTC
  TTGCACAGGCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.727
  Max reward: 13.612
  With intrinsic bonuses: 10.694

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9651, entropy=0.2957, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3735

=== Surrogate Model Training ===
Total samples: 2674

Training on 2548 samples (removed 126 outliers)
Reward range: [7.43, 12.95], mean: 10.24
  Created 13 candidate models for data size 2548
Current R2 threshold: 0.42
  rf-tuned-l: R2 = 0.232 (std: 0.051)
  rf-tuned-xl: R2 = 0.236 (std: 0.048)
  gb-tuned-l: R2 = 0.220 (std: 0.049)
  gb-tuned-xl: R2 = 0.220 (std: 0.049)
  xgb-xl: R2 = 0.196 (std: 0.083)
  xgb-l: R2 = 0.196 (std: 0.083)
  mlp-adaptive-xl: R2 = 0.226 (std: 0.046)
  mlp-l: R2 = 0.211 (std: 0.066)
  svr-rbf-xl: R2 = 0.307 (std: 0.048)
  svr-poly-l: R2 = 0.307 (std: 0.048)
  knn-tuned-sqrt: R2 = 0.122 (std: 0.055)
  knn-tuned-l: R2 = 0.122 (std: 0.055)
  ridge: R2 = -0.007 (std: 0.064)
  Fallback: Using svr-rbf-xl with R2 = 0.307

Model-based training with 1 models
Best R2: 0.307, Mean R2: 0.199
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=0.2439, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3069
  Round 1/5: Mean predicted reward = 10.129
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9666, entropy=0.2607, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0881
  Round 2/5: Mean predicted reward = 10.001
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9672, entropy=0.2616, kl_div=0.0000
    Epoch 1: policy_loss=0.1324, value_loss=0.9672, entropy=0.2643, kl_div=-0.2044
  Round 3/5: Mean predicted reward = 9.914
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9685, entropy=0.2795, kl_div=0.0000
    Epoch 1: policy_loss=-0.0127, value_loss=0.9685, entropy=0.2801, kl_div=-0.1360
  Round 4/5: Mean predicted reward = 10.065
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9677, entropy=0.2511, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3771
  Round 5/5: Mean predicted reward = 10.245

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 82 Results ---
  Mean Oracle Reward: 10.794
  Min Oracle Reward: 3.923
  Max Oracle Reward: 13.884
  Std Oracle Reward: 1.543
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.199, Max: 0.307, Count: 13
  Total Sequences Evaluated: 2674

======================================================================
EXPERIMENT ROUND 83/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2674

--- Round 83 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  GACTGAGACCGT
  GACCGACTGCGT
  GGCGCTCGTACA
  CGAGGCTGAACT
  TCCCGATGCGGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.195
  Max reward: 12.053
  With intrinsic bonuses: 10.198

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.2787, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1852

=== Surrogate Model Training ===
Total samples: 2706

Training on 2579 samples (removed 127 outliers)
Reward range: [7.43, 12.98], mean: 10.25
  Created 13 candidate models for data size 2579
Current R2 threshold: 0.43
  rf-tuned-l: R2 = 0.239 (std: 0.047)
  rf-tuned-xl: R2 = 0.243 (std: 0.050)
  gb-tuned-l: R2 = 0.218 (std: 0.045)
  gb-tuned-xl: R2 = 0.218 (std: 0.045)
  xgb-xl: R2 = 0.194 (std: 0.074)
  xgb-l: R2 = 0.194 (std: 0.074)
  mlp-adaptive-xl: R2 = 0.221 (std: 0.044)
  mlp-l: R2 = 0.237 (std: 0.077)
  svr-rbf-xl: R2 = 0.311 (std: 0.045)
  svr-poly-l: R2 = 0.311 (std: 0.045)
  knn-tuned-sqrt: R2 = 0.121 (std: 0.063)
  knn-tuned-l: R2 = 0.121 (std: 0.063)
  ridge: R2 = -0.008 (std: 0.064)
  Fallback: Using svr-rbf-xl with R2 = 0.311

Model-based training with 1 models
Best R2: 0.311, Mean R2: 0.202
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9673, entropy=0.2500, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0655
  Round 1/5: Mean predicted reward = 9.699
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9677, entropy=0.2626, kl_div=0.0000
    Epoch 1: policy_loss=-0.0714, value_loss=0.9677, entropy=0.2640, kl_div=-0.0503
  Round 2/5: Mean predicted reward = 9.917
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9673, entropy=0.2507, kl_div=0.0000
    Epoch 1: policy_loss=-0.0390, value_loss=0.9673, entropy=0.2531, kl_div=-0.1334
  Round 3/5: Mean predicted reward = 9.828
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9673, entropy=0.2735, kl_div=0.0000
    Epoch 1: policy_loss=-0.0138, value_loss=0.9673, entropy=0.2781, kl_div=-0.1918
  Round 4/5: Mean predicted reward = 10.027
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9671, entropy=0.2600, kl_div=0.0000
    Epoch 1: policy_loss=-0.0359, value_loss=0.9672, entropy=0.2627, kl_div=-0.0818
  Round 5/5: Mean predicted reward = 9.992

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 83 Results ---
  Mean Oracle Reward: 10.187
  Min Oracle Reward: 2.473
  Max Oracle Reward: 12.194
  Std Oracle Reward: 1.936
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.202, Max: 0.311, Count: 13
  Total Sequences Evaluated: 2706

======================================================================
EXPERIMENT ROUND 84/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2706

--- Round 84 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTCGAAGCGCTC
  GCAAATCTGGCG
  GTCGCAGCCATG
  GCCTCGAGACTG
  TAGGCCGTCACG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.649
  Max reward: 12.611
  With intrinsic bonuses: 10.720

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9663, entropy=0.2735, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0595

=== Surrogate Model Training ===
Total samples: 2738

Training on 2609 samples (removed 129 outliers)
Reward range: [7.43, 12.98], mean: 10.25
  Created 13 candidate models for data size 2609
Current R2 threshold: 0.44
  rf-tuned-l: R2 = 0.241 (std: 0.049)
  rf-tuned-xl: R2 = 0.235 (std: 0.048)
  gb-tuned-l: R2 = 0.215 (std: 0.049)
  gb-tuned-xl: R2 = 0.215 (std: 0.049)
  xgb-xl: R2 = 0.202 (std: 0.084)
  xgb-l: R2 = 0.202 (std: 0.084)
  mlp-adaptive-xl: R2 = 0.239 (std: 0.066)
  mlp-l: R2 = 0.218 (std: 0.052)
  svr-rbf-xl: R2 = 0.309 (std: 0.041)
  svr-poly-l: R2 = 0.309 (std: 0.041)
  knn-tuned-sqrt: R2 = 0.119 (std: 0.061)
  knn-tuned-l: R2 = 0.119 (std: 0.061)
  ridge: R2 = -0.015 (std: 0.072)
  Fallback: Using svr-rbf-xl with R2 = 0.309

Model-based training with 1 models
Best R2: 0.309, Mean R2: 0.201
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9674, entropy=0.2706, kl_div=0.0000
    Epoch 1: policy_loss=-0.0111, value_loss=0.9674, entropy=0.2708, kl_div=-0.0110
  Round 1/5: Mean predicted reward = 9.840
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.2917, kl_div=0.0000
    Epoch 1: policy_loss=-0.0183, value_loss=0.9686, entropy=0.2936, kl_div=-0.0651
  Round 2/5: Mean predicted reward = 9.935
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.2705, kl_div=0.0000
    Epoch 1: policy_loss=-0.0207, value_loss=0.9683, entropy=0.2706, kl_div=-0.0377
  Round 3/5: Mean predicted reward = 9.894
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.3257, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0583
  Round 4/5: Mean predicted reward = 10.204
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.2838, kl_div=0.0000
    Epoch 1: policy_loss=0.0111, value_loss=0.9701, entropy=0.2831, kl_div=0.0156
  Round 5/5: Mean predicted reward = 10.167

  === Progress Analysis ===
  Status: NORMAL

--- Round 84 Results ---
  Mean Oracle Reward: 10.685
  Min Oracle Reward: 7.410
  Max Oracle Reward: 12.453
  Std Oracle Reward: 1.230
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.201, Max: 0.309, Count: 13
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
  GGAAGCCGTCTC
  TCCGGGCCATGA
  AGTCCACGCGTG
  GCTCAAGCGTCG
  CTGTCAGCGACG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.554
  Max reward: 13.498
  With intrinsic bonuses: 10.565

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9664, entropy=0.2765, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1615

=== Surrogate Model Training ===
Total samples: 2770

Training on 2639 samples (removed 131 outliers)
Reward range: [7.43, 12.98], mean: 10.26
  Created 13 candidate models for data size 2639
Current R2 threshold: 0.45
  rf-tuned-l: R2 = 0.249 (std: 0.046)
  rf-tuned-xl: R2 = 0.252 (std: 0.050)
  gb-tuned-l: R2 = 0.224 (std: 0.039)
  gb-tuned-xl: R2 = 0.224 (std: 0.039)
  xgb-xl: R2 = 0.214 (std: 0.086)
  xgb-l: R2 = 0.214 (std: 0.086)
  mlp-adaptive-xl: R2 = 0.230 (std: 0.068)
  mlp-l: R2 = 0.219 (std: 0.052)
  svr-rbf-xl: R2 = 0.313 (std: 0.048)
  svr-poly-l: R2 = 0.313 (std: 0.048)
  knn-tuned-sqrt: R2 = 0.129 (std: 0.058)
  knn-tuned-l: R2 = 0.129 (std: 0.058)
  ridge: R2 = -0.008 (std: 0.067)
  Fallback: Using svr-rbf-xl with R2 = 0.313

Model-based training with 1 models
Best R2: 0.313, Mean R2: 0.208
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.2902, kl_div=0.0000
    Epoch 1: policy_loss=-0.0583, value_loss=0.9684, entropy=0.2910, kl_div=-0.2617
  Round 1/5: Mean predicted reward = 9.878
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.2587, kl_div=0.0000
    Epoch 1: policy_loss=-0.0007, value_loss=0.9682, entropy=0.2650, kl_div=-0.0769
  Round 2/5: Mean predicted reward = 9.846
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9677, entropy=0.2622, kl_div=0.0000
    Epoch 1: policy_loss=-0.0103, value_loss=0.9677, entropy=0.2662, kl_div=-0.2301
  Round 3/5: Mean predicted reward = 9.831
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9681, entropy=0.2641, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2521
  Round 4/5: Mean predicted reward = 9.859
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.2554, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3860
  Round 5/5: Mean predicted reward = 10.242

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 85 Results ---
  Mean Oracle Reward: 10.526
  Min Oracle Reward: 7.664
  Max Oracle Reward: 13.557
  Std Oracle Reward: 1.185
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.208, Max: 0.313, Count: 13
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

--- Generated Sequences (Diversity: 0.969) ---
  CAACTGGCTGGC
  TACGTCGCAGCG
  AGGCCGATCTGC
  CGGATCCTCGGA
  TCGGTGGCACCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.740
  Max reward: 13.683
  With intrinsic bonuses: 10.758

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.2388, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4862

=== Surrogate Model Training ===
Total samples: 2802

Training on 2671 samples (removed 131 outliers)
Reward range: [7.42, 12.98], mean: 10.26
  Created 13 candidate models for data size 2671
Current R2 threshold: 0.46
  rf-tuned-l: R2 = 0.256 (std: 0.044)
  rf-tuned-xl: R2 = 0.250 (std: 0.054)
  gb-tuned-l: R2 = 0.229 (std: 0.047)
  gb-tuned-xl: R2 = 0.229 (std: 0.047)
  xgb-xl: R2 = 0.213 (std: 0.099)
  xgb-l: R2 = 0.213 (std: 0.099)
  mlp-adaptive-xl: R2 = 0.218 (std: 0.067)
  mlp-l: R2 = 0.246 (std: 0.076)
  svr-rbf-xl: R2 = 0.317 (std: 0.052)
  svr-poly-l: R2 = 0.317 (std: 0.052)
  knn-tuned-sqrt: R2 = 0.127 (std: 0.064)
  knn-tuned-l: R2 = 0.127 (std: 0.064)
  ridge: R2 = -0.008 (std: 0.068)
  Fallback: Using svr-rbf-xl with R2 = 0.317

Model-based training with 1 models
Best R2: 0.317, Mean R2: 0.210
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9681, entropy=0.2529, kl_div=0.0000
    Epoch 1: policy_loss=-0.0654, value_loss=0.9681, entropy=0.2554, kl_div=0.0328
  Round 1/5: Mean predicted reward = 9.604
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=0.2553, kl_div=0.0000
    Epoch 1: policy_loss=0.3579, value_loss=0.9675, entropy=0.2578, kl_div=-0.3671
  Round 2/5: Mean predicted reward = 9.962
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.2513, kl_div=0.0000
    Epoch 1: policy_loss=0.1586, value_loss=0.9679, entropy=0.2582, kl_div=-0.3513
  Round 3/5: Mean predicted reward = 10.146
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9672, entropy=0.2695, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2942
  Round 4/5: Mean predicted reward = 10.091
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9674, entropy=0.2779, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4992
  Round 5/5: Mean predicted reward = 10.226

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 86 Results ---
  Mean Oracle Reward: 10.722
  Min Oracle Reward: 7.566
  Max Oracle Reward: 13.857
  Std Oracle Reward: 1.442
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.210, Max: 0.317, Count: 13
  Total Sequences Evaluated: 2802

======================================================================
EXPERIMENT ROUND 87/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2802
  Performance plateaued, reducing LR to 0.000100

--- Round 87 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  GCTACGATCGGC
  AACGGTGATCGC
  GTGTCCAAACGG
  ACGAGTGTAGCC
  AGTCGGGACTCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.469
  Max reward: 12.265
  With intrinsic bonuses: 10.467

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.2595, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1612

=== Surrogate Model Training ===
Total samples: 2834

Training on 2701 samples (removed 133 outliers)
Reward range: [7.43, 12.98], mean: 10.27
  Created 13 candidate models for data size 2701
Current R2 threshold: 0.47000000000000003
  rf-tuned-l: R2 = 0.246 (std: 0.039)
  rf-tuned-xl: R2 = 0.248 (std: 0.037)
  gb-tuned-l: R2 = 0.226 (std: 0.040)
  gb-tuned-xl: R2 = 0.226 (std: 0.040)
  xgb-xl: R2 = 0.230 (std: 0.096)
  xgb-l: R2 = 0.230 (std: 0.096)
  mlp-adaptive-xl: R2 = 0.186 (std: 0.079)
  mlp-l: R2 = 0.235 (std: 0.021)
  svr-rbf-xl: R2 = 0.318 (std: 0.046)
  svr-poly-l: R2 = 0.318 (std: 0.046)
  knn-tuned-sqrt: R2 = 0.120 (std: 0.060)
  knn-tuned-l: R2 = 0.120 (std: 0.060)
  ridge: R2 = -0.014 (std: 0.077)
  Fallback: Using svr-rbf-xl with R2 = 0.318

Model-based training with 1 models
Best R2: 0.318, Mean R2: 0.207
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.2657, kl_div=0.0000
    Epoch 1: policy_loss=-0.0094, value_loss=0.9692, entropy=0.2654, kl_div=0.0320
  Round 1/5: Mean predicted reward = 9.549
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.2470, kl_div=0.0000
    Epoch 1: policy_loss=-0.0520, value_loss=0.9697, entropy=0.2499, kl_div=-0.2322
  Round 2/5: Mean predicted reward = 9.673
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.2672, kl_div=0.0000
    Epoch 1: policy_loss=-0.0311, value_loss=0.9698, entropy=0.2693, kl_div=-0.1925
  Round 3/5: Mean predicted reward = 10.056
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2543, kl_div=0.0000
    Epoch 1: policy_loss=-0.0360, value_loss=0.9687, entropy=0.2534, kl_div=0.0116
  Round 4/5: Mean predicted reward = 10.097
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.2542, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2495
  Round 5/5: Mean predicted reward = 10.422

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 87 Results ---
  Mean Oracle Reward: 10.432
  Min Oracle Reward: 7.554
  Max Oracle Reward: 12.431
  Std Oracle Reward: 1.026
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.207, Max: 0.318, Count: 13
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

--- Generated Sequences (Diversity: 0.938) ---
  TGACTCGCCAGG
  AGCCCAGGTCGT
  TCGGCCGAACTG
  CCAGCGTGATCG
  GTGCCATCGGAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.297
  Max reward: 11.868
  With intrinsic bonuses: 10.297

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.2573, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2751

=== Surrogate Model Training ===
Total samples: 2866

Training on 2731 samples (removed 135 outliers)
Reward range: [7.44, 12.98], mean: 10.27
  Created 13 candidate models for data size 2731
Current R2 threshold: 0.48000000000000004
  rf-tuned-l: R2 = 0.241 (std: 0.033)
  rf-tuned-xl: R2 = 0.242 (std: 0.029)
  gb-tuned-l: R2 = 0.216 (std: 0.036)
  gb-tuned-xl: R2 = 0.216 (std: 0.036)
  xgb-xl: R2 = 0.207 (std: 0.115)
  xgb-l: R2 = 0.207 (std: 0.115)
  mlp-adaptive-xl: R2 = 0.220 (std: 0.061)
  mlp-l: R2 = 0.241 (std: 0.045)
  svr-rbf-xl: R2 = 0.315 (std: 0.036)
  svr-poly-l: R2 = 0.315 (std: 0.036)
  knn-tuned-sqrt: R2 = 0.115 (std: 0.049)
  knn-tuned-l: R2 = 0.115 (std: 0.049)
  ridge: R2 = -0.020 (std: 0.084)
  Fallback: Using svr-rbf-xl with R2 = 0.315

Model-based training with 1 models
Best R2: 0.315, Mean R2: 0.202
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2427, kl_div=0.0000
    Epoch 1: policy_loss=0.0321, value_loss=0.9689, entropy=0.2415, kl_div=-0.0001
  Round 1/5: Mean predicted reward = 9.680
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.2496, kl_div=0.0000
    Epoch 1: policy_loss=-0.0806, value_loss=0.9686, entropy=0.2493, kl_div=-0.1904
  Round 2/5: Mean predicted reward = 9.782
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.2538, kl_div=0.0000
    Epoch 1: policy_loss=-0.0547, value_loss=0.9698, entropy=0.2549, kl_div=-0.1495
  Round 3/5: Mean predicted reward = 9.893
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9679, entropy=0.2632, kl_div=0.0000
    Epoch 1: policy_loss=-0.0594, value_loss=0.9679, entropy=0.2641, kl_div=-0.0656
  Round 4/5: Mean predicted reward = 10.066
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.2827, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0819
  Round 5/5: Mean predicted reward = 10.419

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 88 Results ---
  Mean Oracle Reward: 10.314
  Min Oracle Reward: 5.067
  Max Oracle Reward: 12.024
  Std Oracle Reward: 1.300
  Sequence Diversity: 0.938
  Models Used: 1
  Model R2 - Mean: 0.202, Max: 0.315, Count: 13
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

--- Generated Sequences (Diversity: 0.969) ---
  AGATCGGCCTGC
  CACGGCTTCGGA
  CAGTGCGCCAGT
  TGCCTGAGCGAC
  CGTCCGAAGGTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.650
  Max reward: 12.664
  With intrinsic bonuses: 10.611

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.2873, kl_div=0.0000
    Epoch 1: policy_loss=-0.0278, value_loss=0.9680, entropy=0.2876, kl_div=0.0367

=== Surrogate Model Training ===
Total samples: 2898

Training on 2765 samples (removed 133 outliers)
Reward range: [7.43, 12.98], mean: 10.27
  Created 13 candidate models for data size 2765
Current R2 threshold: 0.49000000000000005
  rf-tuned-l: R2 = 0.256 (std: 0.044)
  rf-tuned-xl: R2 = 0.251 (std: 0.038)
  gb-tuned-l: R2 = 0.226 (std: 0.043)
  gb-tuned-xl: R2 = 0.226 (std: 0.043)
  xgb-xl: R2 = 0.224 (std: 0.090)
  xgb-l: R2 = 0.224 (std: 0.090)
  mlp-adaptive-xl: R2 = 0.228 (std: 0.040)
  mlp-l: R2 = 0.239 (std: 0.045)
  svr-rbf-xl: R2 = 0.322 (std: 0.035)
  svr-poly-l: R2 = 0.322 (std: 0.035)
  knn-tuned-sqrt: R2 = 0.121 (std: 0.044)
  knn-tuned-l: R2 = 0.121 (std: 0.044)
  ridge: R2 = -0.018 (std: 0.085)
  Fallback: Using svr-rbf-xl with R2 = 0.322

Model-based training with 1 models
Best R2: 0.322, Mean R2: 0.211
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.2556, kl_div=0.0000
    Epoch 1: policy_loss=0.0000, value_loss=0.9681, entropy=0.2552, kl_div=0.0067
  Round 1/5: Mean predicted reward = 9.471
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.2686, kl_div=0.0000
    Epoch 1: policy_loss=-0.0419, value_loss=0.9688, entropy=0.2690, kl_div=-0.0537
  Round 2/5: Mean predicted reward = 9.632
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.2583, kl_div=0.0000
    Epoch 1: policy_loss=-0.0304, value_loss=0.9680, entropy=0.2595, kl_div=-0.1050
  Round 3/5: Mean predicted reward = 9.719
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9673, entropy=0.2708, kl_div=0.0000
    Epoch 1: policy_loss=-0.0141, value_loss=0.9673, entropy=0.2720, kl_div=-0.1052
  Round 4/5: Mean predicted reward = 9.959
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9702, entropy=0.2751, kl_div=0.0000
    Epoch 1: policy_loss=0.0001, value_loss=0.9702, entropy=0.2757, kl_div=-0.0102
  Round 5/5: Mean predicted reward = 10.301

  === Progress Analysis ===
  Status: NORMAL

--- Round 89 Results ---
  Mean Oracle Reward: 10.637
  Min Oracle Reward: 7.370
  Max Oracle Reward: 12.622
  Std Oracle Reward: 1.211
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.211, Max: 0.322, Count: 13
  Total Sequences Evaluated: 2898

======================================================================
EXPERIMENT ROUND 90/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2898

--- Round 90 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  GCCGATCAGCTG
  CTCATCGCAGGG
  CGGTCCATGAGC
  CAACCGTGTCGG
  TCAGCGGACCGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.185
  Max reward: 12.047
  With intrinsic bonuses: 10.116

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.2743, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1438

=== Surrogate Model Training ===
Total samples: 2930

Training on 2797 samples (removed 133 outliers)
Reward range: [7.42, 12.98], mean: 10.27
  Created 13 candidate models for data size 2797
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.262 (std: 0.041)
  rf-tuned-xl: R2 = 0.262 (std: 0.045)
  gb-tuned-l: R2 = 0.220 (std: 0.049)
  gb-tuned-xl: R2 = 0.220 (std: 0.049)
  xgb-xl: R2 = 0.261 (std: 0.053)
  xgb-l: R2 = 0.261 (std: 0.053)
  mlp-adaptive-xl: R2 = 0.241 (std: 0.067)
  mlp-l: R2 = 0.266 (std: 0.047)
  svr-rbf-xl: R2 = 0.327 (std: 0.039)
  svr-poly-l: R2 = 0.327 (std: 0.039)
  knn-tuned-sqrt: R2 = 0.123 (std: 0.051)
  knn-tuned-l: R2 = 0.123 (std: 0.051)
  ridge: R2 = -0.009 (std: 0.079)
  Fallback: Using svr-rbf-xl with R2 = 0.327

Model-based training with 1 models
Best R2: 0.327, Mean R2: 0.222
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9678, entropy=0.2816, kl_div=0.0000
    Epoch 1: policy_loss=-0.0292, value_loss=0.9679, entropy=0.2883, kl_div=-0.3873
  Round 1/5: Mean predicted reward = 9.567
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9673, entropy=0.2633, kl_div=0.0000
    Epoch 1: policy_loss=-0.0265, value_loss=0.9673, entropy=0.2733, kl_div=-0.3693
  Round 2/5: Mean predicted reward = 9.615
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9685, entropy=0.3227, kl_div=0.0000
    Epoch 1: policy_loss=-0.0072, value_loss=0.9685, entropy=0.3337, kl_div=-0.1743
  Round 3/5: Mean predicted reward = 9.772
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.2782, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3299
  Round 4/5: Mean predicted reward = 10.132
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.3269, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7010
  Round 5/5: Mean predicted reward = 10.376

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 90 Results ---
  Mean Oracle Reward: 10.200
  Min Oracle Reward: 2.819
  Max Oracle Reward: 12.253
  Std Oracle Reward: 1.649
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.222, Max: 0.327, Count: 13
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
  AGCGTCAGTGCA
  ATACCTGGCGCG
  CAGGTCCTGACG
  CAACGTTGCAGG
  GGCCGCTTCAGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.343
  Max reward: 12.461
  With intrinsic bonuses: 10.378

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9709, entropy=0.2707, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4957

=== Surrogate Model Training ===
Total samples: 2962

Training on 2827 samples (removed 135 outliers)
Reward range: [7.42, 12.98], mean: 10.28
  Created 13 candidate models for data size 2827
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.261 (std: 0.043)
  rf-tuned-xl: R2 = 0.251 (std: 0.040)
  gb-tuned-l: R2 = 0.229 (std: 0.054)
  gb-tuned-xl: R2 = 0.229 (std: 0.054)
  xgb-xl: R2 = 0.260 (std: 0.056)
  xgb-l: R2 = 0.260 (std: 0.056)
  mlp-adaptive-xl: R2 = 0.249 (std: 0.065)
  mlp-l: R2 = 0.244 (std: 0.046)
  svr-rbf-xl: R2 = 0.327 (std: 0.045)
  svr-poly-l: R2 = 0.327 (std: 0.045)
  knn-tuned-sqrt: R2 = 0.130 (std: 0.057)
  knn-tuned-l: R2 = 0.130 (std: 0.057)
  ridge: R2 = -0.011 (std: 0.083)
  Fallback: Using svr-rbf-xl with R2 = 0.327

Model-based training with 1 models
Best R2: 0.327, Mean R2: 0.222
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.2490, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3249
  Round 1/5: Mean predicted reward = 9.855
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.2478, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1305
  Round 2/5: Mean predicted reward = 10.020
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9673, entropy=0.2562, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3485
  Round 3/5: Mean predicted reward = 10.038
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.2408, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2063
  Round 4/5: Mean predicted reward = 10.131
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=0.2435, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3443
  Round 5/5: Mean predicted reward = 10.392

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 91 Results ---
  Mean Oracle Reward: 10.371
  Min Oracle Reward: 4.655
  Max Oracle Reward: 12.273
  Std Oracle Reward: 1.503
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.222, Max: 0.327, Count: 13
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

--- Generated Sequences (Diversity: 0.906) ---
  AAAGCGTCGCTG
  AATGGGCTCGAC
  ACGGTCTACAGG
  GCACGCTTGCAG
  CACGTCAGTCGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.167
  Max reward: 12.309
  With intrinsic bonuses: 10.088

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.2418, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1031

=== Surrogate Model Training ===
Total samples: 2994

Training on 2858 samples (removed 136 outliers)
Reward range: [7.42, 13.05], mean: 10.28
  Created 13 candidate models for data size 2858
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.260 (std: 0.040)
  rf-tuned-xl: R2 = 0.268 (std: 0.040)
  gb-tuned-l: R2 = 0.235 (std: 0.051)
  gb-tuned-xl: R2 = 0.235 (std: 0.051)
  xgb-xl: R2 = 0.276 (std: 0.054)
  xgb-l: R2 = 0.276 (std: 0.054)
  mlp-adaptive-xl: R2 = 0.251 (std: 0.044)
  mlp-l: R2 = 0.245 (std: 0.061)
  svr-rbf-xl: R2 = 0.327 (std: 0.044)
  svr-poly-l: R2 = 0.327 (std: 0.044)
  knn-tuned-sqrt: R2 = 0.131 (std: 0.049)
  knn-tuned-l: R2 = 0.131 (std: 0.049)
  ridge: R2 = -0.014 (std: 0.084)
  Fallback: Using svr-rbf-xl with R2 = 0.327

Model-based training with 1 models
Best R2: 0.327, Mean R2: 0.227
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=0.2138, kl_div=0.0000
    Epoch 1: policy_loss=-0.0030, value_loss=0.9675, entropy=0.2169, kl_div=-0.0880
  Round 1/5: Mean predicted reward = 9.580
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9678, entropy=0.2557, kl_div=0.0000
    Epoch 1: policy_loss=-0.0384, value_loss=0.9678, entropy=0.2607, kl_div=-0.1614
  Round 2/5: Mean predicted reward = 9.944
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2410, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0823
  Round 3/5: Mean predicted reward = 9.909
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.2454, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1172
  Round 4/5: Mean predicted reward = 10.210
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.2408, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1472
  Round 5/5: Mean predicted reward = 10.278

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 92 Results ---
  Mean Oracle Reward: 10.117
  Min Oracle Reward: 4.543
  Max Oracle Reward: 12.407
  Std Oracle Reward: 1.642
  Sequence Diversity: 0.906
  Models Used: 1
  Model R2 - Mean: 0.227, Max: 0.327, Count: 13
  Total Sequences Evaluated: 2994

======================================================================
EXPERIMENT ROUND 93/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2994
  Performance plateaued, reducing LR to 0.000055

--- Round 93 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  GGCCGGATACCT
  TCCCACAGGGGT
  CTACGGGACTCG
  GGAAGCATCCTG
  ACGCGGTATAGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.482
  Max reward: 13.011
  With intrinsic bonuses: 10.447

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.2626, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0659

=== Surrogate Model Training ===
Total samples: 3026

Training on 2889 samples (removed 137 outliers)
Reward range: [7.40, 13.07], mean: 10.28
  Created 13 candidate models for data size 2889
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.250 (std: 0.043)
  rf-tuned-xl: R2 = 0.256 (std: 0.036)
  gb-tuned-l: R2 = 0.234 (std: 0.051)
  gb-tuned-xl: R2 = 0.234 (std: 0.051)
  xgb-xl: R2 = 0.271 (std: 0.055)
  xgb-l: R2 = 0.271 (std: 0.055)
  mlp-adaptive-xl: R2 = 0.262 (std: 0.064)
  mlp-l: R2 = 0.229 (std: 0.055)
  svr-rbf-xl: R2 = 0.330 (std: 0.041)
  svr-poly-l: R2 = 0.330 (std: 0.041)
  knn-tuned-sqrt: R2 = 0.124 (std: 0.056)
  knn-tuned-l: R2 = 0.124 (std: 0.056)
  ridge: R2 = -0.018 (std: 0.093)
  Fallback: Using svr-rbf-xl with R2 = 0.330

Model-based training with 1 models
Best R2: 0.330, Mean R2: 0.223
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9681, entropy=0.2658, kl_div=0.0000
    Epoch 1: policy_loss=-0.0318, value_loss=0.9681, entropy=0.2634, kl_div=0.0467
  Round 1/5: Mean predicted reward = 9.978
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.2586, kl_div=0.0000
    Epoch 1: policy_loss=-0.0236, value_loss=0.9684, entropy=0.2582, kl_div=0.0141
  Round 2/5: Mean predicted reward = 9.884
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9695, entropy=0.2662, kl_div=0.0000
    Epoch 1: policy_loss=-0.0314, value_loss=0.9695, entropy=0.2663, kl_div=-0.0013
  Round 3/5: Mean predicted reward = 10.033
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9678, entropy=0.2642, kl_div=0.0000
    Epoch 1: policy_loss=-0.0472, value_loss=0.9678, entropy=0.2640, kl_div=-0.0065
  Round 4/5: Mean predicted reward = 10.199
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2329, kl_div=0.0000
    Epoch 1: policy_loss=-0.0151, value_loss=0.9689, entropy=0.2321, kl_div=-0.0003
  Round 5/5: Mean predicted reward = 10.170

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 93 Results ---
  Mean Oracle Reward: 10.430
  Min Oracle Reward: 6.780
  Max Oracle Reward: 12.969
  Std Oracle Reward: 1.595
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.223, Max: 0.330, Count: 13
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
  TCGTAGCCGGAC
  GTCGCTCGAGCA
  TAGGAGCGTCCC
  GCCAACAGGGTT
  CCAGTCTCGAGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.515
  Max reward: 12.578
  With intrinsic bonuses: 10.510

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9677, entropy=0.2396, kl_div=0.0000
    Epoch 1: policy_loss=-0.0437, value_loss=0.9677, entropy=0.2377, kl_div=0.0243

=== Surrogate Model Training ===
Total samples: 3058

Training on 2918 samples (removed 140 outliers)
Reward range: [7.43, 13.05], mean: 10.29
  Created 13 candidate models for data size 2918
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.256 (std: 0.049)
  rf-tuned-xl: R2 = 0.261 (std: 0.048)
  gb-tuned-l: R2 = 0.238 (std: 0.053)
  gb-tuned-xl: R2 = 0.238 (std: 0.053)
  xgb-xl: R2 = 0.265 (std: 0.065)
  xgb-l: R2 = 0.265 (std: 0.065)
  mlp-adaptive-xl: R2 = 0.260 (std: 0.059)
  mlp-l: R2 = 0.253 (std: 0.069)
  svr-rbf-xl: R2 = 0.334 (std: 0.048)
  svr-poly-l: R2 = 0.334 (std: 0.048)
  knn-tuned-sqrt: R2 = 0.127 (std: 0.056)
  knn-tuned-l: R2 = 0.127 (std: 0.056)
  ridge: R2 = -0.014 (std: 0.088)
  Fallback: Using svr-rbf-xl with R2 = 0.334

Model-based training with 1 models
Best R2: 0.334, Mean R2: 0.227
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9681, entropy=0.2361, kl_div=0.0000
    Epoch 1: policy_loss=-0.0112, value_loss=0.9681, entropy=0.2356, kl_div=0.0095
  Round 1/5: Mean predicted reward = 9.941
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.2386, kl_div=0.0000
    Epoch 1: policy_loss=-0.0305, value_loss=0.9693, entropy=0.2384, kl_div=-0.0053
  Round 2/5: Mean predicted reward = 10.132
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9677, entropy=0.2575, kl_div=0.0000
    Epoch 1: policy_loss=-0.0351, value_loss=0.9678, entropy=0.2578, kl_div=-0.0222
  Round 3/5: Mean predicted reward = 10.016
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2667, kl_div=0.0000
    Epoch 1: policy_loss=-0.0137, value_loss=0.9689, entropy=0.2670, kl_div=-0.0470
  Round 4/5: Mean predicted reward = 10.167
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2259, kl_div=0.0000
    Epoch 1: policy_loss=-0.0054, value_loss=0.9690, entropy=0.2259, kl_div=0.0439
  Round 5/5: Mean predicted reward = 10.153

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 94 Results ---
  Mean Oracle Reward: 10.462
  Min Oracle Reward: 7.174
  Max Oracle Reward: 12.164
  Std Oracle Reward: 0.993
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.227, Max: 0.334, Count: 13
  Total Sequences Evaluated: 3058

======================================================================
EXPERIMENT ROUND 95/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 3058
  Consistent improvement, increasing LR to 0.000360

--- Round 95 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  TGAATCGCGACG
  CTACCCTGAGGG
  GCTGACCGTGAA
  CTCGTTAGGACA
  GAGTCGGCCACT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.584
  Max reward: 13.289
  With intrinsic bonuses: 10.591

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=0.2539, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4356

=== Surrogate Model Training ===
Total samples: 3090

Training on 2950 samples (removed 140 outliers)
Reward range: [7.42, 13.07], mean: 10.29
  Created 13 candidate models for data size 2950
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.276 (std: 0.062)
  rf-tuned-xl: R2 = 0.281 (std: 0.062)
  gb-tuned-l: R2 = 0.245 (std: 0.054)
  gb-tuned-xl: R2 = 0.245 (std: 0.054)
  xgb-xl: R2 = 0.283 (std: 0.056)
  xgb-l: R2 = 0.283 (std: 0.056)
  mlp-adaptive-xl: R2 = 0.265 (std: 0.070)
  mlp-l: R2 = 0.241 (std: 0.071)
  svr-rbf-xl: R2 = 0.343 (std: 0.054)
  svr-poly-l: R2 = 0.343 (std: 0.054)
  knn-tuned-sqrt: R2 = 0.140 (std: 0.063)
  knn-tuned-l: R2 = 0.140 (std: 0.063)
  ridge: R2 = -0.008 (std: 0.084)
  Fallback: Using svr-rbf-xl with R2 = 0.343

Model-based training with 1 models
Best R2: 0.343, Mean R2: 0.237
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.2177, kl_div=0.0000
    Epoch 1: policy_loss=-0.0656, value_loss=0.9682, entropy=0.2205, kl_div=0.0405
  Round 1/5: Mean predicted reward = 9.435
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.2646, kl_div=0.0000
    Epoch 1: policy_loss=0.8744, value_loss=0.9686, entropy=0.2796, kl_div=-0.6126
  Round 2/5: Mean predicted reward = 9.992
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.2827, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0996
  Round 3/5: Mean predicted reward = 10.264
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2696, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2085
  Round 4/5: Mean predicted reward = 10.053
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2678, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2385
  Round 5/5: Mean predicted reward = 10.384

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 95 Results ---
  Mean Oracle Reward: 10.636
  Min Oracle Reward: 7.210
  Max Oracle Reward: 13.424
  Std Oracle Reward: 1.252
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.237, Max: 0.343, Count: 13
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

--- Generated Sequences (Diversity: 0.969) ---
  GGGCCGTCATCA
  GCGACCGTCATG
  ATAGCGCATGCG
  GGCTGCGTACAC
  GGACACTCTGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.599
  Max reward: 12.915
  With intrinsic bonuses: 10.564

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.2552, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2744

=== Surrogate Model Training ===
Total samples: 3122

Training on 2980 samples (removed 142 outliers)
Reward range: [7.42, 13.07], mean: 10.30
  Created 13 candidate models for data size 2980
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.278 (std: 0.055)
  rf-tuned-xl: R2 = 0.280 (std: 0.061)
  gb-tuned-l: R2 = 0.246 (std: 0.057)
  gb-tuned-xl: R2 = 0.246 (std: 0.057)
  xgb-xl: R2 = 0.269 (std: 0.075)
  xgb-l: R2 = 0.269 (std: 0.075)
  mlp-adaptive-xl: R2 = 0.294 (std: 0.052)
  mlp-l: R2 = 0.275 (std: 0.074)
  svr-rbf-xl: R2 = 0.347 (std: 0.055)
  svr-poly-l: R2 = 0.347 (std: 0.055)
  knn-tuned-sqrt: R2 = 0.138 (std: 0.065)
  knn-tuned-l: R2 = 0.138 (std: 0.065)
  ridge: R2 = -0.014 (std: 0.093)
  Fallback: Using svr-rbf-xl with R2 = 0.347

Model-based training with 1 models
Best R2: 0.347, Mean R2: 0.239
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.2607, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1555
  Round 1/5: Mean predicted reward = 10.179
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.2355, kl_div=0.0000
    Epoch 1: policy_loss=0.0049, value_loss=0.9684, entropy=0.2326, kl_div=-0.0514
  Round 2/5: Mean predicted reward = 10.220
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9679, entropy=0.2584, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1282
  Round 3/5: Mean predicted reward = 10.231
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2324, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1804
  Round 4/5: Mean predicted reward = 10.039
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.2565, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1474
  Round 5/5: Mean predicted reward = 10.274

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 96 Results ---
  Mean Oracle Reward: 10.565
  Min Oracle Reward: 5.000
  Max Oracle Reward: 12.655
  Std Oracle Reward: 1.669
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.239, Max: 0.347, Count: 13
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

--- Generated Sequences (Diversity: 0.969) ---
  TGGACACCGCGT
  TCACCACGTGGG
  CATAGGCGCGTC
  AGCGACGTCCGT
  TGGTGCGCAACC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.383
  Max reward: 12.246
  With intrinsic bonuses: 10.392

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.2382, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1409

=== Surrogate Model Training ===
Total samples: 3154

Training on 3012 samples (removed 142 outliers)
Reward range: [7.42, 13.07], mean: 10.30
  Created 13 candidate models for data size 3012
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.276 (std: 0.056)
  rf-tuned-xl: R2 = 0.281 (std: 0.065)
  gb-tuned-l: R2 = 0.245 (std: 0.057)
  gb-tuned-xl: R2 = 0.245 (std: 0.057)
  xgb-xl: R2 = 0.274 (std: 0.087)
  xgb-l: R2 = 0.274 (std: 0.087)
  mlp-adaptive-xl: R2 = 0.260 (std: 0.088)
  mlp-l: R2 = 0.256 (std: 0.095)
  svr-rbf-xl: R2 = 0.349 (std: 0.059)
  svr-poly-l: R2 = 0.349 (std: 0.059)
  knn-tuned-sqrt: R2 = 0.135 (std: 0.067)
  knn-tuned-l: R2 = 0.135 (std: 0.067)
  ridge: R2 = -0.011 (std: 0.089)
  Fallback: Using svr-rbf-xl with R2 = 0.349

Model-based training with 1 models
Best R2: 0.349, Mean R2: 0.236
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2463, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0951
  Round 1/5: Mean predicted reward = 10.185
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=0.2539, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1296
  Round 2/5: Mean predicted reward = 10.404
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.2302, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1677
  Round 3/5: Mean predicted reward = 10.367
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9677, entropy=0.2498, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1015
  Round 4/5: Mean predicted reward = 10.314
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2370, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1082
  Round 5/5: Mean predicted reward = 10.382

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 97 Results ---
  Mean Oracle Reward: 10.362
  Min Oracle Reward: 7.557
  Max Oracle Reward: 12.177
  Std Oracle Reward: 1.115
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.236, Max: 0.349, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  TCGCGACAGGCT
  GTAGCTACGCAG
  ACGTTCGGGAAC
  AGTCGCATGCCG
  CATGGATCCGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.533
  Max reward: 14.268
  With intrinsic bonuses: 10.539

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.2522, kl_div=0.0000
    Epoch 1: policy_loss=-0.0079, value_loss=0.9686, entropy=0.2516, kl_div=0.0480

=== Surrogate Model Training ===
Total samples: 3186

Training on 3041 samples (removed 145 outliers)
Reward range: [7.42, 13.07], mean: 10.30
  Created 13 candidate models for data size 3041
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.289 (std: 0.071)
  rf-tuned-xl: R2 = 0.282 (std: 0.068)
  gb-tuned-l: R2 = 0.249 (std: 0.056)
  gb-tuned-xl: R2 = 0.249 (std: 0.056)
  xgb-xl: R2 = 0.275 (std: 0.096)
  xgb-l: R2 = 0.275 (std: 0.096)
  mlp-adaptive-xl: R2 = 0.282 (std: 0.099)
  mlp-l: R2 = 0.269 (std: 0.095)
  svr-rbf-xl: R2 = 0.355 (std: 0.065)
  svr-poly-l: R2 = 0.355 (std: 0.065)
  knn-tuned-sqrt: R2 = 0.139 (std: 0.072)
  knn-tuned-l: R2 = 0.139 (std: 0.072)
  ridge: R2 = -0.011 (std: 0.088)
  Fallback: Using svr-rbf-xl with R2 = 0.355

Model-based training with 1 models
Best R2: 0.355, Mean R2: 0.242
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.2215, kl_div=0.0000
    Epoch 1: policy_loss=-0.0144, value_loss=0.9679, entropy=0.2212, kl_div=-0.0325
  Round 1/5: Mean predicted reward = 10.088
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.2176, kl_div=0.0000
    Epoch 1: policy_loss=-0.0488, value_loss=0.9683, entropy=0.2178, kl_div=-0.0881
  Round 2/5: Mean predicted reward = 10.086
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2345, kl_div=0.0000
    Epoch 1: policy_loss=-0.0283, value_loss=0.9689, entropy=0.2345, kl_div=0.0184
  Round 3/5: Mean predicted reward = 10.076
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.2443, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0587
  Round 4/5: Mean predicted reward = 10.130
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.2379, kl_div=0.0000
    Epoch 1: policy_loss=-0.0172, value_loss=0.9690, entropy=0.2372, kl_div=0.0369
  Round 5/5: Mean predicted reward = 10.153

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 98 Results ---
  Mean Oracle Reward: 10.541
  Min Oracle Reward: 6.417
  Max Oracle Reward: 13.987
  Std Oracle Reward: 1.469
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.242, Max: 0.355, Count: 13
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
  ACACTGGGTACG
  CTGCGACAGGCT
  TCGTGCGAGCCA
  CATGGTCGCCAG
  GCTGTGAAGCCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.481
  Max reward: 12.396
  With intrinsic bonuses: 10.450

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9677, entropy=0.2345, kl_div=0.0000
    Epoch 1: policy_loss=-0.0123, value_loss=0.9677, entropy=0.2345, kl_div=0.0179

=== Surrogate Model Training ===
Total samples: 3218

Training on 3075 samples (removed 143 outliers)
Reward range: [7.40, 13.13], mean: 10.31
  Created 13 candidate models for data size 3075
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.299 (std: 0.076)
  rf-tuned-xl: R2 = 0.293 (std: 0.076)
  gb-tuned-l: R2 = 0.256 (std: 0.058)
  gb-tuned-xl: R2 = 0.256 (std: 0.058)
  xgb-xl: R2 = 0.289 (std: 0.100)
  xgb-l: R2 = 0.289 (std: 0.100)
  mlp-adaptive-xl: R2 = 0.287 (std: 0.094)
  mlp-l: R2 = 0.285 (std: 0.091)
  svr-rbf-xl: R2 = 0.356 (std: 0.069)
  svr-poly-l: R2 = 0.356 (std: 0.069)
  knn-tuned-sqrt: R2 = 0.140 (std: 0.075)
  knn-tuned-l: R2 = 0.140 (std: 0.075)
  ridge: R2 = -0.008 (std: 0.081)
  Fallback: Using svr-rbf-xl with R2 = 0.356

Model-based training with 1 models
Best R2: 0.356, Mean R2: 0.249
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.2332, kl_div=0.0000
    Epoch 1: policy_loss=-0.0106, value_loss=0.9686, entropy=0.2337, kl_div=-0.0065
  Round 1/5: Mean predicted reward = 9.695
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9673, entropy=0.2435, kl_div=0.0000
    Epoch 1: policy_loss=-0.0199, value_loss=0.9673, entropy=0.2442, kl_div=0.0039
  Round 2/5: Mean predicted reward = 9.996
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.2596, kl_div=0.0000
    Epoch 1: policy_loss=-0.0354, value_loss=0.9680, entropy=0.2611, kl_div=-0.0181
  Round 3/5: Mean predicted reward = 9.865
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.2713, kl_div=0.0000
    Epoch 1: policy_loss=-0.0157, value_loss=0.9679, entropy=0.2719, kl_div=0.0144
  Round 4/5: Mean predicted reward = 10.182
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.2331, kl_div=0.0000
    Epoch 1: policy_loss=-0.0070, value_loss=0.9683, entropy=0.2334, kl_div=0.0196
  Round 5/5: Mean predicted reward = 10.251

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 99 Results ---
  Mean Oracle Reward: 10.480
  Min Oracle Reward: 6.706
  Max Oracle Reward: 12.750
  Std Oracle Reward: 1.427
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.249, Max: 0.356, Count: 13
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

--- Generated Sequences (Diversity: 0.969) ---
  AGTACCTCGGGA
  CTGCAAGCGTCG
  TAAGACGCCGGT
  CTAGCGTAGCGA
  TGGGCCATCAAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.335
  Max reward: 12.440
  With intrinsic bonuses: 10.355

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2341, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2152

=== Surrogate Model Training ===
Total samples: 3250

Training on 3106 samples (removed 144 outliers)
Reward range: [7.40, 13.13], mean: 10.31
  Created 13 candidate models for data size 3106
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.299 (std: 0.082)
  rf-tuned-xl: R2 = 0.294 (std: 0.076)
  gb-tuned-l: R2 = 0.258 (std: 0.066)
  gb-tuned-xl: R2 = 0.258 (std: 0.066)
  xgb-xl: R2 = 0.284 (std: 0.106)
  xgb-l: R2 = 0.284 (std: 0.106)
  mlp-adaptive-xl: R2 = 0.287 (std: 0.100)
  mlp-l: R2 = 0.275 (std: 0.104)
  svr-rbf-xl: R2 = 0.358 (std: 0.073)
  svr-poly-l: R2 = 0.358 (std: 0.073)
  knn-tuned-sqrt: R2 = 0.146 (std: 0.079)
  knn-tuned-l: R2 = 0.146 (std: 0.079)
  ridge: R2 = -0.007 (std: 0.083)
  Fallback: Using svr-rbf-xl with R2 = 0.358

Model-based training with 1 models
Best R2: 0.358, Mean R2: 0.249
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.2680, kl_div=0.0000
    Epoch 1: policy_loss=0.0204, value_loss=0.9697, entropy=0.2692, kl_div=0.0398
  Round 1/5: Mean predicted reward = 9.732
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.2379, kl_div=0.0000
    Epoch 1: policy_loss=-0.0533, value_loss=0.9688, entropy=0.2403, kl_div=-0.1040
  Round 2/5: Mean predicted reward = 10.006
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.2629, kl_div=0.0000
    Epoch 1: policy_loss=0.0160, value_loss=0.9691, entropy=0.2635, kl_div=-0.2358
  Round 3/5: Mean predicted reward = 9.931
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2381, kl_div=0.0000
    Epoch 1: policy_loss=-0.0337, value_loss=0.9689, entropy=0.2377, kl_div=0.0049
  Round 4/5: Mean predicted reward = 10.178
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9676, entropy=0.2472, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2443
  Round 5/5: Mean predicted reward = 10.353

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 100 Results ---
  Mean Oracle Reward: 10.327
  Min Oracle Reward: 6.739
  Max Oracle Reward: 12.478
  Std Oracle Reward: 1.335
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.249, Max: 0.358, Count: 13
  Total Sequences Evaluated: 3250

======================================================================
DyNA PPO ALGORITHM COMPLETE!
======================================================================
Total rounds executed: 100
Total sequences evaluated: 3250
Best mean reward: 10.814 (achieved at round 81)

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 100
Final Mean Reward: 10.3268
Best Mean Reward: 10.8145
Best Max Reward: 14.4085
Initial Lr: 0.0003
Final Lr: 0.0003
Total Updates: 674
Final Diversity: 0.9688
Convergence Round: 6
==================================================

Generating learning curves...
Learning curves saved to learning_curves.png
Saving training metrics...
Metrics saved to training_metrics.json

======================================================================
FINAL OPTIMIZED SEQUENCES
======================================================================

Deterministic (Exploitation):
  GCCGATCGAGCC: 11.717
  GCCGATCGAGCC: 11.663
  GCCGATCGAGCC: 11.540
  GCCGATCGAGCC: 11.811
  GCCGATCGAGCC: 11.682

Stochastic (Exploration):
  GCCGATCGCGAC: 11.784
  GCGCTGCGCTGC: 11.093
  GCCGTCGCTTCG: 10.381
  GCGCAGTCGCTA: 11.816
  GCCGATCGAGCA: 12.270

Final Performance:
  Mean reward: 11.576
  Max reward: 12.270
  Std reward: 0.484

Best sequence found: GCCGATCGAGCA
   Reward: 12.270

======================================================================
Training complete! Check 'learning_curves.png' and 'training_metrics.json'
======================================================================