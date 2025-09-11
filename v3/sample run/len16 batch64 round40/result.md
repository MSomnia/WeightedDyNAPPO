======================================================================
RUNNING IMPROVED DyNA PPO WITH BETTER SURROGATE LEARNING
======================================================================
======================================================================
IMPROVED DyNA PPO ALGORITHM
======================================================================
Configuration:
  Number of experiment rounds N = 40
  Number of model-based training rounds M = 5
  Minimum model score τ = 0.2
  Batch size B = 64
  Warm-up phase: True
======================================================================

=== WARM-UP PHASE ===
Generating 50 warm-up samples...
Warm-up statistics:
  Mean reward: 9.256
  Std reward: 3.618
  Min/Max: 0.000 / 14.608

Pre-training surrogate models on warm-up data...

Training on 45 samples (removed 5 outliers)
Reward range: [4.24, 14.61], mean: 10.19
  Created 8 candidate models for data size 45
Current R2 threshold: -0.3
  rf-xs: R2 = -0.459 (std: 0.512)
  rf-s: R2 = -0.348 (std: 0.367)
  knn-xs: R2 = -0.446 (std: 0.287)
  knn-s: R2 = -0.446 (std: 0.287)
  ridge: R2 = -0.241 (std: 0.086)
  gb-xs: R2 = -1.394 (std: 1.660)
  gp: R2 = -28.671 (std: 17.757)
  svr-rbf-s: R2 = -0.074 (std: 0.138)
Initial models trained: 2
Initial R2 scores - Mean: -4.010, Max: -0.074

======================================================================
EXPERIMENT ROUND 1/40
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.300
Total data collected: 50

--- Round 1 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  TGAAGGGTTCGTACAG
  AGAAATTGAAGGTGGA
  CAGTTTCCGTGAACGC
  TTGGCTGGTATGGCGC
  TTCCCTGTATACAGTT
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.313
  Max reward: 14.770
  With intrinsic bonuses: 11.343

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9838, entropy=1.3845, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0963

=== Surrogate Model Training ===
Total samples: 114

Training on 103 samples (removed 11 outliers)
Reward range: [6.74, 14.72], mean: 11.20
  Created 11 candidate models for data size 103
Current R2 threshold: -0.3
  rf-m: R2 = -0.172 (std: 0.265)
  rf-l: R2 = -0.160 (std: 0.253)
  gb-m: R2 = -0.245 (std: 0.225)
  gb-l: R2 = -0.255 (std: 0.259)
  xgb-m: R2 = -0.434 (std: 0.359)
  knn-m: R2 = -0.313 (std: 0.329)
  knn-tuned: R2 = -0.313 (std: 0.329)
  mlp-m: R2 = -2.275 (std: 1.384)
  svr-rbf: R2 = -0.012 (std: 0.160)
  svr-poly: R2 = -0.012 (std: 0.160)
  ridge: R2 = -0.174 (std: 0.243)

Model-based training with 7 models
Best R2: -0.012, Mean R2: -0.397
Running 2 virtual training rounds
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9973, entropy=1.3800, kl_div=0.0000
  Round 1/2: Mean predicted reward = 11.502
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=1.0019, entropy=1.3724, kl_div=0.0000
  Round 2/2: Mean predicted reward = 11.621

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 1 Results ---
  Mean Oracle Reward: 11.311
  Min Oracle Reward: 5.499
  Max Oracle Reward: 14.824
  Std Oracle Reward: 1.598
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: -0.397, Max: -0.012, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 114

======================================================================
EXPERIMENT ROUND 2/40
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.300
Total data collected: 114

--- Round 2 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  AACGATCACCTTTACG
  TTTTCGCGTACCGACT
  AATAGGGTGCCGTTGT
  TTACCAAACAGAGTCC
  AGACGACTTAGGTTGA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.418
  Max reward: 14.003
  With intrinsic bonuses: 11.430

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9924, entropy=1.3668, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0699

=== Surrogate Model Training ===
Total samples: 178

Training on 163 samples (removed 15 outliers)
Reward range: [7.97, 14.72], mean: 11.41
  Created 11 candidate models for data size 163
Current R2 threshold: -0.3
  rf-m: R2 = -0.061 (std: 0.217)
  rf-l: R2 = -0.055 (std: 0.229)
  gb-m: R2 = -0.053 (std: 0.253)
  gb-l: R2 = -0.038 (std: 0.252)
  xgb-m: R2 = -0.301 (std: 0.301)
  knn-m: R2 = -0.135 (std: 0.258)
  knn-tuned: R2 = -0.135 (std: 0.258)
  mlp-m: R2 = -2.157 (std: 1.159)
  svr-rbf: R2 = 0.043 (std: 0.126)
  svr-poly: R2 = 0.043 (std: 0.126)
  ridge: R2 = -0.025 (std: 0.168)

Model-based training with 9 models
Best R2: 0.043, Mean R2: -0.261
Running 3 virtual training rounds
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9917, entropy=1.3595, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0761
  Round 1/3: Mean predicted reward = 11.547
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9915, entropy=1.3521, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1071
  Round 2/3: Mean predicted reward = 11.375
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9930, entropy=1.3421, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0864
  Round 3/3: Mean predicted reward = 11.465

  === Progress Analysis ===
  Status: NORMAL

--- Round 2 Results ---
  Mean Oracle Reward: 11.422
  Min Oracle Reward: 4.881
  Max Oracle Reward: 14.248
  Std Oracle Reward: 1.649
  Sequence Diversity: 1.000
  Models Used: 9
  Model R2 - Mean: -0.261, Max: 0.043, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 178

======================================================================
EXPERIMENT ROUND 3/40
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.300
Total data collected: 178

--- Round 3 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  GAGCGCCGCATAGATG
  GACGGTCCCATGGGCC
  ACTCCCGCCTCCAGAG
  GCCCCAGGCCCCGGTG
  AGAGCAGGAACCCGCG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.668
  Max reward: 13.728
  With intrinsic bonuses: 11.783

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9880, entropy=1.3308, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0666

=== Surrogate Model Training ===
Total samples: 242

Training on 226 samples (removed 16 outliers)
Reward range: [7.97, 14.72], mean: 11.51
  Created 11 candidate models for data size 226
Current R2 threshold: -0.3
  rf-m: R2 = -0.063 (std: 0.208)
  rf-l: R2 = -0.020 (std: 0.213)
  gb-m: R2 = -0.117 (std: 0.217)
  gb-l: R2 = -0.117 (std: 0.216)
  xgb-m: R2 = -0.243 (std: 0.237)
  knn-m: R2 = -0.141 (std: 0.191)
  knn-tuned: R2 = -0.141 (std: 0.191)
  mlp-m: R2 = -2.085 (std: 1.282)
  svr-rbf: R2 = 0.011 (std: 0.138)
  svr-poly: R2 = 0.011 (std: 0.138)
  ridge: R2 = -0.071 (std: 0.135)

Model-based training with 10 models
Best R2: 0.011, Mean R2: -0.271
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.102 rf-l:0.107 gb-m:0.097 gb-l:0.097 xgb-m:0.085 knn-m:0.095 knn-tuned:0.095 svr-rbf:0.110 svr-poly:0.110 ridge:0.102
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9952, entropy=1.3223, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0679
  Round 1/3: Mean predicted reward = 11.634
    Using performance-based weights
    Model weights: rf-m:0.102 rf-l:0.107 gb-m:0.097 gb-l:0.097 xgb-m:0.085 knn-m:0.095 knn-tuned:0.095 svr-rbf:0.110 svr-poly:0.110 ridge:0.102
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9884, entropy=1.3146, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0645
  Round 2/3: Mean predicted reward = 11.551
    Using performance-based weights
    Model weights: rf-m:0.102 rf-l:0.107 gb-m:0.097 gb-l:0.097 xgb-m:0.085 knn-m:0.095 knn-tuned:0.095 svr-rbf:0.110 svr-poly:0.110 ridge:0.102
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9859, entropy=1.3055, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0803
  Round 3/3: Mean predicted reward = 11.597

  === Progress Analysis ===
  Status: NORMAL

--- Round 3 Results ---
  Mean Oracle Reward: 11.681
  Min Oracle Reward: 4.943
  Max Oracle Reward: 13.756
  Std Oracle Reward: 1.442
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: -0.271, Max: 0.011, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 242

======================================================================
EXPERIMENT ROUND 4/40
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
  GTACGGGATACCCGAT
  AACGGGACCGTTAGCT
  CGTCGATGCGACGAAT
  GAGCGTCATTCCAGAT
  TAGGACCTGAGCAGTC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.938
  Max reward: 16.062
  With intrinsic bonuses: 12.107

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9909, entropy=1.2963, kl_div=0.0000
    Epoch 1: policy_loss=-0.0092, value_loss=0.9908, entropy=1.2926, kl_div=0.0393
    Early stopping at epoch 2: KL divergence = 0.0754

=== Surrogate Model Training ===
Total samples: 306

Training on 287 samples (removed 19 outliers)
Reward range: [7.87, 15.07], mean: 11.61
  Created 11 candidate models for data size 287
Current R2 threshold: -0.3
  rf-m: R2 = -0.067 (std: 0.143)
  rf-l: R2 = -0.048 (std: 0.134)
  gb-m: R2 = -0.038 (std: 0.141)
  gb-l: R2 = -0.037 (std: 0.141)
  xgb-m: R2 = -0.403 (std: 0.224)
  knn-m: R2 = -0.056 (std: 0.063)
  knn-tuned: R2 = -0.056 (std: 0.063)
  mlp-m: R2 = -0.689 (std: 0.243)
  svr-rbf: R2 = 0.029 (std: 0.089)
  svr-poly: R2 = 0.029 (std: 0.089)
  ridge: R2 = -0.019 (std: 0.047)

Model-based training with 9 models
Best R2: 0.029, Mean R2: -0.123
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.107 rf-l:0.109 gb-m:0.110 gb-l:0.110 knn-m:0.108 knn-tuned:0.108 svr-rbf:0.118 svr-poly:0.118 ridge:0.112
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9874, entropy=1.2902, kl_div=0.0000
    Epoch 1: policy_loss=-0.0235, value_loss=0.9874, entropy=1.2868, kl_div=0.0289
  Round 1/3: Mean predicted reward = 11.680
    Using performance-based weights
    Model weights: rf-m:0.107 rf-l:0.109 gb-m:0.110 gb-l:0.110 knn-m:0.108 knn-tuned:0.108 svr-rbf:0.118 svr-poly:0.118 ridge:0.112
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9884, entropy=1.2825, kl_div=0.0000
    Epoch 1: policy_loss=-0.0205, value_loss=0.9884, entropy=1.2790, kl_div=0.0407
  Round 2/3: Mean predicted reward = 11.670
    Using performance-based weights
    Model weights: rf-m:0.107 rf-l:0.109 gb-m:0.110 gb-l:0.110 knn-m:0.108 knn-tuned:0.108 svr-rbf:0.118 svr-poly:0.118 ridge:0.112
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9913, entropy=1.2750, kl_div=0.0000
    Epoch 1: policy_loss=-0.0115, value_loss=0.9913, entropy=1.2716, kl_div=0.0405
  Round 3/3: Mean predicted reward = 11.853

  === Progress Analysis ===
  Status: NORMAL

--- Round 4 Results ---
  Mean Oracle Reward: 11.956
  Min Oracle Reward: 2.408
  Max Oracle Reward: 16.035
  Std Oracle Reward: 1.971
  Sequence Diversity: 1.000
  Models Used: 9
  Model R2 - Mean: -0.123, Max: 0.029, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 306

======================================================================
EXPERIMENT ROUND 5/40
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
  GTATCGAGCGACTACG
  GCAAATTGCCTGCTGA
  CATCGGATGTGACCAG
  TCTGAACATCCTGGAG
  GCGATAATGCTGCAGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.720
  Max reward: 14.914
  With intrinsic bonuses: 11.814

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9950, entropy=1.2689, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2430

=== Surrogate Model Training ===
Total samples: 370

Training on 349 samples (removed 21 outliers)
Reward range: [7.87, 15.39], mean: 11.69
  Created 14 candidate models for data size 349
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.029 (std: 0.139)
  rf-tuned-xl: R2 = -0.018 (std: 0.119)
  gb-tuned-l: R2 = -0.028 (std: 0.145)
  gb-tuned-xl: R2 = -0.029 (std: 0.144)
  xgb-xl: R2 = -0.184 (std: 0.161)
  xgb-l: R2 = -0.184 (std: 0.161)
  mlp-adaptive-xl: R2 = -0.520 (std: 0.335)
  mlp-l: R2 = -0.590 (std: 0.446)
  svr-rbf-xl: R2 = 0.064 (std: 0.104)
  svr-poly-l: R2 = 0.064 (std: 0.104)
  knn-tuned-sqrt: R2 = -0.068 (std: 0.154)
  knn-tuned-l: R2 = -0.068 (std: 0.154)
  ridge: R2 = -0.029 (std: 0.114)
  gp: R2 = -75.019 (std: 10.366)

Model-based training with 11 models
Best R2: 0.064, Mean R2: -5.474
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.092 rf-tuned-xl:0.093 gb-tuned-l:0.092 gb-tuned-xl:0.092 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.101 svr-poly-l:0.101 knn-tuned-sqrt:0.089 knn-tuned-l:0.089 ridge:0.092
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9890, entropy=1.2474, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2927
  Round 1/3: Mean predicted reward = 11.761
    Using performance-based weights
    Model weights: rf-tuned-l:0.092 rf-tuned-xl:0.093 gb-tuned-l:0.092 gb-tuned-xl:0.092 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.101 svr-poly-l:0.101 knn-tuned-sqrt:0.089 knn-tuned-l:0.089 ridge:0.092
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9877, entropy=1.2229, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3893
  Round 2/3: Mean predicted reward = 11.835
    Using performance-based weights
    Model weights: rf-tuned-l:0.092 rf-tuned-xl:0.093 gb-tuned-l:0.092 gb-tuned-xl:0.092 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.101 svr-poly-l:0.101 knn-tuned-sqrt:0.089 knn-tuned-l:0.089 ridge:0.092
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9901, entropy=1.1943, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4806
  Round 3/3: Mean predicted reward = 11.750

  === Progress Analysis ===
  Status: NORMAL

