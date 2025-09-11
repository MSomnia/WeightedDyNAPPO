======================================================================
RUNNING IMPROVED DyNA PPO WITH BETTER SURROGATE LEARNING
======================================================================
======================================================================
IMPROVED DyNA PPO ALGORITHM
======================================================================
Configuration:
  Number of experiment rounds N = 60
  Number of model-based training rounds M = 5
  Minimum model score τ = 0.2
  Batch size B = 64
  Warm-up phase: True
======================================================================

=== WARM-UP PHASE ===
Generating 50 warm-up samples...
Warm-up statistics:
  Mean reward: 9.838
  Std reward: 3.667
  Min/Max: 0.000 / 13.707

Pre-training surrogate models on warm-up data...

Training on 46 samples (removed 4 outliers)
Reward range: [3.99, 13.71], mean: 10.69
  Created 8 candidate models for data size 46
Current R2 threshold: -0.3
  rf-xs: R2 = 0.215 (std: 0.319)
  rf-s: R2 = 0.197 (std: 0.255)
  knn-xs: R2 = 0.240 (std: 0.168)
  knn-s: R2 = 0.240 (std: 0.168)
  ridge: R2 = 0.113 (std: 0.102)
  gb-xs: R2 = -0.113 (std: 0.367)
  gp: R2 = -23.003 (std: 7.490)
  svr-rbf-s: R2 = 0.078 (std: 0.098)
Initial models trained: 7
Initial R2 scores - Mean: -2.754, Max: 0.240

======================================================================
EXPERIMENT ROUND 1/60
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.300
Total data collected: 50

--- Round 1 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  ATGCTCTTCCCTGCTT
  TGTCATAGCTGTTATT
  TTGGCTCTGGAAAGCT
  GAAGATGGCTATAACT
  CAGATCCGTGAGTATC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.249
  Max reward: 14.183
  With intrinsic bonuses: 11.256

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9882, entropy=1.3837, kl_div=0.0000
    Epoch 2: policy_loss=-0.1658, value_loss=0.9882, entropy=1.3809, kl_div=0.0400
    Epoch 4: policy_loss=-0.2174, value_loss=0.9881, entropy=1.3820, kl_div=0.0274
    Epoch 6: policy_loss=-0.2338, value_loss=0.9880, entropy=1.3818, kl_div=0.0429
    Early stopping at epoch 7: KL divergence = 0.0572

=== Surrogate Model Training ===
Total samples: 114

Training on 107 samples (removed 7 outliers)
Reward range: [6.94, 13.89], mean: 11.21
  Created 11 candidate models for data size 107
Current R2 threshold: -0.3
  rf-m: R2 = -0.115 (std: 0.228)
  rf-l: R2 = -0.089 (std: 0.201)
  gb-m: R2 = -0.343 (std: 0.225)
  gb-l: R2 = -0.345 (std: 0.243)
  xgb-m: R2 = -0.440 (std: 0.359)
  knn-m: R2 = -0.189 (std: 0.294)
  knn-tuned: R2 = -0.189 (std: 0.294)
  mlp-m: R2 = -2.359 (std: 1.188)
  svr-rbf: R2 = 0.049 (std: 0.084)
  svr-poly: R2 = 0.049 (std: 0.084)
  ridge: R2 = -0.017 (std: 0.070)

Model-based training with 7 models
Best R2: 0.049, Mean R2: -0.363
Running 3 virtual training rounds
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9827, entropy=1.3811, kl_div=0.0000
    Epoch 1: policy_loss=-0.0369, value_loss=0.9827, entropy=1.3810, kl_div=-0.0013
  Round 1/3: Mean predicted reward = 11.186
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9839, entropy=1.3812, kl_div=0.0000
    Epoch 1: policy_loss=-0.0538, value_loss=0.9840, entropy=1.3811, kl_div=-0.0117
  Round 2/3: Mean predicted reward = 11.282
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9819, entropy=1.3802, kl_div=0.0000
    Epoch 1: policy_loss=-0.0861, value_loss=0.9819, entropy=1.3787, kl_div=0.0078
  Round 3/3: Mean predicted reward = 11.303

  === Progress Analysis ===
  Status: NORMAL

--- Round 1 Results ---
  Mean Oracle Reward: 11.257
  Min Oracle Reward: 7.381
  Max Oracle Reward: 13.709
  Std Oracle Reward: 1.247
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: -0.363, Max: 0.049, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 114

======================================================================
EXPERIMENT ROUND 2/60
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.300
Total data collected: 114

--- Round 2 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  GGGCACTCGGGAAGCT
  GACGGTGATACAGACT
  GCATCTAAACGAATGC
  CCTTCGACATTAAATC
  GAGCACTTCCTCGTGG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.402
  Max reward: 15.538
  With intrinsic bonuses: 11.365

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9892, entropy=1.3764, kl_div=0.0000
    Early stopping at epoch 2: KL divergence = 0.0895

=== Surrogate Model Training ===
Total samples: 178

Training on 168 samples (removed 10 outliers)
Reward range: [7.32, 14.67], mean: 11.31
  Created 11 candidate models for data size 168
Current R2 threshold: -0.3
  rf-m: R2 = 0.048 (std: 0.083)
  rf-l: R2 = 0.066 (std: 0.119)
  gb-m: R2 = -0.043 (std: 0.185)
  gb-l: R2 = -0.042 (std: 0.183)
  xgb-m: R2 = -0.276 (std: 0.324)
  knn-m: R2 = -0.087 (std: 0.149)
  knn-tuned: R2 = -0.087 (std: 0.149)
  mlp-m: R2 = -2.115 (std: 0.823)
  svr-rbf: R2 = 0.074 (std: 0.091)
  svr-poly: R2 = 0.074 (std: 0.091)
  ridge: R2 = 0.021 (std: 0.083)

Model-based training with 10 models
Best R2: 0.074, Mean R2: -0.215
Running 3 virtual training rounds
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9830, entropy=1.3704, kl_div=0.0000
    Epoch 1: policy_loss=-0.0858, value_loss=0.9830, entropy=1.3651, kl_div=0.0354
  Round 1/3: Mean predicted reward = 11.395
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9870, entropy=1.3576, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1025
  Round 2/3: Mean predicted reward = 11.290
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9867, entropy=1.3489, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1083
  Round 3/3: Mean predicted reward = 11.427

  === Progress Analysis ===
  Status: NORMAL

--- Round 2 Results ---
  Mean Oracle Reward: 11.378
  Min Oracle Reward: 5.963
  Max Oracle Reward: 16.277
  Std Oracle Reward: 1.627
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: -0.215, Max: 0.074, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 178

======================================================================
EXPERIMENT ROUND 3/60
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.300
Total data collected: 178

--- Round 3 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  TCAGACATCGTGCACG
  CGCGATATACTGATCC
  CGACGCGCCGCAAGTC
  CTTCAAGACTACTGCT
  TTCACCGTAAACACCG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.846
  Max reward: 14.556
  With intrinsic bonuses: 12.014

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9881, entropy=1.3370, kl_div=0.0000
    Early stopping at epoch 2: KL divergence = 0.0741

=== Surrogate Model Training ===
Total samples: 242

Training on 232 samples (removed 10 outliers)
Reward range: [7.32, 14.67], mean: 11.47
  Created 11 candidate models for data size 232
Current R2 threshold: -0.3
  rf-m: R2 = 0.087 (std: 0.162)
  rf-l: R2 = 0.079 (std: 0.150)
  gb-m: R2 = -0.045 (std: 0.206)
  gb-l: R2 = -0.046 (std: 0.207)
  xgb-m: R2 = -0.070 (std: 0.223)
  knn-m: R2 = 0.048 (std: 0.136)
  knn-tuned: R2 = 0.048 (std: 0.136)
  mlp-m: R2 = -1.393 (std: 0.624)
  svr-rbf: R2 = 0.095 (std: 0.119)
  svr-poly: R2 = 0.095 (std: 0.119)
  ridge: R2 = -0.000 (std: 0.135)

Model-based training with 10 models
Best R2: 0.095, Mean R2: -0.100
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.106 rf-l:0.105 gb-m:0.093 gb-l:0.093 xgb-m:0.090 knn-m:0.102 knn-tuned:0.102 svr-rbf:0.107 svr-poly:0.107 ridge:0.097
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9870, entropy=1.3266, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0537
  Round 1/3: Mean predicted reward = 11.491
    Using performance-based weights
    Model weights: rf-m:0.106 rf-l:0.105 gb-m:0.093 gb-l:0.093 xgb-m:0.090 knn-m:0.102 knn-tuned:0.102 svr-rbf:0.107 svr-poly:0.107 ridge:0.097
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9844, entropy=1.3172, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0677
  Round 2/3: Mean predicted reward = 11.550
    Using performance-based weights
    Model weights: rf-m:0.106 rf-l:0.105 gb-m:0.093 gb-l:0.093 xgb-m:0.090 knn-m:0.102 knn-tuned:0.102 svr-rbf:0.107 svr-poly:0.107 ridge:0.097
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9892, entropy=1.3118, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0617
  Round 3/3: Mean predicted reward = 11.472

  === Progress Analysis ===
  Status: NORMAL

--- Round 3 Results ---
  Mean Oracle Reward: 11.850
  Min Oracle Reward: 9.141
  Max Oracle Reward: 14.498
  Std Oracle Reward: 1.231
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: -0.100, Max: 0.095, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 242

======================================================================
EXPERIMENT ROUND 4/60
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.280
Total data collected: 242
  Consistent improvement, increasing LR to 0.000045

--- Round 4 Configuration ---
Learning rate: 0.000045
Entropy coefficient: 0.0100
Exploration rate: 0.280

--- Generated Sequences (Diversity: 1.000) ---
  TACGAGGAGACTCTCG
  CACAGACCAGTTTGGT
  TGGCCAAGGCTGAACT
  CCTAAACAGCGGTGGT
  CTCCAGTGGTAAGCAG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.920
  Max reward: 15.034
  With intrinsic bonuses: 12.047

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9897, entropy=1.3006, kl_div=0.0000
    Epoch 1: policy_loss=-0.0193, value_loss=0.9897, entropy=1.2969, kl_div=0.0451
    Early stopping at epoch 2: KL divergence = 0.0895

=== Surrogate Model Training ===
Total samples: 306

Training on 293 samples (removed 13 outliers)
Reward range: [7.77, 15.39], mean: 11.62
  Created 11 candidate models for data size 293
Current R2 threshold: -0.3
  rf-m: R2 = 0.051 (std: 0.178)
  rf-l: R2 = 0.059 (std: 0.173)
  gb-m: R2 = 0.056 (std: 0.164)
  gb-l: R2 = 0.055 (std: 0.167)
  xgb-m: R2 = -0.035 (std: 0.210)
  knn-m: R2 = -0.000 (std: 0.235)
  knn-tuned: R2 = -0.000 (std: 0.235)
  mlp-m: R2 = -0.439 (std: 0.376)
  svr-rbf: R2 = 0.055 (std: 0.112)
  svr-poly: R2 = 0.055 (std: 0.112)
  ridge: R2 = -0.038 (std: 0.086)

Model-based training with 10 models
Best R2: 0.059, Mean R2: -0.017
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.102 rf-l:0.103 gb-m:0.103 gb-l:0.103 xgb-m:0.094 knn-m:0.097 knn-tuned:0.097 svr-rbf:0.103 svr-poly:0.103 ridge:0.094
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9900, entropy=1.2951, kl_div=0.0000
    Epoch 1: policy_loss=-0.0118, value_loss=0.9900, entropy=1.2917, kl_div=0.0365
  Round 1/3: Mean predicted reward = 11.642
    Using performance-based weights
    Model weights: rf-m:0.102 rf-l:0.103 gb-m:0.103 gb-l:0.103 xgb-m:0.094 knn-m:0.097 knn-tuned:0.097 svr-rbf:0.103 svr-poly:0.103 ridge:0.094
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9840, entropy=1.2849, kl_div=0.0000
    Epoch 1: policy_loss=-0.0144, value_loss=0.9840, entropy=1.2813, kl_div=0.0423
  Round 2/3: Mean predicted reward = 11.749
    Using performance-based weights
    Model weights: rf-m:0.102 rf-l:0.103 gb-m:0.103 gb-l:0.103 xgb-m:0.094 knn-m:0.097 knn-tuned:0.097 svr-rbf:0.103 svr-poly:0.103 ridge:0.094
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9841, entropy=1.2749, kl_div=0.0000
    Epoch 1: policy_loss=-0.0170, value_loss=0.9841, entropy=1.2710, kl_div=0.0477
  Round 3/3: Mean predicted reward = 11.637

  === Progress Analysis ===
  Status: NORMAL

--- Round 4 Results ---
  Mean Oracle Reward: 11.929
  Min Oracle Reward: 6.766
  Max Oracle Reward: 15.288
  Std Oracle Reward: 1.545
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: -0.017, Max: 0.059, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 306

======================================================================
EXPERIMENT ROUND 5/60
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.250
Total data collected: 306
  Consistent improvement, increasing LR to 0.000360

--- Round 5 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0100
Exploration rate: 0.250

--- Generated Sequences (Diversity: 1.000) ---
  CCATTTCGGAAGGCAT
  GCAATGGGAACTTCCG
  GGCCGAATCGCTAGTA
  AATCTTGTACGCGCGA
  GTCTAGGGAGTCACAC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.007
  Max reward: 15.424
  With intrinsic bonuses: 12.149

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9908, entropy=1.2686, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2973

=== Surrogate Model Training ===
Total samples: 370

Training on 353 samples (removed 17 outliers)
Reward range: [7.92, 15.39], mean: 11.71
  Created 14 candidate models for data size 353
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.058 (std: 0.189)
  rf-tuned-xl: R2 = -0.035 (std: 0.165)
  gb-tuned-l: R2 = -0.100 (std: 0.214)
  gb-tuned-xl: R2 = -0.095 (std: 0.216)
  xgb-xl: R2 = -0.227 (std: 0.308)
  xgb-l: R2 = -0.227 (std: 0.308)
  mlp-adaptive-xl: R2 = -0.433 (std: 0.316)
  mlp-l: R2 = -0.518 (std: 0.257)
  svr-rbf-xl: R2 = 0.002 (std: 0.101)
  svr-poly-l: R2 = 0.002 (std: 0.101)
  knn-tuned-sqrt: R2 = -0.073 (std: 0.171)
  knn-tuned-l: R2 = -0.073 (std: 0.171)
  ridge: R2 = -0.074 (std: 0.091)
  gp: R2 = -79.888 (std: 15.029)

Model-based training with 11 models
Best R2: 0.002, Mean R2: -5.843
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.093 rf-tuned-xl:0.095 gb-tuned-l:0.090 gb-tuned-xl:0.090 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.099 svr-poly-l:0.099 knn-tuned-sqrt:0.092 knn-tuned-l:0.092 ridge:0.092
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9861, entropy=1.2446, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3168
  Round 1/3: Mean predicted reward = 11.795
    Using performance-based weights
    Model weights: rf-tuned-l:0.093 rf-tuned-xl:0.095 gb-tuned-l:0.090 gb-tuned-xl:0.090 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.099 svr-poly-l:0.099 knn-tuned-sqrt:0.092 knn-tuned-l:0.092 ridge:0.092
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9856, entropy=1.2212, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3467
  Round 2/3: Mean predicted reward = 11.721
    Using performance-based weights
    Model weights: rf-tuned-l:0.093 rf-tuned-xl:0.095 gb-tuned-l:0.090 gb-tuned-xl:0.090 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.099 svr-poly-l:0.099 knn-tuned-sqrt:0.092 knn-tuned-l:0.092 ridge:0.092
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9859, entropy=1.1982, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3800
  Round 3/3: Mean predicted reward = 11.734

  === Progress Analysis ===
  Status: NORMAL

--- Round 5 Results ---
  Mean Oracle Reward: 12.009
  Min Oracle Reward: 6.876
  Max Oracle Reward: 15.331
  Std Oracle Reward: 1.496
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -5.843, Max: 0.002, Count: 14
  New best mean reward!
  Total Sequences Evaluated: 370

======================================================================
EXPERIMENT ROUND 6/60
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.220
Total data collected: 370
  Performance plateaued, reducing LR to 0.000136

--- Round 6 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0100
Exploration rate: 0.220

--- Generated Sequences (Diversity: 1.000) ---
  AAGCCTGCTATATGGC
  GAAGCGATGTCCTGCA
  GGAGGCTAACTTCAGC
  TTCGTCGATACGGAAC
  CGACTGGCATGACTGA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.371
  Max reward: 14.806
  With intrinsic bonuses: 11.441

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9900, entropy=1.1682, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1458

=== Surrogate Model Training ===
Total samples: 434

Training on 413 samples (removed 21 outliers)
Reward range: [7.92, 15.39], mean: 11.73
  Created 14 candidate models for data size 413
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.055 (std: 0.062)
  rf-tuned-xl: R2 = -0.061 (std: 0.058)
  gb-tuned-l: R2 = -0.063 (std: 0.094)
  gb-tuned-xl: R2 = -0.063 (std: 0.093)
  xgb-xl: R2 = -0.257 (std: 0.160)
  xgb-l: R2 = -0.257 (std: 0.160)
  mlp-adaptive-xl: R2 = -0.533 (std: 0.310)
  mlp-l: R2 = -0.480 (std: 0.195)
  svr-rbf-xl: R2 = -0.007 (std: 0.035)
  svr-poly-l: R2 = -0.007 (std: 0.035)
  knn-tuned-sqrt: R2 = -0.076 (std: 0.096)
  knn-tuned-l: R2 = -0.076 (std: 0.096)
  ridge: R2 = -0.072 (std: 0.033)
  gp: R2 = -78.655 (std: 15.406)

Model-based training with 11 models
Best R2: -0.007, Mean R2: -5.762
Running 2 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.093 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.077 xgb-l:0.077 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.092 knn-tuned-l:0.092 ridge:0.092
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9887, entropy=1.1909, kl_div=0.0000
  Round 1/2: Mean predicted reward = 11.710
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.093 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.077 xgb-l:0.077 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.092 knn-tuned-l:0.092 ridge:0.092
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9884, entropy=1.1841, kl_div=0.0000
  Round 2/2: Mean predicted reward = 11.632

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 6 Results ---
  Mean Oracle Reward: 11.407
  Min Oracle Reward: 0.000
  Max Oracle Reward: 14.585
  Std Oracle Reward: 2.257
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -5.762, Max: -0.007, Count: 14
  Total Sequences Evaluated: 434

======================================================================
EXPERIMENT ROUND 7/60
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.190
Total data collected: 434

--- Round 7 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0100
Exploration rate: 0.190

--- Generated Sequences (Diversity: 1.000) ---
  GCGGCGATTCAGATCA
  CGTGTGAAGTCTAACA
  ACCTAAGCTCGAGTGG
  AAGGATTCGCCGGACT
  AATGGTGCCAGTCTCA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.715
  Max reward: 14.798
  With intrinsic bonuses: 11.759

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9908, entropy=1.1453, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1130

=== Surrogate Model Training ===
Total samples: 498

Training on 475 samples (removed 23 outliers)
Reward range: [7.92, 15.39], mean: 11.74
  Created 14 candidate models for data size 475
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.009 (std: 0.176)
  rf-tuned-xl: R2 = -0.031 (std: 0.185)
  gb-tuned-l: R2 = -0.011 (std: 0.232)
  gb-tuned-xl: R2 = -0.011 (std: 0.233)
  xgb-xl: R2 = -0.180 (std: 0.325)
  xgb-l: R2 = -0.180 (std: 0.325)
  mlp-adaptive-xl: R2 = -0.413 (std: 0.502)
  mlp-l: R2 = -0.469 (std: 0.515)
  svr-rbf-xl: R2 = 0.024 (std: 0.136)
  svr-poly-l: R2 = 0.024 (std: 0.136)
  knn-tuned-sqrt: R2 = -0.023 (std: 0.133)
  knn-tuned-l: R2 = -0.023 (std: 0.133)
  ridge: R2 = -0.092 (std: 0.100)
  gp: R2 = -79.547 (std: 17.907)

Model-based training with 11 models
Best R2: 0.024, Mean R2: -5.782
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.092 gb-tuned-l:0.094 gb-tuned-xl:0.094 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.097 svr-poly-l:0.097 knn-tuned-sqrt:0.093 knn-tuned-l:0.093 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9865, entropy=1.1332, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0739
  Round 1/3: Mean predicted reward = 11.730
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.092 gb-tuned-l:0.094 gb-tuned-xl:0.094 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.097 svr-poly-l:0.097 knn-tuned-sqrt:0.093 knn-tuned-l:0.093 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9874, entropy=1.1320, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1037
  Round 2/3: Mean predicted reward = 11.890
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.092 gb-tuned-l:0.094 gb-tuned-xl:0.094 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.097 svr-poly-l:0.097 knn-tuned-sqrt:0.093 knn-tuned-l:0.093 ridge:0.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9840, entropy=1.1309, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1353
  Round 3/3: Mean predicted reward = 11.773

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 7 Results ---
  Mean Oracle Reward: 11.710
  Min Oracle Reward: 6.427
  Max Oracle Reward: 14.769
  Std Oracle Reward: 1.604
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -5.782, Max: 0.024, Count: 14
  Total Sequences Evaluated: 498

