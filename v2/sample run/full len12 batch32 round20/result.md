======================================================================
RUNNING IMPROVED DyNA PPO WITH BETTER SURROGATE LEARNING
======================================================================
======================================================================
IMPROVED DyNA PPO ALGORITHM
======================================================================
Configuration:
  Number of experiment rounds N = 20
  Number of model-based training rounds M = 5
  Minimum model score τ = 0.2
  Batch size B = 32
  Warm-up phase: True
======================================================================

=== WARM-UP PHASE ===
Generating 50 warm-up samples...
Warm-up statistics:
  Mean reward: 8.327
  Std reward: 2.197
  Min/Max: 2.860 / 12.108

======================================================================
EXPERIMENT ROUND 1/20
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.300
Total data collected: 50

--- Round 1 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  CCTGAACCTAAA
  ACGCACGGCTAT
  CGTTGGGACATA
  TTGTGCCTTGCT
  TCTGTATACCGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.574
  Max reward: 12.411
  With intrinsic bonuses: 9.618

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9584, entropy=1.3795, kl_div=0.0000
    Epoch 2: policy_loss=-0.1652, value_loss=0.9587, entropy=1.3807, kl_div=-0.0008
    Epoch 4: policy_loss=-0.1839, value_loss=0.9590, entropy=1.3768, kl_div=0.0266
    Epoch 6: policy_loss=-0.1907, value_loss=0.9594, entropy=1.3767, kl_div=-0.0016

=== Surrogate Model Training ===
Total samples: 82

Training on 75 samples (removed 7 outliers)
Reward range: [5.83, 12.24], mean: 9.30
  Created 8 candidate models for data size 75
  rf-xs: R² = -0.761 (std: 0.654)
  rf-s: R² = -0.710 (std: 0.588)
  knn-xs: R² = -0.388 (std: 0.505)
  knn-s: R² = -0.388 (std: 0.505)
  ridge: R² = -0.487 (std: 0.454)
  gb-xs: R² = -1.247 (std: 0.570)
  gp: R² = -59.436 (std: 26.919)
  svr-rbf-s: R² = -0.358 (std: 0.402)
  Fallback: Using svr-rbf-s with R² = -0.358

Model-based training with 1 models
Best R²: -0.358, Mean R²: -7.972
Running 1 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9670, entropy=1.3768, kl_div=0.0000
  Round 1/1: Mean predicted reward = 9.569

  === Progress Analysis ===
  Status: WARNING
  • R² scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 1 Results ---
  Mean Oracle Reward: 9.583
  Min Oracle Reward: 4.708
  Max Oracle Reward: 12.127
  Std Oracle Reward: 1.503
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -7.972, Max: -0.358, Count: 8
  New best mean reward!
  Total Sequences Evaluated: 82

======================================================================
EXPERIMENT ROUND 2/20
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.300
Total data collected: 82

--- Round 2 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  GGGCATCTAGCC
  GAAGTCTTTGGT
  AGACCAAACAGA
  TAATAAGGCAAG
  CCTTGCTGGGTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.528
  Max reward: 12.350
  With intrinsic bonuses: 9.495

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=1.3771, kl_div=0.0000
    Epoch 2: policy_loss=-0.1118, value_loss=0.9684, entropy=1.3778, kl_div=-0.0186
    Epoch 4: policy_loss=-0.1553, value_loss=0.9685, entropy=1.3770, kl_div=-0.0202
    Epoch 6: policy_loss=-0.1973, value_loss=0.9686, entropy=1.3747, kl_div=0.0121

=== Surrogate Model Training ===
Total samples: 114

Training on 107 samples (removed 7 outliers)
Reward range: [5.83, 12.46], mean: 9.36
  Created 11 candidate models for data size 107
  rf-m: R² = -0.361 (std: 0.315)
  rf-l: R² = -0.366 (std: 0.342)
  gb-m: R² = -0.712 (std: 0.378)
  gb-l: R² = -0.729 (std: 0.423)
  xgb-m: R² = -0.724 (std: 0.434)
  knn-m: R² = -0.228 (std: 0.206)
  knn-tuned: R² = -0.228 (std: 0.206)
  mlp-m: R² = -3.176 (std: 2.175)
  svr-rbf: R² = -0.231 (std: 0.214)
  svr-poly: R² = -0.231 (std: 0.214)
  ridge: R² = -0.264 (std: 0.226)
  Fallback: Using knn-m with R² = -0.228

Model-based training with 1 models
Best R²: -0.228, Mean R²: -0.659
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9657, entropy=1.3733, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.564
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9638, entropy=1.3725, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.482

  === Progress Analysis ===
  Status: WARNING
  • R² scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 2 Results ---
  Mean Oracle Reward: 9.544
  Min Oracle Reward: 6.506
  Max Oracle Reward: 12.444
  Std Oracle Reward: 1.227
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -0.659, Max: -0.228, Count: 11
  Total Sequences Evaluated: 114

======================================================================
EXPERIMENT ROUND 3/20
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.300
Total data collected: 114

--- Round 3 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  TCTATTCGACCA
  AGCGCGTGAGCA
  TATGCGATATGG
  ACCTGGGAGCAC
  GAACAGTTCGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.291
  Max reward: 11.532
  With intrinsic bonuses: 9.418

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9599, entropy=1.3709, kl_div=0.0000
    Epoch 2: policy_loss=-0.0596, value_loss=0.9601, entropy=1.3684, kl_div=0.0137
    Epoch 4: policy_loss=-0.0966, value_loss=0.9603, entropy=1.3645, kl_div=0.0343
    Early stopping at epoch 6: KL divergence = 0.0582