--- Round 5 Results ---
  Mean Oracle Reward: 11.730
  Min Oracle Reward: 6.213
  Max Oracle Reward: 14.803
  Std Oracle Reward: 1.710
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -5.474, Max: 0.064, Count: 14
  Total Sequences Evaluated: 370

======================================================================
EXPERIMENT ROUND 6/40
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.220
Total data collected: 370

--- Round 6 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0100
Exploration rate: 0.220

--- Generated Sequences (Diversity: 1.000) ---
  GGTATACAGGCTACCG
  AGAGGTCGCCTAATCG
  GTAAGATGCCCGCATT
  CCGAGGACAGGTTCTA
  CGCTGTAACAAGCTGG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.257
  Max reward: 14.429
  With intrinsic bonuses: 11.347

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9956, entropy=1.1620, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3353

=== Surrogate Model Training ===
Total samples: 434

Training on 408 samples (removed 26 outliers)
Reward range: [7.87, 15.39], mean: 11.71
  Created 14 candidate models for data size 408
Current R2 threshold: -0.3
  rf-tuned-l: R2 = 0.022 (std: 0.123)
  rf-tuned-xl: R2 = 0.014 (std: 0.096)
  gb-tuned-l: R2 = 0.013 (std: 0.113)
  gb-tuned-xl: R2 = 0.013 (std: 0.113)
  xgb-xl: R2 = -0.189 (std: 0.122)
  xgb-l: R2 = -0.189 (std: 0.122)
  mlp-adaptive-xl: R2 = -0.478 (std: 0.282)
  mlp-l: R2 = -0.408 (std: 0.404)
  svr-rbf-xl: R2 = 0.100 (std: 0.075)
  svr-poly-l: R2 = 0.100 (std: 0.075)
  knn-tuned-sqrt: R2 = -0.030 (std: 0.085)
  knn-tuned-l: R2 = -0.030 (std: 0.085)
  ridge: R2 = -0.000 (std: 0.085)
  gp: R2 = -73.169 (std: 14.895)

Model-based training with 11 models
Best R2: 0.100, Mean R2: -5.302
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.093 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.076 xgb-l:0.076 svr-rbf-xl:0.102 svr-poly-l:0.102 knn-tuned-sqrt:0.089 knn-tuned-l:0.089 ridge:0.092
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9915, entropy=1.1364, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3926
  Round 1/3: Mean predicted reward = 11.887
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.093 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.076 xgb-l:0.076 svr-rbf-xl:0.102 svr-poly-l:0.102 knn-tuned-sqrt:0.089 knn-tuned-l:0.089 ridge:0.092
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9911, entropy=1.1129, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4364
  Round 2/3: Mean predicted reward = 11.814
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.093 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.076 xgb-l:0.076 svr-rbf-xl:0.102 svr-poly-l:0.102 knn-tuned-sqrt:0.089 knn-tuned-l:0.089 ridge:0.092
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9901, entropy=1.0846, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5405
  Round 3/3: Mean predicted reward = 11.822

  === Progress Analysis ===
  Status: NORMAL

--- Round 6 Results ---
  Mean Oracle Reward: 11.285
  Min Oracle Reward: 0.000
  Max Oracle Reward: 14.841
  Std Oracle Reward: 2.471
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -5.302, Max: 0.100, Count: 14
  Total Sequences Evaluated: 434

======================================================================
EXPERIMENT ROUND 7/40
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.190
Total data collected: 434

--- Round 7 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0100
Exploration rate: 0.190

--- Generated Sequences (Diversity: 1.000) ---
  CGCTTAGACACGATGG
  ATGCCAGGGATCTAGC
  TCGTGGAATCTCAGAC
  TAGACAGGTCATGTCC
  CCCCTGGGATACAGTG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.260
  Max reward: 14.939
  With intrinsic bonuses: 11.340

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9954, entropy=1.0564, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3222

=== Surrogate Model Training ===
Total samples: 498

Training on 472 samples (removed 26 outliers)
Reward range: [7.73, 15.39], mean: 11.65
  Created 14 candidate models for data size 472
Current R2 threshold: -0.3
  rf-tuned-l: R2 = 0.032 (std: 0.048)
  rf-tuned-xl: R2 = 0.029 (std: 0.058)
  gb-tuned-l: R2 = 0.032 (std: 0.053)
  gb-tuned-xl: R2 = 0.032 (std: 0.053)
  xgb-xl: R2 = -0.139 (std: 0.172)
  xgb-l: R2 = -0.139 (std: 0.172)
  mlp-adaptive-xl: R2 = -0.292 (std: 0.165)
  mlp-l: R2 = -0.416 (std: 0.220)
  svr-rbf-xl: R2 = 0.095 (std: 0.032)
  svr-poly-l: R2 = 0.095 (std: 0.032)
  knn-tuned-sqrt: R2 = -0.098 (std: 0.103)
  knn-tuned-l: R2 = -0.098 (std: 0.103)
  ridge: R2 = -0.018 (std: 0.035)
  gp: R2 = -68.484 (std: 12.117)

Model-based training with 12 models
Best R2: 0.095, Mean R2: -4.955
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.089 rf-tuned-xl:0.089 gb-tuned-l:0.089 gb-tuned-xl:0.089 xgb-xl:0.075 xgb-l:0.075 mlp-adaptive-xl:0.064 svr-rbf-xl:0.095 svr-poly-l:0.095 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.085
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9932, entropy=1.0394, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3238
  Round 1/3: Mean predicted reward = 11.819
    Using performance-based weights
    Model weights: rf-tuned-l:0.089 rf-tuned-xl:0.089 gb-tuned-l:0.089 gb-tuned-xl:0.089 xgb-xl:0.075 xgb-l:0.075 mlp-adaptive-xl:0.064 svr-rbf-xl:0.095 svr-poly-l:0.095 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.085
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9920, entropy=1.0241, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3253
  Round 2/3: Mean predicted reward = 11.645
    Using performance-based weights
    Model weights: rf-tuned-l:0.089 rf-tuned-xl:0.089 gb-tuned-l:0.089 gb-tuned-xl:0.089 xgb-xl:0.075 xgb-l:0.075 mlp-adaptive-xl:0.064 svr-rbf-xl:0.095 svr-poly-l:0.095 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.085
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9942, entropy=1.0077, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3023
  Round 3/3: Mean predicted reward = 11.809

  === Progress Analysis ===
  Status: NORMAL

--- Round 7 Results ---
  Mean Oracle Reward: 11.288
  Min Oracle Reward: 7.384
  Max Oracle Reward: 14.661
  Std Oracle Reward: 1.618
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: -4.955, Max: 0.095, Count: 14
  Total Sequences Evaluated: 498

======================================================================
EXPERIMENT ROUND 8/40
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.080
Total data collected: 498

--- Round 8 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.080

--- Generated Sequences (Diversity: 1.000) ---
  GAATTCATAGTCCCGG
  TGACGTCGCGTACCGA
  AATACCCTTGTGAGCG
  TACCACGCGTTGTGAA
  CATAACGTCGGCTGTA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.408
  Max reward: 14.869
  With intrinsic bonuses: 11.419

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9938, entropy=0.9956, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1328

=== Surrogate Model Training ===
Total samples: 562

Training on 530 samples (removed 32 outliers)
Reward range: [7.73, 15.39], mean: 11.68
  Created 13 candidate models for data size 530
Current R2 threshold: -0.3
  rf-tuned-l: R2 = 0.012 (std: 0.080)
  rf-tuned-xl: R2 = 0.002 (std: 0.068)
  gb-tuned-l: R2 = 0.028 (std: 0.086)
  gb-tuned-xl: R2 = 0.028 (std: 0.086)
  xgb-xl: R2 = -0.205 (std: 0.103)
  xgb-l: R2 = -0.205 (std: 0.103)
  mlp-adaptive-xl: R2 = -0.297 (std: 0.171)
  mlp-l: R2 = -0.215 (std: 0.049)
  svr-rbf-xl: R2 = 0.086 (std: 0.079)
  svr-poly-l: R2 = 0.086 (std: 0.079)
  knn-tuned-sqrt: R2 = -0.078 (std: 0.083)
  knn-tuned-l: R2 = -0.078 (std: 0.083)
  ridge: R2 = -0.010 (std: 0.047)

Model-based training with 13 models
Best R2: 0.086, Mean R2: -0.065
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.082 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.061 mlp-l:0.066 svr-rbf-xl:0.089 svr-poly-l:0.089 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.081
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9938, entropy=0.9906, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0910
  Round 1/3: Mean predicted reward = 11.717
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.082 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.061 mlp-l:0.066 svr-rbf-xl:0.089 svr-poly-l:0.089 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.081
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9918, entropy=0.9864, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1207
  Round 2/3: Mean predicted reward = 11.774
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.082 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.061 mlp-l:0.066 svr-rbf-xl:0.089 svr-poly-l:0.089 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.081
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9898, entropy=0.9856, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1354
  Round 3/3: Mean predicted reward = 11.959

  === Progress Analysis ===
  Status: NORMAL

--- Round 8 Results ---
  Mean Oracle Reward: 11.415
  Min Oracle Reward: 4.778
  Max Oracle Reward: 15.097
  Std Oracle Reward: 1.995
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.065, Max: 0.086, Count: 13
  Total Sequences Evaluated: 562

======================================================================
EXPERIMENT ROUND 9/40
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.065
Total data collected: 562
  Performance plateaued, reducing LR to 0.000019

--- Round 9 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.065

--- Generated Sequences (Diversity: 1.000) ---
  ACCCTGCTAGGGATAG
  GCCGCAATACGTGGTA
  GGATCACCCGATCTGG
  CAAGGACCAGTTTGCG
  TCCATCGAGGCCTGGA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.164
  Max reward: 15.549
  With intrinsic bonuses: 12.157

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9880, entropy=0.9770, kl_div=0.0000
    Epoch 1: policy_loss=-0.0105, value_loss=0.9880, entropy=0.9758, kl_div=0.0305

=== Surrogate Model Training ===
Total samples: 626

Training on 589 samples (removed 37 outliers)
Reward range: [7.87, 15.39], mean: 11.75
  Created 13 candidate models for data size 589
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.023 (std: 0.068)
  rf-tuned-xl: R2 = -0.022 (std: 0.073)
  gb-tuned-l: R2 = -0.008 (std: 0.076)
  gb-tuned-xl: R2 = -0.008 (std: 0.076)
  xgb-xl: R2 = -0.195 (std: 0.104)
  xgb-l: R2 = -0.195 (std: 0.104)
  mlp-adaptive-xl: R2 = -0.198 (std: 0.147)
  mlp-l: R2 = -0.213 (std: 0.104)
  svr-rbf-xl: R2 = 0.060 (std: 0.078)
  svr-poly-l: R2 = 0.060 (std: 0.078)
  knn-tuned-sqrt: R2 = -0.095 (std: 0.112)
  knn-tuned-l: R2 = -0.095 (std: 0.112)
  ridge: R2 = -0.010 (std: 0.053)

Model-based training with 13 models
Best R2: 0.060, Mean R2: -0.072
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.068 mlp-l:0.067 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.082
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9901, entropy=0.9773, kl_div=0.0000
    Epoch 1: policy_loss=-0.0074, value_loss=0.9901, entropy=0.9758, kl_div=0.0332
  Round 1/3: Mean predicted reward = 11.903
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.068 mlp-l:0.067 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.082
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9882, entropy=0.9730, kl_div=0.0000
    Epoch 1: policy_loss=-0.0203, value_loss=0.9882, entropy=0.9713, kl_div=0.0377
  Round 2/3: Mean predicted reward = 11.924
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.068 mlp-l:0.067 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.082
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9884, entropy=0.9684, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0507
  Round 3/3: Mean predicted reward = 11.911

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 9 Results ---
  Mean Oracle Reward: 12.194
  Min Oracle Reward: 9.361
  Max Oracle Reward: 15.557
  Std Oracle Reward: 1.320
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.072, Max: 0.060, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 626

======================================================================
EXPERIMENT ROUND 10/40
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 626
  Consistent improvement, increasing LR to 0.000360

--- Round 10 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GATGCCAAGGCAGTCT
  TCCACAGCGGGCATGG
  TCGGGCCAGAACATGT
  CCGGGTACGACGCAGT
  GGCATTACAAGTGCCG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.616
  Max reward: 14.872
  With intrinsic bonuses: 11.610

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9878, entropy=0.9651, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9291

=== Surrogate Model Training ===
Total samples: 690

Training on 655 samples (removed 35 outliers)
Reward range: [7.73, 15.63], mean: 11.75
  Created 13 candidate models for data size 655
Current R2 threshold: -0.3
  rf-tuned-l: R2 = 0.035 (std: 0.119)
  rf-tuned-xl: R2 = 0.037 (std: 0.127)
  gb-tuned-l: R2 = 0.052 (std: 0.095)
  gb-tuned-xl: R2 = 0.052 (std: 0.095)
  xgb-xl: R2 = -0.145 (std: 0.139)
  xgb-l: R2 = -0.145 (std: 0.139)
  mlp-adaptive-xl: R2 = -0.134 (std: 0.233)
  mlp-l: R2 = -0.092 (std: 0.191)
  svr-rbf-xl: R2 = 0.094 (std: 0.090)
  svr-poly-l: R2 = 0.094 (std: 0.090)
  knn-tuned-sqrt: R2 = -0.082 (std: 0.138)
  knn-tuned-l: R2 = -0.082 (std: 0.138)
  ridge: R2 = -0.004 (std: 0.072)