======================================================================
EXPERIMENT ROUND 8/60
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.080
Total data collected: 498

--- Round 8 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.080

--- Generated Sequences (Diversity: 1.000) ---
  TTCGACGTTAGACAGC
  GTGTGCACACCTAAGT
  TTCCCATTCGGGAAAG
  GAGATCTTAACGTCCG
  ATTAAGGCCGGTCCGA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.549
  Max reward: 14.237
  With intrinsic bonuses: 11.576

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9867, entropy=1.1219, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0762

=== Surrogate Model Training ===
Total samples: 562

Training on 531 samples (removed 31 outliers)
Reward range: [8.18, 15.06], mean: 11.76
  Created 13 candidate models for data size 531
Current R2 threshold: -0.3
  rf-tuned-l: R2 = 0.020 (std: 0.095)
  rf-tuned-xl: R2 = 0.011 (std: 0.090)
  gb-tuned-l: R2 = -0.017 (std: 0.141)
  gb-tuned-xl: R2 = -0.017 (std: 0.141)
  xgb-xl: R2 = -0.176 (std: 0.181)
  xgb-l: R2 = -0.176 (std: 0.181)
  mlp-adaptive-xl: R2 = -0.350 (std: 0.219)
  mlp-l: R2 = -0.369 (std: 0.205)
  svr-rbf-xl: R2 = 0.042 (std: 0.085)
  svr-poly-l: R2 = 0.042 (std: 0.085)
  knn-tuned-sqrt: R2 = -0.041 (std: 0.116)
  knn-tuned-l: R2 = -0.041 (std: 0.116)
  ridge: R2 = -0.048 (std: 0.052)

Model-based training with 11 models
Best R2: 0.042, Mean R2: -0.086
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.096 rf-tuned-xl:0.095 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.090 knn-tuned-l:0.090 ridge:0.090
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9894, entropy=1.1174, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0604
  Round 1/3: Mean predicted reward = 11.718
    Using performance-based weights
    Model weights: rf-tuned-l:0.096 rf-tuned-xl:0.095 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.090 knn-tuned-l:0.090 ridge:0.090
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9856, entropy=1.1069, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0589
  Round 2/3: Mean predicted reward = 11.752
    Using performance-based weights
    Model weights: rf-tuned-l:0.096 rf-tuned-xl:0.095 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.090 knn-tuned-l:0.090 ridge:0.090
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9857, entropy=1.1116, kl_div=0.0000
    Epoch 1: policy_loss=-0.0187, value_loss=0.9857, entropy=1.1107, kl_div=0.0336
  Round 3/3: Mean predicted reward = 11.811

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 8 Results ---
  Mean Oracle Reward: 11.509
  Min Oracle Reward: 4.399
  Max Oracle Reward: 14.301
  Std Oracle Reward: 1.794
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -0.086, Max: 0.042, Count: 13
  Total Sequences Evaluated: 562

======================================================================
EXPERIMENT ROUND 9/60
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.065
Total data collected: 562

--- Round 9 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.065

--- Generated Sequences (Diversity: 1.000) ---
  GGGTCCAACCTAGTGA
  GAGGACACTTTCTACG
  TAATGCCGAAGCTCGT
  ACATTACCTAGGTCGG
  CAAGCAGGTCGGTTAC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.440
  Max reward: 15.830
  With intrinsic bonuses: 11.500

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9872, entropy=1.1070, kl_div=0.0000
    Epoch 1: policy_loss=-0.0100, value_loss=0.9872, entropy=1.1072, kl_div=0.0067

=== Surrogate Model Training ===
Total samples: 626

Training on 589 samples (removed 37 outliers)
Reward range: [8.18, 15.06], mean: 11.77
  Created 13 candidate models for data size 589
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.032 (std: 0.075)
  rf-tuned-xl: R2 = -0.025 (std: 0.086)
  gb-tuned-l: R2 = -0.033 (std: 0.092)
  gb-tuned-xl: R2 = -0.032 (std: 0.092)
  xgb-xl: R2 = -0.185 (std: 0.134)
  xgb-l: R2 = -0.185 (std: 0.134)
  mlp-adaptive-xl: R2 = -0.348 (std: 0.155)
  mlp-l: R2 = -0.327 (std: 0.147)
  svr-rbf-xl: R2 = 0.024 (std: 0.095)
  svr-poly-l: R2 = 0.024 (std: 0.095)
  knn-tuned-sqrt: R2 = -0.082 (std: 0.098)
  knn-tuned-l: R2 = -0.082 (std: 0.098)
  ridge: R2 = -0.062 (std: 0.057)

Model-based training with 11 models
Best R2: 0.024, Mean R2: -0.103
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.093 rf-tuned-xl:0.094 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.080 xgb-l:0.080 svr-rbf-xl:0.099 svr-poly-l:0.099 knn-tuned-sqrt:0.089 knn-tuned-l:0.089 ridge:0.091
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9874, entropy=1.1093, kl_div=0.0000
    Epoch 1: policy_loss=-0.0088, value_loss=0.9874, entropy=1.1095, kl_div=0.0049
  Round 1/3: Mean predicted reward = 11.798
    Using performance-based weights
    Model weights: rf-tuned-l:0.093 rf-tuned-xl:0.094 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.080 xgb-l:0.080 svr-rbf-xl:0.099 svr-poly-l:0.099 knn-tuned-sqrt:0.089 knn-tuned-l:0.089 ridge:0.091
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9871, entropy=1.1097, kl_div=0.0000
    Epoch 1: policy_loss=-0.0165, value_loss=0.9871, entropy=1.1092, kl_div=0.0172
  Round 2/3: Mean predicted reward = 11.749
    Using performance-based weights
    Model weights: rf-tuned-l:0.093 rf-tuned-xl:0.094 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.080 xgb-l:0.080 svr-rbf-xl:0.099 svr-poly-l:0.099 knn-tuned-sqrt:0.089 knn-tuned-l:0.089 ridge:0.091
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9899, entropy=1.1078, kl_div=0.0000
    Epoch 1: policy_loss=-0.0205, value_loss=0.9899, entropy=1.1063, kl_div=0.0319
  Round 3/3: Mean predicted reward = 11.800

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 9 Results ---
  Mean Oracle Reward: 11.443
  Min Oracle Reward: 5.120
  Max Oracle Reward: 15.460
  Std Oracle Reward: 1.931
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -0.103, Max: 0.024, Count: 13
  Total Sequences Evaluated: 626

======================================================================
EXPERIMENT ROUND 10/60
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 626

--- Round 10 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGCGTTAGGCCGTACA
  AAACCTGGCGGCATTG
  CCAAGGACACGGTTTT
  GAATCAGGGCTCCTAG
  GAACGCTAACTGGGTC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.052
  Max reward: 16.476
  With intrinsic bonuses: 12.094

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9893, entropy=1.1019, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3468

=== Surrogate Model Training ===
Total samples: 690

Training on 654 samples (removed 36 outliers)
Reward range: [7.95, 15.39], mean: 11.79
  Created 13 candidate models for data size 654
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.007 (std: 0.057)
  rf-tuned-xl: R2 = -0.016 (std: 0.048)
  gb-tuned-l: R2 = -0.006 (std: 0.079)
  gb-tuned-xl: R2 = -0.006 (std: 0.079)
  xgb-xl: R2 = -0.180 (std: 0.098)
  xgb-l: R2 = -0.180 (std: 0.098)
  mlp-adaptive-xl: R2 = -0.287 (std: 0.138)
  mlp-l: R2 = -0.253 (std: 0.179)
  svr-rbf-xl: R2 = 0.066 (std: 0.052)
  svr-poly-l: R2 = 0.066 (std: 0.052)
  knn-tuned-sqrt: R2 = -0.046 (std: 0.051)
  knn-tuned-l: R2 = -0.046 (std: 0.051)
  ridge: R2 = -0.036 (std: 0.064)

Model-based training with 13 models
Best R2: 0.066, Mean R2: -0.072
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.062 mlp-l:0.064 svr-rbf-xl:0.088 svr-poly-l:0.088 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.079
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9865, entropy=1.0845, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4186
  Round 1/3: Mean predicted reward = 11.860
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.062 mlp-l:0.064 svr-rbf-xl:0.088 svr-poly-l:0.088 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.079
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9885, entropy=1.0641, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3974
  Round 2/3: Mean predicted reward = 11.921
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.062 mlp-l:0.064 svr-rbf-xl:0.088 svr-poly-l:0.088 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.079
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9880, entropy=1.0380, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4775
  Round 3/3: Mean predicted reward = 11.952

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 10 Results ---
  Mean Oracle Reward: 12.067
  Min Oracle Reward: 7.207
  Max Oracle Reward: 16.381
  Std Oracle Reward: 1.627
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.072, Max: 0.066, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 690

======================================================================
EXPERIMENT ROUND 11/60
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 690

--- Round 11 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCGCAAGCACTGAGTG
  TGCGTTACGCAATCAG
  ATCGACAGTTGACCTG
  CAAAGGCGCCTCTGTG
  GTATATCGCAGAGGCC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.478
  Max reward: 16.443
  With intrinsic bonuses: 12.482

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9843, entropy=1.0168, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5438

=== Surrogate Model Training ===
Total samples: 754

Training on 712 samples (removed 42 outliers)
Reward range: [8.21, 15.32], mean: 11.85
  Created 13 candidate models for data size 712
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.032 (std: 0.101)
  rf-tuned-xl: R2 = -0.035 (std: 0.094)
  gb-tuned-l: R2 = 0.011 (std: 0.102)
  gb-tuned-xl: R2 = 0.011 (std: 0.102)
  xgb-xl: R2 = -0.233 (std: 0.136)
  xgb-l: R2 = -0.233 (std: 0.136)
  mlp-adaptive-xl: R2 = -0.276 (std: 0.161)
  mlp-l: R2 = -0.194 (std: 0.229)
  svr-rbf-xl: R2 = 0.049 (std: 0.094)
  svr-poly-l: R2 = 0.049 (std: 0.094)
  knn-tuned-sqrt: R2 = -0.058 (std: 0.049)
  knn-tuned-l: R2 = -0.058 (std: 0.049)
  ridge: R2 = -0.045 (std: 0.067)

Model-based training with 13 models
Best R2: 0.049, Mean R2: -0.080
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.063 mlp-l:0.068 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.079
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9871, entropy=0.9863, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6187
  Round 1/3: Mean predicted reward = 12.029
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.063 mlp-l:0.068 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.079
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9896, entropy=0.9527, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7607
  Round 2/3: Mean predicted reward = 11.985
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.063 mlp-l:0.068 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.079
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9861, entropy=0.9178, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9585
  Round 3/3: Mean predicted reward = 12.000

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 11 Results ---
  Mean Oracle Reward: 12.493
  Min Oracle Reward: 9.527
  Max Oracle Reward: 16.465
  Std Oracle Reward: 1.321
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.080, Max: 0.049, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 754

======================================================================
EXPERIMENT ROUND 12/60
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 754
  Consistent improvement, increasing LR to 0.000240

--- Round 12 Configuration ---
Learning rate: 0.000240
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCCGCATGGCAAGTAG
  CAGTCGGAAGAGCTCT
  CCTCAGGGGTAAACTT
  AGCTCTCATGCGTAGA
  CACCTTGCGGGGAAGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.279
  Max reward: 15.975
  With intrinsic bonuses: 12.264

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9898, entropy=0.8840, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8713

=== Surrogate Model Training ===
Total samples: 818

Training on 775 samples (removed 43 outliers)
Reward range: [8.21, 15.44], mean: 11.91
  Created 13 candidate models for data size 775
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.015 (std: 0.063)
  rf-tuned-xl: R2 = 0.005 (std: 0.059)
  gb-tuned-l: R2 = 0.044 (std: 0.052)
  gb-tuned-xl: R2 = 0.044 (std: 0.052)
  xgb-xl: R2 = -0.189 (std: 0.039)
  xgb-l: R2 = -0.189 (std: 0.039)
  mlp-adaptive-xl: R2 = -0.176 (std: 0.065)
  mlp-l: R2 = -0.140 (std: 0.097)
  svr-rbf-xl: R2 = 0.066 (std: 0.043)
  svr-poly-l: R2 = 0.066 (std: 0.043)
  knn-tuned-sqrt: R2 = -0.030 (std: 0.061)
  knn-tuned-l: R2 = -0.030 (std: 0.061)
  ridge: R2 = -0.032 (std: 0.045)

Model-based training with 13 models
Best R2: 0.066, Mean R2: -0.044
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.067 mlp-l:0.070 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.078
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9875, entropy=0.8441, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0948
  Round 1/3: Mean predicted reward = 12.084
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.067 mlp-l:0.070 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.078
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9895, entropy=0.8123, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.2541
  Round 2/3: Mean predicted reward = 12.108
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.067 mlp-l:0.070 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.078
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9916, entropy=0.7772, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.3384
  Round 3/3: Mean predicted reward = 12.142

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 12 Results ---
  Mean Oracle Reward: 12.274
  Min Oracle Reward: 4.628
  Max Oracle Reward: 16.103
  Std Oracle Reward: 1.887
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.044, Max: 0.066, Count: 13
  Total Sequences Evaluated: 818

======================================================================
EXPERIMENT ROUND 13/60
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 818

--- Round 13 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCGCGTACGTCACGTA
  AGTCCCGATGCGACGT
  TACCGTGGAGCTGCAC
  TAAGGGTCCGCGCTAC
  AGGGCCTCAGTACTGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.098
  Max reward: 14.976
  With intrinsic bonuses: 12.024

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9860, entropy=0.7403, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6238

=== Surrogate Model Training ===
Total samples: 882

Training on 840 samples (removed 42 outliers)
Reward range: [8.18, 15.64], mean: 11.93
  Created 13 candidate models for data size 840
Current R2 threshold: -0.3
  rf-tuned-l: R2 = 0.035 (std: 0.097)
  rf-tuned-xl: R2 = 0.018 (std: 0.095)
  gb-tuned-l: R2 = 0.063 (std: 0.079)
  gb-tuned-xl: R2 = 0.063 (std: 0.079)
  xgb-xl: R2 = -0.143 (std: 0.129)
  xgb-l: R2 = -0.143 (std: 0.129)
  mlp-adaptive-xl: R2 = -0.066 (std: 0.095)
  mlp-l: R2 = -0.086 (std: 0.115)
  svr-rbf-xl: R2 = 0.086 (std: 0.075)
  svr-poly-l: R2 = 0.086 (std: 0.075)
  knn-tuned-sqrt: R2 = -0.032 (std: 0.067)
  knn-tuned-l: R2 = -0.032 (std: 0.067)
  ridge: R2 = -0.023 (std: 0.075)

Model-based training with 13 models
Best R2: 0.086, Mean R2: -0.013
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.079 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.073 mlp-l:0.071 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9903, entropy=0.7231, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6444
  Round 1/3: Mean predicted reward = 12.136
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.079 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.073 mlp-l:0.071 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9901, entropy=0.7163, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6609
  Round 2/3: Mean predicted reward = 12.056
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.079 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.073 mlp-l:0.071 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9912, entropy=0.6960, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7654
  Round 3/3: Mean predicted reward = 12.139

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 13 Results ---
  Mean Oracle Reward: 12.066
  Min Oracle Reward: 6.935
  Max Oracle Reward: 14.891
  Std Oracle Reward: 1.854
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.013, Max: 0.086, Count: 13
  Total Sequences Evaluated: 882

======================================================================
EXPERIMENT ROUND 14/60
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 882

--- Round 14 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TAGGGGCCAATGTCCC
  GGATGTCGGCACTACC
  CTCGACCGTAGGTGAA
  TTCGACGCCTAGCAGG
  ACCGGCTGATCGAGGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.343
  Max reward: 14.471
  With intrinsic bonuses: 11.343

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9803, entropy=0.6866, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1874

=== Surrogate Model Training ===
Total samples: 946

Training on 901 samples (removed 45 outliers)
Reward range: [8.15, 15.64], mean: 11.92
  Created 13 candidate models for data size 901
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.002 (std: 0.100)
  rf-tuned-xl: R2 = 0.009 (std: 0.105)
  gb-tuned-l: R2 = 0.044 (std: 0.068)
  gb-tuned-xl: R2 = 0.044 (std: 0.068)
  xgb-xl: R2 = -0.226 (std: 0.138)
  xgb-l: R2 = -0.226 (std: 0.138)
  mlp-adaptive-xl: R2 = -0.120 (std: 0.117)
  mlp-l: R2 = -0.034 (std: 0.143)
  svr-rbf-xl: R2 = 0.077 (std: 0.066)
  svr-poly-l: R2 = 0.077 (std: 0.066)
  knn-tuned-sqrt: R2 = -0.072 (std: 0.102)
  knn-tuned-l: R2 = -0.072 (std: 0.102)
  ridge: R2 = -0.061 (std: 0.066)

Model-based training with 13 models
Best R2: 0.077, Mean R2: -0.043
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.081 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.064 xgb-l:0.064 mlp-adaptive-xl:0.071 mlp-l:0.077 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9881, entropy=0.6830, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2132
  Round 1/3: Mean predicted reward = 11.938
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.081 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.064 xgb-l:0.064 mlp-adaptive-xl:0.071 mlp-l:0.077 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9851, entropy=0.6798, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2005
  Round 2/3: Mean predicted reward = 12.050
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.081 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.064 xgb-l:0.064 mlp-adaptive-xl:0.071 mlp-l:0.077 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9925, entropy=0.6736, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2438
  Round 3/3: Mean predicted reward = 12.049

  === Progress Analysis ===
  Status: NORMAL

--- Round 14 Results ---
  Mean Oracle Reward: 11.347
  Min Oracle Reward: 0.000
  Max Oracle Reward: 14.555
  Std Oracle Reward: 2.563
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.043, Max: 0.077, Count: 13
  Total Sequences Evaluated: 946

======================================================================
EXPERIMENT ROUND 15/60
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 946

--- Round 15 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ACGGCTCGACTCGGGA
  TCTGGGCGCCCAGAAG
  CAGGAGGTTCCGCCGA
  GCCACTGCACGGGTAT
  GGCGACCTCGGTACAG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.967
  Max reward: 15.277
  With intrinsic bonuses: 11.969

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9872, entropy=0.6691, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.9815

=== Surrogate Model Training ===
Total samples: 1010

Training on 963 samples (removed 47 outliers)
Reward range: [8.15, 15.64], mean: 11.93
  Created 13 candidate models for data size 963
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.006 (std: 0.070)
  rf-tuned-xl: R2 = 0.008 (std: 0.062)
  gb-tuned-l: R2 = 0.053 (std: 0.068)
  gb-tuned-xl: R2 = 0.053 (std: 0.068)
  xgb-xl: R2 = -0.174 (std: 0.105)
  xgb-l: R2 = -0.174 (std: 0.105)
  mlp-adaptive-xl: R2 = -0.042 (std: 0.066)
  mlp-l: R2 = -0.080 (std: 0.055)
  svr-rbf-xl: R2 = 0.080 (std: 0.050)
  svr-poly-l: R2 = 0.080 (std: 0.050)
  knn-tuned-sqrt: R2 = -0.078 (std: 0.049)
  knn-tuned-l: R2 = -0.078 (std: 0.049)
  ridge: R2 = -0.062 (std: 0.035)

Model-based training with 13 models
Best R2: 0.080, Mean R2: -0.032
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.076 mlp-l:0.073 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9883, entropy=0.6406, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.1761
  Round 1/3: Mean predicted reward = 11.970
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.076 mlp-l:0.073 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9857, entropy=0.6209, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.2652
  Round 2/3: Mean predicted reward = 12.003
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.076 mlp-l:0.073 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9879, entropy=0.6045, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.5227
  Round 3/3: Mean predicted reward = 12.000

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 15 Results ---
  Mean Oracle Reward: 11.962
  Min Oracle Reward: 5.622
  Max Oracle Reward: 14.772
  Std Oracle Reward: 1.681
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.032, Max: 0.080, Count: 13
  Total Sequences Evaluated: 1010

======================================================================
EXPERIMENT ROUND 16/60
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1010