=== Surrogate Model Training ===
Total samples: 146

Training on 136 samples (removed 10 outliers)
Reward range: [6.04, 12.46], mean: 9.46
  Created 11 candidate models for data size 136
  rf-m: R² = -0.124 (std: 0.166)
  rf-l: R² = -0.149 (std: 0.157)
  gb-m: R² = -0.329 (std: 0.239)
  gb-l: R² = -0.321 (std: 0.241)
  xgb-m: R² = -0.463 (std: 0.270)
  knn-m: R² = -0.178 (std: 0.155)
  knn-tuned: R² = -0.178 (std: 0.155)
  mlp-m: R² = -2.938 (std: 1.087)
  svr-rbf: R² = -0.088 (std: 0.199)
  svr-poly: R² = -0.088 (std: 0.199)
  ridge: R² = -0.101 (std: 0.131)

Model-based training with 7 models
Best R²: -0.088, Mean R²: -0.451
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=1.3613, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.643
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=1.3571, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.629

  === Progress Analysis ===
  Status: WARNING
  • R² scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 3 Results ---
  Mean Oracle Reward: 9.278
  Min Oracle Reward: 0.000
  Max Oracle Reward: 11.402
  Std Oracle Reward: 2.021
  Sequence Diversity: 1.000
  Models Used: 7
  Model R² - Mean: -0.451, Max: -0.088, Count: 11
  Total Sequences Evaluated: 146

======================================================================
EXPERIMENT ROUND 4/20
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.280
Total data collected: 146

--- Round 4 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0100
Exploration rate: 0.280

--- Generated Sequences (Diversity: 1.000) ---
  GGTCTAAGCGAC
  CCGGATACGTAT
  AAGTTGTACCGC
  GTGAACCAGCTG
  TCTTCAAGCGAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.978
  Max reward: 12.633
  With intrinsic bonuses: 10.113

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9586, entropy=1.3553, kl_div=0.0000
    Epoch 1: policy_loss=-0.0113, value_loss=0.9586, entropy=1.3543, kl_div=0.0081
    Epoch 2: policy_loss=-0.0244, value_loss=0.9586, entropy=1.3533, kl_div=0.0171
    Epoch 3: policy_loss=-0.0389, value_loss=0.9586, entropy=1.3522, kl_div=0.0268

=== Surrogate Model Training ===
Total samples: 178

Training on 168 samples (removed 10 outliers)
Reward range: [6.04, 12.81], mean: 9.55
  Created 11 candidate models for data size 168
  rf-m: R² = -0.123 (std: 0.150)
  rf-l: R² = -0.109 (std: 0.131)
  gb-m: R² = -0.334 (std: 0.192)
  gb-l: R² = -0.333 (std: 0.191)
  xgb-m: R² = -0.177 (std: 0.144)
  knn-m: R² = -0.126 (std: 0.193)
  knn-tuned: R² = -0.126 (std: 0.193)
  mlp-m: R² = -2.151 (std: 0.407)
  svr-rbf: R² = -0.061 (std: 0.192)
  svr-poly: R² = -0.061 (std: 0.192)
  ridge: R² = -0.110 (std: 0.141)
  Fallback: Using svr-rbf with R² = -0.061

Model-based training with 1 models
Best R²: -0.061, Mean R²: -0.337
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9578, entropy=1.3525, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.928
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9647, entropy=1.3528, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.037

  === Progress Analysis ===
  Status: WARNING
  • R² scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 4 Results ---
  Mean Oracle Reward: 9.991
  Min Oracle Reward: 7.415
  Max Oracle Reward: 13.054
  Std Oracle Reward: 1.389
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -0.337, Max: -0.061, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 178

======================================================================
EXPERIMENT ROUND 5/20
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.250
Total data collected: 178

--- Round 5 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0100
Exploration rate: 0.250

--- Generated Sequences (Diversity: 1.000) ---
  GCACTAGCGATG
  GTGGAACACCGT
  ACTCAGTGCATG
  GGTAGCATACGC
  CGGGTTCTAAAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.083
  Max reward: 12.222
  With intrinsic bonuses: 10.178

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9728, entropy=1.3488, kl_div=0.0000
    Epoch 1: policy_loss=-0.0165, value_loss=0.9727, entropy=1.3388, kl_div=0.0467
    Early stopping at epoch 2: KL divergence = 0.0982

=== Surrogate Model Training ===
Total samples: 210

Training on 199 samples (removed 11 outliers)
Reward range: [6.29, 12.81], mean: 9.65
  Created 11 candidate models for data size 199
  rf-m: R² = -0.089 (std: 0.231)
  rf-l: R² = -0.113 (std: 0.271)
  gb-m: R² = -0.070 (std: 0.270)
  gb-l: R² = -0.087 (std: 0.272)
  xgb-m: R² = -0.298 (std: 0.295)
  knn-m: R² = -0.229 (std: 0.242)
  knn-tuned: R² = -0.229 (std: 0.242)
  mlp-m: R² = -1.864 (std: 0.650)
  svr-rbf: R² = -0.028 (std: 0.224)
  svr-poly: R² = -0.028 (std: 0.224)
  ridge: R² = -0.115 (std: 0.176)
  Fallback: Using svr-rbf with R² = -0.028

Model-based training with 1 models
Best R²: -0.028, Mean R²: -0.286
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=1.3338, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.165
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9714, entropy=1.3236, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.048

  === Progress Analysis ===
  Status: WARNING
  • R² scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 5 Results ---
  Mean Oracle Reward: 10.062
  Min Oracle Reward: 6.957
  Max Oracle Reward: 12.211
  Std Oracle Reward: 1.036
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -0.286, Max: -0.028, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 210