Model-based training with 13 models
Best R2: 0.094, Mean R2: -0.025
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.082 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.069 mlp-l:0.072 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.078
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9917, entropy=0.9337, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9580
  Round 1/3: Mean predicted reward = 11.872
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.082 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.069 mlp-l:0.072 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.078
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9900, entropy=0.9031, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1138
  Round 2/3: Mean predicted reward = 11.853
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.082 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.069 mlp-l:0.072 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.078
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9928, entropy=0.8715, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1743
  Round 3/3: Mean predicted reward = 11.698

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 10 Results ---
  Mean Oracle Reward: 11.603
  Min Oracle Reward: 3.814
  Max Oracle Reward: 15.150
  Std Oracle Reward: 2.017
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.025, Max: 0.094, Count: 13
  Total Sequences Evaluated: 690

======================================================================
EXPERIMENT ROUND 11/40
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 690

--- Round 11 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCTCCCAGAGCGGGGA
  CGTTGCACGTGCGAAA
  AGCCAGGGCAATTCGT
  CAGCGCTACAATTGGG
  TATACACGAATCGGGT
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.869
  Max reward: 14.779
  With intrinsic bonuses: 11.885

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9908, entropy=0.8465, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0509

=== Surrogate Model Training ===
Total samples: 754

Training on 718 samples (removed 36 outliers)
Reward range: [7.73, 15.63], mean: 11.77
  Created 13 candidate models for data size 718
Current R2 threshold: -0.27999999999999997
  rf-tuned-l: R2 = 0.082 (std: 0.066)
  rf-tuned-xl: R2 = 0.094 (std: 0.070)
  gb-tuned-l: R2 = 0.111 (std: 0.042)
  gb-tuned-xl: R2 = 0.111 (std: 0.042)
  xgb-xl: R2 = -0.096 (std: 0.095)
  xgb-l: R2 = -0.096 (std: 0.095)
  mlp-adaptive-xl: R2 = -0.063 (std: 0.074)
  mlp-l: R2 = -0.117 (std: 0.184)
  svr-rbf-xl: R2 = 0.122 (std: 0.047)
  svr-poly-l: R2 = 0.122 (std: 0.047)
  knn-tuned-sqrt: R2 = -0.042 (std: 0.090)
  knn-tuned-l: R2 = -0.042 (std: 0.090)
  ridge: R2 = 0.023 (std: 0.032)

Model-based training with 13 models
Best R2: 0.122, Mean R2: 0.016
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.083 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.071 mlp-l:0.067 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.077
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9880, entropy=0.8183, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1688
  Round 1/3: Mean predicted reward = 11.839
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.083 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.071 mlp-l:0.067 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.077
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9871, entropy=0.7941, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.3554
  Round 2/3: Mean predicted reward = 11.796
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.083 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.071 mlp-l:0.067 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.077
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9878, entropy=0.7735, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.4261
  Round 3/3: Mean predicted reward = 11.935

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 11 Results ---
  Mean Oracle Reward: 11.897
  Min Oracle Reward: 2.084
  Max Oracle Reward: 14.701
  Std Oracle Reward: 1.903
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.016, Max: 0.122, Count: 13
  Total Sequences Evaluated: 754

======================================================================
EXPERIMENT ROUND 12/40
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 754

--- Round 12 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AGAGTCCGCCCGTGTA
  GCTAGGGCGATGCACC
  CGTGGCCAGGACGACT
  CGTAGGGCACGTTAAC
  AGGTTGTGACGCCACC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.421
  Max reward: 14.970
  With intrinsic bonuses: 12.395

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9851, entropy=0.7519, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1172

=== Surrogate Model Training ===
Total samples: 818

Training on 779 samples (removed 39 outliers)
Reward range: [7.80, 15.63], mean: 11.84
  Created 13 candidate models for data size 779
Current R2 threshold: -0.26
  rf-tuned-l: R2 = 0.070 (std: 0.068)
  rf-tuned-xl: R2 = 0.055 (std: 0.064)
  gb-tuned-l: R2 = 0.095 (std: 0.073)
  gb-tuned-xl: R2 = 0.095 (std: 0.073)
  xgb-xl: R2 = -0.136 (std: 0.128)
  xgb-l: R2 = -0.136 (std: 0.128)
  mlp-adaptive-xl: R2 = -0.142 (std: 0.077)
  mlp-l: R2 = -0.104 (std: 0.098)
  svr-rbf-xl: R2 = 0.114 (std: 0.050)
  svr-poly-l: R2 = 0.114 (std: 0.050)
  knn-tuned-sqrt: R2 = -0.067 (std: 0.067)
  knn-tuned-l: R2 = -0.067 (std: 0.067)
  ridge: R2 = 0.037 (std: 0.040)

Model-based training with 13 models
Best R2: 0.114, Mean R2: -0.005
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.081 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.067 mlp-l:0.069 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.080
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9918, entropy=0.7383, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1766
  Round 1/3: Mean predicted reward = 12.086
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.081 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.067 mlp-l:0.069 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.080
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9883, entropy=0.7205, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.3176
  Round 2/3: Mean predicted reward = 11.875
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.081 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.067 mlp-l:0.069 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.080
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9833, entropy=0.7018, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.4465
  Round 3/3: Mean predicted reward = 11.949

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 12 Results ---
  Mean Oracle Reward: 12.375
  Min Oracle Reward: 9.271
  Max Oracle Reward: 15.068
  Std Oracle Reward: 1.278
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.005, Max: 0.114, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 818

======================================================================
EXPERIMENT ROUND 13/40
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 818
  Consistent improvement, increasing LR to 0.000132

--- Round 13 Configuration ---
Learning rate: 0.000132
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGAGTCGGTGCAACCT
  GGATCACGGACCGATT
  GCGGTCCAGGCGCTAA
  TTCTAGCGCAGCGCGA
  CACGCCAAGGGTGCTG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.013
  Max reward: 15.031
  With intrinsic bonuses: 12.020

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9882, entropy=0.6933, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9436

=== Surrogate Model Training ===
Total samples: 882

Training on 837 samples (removed 45 outliers)
Reward range: [7.97, 15.39], mean: 11.88
  Created 13 candidate models for data size 837
Current R2 threshold: -0.24
  rf-tuned-l: R2 = 0.058 (std: 0.043)
  rf-tuned-xl: R2 = 0.075 (std: 0.026)
  gb-tuned-l: R2 = 0.129 (std: 0.036)
  gb-tuned-xl: R2 = 0.129 (std: 0.036)
  xgb-xl: R2 = -0.159 (std: 0.047)
  xgb-l: R2 = -0.159 (std: 0.047)
  mlp-adaptive-xl: R2 = -0.082 (std: 0.105)
  mlp-l: R2 = -0.035 (std: 0.147)
  svr-rbf-xl: R2 = 0.113 (std: 0.026)
  svr-poly-l: R2 = 0.113 (std: 0.026)
  knn-tuned-sqrt: R2 = -0.050 (std: 0.063)
  knn-tuned-l: R2 = -0.050 (std: 0.063)
  ridge: R2 = 0.032 (std: 0.034)

Model-based training with 13 models
Best R2: 0.129, Mean R2: 0.009
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.082 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.065 xgb-l:0.065 mlp-adaptive-xl:0.070 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.078
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9925, entropy=0.6778, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0378
  Round 1/3: Mean predicted reward = 11.928
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.082 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.065 xgb-l:0.065 mlp-adaptive-xl:0.070 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.078
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9866, entropy=0.6772, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9782
  Round 2/3: Mean predicted reward = 12.092
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.082 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.065 xgb-l:0.065 mlp-adaptive-xl:0.070 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.078
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9903, entropy=0.6617, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0934
  Round 3/3: Mean predicted reward = 12.013

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 13 Results ---
  Mean Oracle Reward: 11.987
  Min Oracle Reward: 5.790
  Max Oracle Reward: 15.158
  Std Oracle Reward: 1.581
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.009, Max: 0.129, Count: 13
  Total Sequences Evaluated: 882

======================================================================
EXPERIMENT ROUND 14/40
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 882

--- Round 14 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GACGGCGTACCTTGAC
  CTGCCGGATTAGCACG
  AGGTACCCCTGCGGAG
  TGGGCCCGTATGAAAC
  CCGCCACAATGGTGGG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.071
  Max reward: 16.244
  With intrinsic bonuses: 12.038

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9845, entropy=0.6471, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3238

=== Surrogate Model Training ===
Total samples: 946

Training on 897 samples (removed 49 outliers)
Reward range: [8.04, 15.39], mean: 11.89
  Created 13 candidate models for data size 897
Current R2 threshold: -0.21999999999999997
  rf-tuned-l: R2 = 0.106 (std: 0.017)
  rf-tuned-xl: R2 = 0.097 (std: 0.022)
  gb-tuned-l: R2 = 0.145 (std: 0.023)
  gb-tuned-xl: R2 = 0.145 (std: 0.023)
  xgb-xl: R2 = -0.069 (std: 0.080)
  xgb-l: R2 = -0.069 (std: 0.080)
  mlp-adaptive-xl: R2 = -0.014 (std: 0.093)
  mlp-l: R2 = 0.026 (std: 0.095)
  svr-rbf-xl: R2 = 0.144 (std: 0.041)
  svr-poly-l: R2 = 0.144 (std: 0.041)
  knn-tuned-sqrt: R2 = -0.059 (std: 0.059)
  knn-tuned-l: R2 = -0.059 (std: 0.059)
  ridge: R2 = 0.043 (std: 0.045)

Model-based training with 13 models
Best R2: 0.145, Mean R2: 0.045
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.072 mlp-l:0.075 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.069 knn-tuned-l:0.069 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9878, entropy=0.6507, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3181
  Round 1/3: Mean predicted reward = 12.035
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.072 mlp-l:0.075 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.069 knn-tuned-l:0.069 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9877, entropy=0.6512, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3262
  Round 2/3: Mean predicted reward = 12.034
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.072 mlp-l:0.075 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.069 knn-tuned-l:0.069 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9901, entropy=0.6458, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3088
  Round 3/3: Mean predicted reward = 11.968

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 14 Results ---
  Mean Oracle Reward: 12.064
  Min Oracle Reward: 6.221
  Max Oracle Reward: 16.264
  Std Oracle Reward: 1.754
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.045, Max: 0.145, Count: 13
  Total Sequences Evaluated: 946

======================================================================
EXPERIMENT ROUND 15/40
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 946

--- Round 15 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTACATGCGGGCGCAC
  GCCCACACTTGGGAGT
  GGTCAGGGCTAGCCAC
  CTGGGGCTACGCACAG
  GGAAACTCCGTGGCGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.244
  Max reward: 15.275
  With intrinsic bonuses: 12.235

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9875, entropy=0.6416, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.6568

=== Surrogate Model Training ===
Total samples: 1010

Training on 961 samples (removed 49 outliers)
Reward range: [8.04, 15.39], mean: 11.91
  Created 13 candidate models for data size 961
Current R2 threshold: -0.19999999999999998
  rf-tuned-l: R2 = 0.126 (std: 0.069)
  rf-tuned-xl: R2 = 0.119 (std: 0.065)
  gb-tuned-l: R2 = 0.177 (std: 0.043)
  gb-tuned-xl: R2 = 0.177 (std: 0.043)
  xgb-xl: R2 = -0.045 (std: 0.108)
  xgb-l: R2 = -0.045 (std: 0.108)
  mlp-adaptive-xl: R2 = 0.020 (std: 0.074)
  mlp-l: R2 = 0.014 (std: 0.105)
  svr-rbf-xl: R2 = 0.172 (std: 0.057)
  svr-poly-l: R2 = 0.172 (std: 0.057)
  knn-tuned-sqrt: R2 = 0.014 (std: 0.092)
  knn-tuned-l: R2 = 0.014 (std: 0.092)
  ridge: R2 = 0.066 (std: 0.059)

Model-based training with 13 models
Best R2: 0.177, Mean R2: 0.075
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.080 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.073 mlp-l:0.072 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9861, entropy=0.6114, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 3.0610
  Round 1/3: Mean predicted reward = 12.030
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.080 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.073 mlp-l:0.072 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9898, entropy=0.5870, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 3.2831
  Round 2/3: Mean predicted reward = 12.118
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.080 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.073 mlp-l:0.072 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9866, entropy=0.5573, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 3.6029
  Round 3/3: Mean predicted reward = 12.037

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 15 Results ---
  Mean Oracle Reward: 12.231
  Min Oracle Reward: 8.448
  Max Oracle Reward: 15.054
  Std Oracle Reward: 1.427
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.075, Max: 0.177, Count: 13
  Total Sequences Evaluated: 1010

======================================================================
EXPERIMENT ROUND 16/40
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1010
  Performance plateaued, reducing LR to 0.000136

--- Round 16 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGCGGACATGGACTCG
  AGTCCGCGCTCAGGGA
  CGCAGTCGGCAGGCAT
  GCCCGTACAGTCAGGG
  GGTGGGACTGCCCAAC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.285
  Max reward: 14.951
  With intrinsic bonuses: 12.229

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9869, entropy=0.5244, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.6771

=== Surrogate Model Training ===
Total samples: 1074

Training on 1027 samples (removed 47 outliers)
Reward range: [8.04, 15.63], mean: 11.94
  Created 13 candidate models for data size 1027