--- Round 16 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTTAACCGCTGCGGAG
  GAGTGCTGGCCAGCCA
  CATCCACCGTGTGGAG
  GTTCAACCGGGGTCAC
  GCGAAGGACTGCCGCT
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.799
  Max reward: 15.159
  With intrinsic bonuses: 11.778

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9879, entropy=0.5816, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.3921

=== Surrogate Model Training ===
Total samples: 1074

Training on 1024 samples (removed 50 outliers)
Reward range: [8.15, 15.64], mean: 11.94
  Created 13 candidate models for data size 1024
Current R2 threshold: -0.27999999999999997
  rf-tuned-l: R2 = 0.033 (std: 0.065)
  rf-tuned-xl: R2 = 0.032 (std: 0.058)
  gb-tuned-l: R2 = 0.064 (std: 0.066)
  gb-tuned-xl: R2 = 0.064 (std: 0.066)
  xgb-xl: R2 = -0.148 (std: 0.135)
  xgb-l: R2 = -0.148 (std: 0.135)
  mlp-adaptive-xl: R2 = -0.047 (std: 0.033)
  mlp-l: R2 = -0.085 (std: 0.075)
  svr-rbf-xl: R2 = 0.103 (std: 0.056)
  svr-poly-l: R2 = 0.103 (std: 0.056)
  knn-tuned-sqrt: R2 = -0.063 (std: 0.045)
  knn-tuned-l: R2 = -0.063 (std: 0.045)
  ridge: R2 = -0.045 (std: 0.023)

Model-based training with 13 models
Best R2: 0.103, Mean R2: -0.016
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.074 mlp-l:0.071 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9847, entropy=0.5624, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.5092
  Round 1/3: Mean predicted reward = 11.940
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.074 mlp-l:0.071 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9866, entropy=0.5603, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.5311
  Round 2/3: Mean predicted reward = 12.133
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.074 mlp-l:0.071 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9901, entropy=0.5474, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 3.0636
  Round 3/3: Mean predicted reward = 12.043

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 16 Results ---
  Mean Oracle Reward: 11.783
  Min Oracle Reward: 6.630
  Max Oracle Reward: 15.223
  Std Oracle Reward: 1.831
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.016, Max: 0.103, Count: 13
  Total Sequences Evaluated: 1074

======================================================================
EXPERIMENT ROUND 17/60
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1074

--- Round 17 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCGCCGGGAGATATCG
  CACCGGTGCGGTACAG
  CTCGGTGCAATCGAAT
  CCCCTGAAGAGGTGTC
  TTACGCAGACGCTGCG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.174
  Max reward: 15.588
  With intrinsic bonuses: 12.193

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9857, entropy=0.5357, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.0964

=== Surrogate Model Training ===
Total samples: 1138

Training on 1088 samples (removed 50 outliers)
Reward range: [8.15, 15.71], mean: 11.95
  Created 13 candidate models for data size 1088
Current R2 threshold: -0.26
  rf-tuned-l: R2 = 0.057 (std: 0.104)
  rf-tuned-xl: R2 = 0.074 (std: 0.086)
  gb-tuned-l: R2 = 0.079 (std: 0.097)
  gb-tuned-xl: R2 = 0.079 (std: 0.097)
  xgb-xl: R2 = -0.100 (std: 0.160)
  xgb-l: R2 = -0.100 (std: 0.160)
  mlp-adaptive-xl: R2 = -0.037 (std: 0.160)
  mlp-l: R2 = -0.029 (std: 0.149)
  svr-rbf-xl: R2 = 0.125 (std: 0.109)
  svr-poly-l: R2 = 0.125 (std: 0.109)
  knn-tuned-sqrt: R2 = -0.039 (std: 0.125)
  knn-tuned-l: R2 = -0.039 (std: 0.125)
  ridge: R2 = -0.033 (std: 0.066)

Model-based training with 13 models
Best R2: 0.125, Mean R2: 0.013
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.082 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.073 mlp-l:0.074 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9831, entropy=0.5241, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.9299
  Round 1/3: Mean predicted reward = 11.919
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.082 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.073 mlp-l:0.074 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9867, entropy=0.5154, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.0947
  Round 2/3: Mean predicted reward = 12.053
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.082 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.073 mlp-l:0.074 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9883, entropy=0.5036, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.2134
  Round 3/3: Mean predicted reward = 12.074

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 17 Results ---
  Mean Oracle Reward: 12.130
  Min Oracle Reward: 8.452
  Max Oracle Reward: 15.394
  Std Oracle Reward: 1.495
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.013, Max: 0.125, Count: 13
  Total Sequences Evaluated: 1138

======================================================================
EXPERIMENT ROUND 18/60
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1138

--- Round 18 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCGGGCCAACTAGTGC
  TCGTCAAGGGACCCGG
  CCGGGAGGCCCGTTAA
  GAGTAGTCCCCTGGAC
  GGCTATGCCGCACGGA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.822
  Max reward: 15.713
  With intrinsic bonuses: 11.839

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9822, entropy=0.5078, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9716

=== Surrogate Model Training ===
Total samples: 1202

Training on 1146 samples (removed 56 outliers)
Reward range: [8.15, 15.71], mean: 11.97
  Created 13 candidate models for data size 1146
Current R2 threshold: -0.24
  rf-tuned-l: R2 = 0.074 (std: 0.082)
  rf-tuned-xl: R2 = 0.065 (std: 0.078)
  gb-tuned-l: R2 = 0.100 (std: 0.081)
  gb-tuned-xl: R2 = 0.100 (std: 0.081)
  xgb-xl: R2 = -0.142 (std: 0.136)
  xgb-l: R2 = -0.142 (std: 0.136)
  mlp-adaptive-xl: R2 = 0.001 (std: 0.111)
  mlp-l: R2 = 0.002 (std: 0.087)
  svr-rbf-xl: R2 = 0.134 (std: 0.085)
  svr-poly-l: R2 = 0.134 (std: 0.085)
  knn-tuned-sqrt: R2 = -0.031 (std: 0.078)
  knn-tuned-l: R2 = -0.031 (std: 0.078)
  ridge: R2 = -0.018 (std: 0.064)

Model-based training with 13 models
Best R2: 0.134, Mean R2: 0.019
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.065 xgb-l:0.065 mlp-adaptive-xl:0.075 mlp-l:0.075 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9861, entropy=0.5015, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9217
  Round 1/3: Mean predicted reward = 11.994
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.065 xgb-l:0.065 mlp-adaptive-xl:0.075 mlp-l:0.075 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9912, entropy=0.4929, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1348
  Round 2/3: Mean predicted reward = 12.038
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.065 xgb-l:0.065 mlp-adaptive-xl:0.075 mlp-l:0.075 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9842, entropy=0.5073, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0378
  Round 3/3: Mean predicted reward = 12.095

  === Progress Analysis ===
  Status: NORMAL

--- Round 18 Results ---
  Mean Oracle Reward: 11.828
  Min Oracle Reward: 0.000
  Max Oracle Reward: 15.998
  Std Oracle Reward: 2.352
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.019, Max: 0.134, Count: 13
  Total Sequences Evaluated: 1202

======================================================================
EXPERIMENT ROUND 19/60
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1202

--- Round 19 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGATACCGGCCCGTGA
  CGTCCACGAGATGATG
  GGCAGCGACGCGTTCA
  CTCGGACGAGACCTGG
  TGAAGCGCCGTCGACT
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.761
  Max reward: 16.163
  With intrinsic bonuses: 11.793

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9859, entropy=0.4995, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3497

=== Surrogate Model Training ===
Total samples: 1266

Training on 1209 samples (removed 57 outliers)
Reward range: [8.09, 15.71], mean: 11.97
  Created 13 candidate models for data size 1209
Current R2 threshold: -0.21999999999999997
  rf-tuned-l: R2 = 0.060 (std: 0.113)
  rf-tuned-xl: R2 = 0.070 (std: 0.104)
  gb-tuned-l: R2 = 0.102 (std: 0.097)
  gb-tuned-xl: R2 = 0.102 (std: 0.097)
  xgb-xl: R2 = -0.106 (std: 0.149)
  xgb-l: R2 = -0.106 (std: 0.149)
  mlp-adaptive-xl: R2 = 0.000 (std: 0.116)
  mlp-l: R2 = 0.014 (std: 0.099)
  svr-rbf-xl: R2 = 0.136 (std: 0.083)
  svr-poly-l: R2 = 0.136 (std: 0.083)
  knn-tuned-sqrt: R2 = -0.001 (std: 0.110)
  knn-tuned-l: R2 = -0.001 (std: 0.110)
  ridge: R2 = -0.013 (std: 0.063)

Model-based training with 13 models
Best R2: 0.136, Mean R2: 0.030
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.074 mlp-l:0.075 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9836, entropy=0.4932, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3796
  Round 1/3: Mean predicted reward = 11.877
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.074 mlp-l:0.075 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9825, entropy=0.4940, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3111
  Round 2/3: Mean predicted reward = 11.962
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.074 mlp-l:0.075 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9894, entropy=0.4940, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4031
  Round 3/3: Mean predicted reward = 12.044

  === Progress Analysis ===
  Status: NORMAL

--- Round 19 Results ---
  Mean Oracle Reward: 11.760
  Min Oracle Reward: 0.000
  Max Oracle Reward: 16.016
  Std Oracle Reward: 2.229
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.030, Max: 0.136, Count: 13
  Total Sequences Evaluated: 1266

======================================================================
EXPERIMENT ROUND 20/60
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1266

--- Round 20 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGACCGAGGTCACTGG
  CCGGGGTGAGCACTAC
  TGACCTGAACCGCGGG
  CTACAGCTCGGGCTGA
  AGCGGTGCGACGTCCA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.707
  Max reward: 16.317
  With intrinsic bonuses: 11.689

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9862, entropy=0.4892, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.6793

=== Surrogate Model Training ===
Total samples: 1330

Training on 1267 samples (removed 63 outliers)
Reward range: [8.15, 15.71], mean: 11.98
  Created 13 candidate models for data size 1267
Current R2 threshold: -0.19999999999999998
  rf-tuned-l: R2 = 0.078 (std: 0.119)
  rf-tuned-xl: R2 = 0.077 (std: 0.119)
  gb-tuned-l: R2 = 0.095 (std: 0.096)
  gb-tuned-xl: R2 = 0.095 (std: 0.096)
  xgb-xl: R2 = -0.070 (std: 0.134)
  xgb-l: R2 = -0.070 (std: 0.134)
  mlp-adaptive-xl: R2 = 0.005 (std: 0.135)
  mlp-l: R2 = 0.054 (std: 0.101)
  svr-rbf-xl: R2 = 0.139 (std: 0.098)
  svr-poly-l: R2 = 0.139 (std: 0.098)
  knn-tuned-sqrt: R2 = -0.023 (std: 0.121)
  knn-tuned-l: R2 = -0.023 (std: 0.121)
  ridge: R2 = -0.012 (std: 0.072)

Model-based training with 13 models
Best R2: 0.139, Mean R2: 0.037
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.074 mlp-l:0.078 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9871, entropy=0.4885, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.8916
  Round 1/3: Mean predicted reward = 11.937
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.074 mlp-l:0.078 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9882, entropy=0.4918, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.3869
  Round 2/3: Mean predicted reward = 12.113
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.074 mlp-l:0.078 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9894, entropy=0.4932, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.3344
  Round 3/3: Mean predicted reward = 12.030

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 20 Results ---
  Mean Oracle Reward: 11.692
  Min Oracle Reward: 0.999
  Max Oracle Reward: 16.093
  Std Oracle Reward: 2.461
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.037, Max: 0.139, Count: 13
  Total Sequences Evaluated: 1330

======================================================================
EXPERIMENT ROUND 21/60
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1330
  Performance plateaued, reducing LR to 0.000136

--- Round 21 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CATGGGCACCGGCAGT
  CTTCAACCGGGCGGAG
  GAACGCTCTGCAGTGA
  GCGCAAGCAGTCGCTG
  ATAGATCGCCGCGTCG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.445
  Max reward: 16.888
  With intrinsic bonuses: 12.428

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9873, entropy=0.4730, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9891

=== Surrogate Model Training ===
Total samples: 1394

Training on 1326 samples (removed 68 outliers)
Reward range: [8.15, 15.71], mean: 12.00
  Created 13 candidate models for data size 1326
Current R2 threshold: -0.18
  rf-tuned-l: R2 = 0.074 (std: 0.096)
  rf-tuned-xl: R2 = 0.068 (std: 0.100)
  gb-tuned-l: R2 = 0.119 (std: 0.059)
  gb-tuned-xl: R2 = 0.119 (std: 0.059)
  xgb-xl: R2 = -0.051 (std: 0.098)
  xgb-l: R2 = -0.051 (std: 0.098)
  mlp-adaptive-xl: R2 = 0.047 (std: 0.063)
  mlp-l: R2 = 0.034 (std: 0.055)
  svr-rbf-xl: R2 = 0.154 (std: 0.075)
  svr-poly-l: R2 = 0.154 (std: 0.075)
  knn-tuned-sqrt: R2 = 0.000 (std: 0.075)
  knn-tuned-l: R2 = 0.000 (std: 0.075)
  ridge: R2 = -0.007 (std: 0.061)

Model-based training with 13 models
Best R2: 0.154, Mean R2: 0.051
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.143 gb-tuned-xl:0.018 xgb-xl:0.262 xgb-l:0.101 mlp-adaptive-xl:0.207 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.174 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.095
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9837, entropy=0.4671, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8728
  Round 1/3: Mean predicted reward = 11.925
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.143 gb-tuned-xl:0.018 xgb-xl:0.262 xgb-l:0.101 mlp-adaptive-xl:0.207 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.174 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.095
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9874, entropy=0.4681, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8129
  Round 2/3: Mean predicted reward = 12.092
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.143 gb-tuned-xl:0.018 xgb-xl:0.262 xgb-l:0.101 mlp-adaptive-xl:0.207 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.174 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.095
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9879, entropy=0.4691, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9144
  Round 3/3: Mean predicted reward = 12.171

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 21 Results ---
  Mean Oracle Reward: 12.430
  Min Oracle Reward: 3.349
  Max Oracle Reward: 16.754
  Std Oracle Reward: 2.047
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.051, Max: 0.154, Count: 13
  Total Sequences Evaluated: 1394

======================================================================
EXPERIMENT ROUND 22/60
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1394

--- Round 22 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCACGGAGCTGCTGGA
  CACGGCAGGTTGACCG
  ACGCGCGGATGCATCG
  GCGGGCCTCGCATAGA
  CGTGGCATCCAGGAGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.236
  Max reward: 17.728
  With intrinsic bonuses: 12.208

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9858, entropy=0.4568, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9856

=== Surrogate Model Training ===
Total samples: 1458

Training on 1385 samples (removed 73 outliers)
Reward range: [8.15, 15.71], mean: 12.01
  Created 13 candidate models for data size 1385
Current R2 threshold: -0.15999999999999998
  rf-tuned-l: R2 = 0.062 (std: 0.065)
  rf-tuned-xl: R2 = 0.081 (std: 0.072)
  gb-tuned-l: R2 = 0.098 (std: 0.074)
  gb-tuned-xl: R2 = 0.098 (std: 0.074)
  xgb-xl: R2 = -0.117 (std: 0.143)
  xgb-l: R2 = -0.117 (std: 0.143)
  mlp-adaptive-xl: R2 = 0.049 (std: 0.067)
  mlp-l: R2 = 0.055 (std: 0.063)
  svr-rbf-xl: R2 = 0.139 (std: 0.050)
  svr-poly-l: R2 = 0.139 (std: 0.050)
  knn-tuned-sqrt: R2 = -0.013 (std: 0.083)
  knn-tuned-l: R2 = -0.013 (std: 0.083)
  ridge: R2 = -0.007 (std: 0.067)

Model-based training with 13 models
Best R2: 0.139, Mean R2: 0.035
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.123 rf-tuned-xl:0.395 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.253 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000 knn-tuned-sqrt:0.226 knn-tuned-l:0.000 ridge:0.003
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9868, entropy=0.4566, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7961
  Round 1/3: Mean predicted reward = 12.060
    Using ridge regression weights
    Model weights: rf-tuned-l:0.123 rf-tuned-xl:0.395 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.253 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000 knn-tuned-sqrt:0.226 knn-tuned-l:0.000 ridge:0.003
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9862, entropy=0.4325, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8455
  Round 2/3: Mean predicted reward = 12.038
    Using ridge regression weights
    Model weights: rf-tuned-l:0.123 rf-tuned-xl:0.395 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.253 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000 knn-tuned-sqrt:0.226 knn-tuned-l:0.000 ridge:0.003
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9881, entropy=0.4486, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8173
  Round 3/3: Mean predicted reward = 12.149

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 22 Results ---
  Mean Oracle Reward: 12.265
  Min Oracle Reward: 6.640
  Max Oracle Reward: 17.552
  Std Oracle Reward: 1.891
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.035, Max: 0.139, Count: 13
  Total Sequences Evaluated: 1458

======================================================================
EXPERIMENT ROUND 23/60
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1458

--- Round 23 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCTCGTCCGCGGGAAA
  TCCAAGCGGGTAGGCC
  CCTGCAGTGACGAGGC
  CCCGGAGCCGGTATAG
  CGAATGTGAGCGCGCC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.266
  Max reward: 16.408
  With intrinsic bonuses: 12.287

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9870, entropy=0.4308, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2922

=== Surrogate Model Training ===
Total samples: 1522

Training on 1444 samples (removed 78 outliers)
Reward range: [8.21, 15.71], mean: 12.03
  Created 13 candidate models for data size 1444
Current R2 threshold: -0.13999999999999999
  rf-tuned-l: R2 = 0.100 (std: 0.049)
  rf-tuned-xl: R2 = 0.106 (std: 0.035)
  gb-tuned-l: R2 = 0.108 (std: 0.057)
  gb-tuned-xl: R2 = 0.108 (std: 0.057)
  xgb-xl: R2 = -0.081 (std: 0.097)
  xgb-l: R2 = -0.081 (std: 0.097)
  mlp-adaptive-xl: R2 = 0.039 (std: 0.075)
  mlp-l: R2 = 0.050 (std: 0.069)
  svr-rbf-xl: R2 = 0.153 (std: 0.043)
  svr-poly-l: R2 = 0.153 (std: 0.043)
  knn-tuned-sqrt: R2 = 0.003 (std: 0.060)
  knn-tuned-l: R2 = 0.003 (std: 0.060)
  ridge: R2 = -0.004 (std: 0.075)

Model-based training with 13 models
Best R2: 0.153, Mean R2: 0.051
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.040 rf-tuned-xl:0.166 gb-tuned-l:0.000 gb-tuned-xl:0.141 xgb-xl:0.454 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.076 knn-tuned-sqrt:0.009 knn-tuned-l:0.114 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9870, entropy=0.4102, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2441
  Round 1/3: Mean predicted reward = 12.259
    Using ridge regression weights
    Model weights: rf-tuned-l:0.040 rf-tuned-xl:0.166 gb-tuned-l:0.000 gb-tuned-xl:0.141 xgb-xl:0.454 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.076 knn-tuned-sqrt:0.009 knn-tuned-l:0.114 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9861, entropy=0.4108, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1651
  Round 2/3: Mean predicted reward = 12.049
    Using ridge regression weights
    Model weights: rf-tuned-l:0.040 rf-tuned-xl:0.166 gb-tuned-l:0.000 gb-tuned-xl:0.141 xgb-xl:0.454 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.076 knn-tuned-sqrt:0.009 knn-tuned-l:0.114 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9875, entropy=0.4176, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1646
  Round 3/3: Mean predicted reward = 12.044

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 23 Results ---
  Mean Oracle Reward: 12.277
  Min Oracle Reward: 3.611
  Max Oracle Reward: 16.286
  Std Oracle Reward: 1.904
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.051, Max: 0.153, Count: 13
  Total Sequences Evaluated: 1522

======================================================================
EXPERIMENT ROUND 24/60
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1522
  Performance plateaued, reducing LR to 0.000019

--- Round 24 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGCACCCAATTGGGCG
  CGCGATACACGGCTGG
  AGGTCATCCGCGAGCG
  CCGAATGCGGCAGATT
  GCCGGCCATTGGCAGA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.371
  Max reward: 17.515
  With intrinsic bonuses: 12.402

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9899, entropy=0.4024, kl_div=0.0000
    Epoch 1: policy_loss=-0.0075, value_loss=0.9899, entropy=0.4014, kl_div=0.0342

=== Surrogate Model Training ===
Total samples: 1586

Training on 1506 samples (removed 80 outliers)
Reward range: [8.21, 15.71], mean: 12.05
  Created 13 candidate models for data size 1506