======================================================================
EXPERIMENT ROUND 6/20
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
  TGAAGTCACCTG
  GAAGCATTCTCG
  TTAGGTCACACG
  ATATCTACCGGG
  TCAACCTGGATG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.770
  Max reward: 12.373
  With intrinsic bonuses: 9.802

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9632, entropy=1.3067, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1252

=== Surrogate Model Training ===
Total samples: 242

Training on 224 samples (removed 18 outliers)
Reward range: [6.71, 12.46], mean: 9.71
  Created 11 candidate models for data size 224
  rf-m: R² = -0.074 (std: 0.044)
  rf-l: R² = -0.034 (std: 0.048)
  gb-m: R² = -0.152 (std: 0.088)
  gb-l: R² = -0.160 (std: 0.098)
  xgb-m: R² = -0.288 (std: 0.248)
  knn-m: R² = -0.207 (std: 0.127)
  knn-tuned: R² = -0.207 (std: 0.127)
  mlp-m: R² = -1.951 (std: 0.745)
  svr-rbf: R² = 0.004 (std: 0.110)
  svr-poly: R² = 0.004 (std: 0.110)
  ridge: R² = -0.038 (std: 0.062)

Model-based training with 2 models
Best R²: 0.004, Mean R²: -0.282
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9667, entropy=1.2989, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1386
  Round 1/3: Mean predicted reward = 9.793
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9655, entropy=1.2823, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1133
  Round 2/3: Mean predicted reward = 9.864
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9660, entropy=1.2654, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1370
  Round 3/3: Mean predicted reward = 9.797

  === Progress Analysis ===
  Status: NORMAL

--- Round 6 Results ---
  Mean Oracle Reward: 9.707
  Min Oracle Reward: 7.442
  Max Oracle Reward: 12.466
  Std Oracle Reward: 0.978
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -0.282, Max: 0.004, Count: 11
  Total Sequences Evaluated: 242

======================================================================
EXPERIMENT ROUND 7/20
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.190
Total data collected: 242

--- Round 7 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0100
Exploration rate: 0.190

--- Generated Sequences (Diversity: 1.000) ---
  GGGCGAATTACC
  TCTCCGAGTAAG
  GCACGAGACTGT
  GTCCAAGTGACG
  GAGGTATTCCCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.724
  Max reward: 12.187
  With intrinsic bonuses: 9.691

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9760, entropy=1.2477, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1190

=== Surrogate Model Training ===
Total samples: 274

Training on 254 samples (removed 20 outliers)
Reward range: [6.93, 12.46], mean: 9.74
  Created 11 candidate models for data size 254
  rf-m: R² = 0.039 (std: 0.095)
  rf-l: R² = 0.043 (std: 0.106)
  gb-m: R² = 0.040 (std: 0.154)
  gb-l: R² = 0.034 (std: 0.161)
  xgb-m: R² = -0.117 (std: 0.222)
  knn-m: R² = -0.085 (std: 0.115)
  knn-tuned: R² = -0.085 (std: 0.115)
  mlp-m: R² = -1.202 (std: 0.655)
  svr-rbf: R² = 0.063 (std: 0.072)
  svr-poly: R² = 0.063 (std: 0.072)
  ridge: R² = -0.009 (std: 0.026)

Model-based training with 6 models
Best R²: 0.063, Mean R²: -0.110
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=1.2363, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1006
  Round 1/3: Mean predicted reward = 9.828
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9642, entropy=1.2230, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1459
  Round 2/3: Mean predicted reward = 9.682
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9640, entropy=1.2056, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1718
  Round 3/3: Mean predicted reward = 9.827

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 7 Results ---
  Mean Oracle Reward: 9.709
  Min Oracle Reward: 4.468
  Max Oracle Reward: 12.392
  Std Oracle Reward: 1.327
  Sequence Diversity: 1.000
  Models Used: 6
  Model R² - Mean: -0.110, Max: 0.063, Count: 11
  Total Sequences Evaluated: 274

======================================================================
EXPERIMENT ROUND 8/20
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.080
Total data collected: 274

--- Round 8 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.080

--- Generated Sequences (Diversity: 1.000) ---
  TAGAGTCTGAAC
  GCAGGCTGATAC
  CATGCCTGTAAG
  CAGACCTGTAGT
  GCTCAGTTACGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.147
  Max reward: 12.851
  With intrinsic bonuses: 10.169

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9709, entropy=1.1892, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0954

=== Surrogate Model Training ===
Total samples: 306

Training on 284 samples (removed 22 outliers)
Reward range: [6.93, 12.46], mean: 9.79
  Created 11 candidate models for data size 284
  rf-m: R² = -0.017 (std: 0.065)
  rf-l: R² = -0.055 (std: 0.074)
  gb-m: R² = -0.171 (std: 0.153)
  gb-l: R² = -0.167 (std: 0.154)
  xgb-m: R² = -0.216 (std: 0.106)
  knn-m: R² = -0.287 (std: 0.108)
  knn-tuned: R² = -0.287 (std: 0.108)
  mlp-m: R² = -1.362 (std: 0.558)
  svr-rbf: R² = -0.012 (std: 0.111)
  svr-poly: R² = -0.012 (std: 0.111)
  ridge: R² = -0.054 (std: 0.079)
  Fallback: Using svr-rbf with R² = -0.012

Model-based training with 1 models
Best R²: -0.012, Mean R²: -0.240
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9625, entropy=1.2056, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.075
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9732, entropy=1.1874, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.158

  === Progress Analysis ===
  Status: WARNING
  • R² scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 8 Results ---
  Mean Oracle Reward: 10.122
  Min Oracle Reward: 6.634
  Max Oracle Reward: 13.096
  Std Oracle Reward: 1.198
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -0.240, Max: -0.012, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 306