Current R2 threshold: -0.18
  rf-tuned-l: R2 = 0.123 (std: 0.075)
  rf-tuned-xl: R2 = 0.125 (std: 0.066)
  gb-tuned-l: R2 = 0.178 (std: 0.054)
  gb-tuned-xl: R2 = 0.178 (std: 0.054)
  xgb-xl: R2 = -0.027 (std: 0.086)
  xgb-l: R2 = -0.027 (std: 0.086)
  mlp-adaptive-xl: R2 = 0.028 (std: 0.131)
  mlp-l: R2 = 0.068 (std: 0.071)
  svr-rbf-xl: R2 = 0.176 (std: 0.069)
  svr-poly-l: R2 = 0.176 (std: 0.069)
  knn-tuned-sqrt: R2 = 0.027 (std: 0.088)
  knn-tuned-l: R2 = 0.027 (std: 0.088)
  ridge: R2 = 0.060 (std: 0.050)

Model-based training with 13 models
Best R2: 0.178, Mean R2: 0.086
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.072 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9896, entropy=0.5085, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.7208
  Round 1/3: Mean predicted reward = 12.099
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.072 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9882, entropy=0.4949, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.7926
  Round 2/3: Mean predicted reward = 12.099
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.072 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9870, entropy=0.4772, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.8394
  Round 3/3: Mean predicted reward = 12.094

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 16 Results ---
  Mean Oracle Reward: 12.250
  Min Oracle Reward: 8.900
  Max Oracle Reward: 15.114
  Std Oracle Reward: 1.341
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.086, Max: 0.178, Count: 13
  Total Sequences Evaluated: 1074

======================================================================
EXPERIMENT ROUND 17/40
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1074
  Performance plateaued, reducing LR to 0.000100

--- Round 17 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCCAATGGGCGCAGTG
  GGCCTGCGGACTAGAC
  GGCCGAGTAGTCGCCA
  CGACTTGAGAGCCGGC
  TAGACCGTCCGGTCGA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.882
  Max reward: 14.716
  With intrinsic bonuses: 11.897

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9891, entropy=0.4495, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.4197

=== Surrogate Model Training ===
Total samples: 1138

Training on 1090 samples (removed 48 outliers)
Reward range: [8.04, 15.63], mean: 11.94
  Created 13 candidate models for data size 1090
Current R2 threshold: -0.15999999999999998
  rf-tuned-l: R2 = 0.121 (std: 0.045)
  rf-tuned-xl: R2 = 0.118 (std: 0.031)
  gb-tuned-l: R2 = 0.191 (std: 0.054)
  gb-tuned-xl: R2 = 0.191 (std: 0.054)
  xgb-xl: R2 = -0.053 (std: 0.064)
  xgb-l: R2 = -0.053 (std: 0.064)
  mlp-adaptive-xl: R2 = 0.036 (std: 0.102)
  mlp-l: R2 = 0.054 (std: 0.103)
  svr-rbf-xl: R2 = 0.177 (std: 0.054)
  svr-poly-l: R2 = 0.177 (std: 0.054)
  knn-tuned-sqrt: R2 = 0.019 (std: 0.053)
  knn-tuned-l: R2 = 0.019 (std: 0.053)
  ridge: R2 = 0.068 (std: 0.056)

Model-based training with 13 models
Best R2: 0.191, Mean R2: 0.082
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.079 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.073 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9879, entropy=0.4403, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.3924
  Round 1/3: Mean predicted reward = 12.003
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.079 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.073 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9849, entropy=0.4181, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.4827
  Round 2/3: Mean predicted reward = 11.934
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.079 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.073 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9863, entropy=0.4148, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.4357
  Round 3/3: Mean predicted reward = 12.021

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 17 Results ---
  Mean Oracle Reward: 11.896
  Min Oracle Reward: 5.336
  Max Oracle Reward: 14.679
  Std Oracle Reward: 1.822
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.082, Max: 0.191, Count: 13
  Total Sequences Evaluated: 1138

======================================================================
EXPERIMENT ROUND 18/40
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1138

--- Round 18 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ACCTGCGCGTGAGACG
  CAGGACCCAGTGGTGC
  GACTGGGCAGCCATCG
  ACTCGGCAAGCCGTTG
  CCGAAAGCGCTTGCGG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.640
  Max reward: 14.655
  With intrinsic bonuses: 11.644

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9896, entropy=0.3951, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.2761

=== Surrogate Model Training ===
Total samples: 1202

Training on 1152 samples (removed 50 outliers)
Reward range: [8.04, 15.63], mean: 11.93
  Created 13 candidate models for data size 1152
Current R2 threshold: -0.13999999999999999
  rf-tuned-l: R2 = 0.111 (std: 0.032)
  rf-tuned-xl: R2 = 0.120 (std: 0.029)
  gb-tuned-l: R2 = 0.186 (std: 0.057)
  gb-tuned-xl: R2 = 0.186 (std: 0.057)
  xgb-xl: R2 = -0.061 (std: 0.038)
  xgb-l: R2 = -0.061 (std: 0.038)
  mlp-adaptive-xl: R2 = 0.072 (std: 0.065)
  mlp-l: R2 = 0.069 (std: 0.050)
  svr-rbf-xl: R2 = 0.191 (std: 0.045)
  svr-poly-l: R2 = 0.191 (std: 0.045)
  knn-tuned-sqrt: R2 = 0.005 (std: 0.064)
  knn-tuned-l: R2 = 0.005 (std: 0.064)
  ridge: R2 = 0.073 (std: 0.049)

Model-based training with 13 models
Best R2: 0.191, Mean R2: 0.084
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.079 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.076 mlp-l:0.076 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9891, entropy=0.3846, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.3077
  Round 1/3: Mean predicted reward = 11.933
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.079 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.076 mlp-l:0.076 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9863, entropy=0.3825, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.2203
  Round 2/3: Mean predicted reward = 11.856
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.079 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.076 mlp-l:0.076 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.076
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9882, entropy=0.3599, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.3342
  Round 3/3: Mean predicted reward = 11.880

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 18 Results ---
  Mean Oracle Reward: 11.621
  Min Oracle Reward: 5.872
  Max Oracle Reward: 14.743
  Std Oracle Reward: 1.711
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.084, Max: 0.191, Count: 13
  Total Sequences Evaluated: 1202

======================================================================
EXPERIMENT ROUND 19/40
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1202

--- Round 19 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCGAGCCATGGAGGCC
  CGCGGAGTCACCGAGT
  AGTTAGTACGCGCCAG
  GCTCTCGACGGACAGG
  GACCATGATGGGCCCG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.348
  Max reward: 14.645
  With intrinsic bonuses: 11.353

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9913, entropy=0.3468, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3474

=== Surrogate Model Training ===
Total samples: 1266

Training on 1213 samples (removed 53 outliers)
Reward range: [7.97, 15.63], mean: 11.92
  Created 13 candidate models for data size 1213
Current R2 threshold: -0.12
  rf-tuned-l: R2 = 0.129 (std: 0.030)
  rf-tuned-xl: R2 = 0.143 (std: 0.035)
  gb-tuned-l: R2 = 0.188 (std: 0.051)
  gb-tuned-xl: R2 = 0.188 (std: 0.051)
  xgb-xl: R2 = -0.052 (std: 0.034)
  xgb-l: R2 = -0.052 (std: 0.034)
  mlp-adaptive-xl: R2 = 0.079 (std: 0.017)
  mlp-l: R2 = 0.093 (std: 0.058)
  svr-rbf-xl: R2 = 0.204 (std: 0.023)
  svr-poly-l: R2 = 0.204 (std: 0.023)
  knn-tuned-sqrt: R2 = 0.017 (std: 0.032)
  knn-tuned-l: R2 = 0.017 (std: 0.032)
  ridge: R2 = 0.075 (std: 0.037)

Model-based training with 13 models
Best R2: 0.204, Mean R2: 0.095
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.075 mlp-l:0.077 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9888, entropy=0.3581, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2802
  Round 1/3: Mean predicted reward = 11.699
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.075 mlp-l:0.077 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9900, entropy=0.3578, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2687
  Round 2/3: Mean predicted reward = 11.908
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.075 mlp-l:0.077 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9883, entropy=0.3594, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2765
  Round 3/3: Mean predicted reward = 11.962

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 19 Results ---
  Mean Oracle Reward: 11.340
  Min Oracle Reward: 3.201
  Max Oracle Reward: 14.614
  Std Oracle Reward: 2.084
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.095, Max: 0.204, Count: 13
  Total Sequences Evaluated: 1266

======================================================================
EXPERIMENT ROUND 20/40
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1266

--- Round 20 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCTGGGACTGCGCCAA
  TAAGCGGCGACCGCTG
  GCGCATCCGAGGGTCA
  TGCGGCCTGACAGGAC
  ACTACGCGGGCGGCTA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.854
  Max reward: 14.817
  With intrinsic bonuses: 11.898

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9914, entropy=0.3510, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.5924

=== Surrogate Model Training ===
Total samples: 1330

Training on 1274 samples (removed 56 outliers)
Reward range: [8.04, 15.63], mean: 11.93
  Created 13 candidate models for data size 1274
Current R2 threshold: -0.09999999999999998
  rf-tuned-l: R2 = 0.139 (std: 0.025)
  rf-tuned-xl: R2 = 0.138 (std: 0.032)
  gb-tuned-l: R2 = 0.156 (std: 0.025)
  gb-tuned-xl: R2 = 0.156 (std: 0.025)
  xgb-xl: R2 = -0.035 (std: 0.043)
  xgb-l: R2 = -0.035 (std: 0.043)
  mlp-adaptive-xl: R2 = 0.088 (std: 0.054)
  mlp-l: R2 = 0.114 (std: 0.020)
  svr-rbf-xl: R2 = 0.193 (std: 0.027)
  svr-poly-l: R2 = 0.193 (std: 0.027)
  knn-tuned-sqrt: R2 = 0.023 (std: 0.034)
  knn-tuned-l: R2 = 0.023 (std: 0.034)
  ridge: R2 = 0.057 (std: 0.023)

Model-based training with 13 models
Best R2: 0.193, Mean R2: 0.093
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.076 mlp-l:0.078 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9941, entropy=0.3583, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8921
  Round 1/3: Mean predicted reward = 11.866
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.076 mlp-l:0.078 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9878, entropy=0.3636, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0500
  Round 2/3: Mean predicted reward = 11.953
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.076 mlp-l:0.078 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9852, entropy=0.3633, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1311
  Round 3/3: Mean predicted reward = 11.984

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 20 Results ---
  Mean Oracle Reward: 11.833
  Min Oracle Reward: 6.526
  Max Oracle Reward: 14.603
  Std Oracle Reward: 1.666
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.093, Max: 0.193, Count: 13
  Total Sequences Evaluated: 1330

======================================================================
EXPERIMENT ROUND 21/40
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1330

--- Round 21 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCTTACAGGGCACGCG
  CGCATACGGGTGCCGA
  CACTTTCGCAGGAGCG
  CCAAGTGCGGCGACGT
  CGGGGTACCAGATCGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.848
  Max reward: 15.413
  With intrinsic bonuses: 11.883

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9839, entropy=0.3576, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0080

=== Surrogate Model Training ===
Total samples: 1394

Training on 1336 samples (removed 58 outliers)
Reward range: [8.04, 15.63], mean: 11.93
  Created 13 candidate models for data size 1336
Current R2 threshold: -0.07999999999999999
  rf-tuned-l: R2 = 0.155 (std: 0.021)
  rf-tuned-xl: R2 = 0.159 (std: 0.017)
  gb-tuned-l: R2 = 0.191 (std: 0.015)
  gb-tuned-xl: R2 = 0.191 (std: 0.015)
  xgb-xl: R2 = 0.007 (std: 0.038)
  xgb-l: R2 = 0.007 (std: 0.038)
  mlp-adaptive-xl: R2 = 0.140 (std: 0.044)
  mlp-l: R2 = 0.130 (std: 0.059)
  svr-rbf-xl: R2 = 0.220 (std: 0.040)
  svr-poly-l: R2 = 0.220 (std: 0.040)
  knn-tuned-sqrt: R2 = 0.037 (std: 0.031)
  knn-tuned-l: R2 = 0.037 (std: 0.031)
  ridge: R2 = 0.066 (std: 0.024)

Model-based training with 13 models
Best R2: 0.220, Mean R2: 0.120
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.078 mlp-l:0.077 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9901, entropy=0.3564, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6078
  Round 1/3: Mean predicted reward = 11.986
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.078 mlp-l:0.077 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9850, entropy=0.3442, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8411
  Round 2/3: Mean predicted reward = 11.867
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.078 mlp-l:0.077 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.071 knn-tuned-l:0.071 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9869, entropy=0.3569, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8767
  Round 3/3: Mean predicted reward = 12.054

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 21 Results ---
  Mean Oracle Reward: 11.895
  Min Oracle Reward: 6.342
  Max Oracle Reward: 15.280
  Std Oracle Reward: 1.618
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.120, Max: 0.220, Count: 13
  Total Sequences Evaluated: 1394

======================================================================
EXPERIMENT ROUND 22/40
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1394

--- Round 22 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTACCGGAAGGCTGGC
  GCAGCTCGAGTGCACG
  GATTCACGCGGCGAGC
  TCGTCGGGGCAGCAAC
  GTGCGGGTTCCAAAAC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.238
  Max reward: 15.167
  With intrinsic bonuses: 12.271

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9871, entropy=0.3452, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6110

=== Surrogate Model Training ===
Total samples: 1458

Training on 1398 samples (removed 60 outliers)
Reward range: [8.02, 15.63], mean: 11.95
  Created 13 candidate models for data size 1398