Current R2 threshold: -0.12
  rf-tuned-l: R2 = 0.131 (std: 0.033)
  rf-tuned-xl: R2 = 0.130 (std: 0.041)
  gb-tuned-l: R2 = 0.127 (std: 0.040)
  gb-tuned-xl: R2 = 0.127 (std: 0.040)
  xgb-xl: R2 = -0.029 (std: 0.081)
  xgb-l: R2 = -0.029 (std: 0.081)
  mlp-adaptive-xl: R2 = 0.043 (std: 0.058)
  mlp-l: R2 = 0.070 (std: 0.050)
  svr-rbf-xl: R2 = 0.168 (std: 0.026)
  svr-poly-l: R2 = 0.168 (std: 0.026)
  knn-tuned-sqrt: R2 = 0.015 (std: 0.049)
  knn-tuned-l: R2 = 0.015 (std: 0.049)
  ridge: R2 = 0.014 (std: 0.053)

Model-based training with 13 models
Best R2: 0.168, Mean R2: 0.073
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.411 gb-tuned-l:0.013 gb-tuned-xl:0.000 xgb-xl:0.220 xgb-l:0.033 mlp-adaptive-xl:0.114 mlp-l:0.042 svr-rbf-xl:0.028 svr-poly-l:0.010 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.129
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9850, entropy=0.4069, kl_div=0.0000
    Epoch 1: policy_loss=-0.0060, value_loss=0.9850, entropy=0.4060, kl_div=0.0233
  Round 1/3: Mean predicted reward = 11.807
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.411 gb-tuned-l:0.013 gb-tuned-xl:0.000 xgb-xl:0.220 xgb-l:0.033 mlp-adaptive-xl:0.114 mlp-l:0.042 svr-rbf-xl:0.028 svr-poly-l:0.010 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.129
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9838, entropy=0.4103, kl_div=0.0000
    Epoch 1: policy_loss=-0.0084, value_loss=0.9838, entropy=0.4097, kl_div=0.0015
  Round 2/3: Mean predicted reward = 11.966
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.411 gb-tuned-l:0.013 gb-tuned-xl:0.000 xgb-xl:0.220 xgb-l:0.033 mlp-adaptive-xl:0.114 mlp-l:0.042 svr-rbf-xl:0.028 svr-poly-l:0.010 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.129
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9866, entropy=0.4079, kl_div=0.0000
    Epoch 1: policy_loss=-0.0075, value_loss=0.9866, entropy=0.4071, kl_div=0.0060
  Round 3/3: Mean predicted reward = 12.289

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 24 Results ---
  Mean Oracle Reward: 12.397
  Min Oracle Reward: 7.773
  Max Oracle Reward: 17.733
  Std Oracle Reward: 1.662
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.073, Max: 0.168, Count: 13
  Total Sequences Evaluated: 1586

======================================================================
EXPERIMENT ROUND 25/60
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1586
  Performance plateaued, reducing LR to 0.000150

--- Round 25 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGGCGTAGCGCGCACA
  CCCGGTAATAGCGGCG
  CTGAAGAGCCTCCGGG
  TGAGTAGACGCCGCCG
  GAGCCAGCTCACGGTT
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.300
  Max reward: 15.146
  With intrinsic bonuses: 12.320

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9919, entropy=0.3988, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1678

=== Surrogate Model Training ===
Total samples: 1650

Training on 1572 samples (removed 78 outliers)
Reward range: [8.21, 15.87], mean: 12.06
  Created 13 candidate models for data size 1572
Current R2 threshold: -0.09999999999999998
  rf-tuned-l: R2 = 0.133 (std: 0.029)
  rf-tuned-xl: R2 = 0.133 (std: 0.025)
  gb-tuned-l: R2 = 0.153 (std: 0.036)
  gb-tuned-xl: R2 = 0.153 (std: 0.036)
  xgb-xl: R2 = -0.024 (std: 0.056)
  xgb-l: R2 = -0.024 (std: 0.056)
  mlp-adaptive-xl: R2 = 0.119 (std: 0.052)
  mlp-l: R2 = 0.128 (std: 0.052)
  svr-rbf-xl: R2 = 0.190 (std: 0.033)
  svr-poly-l: R2 = 0.190 (std: 0.033)
  knn-tuned-sqrt: R2 = 0.023 (std: 0.059)
  knn-tuned-l: R2 = 0.023 (std: 0.059)
  ridge: R2 = 0.035 (std: 0.053)

Model-based training with 13 models
Best R2: 0.190, Mean R2: 0.095
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.089 rf-tuned-xl:0.353 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.342 xgb-l:0.082 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000 knn-tuned-sqrt:0.057 knn-tuned-l:0.076 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9826, entropy=0.3753, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0996
  Round 1/3: Mean predicted reward = 11.982
    Using ridge regression weights
    Model weights: rf-tuned-l:0.089 rf-tuned-xl:0.353 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.342 xgb-l:0.082 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000 knn-tuned-sqrt:0.057 knn-tuned-l:0.076 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9857, entropy=0.3900, kl_div=0.0000
    Epoch 1: policy_loss=-0.0227, value_loss=0.9857, entropy=0.3852, kl_div=0.0027
  Round 2/3: Mean predicted reward = 11.977
    Using ridge regression weights
    Model weights: rf-tuned-l:0.089 rf-tuned-xl:0.353 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.342 xgb-l:0.082 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000 knn-tuned-sqrt:0.057 knn-tuned-l:0.076 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9891, entropy=0.3808, kl_div=0.0000
    Epoch 1: policy_loss=-0.0424, value_loss=0.9891, entropy=0.3769, kl_div=-0.0434
  Round 3/3: Mean predicted reward = 12.047

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 25 Results ---
  Mean Oracle Reward: 12.313
  Min Oracle Reward: 8.531
  Max Oracle Reward: 15.135
  Std Oracle Reward: 1.554
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.095, Max: 0.190, Count: 13
  Total Sequences Evaluated: 1650

======================================================================
EXPERIMENT ROUND 26/60
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1650
  Performance plateaued, reducing LR to 0.000136

--- Round 26 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TAGGGCACCTCGCGAG
  AGGCAGCCGTCCTGAG
  CACGGCTCGCGAAGTG
  ACGGGGAGCCTAGCTC
  TGCGGGCGAATGCCAC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.151
  Max reward: 16.437
  With intrinsic bonuses: 12.149

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9904, entropy=0.3677, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0625

=== Surrogate Model Training ===
Total samples: 1714

Training on 1630 samples (removed 84 outliers)
Reward range: [8.21, 15.71], mean: 12.06
  Created 13 candidate models for data size 1630
Current R2 threshold: -0.07999999999999999
  rf-tuned-l: R2 = 0.124 (std: 0.036)
  rf-tuned-xl: R2 = 0.123 (std: 0.031)
  gb-tuned-l: R2 = 0.140 (std: 0.036)
  gb-tuned-xl: R2 = 0.140 (std: 0.036)
  xgb-xl: R2 = -0.001 (std: 0.041)
  xgb-l: R2 = -0.001 (std: 0.041)
  mlp-adaptive-xl: R2 = 0.115 (std: 0.027)
  mlp-l: R2 = 0.128 (std: 0.028)
  svr-rbf-xl: R2 = 0.188 (std: 0.037)
  svr-poly-l: R2 = 0.188 (std: 0.037)
  knn-tuned-sqrt: R2 = 0.022 (std: 0.042)
  knn-tuned-l: R2 = 0.022 (std: 0.042)
  ridge: R2 = 0.031 (std: 0.039)

Model-based training with 13 models
Best R2: 0.188, Mean R2: 0.094
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.000 gb-tuned-xl:0.083 xgb-xl:0.222 xgb-l:0.000 mlp-adaptive-xl:0.240 mlp-l:0.000 svr-rbf-xl:0.189 svr-poly-l:0.075 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.192
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9836, entropy=0.3564, kl_div=0.0000
    Epoch 1: policy_loss=-0.0289, value_loss=0.9836, entropy=0.3530, kl_div=-0.0488
  Round 1/3: Mean predicted reward = 11.865
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.000 gb-tuned-xl:0.083 xgb-xl:0.222 xgb-l:0.000 mlp-adaptive-xl:0.240 mlp-l:0.000 svr-rbf-xl:0.189 svr-poly-l:0.075 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.192
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9879, entropy=0.3651, kl_div=0.0000
    Epoch 1: policy_loss=-0.0251, value_loss=0.9879, entropy=0.3619, kl_div=-0.0512
  Round 2/3: Mean predicted reward = 12.041
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.000 gb-tuned-l:0.000 gb-tuned-xl:0.083 xgb-xl:0.222 xgb-l:0.000 mlp-adaptive-xl:0.240 mlp-l:0.000 svr-rbf-xl:0.189 svr-poly-l:0.075 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.192
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9886, entropy=0.3610, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1958
  Round 3/3: Mean predicted reward = 12.107

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 26 Results ---
  Mean Oracle Reward: 12.160
  Min Oracle Reward: 6.469
  Max Oracle Reward: 16.407
  Std Oracle Reward: 1.828
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.094, Max: 0.188, Count: 13
  Total Sequences Evaluated: 1714

======================================================================
EXPERIMENT ROUND 27/60
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1714
  Performance plateaued, reducing LR to 0.000100

--- Round 27 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GACCGACCAGCGGTGT
  CACGTCGACGGGATGC
  TACGTGGACGCCGCAG
  GTCACGCCGAGGACGT
  GATCAGGTCCGGAGCC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.374
  Max reward: 15.590
  With intrinsic bonuses: 12.384

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9863, entropy=0.3519, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1531

=== Surrogate Model Training ===
Total samples: 1778

Training on 1694 samples (removed 84 outliers)
Reward range: [8.24, 15.87], mean: 12.08
  Created 13 candidate models for data size 1694
Current R2 threshold: -0.06
  rf-tuned-l: R2 = 0.120 (std: 0.040)
  rf-tuned-xl: R2 = 0.114 (std: 0.038)
  gb-tuned-l: R2 = 0.141 (std: 0.053)
  gb-tuned-xl: R2 = 0.141 (std: 0.053)
  xgb-xl: R2 = -0.026 (std: 0.048)
  xgb-l: R2 = -0.026 (std: 0.048)
  mlp-adaptive-xl: R2 = 0.092 (std: 0.050)
  mlp-l: R2 = 0.111 (std: 0.067)
  svr-rbf-xl: R2 = 0.188 (std: 0.052)
  svr-poly-l: R2 = 0.188 (std: 0.052)
  knn-tuned-sqrt: R2 = 0.008 (std: 0.048)
  knn-tuned-l: R2 = 0.008 (std: 0.048)
  ridge: R2 = 0.042 (std: 0.039)

Model-based training with 13 models
Best R2: 0.188, Mean R2: 0.085
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.276 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.167 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.086 svr-rbf-xl:0.074 svr-poly-l:0.282 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.115
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9814, entropy=0.3478, kl_div=0.0000
    Epoch 1: policy_loss=0.0033, value_loss=0.9815, entropy=0.3453, kl_div=0.0456
  Round 1/3: Mean predicted reward = 11.888
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.276 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.167 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.086 svr-rbf-xl:0.074 svr-poly-l:0.282 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.115
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9847, entropy=0.3348, kl_div=0.0000
    Epoch 1: policy_loss=-0.0290, value_loss=0.9847, entropy=0.3349, kl_div=-0.1581
  Round 2/3: Mean predicted reward = 11.895
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.276 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.167 xgb-l:0.000 mlp-adaptive-xl:0.000 mlp-l:0.086 svr-rbf-xl:0.074 svr-poly-l:0.282 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.115
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9897, entropy=0.3302, kl_div=0.0000
    Epoch 1: policy_loss=-0.0320, value_loss=0.9897, entropy=0.3280, kl_div=0.0293
  Round 3/3: Mean predicted reward = 12.224

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 27 Results ---
  Mean Oracle Reward: 12.382
  Min Oracle Reward: 8.214
  Max Oracle Reward: 15.495
  Std Oracle Reward: 1.480
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.085, Max: 0.188, Count: 13
  Total Sequences Evaluated: 1778

======================================================================
EXPERIMENT ROUND 28/60
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1778
  Performance plateaued, reducing LR to 0.000055

--- Round 28 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AGGTCTCGCGGCGAAC
  TTCGGGGACGCCGACA
  GCGTCCGTCGAGAGCA
  CTGACCACGACTGGGG
  CCGGTTGAAGGCCCAG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.104
  Max reward: 15.523
  With intrinsic bonuses: 12.091

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9884, entropy=0.3316, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0817

=== Surrogate Model Training ===
Total samples: 1842

Training on 1757 samples (removed 85 outliers)
Reward range: [8.24, 15.87], mean: 12.09
  Created 13 candidate models for data size 1757
Current R2 threshold: -0.03999999999999998
  rf-tuned-l: R2 = 0.121 (std: 0.061)
  rf-tuned-xl: R2 = 0.123 (std: 0.057)
  gb-tuned-l: R2 = 0.152 (std: 0.066)
  gb-tuned-xl: R2 = 0.152 (std: 0.066)
  xgb-xl: R2 = 0.005 (std: 0.096)
  xgb-l: R2 = 0.005 (std: 0.096)
  mlp-adaptive-xl: R2 = 0.096 (std: 0.091)
  mlp-l: R2 = 0.140 (std: 0.042)
  svr-rbf-xl: R2 = 0.197 (std: 0.060)
  svr-poly-l: R2 = 0.197 (std: 0.060)
  knn-tuned-sqrt: R2 = 0.010 (std: 0.050)
  knn-tuned-l: R2 = 0.010 (std: 0.050)
  ridge: R2 = 0.047 (std: 0.049)

Model-based training with 13 models
Best R2: 0.197, Mean R2: 0.097
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.054 rf-tuned-xl:0.097 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.000 xgb-l:0.210 mlp-adaptive-xl:0.108 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.344 knn-tuned-sqrt:0.034 knn-tuned-l:0.153 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9839, entropy=0.3199, kl_div=0.0000
    Epoch 1: policy_loss=-0.0122, value_loss=0.9839, entropy=0.3186, kl_div=0.0108
  Round 1/3: Mean predicted reward = 11.790
    Using ridge regression weights
    Model weights: rf-tuned-l:0.054 rf-tuned-xl:0.097 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.000 xgb-l:0.210 mlp-adaptive-xl:0.108 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.344 knn-tuned-sqrt:0.034 knn-tuned-l:0.153 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9853, entropy=0.3334, kl_div=0.0000
    Epoch 1: policy_loss=-0.0320, value_loss=0.9853, entropy=0.3330, kl_div=-0.0985
  Round 2/3: Mean predicted reward = 11.873
    Using ridge regression weights
    Model weights: rf-tuned-l:0.054 rf-tuned-xl:0.097 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.000 xgb-l:0.210 mlp-adaptive-xl:0.108 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.344 knn-tuned-sqrt:0.034 knn-tuned-l:0.153 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9815, entropy=0.3425, kl_div=0.0000
    Epoch 1: policy_loss=-0.0159, value_loss=0.9815, entropy=0.3420, kl_div=-0.0776
  Round 3/3: Mean predicted reward = 12.167

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 28 Results ---
  Mean Oracle Reward: 12.082
  Min Oracle Reward: 7.739
  Max Oracle Reward: 15.737
  Std Oracle Reward: 1.610
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.097, Max: 0.197, Count: 13
  Total Sequences Evaluated: 1842

======================================================================
EXPERIMENT ROUND 29/60
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1842

--- Round 29 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  GCCTCGGGAGCATGCA
  TGCCGGCGAACGGATC
  CCACGTCAAGGGCGTG
  GTACGCGAGCGACGCT
  GGCTCTGGGCACGAAC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.312
  Max reward: 16.488
  With intrinsic bonuses: 12.313

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9841, entropy=0.3314, kl_div=0.0000
    Epoch 1: policy_loss=-0.0122, value_loss=0.9841, entropy=0.3313, kl_div=-0.0257

=== Surrogate Model Training ===
Total samples: 1906

Training on 1818 samples (removed 88 outliers)
Reward range: [8.21, 15.89], mean: 12.09
  Created 13 candidate models for data size 1818
Current R2 threshold: -0.019999999999999962
  rf-tuned-l: R2 = 0.144 (std: 0.058)
  rf-tuned-xl: R2 = 0.142 (std: 0.050)
  gb-tuned-l: R2 = 0.161 (std: 0.058)
  gb-tuned-xl: R2 = 0.161 (std: 0.058)
  xgb-xl: R2 = 0.033 (std: 0.083)
  xgb-l: R2 = 0.033 (std: 0.083)
  mlp-adaptive-xl: R2 = 0.154 (std: 0.066)
  mlp-l: R2 = 0.139 (std: 0.051)
  svr-rbf-xl: R2 = 0.202 (std: 0.057)
  svr-poly-l: R2 = 0.202 (std: 0.057)
  knn-tuned-sqrt: R2 = 0.035 (std: 0.064)
  knn-tuned-l: R2 = 0.035 (std: 0.064)
  ridge: R2 = 0.051 (std: 0.053)

Model-based training with 13 models
Best R2: 0.202, Mean R2: 0.115
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.027 gb-tuned-l:0.182 gb-tuned-xl:0.049 xgb-xl:0.133 xgb-l:0.000 mlp-adaptive-xl:0.281 mlp-l:0.000 svr-rbf-xl:0.055 svr-poly-l:0.146 knn-tuned-sqrt:0.028 knn-tuned-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9833, entropy=0.3276, kl_div=0.0000
    Epoch 1: policy_loss=-0.0260, value_loss=0.9833, entropy=0.3275, kl_div=-0.0322
  Round 1/3: Mean predicted reward = 11.694
    Using ridge regression weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.027 gb-tuned-l:0.182 gb-tuned-xl:0.049 xgb-xl:0.133 xgb-l:0.000 mlp-adaptive-xl:0.281 mlp-l:0.000 svr-rbf-xl:0.055 svr-poly-l:0.146 knn-tuned-sqrt:0.028 knn-tuned-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9853, entropy=0.3294, kl_div=0.0000
    Epoch 1: policy_loss=-0.0121, value_loss=0.9853, entropy=0.3299, kl_div=-0.0892
  Round 2/3: Mean predicted reward = 11.973
    Using ridge regression weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.027 gb-tuned-l:0.182 gb-tuned-xl:0.049 xgb-xl:0.133 xgb-l:0.000 mlp-adaptive-xl:0.281 mlp-l:0.000 svr-rbf-xl:0.055 svr-poly-l:0.146 knn-tuned-sqrt:0.028 knn-tuned-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9871, entropy=0.3239, kl_div=0.0000
    Epoch 1: policy_loss=-0.0037, value_loss=0.9871, entropy=0.3237, kl_div=-0.0380
  Round 3/3: Mean predicted reward = 12.223

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 29 Results ---
  Mean Oracle Reward: 12.316
  Min Oracle Reward: 1.758
  Max Oracle Reward: 16.372
  Std Oracle Reward: 2.212
  Sequence Diversity: 0.984
  Models Used: 13
  Model R2 - Mean: 0.115, Max: 0.202, Count: 13
  Total Sequences Evaluated: 1906

======================================================================
EXPERIMENT ROUND 30/60
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1906

--- Round 30 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTTCACGAGCCGGCGA
  TCCAACCGGGGTAGCG
  AACCGCGGGCTTAGCG
  TGACCCAGCGAGGTCG
  CCCTGGAGACTGAGGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.396
  Max reward: 15.753
  With intrinsic bonuses: 12.360

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9913, entropy=0.3131, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1084

=== Surrogate Model Training ===
Total samples: 1970

Training on 1879 samples (removed 91 outliers)
Reward range: [8.24, 15.89], mean: 12.11
  Created 13 candidate models for data size 1879
Current R2 threshold: 0.0
  rf-tuned-l: R2 = 0.122 (std: 0.063)
  rf-tuned-xl: R2 = 0.126 (std: 0.066)
  gb-tuned-l: R2 = 0.166 (std: 0.073)
  gb-tuned-xl: R2 = 0.166 (std: 0.073)
  xgb-xl: R2 = 0.048 (std: 0.081)
  xgb-l: R2 = 0.048 (std: 0.081)
  mlp-adaptive-xl: R2 = 0.141 (std: 0.066)
  mlp-l: R2 = 0.140 (std: 0.074)
  svr-rbf-xl: R2 = 0.193 (std: 0.079)
  svr-poly-l: R2 = 0.193 (std: 0.079)
  knn-tuned-sqrt: R2 = 0.015 (std: 0.091)
  knn-tuned-l: R2 = 0.015 (std: 0.091)
  ridge: R2 = 0.058 (std: 0.058)