======================================================================
EXPERIMENT ROUND 9/20
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.065
Total data collected: 306

--- Round 9 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.065

--- Generated Sequences (Diversity: 1.000) ---
  AGACGGGCATTC
  TCTAGATACCGG
  GCTCGGCAAGTA
  GAGGTGTACCAC
  GCAGCCTATATG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.684
  Max reward: 12.752
  With intrinsic bonuses: 9.750

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9779, entropy=1.1610, kl_div=0.0000
    Epoch 1: policy_loss=-0.0039, value_loss=0.9779, entropy=1.1590, kl_div=0.0173

=== Surrogate Model Training ===
Total samples: 338

Training on 315 samples (removed 23 outliers)
Reward range: [6.93, 12.50], mean: 9.79
  Created 14 candidate models for data size 315
  rf-tuned-l: R² = -0.067 (std: 0.073)
  rf-tuned-xl: R² = -0.091 (std: 0.053)
  gb-tuned-l: R² = -0.141 (std: 0.202)
  gb-tuned-xl: R² = -0.145 (std: 0.199)
  xgb-xl: R² = -0.238 (std: 0.077)
  xgb-l: R² = -0.238 (std: 0.077)
  mlp-adaptive-xl: R² = -1.484 (std: 0.312)
  mlp-l: R² = -1.628 (std: 0.578)
  svr-rbf-xl: R² = -0.044 (std: 0.127)
  svr-poly-l: R² = -0.044 (std: 0.127)
  knn-tuned-sqrt: R² = -0.272 (std: 0.142)
  knn-tuned-l: R² = -0.272 (std: 0.142)
  ridge: R² = -0.079 (std: 0.092)
  gp: R² = -91.536 (std: 20.903)
  Fallback: Using svr-rbf-xl with R² = -0.044

Model-based training with 1 models
Best R²: -0.044, Mean R²: -6.877
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9743, entropy=1.1900, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.789
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9758, entropy=1.1913, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.798

  === Progress Analysis ===
  Status: WARNING
  • R² scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 9 Results ---
  Mean Oracle Reward: 9.687
  Min Oracle Reward: 6.278
  Max Oracle Reward: 12.647
  Std Oracle Reward: 1.297
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -6.877, Max: -0.044, Count: 14
  Total Sequences Evaluated: 338

======================================================================
EXPERIMENT ROUND 10/20
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 338

--- Round 10 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCCAATTCAGTG
  CAGAGATGCCTT
  TCGCTCTAGAAG
  ATACTCGCGGGA
  TCTACGGAGTAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.926
  Max reward: 12.859
  With intrinsic bonuses: 9.914

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9737, entropy=1.1581, kl_div=0.0000
    Epoch 1: policy_loss=-0.0613, value_loss=0.9737, entropy=1.1631, kl_div=0.0172

=== Surrogate Model Training ===
Total samples: 370

Training on 345 samples (removed 25 outliers)
Reward range: [6.93, 12.50], mean: 9.81
  Created 14 candidate models for data size 345
  rf-tuned-l: R² = -0.017 (std: 0.076)
  rf-tuned-xl: R² = -0.019 (std: 0.092)
  gb-tuned-l: R² = -0.114 (std: 0.159)
  gb-tuned-xl: R² = -0.112 (std: 0.156)
  xgb-xl: R² = -0.171 (std: 0.174)
  xgb-l: R² = -0.171 (std: 0.174)
  mlp-adaptive-xl: R² = -0.943 (std: 0.450)
  mlp-l: R² = -1.086 (std: 0.708)
  svr-rbf-xl: R² = -0.004 (std: 0.095)
  svr-poly-l: R² = -0.004 (std: 0.095)
  knn-tuned-sqrt: R² = -0.196 (std: 0.068)
  knn-tuned-l: R² = -0.196 (std: 0.068)
  ridge: R² = -0.038 (std: 0.057)
  gp: R² = -90.885 (std: 20.110)
  Fallback: Using svr-rbf-xl with R² = -0.004

Model-based training with 1 models
Best R²: -0.004, Mean R²: -6.711
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9758, entropy=1.1829, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.960
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9752, entropy=1.1804, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.254

  === Progress Analysis ===
  Status: WARNING
  • R² scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 10 Results ---
  Mean Oracle Reward: 9.933
  Min Oracle Reward: 6.161
  Max Oracle Reward: 12.694
  Std Oracle Reward: 1.253
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -6.711, Max: -0.004, Count: 14
  Total Sequences Evaluated: 370

======================================================================
EXPERIMENT ROUND 11/20
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 370

--- Round 11 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ATGGTACAACGT
  AAGGCCTTTAGC
  GTATCAGTACGC
  ACTAGGGCGTCC
  TATCCGGCAAGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.333
  Max reward: 13.049
  With intrinsic bonuses: 10.297

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=1.1826, kl_div=0.0000
    Epoch 1: policy_loss=-0.0187, value_loss=0.9686, entropy=1.1883, kl_div=-0.0655

=== Surrogate Model Training ===
Total samples: 402