Current R2 threshold: -0.06
  rf-tuned-l: R2 = 0.170 (std: 0.036)
  rf-tuned-xl: R2 = 0.165 (std: 0.027)
  gb-tuned-l: R2 = 0.193 (std: 0.027)
  gb-tuned-xl: R2 = 0.193 (std: 0.027)
  xgb-xl: R2 = 0.009 (std: 0.063)
  xgb-l: R2 = 0.009 (std: 0.063)
  mlp-adaptive-xl: R2 = 0.111 (std: 0.027)
  mlp-l: R2 = 0.140 (std: 0.041)
  svr-rbf-xl: R2 = 0.220 (std: 0.033)
  svr-poly-l: R2 = 0.220 (std: 0.033)
  knn-tuned-sqrt: R2 = 0.076 (std: 0.044)
  knn-tuned-l: R2 = 0.076 (std: 0.044)
  ridge: R2 = 0.074 (std: 0.033)

Model-based training with 13 models
Best R2: 0.220, Mean R2: 0.127
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.075 mlp-l:0.078 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9866, entropy=0.3277, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7204
  Round 1/3: Mean predicted reward = 11.969
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.075 mlp-l:0.078 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9881, entropy=0.3215, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8147
  Round 2/3: Mean predicted reward = 12.019
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.075 mlp-l:0.078 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9905, entropy=0.3175, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8384
  Round 3/3: Mean predicted reward = 12.123

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 22 Results ---
  Mean Oracle Reward: 12.251
  Min Oracle Reward: 6.336
  Max Oracle Reward: 15.332
  Std Oracle Reward: 1.746
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.127, Max: 0.220, Count: 13
  Total Sequences Evaluated: 1458

======================================================================
EXPERIMENT ROUND 23/40
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1458

--- Round 23 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCCGGATACACCGGGT
  ACGCTCGCAGCGTGGA
  TTGCGCGAGCGAACGC
  ATCAAGTCGCGGGGCC
  AAGGTCGTAGGCCCCG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.434
  Max reward: 16.210
  With intrinsic bonuses: 12.437

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9889, entropy=0.3045, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5341

=== Surrogate Model Training ===
Total samples: 1522

Training on 1462 samples (removed 60 outliers)
Reward range: [8.02, 15.81], mean: 11.97
  Created 13 candidate models for data size 1462
Current R2 threshold: -0.03999999999999998
  rf-tuned-l: R2 = 0.152 (std: 0.049)
  rf-tuned-xl: R2 = 0.147 (std: 0.045)
  gb-tuned-l: R2 = 0.189 (std: 0.023)
  gb-tuned-xl: R2 = 0.189 (std: 0.023)
  xgb-xl: R2 = 0.002 (std: 0.072)
  xgb-l: R2 = 0.002 (std: 0.072)
  mlp-adaptive-xl: R2 = 0.121 (std: 0.032)
  mlp-l: R2 = 0.134 (std: 0.045)
  svr-rbf-xl: R2 = 0.211 (std: 0.033)
  svr-poly-l: R2 = 0.211 (std: 0.033)
  knn-tuned-sqrt: R2 = 0.059 (std: 0.063)
  knn-tuned-l: R2 = 0.059 (std: 0.063)
  ridge: R2 = 0.076 (std: 0.033)

Model-based training with 13 models
Best R2: 0.211, Mean R2: 0.119
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.079 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.077 mlp-l:0.078 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9887, entropy=0.2930, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2754
  Round 1/3: Mean predicted reward = 12.006
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.079 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.077 mlp-l:0.078 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9878, entropy=0.2880, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4023
  Round 2/3: Mean predicted reward = 12.041
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.079 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.077 mlp-l:0.078 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9871, entropy=0.2861, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3568
  Round 3/3: Mean predicted reward = 12.084

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 23 Results ---
  Mean Oracle Reward: 12.433
  Min Oracle Reward: 9.170
  Max Oracle Reward: 16.050
  Std Oracle Reward: 1.543
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.119, Max: 0.211, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 1522

======================================================================
EXPERIMENT ROUND 24/40
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1522
  Consistent improvement, increasing LR to 0.000045

--- Round 24 Configuration ---
Learning rate: 0.000045
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGAGGCAGCGCTGACT
  GGAAGTCCTCTGGCCA
  CGCTGGATCAACGTCG
  TGCTAACAGGGGCCCG
  GAGTCATGACCCCGGG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.233
  Max reward: 15.144
  With intrinsic bonuses: 12.240

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9854, entropy=0.2887, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1792

=== Surrogate Model Training ===
Total samples: 1586

Training on 1524 samples (removed 62 outliers)
Reward range: [8.02, 15.81], mean: 11.99
  Created 13 candidate models for data size 1524
Current R2 threshold: -0.019999999999999962
  rf-tuned-l: R2 = 0.171 (std: 0.049)
  rf-tuned-xl: R2 = 0.170 (std: 0.051)
  gb-tuned-l: R2 = 0.204 (std: 0.035)
  gb-tuned-xl: R2 = 0.204 (std: 0.035)
  xgb-xl: R2 = 0.015 (std: 0.065)
  xgb-l: R2 = 0.015 (std: 0.065)
  mlp-adaptive-xl: R2 = 0.153 (std: 0.028)
  mlp-l: R2 = 0.113 (std: 0.028)
  svr-rbf-xl: R2 = 0.219 (std: 0.043)
  svr-poly-l: R2 = 0.219 (std: 0.043)
  knn-tuned-sqrt: R2 = 0.062 (std: 0.062)
  knn-tuned-l: R2 = 0.062 (std: 0.062)
  ridge: R2 = 0.080 (std: 0.043)

Model-based training with 13 models
Best R2: 0.219, Mean R2: 0.130
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.079 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9893, entropy=0.2661, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1233
  Round 1/3: Mean predicted reward = 11.776
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.079 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9899, entropy=0.2812, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1015
  Round 2/3: Mean predicted reward = 12.018
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.079 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9860, entropy=0.2834, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1363
  Round 3/3: Mean predicted reward = 12.163

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 24 Results ---
  Mean Oracle Reward: 12.256
  Min Oracle Reward: 5.058
  Max Oracle Reward: 15.254
  Std Oracle Reward: 1.853
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.130, Max: 0.219, Count: 13
  Total Sequences Evaluated: 1586

======================================================================
EXPERIMENT ROUND 25/40
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
  CAGGAGGTCATCGGCC
  GTACGCGGAGTCCACG
  GCAACGGGCTAGCTCG
  CCGGACGAACTGTCGG
  CGTCACCCGTGGGAAG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.383
  Max reward: 15.747
  With intrinsic bonuses: 12.374

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9880, entropy=0.2771, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5815

=== Surrogate Model Training ===
Total samples: 1650

Training on 1585 samples (removed 65 outliers)
Reward range: [8.14, 15.81], mean: 12.02
  Created 13 candidate models for data size 1585
Current R2 threshold: 0.0
  rf-tuned-l: R2 = 0.147 (std: 0.040)
  rf-tuned-xl: R2 = 0.144 (std: 0.052)
  gb-tuned-l: R2 = 0.193 (std: 0.044)
  gb-tuned-xl: R2 = 0.193 (std: 0.044)
  xgb-xl: R2 = 0.017 (std: 0.086)
  xgb-l: R2 = 0.017 (std: 0.086)
  mlp-adaptive-xl: R2 = 0.140 (std: 0.018)
  mlp-l: R2 = 0.138 (std: 0.037)
  svr-rbf-xl: R2 = 0.209 (std: 0.048)
  svr-poly-l: R2 = 0.209 (std: 0.048)
  knn-tuned-sqrt: R2 = 0.034 (std: 0.088)
  knn-tuned-l: R2 = 0.034 (std: 0.088)
  ridge: R2 = 0.070 (std: 0.054)

Model-based training with 13 models
Best R2: 0.209, Mean R2: 0.119
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.079 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.078 mlp-l:0.078 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9895, entropy=0.2748, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3206
  Round 1/3: Mean predicted reward = 11.866
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.079 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.078 mlp-l:0.078 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9897, entropy=0.2741, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2238
  Round 2/3: Mean predicted reward = 12.055
    Using performance-based weights
    Model weights: rf-tuned-l:0.079 rf-tuned-xl:0.079 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.078 mlp-l:0.078 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.070 knn-tuned-l:0.070 ridge:0.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9883, entropy=0.2453, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4204
  Round 3/3: Mean predicted reward = 12.029

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 25 Results ---
  Mean Oracle Reward: 12.386
  Min Oracle Reward: 6.579
  Max Oracle Reward: 15.903
  Std Oracle Reward: 1.801
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.119, Max: 0.209, Count: 13
  Total Sequences Evaluated: 1650

======================================================================
EXPERIMENT ROUND 26/40
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
  TGCGAGCCGGCGTACA
  CACGAGTGCACGGGCT
  CGTGATGGACCACCGG
  CATAGGGCGTCGCGAC
  ATGGACCGGAGGCCTC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.344
  Max reward: 15.813
  With intrinsic bonuses: 12.337

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9879, entropy=0.2506, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3974

=== Surrogate Model Training ===
Total samples: 1714

Training on 1643 samples (removed 71 outliers)
Reward range: [8.16, 15.71], mean: 12.03
  Created 13 candidate models for data size 1643
Current R2 threshold: 0.020000000000000018
  rf-tuned-l: R2 = 0.132 (std: 0.030)
  rf-tuned-xl: R2 = 0.139 (std: 0.037)
  gb-tuned-l: R2 = 0.191 (std: 0.051)
  gb-tuned-xl: R2 = 0.191 (std: 0.051)
  xgb-xl: R2 = -0.002 (std: 0.062)
  xgb-l: R2 = -0.002 (std: 0.062)
  mlp-adaptive-xl: R2 = 0.138 (std: 0.061)
  mlp-l: R2 = 0.110 (std: 0.035)
  svr-rbf-xl: R2 = 0.201 (std: 0.050)
  svr-poly-l: R2 = 0.201 (std: 0.050)
  knn-tuned-sqrt: R2 = 0.028 (std: 0.068)
  knn-tuned-l: R2 = 0.028 (std: 0.068)
  ridge: R2 = 0.064 (std: 0.050)

Model-based training with 11 models
Best R2: 0.201, Mean R2: 0.109
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.091 rf-tuned-xl:0.092 gb-tuned-l:0.096 gb-tuned-xl:0.096 mlp-adaptive-xl:0.092 mlp-l:0.089 svr-rbf-xl:0.097 svr-poly-l:0.097 knn-tuned-sqrt:0.082 knn-tuned-l:0.082 ridge:0.085
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9891, entropy=0.2561, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1553
  Round 1/3: Mean predicted reward = 12.015
    Using performance-based weights
    Model weights: rf-tuned-l:0.091 rf-tuned-xl:0.092 gb-tuned-l:0.096 gb-tuned-xl:0.096 mlp-adaptive-xl:0.092 mlp-l:0.089 svr-rbf-xl:0.097 svr-poly-l:0.097 knn-tuned-sqrt:0.082 knn-tuned-l:0.082 ridge:0.085
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9894, entropy=0.2664, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1696
  Round 2/3: Mean predicted reward = 11.963
    Using performance-based weights
    Model weights: rf-tuned-l:0.091 rf-tuned-xl:0.092 gb-tuned-l:0.096 gb-tuned-xl:0.096 mlp-adaptive-xl:0.092 mlp-l:0.089 svr-rbf-xl:0.097 svr-poly-l:0.097 knn-tuned-sqrt:0.082 knn-tuned-l:0.082 ridge:0.085
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9872, entropy=0.2551, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2371
  Round 3/3: Mean predicted reward = 12.141

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 26 Results ---
  Mean Oracle Reward: 12.318
  Min Oracle Reward: 8.071
  Max Oracle Reward: 15.797
  Std Oracle Reward: 1.493
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: 0.109, Max: 0.201, Count: 13
  Total Sequences Evaluated: 1714

======================================================================
EXPERIMENT ROUND 27/40
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
  CGAGGATTCCCGGGAC
  GCGGGAAGTCACGCCT
  CGCCTCGCAGAGGTGA
  ACGTTGCCAGCGGGAC
  GGTGGCCACCTCGAGA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.203
  Max reward: 17.154
  With intrinsic bonuses: 12.184

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9859, entropy=0.2396, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2929

=== Surrogate Model Training ===
Total samples: 1778

Training on 1701 samples (removed 77 outliers)
Reward range: [8.19, 15.71], mean: 12.04
  Created 13 candidate models for data size 1701
Current R2 threshold: 0.040000000000000036
  rf-tuned-l: R2 = 0.132 (std: 0.059)
  rf-tuned-xl: R2 = 0.143 (std: 0.049)
  gb-tuned-l: R2 = 0.191 (std: 0.058)
  gb-tuned-xl: R2 = 0.191 (std: 0.058)
  xgb-xl: R2 = -0.003 (std: 0.102)
  xgb-l: R2 = -0.003 (std: 0.102)
  mlp-adaptive-xl: R2 = 0.112 (std: 0.046)
  mlp-l: R2 = 0.129 (std: 0.049)
  svr-rbf-xl: R2 = 0.204 (std: 0.061)
  svr-poly-l: R2 = 0.204 (std: 0.061)
  knn-tuned-sqrt: R2 = 0.029 (std: 0.072)
  knn-tuned-l: R2 = 0.029 (std: 0.072)
  ridge: R2 = 0.078 (std: 0.048)