Model-based training with 13 models
Best R2: 0.193, Mean R2: 0.110
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.061 rf-tuned-xl:0.150 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.076 xgb-l:0.255 mlp-adaptive-xl:0.000 mlp-l:0.028 svr-rbf-xl:0.310 svr-poly-l:0.000 knn-tuned-sqrt:0.000 knn-tuned-l:0.120 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9844, entropy=0.3240, kl_div=0.0000
    Epoch 1: policy_loss=-0.0497, value_loss=0.9844, entropy=0.3212, kl_div=-0.3311
  Round 1/3: Mean predicted reward = 11.615
    Using ridge regression weights
    Model weights: rf-tuned-l:0.061 rf-tuned-xl:0.150 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.076 xgb-l:0.255 mlp-adaptive-xl:0.000 mlp-l:0.028 svr-rbf-xl:0.310 svr-poly-l:0.000 knn-tuned-sqrt:0.000 knn-tuned-l:0.120 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9839, entropy=0.3022, kl_div=0.0000
    Epoch 1: policy_loss=0.0129, value_loss=0.9839, entropy=0.3001, kl_div=-0.2901
  Round 2/3: Mean predicted reward = 11.740
    Using ridge regression weights
    Model weights: rf-tuned-l:0.061 rf-tuned-xl:0.150 gb-tuned-l:0.000 gb-tuned-xl:0.000 xgb-xl:0.076 xgb-l:0.255 mlp-adaptive-xl:0.000 mlp-l:0.028 svr-rbf-xl:0.310 svr-poly-l:0.000 knn-tuned-sqrt:0.000 knn-tuned-l:0.120 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9896, entropy=0.3018, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1700
  Round 3/3: Mean predicted reward = 11.996

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 30 Results ---
  Mean Oracle Reward: 12.359
  Min Oracle Reward: 7.642
  Max Oracle Reward: 15.658
  Std Oracle Reward: 1.534
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.110, Max: 0.193, Count: 13
  Total Sequences Evaluated: 1970

======================================================================
EXPERIMENT ROUND 31/60
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1970
  Consistent improvement, increasing LR to 0.000327

--- Round 31 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  TCACCGAGCCGGGGAT
  GAGGGCCTAATCGCGC
  GCGGTGGCATACAGCC
  TACTGAGCACGGCGCG
  AGGGTCGCCAGTCCTA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.175
  Max reward: 16.715
  With intrinsic bonuses: 12.170

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9932, entropy=0.2863, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3454

=== Surrogate Model Training ===
Total samples: 2034

Training on 1945 samples (removed 89 outliers)
Reward range: [8.16, 15.90], mean: 12.11
  Created 13 candidate models for data size 1945
Current R2 threshold: 0.020000000000000018
  rf-tuned-l: R2 = 0.131 (std: 0.071)
  rf-tuned-xl: R2 = 0.128 (std: 0.067)
  gb-tuned-l: R2 = 0.166 (std: 0.080)
  gb-tuned-xl: R2 = 0.166 (std: 0.080)
  xgb-xl: R2 = 0.053 (std: 0.073)
  xgb-l: R2 = 0.053 (std: 0.073)
  mlp-adaptive-xl: R2 = 0.133 (std: 0.079)
  mlp-l: R2 = 0.160 (std: 0.065)
  svr-rbf-xl: R2 = 0.200 (std: 0.071)
  svr-poly-l: R2 = 0.200 (std: 0.071)
  knn-tuned-sqrt: R2 = 0.027 (std: 0.076)
  knn-tuned-l: R2 = 0.027 (std: 0.076)
  ridge: R2 = 0.059 (std: 0.067)

Model-based training with 13 models
Best R2: 0.200, Mean R2: 0.115
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.073 rf-tuned-xl:0.289 gb-tuned-l:0.206 gb-tuned-xl:0.081 xgb-xl:0.107 xgb-l:0.000 mlp-adaptive-xl:0.015 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.228 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9816, entropy=0.2997, kl_div=0.0000
    Epoch 1: policy_loss=-0.0316, value_loss=0.9816, entropy=0.2971, kl_div=-0.1350
  Round 1/3: Mean predicted reward = 11.702
    Using ridge regression weights
    Model weights: rf-tuned-l:0.073 rf-tuned-xl:0.289 gb-tuned-l:0.206 gb-tuned-xl:0.081 xgb-xl:0.107 xgb-l:0.000 mlp-adaptive-xl:0.015 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.228 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9848, entropy=0.3039, kl_div=0.0000
    Epoch 1: policy_loss=0.2406, value_loss=0.9848, entropy=0.3061, kl_div=-0.6847
  Round 2/3: Mean predicted reward = 11.889
    Using ridge regression weights
    Model weights: rf-tuned-l:0.073 rf-tuned-xl:0.289 gb-tuned-l:0.206 gb-tuned-xl:0.081 xgb-xl:0.107 xgb-l:0.000 mlp-adaptive-xl:0.015 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.228 knn-tuned-sqrt:0.000 knn-tuned-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9870, entropy=0.2956, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1083
  Round 3/3: Mean predicted reward = 12.168

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 31 Results ---
  Mean Oracle Reward: 12.167
  Min Oracle Reward: 5.672
  Max Oracle Reward: 16.807
  Std Oracle Reward: 2.125
  Sequence Diversity: 0.984
  Models Used: 13
  Model R2 - Mean: 0.115, Max: 0.200, Count: 13
  Total Sequences Evaluated: 2034

======================================================================
EXPERIMENT ROUND 32/60
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2034
  Performance plateaued, reducing LR to 0.000100

--- Round 32 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AACCGTCACTGCGGGG
  GTGGCGCGACATCGCA
  TGTCGCGAAGCCCGGA
  GGATCGTCCAGCGGAC
  CAGCGCGGAACGTGTC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.573
  Max reward: 16.890
  With intrinsic bonuses: 12.545

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9903, entropy=0.2909, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1278

=== Surrogate Model Training ===
Total samples: 2098

Training on 2006 samples (removed 92 outliers)
Reward range: [8.15, 15.90], mean: 12.11
  Created 13 candidate models for data size 2006
Current R2 threshold: 0.040000000000000036
  rf-tuned-l: R2 = 0.146 (std: 0.070)
  rf-tuned-xl: R2 = 0.157 (std: 0.070)
  gb-tuned-l: R2 = 0.179 (std: 0.065)
  gb-tuned-xl: R2 = 0.179 (std: 0.065)
  xgb-xl: R2 = 0.071 (std: 0.084)
  xgb-l: R2 = 0.071 (std: 0.084)
  mlp-adaptive-xl: R2 = 0.115 (std: 0.080)
  mlp-l: R2 = 0.167 (std: 0.060)
  svr-rbf-xl: R2 = 0.209 (std: 0.066)
  svr-poly-l: R2 = 0.209 (std: 0.066)
  knn-tuned-sqrt: R2 = 0.031 (std: 0.074)
  knn-tuned-l: R2 = 0.031 (std: 0.074)
  ridge: R2 = 0.068 (std: 0.068)

Model-based training with 11 models
Best R2: 0.209, Mean R2: 0.126
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.052 rf-tuned-xl:0.398 gb-tuned-l:0.193 gb-tuned-xl:0.000 xgb-xl:0.322 xgb-l:0.000 mlp-adaptive-xl:0.036 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9837, entropy=0.2899, kl_div=0.0000
    Epoch 1: policy_loss=-0.0311, value_loss=0.9837, entropy=0.2891, kl_div=-0.0182
  Round 1/3: Mean predicted reward = 11.757
    Using ridge regression weights
    Model weights: rf-tuned-l:0.052 rf-tuned-xl:0.398 gb-tuned-l:0.193 gb-tuned-xl:0.000 xgb-xl:0.322 xgb-l:0.000 mlp-adaptive-xl:0.036 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9859, entropy=0.2936, kl_div=0.0000
    Epoch 1: policy_loss=0.0004, value_loss=0.9859, entropy=0.2941, kl_div=-0.2488
  Round 2/3: Mean predicted reward = 11.962
    Using ridge regression weights
    Model weights: rf-tuned-l:0.052 rf-tuned-xl:0.398 gb-tuned-l:0.193 gb-tuned-xl:0.000 xgb-xl:0.322 xgb-l:0.000 mlp-adaptive-xl:0.036 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9879, entropy=0.2973, kl_div=0.0000
    Epoch 1: policy_loss=-0.0210, value_loss=0.9879, entropy=0.2964, kl_div=0.0161
  Round 3/3: Mean predicted reward = 12.038

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 32 Results ---
  Mean Oracle Reward: 12.503
  Min Oracle Reward: 8.007
  Max Oracle Reward: 16.833
  Std Oracle Reward: 1.940
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: 0.126, Max: 0.209, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 2098

======================================================================
EXPERIMENT ROUND 33/60
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2098

--- Round 33 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  TAAGCCGCCTCGGAGG
  AGCTGAACTCAGCGTG
  GACGGCTCGGCGACAT
  GGCGGCACCGCTAGTA
  GGCCCGCAAAGGTTGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.797
  Max reward: 16.911
  With intrinsic bonuses: 12.794

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9890, entropy=0.2941, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2754

=== Surrogate Model Training ===
Total samples: 2162

Training on 2064 samples (removed 98 outliers)
Reward range: [8.15, 16.02], mean: 12.13
  Created 13 candidate models for data size 2064
Current R2 threshold: 0.06
  rf-tuned-l: R2 = 0.148 (std: 0.070)
  rf-tuned-xl: R2 = 0.142 (std: 0.073)
  gb-tuned-l: R2 = 0.182 (std: 0.072)
  gb-tuned-xl: R2 = 0.182 (std: 0.072)
  xgb-xl: R2 = 0.040 (std: 0.096)
  xgb-l: R2 = 0.040 (std: 0.096)
  mlp-adaptive-xl: R2 = 0.155 (std: 0.050)
  mlp-l: R2 = 0.161 (std: 0.089)
  svr-rbf-xl: R2 = 0.210 (std: 0.065)
  svr-poly-l: R2 = 0.210 (std: 0.065)
  knn-tuned-sqrt: R2 = 0.036 (std: 0.085)
  knn-tuned-l: R2 = 0.036 (std: 0.085)
  ridge: R2 = 0.073 (std: 0.068)

Model-based training with 9 models
Best R2: 0.210, Mean R2: 0.124
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.558 gb-tuned-l:0.060 gb-tuned-xl:0.166 mlp-adaptive-xl:0.060 mlp-l:0.000 svr-rbf-xl:0.156 svr-poly-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9815, entropy=0.2839, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0914
  Round 1/3: Mean predicted reward = 11.683
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.558 gb-tuned-l:0.060 gb-tuned-xl:0.166 mlp-adaptive-xl:0.060 mlp-l:0.000 svr-rbf-xl:0.156 svr-poly-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9843, entropy=0.2742, kl_div=0.0000
    Epoch 1: policy_loss=-0.0250, value_loss=0.9843, entropy=0.2739, kl_div=-0.0440
  Round 2/3: Mean predicted reward = 11.757
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.558 gb-tuned-l:0.060 gb-tuned-xl:0.166 mlp-adaptive-xl:0.060 mlp-l:0.000 svr-rbf-xl:0.156 svr-poly-l:0.000 ridge:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9869, entropy=0.2951, kl_div=0.0000
    Epoch 1: policy_loss=-0.0173, value_loss=0.9869, entropy=0.2948, kl_div=-0.0512
  Round 3/3: Mean predicted reward = 12.138

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 33 Results ---
  Mean Oracle Reward: 12.855
  Min Oracle Reward: 7.281
  Max Oracle Reward: 16.826
  Std Oracle Reward: 2.000
  Sequence Diversity: 0.984
  Models Used: 9
  Model R2 - Mean: 0.124, Max: 0.210, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 2162

======================================================================
EXPERIMENT ROUND 34/60
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2162
  Consistent improvement, increasing LR to 0.000045

--- Round 34 Configuration ---
Learning rate: 0.000045
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  CCGCGACGGGTATACG
  GAGGAAGCCGTCGCCT
  GATGGCGGCTCCCAGA
  GCATAGCGTCGAGCCG
  CGTACTGGAGGACTCC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.354
  Max reward: 15.838
  With intrinsic bonuses: 12.386

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9903, entropy=0.2910, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0844

=== Surrogate Model Training ===
Total samples: 2226

Training on 2127 samples (removed 99 outliers)
Reward range: [8.15, 16.08], mean: 12.14
  Created 13 candidate models for data size 2127
Current R2 threshold: 0.08000000000000002
  rf-tuned-l: R2 = 0.151 (std: 0.083)
  rf-tuned-xl: R2 = 0.149 (std: 0.082)
  gb-tuned-l: R2 = 0.186 (std: 0.088)
  gb-tuned-xl: R2 = 0.186 (std: 0.088)
  xgb-xl: R2 = 0.056 (std: 0.111)
  xgb-l: R2 = 0.056 (std: 0.111)
  mlp-adaptive-xl: R2 = 0.152 (std: 0.094)
  mlp-l: R2 = 0.142 (std: 0.101)
  svr-rbf-xl: R2 = 0.214 (std: 0.086)
  svr-poly-l: R2 = 0.214 (std: 0.086)
  knn-tuned-sqrt: R2 = 0.031 (std: 0.107)
  knn-tuned-l: R2 = 0.031 (std: 0.107)
  ridge: R2 = 0.075 (std: 0.080)

Model-based training with 8 models
Best R2: 0.214, Mean R2: 0.126
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.299 gb-tuned-l:0.000 gb-tuned-xl:0.160 mlp-adaptive-xl:0.367 mlp-l:0.042 svr-rbf-xl:0.000 svr-poly-l:0.132
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9827, entropy=0.2810, kl_div=0.0000
    Epoch 1: policy_loss=0.0026, value_loss=0.9827, entropy=0.2808, kl_div=0.0149
  Round 1/3: Mean predicted reward = 11.670
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.299 gb-tuned-l:0.000 gb-tuned-xl:0.160 mlp-adaptive-xl:0.367 mlp-l:0.042 svr-rbf-xl:0.000 svr-poly-l:0.132
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9853, entropy=0.2794, kl_div=0.0000
    Epoch 1: policy_loss=-0.0426, value_loss=0.9853, entropy=0.2796, kl_div=-0.0948
  Round 2/3: Mean predicted reward = 11.808
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.299 gb-tuned-l:0.000 gb-tuned-xl:0.160 mlp-adaptive-xl:0.367 mlp-l:0.042 svr-rbf-xl:0.000 svr-poly-l:0.132
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9893, entropy=0.2832, kl_div=0.0000
    Epoch 1: policy_loss=0.0060, value_loss=0.9893, entropy=0.2832, kl_div=-0.0746
  Round 3/3: Mean predicted reward = 12.026

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 34 Results ---
  Mean Oracle Reward: 12.370
  Min Oracle Reward: 5.362
  Max Oracle Reward: 15.912
  Std Oracle Reward: 2.115
  Sequence Diversity: 0.984
  Models Used: 8
  Model R2 - Mean: 0.126, Max: 0.214, Count: 13
  Total Sequences Evaluated: 2226

======================================================================
EXPERIMENT ROUND 35/60
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2226

--- Round 35 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AGTCCGTGGACCCAGG
  AGGGAGGCACCTGCCT
  ACTTCCCGCGGGGTAA
  GAATGGGAGCCCCTCG
  GCAAGCCGGTACCTGG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.416
  Max reward: 16.860
  With intrinsic bonuses: 12.419

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9870, entropy=0.2758, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2514

=== Surrogate Model Training ===
Total samples: 2290

Training on 2186 samples (removed 104 outliers)
Reward range: [8.15, 16.10], mean: 12.15
  Created 13 candidate models for data size 2186
Current R2 threshold: 0.10000000000000003
  rf-tuned-l: R2 = 0.171 (std: 0.074)
  rf-tuned-xl: R2 = 0.170 (std: 0.071)
  gb-tuned-l: R2 = 0.194 (std: 0.072)
  gb-tuned-xl: R2 = 0.194 (std: 0.072)
  xgb-xl: R2 = 0.063 (std: 0.088)
  xgb-l: R2 = 0.063 (std: 0.088)
  mlp-adaptive-xl: R2 = 0.162 (std: 0.072)
  mlp-l: R2 = 0.173 (std: 0.079)
  svr-rbf-xl: R2 = 0.217 (std: 0.066)
  svr-poly-l: R2 = 0.217 (std: 0.066)
  knn-tuned-sqrt: R2 = 0.044 (std: 0.098)
  knn-tuned-l: R2 = 0.044 (std: 0.098)
  ridge: R2 = 0.082 (std: 0.074)

Model-based training with 8 models
Best R2: 0.217, Mean R2: 0.138
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.474 gb-tuned-l:0.195 gb-tuned-xl:0.214 mlp-adaptive-xl:0.062 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.055
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9814, entropy=0.2823, kl_div=0.0000
    Epoch 1: policy_loss=-0.0638, value_loss=0.9814, entropy=0.2810, kl_div=-0.1911
  Round 1/3: Mean predicted reward = 11.676
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.474 gb-tuned-l:0.195 gb-tuned-xl:0.214 mlp-adaptive-xl:0.062 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.055
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9824, entropy=0.2796, kl_div=0.0000
    Epoch 1: policy_loss=0.0294, value_loss=0.9824, entropy=0.2790, kl_div=-0.3248
  Round 2/3: Mean predicted reward = 11.812
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.474 gb-tuned-l:0.195 gb-tuned-xl:0.214 mlp-adaptive-xl:0.062 mlp-l:0.000 svr-rbf-xl:0.000 svr-poly-l:0.055
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9855, entropy=0.2732, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4714
  Round 3/3: Mean predicted reward = 12.259

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 35 Results ---
  Mean Oracle Reward: 12.436
  Min Oracle Reward: 4.351
  Max Oracle Reward: 17.025
  Std Oracle Reward: 2.151
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: 0.138, Max: 0.217, Count: 13
  Total Sequences Evaluated: 2290

======================================================================
EXPERIMENT ROUND 36/60
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2290

--- Round 36 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGCGCCAGAATGGCCT
  GACCGATCGTCGCGAG
  AGGCGGCATTCCAGCG
  ATGGGACGCACCGGTC
  GCTGGCCGTAGCAAGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 13.070
  Max reward: 16.932
  With intrinsic bonuses: 13.030

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9897, entropy=0.2695, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7425

=== Surrogate Model Training ===
Total samples: 2354

Training on 2246 samples (removed 108 outliers)
Reward range: [8.09, 16.15], mean: 12.16
  Created 13 candidate models for data size 2246
Current R2 threshold: 0.12
  rf-tuned-l: R2 = 0.185 (std: 0.067)
  rf-tuned-xl: R2 = 0.177 (std: 0.076)
  gb-tuned-l: R2 = 0.200 (std: 0.070)
  gb-tuned-xl: R2 = 0.200 (std: 0.070)
  xgb-xl: R2 = 0.087 (std: 0.103)
  xgb-l: R2 = 0.087 (std: 0.103)
  mlp-adaptive-xl: R2 = 0.187 (std: 0.083)
  mlp-l: R2 = 0.182 (std: 0.070)
  svr-rbf-xl: R2 = 0.225 (std: 0.064)
  svr-poly-l: R2 = 0.225 (std: 0.064)
  knn-tuned-sqrt: R2 = 0.048 (std: 0.109)
  knn-tuned-l: R2 = 0.048 (std: 0.109)
  ridge: R2 = 0.083 (std: 0.075)

Model-based training with 8 models
Best R2: 0.225, Mean R2: 0.149
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.711 gb-tuned-l:0.000 gb-tuned-xl:0.035 mlp-adaptive-xl:0.051 mlp-l:0.000 svr-rbf-xl:0.202 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9842, entropy=0.2774, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2329
  Round 1/3: Mean predicted reward = 11.564
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.711 gb-tuned-l:0.000 gb-tuned-xl:0.035 mlp-adaptive-xl:0.051 mlp-l:0.000 svr-rbf-xl:0.202 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9852, entropy=0.2677, kl_div=0.0000
    Epoch 1: policy_loss=-0.0122, value_loss=0.9852, entropy=0.2674, kl_div=-0.2253
  Round 2/3: Mean predicted reward = 11.968
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.711 gb-tuned-l:0.000 gb-tuned-xl:0.035 mlp-adaptive-xl:0.051 mlp-l:0.000 svr-rbf-xl:0.202 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9874, entropy=0.2713, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3138
  Round 3/3: Mean predicted reward = 12.276

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 36 Results ---
  Mean Oracle Reward: 13.074
  Min Oracle Reward: 9.038
  Max Oracle Reward: 16.760
  Std Oracle Reward: 2.073
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: 0.149, Max: 0.225, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 2354

======================================================================
EXPERIMENT ROUND 37/60
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2354
  Consistent improvement, increasing LR to 0.000240