Training on 378 samples (removed 24 outliers)
Reward range: [6.93, 12.61], mean: 9.86
  Created 14 candidate models for data size 378
  rf-tuned-l: R² = -0.043 (std: 0.042)
  rf-tuned-xl: R² = -0.047 (std: 0.051)
  gb-tuned-l: R² = -0.106 (std: 0.110)
  gb-tuned-xl: R² = -0.108 (std: 0.105)
  xgb-xl: R² = -0.178 (std: 0.140)
  xgb-l: R² = -0.178 (std: 0.140)
  mlp-adaptive-xl: R² = -1.085 (std: 0.277)
  mlp-l: R² = -1.046 (std: 0.346)
  svr-rbf-xl: R² = -0.029 (std: 0.054)
  svr-poly-l: R² = -0.029 (std: 0.054)
  knn-tuned-sqrt: R² = -0.171 (std: 0.080)
  knn-tuned-l: R² = -0.171 (std: 0.080)
  ridge: R² = -0.054 (std: 0.046)
  gp: R² = -88.966 (std: 8.522)
  Fallback: Using svr-rbf-xl with R² = -0.029

Model-based training with 1 models
Best R²: -0.029, Mean R²: -6.587
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9736, entropy=1.2053, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.159
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9724, entropy=1.2009, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.154

  === Progress Analysis ===
  Status: WARNING
  • R² scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 11 Results ---
  Mean Oracle Reward: 10.301
  Min Oracle Reward: 8.557
  Max Oracle Reward: 12.877
  Std Oracle Reward: 0.992
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -6.587, Max: -0.029, Count: 14
  New best mean reward!
  Total Sequences Evaluated: 402

======================================================================
EXPERIMENT ROUND 12/20
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 402
  Consistent improvement, increasing LR to 0.000240

--- Round 12 Configuration ---
Learning rate: 0.000240
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TTGACCGCTAAG
  GTGAGCCTAAGC
  ACGACCTTAGGT
  CAATGGACTGCG
  GTTGAACCCAGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.513
  Max reward: 11.801
  With intrinsic bonuses: 10.530

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=1.1837, kl_div=0.0000
    Epoch 1: policy_loss=-0.0090, value_loss=0.9695, entropy=1.1782, kl_div=0.0229

=== Surrogate Model Training ===
Total samples: 434

Training on 406 samples (removed 28 outliers)
Reward range: [7.15, 12.56], mean: 9.93
  Created 14 candidate models for data size 406
  rf-tuned-l: R² = -0.059 (std: 0.107)
  rf-tuned-xl: R² = -0.057 (std: 0.083)
  gb-tuned-l: R² = -0.116 (std: 0.080)
  gb-tuned-xl: R² = -0.117 (std: 0.077)
  xgb-xl: R² = -0.195 (std: 0.185)
  xgb-l: R² = -0.195 (std: 0.185)
  mlp-adaptive-xl: R² = -1.223 (std: 0.516)
  mlp-l: R² = -1.116 (std: 0.370)
  svr-rbf-xl: R² = -0.047 (std: 0.071)
  svr-poly-l: R² = -0.047 (std: 0.071)
  knn-tuned-sqrt: R² = -0.190 (std: 0.107)
  knn-tuned-l: R² = -0.190 (std: 0.107)
  ridge: R² = -0.083 (std: 0.077)
  gp: R² = -101.877 (std: 21.436)
  Fallback: Using svr-rbf-xl with R² = -0.047

Model-based training with 1 models
Best R²: -0.047, Mean R²: -7.536
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9753, entropy=1.1892, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.148
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9753, entropy=1.1859, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.186

  === Progress Analysis ===
  Status: WARNING
  • R² scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 12 Results ---
  Mean Oracle Reward: 10.527
  Min Oracle Reward: 8.825
  Max Oracle Reward: 11.856
  Std Oracle Reward: 0.744
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -7.536, Max: -0.047, Count: 14
  New best mean reward!
  Total Sequences Evaluated: 434

======================================================================
EXPERIMENT ROUND 13/20
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 434
  Consistent improvement, increasing LR to 0.000132

--- Round 13 Configuration ---
Learning rate: 0.000132
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AGTCCCTGTAAG
  TATGAGTCAACG
  TGGCAATGCAGC
  AGCTATAAGTCG
  GCAATGTCAGTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.131
  Max reward: 12.154
  With intrinsic bonuses: 10.074

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9700, entropy=1.1678, kl_div=0.0000
    Epoch 1: policy_loss=-0.0188, value_loss=0.9700, entropy=1.1629, kl_div=0.0401

=== Surrogate Model Training ===
Total samples: 466

Training on 439 samples (removed 27 outliers)
Reward range: [7.14, 12.61], mean: 9.95
  Created 14 candidate models for data size 439
  rf-tuned-l: R² = -0.051 (std: 0.095)
  rf-tuned-xl: R² = -0.021 (std: 0.098)
  gb-tuned-l: R² = -0.062 (std: 0.108)
  gb-tuned-xl: R² = -0.065 (std: 0.112)
  xgb-xl: R² = -0.210 (std: 0.113)
  xgb-l: R² = -0.210 (std: 0.113)
  mlp-adaptive-xl: R² = -1.058 (std: 0.537)
  mlp-l: R² = -0.876 (std: 0.253)
  svr-rbf-xl: R² = -0.003 (std: 0.078)
  svr-poly-l: R² = -0.003 (std: 0.078)
  knn-tuned-sqrt: R² = -0.136 (std: 0.108)
  knn-tuned-l: R² = -0.136 (std: 0.108)
  ridge: R² = -0.062 (std: 0.093)
  gp: R² = -97.871 (std: 15.717)
  Fallback: Using svr-rbf-xl with R² = -0.003

Model-based training with 1 models
Best R²: -0.003, Mean R²: -7.197
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9728, entropy=1.1783, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.278
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9740, entropy=1.1718, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.144

  === Progress Analysis ===
  Status: WARNING
  • R² scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 13 Results ---
  Mean Oracle Reward: 10.120
  Min Oracle Reward: 7.415
  Max Oracle Reward: 12.184
  Std Oracle Reward: 1.147
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -7.197, Max: -0.003, Count: 14
  Total Sequences Evaluated: 466