Model-based training with 9 models
Best R2: 0.204, Mean R2: 0.110
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.109 rf-tuned-xl:0.110 gb-tuned-l:0.115 gb-tuned-xl:0.115 mlp-adaptive-xl:0.106 mlp-l:0.108 svr-rbf-xl:0.117 svr-poly-l:0.117 ridge:0.103
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9907, entropy=0.2399, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1575
  Round 1/3: Mean predicted reward = 11.842
    Using performance-based weights
    Model weights: rf-tuned-l:0.109 rf-tuned-xl:0.110 gb-tuned-l:0.115 gb-tuned-xl:0.115 mlp-adaptive-xl:0.106 mlp-l:0.108 svr-rbf-xl:0.117 svr-poly-l:0.117 ridge:0.103
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9874, entropy=0.2530, kl_div=0.0000
    Epoch 1: policy_loss=-0.0509, value_loss=0.9874, entropy=0.2526, kl_div=-0.0781
  Round 2/3: Mean predicted reward = 11.871
    Using performance-based weights
    Model weights: rf-tuned-l:0.109 rf-tuned-xl:0.110 gb-tuned-l:0.115 gb-tuned-xl:0.115 mlp-adaptive-xl:0.106 mlp-l:0.108 svr-rbf-xl:0.117 svr-poly-l:0.117 ridge:0.103
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9874, entropy=0.2377, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1793
  Round 3/3: Mean predicted reward = 12.050

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 27 Results ---
  Mean Oracle Reward: 12.205
  Min Oracle Reward: 7.240
  Max Oracle Reward: 17.356
  Std Oracle Reward: 1.760
  Sequence Diversity: 1.000
  Models Used: 9
  Model R2 - Mean: 0.110, Max: 0.204, Count: 13
  Total Sequences Evaluated: 1778

======================================================================
EXPERIMENT ROUND 28/40
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
  CTGATACGGCGCACGG
  GCTAGGGGCATGACCC
  AGTCTGGGCGCACAGC
  GAGTCCGATGCGGCAC
  ATCGCGTCGGGCAACG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.377
  Max reward: 16.824
  With intrinsic bonuses: 12.397

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9843, entropy=0.2513, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1147

=== Surrogate Model Training ===
Total samples: 1842

Training on 1764 samples (removed 78 outliers)
Reward range: [8.19, 15.81], mean: 12.06
  Created 13 candidate models for data size 1764
Current R2 threshold: 0.06
  rf-tuned-l: R2 = 0.144 (std: 0.037)
  rf-tuned-xl: R2 = 0.143 (std: 0.039)
  gb-tuned-l: R2 = 0.199 (std: 0.057)
  gb-tuned-xl: R2 = 0.199 (std: 0.057)
  xgb-xl: R2 = 0.010 (std: 0.084)
  xgb-l: R2 = 0.010 (std: 0.084)
  mlp-adaptive-xl: R2 = 0.127 (std: 0.071)
  mlp-l: R2 = 0.128 (std: 0.062)
  svr-rbf-xl: R2 = 0.225 (std: 0.055)
  svr-poly-l: R2 = 0.225 (std: 0.055)
  knn-tuned-sqrt: R2 = 0.076 (std: 0.071)
  knn-tuned-l: R2 = 0.076 (std: 0.071)
  ridge: R2 = 0.084 (std: 0.044)

Model-based training with 11 models
Best R2: 0.225, Mean R2: 0.127
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.090 rf-tuned-xl:0.090 gb-tuned-l:0.096 gb-tuned-xl:0.096 mlp-adaptive-xl:0.089 mlp-l:0.089 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.084 knn-tuned-l:0.084 ridge:0.085
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9920, entropy=0.2377, kl_div=0.0000
    Epoch 1: policy_loss=0.0006, value_loss=0.9920, entropy=0.2369, kl_div=0.0353
  Round 1/3: Mean predicted reward = 11.779
    Using performance-based weights
    Model weights: rf-tuned-l:0.090 rf-tuned-xl:0.090 gb-tuned-l:0.096 gb-tuned-xl:0.096 mlp-adaptive-xl:0.089 mlp-l:0.089 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.084 knn-tuned-l:0.084 ridge:0.085
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9878, entropy=0.2413, kl_div=0.0000
    Epoch 1: policy_loss=-0.0374, value_loss=0.9877, entropy=0.2418, kl_div=-0.1321
  Round 2/3: Mean predicted reward = 11.956
    Using performance-based weights
    Model weights: rf-tuned-l:0.090 rf-tuned-xl:0.090 gb-tuned-l:0.096 gb-tuned-xl:0.096 mlp-adaptive-xl:0.089 mlp-l:0.089 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.084 knn-tuned-l:0.084 ridge:0.085
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9888, entropy=0.2532, kl_div=0.0000
    Epoch 1: policy_loss=-0.0345, value_loss=0.9888, entropy=0.2526, kl_div=0.0212
  Round 3/3: Mean predicted reward = 12.159

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 28 Results ---
  Mean Oracle Reward: 12.383
  Min Oracle Reward: 0.000
  Max Oracle Reward: 16.745
  Std Oracle Reward: 2.248
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: 0.127, Max: 0.225, Count: 13
  Total Sequences Evaluated: 1842

======================================================================
EXPERIMENT ROUND 29/40
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1842
  Performance plateaued, reducing LR to 0.000019

--- Round 29 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  GACCCTACGTGGAGCG
  CCCCGGGAAGTTCAGG
  GCGCTTGCCCAAAGGG
  GAGTACGTACGCCCGG
  CCACTGGGCAGACTGG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.232
  Max reward: 15.822
  With intrinsic bonuses: 12.244

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9867, entropy=0.2388, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0550

=== Surrogate Model Training ===
Total samples: 1906

Training on 1827 samples (removed 79 outliers)
Reward range: [8.19, 15.81], mean: 12.07
  Created 13 candidate models for data size 1827
Current R2 threshold: 0.08000000000000002
  rf-tuned-l: R2 = 0.136 (std: 0.050)
  rf-tuned-xl: R2 = 0.139 (std: 0.050)
  gb-tuned-l: R2 = 0.200 (std: 0.056)
  gb-tuned-xl: R2 = 0.200 (std: 0.056)
  xgb-xl: R2 = -0.010 (std: 0.064)
  xgb-l: R2 = -0.010 (std: 0.064)
  mlp-adaptive-xl: R2 = 0.157 (std: 0.066)
  mlp-l: R2 = 0.139 (std: 0.059)
  svr-rbf-xl: R2 = 0.221 (std: 0.059)
  svr-poly-l: R2 = 0.221 (std: 0.059)
  knn-tuned-sqrt: R2 = 0.057 (std: 0.082)
  knn-tuned-l: R2 = 0.057 (std: 0.082)
  ridge: R2 = 0.084 (std: 0.064)

Model-based training with 9 models
Best R2: 0.221, Mean R2: 0.122
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.108 rf-tuned-xl:0.108 gb-tuned-l:0.115 gb-tuned-xl:0.115 mlp-adaptive-xl:0.110 mlp-l:0.108 svr-rbf-xl:0.117 svr-poly-l:0.117 ridge:0.102
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9904, entropy=0.2251, kl_div=0.0000
    Epoch 1: policy_loss=-0.0018, value_loss=0.9904, entropy=0.2248, kl_div=0.0255
  Round 1/3: Mean predicted reward = 11.688
    Using performance-based weights
    Model weights: rf-tuned-l:0.108 rf-tuned-xl:0.108 gb-tuned-l:0.115 gb-tuned-xl:0.115 mlp-adaptive-xl:0.110 mlp-l:0.108 svr-rbf-xl:0.117 svr-poly-l:0.117 ridge:0.102
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9879, entropy=0.2431, kl_div=0.0000
    Epoch 1: policy_loss=-0.0225, value_loss=0.9879, entropy=0.2432, kl_div=-0.0393
  Round 2/3: Mean predicted reward = 11.961
    Using performance-based weights
    Model weights: rf-tuned-l:0.108 rf-tuned-xl:0.108 gb-tuned-l:0.115 gb-tuned-xl:0.115 mlp-adaptive-xl:0.110 mlp-l:0.108 svr-rbf-xl:0.117 svr-poly-l:0.117 ridge:0.102
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9860, entropy=0.2269, kl_div=0.0000
    Epoch 1: policy_loss=-0.0111, value_loss=0.9860, entropy=0.2268, kl_div=-0.0330
  Round 3/3: Mean predicted reward = 12.135

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 29 Results ---
  Mean Oracle Reward: 12.211
  Min Oracle Reward: 2.792
  Max Oracle Reward: 15.783
  Std Oracle Reward: 1.781
  Sequence Diversity: 0.984
  Models Used: 9
  Model R2 - Mean: 0.122, Max: 0.221, Count: 13
  Total Sequences Evaluated: 1906

======================================================================
EXPERIMENT ROUND 30/40
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1906
  Performance plateaued, reducing LR to 0.000150

--- Round 30 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  ACCCGGGAGGCTTGAC
  TGGCCGGGACCGAATC
  CAGCGGGGAATCGCCT
  AGGGACTGGATCGCCC
  AAGGCGGCGACCTTGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.795
  Max reward: 15.018
  With intrinsic bonuses: 11.809

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9870, entropy=0.2407, kl_div=0.0000
    Epoch 1: policy_loss=0.0676, value_loss=0.9870, entropy=0.2407, kl_div=-0.3870

=== Surrogate Model Training ===
Total samples: 1970

Training on 1891 samples (removed 79 outliers)
Reward range: [8.15, 15.81], mean: 12.07
  Created 13 candidate models for data size 1891
Current R2 threshold: 0.10000000000000003
  rf-tuned-l: R2 = 0.137 (std: 0.026)
  rf-tuned-xl: R2 = 0.138 (std: 0.030)
  gb-tuned-l: R2 = 0.208 (std: 0.028)
  gb-tuned-xl: R2 = 0.208 (std: 0.028)
  xgb-xl: R2 = 0.010 (std: 0.058)
  xgb-l: R2 = 0.010 (std: 0.058)
  mlp-adaptive-xl: R2 = 0.182 (std: 0.040)
  mlp-l: R2 = 0.167 (std: 0.041)
  svr-rbf-xl: R2 = 0.226 (std: 0.029)
  svr-poly-l: R2 = 0.226 (std: 0.029)
  knn-tuned-sqrt: R2 = 0.047 (std: 0.050)
  knn-tuned-l: R2 = 0.047 (std: 0.050)
  ridge: R2 = 0.091 (std: 0.043)

Model-based training with 8 models
Best R2: 0.226, Mean R2: 0.131
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.119 rf-tuned-xl:0.119 gb-tuned-l:0.128 gb-tuned-xl:0.128 mlp-adaptive-xl:0.124 mlp-l:0.122 svr-rbf-xl:0.130 svr-poly-l:0.130
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9907, entropy=0.2371, kl_div=0.0000
    Epoch 1: policy_loss=-0.0757, value_loss=0.9906, entropy=0.2370, kl_div=-0.3388
  Round 1/3: Mean predicted reward = 11.523
    Using performance-based weights
    Model weights: rf-tuned-l:0.119 rf-tuned-xl:0.119 gb-tuned-l:0.128 gb-tuned-xl:0.128 mlp-adaptive-xl:0.124 mlp-l:0.122 svr-rbf-xl:0.130 svr-poly-l:0.130
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9897, entropy=0.2494, kl_div=0.0000
    Epoch 1: policy_loss=-0.0370, value_loss=0.9897, entropy=0.2483, kl_div=-0.2947
  Round 2/3: Mean predicted reward = 11.844
    Using performance-based weights
    Model weights: rf-tuned-l:0.119 rf-tuned-xl:0.119 gb-tuned-l:0.128 gb-tuned-xl:0.128 mlp-adaptive-xl:0.124 mlp-l:0.122 svr-rbf-xl:0.130 svr-poly-l:0.130
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9877, entropy=0.2410, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1006
  Round 3/3: Mean predicted reward = 12.102

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 30 Results ---
  Mean Oracle Reward: 11.805
  Min Oracle Reward: 5.108
  Max Oracle Reward: 14.921
  Std Oracle Reward: 1.782
  Sequence Diversity: 0.984
  Models Used: 8
  Model R2 - Mean: 0.131, Max: 0.226, Count: 13
  Total Sequences Evaluated: 1970

======================================================================
EXPERIMENT ROUND 31/40
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1970

--- Round 31 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  ACGCGACCTAGCGGGT
  GATGTGAAGCCGCGCC
  AACCGGGGACTCTGGC
  GCGGCGAATGGCCTAC
  ACAGGCGCGCTGGACT
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.685
  Max reward: 14.271
  With intrinsic bonuses: 11.691

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9860, entropy=0.2521, kl_div=0.0000
    Epoch 1: policy_loss=-0.0313, value_loss=0.9860, entropy=0.2478, kl_div=-0.1700

=== Surrogate Model Training ===
Total samples: 2034

Training on 1951 samples (removed 83 outliers)
Reward range: [8.15, 15.81], mean: 12.06
  Created 13 candidate models for data size 1951
Current R2 threshold: 0.12
  rf-tuned-l: R2 = 0.153 (std: 0.032)
  rf-tuned-xl: R2 = 0.160 (std: 0.036)
  gb-tuned-l: R2 = 0.201 (std: 0.021)
  gb-tuned-xl: R2 = 0.201 (std: 0.021)
  xgb-xl: R2 = 0.036 (std: 0.070)
  xgb-l: R2 = 0.036 (std: 0.070)
  mlp-adaptive-xl: R2 = 0.156 (std: 0.036)
  mlp-l: R2 = 0.147 (std: 0.038)
  svr-rbf-xl: R2 = 0.224 (std: 0.040)
  svr-poly-l: R2 = 0.224 (std: 0.040)
  knn-tuned-sqrt: R2 = 0.064 (std: 0.083)
  knn-tuned-l: R2 = 0.064 (std: 0.083)
  ridge: R2 = 0.092 (std: 0.027)