--- Round 37 Configuration ---
Learning rate: 0.000240
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGGTCACTGGCGAGAC
  CCCGATGGACGGCTAG
  AGCTCAGGGCGGCTAC
  GGACGCGACTTCCGAG
  GGTCAGCGTCCGGACA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.746
  Max reward: 18.732
  With intrinsic bonuses: 12.785

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9912, entropy=0.2613, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5661

=== Surrogate Model Training ===
Total samples: 2418

Training on 2303 samples (removed 115 outliers)
Reward range: [8.15, 16.15], mean: 12.17
  Created 13 candidate models for data size 2303
Current R2 threshold: 0.14
  rf-tuned-l: R2 = 0.181 (std: 0.070)
  rf-tuned-xl: R2 = 0.177 (std: 0.073)
  gb-tuned-l: R2 = 0.192 (std: 0.071)
  gb-tuned-xl: R2 = 0.192 (std: 0.071)
  xgb-xl: R2 = 0.073 (std: 0.100)
  xgb-l: R2 = 0.073 (std: 0.100)
  mlp-adaptive-xl: R2 = 0.199 (std: 0.074)
  mlp-l: R2 = 0.171 (std: 0.087)
  svr-rbf-xl: R2 = 0.228 (std: 0.070)
  svr-poly-l: R2 = 0.228 (std: 0.070)
  knn-tuned-sqrt: R2 = 0.042 (std: 0.099)
  knn-tuned-l: R2 = 0.042 (std: 0.099)
  ridge: R2 = 0.080 (std: 0.084)

Model-based training with 8 models
Best R2: 0.228, Mean R2: 0.145
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.645 gb-tuned-l:0.082 gb-tuned-xl:0.193 mlp-adaptive-xl:0.000 mlp-l:0.071 svr-rbf-xl:0.010 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9811, entropy=0.2595, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1057
  Round 1/3: Mean predicted reward = 11.545
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.645 gb-tuned-l:0.082 gb-tuned-xl:0.193 mlp-adaptive-xl:0.000 mlp-l:0.071 svr-rbf-xl:0.010 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9864, entropy=0.2400, kl_div=0.0000
    Epoch 1: policy_loss=-0.0145, value_loss=0.9864, entropy=0.2398, kl_div=-0.2145
  Round 2/3: Mean predicted reward = 11.789
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.645 gb-tuned-l:0.082 gb-tuned-xl:0.193 mlp-adaptive-xl:0.000 mlp-l:0.071 svr-rbf-xl:0.010 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9862, entropy=0.2447, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4365
  Round 3/3: Mean predicted reward = 12.185

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 37 Results ---
  Mean Oracle Reward: 12.758
  Min Oracle Reward: 6.843
  Max Oracle Reward: 18.637
  Std Oracle Reward: 2.119
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: 0.145, Max: 0.228, Count: 13
  Total Sequences Evaluated: 2418

======================================================================
EXPERIMENT ROUND 38/60
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2418

--- Round 38 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  ACCGCGCTCTGGATGA
  GGAATGCCCCGGCATG
  CATGCCGGAGCGAGCT
  CGGCGTGCCAAAGCGT
  TGGCGCGGCTACAACG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.904
  Max reward: 18.596
  With intrinsic bonuses: 12.832

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9892, entropy=0.2444, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3112

=== Surrogate Model Training ===
Total samples: 2482

Training on 2359 samples (removed 123 outliers)
Reward range: [8.15, 16.15], mean: 12.18
  Created 13 candidate models for data size 2359
Current R2 threshold: 0.16000000000000003
  rf-tuned-l: R2 = 0.170 (std: 0.077)
  rf-tuned-xl: R2 = 0.178 (std: 0.083)
  gb-tuned-l: R2 = 0.196 (std: 0.072)
  gb-tuned-xl: R2 = 0.196 (std: 0.072)
  xgb-xl: R2 = 0.070 (std: 0.099)
  xgb-l: R2 = 0.070 (std: 0.099)
  mlp-adaptive-xl: R2 = 0.190 (std: 0.084)
  mlp-l: R2 = 0.185 (std: 0.084)
  svr-rbf-xl: R2 = 0.225 (std: 0.072)
  svr-poly-l: R2 = 0.225 (std: 0.072)
  knn-tuned-sqrt: R2 = 0.040 (std: 0.111)
  knn-tuned-l: R2 = 0.040 (std: 0.111)
  ridge: R2 = 0.082 (std: 0.090)

Model-based training with 8 models
Best R2: 0.225, Mean R2: 0.144
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.505 gb-tuned-l:0.099 gb-tuned-xl:0.206 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.181 svr-poly-l:0.009
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9810, entropy=0.2588, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0899
  Round 1/3: Mean predicted reward = 11.745
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.505 gb-tuned-l:0.099 gb-tuned-xl:0.206 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.181 svr-poly-l:0.009
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9864, entropy=0.2467, kl_div=0.0000
    Epoch 1: policy_loss=-0.0401, value_loss=0.9864, entropy=0.2463, kl_div=-0.0883
  Round 2/3: Mean predicted reward = 11.809
    Using ridge regression weights
    Model weights: rf-tuned-l:0.000 rf-tuned-xl:0.505 gb-tuned-l:0.099 gb-tuned-xl:0.206 mlp-adaptive-xl:0.000 mlp-l:0.000 svr-rbf-xl:0.181 svr-poly-l:0.009
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9877, entropy=0.2392, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2007
  Round 3/3: Mean predicted reward = 12.190

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 38 Results ---
  Mean Oracle Reward: 12.876
  Min Oracle Reward: 5.967
  Max Oracle Reward: 18.960
  Std Oracle Reward: 2.144
  Sequence Diversity: 0.984
  Models Used: 8
  Model R2 - Mean: 0.144, Max: 0.225, Count: 13
  Total Sequences Evaluated: 2482

======================================================================
EXPERIMENT ROUND 39/60
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2482

--- Round 39 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTCAGGGGCGTGCAAC
  GCCCGCAAGTGAGGTC
  CCACTGGTGGGCCAAG
  TGGTCAGGCCACCAGG
  GGCAGCACCTAGGTCG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.646
  Max reward: 18.525
  With intrinsic bonuses: 12.668

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9905, entropy=0.2402, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1043

=== Surrogate Model Training ===
Total samples: 2546

Training on 2416 samples (removed 130 outliers)
Reward range: [8.15, 16.25], mean: 12.19
  Created 13 candidate models for data size 2416
Current R2 threshold: 0.18
  rf-tuned-l: R2 = 0.177 (std: 0.069)
  rf-tuned-xl: R2 = 0.173 (std: 0.070)
  gb-tuned-l: R2 = 0.192 (std: 0.073)
  gb-tuned-xl: R2 = 0.192 (std: 0.073)
  xgb-xl: R2 = 0.091 (std: 0.071)
  xgb-l: R2 = 0.091 (std: 0.071)
  mlp-adaptive-xl: R2 = 0.193 (std: 0.088)
  mlp-l: R2 = 0.169 (std: 0.076)
  svr-rbf-xl: R2 = 0.230 (std: 0.066)
  svr-poly-l: R2 = 0.230 (std: 0.066)
  knn-tuned-sqrt: R2 = 0.055 (std: 0.122)
  knn-tuned-l: R2 = 0.055 (std: 0.122)
  ridge: R2 = 0.087 (std: 0.090)

Model-based training with 5 models
Best R2: 0.230, Mean R2: 0.149
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: gb-tuned-l:0.098 gb-tuned-xl:0.309 mlp-adaptive-xl:0.000 svr-rbf-xl:0.593 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9813, entropy=0.2429, kl_div=0.0000
    Epoch 1: policy_loss=0.0128, value_loss=0.9813, entropy=0.2426, kl_div=0.0337
  Round 1/3: Mean predicted reward = 11.366
    Using ridge regression weights
    Model weights: gb-tuned-l:0.098 gb-tuned-xl:0.309 mlp-adaptive-xl:0.000 svr-rbf-xl:0.593 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9832, entropy=0.2475, kl_div=0.0000
    Epoch 1: policy_loss=-0.0517, value_loss=0.9833, entropy=0.2476, kl_div=-0.0888
  Round 2/3: Mean predicted reward = 11.817
    Using ridge regression weights
    Model weights: gb-tuned-l:0.098 gb-tuned-xl:0.309 mlp-adaptive-xl:0.000 svr-rbf-xl:0.593 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9863, entropy=0.2433, kl_div=0.0000
    Epoch 1: policy_loss=0.0003, value_loss=0.9863, entropy=0.2434, kl_div=-0.0774
  Round 3/3: Mean predicted reward = 12.127

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 39 Results ---
  Mean Oracle Reward: 12.683
  Min Oracle Reward: 6.588
  Max Oracle Reward: 18.585
  Std Oracle Reward: 2.331
  Sequence Diversity: 1.000
  Models Used: 5
  Model R2 - Mean: 0.149, Max: 0.230, Count: 13
  Total Sequences Evaluated: 2546

======================================================================
EXPERIMENT ROUND 40/60
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2546

--- Round 40 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  CCAGCGAAGCGTGCGT
  CTCGCGAGGTACAGGC
  CGATGGGCCACACGGT
  AGCGGCAGTCCTCAGG
  CGAGTCCAGACTGGGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 13.170
  Max reward: 18.731
  With intrinsic bonuses: 13.159

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9876, entropy=0.2462, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1768

=== Surrogate Model Training ===
Total samples: 2610

Training on 2473 samples (removed 137 outliers)
Reward range: [8.15, 16.25], mean: 12.20
  Created 13 candidate models for data size 2473
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.167 (std: 0.072)
  rf-tuned-xl: R2 = 0.164 (std: 0.075)
  gb-tuned-l: R2 = 0.199 (std: 0.077)
  gb-tuned-xl: R2 = 0.199 (std: 0.077)
  xgb-xl: R2 = 0.081 (std: 0.081)
  xgb-l: R2 = 0.081 (std: 0.081)
  mlp-adaptive-xl: R2 = 0.175 (std: 0.089)
  mlp-l: R2 = 0.173 (std: 0.105)
  svr-rbf-xl: R2 = 0.226 (std: 0.074)
  svr-poly-l: R2 = 0.226 (std: 0.074)
  knn-tuned-sqrt: R2 = 0.053 (std: 0.128)
  knn-tuned-l: R2 = 0.053 (std: 0.128)
  ridge: R2 = 0.084 (std: 0.093)

Model-based training with 2 models
Best R2: 0.226, Mean R2: 0.145
Running 3 virtual training rounds
    Using ridge regression weights
    Model weights: svr-rbf-xl:1.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9821, entropy=0.2563, kl_div=0.0000
    Epoch 1: policy_loss=-0.0254, value_loss=0.9821, entropy=0.2556, kl_div=-0.3193
  Round 1/3: Mean predicted reward = 11.292
    Using ridge regression weights
    Model weights: svr-rbf-xl:1.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9815, entropy=0.2514, kl_div=0.0000
    Epoch 1: policy_loss=-0.0482, value_loss=0.9815, entropy=0.2515, kl_div=-0.2892
  Round 2/3: Mean predicted reward = 11.817
    Using ridge regression weights
    Model weights: svr-rbf-xl:1.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9871, entropy=0.2491, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3124
  Round 3/3: Mean predicted reward = 12.333

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 40 Results ---
  Mean Oracle Reward: 13.171
  Min Oracle Reward: 8.669
  Max Oracle Reward: 18.782
  Std Oracle Reward: 2.087
  Sequence Diversity: 0.969
  Models Used: 2
  Model R2 - Mean: 0.145, Max: 0.226, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 2610

======================================================================
EXPERIMENT ROUND 41/60
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2610

--- Round 41 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  CGGAATGGCTCACCGG
  GGATGGTCCACGCAGC
  CTCCCGATGCAGGGAG
  CTGATACAGGGCGCGC
  AAGACGCGGCCTCGTG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.838
  Max reward: 18.791
  With intrinsic bonuses: 12.836

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9909, entropy=0.2312, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6792

=== Surrogate Model Training ===
Total samples: 2674

Training on 2530 samples (removed 144 outliers)
Reward range: [8.15, 16.25], mean: 12.21
  Created 13 candidate models for data size 2530
Current R2 threshold: 0.22000000000000003
  rf-tuned-l: R2 = 0.179 (std: 0.083)
  rf-tuned-xl: R2 = 0.179 (std: 0.083)
  gb-tuned-l: R2 = 0.191 (std: 0.084)
  gb-tuned-xl: R2 = 0.191 (std: 0.084)
  xgb-xl: R2 = 0.085 (std: 0.095)
  xgb-l: R2 = 0.085 (std: 0.095)
  mlp-adaptive-xl: R2 = 0.195 (std: 0.096)
  mlp-l: R2 = 0.197 (std: 0.081)
  svr-rbf-xl: R2 = 0.226 (std: 0.077)
  svr-poly-l: R2 = 0.226 (std: 0.077)
  knn-tuned-sqrt: R2 = 0.060 (std: 0.143)
  knn-tuned-l: R2 = 0.060 (std: 0.143)
  ridge: R2 = 0.085 (std: 0.097)

Model-based training with 2 models
Best R2: 0.226, Mean R2: 0.151
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9836, entropy=0.2395, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1907
  Round 1/3: Mean predicted reward = 11.458
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9845, entropy=0.2571, kl_div=0.0000
    Epoch 1: policy_loss=0.0491, value_loss=0.9845, entropy=0.2569, kl_div=-0.3571
  Round 2/3: Mean predicted reward = 11.913
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000 svr-poly-l:0.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9884, entropy=0.2403, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5058
  Round 3/3: Mean predicted reward = 12.142

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 41 Results ---
  Mean Oracle Reward: 12.848
  Min Oracle Reward: 6.714
  Max Oracle Reward: 18.621
  Std Oracle Reward: 2.389
  Sequence Diversity: 0.969
  Models Used: 2
  Model R2 - Mean: 0.151, Max: 0.226, Count: 13
  Total Sequences Evaluated: 2674

======================================================================
EXPERIMENT ROUND 42/60
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2674

--- Round 42 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGCCTGGCGGAACCAG
  CAGGCTCTACAGGGGC
  GGGCATCCGAGTCCGA
  GGGATGACGGCTCACC
  ACGGATTGCCGACGGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.660
  Max reward: 17.102
  With intrinsic bonuses: 12.632

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9891, entropy=0.2446, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6912

=== Surrogate Model Training ===
Total samples: 2738

Training on 2589 samples (removed 149 outliers)
Reward range: [8.15, 16.25], mean: 12.22
  Created 13 candidate models for data size 2589
Current R2 threshold: 0.24000000000000005
  rf-tuned-l: R2 = 0.187 (std: 0.091)
  rf-tuned-xl: R2 = 0.180 (std: 0.096)
  gb-tuned-l: R2 = 0.201 (std: 0.092)
  gb-tuned-xl: R2 = 0.201 (std: 0.092)
  xgb-xl: R2 = 0.102 (std: 0.103)
  xgb-l: R2 = 0.102 (std: 0.103)
  mlp-adaptive-xl: R2 = 0.197 (std: 0.098)
  mlp-l: R2 = 0.163 (std: 0.110)
  svr-rbf-xl: R2 = 0.228 (std: 0.080)
  svr-poly-l: R2 = 0.228 (std: 0.080)
  knn-tuned-sqrt: R2 = 0.075 (std: 0.140)
  knn-tuned-l: R2 = 0.075 (std: 0.140)
  ridge: R2 = 0.090 (std: 0.101)
  Fallback: Using svr-rbf-xl with R2 = 0.228

Model-based training with 1 models
Best R2: 0.228, Mean R2: 0.156
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9771, entropy=0.2276, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2759
  Round 1/3: Mean predicted reward = 11.333
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9838, entropy=0.2384, kl_div=0.0000
    Epoch 1: policy_loss=-0.0475, value_loss=0.9838, entropy=0.2386, kl_div=-0.0818
  Round 2/3: Mean predicted reward = 11.824
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9892, entropy=0.2356, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1640
  Round 3/3: Mean predicted reward = 12.216

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 42 Results ---
  Mean Oracle Reward: 12.687
  Min Oracle Reward: 6.282
  Max Oracle Reward: 16.934
  Std Oracle Reward: 1.812
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.156, Max: 0.228, Count: 13
  Total Sequences Evaluated: 2738

======================================================================
EXPERIMENT ROUND 43/60
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2738

--- Round 43 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCCGGCGACGACAGTG
  GGTCGTAAGACCGCCG
  GAAGCGCGGGCTCATC
  CCTCGGCGGCGAGTAA
  CCGGCGGGTCCATAAG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.553
  Max reward: 16.682
  With intrinsic bonuses: 12.512

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9888, entropy=0.2352, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2612

=== Surrogate Model Training ===
Total samples: 2802

Training on 2651 samples (removed 151 outliers)
Reward range: [8.15, 16.25], mean: 12.23
  Created 13 candidate models for data size 2651
Current R2 threshold: 0.26000000000000006
  rf-tuned-l: R2 = 0.202 (std: 0.106)
  rf-tuned-xl: R2 = 0.200 (std: 0.102)
  gb-tuned-l: R2 = 0.207 (std: 0.099)
  gb-tuned-xl: R2 = 0.207 (std: 0.099)
  xgb-xl: R2 = 0.123 (std: 0.136)
  xgb-l: R2 = 0.123 (std: 0.136)
  mlp-adaptive-xl: R2 = 0.191 (std: 0.097)
  mlp-l: R2 = 0.203 (std: 0.100)
  svr-rbf-xl: R2 = 0.243 (std: 0.092)
  svr-poly-l: R2 = 0.243 (std: 0.092)
  knn-tuned-sqrt: R2 = 0.089 (std: 0.144)
  knn-tuned-l: R2 = 0.089 (std: 0.144)
  ridge: R2 = 0.098 (std: 0.111)
  Fallback: Using svr-rbf-xl with R2 = 0.243

Model-based training with 1 models
Best R2: 0.243, Mean R2: 0.170
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9813, entropy=0.2407, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0562
  Round 1/3: Mean predicted reward = 11.641
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9838, entropy=0.2427, kl_div=0.0000
    Epoch 1: policy_loss=-0.0268, value_loss=0.9838, entropy=0.2435, kl_div=-0.1385
  Round 2/3: Mean predicted reward = 11.779
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9886, entropy=0.2248, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1231
  Round 3/3: Mean predicted reward = 12.309

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 43 Results ---
  Mean Oracle Reward: 12.526
  Min Oracle Reward: 8.123
  Max Oracle Reward: 16.862
  Std Oracle Reward: 1.580
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.170, Max: 0.243, Count: 13
  Total Sequences Evaluated: 2802

======================================================================
EXPERIMENT ROUND 44/60
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2802

--- Round 44 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  ACCCGTGGCACTGAGG
  CCAGACGTCAGGGCGT
  TTCCGGGGACGCCAGA
  GGGCGCAGCCGATCTA
  AGCAGTGGTGCCCCAG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.343
  Max reward: 15.509
  With intrinsic bonuses: 12.345

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9885, entropy=0.2424, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0771

=== Surrogate Model Training ===
Total samples: 2866

Training on 2713 samples (removed 153 outliers)
Reward range: [8.15, 16.25], mean: 12.24
  Created 13 candidate models for data size 2713
Current R2 threshold: 0.27999999999999997
  rf-tuned-l: R2 = 0.183 (std: 0.110)
  rf-tuned-xl: R2 = 0.187 (std: 0.097)
  gb-tuned-l: R2 = 0.209 (std: 0.099)
  gb-tuned-xl: R2 = 0.209 (std: 0.099)
  xgb-xl: R2 = 0.116 (std: 0.107)
  xgb-l: R2 = 0.116 (std: 0.107)
  mlp-adaptive-xl: R2 = 0.194 (std: 0.103)
  mlp-l: R2 = 0.208 (std: 0.089)
  svr-rbf-xl: R2 = 0.239 (std: 0.095)
  svr-poly-l: R2 = 0.239 (std: 0.095)
  knn-tuned-sqrt: R2 = 0.076 (std: 0.152)
  knn-tuned-l: R2 = 0.076 (std: 0.152)
  ridge: R2 = 0.101 (std: 0.115)
  Fallback: Using svr-rbf-xl with R2 = 0.239