======================================================================
EXPERIMENT ROUND 14/20
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 466

--- Round 14 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTGAAGCTACCT
  ACAGTACGGGCT
  AGTGTACCATCG
  AGCAGCTTGTCA
  CGATTAGCCGTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.385
  Max reward: 11.964
  With intrinsic bonuses: 10.372

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9681, entropy=1.1355, kl_div=0.0000
    Epoch 1: policy_loss=-0.0049, value_loss=0.9681, entropy=1.1333, kl_div=0.0173

=== Surrogate Model Training ===
Total samples: 498

Training on 472 samples (removed 26 outliers)
Reward range: [7.14, 12.66], mean: 9.98
  Created 14 candidate models for data size 472
  rf-tuned-l: R² = -0.025 (std: 0.048)
  rf-tuned-xl: R² = -0.027 (std: 0.064)
  gb-tuned-l: R² = -0.064 (std: 0.092)
  gb-tuned-xl: R² = -0.064 (std: 0.092)
  xgb-xl: R² = -0.132 (std: 0.043)
  xgb-l: R² = -0.132 (std: 0.043)
  mlp-adaptive-xl: R² = -0.805 (std: 0.302)
  mlp-l: R² = -0.676 (std: 0.250)
  svr-rbf-xl: R² = 0.014 (std: 0.044)
  svr-poly-l: R² = 0.014 (std: 0.044)
  knn-tuned-sqrt: R² = -0.129 (std: 0.052)
  knn-tuned-l: R² = -0.129 (std: 0.052)
  ridge: R² = -0.065 (std: 0.073)
  gp: R² = -95.068 (std: 9.052)

Model-based training with 2 models
Best R²: 0.014, Mean R²: -6.949
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9644, entropy=1.1429, kl_div=0.0000
    Epoch 1: policy_loss=-0.0112, value_loss=0.9644, entropy=1.1406, kl_div=0.0209
  Round 1/3: Mean predicted reward = 10.049
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=1.1300, kl_div=0.0000
    Epoch 1: policy_loss=-0.0201, value_loss=0.9705, entropy=1.1267, kl_div=0.0312
  Round 2/3: Mean predicted reward = 10.011
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=1.1159, kl_div=0.0000
    Epoch 1: policy_loss=-0.0258, value_loss=0.9679, entropy=1.1114, kl_div=0.0495
  Round 3/3: Mean predicted reward = 10.063

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 14 Results ---
  Mean Oracle Reward: 10.385
  Min Oracle Reward: 7.124
  Max Oracle Reward: 11.604
  Std Oracle Reward: 0.986
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -6.949, Max: 0.014, Count: 14
  Total Sequences Evaluated: 498

======================================================================
EXPERIMENT ROUND 15/20
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 498

--- Round 15 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTCAGCAGGATG
  CCCAGAGTTGAG
  GCTTACGAGAGC
  CATACATGGCGG
  TCGCCGAGTGAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.750
  Max reward: 11.349
  With intrinsic bonuses: 9.722

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=1.1158, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4517

=== Surrogate Model Training ===
Total samples: 530

Training on 502 samples (removed 28 outliers)
Reward range: [7.14, 12.66], mean: 9.98
  Created 13 candidate models for data size 502
  rf-tuned-l: R² = 0.005 (std: 0.048)
  rf-tuned-xl: R² = 0.008 (std: 0.039)
  gb-tuned-l: R² = -0.045 (std: 0.110)
  gb-tuned-xl: R² = -0.045 (std: 0.110)
  xgb-xl: R² = -0.025 (std: 0.066)
  xgb-l: R² = -0.025 (std: 0.066)
  mlp-adaptive-xl: R² = -0.664 (std: 0.210)
  mlp-l: R² = -0.634 (std: 0.210)
  svr-rbf-xl: R² = 0.018 (std: 0.051)
  svr-poly-l: R² = 0.018 (std: 0.051)
  knn-tuned-sqrt: R² = -0.119 (std: 0.028)
  knn-tuned-l: R² = -0.119 (std: 0.028)
  ridge: R² = -0.042 (std: 0.035)

Model-based training with 4 models
Best R²: 0.018, Mean R²: -0.129
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9624, entropy=1.0744, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6487
  Round 1/3: Mean predicted reward = 9.948
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9720, entropy=1.0267, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7336
  Round 2/3: Mean predicted reward = 9.956
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.9875, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5664
  Round 3/3: Mean predicted reward = 10.049

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 15 Results ---
  Mean Oracle Reward: 9.744
  Min Oracle Reward: 5.005
  Max Oracle Reward: 11.478
  Std Oracle Reward: 1.346
  Sequence Diversity: 1.000
  Models Used: 4
  Model R² - Mean: -0.129, Max: 0.018, Count: 13
  Total Sequences Evaluated: 530

======================================================================
EXPERIMENT ROUND 16/20
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 530

--- Round 16 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTGATAGTACCC
  ATATGCGACCGT
  TTCGACATAGGC
  TAACCTGGGGCA
  TGCAGTATCGCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.930
  Max reward: 13.026
  With intrinsic bonuses: 9.958

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9676, entropy=0.9353, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6130

=== Surrogate Model Training ===
Total samples: 562