Model-based training with 8 models
Best R2: 0.224, Mean R2: 0.135
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.121 rf-tuned-xl:0.122 gb-tuned-l:0.127 gb-tuned-xl:0.127 mlp-adaptive-xl:0.122 mlp-l:0.121 svr-rbf-xl:0.130 svr-poly-l:0.130
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9907, entropy=0.2480, kl_div=0.0000
    Epoch 1: policy_loss=-0.0150, value_loss=0.9907, entropy=0.2452, kl_div=-0.1778
  Round 1/3: Mean predicted reward = 11.633
    Using performance-based weights
    Model weights: rf-tuned-l:0.121 rf-tuned-xl:0.122 gb-tuned-l:0.127 gb-tuned-xl:0.127 mlp-adaptive-xl:0.122 mlp-l:0.121 svr-rbf-xl:0.130 svr-poly-l:0.130
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9889, entropy=0.2333, kl_div=0.0000
    Epoch 1: policy_loss=0.2852, value_loss=0.9889, entropy=0.2317, kl_div=-0.8503
  Round 2/3: Mean predicted reward = 11.773
    Using performance-based weights
    Model weights: rf-tuned-l:0.121 rf-tuned-xl:0.122 gb-tuned-l:0.127 gb-tuned-xl:0.127 mlp-adaptive-xl:0.122 mlp-l:0.121 svr-rbf-xl:0.130 svr-poly-l:0.130
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9865, entropy=0.2212, kl_div=0.0000
    Epoch 1: policy_loss=-0.0252, value_loss=0.9865, entropy=0.2198, kl_div=-0.1038
  Round 3/3: Mean predicted reward = 12.043

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 31 Results ---
  Mean Oracle Reward: 11.686
  Min Oracle Reward: 5.473
  Max Oracle Reward: 14.529
  Std Oracle Reward: 1.930
  Sequence Diversity: 0.969
  Models Used: 8
  Model R2 - Mean: 0.135, Max: 0.224, Count: 13
  Total Sequences Evaluated: 2034

======================================================================
EXPERIMENT ROUND 32/40
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2034

--- Round 32 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCAGGGGGTACCCAGT
  GGCGGCAACGCACTTG
  CAGTGGTCCAGCTAGC
  GACGCACGACCGGGTT
  GTGGACCTAACGCGGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.121
  Max reward: 14.766
  With intrinsic bonuses: 12.118

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9866, entropy=0.2152, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1612

=== Surrogate Model Training ===
Total samples: 2098

Training on 2010 samples (removed 88 outliers)
Reward range: [8.19, 15.81], mean: 12.08
  Created 13 candidate models for data size 2010
Current R2 threshold: 0.14
  rf-tuned-l: R2 = 0.145 (std: 0.051)
  rf-tuned-xl: R2 = 0.151 (std: 0.050)
  gb-tuned-l: R2 = 0.199 (std: 0.029)
  gb-tuned-xl: R2 = 0.199 (std: 0.029)
  xgb-xl: R2 = 0.006 (std: 0.094)
  xgb-l: R2 = 0.006 (std: 0.094)
  mlp-adaptive-xl: R2 = 0.132 (std: 0.068)
  mlp-l: R2 = 0.150 (std: 0.045)
  svr-rbf-xl: R2 = 0.222 (std: 0.053)
  svr-poly-l: R2 = 0.222 (std: 0.053)
  knn-tuned-sqrt: R2 = 0.073 (std: 0.086)
  knn-tuned-l: R2 = 0.073 (std: 0.086)
  ridge: R2 = 0.088 (std: 0.021)

Model-based training with 7 models
Best R2: 0.222, Mean R2: 0.128
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.137 rf-tuned-xl:0.138 gb-tuned-l:0.145 gb-tuned-xl:0.145 mlp-l:0.138 svr-rbf-xl:0.148 svr-poly-l:0.148
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9892, entropy=0.2262, kl_div=0.0000
    Epoch 1: policy_loss=-0.0177, value_loss=0.9892, entropy=0.2256, kl_div=-0.2214
  Round 1/3: Mean predicted reward = 11.606
    Using performance-based weights
    Model weights: rf-tuned-l:0.137 rf-tuned-xl:0.138 gb-tuned-l:0.145 gb-tuned-xl:0.145 mlp-l:0.138 svr-rbf-xl:0.148 svr-poly-l:0.148
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9903, entropy=0.2451, kl_div=0.0000
    Epoch 1: policy_loss=-0.0252, value_loss=0.9902, entropy=0.2462, kl_div=-0.3090
  Round 2/3: Mean predicted reward = 11.601
    Using performance-based weights
    Model weights: rf-tuned-l:0.137 rf-tuned-xl:0.138 gb-tuned-l:0.145 gb-tuned-xl:0.145 mlp-l:0.138 svr-rbf-xl:0.148 svr-poly-l:0.148
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9892, entropy=0.2261, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2099
  Round 3/3: Mean predicted reward = 11.969

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 32 Results ---
  Mean Oracle Reward: 12.172
  Min Oracle Reward: 7.200
  Max Oracle Reward: 14.509
  Std Oracle Reward: 1.537
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: 0.128, Max: 0.222, Count: 13
  Total Sequences Evaluated: 2098

======================================================================
EXPERIMENT ROUND 33/40
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2098

--- Round 33 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  GGCAAGTGCGCTCCAG
  CACCTGGTAGCCGGAG
  AGGCCACGGCATTGCG
  ACTGACCGGGCGGTCA
  GGGCCTATGACGACGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.122
  Max reward: 15.432
  With intrinsic bonuses: 12.152

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9870, entropy=0.2216, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2280

=== Surrogate Model Training ===
Total samples: 2162

Training on 2068 samples (removed 94 outliers)
Reward range: [8.23, 15.81], mean: 12.09
  Created 13 candidate models for data size 2068
Current R2 threshold: 0.16000000000000003
  rf-tuned-l: R2 = 0.143 (std: 0.039)
  rf-tuned-xl: R2 = 0.146 (std: 0.046)
  gb-tuned-l: R2 = 0.195 (std: 0.030)
  gb-tuned-xl: R2 = 0.195 (std: 0.030)
  xgb-xl: R2 = 0.022 (std: 0.082)
  xgb-l: R2 = 0.022 (std: 0.082)
  mlp-adaptive-xl: R2 = 0.144 (std: 0.047)
  mlp-l: R2 = 0.119 (std: 0.059)
  svr-rbf-xl: R2 = 0.220 (std: 0.048)
  svr-poly-l: R2 = 0.220 (std: 0.048)
  knn-tuned-sqrt: R2 = 0.055 (std: 0.083)
  knn-tuned-l: R2 = 0.055 (std: 0.083)
  ridge: R2 = 0.087 (std: 0.016)

Model-based training with 4 models
Best R2: 0.220, Mean R2: 0.125
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: gb-tuned-l:0.247 gb-tuned-xl:0.247 svr-rbf-xl:0.253 svr-poly-l:0.253
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9908, entropy=0.2207, kl_div=0.0000
    Epoch 1: policy_loss=-0.0334, value_loss=0.9908, entropy=0.2209, kl_div=-0.0006
  Round 1/3: Mean predicted reward = 11.489
    Using performance-based weights
    Model weights: gb-tuned-l:0.247 gb-tuned-xl:0.247 svr-rbf-xl:0.253 svr-poly-l:0.253
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9902, entropy=0.2304, kl_div=0.0000
    Epoch 1: policy_loss=-0.0356, value_loss=0.9902, entropy=0.2325, kl_div=-0.4160
  Round 2/3: Mean predicted reward = 11.645
    Using performance-based weights
    Model weights: gb-tuned-l:0.247 gb-tuned-xl:0.247 svr-rbf-xl:0.253 svr-poly-l:0.253
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9864, entropy=0.2277, kl_div=0.0000
    Epoch 1: policy_loss=0.0014, value_loss=0.9864, entropy=0.2286, kl_div=-0.2296
  Round 3/3: Mean predicted reward = 11.882

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 33 Results ---
  Mean Oracle Reward: 12.116
  Min Oracle Reward: 6.757
  Max Oracle Reward: 15.755
  Std Oracle Reward: 1.780
  Sequence Diversity: 0.984
  Models Used: 4
  Model R2 - Mean: 0.125, Max: 0.220, Count: 13
  Total Sequences Evaluated: 2162

======================================================================
EXPERIMENT ROUND 34/40
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
  CCGACACTTAGGCGGG
  CCGGGAAGCTGGCTCA
  GTCCACGGGGTACACG
  CAGGAGGTCCGACCGT
  CCCCGAGCGAGGTTAG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.943
  Max reward: 15.179
  With intrinsic bonuses: 11.984

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9873, entropy=0.2290, kl_div=0.0000
    Epoch 1: policy_loss=-0.0188, value_loss=0.9873, entropy=0.2292, kl_div=-0.0357

=== Surrogate Model Training ===
Total samples: 2226

Training on 2132 samples (removed 94 outliers)
Reward range: [8.20, 15.81], mean: 12.09
  Created 13 candidate models for data size 2132
Current R2 threshold: 0.18
  rf-tuned-l: R2 = 0.142 (std: 0.040)
  rf-tuned-xl: R2 = 0.136 (std: 0.041)
  gb-tuned-l: R2 = 0.186 (std: 0.035)
  gb-tuned-xl: R2 = 0.186 (std: 0.035)
  xgb-xl: R2 = 0.026 (std: 0.053)
  xgb-l: R2 = 0.026 (std: 0.053)
  mlp-adaptive-xl: R2 = 0.146 (std: 0.053)
  mlp-l: R2 = 0.161 (std: 0.050)
  svr-rbf-xl: R2 = 0.214 (std: 0.052)
  svr-poly-l: R2 = 0.214 (std: 0.052)
  knn-tuned-sqrt: R2 = 0.041 (std: 0.071)
  knn-tuned-l: R2 = 0.041 (std: 0.071)
  ridge: R2 = 0.082 (std: 0.024)

Model-based training with 4 models
Best R2: 0.214, Mean R2: 0.123
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: gb-tuned-l:0.246 gb-tuned-xl:0.246 svr-rbf-xl:0.254 svr-poly-l:0.254
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9906, entropy=0.2394, kl_div=0.0000
    Epoch 1: policy_loss=-0.0720, value_loss=0.9905, entropy=0.2402, kl_div=-0.1491
  Round 1/3: Mean predicted reward = 11.240
    Using performance-based weights
    Model weights: gb-tuned-l:0.246 gb-tuned-xl:0.246 svr-rbf-xl:0.254 svr-poly-l:0.254
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9905, entropy=0.2489, kl_div=0.0000
    Epoch 1: policy_loss=-0.0463, value_loss=0.9905, entropy=0.2503, kl_div=-0.2546
  Round 2/3: Mean predicted reward = 11.597
    Using performance-based weights
    Model weights: gb-tuned-l:0.246 gb-tuned-xl:0.246 svr-rbf-xl:0.254 svr-poly-l:0.254
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9871, entropy=0.2290, kl_div=0.0000
    Epoch 1: policy_loss=-0.0099, value_loss=0.9871, entropy=0.2301, kl_div=-0.1488
  Round 3/3: Mean predicted reward = 11.804

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 34 Results ---
  Mean Oracle Reward: 11.970
  Min Oracle Reward: 5.859
  Max Oracle Reward: 15.620
  Std Oracle Reward: 1.723
  Sequence Diversity: 0.984
  Models Used: 4
  Model R2 - Mean: 0.123, Max: 0.214, Count: 13
  Total Sequences Evaluated: 2226

======================================================================
EXPERIMENT ROUND 35/40
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2226
  Performance plateaued, reducing LR to 0.000150

--- Round 35 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  CCGGGGAGTACCTGAC
  CGCCGGAAATCCTGGG
  GGTACTAGCGGACCGC
  CCCCTGGGCAAAGGGT
  CCATGGCATAGGCCGG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.943
  Max reward: 16.315
  With intrinsic bonuses: 11.925

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9860, entropy=0.2433, kl_div=0.0000
    Epoch 1: policy_loss=-0.0364, value_loss=0.9860, entropy=0.2450, kl_div=-0.0345

=== Surrogate Model Training ===
Total samples: 2290

Training on 2195 samples (removed 95 outliers)
Reward range: [8.19, 15.81], mean: 12.08
  Created 13 candidate models for data size 2195
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.140 (std: 0.050)
  rf-tuned-xl: R2 = 0.137 (std: 0.052)
  gb-tuned-l: R2 = 0.184 (std: 0.048)
  gb-tuned-xl: R2 = 0.184 (std: 0.048)
  xgb-xl: R2 = 0.032 (std: 0.076)
  xgb-l: R2 = 0.032 (std: 0.076)
  mlp-adaptive-xl: R2 = 0.158 (std: 0.057)
  mlp-l: R2 = 0.151 (std: 0.031)
  svr-rbf-xl: R2 = 0.207 (std: 0.052)
  svr-poly-l: R2 = 0.207 (std: 0.052)
  knn-tuned-sqrt: R2 = 0.039 (std: 0.069)
  knn-tuned-l: R2 = 0.039 (std: 0.069)
  ridge: R2 = 0.075 (std: 0.034)

Model-based training with 2 models
Best R2: 0.207, Mean R2: 0.122
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9910, entropy=0.2228, kl_div=0.0000
    Epoch 1: policy_loss=-0.0806, value_loss=0.9910, entropy=0.2238, kl_div=-0.1973
  Round 1/3: Mean predicted reward = 11.638
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9889, entropy=0.2411, kl_div=0.0000
    Epoch 1: policy_loss=-0.0179, value_loss=0.9889, entropy=0.2420, kl_div=-0.2728
  Round 2/3: Mean predicted reward = 11.825
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9872, entropy=0.2428, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2337
  Round 3/3: Mean predicted reward = 12.080

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 35 Results ---
  Mean Oracle Reward: 11.931
  Min Oracle Reward: 5.687
  Max Oracle Reward: 15.916
  Std Oracle Reward: 1.943
  Sequence Diversity: 0.969
  Models Used: 2
  Model R2 - Mean: 0.122, Max: 0.207, Count: 13
  Total Sequences Evaluated: 2290

======================================================================
EXPERIMENT ROUND 36/40
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2290
  Performance plateaued, reducing LR to 0.000136