Model-based training with 1 models
Best R2: 0.239, Mean R2: 0.166
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9800, entropy=0.2244, kl_div=0.0000
    Epoch 1: policy_loss=-0.0005, value_loss=0.9800, entropy=0.2245, kl_div=0.0144
  Round 1/3: Mean predicted reward = 11.576
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9827, entropy=0.2391, kl_div=0.0000
    Epoch 1: policy_loss=-0.0352, value_loss=0.9827, entropy=0.2396, kl_div=-0.1123
  Round 2/3: Mean predicted reward = 11.673
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9893, entropy=0.2336, kl_div=0.0000
    Epoch 1: policy_loss=0.0128, value_loss=0.9893, entropy=0.2340, kl_div=-0.0459
  Round 3/3: Mean predicted reward = 12.081

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 44 Results ---
  Mean Oracle Reward: 12.357
  Min Oracle Reward: 6.613
  Max Oracle Reward: 15.440
  Std Oracle Reward: 1.837
  Sequence Diversity: 0.984
  Models Used: 1
  Model R2 - Mean: 0.166, Max: 0.239, Count: 13
  Total Sequences Evaluated: 2866

======================================================================
EXPERIMENT ROUND 45/60
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2866

--- Round 45 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  AAGTCGGGCGGCATCC
  GCATACCGGGCCTGGA
  GTCGAAGAGCCGTCGC
  GTGATCGAGCCGGACC
  AGGCGGCTCTGAACCG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.606
  Max reward: 16.575
  With intrinsic bonuses: 12.602

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9903, entropy=0.2410, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4942

=== Surrogate Model Training ===
Total samples: 2930

Training on 2771 samples (removed 159 outliers)
Reward range: [8.16, 16.25], mean: 12.25
  Created 13 candidate models for data size 2771
Current R2 threshold: 0.3
  rf-tuned-l: R2 = 0.189 (std: 0.106)
  rf-tuned-xl: R2 = 0.197 (std: 0.107)
  gb-tuned-l: R2 = 0.214 (std: 0.101)
  gb-tuned-xl: R2 = 0.214 (std: 0.101)
  xgb-xl: R2 = 0.123 (std: 0.122)
  xgb-l: R2 = 0.123 (std: 0.122)
  mlp-adaptive-xl: R2 = 0.189 (std: 0.116)
  mlp-l: R2 = 0.193 (std: 0.108)
  svr-rbf-xl: R2 = 0.240 (std: 0.100)
  svr-poly-l: R2 = 0.240 (std: 0.100)
  knn-tuned-sqrt: R2 = 0.076 (std: 0.152)
  knn-tuned-l: R2 = 0.076 (std: 0.152)
  ridge: R2 = 0.098 (std: 0.117)
  Fallback: Using svr-rbf-xl with R2 = 0.240

Model-based training with 1 models
Best R2: 0.240, Mean R2: 0.167
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9818, entropy=0.2340, kl_div=0.0000
    Epoch 1: policy_loss=-0.0512, value_loss=0.9818, entropy=0.2352, kl_div=-0.0594
  Round 1/3: Mean predicted reward = 11.434
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9822, entropy=0.2396, kl_div=0.0000
    Epoch 1: policy_loss=0.2781, value_loss=0.9822, entropy=0.2456, kl_div=-0.8935
  Round 2/3: Mean predicted reward = 11.548
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9892, entropy=0.2489, kl_div=0.0000
    Epoch 1: policy_loss=-0.0066, value_loss=0.9892, entropy=0.2511, kl_div=-0.0925
  Round 3/3: Mean predicted reward = 12.136

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 45 Results ---
  Mean Oracle Reward: 12.595
  Min Oracle Reward: 6.125
  Max Oracle Reward: 16.460
  Std Oracle Reward: 1.855
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.167, Max: 0.240, Count: 13
  Total Sequences Evaluated: 2930

======================================================================
EXPERIMENT ROUND 46/60
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2930

--- Round 46 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  GTCCCGCGGGTCAGAA
  TAACCGGTCACGCGGG
  TGGGACTGGAGCCCCA
  GCCAGTCCGTGGAAGC
  CGAGAGAGCGCTCGCT
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.381
  Max reward: 16.126
  With intrinsic bonuses: 12.380

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9904, entropy=0.2318, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7575

=== Surrogate Model Training ===
Total samples: 2994

Training on 2834 samples (removed 160 outliers)
Reward range: [8.15, 16.27], mean: 12.26
  Created 13 candidate models for data size 2834
Current R2 threshold: 0.32
  rf-tuned-l: R2 = 0.201 (std: 0.111)
  rf-tuned-xl: R2 = 0.202 (std: 0.115)
  gb-tuned-l: R2 = 0.214 (std: 0.107)
  gb-tuned-xl: R2 = 0.214 (std: 0.107)
  xgb-xl: R2 = 0.138 (std: 0.131)
  xgb-l: R2 = 0.138 (std: 0.131)
  mlp-adaptive-xl: R2 = 0.202 (std: 0.111)
  mlp-l: R2 = 0.204 (std: 0.112)
  svr-rbf-xl: R2 = 0.247 (std: 0.103)
  svr-poly-l: R2 = 0.247 (std: 0.103)
  knn-tuned-sqrt: R2 = 0.083 (std: 0.162)
  knn-tuned-l: R2 = 0.083 (std: 0.162)
  ridge: R2 = 0.103 (std: 0.122)
  Fallback: Using svr-rbf-xl with R2 = 0.247

Model-based training with 1 models
Best R2: 0.247, Mean R2: 0.175
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9828, entropy=0.2482, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1499
  Round 1/3: Mean predicted reward = 11.641
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9881, entropy=0.2277, kl_div=0.0000
    Epoch 1: policy_loss=-0.0305, value_loss=0.9881, entropy=0.2312, kl_div=-0.3219
  Round 2/3: Mean predicted reward = 11.633
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9879, entropy=0.2517, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2465
  Round 3/3: Mean predicted reward = 12.109

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 46 Results ---
  Mean Oracle Reward: 12.374
  Min Oracle Reward: 0.000
  Max Oracle Reward: 16.259
  Std Oracle Reward: 2.402
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.175, Max: 0.247, Count: 13
  Total Sequences Evaluated: 2994

======================================================================
EXPERIMENT ROUND 47/60
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2994

--- Round 47 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GATAGGCCCTCGGCGA
  ACGGCACTGGTGACCG
  CAGAGCTGCTACGGGC
  CGTGCGCAAGCCGATG
  GTTGGAACGGACCGCC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.381
  Max reward: 16.509
  With intrinsic bonuses: 12.383

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9909, entropy=0.2468, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4047

=== Surrogate Model Training ===
Total samples: 3058

Training on 2897 samples (removed 161 outliers)
Reward range: [8.15, 16.27], mean: 12.26
  Created 13 candidate models for data size 2897
Current R2 threshold: 0.34
  rf-tuned-l: R2 = 0.206 (std: 0.113)
  rf-tuned-xl: R2 = 0.202 (std: 0.117)
  gb-tuned-l: R2 = 0.216 (std: 0.118)
  gb-tuned-xl: R2 = 0.216 (std: 0.118)
  xgb-xl: R2 = 0.130 (std: 0.149)
  xgb-l: R2 = 0.130 (std: 0.149)
  mlp-adaptive-xl: R2 = 0.218 (std: 0.109)
  mlp-l: R2 = 0.224 (std: 0.111)
  svr-rbf-xl: R2 = 0.249 (std: 0.114)
  svr-poly-l: R2 = 0.249 (std: 0.114)
  knn-tuned-sqrt: R2 = 0.089 (std: 0.172)
  knn-tuned-l: R2 = 0.089 (std: 0.172)
  ridge: R2 = 0.106 (std: 0.130)
  Fallback: Using svr-rbf-xl with R2 = 0.249

Model-based training with 1 models
Best R2: 0.249, Mean R2: 0.179
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9852, entropy=0.2621, kl_div=0.0000
    Epoch 1: policy_loss=-0.0493, value_loss=0.9852, entropy=0.2642, kl_div=-0.0822
  Round 1/3: Mean predicted reward = 11.834
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9833, entropy=0.2603, kl_div=0.0000
    Epoch 1: policy_loss=0.1086, value_loss=0.9833, entropy=0.2673, kl_div=-0.5018
  Round 2/3: Mean predicted reward = 12.120
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9907, entropy=0.2403, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2078
  Round 3/3: Mean predicted reward = 12.052

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 47 Results ---
  Mean Oracle Reward: 12.377
  Min Oracle Reward: 7.816
  Max Oracle Reward: 16.937
  Std Oracle Reward: 1.671
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.179, Max: 0.249, Count: 13
  Total Sequences Evaluated: 3058

======================================================================
EXPERIMENT ROUND 48/60
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 3058

--- Round 48 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GACGCGCGGCTACGAT
  GGCGTAGACTGCGCCA
  AACGTGCGGCGGATCC
  CGGCGATGAACGCTGC
  AGCGGTCGAGATGCCC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.576
  Max reward: 16.352
  With intrinsic bonuses: 12.562

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9875, entropy=0.2591, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2067

=== Surrogate Model Training ===
Total samples: 3122

Training on 2956 samples (removed 166 outliers)
Reward range: [8.16, 16.27], mean: 12.27
  Created 13 candidate models for data size 2956
Current R2 threshold: 0.36000000000000004
  rf-tuned-l: R2 = 0.203 (std: 0.111)
  rf-tuned-xl: R2 = 0.205 (std: 0.109)
  gb-tuned-l: R2 = 0.223 (std: 0.115)
  gb-tuned-xl: R2 = 0.223 (std: 0.115)
  xgb-xl: R2 = 0.142 (std: 0.147)
  xgb-l: R2 = 0.142 (std: 0.147)
  mlp-adaptive-xl: R2 = 0.223 (std: 0.114)
  mlp-l: R2 = 0.206 (std: 0.117)
  svr-rbf-xl: R2 = 0.253 (std: 0.116)
  svr-poly-l: R2 = 0.253 (std: 0.116)
  knn-tuned-sqrt: R2 = 0.077 (std: 0.158)
  knn-tuned-l: R2 = 0.077 (std: 0.158)
  ridge: R2 = 0.104 (std: 0.126)
  Fallback: Using svr-rbf-xl with R2 = 0.253

Model-based training with 1 models
Best R2: 0.253, Mean R2: 0.179
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9855, entropy=0.2421, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3104
  Round 1/3: Mean predicted reward = 12.122
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9858, entropy=0.2468, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1119
  Round 2/3: Mean predicted reward = 11.953
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9890, entropy=0.2574, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1931
  Round 3/3: Mean predicted reward = 12.179

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 48 Results ---
  Mean Oracle Reward: 12.575
  Min Oracle Reward: 7.785
  Max Oracle Reward: 16.355
  Std Oracle Reward: 1.657
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.179, Max: 0.253, Count: 13
  Total Sequences Evaluated: 3122

======================================================================
EXPERIMENT ROUND 49/60
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 3122
  Performance plateaued, reducing LR to 0.000019

--- Round 49 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  GAGCCGCGAGTTCGCA
  GCGATGGGGCCATACC
  GAGTTAAGCGGGCCCC
  TGGGCTAGCAGGCACC
  CAGATGGGTCCCGCAG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.613
  Max reward: 15.748
  With intrinsic bonuses: 12.598

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9912, entropy=0.2738, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0591

=== Surrogate Model Training ===
Total samples: 3186

Training on 3016 samples (removed 170 outliers)
Reward range: [8.18, 16.27], mean: 12.28
  Created 13 candidate models for data size 3016
Current R2 threshold: 0.38000000000000006
  rf-tuned-l: R2 = 0.214 (std: 0.109)
  rf-tuned-xl: R2 = 0.210 (std: 0.102)
  gb-tuned-l: R2 = 0.225 (std: 0.104)
  gb-tuned-xl: R2 = 0.225 (std: 0.104)
  xgb-xl: R2 = 0.153 (std: 0.113)
  xgb-l: R2 = 0.153 (std: 0.113)
  mlp-adaptive-xl: R2 = 0.195 (std: 0.116)
  mlp-l: R2 = 0.204 (std: 0.109)
  svr-rbf-xl: R2 = 0.255 (std: 0.109)
  svr-poly-l: R2 = 0.255 (std: 0.109)
  knn-tuned-sqrt: R2 = 0.078 (std: 0.153)
  knn-tuned-l: R2 = 0.078 (std: 0.153)
  ridge: R2 = 0.105 (std: 0.124)
  Fallback: Using svr-rbf-xl with R2 = 0.255

Model-based training with 1 models
Best R2: 0.255, Mean R2: 0.181
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9852, entropy=0.2550, kl_div=0.0000
    Epoch 1: policy_loss=-0.0039, value_loss=0.9852, entropy=0.2551, kl_div=0.0177
  Round 1/3: Mean predicted reward = 11.700
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9851, entropy=0.2504, kl_div=0.0000
    Epoch 1: policy_loss=-0.0206, value_loss=0.9851, entropy=0.2514, kl_div=-0.0502
  Round 2/3: Mean predicted reward = 11.953
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9877, entropy=0.2641, kl_div=0.0000
    Epoch 1: policy_loss=0.0021, value_loss=0.9877, entropy=0.2650, kl_div=-0.0452
  Round 3/3: Mean predicted reward = 12.221

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 49 Results ---
  Mean Oracle Reward: 12.595
  Min Oracle Reward: 7.869
  Max Oracle Reward: 15.996
  Std Oracle Reward: 1.442
  Sequence Diversity: 0.984
  Models Used: 1
  Model R2 - Mean: 0.181, Max: 0.255, Count: 13
  Total Sequences Evaluated: 3186

======================================================================
EXPERIMENT ROUND 50/60
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 3186
  Consistent improvement, increasing LR to 0.000360

--- Round 50 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AGCAGGGTCGACCCGT
  GGCCATAACTGGCGCG
  CGTAGCAGCCCATGGG
  GTAGGATCCCCAGGCG
  GGATGCCGCATCCAGG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.512
  Max reward: 15.143
  With intrinsic bonuses: 12.547

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9920, entropy=0.2573, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2584

=== Surrogate Model Training ===
Total samples: 3250

Training on 3079 samples (removed 171 outliers)
Reward range: [8.18, 16.27], mean: 12.29
  Created 13 candidate models for data size 3079
Current R2 threshold: 0.4000000000000001
  rf-tuned-l: R2 = 0.210 (std: 0.107)
  rf-tuned-xl: R2 = 0.209 (std: 0.105)
  gb-tuned-l: R2 = 0.226 (std: 0.114)
  gb-tuned-xl: R2 = 0.226 (std: 0.114)
  xgb-xl: R2 = 0.156 (std: 0.122)
  xgb-l: R2 = 0.156 (std: 0.122)
  mlp-adaptive-xl: R2 = 0.213 (std: 0.102)
  mlp-l: R2 = 0.216 (std: 0.121)
  svr-rbf-xl: R2 = 0.261 (std: 0.112)
  svr-poly-l: R2 = 0.261 (std: 0.112)
  knn-tuned-sqrt: R2 = 0.090 (std: 0.154)
  knn-tuned-l: R2 = 0.090 (std: 0.154)
  ridge: R2 = 0.109 (std: 0.128)
  Fallback: Using svr-rbf-xl with R2 = 0.261

Model-based training with 1 models
Best R2: 0.261, Mean R2: 0.186
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9844, entropy=0.2538, kl_div=0.0000
    Epoch 1: policy_loss=0.0241, value_loss=0.9844, entropy=0.2642, kl_div=-0.2918
  Round 1/3: Mean predicted reward = 11.862
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9838, entropy=0.2833, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0736
  Round 2/3: Mean predicted reward = 12.293
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9883, entropy=0.2747, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2646
  Round 3/3: Mean predicted reward = 12.099

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 50 Results ---
  Mean Oracle Reward: 12.558
  Min Oracle Reward: 6.553
  Max Oracle Reward: 15.127
  Std Oracle Reward: 1.622
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.186, Max: 0.261, Count: 13
  Total Sequences Evaluated: 3250

======================================================================
EXPERIMENT ROUND 51/60
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 3250
  Performance plateaued, reducing LR to 0.000136

--- Round 51 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCCTCGGGGTCAGAGA
  ATGCCCTGAGGGGACC
  GCAGCGGAGCCTTACG
  CTTGGAACGAGGCGCC
  CGAAGGGTCGCGCATC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.277
  Max reward: 16.234
  With intrinsic bonuses: 12.279

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9876, entropy=0.2947, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2226

=== Surrogate Model Training ===
Total samples: 3314

Training on 3142 samples (removed 172 outliers)
Reward range: [8.21, 16.27], mean: 12.29
  Created 13 candidate models for data size 3142
Current R2 threshold: 0.42
  rf-tuned-l: R2 = 0.213 (std: 0.105)
  rf-tuned-xl: R2 = 0.209 (std: 0.114)
  gb-tuned-l: R2 = 0.234 (std: 0.108)
  gb-tuned-xl: R2 = 0.234 (std: 0.108)
  xgb-xl: R2 = 0.142 (std: 0.140)
  xgb-l: R2 = 0.142 (std: 0.140)
  mlp-adaptive-xl: R2 = 0.212 (std: 0.121)
  mlp-l: R2 = 0.216 (std: 0.122)
  svr-rbf-xl: R2 = 0.266 (std: 0.118)
  svr-poly-l: R2 = 0.266 (std: 0.118)
  knn-tuned-sqrt: R2 = 0.094 (std: 0.159)
  knn-tuned-l: R2 = 0.094 (std: 0.159)
  ridge: R2 = 0.113 (std: 0.126)
  Fallback: Using svr-rbf-xl with R2 = 0.266

Model-based training with 1 models
Best R2: 0.266, Mean R2: 0.187
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9863, entropy=0.2636, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4261
  Round 1/3: Mean predicted reward = 12.235
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9890, entropy=0.2709, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4408
  Round 2/3: Mean predicted reward = 12.378
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9870, entropy=0.2684, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5585
  Round 3/3: Mean predicted reward = 12.363

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 51 Results ---
  Mean Oracle Reward: 12.303
  Min Oracle Reward: 8.302
  Max Oracle Reward: 16.637
  Std Oracle Reward: 1.640
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.187, Max: 0.266, Count: 13
  Total Sequences Evaluated: 3314

======================================================================
EXPERIMENT ROUND 52/60
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 3314

--- Round 52 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  GACTGGCGCGACATCG
  CCGGGCGTGCACTAAG
  GCTGCCGTAGAACGGC
  GGGGAACCCGCCTGTA
  AGTGCGTGGGCAACCC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.322
  Max reward: 15.384
  With intrinsic bonuses: 12.296

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9932, entropy=0.2604, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0224

=== Surrogate Model Training ===
Total samples: 3378

Training on 3205 samples (removed 173 outliers)
Reward range: [8.21, 16.27], mean: 12.29
  Created 13 candidate models for data size 3205
Current R2 threshold: 0.44
  rf-tuned-l: R2 = 0.218 (std: 0.119)
  rf-tuned-xl: R2 = 0.218 (std: 0.116)
  gb-tuned-l: R2 = 0.234 (std: 0.121)
  gb-tuned-xl: R2 = 0.234 (std: 0.121)
  xgb-xl: R2 = 0.171 (std: 0.129)
  xgb-l: R2 = 0.171 (std: 0.129)
  mlp-adaptive-xl: R2 = 0.223 (std: 0.124)
  mlp-l: R2 = 0.217 (std: 0.123)
  svr-rbf-xl: R2 = 0.266 (std: 0.123)
  svr-poly-l: R2 = 0.266 (std: 0.123)
  knn-tuned-sqrt: R2 = 0.102 (std: 0.165)
  knn-tuned-l: R2 = 0.102 (std: 0.165)
  ridge: R2 = 0.116 (std: 0.135)
  Fallback: Using svr-rbf-xl with R2 = 0.266

Model-based training with 1 models
Best R2: 0.266, Mean R2: 0.195
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9856, entropy=0.2524, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5426
  Round 1/3: Mean predicted reward = 11.691
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9883, entropy=0.2694, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6142
  Round 2/3: Mean predicted reward = 12.215
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9874, entropy=0.2571, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8687
  Round 3/3: Mean predicted reward = 12.480

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 52 Results ---
  Mean Oracle Reward: 12.300
  Min Oracle Reward: 6.302
  Max Oracle Reward: 14.989
  Std Oracle Reward: 1.763
  Sequence Diversity: 0.984
  Models Used: 1
  Model R2 - Mean: 0.195, Max: 0.266, Count: 13
  Total Sequences Evaluated: 3378

======================================================================
EXPERIMENT ROUND 53/60
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 3378

--- Round 53 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGCGCAGGCATGGTAC
  ACCAGCGCACTGTGGG
  GCATGGACCGCATCGG
  GGGACGTAGCCGCACT
  TGGCGCATCACAGGGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.679
  Max reward: 16.964
  With intrinsic bonuses: 12.674

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9886, entropy=0.2461, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6154

=== Surrogate Model Training ===
Total samples: 3442

Training on 3272 samples (removed 170 outliers)
Reward range: [8.18, 16.37], mean: 12.30
  Created 13 candidate models for data size 3272