Training on 537 samples (removed 25 outliers)
Reward range: [6.93, 12.81], mean: 9.98
  Created 13 candidate models for data size 537
  rf-tuned-l: R² = -0.001 (std: 0.115)
  rf-tuned-xl: R² = 0.006 (std: 0.089)
  gb-tuned-l: R² = -0.019 (std: 0.112)
  gb-tuned-xl: R² = -0.020 (std: 0.112)
  xgb-xl: R² = -0.069 (std: 0.165)
  xgb-l: R² = -0.069 (std: 0.165)
  mlp-adaptive-xl: R² = -0.657 (std: 0.262)
  mlp-l: R² = -0.689 (std: 0.368)
  svr-rbf-xl: R² = 0.023 (std: 0.086)
  svr-poly-l: R² = 0.023 (std: 0.086)
  knn-tuned-sqrt: R² = -0.097 (std: 0.101)
  knn-tuned-l: R² = -0.097 (std: 0.101)
  ridge: R² = -0.061 (std: 0.080)

Model-based training with 3 models
Best R²: 0.023, Mean R²: -0.133
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.8935, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5710
  Round 1/3: Mean predicted reward = 10.039
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.8645, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5288
  Round 2/3: Mean predicted reward = 10.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9677, entropy=0.8266, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8263
  Round 3/3: Mean predicted reward = 9.917

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 16 Results ---
  Mean Oracle Reward: 9.950
  Min Oracle Reward: 5.513
  Max Oracle Reward: 13.050
  Std Oracle Reward: 1.432
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: -0.133, Max: 0.023, Count: 13
  Total Sequences Evaluated: 562

======================================================================
EXPERIMENT ROUND 17/20
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 562

--- Round 17 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGCATCGAGCAT
  TCAGGATGTCCA
  ACGGTTCACTGA
  GTACGCATATGC
  ATGGCGCATTCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.027
  Max reward: 13.272
  With intrinsic bonuses: 10.000

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.8198, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3169

=== Surrogate Model Training ===
Total samples: 594

Training on 564 samples (removed 30 outliers)
Reward range: [7.14, 12.85], mean: 10.01
  Created 13 candidate models for data size 564
  rf-tuned-l: R² = -0.016 (std: 0.115)
  rf-tuned-xl: R² = -0.008 (std: 0.111)
  gb-tuned-l: R² = -0.032 (std: 0.136)
  gb-tuned-xl: R² = -0.032 (std: 0.136)
  xgb-xl: R² = -0.090 (std: 0.169)
  xgb-l: R² = -0.090 (std: 0.169)
  mlp-adaptive-xl: R² = -0.534 (std: 0.359)
  mlp-l: R² = -0.565 (std: 0.326)
  svr-rbf-xl: R² = 0.028 (std: 0.071)
  svr-poly-l: R² = 0.028 (std: 0.071)
  knn-tuned-sqrt: R² = -0.075 (std: 0.104)
  knn-tuned-l: R² = -0.075 (std: 0.104)
  ridge: R² = -0.066 (std: 0.073)

Model-based training with 2 models
Best R²: 0.028, Mean R²: -0.117
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9668, entropy=0.7958, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3207
  Round 1/3: Mean predicted reward = 9.909
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9710, entropy=0.7829, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2046
  Round 2/3: Mean predicted reward = 10.007
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9708, entropy=0.7812, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1337
  Round 3/3: Mean predicted reward = 10.083

  === Progress Analysis ===
  Status: NORMAL

--- Round 17 Results ---
  Mean Oracle Reward: 10.048
  Min Oracle Reward: 5.552
  Max Oracle Reward: 12.888
  Std Oracle Reward: 1.461
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -0.117, Max: 0.028, Count: 13
  Total Sequences Evaluated: 594

======================================================================
EXPERIMENT ROUND 18/20
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
  GACCTGTGAGCA
  GATACGTACCGG
  TCGTACTAGCAG
  GCCGTCATGGAA
  TAAGTGGCTCCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.639
  Max reward: 12.567
  With intrinsic bonuses: 9.671

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.7766, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0990

=== Surrogate Model Training ===
Total samples: 626

Training on 597 samples (removed 29 outliers)
Reward range: [6.93, 12.85], mean: 9.99
  Created 13 candidate models for data size 597
  rf-tuned-l: R² = 0.012 (std: 0.140)
  rf-tuned-xl: R² = -0.022 (std: 0.142)
  gb-tuned-l: R² = -0.020 (std: 0.133)
  gb-tuned-xl: R² = -0.023 (std: 0.133)
  xgb-xl: R² = -0.021 (std: 0.115)
  xgb-l: R² = -0.021 (std: 0.115)
  mlp-adaptive-xl: R² = -0.420 (std: 0.090)
  mlp-l: R² = -0.503 (std: 0.200)
  svr-rbf-xl: R² = 0.056 (std: 0.086)
  svr-poly-l: R² = 0.056 (std: 0.086)
  knn-tuned-sqrt: R² = -0.042 (std: 0.125)
  knn-tuned-l: R² = -0.042 (std: 0.125)
  ridge: R² = -0.071 (std: 0.081)

Model-based training with 3 models
Best R²: 0.056, Mean R²: -0.082
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9668, entropy=0.7753, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1159
  Round 1/3: Mean predicted reward = 9.997
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9658, entropy=0.7796, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0854
  Round 2/3: Mean predicted reward = 10.103
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.7897, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1268
  Round 3/3: Mean predicted reward = 10.014

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 18 Results ---
  Mean Oracle Reward: 9.625
  Min Oracle Reward: 4.547
  Max Oracle Reward: 12.662
  Std Oracle Reward: 1.659
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: -0.082, Max: 0.056, Count: 13
  Total Sequences Evaluated: 626

======================================================================
EXPERIMENT ROUND 19/20
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 626