--- Round 36 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  ACCCGCTGCGGAAGTG
  GGACATTGCGCACGGC
  CTACGGCGATGGAGCC
  GAGGCCCCGGAGCTTA
  CGCACCAGGGGTGTAC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.273
  Max reward: 15.609
  With intrinsic bonuses: 12.297

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9857, entropy=0.2447, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3364

=== Surrogate Model Training ===
Total samples: 2354

Training on 2261 samples (removed 93 outliers)
Reward range: [8.15, 15.88], mean: 12.09
  Created 13 candidate models for data size 2261
Current R2 threshold: 0.22000000000000003
  rf-tuned-l: R2 = 0.142 (std: 0.050)
  rf-tuned-xl: R2 = 0.145 (std: 0.048)
  gb-tuned-l: R2 = 0.188 (std: 0.046)
  gb-tuned-xl: R2 = 0.188 (std: 0.046)
  xgb-xl: R2 = 0.045 (std: 0.082)
  xgb-l: R2 = 0.045 (std: 0.082)
  mlp-adaptive-xl: R2 = 0.172 (std: 0.047)
  mlp-l: R2 = 0.159 (std: 0.040)
  svr-rbf-xl: R2 = 0.210 (std: 0.047)
  svr-poly-l: R2 = 0.210 (std: 0.047)
  knn-tuned-sqrt: R2 = 0.037 (std: 0.068)
  knn-tuned-l: R2 = 0.037 (std: 0.068)
  ridge: R2 = 0.076 (std: 0.038)
  Fallback: Using svr-rbf-xl with R2 = 0.210

Model-based training with 1 models
Best R2: 0.210, Mean R2: 0.127
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9884, entropy=0.2446, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1086
  Round 1/3: Mean predicted reward = 11.679
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9897, entropy=0.2415, kl_div=0.0000
    Epoch 1: policy_loss=-0.0303, value_loss=0.9897, entropy=0.2415, kl_div=-0.2231
  Round 2/3: Mean predicted reward = 11.828
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9882, entropy=0.2393, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2932
  Round 3/3: Mean predicted reward = 12.024

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 36 Results ---
  Mean Oracle Reward: 12.320
  Min Oracle Reward: 7.327
  Max Oracle Reward: 15.400
  Std Oracle Reward: 1.808
  Sequence Diversity: 0.984
  Models Used: 1
  Model R2 - Mean: 0.127, Max: 0.210, Count: 13
  Total Sequences Evaluated: 2354

======================================================================
EXPERIMENT ROUND 37/40
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
  TAGAGCGGGCCAGTCC
  GTACGCACGGCATGGC
  CGTGGAGACGCCCGTA
  GAGAGTTCGCCCCGAG
  GAACCGCCTGCGTGAG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.718
  Max reward: 16.896
  With intrinsic bonuses: 12.712

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9853, entropy=0.2461, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7415

=== Surrogate Model Training ===
Total samples: 2418

Training on 2316 samples (removed 102 outliers)
Reward range: [8.19, 15.88], mean: 12.11
  Created 13 candidate models for data size 2316
Current R2 threshold: 0.24000000000000005
  rf-tuned-l: R2 = 0.154 (std: 0.031)
  rf-tuned-xl: R2 = 0.166 (std: 0.034)
  gb-tuned-l: R2 = 0.191 (std: 0.026)
  gb-tuned-xl: R2 = 0.191 (std: 0.026)
  xgb-xl: R2 = 0.050 (std: 0.074)
  xgb-l: R2 = 0.050 (std: 0.074)
  mlp-adaptive-xl: R2 = 0.170 (std: 0.027)
  mlp-l: R2 = 0.163 (std: 0.040)
  svr-rbf-xl: R2 = 0.217 (std: 0.032)
  svr-poly-l: R2 = 0.217 (std: 0.032)
  knn-tuned-sqrt: R2 = 0.061 (std: 0.063)
  knn-tuned-l: R2 = 0.061 (std: 0.063)
  ridge: R2 = 0.084 (std: 0.030)
  Fallback: Using svr-rbf-xl with R2 = 0.217

Model-based training with 1 models
Best R2: 0.217, Mean R2: 0.137
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9913, entropy=0.2390, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2276
  Round 1/3: Mean predicted reward = 11.661
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9874, entropy=0.2451, kl_div=0.0000
    Epoch 1: policy_loss=-0.0321, value_loss=0.9874, entropy=0.2437, kl_div=-0.2237
  Round 2/3: Mean predicted reward = 12.070
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9869, entropy=0.2385, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5379
  Round 3/3: Mean predicted reward = 12.130

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 37 Results ---
  Mean Oracle Reward: 12.696
  Min Oracle Reward: 5.954
  Max Oracle Reward: 17.156
  Std Oracle Reward: 2.169
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.137, Max: 0.217, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 2418

======================================================================
EXPERIMENT ROUND 38/40
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2418
  Consistent improvement, increasing LR to 0.000132

--- Round 38 Configuration ---
Learning rate: 0.000132
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  AAATGCTGGGCCCGCG
  GAGCACGCGCAGGTCT
  CCCATGAGGGAGCGCT
  CCCAGCGCTGATGGAG
  CAGGGTCACGATCGCG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.567
  Max reward: 16.960
  With intrinsic bonuses: 12.547

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9857, entropy=0.2339, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4400

=== Surrogate Model Training ===
Total samples: 2482

Training on 2376 samples (removed 106 outliers)
Reward range: [8.15, 15.96], mean: 12.12
  Created 13 candidate models for data size 2376
Current R2 threshold: 0.26000000000000006
  rf-tuned-l: R2 = 0.173 (std: 0.038)
  rf-tuned-xl: R2 = 0.181 (std: 0.031)
  gb-tuned-l: R2 = 0.216 (std: 0.038)
  gb-tuned-xl: R2 = 0.216 (std: 0.038)
  xgb-xl: R2 = 0.069 (std: 0.080)
  xgb-l: R2 = 0.069 (std: 0.080)
  mlp-adaptive-xl: R2 = 0.189 (std: 0.039)
  mlp-l: R2 = 0.204 (std: 0.051)
  svr-rbf-xl: R2 = 0.235 (std: 0.042)
  svr-poly-l: R2 = 0.235 (std: 0.042)
  knn-tuned-sqrt: R2 = 0.069 (std: 0.072)
  knn-tuned-l: R2 = 0.069 (std: 0.072)
  ridge: R2 = 0.094 (std: 0.047)
  Fallback: Using svr-rbf-xl with R2 = 0.235

Model-based training with 1 models
Best R2: 0.235, Mean R2: 0.155
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9877, entropy=0.2431, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1897
  Round 1/3: Mean predicted reward = 11.632
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9880, entropy=0.2309, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2301
  Round 2/3: Mean predicted reward = 12.090
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9863, entropy=0.2158, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4235
  Round 3/3: Mean predicted reward = 11.999

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 38 Results ---
  Mean Oracle Reward: 12.573
  Min Oracle Reward: 6.674
  Max Oracle Reward: 16.790
  Std Oracle Reward: 2.211
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.155, Max: 0.235, Count: 13
  Total Sequences Evaluated: 2482

======================================================================
EXPERIMENT ROUND 39/40
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2482

--- Round 39 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  CGCAGCCTTGCGAGAG
  GCAGCTCGACCGAGTG
  TGGGCAGCAGCGCCAT
  CTGCGACCAAGCGGTG
  CTGGACGAGGCGCTAC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 13.375
  Max reward: 18.699
  With intrinsic bonuses: 13.365

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9870, entropy=0.2373, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1705

=== Surrogate Model Training ===
Total samples: 2546

Training on 2435 samples (removed 111 outliers)
Reward range: [8.15, 16.02], mean: 12.14
  Created 13 candidate models for data size 2435
Current R2 threshold: 0.27999999999999997
  rf-tuned-l: R2 = 0.177 (std: 0.034)
  rf-tuned-xl: R2 = 0.175 (std: 0.034)
  gb-tuned-l: R2 = 0.219 (std: 0.036)
  gb-tuned-xl: R2 = 0.219 (std: 0.036)
  xgb-xl: R2 = 0.071 (std: 0.076)
  xgb-l: R2 = 0.071 (std: 0.076)
  mlp-adaptive-xl: R2 = 0.194 (std: 0.042)
  mlp-l: R2 = 0.203 (std: 0.032)
  svr-rbf-xl: R2 = 0.232 (std: 0.047)
  svr-poly-l: R2 = 0.232 (std: 0.047)
  knn-tuned-sqrt: R2 = 0.072 (std: 0.074)
  knn-tuned-l: R2 = 0.072 (std: 0.074)
  ridge: R2 = 0.090 (std: 0.051)
  Fallback: Using svr-rbf-xl with R2 = 0.232

Model-based training with 1 models
Best R2: 0.232, Mean R2: 0.156
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9875, entropy=0.2381, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0705
  Round 1/3: Mean predicted reward = 11.687
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9874, entropy=0.2259, kl_div=0.0000
    Epoch 1: policy_loss=-0.0105, value_loss=0.9874, entropy=0.2256, kl_div=0.0322
  Round 2/3: Mean predicted reward = 12.021
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9867, entropy=0.2298, kl_div=0.0000
    Epoch 1: policy_loss=-0.0274, value_loss=0.9867, entropy=0.2292, kl_div=-0.0074
  Round 3/3: Mean predicted reward = 12.324

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 39 Results ---
  Mean Oracle Reward: 13.334
  Min Oracle Reward: 8.548
  Max Oracle Reward: 18.626
  Std Oracle Reward: 1.975
  Sequence Diversity: 0.984
  Models Used: 1
  Model R2 - Mean: 0.156, Max: 0.232, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 2546

======================================================================
EXPERIMENT ROUND 40/40
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2546

--- Round 40 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  GCGACTTAGCACGGCG
  AGGCTGCCCGACGATG
  CGGCCGCAATAGGCGT
  CGAGTTGCAGCCGGCA
  CTACCTGGGCACGGGA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 13.070
  Max reward: 18.579
  With intrinsic bonuses: 13.090

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9851, entropy=0.2267, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3405

=== Surrogate Model Training ===
Total samples: 2610

Training on 2494 samples (removed 116 outliers)
Reward range: [8.14, 16.06], mean: 12.15
  Created 13 candidate models for data size 2494
Current R2 threshold: 0.3
  rf-tuned-l: R2 = 0.164 (std: 0.040)
  rf-tuned-xl: R2 = 0.166 (std: 0.045)
  gb-tuned-l: R2 = 0.217 (std: 0.041)
  gb-tuned-xl: R2 = 0.217 (std: 0.041)
  xgb-xl: R2 = 0.054 (std: 0.088)
  xgb-l: R2 = 0.054 (std: 0.088)
  mlp-adaptive-xl: R2 = 0.190 (std: 0.038)
  mlp-l: R2 = 0.179 (std: 0.056)
  svr-rbf-xl: R2 = 0.230 (std: 0.051)
  svr-poly-l: R2 = 0.230 (std: 0.051)
  knn-tuned-sqrt: R2 = 0.072 (std: 0.067)
  knn-tuned-l: R2 = 0.072 (std: 0.067)
  ridge: R2 = 0.093 (std: 0.057)
  Fallback: Using svr-rbf-xl with R2 = 0.230

Model-based training with 1 models
Best R2: 0.230, Mean R2: 0.149
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9907, entropy=0.2266, kl_div=0.0000
    Epoch 1: policy_loss=0.0185, value_loss=0.9906, entropy=0.2211, kl_div=-0.3006
  Round 1/3: Mean predicted reward = 11.641
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9873, entropy=0.2106, kl_div=0.0000
    Epoch 1: policy_loss=0.0767, value_loss=0.9873, entropy=0.2073, kl_div=-0.2475
  Round 2/3: Mean predicted reward = 11.986
    Using performance-based weights
    Model weights: svr-rbf-xl:1.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9888, entropy=0.2017, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8230
  Round 3/3: Mean predicted reward = 12.419

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 40 Results ---
  Mean Oracle Reward: 13.090
  Min Oracle Reward: 8.182
  Max Oracle Reward: 18.900
  Std Oracle Reward: 2.256
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.149, Max: 0.230, Count: 13
  Total Sequences Evaluated: 2610

======================================================================
DyNA PPO ALGORITHM COMPLETE!
======================================================================
Total rounds executed: 40
Total sequences evaluated: 2610
Best mean reward: 13.334 (achieved at round 39)

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 40
Final Mean Reward: 13.0903
Best Mean Reward: 13.3337
Best Max Reward: 18.9000
Initial Lr: 0.0003
Final Lr: 0.0003
Total Updates: 198
Final Diversity: 0.9688
Convergence Round: 7
==================================================

Generating learning curves...
Learning curves saved to learning_curves.png
Saving training metrics...
Metrics saved to training_metrics.json

======================================================================
FINAL OPTIMIZED SEQUENCES
======================================================================

Deterministic (Exploitation):
  GGCCGCCGGCCGGCCG: 16.973
  GGCCGCCGGCCGGCCG: 17.119
  GGCCGCCGGCCGGCCG: 17.111
  GGCCGCCGGCCGGCCG: 17.289
  GGCCGCCGGCCGGCCG: 17.290

Stochastic (Exploration):
  GGCCGGCCGGCCGCCG: 17.130
  GGCCGGCCGCCGCGCC: 15.811
  GGCCGGCCGGCCGGCC: 18.628
  GGCGCCGGCCGGCAGC: 14.375
  GGCCGGGCCCGCCGGC: 14.720

Final Performance:
  Mean reward: 16.644
  Max reward: 18.628
  Std reward: 1.229

Best sequence found: GGCCGGCCGGCCGGCC
   Reward: 18.628

======================================================================
Training complete! Check 'learning_curves.png' and 'training_metrics.json'
======================================================================