Current R2 threshold: 0.46
  rf-tuned-l: R2 = 0.235 (std: 0.107)
  rf-tuned-xl: R2 = 0.226 (std: 0.114)
  gb-tuned-l: R2 = 0.244 (std: 0.110)
  gb-tuned-xl: R2 = 0.244 (std: 0.110)
  xgb-xl: R2 = 0.157 (std: 0.125)
  xgb-l: R2 = 0.157 (std: 0.125)
  mlp-adaptive-xl: R2 = 0.237 (std: 0.122)
  mlp-l: R2 = 0.232 (std: 0.122)
  svr-rbf-xl: R2 = 0.275 (std: 0.122)
  svr-poly-l: R2 = 0.275 (std: 0.122)
  knn-tuned-sqrt: R2 = 0.111 (std: 0.152)
  knn-tuned-l: R2 = 0.111 (std: 0.152)
  ridge: R2 = 0.116 (std: 0.133)
  Fallback: Using svr-rbf-xl with R2 = 0.275

Model-based training with 1 models
Best R2: 0.275, Mean R2: 0.202
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9859, entropy=0.2488, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2892
  Round 1/3: Mean predicted reward = 12.002
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9863, entropy=0.2531, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2965
  Round 2/3: Mean predicted reward = 12.335
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9859, entropy=0.2441, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4948
  Round 3/3: Mean predicted reward = 12.404

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 53 Results ---
  Mean Oracle Reward: 12.631
  Min Oracle Reward: 8.097
  Max Oracle Reward: 16.810
  Std Oracle Reward: 1.724
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.202, Max: 0.275, Count: 13
  Total Sequences Evaluated: 3442

======================================================================
EXPERIMENT ROUND 54/60
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 3442
  Consistent improvement, increasing LR to 0.000045

--- Round 54 Configuration ---
Learning rate: 0.000045
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GACGGCACTTCCAGGG
  CGCCGAGTCATAGCGG
  TCCCCCAGAGTGGGGA
  GTCCCATAGGGCGCGA
  CAGATGCAGGCGTGCC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.575
  Max reward: 16.355
  With intrinsic bonuses: 12.516

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9889, entropy=0.2407, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2440

=== Surrogate Model Training ===
Total samples: 3506

Training on 3327 samples (removed 179 outliers)
Reward range: [8.22, 16.27], mean: 12.31
  Created 13 candidate models for data size 3327
Current R2 threshold: 0.48000000000000004
  rf-tuned-l: R2 = 0.228 (std: 0.108)
  rf-tuned-xl: R2 = 0.233 (std: 0.105)
  gb-tuned-l: R2 = 0.241 (std: 0.115)
  gb-tuned-xl: R2 = 0.241 (std: 0.115)
  xgb-xl: R2 = 0.162 (std: 0.141)
  xgb-l: R2 = 0.162 (std: 0.141)
  mlp-adaptive-xl: R2 = 0.248 (std: 0.111)
  mlp-l: R2 = 0.239 (std: 0.119)
  svr-rbf-xl: R2 = 0.275 (std: 0.124)
  svr-poly-l: R2 = 0.275 (std: 0.124)
  knn-tuned-sqrt: R2 = 0.112 (std: 0.162)
  knn-tuned-l: R2 = 0.112 (std: 0.162)
  ridge: R2 = 0.117 (std: 0.130)
  Fallback: Using svr-rbf-xl with R2 = 0.275

Model-based training with 1 models
Best R2: 0.275, Mean R2: 0.203
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9843, entropy=0.2330, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1533
  Round 1/3: Mean predicted reward = 11.939
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9899, entropy=0.2178, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1558
  Round 2/3: Mean predicted reward = 12.208
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9918, entropy=0.2358, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2048
  Round 3/3: Mean predicted reward = 12.473

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 54 Results ---
  Mean Oracle Reward: 12.540
  Min Oracle Reward: 6.977
  Max Oracle Reward: 16.541
  Std Oracle Reward: 1.852
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.203, Max: 0.275, Count: 13
  Total Sequences Evaluated: 3506

======================================================================
EXPERIMENT ROUND 55/60
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 3506

--- Round 55 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGTGGCGCACCTAGAG
  AGCGGCGGACCGTACT
  TAGGCGCGATCGACGC
  AACGCGCTGCGCTGAG
  GTGAGTGCGCGACACC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.667
  Max reward: 15.443
  With intrinsic bonuses: 12.688

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9893, entropy=0.2406, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.7882

=== Surrogate Model Training ===
Total samples: 3570

Training on 3396 samples (removed 174 outliers)
Reward range: [8.21, 16.39], mean: 12.32
  Created 13 candidate models for data size 3396
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.227 (std: 0.113)
  rf-tuned-xl: R2 = 0.225 (std: 0.104)
  gb-tuned-l: R2 = 0.237 (std: 0.116)
  gb-tuned-xl: R2 = 0.237 (std: 0.116)
  xgb-xl: R2 = 0.157 (std: 0.147)
  xgb-l: R2 = 0.157 (std: 0.147)
  mlp-adaptive-xl: R2 = 0.227 (std: 0.120)
  mlp-l: R2 = 0.236 (std: 0.125)
  svr-rbf-xl: R2 = 0.280 (std: 0.132)
  svr-poly-l: R2 = 0.280 (std: 0.132)
  knn-tuned-sqrt: R2 = 0.107 (std: 0.161)
  knn-tuned-l: R2 = 0.107 (std: 0.161)
  ridge: R2 = 0.118 (std: 0.138)
  Fallback: Using svr-rbf-xl with R2 = 0.280

Model-based training with 1 models
Best R2: 0.280, Mean R2: 0.200
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9869, entropy=0.2160, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.8920
  Round 1/3: Mean predicted reward = 12.162
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9845, entropy=0.2162, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0060
  Round 2/3: Mean predicted reward = 11.953
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9895, entropy=0.2055, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1788
  Round 3/3: Mean predicted reward = 12.379

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 55 Results ---
  Mean Oracle Reward: 12.672
  Min Oracle Reward: 8.968
  Max Oracle Reward: 15.276
  Std Oracle Reward: 1.488
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.200, Max: 0.280, Count: 13
  Total Sequences Evaluated: 3570

======================================================================
EXPERIMENT ROUND 56/60
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 3570
  Performance plateaued, reducing LR to 0.000136

--- Round 56 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ATCCCCCGGTGGAGGA
  ACAGCGCGGATGGCCT
  CGGGGCCAGTCCATAG
  GGTAGGTCCGCGACAC
  CGGGCATCGACCGTGA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.655
  Max reward: 16.720
  With intrinsic bonuses: 12.658

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9895, entropy=0.2126, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5574

=== Surrogate Model Training ===
Total samples: 3634

Training on 3469 samples (removed 165 outliers)
Reward range: [8.18, 16.43], mean: 12.33
  Created 13 candidate models for data size 3469
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.242 (std: 0.112)
  rf-tuned-xl: R2 = 0.249 (std: 0.107)
  gb-tuned-l: R2 = 0.257 (std: 0.115)
  gb-tuned-xl: R2 = 0.257 (std: 0.115)
  xgb-xl: R2 = 0.191 (std: 0.150)
  xgb-l: R2 = 0.191 (std: 0.150)
  mlp-adaptive-xl: R2 = 0.237 (std: 0.140)
  mlp-l: R2 = 0.244 (std: 0.123)
  svr-rbf-xl: R2 = 0.294 (std: 0.132)
  svr-poly-l: R2 = 0.294 (std: 0.132)
  knn-tuned-sqrt: R2 = 0.127 (std: 0.154)
  knn-tuned-l: R2 = 0.127 (std: 0.154)
  ridge: R2 = 0.120 (std: 0.140)
  Fallback: Using svr-rbf-xl with R2 = 0.294

Model-based training with 1 models
Best R2: 0.294, Mean R2: 0.218
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9855, entropy=0.1933, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5320
  Round 1/3: Mean predicted reward = 11.993
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9876, entropy=0.1994, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5817
  Round 2/3: Mean predicted reward = 12.240
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9870, entropy=0.1981, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8040
  Round 3/3: Mean predicted reward = 12.394

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 56 Results ---
  Mean Oracle Reward: 12.639
  Min Oracle Reward: 7.425
  Max Oracle Reward: 16.489
  Std Oracle Reward: 1.940
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.218, Max: 0.294, Count: 13
  Total Sequences Evaluated: 3634

======================================================================
EXPERIMENT ROUND 57/60
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 3634
  Performance plateaued, reducing LR to 0.000100

--- Round 57 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  GAGCGCTCGTAGGACC
  GGACTCGGCCGATGCA
  ACCGCGCGAGACGTGT
  AACCGAGTGGCCCTGG
  GTCGGCCGGATAGCCA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.461
  Max reward: 15.424
  With intrinsic bonuses: 12.431

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9887, entropy=0.1930, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3033

=== Surrogate Model Training ===
Total samples: 3698

Training on 3531 samples (removed 167 outliers)
Reward range: [8.21, 16.43], mean: 12.34
  Created 13 candidate models for data size 3531
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.246 (std: 0.120)
  rf-tuned-xl: R2 = 0.246 (std: 0.117)
  gb-tuned-l: R2 = 0.254 (std: 0.124)
  gb-tuned-xl: R2 = 0.254 (std: 0.124)
  xgb-xl: R2 = 0.197 (std: 0.147)
  xgb-l: R2 = 0.197 (std: 0.147)
  mlp-adaptive-xl: R2 = 0.250 (std: 0.137)
  mlp-l: R2 = 0.256 (std: 0.121)
  svr-rbf-xl: R2 = 0.295 (std: 0.137)
  svr-poly-l: R2 = 0.295 (std: 0.137)
  knn-tuned-sqrt: R2 = 0.130 (std: 0.173)
  knn-tuned-l: R2 = 0.130 (std: 0.173)
  ridge: R2 = 0.123 (std: 0.148)
  Fallback: Using svr-rbf-xl with R2 = 0.295

Model-based training with 1 models
Best R2: 0.295, Mean R2: 0.221
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9849, entropy=0.1965, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0958
  Round 1/3: Mean predicted reward = 11.833
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9889, entropy=0.1867, kl_div=0.0000
    Epoch 1: policy_loss=-0.0101, value_loss=0.9889, entropy=0.1875, kl_div=-0.0507
  Round 2/3: Mean predicted reward = 12.113
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9888, entropy=0.1804, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2145
  Round 3/3: Mean predicted reward = 12.319

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 57 Results ---
  Mean Oracle Reward: 12.464
  Min Oracle Reward: 6.708
  Max Oracle Reward: 15.534
  Std Oracle Reward: 1.770
  Sequence Diversity: 0.984
  Models Used: 1
  Model R2 - Mean: 0.221, Max: 0.295, Count: 13
  Total Sequences Evaluated: 3698

======================================================================
EXPERIMENT ROUND 58/60
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 3698
  Performance plateaued, reducing LR to 0.000055

--- Round 58 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGCATGGGACCGCGCA
  CGGAGATCGCCTCAGG
  AGGTGGCTACGGCCAC
  ACCTTCGGCGACGAGG
  CGGACAGCCAGGGTTC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.515
  Max reward: 17.254
  With intrinsic bonuses: 12.500

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9928, entropy=0.1804, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0796

=== Surrogate Model Training ===
Total samples: 3762

Training on 3592 samples (removed 170 outliers)
Reward range: [8.21, 16.43], mean: 12.34
  Created 13 candidate models for data size 3592
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.241 (std: 0.112)
  rf-tuned-xl: R2 = 0.243 (std: 0.106)
  gb-tuned-l: R2 = 0.254 (std: 0.118)
  gb-tuned-xl: R2 = 0.254 (std: 0.118)
  xgb-xl: R2 = 0.197 (std: 0.144)
  xgb-l: R2 = 0.197 (std: 0.144)
  mlp-adaptive-xl: R2 = 0.258 (std: 0.125)
  mlp-l: R2 = 0.267 (std: 0.125)
  svr-rbf-xl: R2 = 0.297 (std: 0.129)
  svr-poly-l: R2 = 0.297 (std: 0.129)
  knn-tuned-sqrt: R2 = 0.130 (std: 0.169)
  knn-tuned-l: R2 = 0.130 (std: 0.169)
  ridge: R2 = 0.129 (std: 0.142)
  Fallback: Using svr-rbf-xl with R2 = 0.297

Model-based training with 1 models
Best R2: 0.297, Mean R2: 0.222
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9820, entropy=0.1816, kl_div=0.0000
    Epoch 1: policy_loss=-0.0242, value_loss=0.9820, entropy=0.1827, kl_div=-0.0174
  Round 1/3: Mean predicted reward = 11.793
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9864, entropy=0.1805, kl_div=0.0000
    Epoch 1: policy_loss=0.0169, value_loss=0.9864, entropy=0.1823, kl_div=-0.1818
  Round 2/3: Mean predicted reward = 12.063
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9881, entropy=0.1791, kl_div=0.0000
    Epoch 1: policy_loss=-0.0138, value_loss=0.9881, entropy=0.1795, kl_div=-0.0414
  Round 3/3: Mean predicted reward = 12.486

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 58 Results ---
  Mean Oracle Reward: 12.483
  Min Oracle Reward: 3.208
  Max Oracle Reward: 17.196
  Std Oracle Reward: 1.913
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.222, Max: 0.297, Count: 13
  Total Sequences Evaluated: 3762

======================================================================
EXPERIMENT ROUND 59/60
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 3762
  Performance plateaued, reducing LR to 0.000019

--- Round 59 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTGCGGCCGCCGAAAT
  CGGTGCCCAGAGACTG
  TCCAGGAAGGTCGGCC
  GTGCCAAGCGGTCACG
  TGGGCGCCGACTAAGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.657
  Max reward: 16.558
  With intrinsic bonuses: 12.660

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9887, entropy=0.1830, kl_div=0.0000
    Epoch 1: policy_loss=-0.0123, value_loss=0.9887, entropy=0.1827, kl_div=0.0329

=== Surrogate Model Training ===
Total samples: 3826

Training on 3650 samples (removed 176 outliers)
Reward range: [8.24, 16.43], mean: 12.36
  Created 13 candidate models for data size 3650
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.240 (std: 0.108)
  rf-tuned-xl: R2 = 0.234 (std: 0.115)
  gb-tuned-l: R2 = 0.255 (std: 0.121)
  gb-tuned-xl: R2 = 0.255 (std: 0.121)
  xgb-xl: R2 = 0.191 (std: 0.136)
  xgb-l: R2 = 0.191 (std: 0.136)
  mlp-adaptive-xl: R2 = 0.248 (std: 0.119)
  mlp-l: R2 = 0.250 (std: 0.119)
  svr-rbf-xl: R2 = 0.294 (std: 0.128)
  svr-poly-l: R2 = 0.294 (std: 0.128)
  knn-tuned-sqrt: R2 = 0.124 (std: 0.164)
  knn-tuned-l: R2 = 0.124 (std: 0.164)
  ridge: R2 = 0.128 (std: 0.136)
  Fallback: Using svr-rbf-xl with R2 = 0.294

Model-based training with 1 models
Best R2: 0.294, Mean R2: 0.218
Running 3 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9838, entropy=0.1819, kl_div=0.0000
    Epoch 1: policy_loss=0.0069, value_loss=0.9838, entropy=0.1816, kl_div=0.0220
  Round 1/3: Mean predicted reward = 11.582
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9869, entropy=0.1878, kl_div=0.0000
    Epoch 1: policy_loss=-0.0169, value_loss=0.9869, entropy=0.1881, kl_div=-0.0346
  Round 2/3: Mean predicted reward = 12.036
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9880, entropy=0.1885, kl_div=0.0000
    Epoch 1: policy_loss=-0.0085, value_loss=0.9880, entropy=0.1891, kl_div=-0.0410
  Round 3/3: Mean predicted reward = 12.169

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 59 Results ---
  Mean Oracle Reward: 12.668
  Min Oracle Reward: 7.189
  Max Oracle Reward: 16.959
  Std Oracle Reward: 1.684
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.218, Max: 0.294, Count: 13
  Total Sequences Evaluated: 3826

======================================================================
EXPERIMENT ROUND 60/60
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 3826
  Performance plateaued, reducing LR to 0.000150

--- Round 60 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  GGGTACAGGCCCGCTA
  GAGGTCCGCTGCAAGC
  CCGTGGAGCTCCAGGA
  GTAGGAAGGCCCGTCC
  GAGTGGATCCGCGCAC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.701
  Max reward: 16.388
  With intrinsic bonuses: 12.694

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9908, entropy=0.1785, kl_div=0.0000
    Epoch 1: policy_loss=0.0533, value_loss=0.9908, entropy=0.1829, kl_div=-0.3519

=== Surrogate Model Training ===
Total samples: 3890

Training on 3719 samples (removed 171 outliers)
Reward range: [8.22, 16.47], mean: 12.36
  Created 13 candidate models for data size 3719
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.251 (std: 0.122)
  rf-tuned-xl: R2 = 0.248 (std: 0.126)
  gb-tuned-l: R2 = 0.267 (std: 0.125)
  gb-tuned-xl: R2 = 0.267 (std: 0.125)
  xgb-xl: R2 = 0.205 (std: 0.159)
  xgb-l: R2 = 0.205 (std: 0.159)
  mlp-adaptive-xl: R2 = 0.256 (std: 0.154)
  mlp-l: R2 = 0.245 (std: 0.142)
  svr-rbf-xl: R2 = 0.307 (std: 0.141)
  svr-poly-l: R2 = 0.307 (std: 0.141)
  knn-tuned-sqrt: R2 = 0.142 (std: 0.172)
  knn-tuned-l: R2 = 0.142 (std: 0.172)
  ridge: R2 = 0.137 (std: 0.144)
  Fallback: Using svr-rbf-xl with R2 = 0.307

Model-based training with 1 models
Best R2: 0.307, Mean R2: 0.229
Running 5 virtual training rounds
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9865, entropy=0.1751, kl_div=0.0000
    Epoch 1: policy_loss=0.0559, value_loss=0.9865, entropy=0.1787, kl_div=-0.3123
  Round 1/5: Mean predicted reward = 11.918
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9862, entropy=0.1652, kl_div=0.0000
    Epoch 1: policy_loss=0.0166, value_loss=0.9862, entropy=0.1690, kl_div=-0.3022
  Round 2/5: Mean predicted reward = 12.276
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9864, entropy=0.1857, kl_div=0.0000
    Epoch 1: policy_loss=-0.0187, value_loss=0.9864, entropy=0.1881, kl_div=-0.0667
  Round 3/5: Mean predicted reward = 12.095
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9887, entropy=0.1901, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2190
  Round 4/5: Mean predicted reward = 12.615
    Using validation-optimized weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9886, entropy=0.1789, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4210
  Round 5/5: Mean predicted reward = 12.597

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 60 Results ---
  Mean Oracle Reward: 12.678
  Min Oracle Reward: 7.501
  Max Oracle Reward: 16.486
  Std Oracle Reward: 1.818
  Sequence Diversity: 0.984
  Models Used: 1
  Model R2 - Mean: 0.229, Max: 0.307, Count: 13
  Total Sequences Evaluated: 3890

======================================================================
DyNA PPO ALGORITHM COMPLETE!
======================================================================
Total rounds executed: 60
Total sequences evaluated: 3890
Best mean reward: 13.171 (achieved at round 40)

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 60
Final Mean Reward: 12.6778
Best Mean Reward: 13.1707
Best Max Reward: 18.9598
Initial Lr: 0.0003
Final Lr: 0.0003
Total Updates: 330
Final Diversity: 0.9844
Convergence Round: 4
==================================================

Generating learning curves...
Learning curves saved to learning_curves.png
Saving training metrics...
Metrics saved to training_metrics.json

======================================================================
FINAL OPTIMIZED SEQUENCES
======================================================================

Deterministic (Exploitation):
  GGGCCGAGCCGGCCGA: 15.240
  GGGCCGAGCCGGCCGA: 15.193
  GGGCCGAGCCGGCCGA: 15.131
  GGGCCGAGCCGGCCGA: 15.200
  GGGCCGAGCCGGCCGA: 15.176

Stochastic (Exploration):
  GGGCCGACGGCCGAGC: 15.323
  GGGCCGTGCGCGCCGA: 13.180
  GGGCCGAGCCGGCCGA: 15.133
  GGGCCGAGCCGGCCGC: 15.412
  GGGCCGAGCCGGAGCA: 13.620

Final Performance:
  Mean reward: 14.861
  Max reward: 15.412
  Std reward: 0.741

Best sequence found: GGGCCGAGCCGGCCGC
   Reward: 15.412

======================================================================
Training complete! Check 'learning_curves.png' and 'training_metrics.json'
======================================================================