--- Round 19 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGGATTAATCCC
  AGAGCCTGTACG
  GCACTAATATGG
  TGATACCGACTG
  AACTTTGCGCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.811
  Max reward: 12.574
  With intrinsic bonuses: 9.832

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9658, entropy=0.7773, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0577

=== Surrogate Model Training ===
Total samples: 658

Training on 625 samples (removed 33 outliers)
Reward range: [7.14, 12.85], mean: 10.00
  Created 13 candidate models for data size 625
  rf-tuned-l: R² = -0.007 (std: 0.129)
  rf-tuned-xl: R² = 0.010 (std: 0.142)
  gb-tuned-l: R² = -0.016 (std: 0.136)
  gb-tuned-xl: R² = -0.018 (std: 0.138)
  xgb-xl: R² = -0.085 (std: 0.159)
  xgb-l: R² = -0.085 (std: 0.159)
  mlp-adaptive-xl: R² = -0.519 (std: 0.098)
  mlp-l: R² = -0.558 (std: 0.128)
  svr-rbf-xl: R² = 0.054 (std: 0.098)
  svr-poly-l: R² = 0.054 (std: 0.098)
  knn-tuned-sqrt: R² = -0.022 (std: 0.114)
  knn-tuned-l: R² = -0.022 (std: 0.114)
  ridge: R² = -0.062 (std: 0.086)

Model-based training with 3 models
Best R²: 0.054, Mean R²: -0.098
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9673, entropy=0.7878, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0565
  Round 1/3: Mean predicted reward = 10.047
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.7854, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0749
  Round 2/3: Mean predicted reward = 10.018
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9655, entropy=0.7777, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0910
  Round 3/3: Mean predicted reward = 9.947

  === Progress Analysis ===
  Status: NORMAL

--- Round 19 Results ---
  Mean Oracle Reward: 9.798
  Min Oracle Reward: 5.996
  Max Oracle Reward: 12.480
  Std Oracle Reward: 1.168
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: -0.098, Max: 0.054, Count: 13
  Total Sequences Evaluated: 658

======================================================================
EXPERIMENT ROUND 20/20
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 658

--- Round 20 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ACCGGACTGTGC
  TCTGGAGGCCAA
  TGGAGCCAATTC
  CATCATCGGATG
  CGGGAACTCTAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.792
  Max reward: 12.986
  With intrinsic bonuses: 9.741

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9771, entropy=0.7795, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5091

=== Surrogate Model Training ===
Total samples: 690

Training on 655 samples (removed 35 outliers)
Reward range: [7.14, 12.85], mean: 10.01
  Created 13 candidate models for data size 655
  rf-tuned-l: R² = 0.028 (std: 0.134)
  rf-tuned-xl: R² = 0.013 (std: 0.141)
  gb-tuned-l: R² = 0.018 (std: 0.147)
  gb-tuned-xl: R² = 0.021 (std: 0.147)
  xgb-xl: R² = -0.041 (std: 0.122)
  xgb-l: R² = -0.041 (std: 0.122)
  mlp-adaptive-xl: R² = -0.511 (std: 0.097)
  mlp-l: R² = -0.635 (std: 0.196)
  svr-rbf-xl: R² = 0.077 (std: 0.081)
  svr-poly-l: R² = 0.077 (std: 0.081)
  knn-tuned-sqrt: R² = -0.025 (std: 0.078)
  knn-tuned-l: R² = -0.025 (std: 0.078)
  ridge: R² = -0.025 (std: 0.080)

Model-based training with 6 models
Best R²: 0.077, Mean R²: -0.082
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.7569, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3305
  Round 1/3: Mean predicted reward = 10.081
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.7857, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2600
  Round 2/3: Mean predicted reward = 10.109
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9671, entropy=0.7743, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4609
  Round 3/3: Mean predicted reward = 10.016

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 20 Results ---
  Mean Oracle Reward: 9.770
  Min Oracle Reward: 1.570
  Max Oracle Reward: 12.915
  Std Oracle Reward: 1.926
  Sequence Diversity: 1.000
  Models Used: 6
  Model R² - Mean: -0.082, Max: 0.077, Count: 13
  Total Sequences Evaluated: 690

======================================================================
DyNA PPO ALGORITHM COMPLETE!
======================================================================
Total rounds executed: 20
Total sequences evaluated: 690
Best mean reward: 10.527 (achieved at round 12)

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 20
Final Mean Reward: 9.7696
Best Mean Reward: 10.5274
Best Max Reward: 13.0959
Initial Lr: 0.0003
Final Lr: 0.0003
Total Updates: 100
Final Diversity: 1.0000
Convergence Round: 5
==================================================

Generating learning curves...
Learning curves saved to learning_curves.png
Saving training metrics...
Metrics saved to training_metrics.json

======================================================================
FINAL OPTIMIZED SEQUENCES
======================================================================

Deterministic (Exploitation):
  GGCGCGCGCCAG: 7.867
  GGCGCGCGCCAG: 7.895
  GGCGCGCGCCAG: 7.642
  GGCGCGCGCCAG: 7.757
  GGCGCGCGCCAG: 7.666

Stochastic (Exploration):
  CGCGCCGCGCGC: 9.458
  GCCGCGAGCGAC: 10.479
  GGCGCCACGAGC: 9.941
  GGCGCGCGACGC: 9.161
  CGGCCGCACATG: 11.852

Final Performance:
  Mean reward: 8.972
  Max reward: 11.852
  Std reward: 1.382

Best sequence found: CGGCCGCACATG
   Reward: 11.852

======================================================================
Training complete! Check 'learning_curves.png' and 'training_metrics.json'
======================================================================