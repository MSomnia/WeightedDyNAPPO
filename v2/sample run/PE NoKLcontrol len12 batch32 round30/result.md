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
  Mean reward: 8.668
  Std reward: 2.245
  Min/Max: 0.000 / 12.736

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
  AAATGCCGCGCT
  TAGTGTGGTAGA
  TTCACGGTTAAG
  ACCATTCGTCAG
  TCCAATCGCCAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.682
  Max reward: 12.117
  With intrinsic bonuses: 9.647

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9768, entropy=1.3844, kl_div=0.0000
    Epoch 2: policy_loss=-0.1716, value_loss=0.9764, entropy=1.3822, kl_div=0.0345
    Epoch 4: policy_loss=-0.2066, value_loss=0.9761, entropy=1.3827, kl_div=0.0088
    Epoch 6: policy_loss=-0.2159, value_loss=0.9757, entropy=1.3825, kl_div=-0.0273

=== Surrogate Model Training ===
Total samples: 82

Training on 78 samples (removed 4 outliers)
Reward range: [5.96, 12.74], mean: 9.35
  Created 8 candidate models for data size 78
  rf-xs: R2 = -0.179 (std: 0.593)
  rf-s: R2 = -0.176 (std: 0.488)
  knn-xs: R2 = -0.233 (std: 0.468)
  knn-s: R2 = -0.233 (std: 0.468)
  ridge: R2 = -0.157 (std: 0.388)
  gb-xs: R2 = -0.476 (std: 0.810)
  gp: R2 = -60.979 (std: 41.477)
  svr-rbf-s: R2 = -0.056 (std: 0.209)

Model-based training with 4 models
Best R2: -0.056, Mean R2: -7.811
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9617, entropy=1.3827, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.520
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9626, entropy=1.3823, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.367

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 1 Results ---
  Mean Oracle Reward: 9.634
  Min Oracle Reward: 6.819
  Max Oracle Reward: 12.168
  Std Oracle Reward: 1.167
  Sequence Diversity: 1.000
  Models Used: 4
  Model R² - Mean: -7.811, Max: -0.056, Count: 8
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
  CTTGCCGGCACT
  CAAACATAAACG
  GGTGCTTAGGCG
  GACGGGTATTTA
  GCAGGATTACGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.666
  Max reward: 12.117
  With intrinsic bonuses: 9.654

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=1.3802, kl_div=0.0000
    Epoch 2: policy_loss=-0.0890, value_loss=0.9693, entropy=1.3760, kl_div=0.0099
    Epoch 4: policy_loss=-0.1414, value_loss=0.9691, entropy=1.3702, kl_div=0.0241
    Epoch 6: policy_loss=-0.1871, value_loss=0.9690, entropy=1.3676, kl_div=0.0122

=== Surrogate Model Training ===
Total samples: 114

Training on 108 samples (removed 6 outliers)
Reward range: [6.21, 12.26], mean: 9.46
  Created 11 candidate models for data size 108
  rf-m: R2 = 0.062 (std: 0.084)
  rf-l: R2 = 0.108 (std: 0.107)
  gb-m: R2 = -0.202 (std: 0.225)
  gb-l: R2 = -0.171 (std: 0.199)
  xgb-m: R2 = -0.220 (std: 0.262)
  knn-m: R2 = -0.051 (std: 0.155)
  knn-tuned: R2 = -0.051 (std: 0.155)
  mlp-m: R2 = -1.613 (std: 0.659)
  svr-rbf: R2 = 0.062 (std: 0.135)
  svr-poly: R2 = 0.062 (std: 0.135)
  ridge: R2 = -0.007 (std: 0.118)

Model-based training with 8 models
Best R2: 0.108, Mean R2: -0.184
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9728, entropy=1.3672, kl_div=0.0000
    Epoch 1: policy_loss=-0.0175, value_loss=0.9727, entropy=1.3660, kl_div=0.0101
  Round 1/3: Mean predicted reward = 9.532
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9719, entropy=1.3644, kl_div=0.0000
    Epoch 1: policy_loss=-0.0542, value_loss=0.9718, entropy=1.3618, kl_div=0.0193
  Round 2/3: Mean predicted reward = 9.393
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=1.3588, kl_div=0.0000
    Epoch 1: policy_loss=-0.0460, value_loss=0.9694, entropy=1.3544, kl_div=0.0220
  Round 3/3: Mean predicted reward = 9.417

  === Progress Analysis ===
  Status: NORMAL

--- Round 2 Results ---
  Mean Oracle Reward: 9.669
  Min Oracle Reward: 6.783
  Max Oracle Reward: 11.960
  Std Oracle Reward: 1.111
  Sequence Diversity: 1.000
  Models Used: 8
  Model R² - Mean: -0.184, Max: 0.108, Count: 11
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
  GCGTCCGGCTGG
  AGTCGGTATTGT
  AAGCCGATAGTC
  TTTGAGCGGTCT
  CAATCGCGTGCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.735
  Max reward: 12.016
  With intrinsic bonuses: 9.859

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9673, entropy=1.3495, kl_div=0.0000
    Epoch 2: policy_loss=-0.0406, value_loss=0.9673, entropy=1.3425, kl_div=0.0300
    Epoch 4: policy_loss=-0.0897, value_loss=0.9673, entropy=1.3376, kl_div=0.0484
    Epoch 6: policy_loss=-0.1345, value_loss=0.9673, entropy=1.3357, kl_div=0.0429

=== Surrogate Model Training ===
Total samples: 146

Training on 139 samples (removed 7 outliers)
Reward range: [6.21, 12.74], mean: 9.61
  Created 11 candidate models for data size 139
  rf-m: R2 = 0.087 (std: 0.104)
  rf-l: R2 = 0.088 (std: 0.109)
  gb-m: R2 = -0.041 (std: 0.221)
  gb-l: R2 = -0.039 (std: 0.221)
  xgb-m: R2 = -0.166 (std: 0.191)
  knn-m: R2 = 0.002 (std: 0.090)
  knn-tuned: R2 = 0.002 (std: 0.090)
  mlp-m: R2 = -1.761 (std: 1.034)
  svr-rbf: R2 = 0.098 (std: 0.075)
  svr-poly: R2 = 0.098 (std: 0.075)
  ridge: R2 = 0.036 (std: 0.135)

Model-based training with 10 models
Best R2: 0.098, Mean R2: -0.145
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9659, entropy=1.3367, kl_div=0.0000
    Epoch 1: policy_loss=-0.0147, value_loss=0.9659, entropy=1.3369, kl_div=0.0012
  Round 1/3: Mean predicted reward = 9.545
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9634, entropy=1.3342, kl_div=0.0000
    Epoch 1: policy_loss=-0.0252, value_loss=0.9634, entropy=1.3318, kl_div=0.0131
  Round 2/3: Mean predicted reward = 9.622
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=1.3304, kl_div=0.0000
    Epoch 1: policy_loss=-0.0277, value_loss=0.9705, entropy=1.3259, kl_div=0.0275
  Round 3/3: Mean predicted reward = 9.711

  === Progress Analysis ===
  Status: NORMAL

--- Round 3 Results ---
  Mean Oracle Reward: 9.739
  Min Oracle Reward: 4.158
  Max Oracle Reward: 11.973
  Std Oracle Reward: 1.616
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -0.145, Max: 0.098, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 146

======================================================================
EXPERIMENT ROUND 4/30
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.280
Total data collected: 146
  Performance plateaued, reducing LR to 0.000019

--- Round 4 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0100
Exploration rate: 0.280

--- Generated Sequences (Diversity: 1.000) ---
  GCCAGGGTAATC
  GTCTCATAAGCG
  CAACGGTGTAGC
  GAATCGCCTTAG
  ACAGCTGAGGCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.270
  Max reward: 11.617
  With intrinsic bonuses: 10.324

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9710, entropy=1.3192, kl_div=0.0000
    Epoch 1: policy_loss=-0.0040, value_loss=0.9710, entropy=1.3183, kl_div=0.0050
    Epoch 2: policy_loss=-0.0088, value_loss=0.9710, entropy=1.3174, kl_div=0.0101
    Epoch 3: policy_loss=-0.0141, value_loss=0.9710, entropy=1.3165, kl_div=0.0154

=== Surrogate Model Training ===
Total samples: 178

Training on 171 samples (removed 7 outliers)
Reward range: [6.21, 12.74], mean: 9.72
  Created 11 candidate models for data size 171
  rf-m: R2 = -0.066 (std: 0.237)
  rf-l: R2 = -0.041 (std: 0.257)
  gb-m: R2 = -0.222 (std: 0.283)
  gb-l: R2 = -0.223 (std: 0.281)
  xgb-m: R2 = -0.267 (std: 0.377)
  knn-m: R2 = 0.014 (std: 0.184)
  knn-tuned: R2 = 0.014 (std: 0.184)
  mlp-m: R2 = -1.215 (std: 0.827)
  svr-rbf: R2 = 0.063 (std: 0.113)
  svr-poly: R2 = 0.063 (std: 0.113)
  ridge: R2 = -0.014 (std: 0.134)

Model-based training with 4 models
Best R2: 0.063, Mean R2: -0.172
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=1.3159, kl_div=0.0000
    Epoch 1: policy_loss=-0.0046, value_loss=0.9686, entropy=1.3150, kl_div=0.0080
  Round 1/3: Mean predicted reward = 9.657
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9646, entropy=1.3162, kl_div=0.0000
    Epoch 1: policy_loss=-0.0052, value_loss=0.9646, entropy=1.3152, kl_div=0.0078
  Round 2/3: Mean predicted reward = 9.805
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9741, entropy=1.3123, kl_div=0.0000
    Epoch 1: policy_loss=-0.0014, value_loss=0.9741, entropy=1.3113, kl_div=0.0075
  Round 3/3: Mean predicted reward = 9.727

  === Progress Analysis ===
  Status: NORMAL

--- Round 4 Results ---
  Mean Oracle Reward: 10.221
  Min Oracle Reward: 7.989
  Max Oracle Reward: 11.509
  Std Oracle Reward: 0.960
  Sequence Diversity: 1.000
  Models Used: 4
  Model R² - Mean: -0.172, Max: 0.063, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 178

======================================================================
EXPERIMENT ROUND 5/30
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
  AGGCGGCTCAAT
  ACGCACTGGTCG
  CAGAGGGATTCC
  TTGAGCCCGAAG
  CATGAACGGCTT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.069
  Max reward: 11.469
  With intrinsic bonuses: 10.205

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9771, entropy=1.3106, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0869

=== Surrogate Model Training ===
Total samples: 210

Training on 201 samples (removed 9 outliers)
Reward range: [6.65, 12.74], mean: 9.82
  Created 11 candidate models for data size 201
  rf-m: R2 = -0.068 (std: 0.129)
  rf-l: R2 = -0.093 (std: 0.140)
  gb-m: R2 = -0.189 (std: 0.217)
  gb-l: R2 = -0.192 (std: 0.219)
  xgb-m: R2 = -0.307 (std: 0.253)
  knn-m: R2 = -0.205 (std: 0.265)
  knn-tuned: R2 = -0.205 (std: 0.265)
  mlp-m: R2 = -1.938 (std: 1.194)
  svr-rbf: R2 = -0.035 (std: 0.084)
  svr-poly: R2 = -0.035 (std: 0.084)
  ridge: R2 = -0.077 (std: 0.120)
  Fallback: Using svr-rbf with R2 = -0.035

Model-based training with 1 models
Best R2: -0.035, Mean R2: -0.304
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9731, entropy=1.3103, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.133
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9742, entropy=1.2983, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.119

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 5 Results ---
  Mean Oracle Reward: 10.078
  Min Oracle Reward: 9.112
  Max Oracle Reward: 11.537
  Std Oracle Reward: 0.685
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -0.304, Max: -0.035, Count: 11
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
  AGTCCAATGGGC
  CTATCGGAATGC
  CGGGACATACGT
  ATATGCCGCAGT
  CGTAACGTCGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.772
  Max reward: 11.992
  With intrinsic bonuses: 9.803

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9778, entropy=1.2779, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0904

=== Surrogate Model Training ===
Total samples: 242

Training on 232 samples (removed 10 outliers)
Reward range: [6.65, 12.74], mean: 9.83
  Created 11 candidate models for data size 232
  rf-m: R2 = -0.027 (std: 0.183)
  rf-l: R2 = -0.022 (std: 0.166)
  gb-m: R2 = -0.089 (std: 0.147)
  gb-l: R2 = -0.083 (std: 0.151)
  xgb-m: R2 = -0.229 (std: 0.228)
  knn-m: R2 = -0.209 (std: 0.217)
  knn-tuned: R2 = -0.209 (std: 0.217)
  mlp-m: R2 = -1.157 (std: 0.750)
  svr-rbf: R2 = 0.004 (std: 0.123)
  svr-poly: R2 = 0.004 (std: 0.123)
  ridge: R2 = -0.085 (std: 0.150)

Model-based training with 2 models
Best R2: 0.004, Mean R2: -0.191
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=1.2696, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0837
  Round 1/3: Mean predicted reward = 9.942
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9617, entropy=1.2581, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1169
  Round 2/3: Mean predicted reward = 9.962
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=1.2457, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1472
  Round 3/3: Mean predicted reward = 10.094

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 6 Results ---
  Mean Oracle Reward: 9.775
  Min Oracle Reward: 5.690
  Max Oracle Reward: 12.128
  Std Oracle Reward: 1.315
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -0.191, Max: 0.004, Count: 11
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
  TCGGCTAGAATC
  CGTGTGCACACG
  CGGTACACGATT
  AACTTGCGAGCG
  CCGAAGTCTGGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.113
  Max reward: 12.534
  With intrinsic bonuses: 10.178

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9723, entropy=1.2259, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1436

=== Surrogate Model Training ===
Total samples: 274

Training on 263 samples (removed 11 outliers)
Reward range: [6.68, 12.74], mean: 9.87
  Created 11 candidate models for data size 263
  rf-m: R2 = 0.051 (std: 0.090)
  rf-l: R2 = 0.046 (std: 0.086)
  gb-m: R2 = -0.068 (std: 0.185)
  gb-l: R2 = -0.070 (std: 0.185)
  xgb-m: R2 = -0.099 (std: 0.084)
  knn-m: R2 = -0.172 (std: 0.151)
  knn-tuned: R2 = -0.172 (std: 0.151)
  mlp-m: R2 = -0.816 (std: 0.861)
  svr-rbf: R2 = 0.023 (std: 0.074)
  svr-poly: R2 = 0.023 (std: 0.074)
  ridge: R2 = -0.068 (std: 0.077)

Model-based training with 4 models
Best R2: 0.051, Mean R2: -0.120
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9651, entropy=1.2119, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1633
  Round 1/3: Mean predicted reward = 10.006
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9660, entropy=1.1927, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1675
  Round 2/3: Mean predicted reward = 10.189
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9633, entropy=1.1729, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2129
  Round 3/3: Mean predicted reward = 10.144

  === Progress Analysis ===
  Status: NORMAL

--- Round 7 Results ---
  Mean Oracle Reward: 10.169
  Min Oracle Reward: 7.869
  Max Oracle Reward: 12.305
  Std Oracle Reward: 0.999
  Sequence Diversity: 1.000
  Models Used: 4
  Model R² - Mean: -0.120, Max: 0.051, Count: 11
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
  TCGCATCGGCGA
  TGCACACGTGAG
  CCCGATTGAGGA
  ACTTCGGAAGCG
  CAGCTGAAGCTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.759
  Max reward: 12.716
  With intrinsic bonuses: 9.751

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9745, entropy=1.1476, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1169

=== Surrogate Model Training ===
Total samples: 306

Training on 292 samples (removed 14 outliers)
Reward range: [6.73, 12.74], mean: 9.90
  Created 11 candidate models for data size 292
  rf-m: R2 = 0.030 (std: 0.113)
  rf-l: R2 = 0.043 (std: 0.074)
  gb-m: R2 = 0.041 (std: 0.116)
  gb-l: R2 = 0.042 (std: 0.114)
  xgb-m: R2 = -0.131 (std: 0.114)
  knn-m: R2 = -0.114 (std: 0.052)
  knn-tuned: R2 = -0.114 (std: 0.052)
  mlp-m: R2 = -0.580 (std: 0.419)
  svr-rbf: R2 = 0.071 (std: 0.050)
  svr-poly: R2 = 0.071 (std: 0.050)
  ridge: R2 = -0.072 (std: 0.065)

Model-based training with 6 models
Best R2: 0.071, Mean R2: -0.065
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=1.1358, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1456
  Round 1/3: Mean predicted reward = 10.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9716, entropy=1.1210, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1625
  Round 2/3: Mean predicted reward = 10.022
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=1.1115, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1408
  Round 3/3: Mean predicted reward = 9.971

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 8 Results ---
  Mean Oracle Reward: 9.735
  Min Oracle Reward: 5.839
  Max Oracle Reward: 12.795
  Std Oracle Reward: 1.511
  Sequence Diversity: 1.000
  Models Used: 6
  Model R² - Mean: -0.065, Max: 0.071, Count: 11
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
  TCGGACGCTAGA
  GGCGCTGCATCA
  TGAGAGCCGTAC
  CGAGACCTATGT
  TTGCGAAGCGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.725
  Max reward: 12.005
  With intrinsic bonuses: 9.750

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9626, entropy=1.0954, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0585

=== Surrogate Model Training ===
Total samples: 338

Training on 321 samples (removed 17 outliers)
Reward range: [7.02, 12.74], mean: 9.92
  Created 14 candidate models for data size 321
  rf-tuned-l: R2 = 0.009 (std: 0.100)
  rf-tuned-xl: R2 = 0.046 (std: 0.097)
  gb-tuned-l: R2 = 0.048 (std: 0.134)
  gb-tuned-xl: R2 = 0.052 (std: 0.140)
  xgb-xl: R2 = -0.240 (std: 0.131)
  xgb-l: R2 = -0.240 (std: 0.131)
  mlp-adaptive-xl: R2 = -0.623 (std: 0.457)
  mlp-l: R2 = -0.548 (std: 0.314)
  svr-rbf-xl: R2 = 0.042 (std: 0.101)
  svr-poly-l: R2 = 0.042 (std: 0.101)
  knn-tuned-sqrt: R2 = -0.172 (std: 0.111)
  knn-tuned-l: R2 = -0.172 (std: 0.111)
  ridge: R2 = -0.072 (std: 0.072)
  gp: R2 = -96.730 (std: 29.923)

Model-based training with 6 models
Best R2: 0.052, Mean R2: -7.040
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9662, entropy=1.0902, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0611
  Round 1/3: Mean predicted reward = 9.863
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9653, entropy=1.0829, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0592
  Round 2/3: Mean predicted reward = 9.953
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9663, entropy=1.0824, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0570
  Round 3/3: Mean predicted reward = 10.155

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 9 Results ---
  Mean Oracle Reward: 9.683
  Min Oracle Reward: 1.978
  Max Oracle Reward: 11.787
  Std Oracle Reward: 1.696
  Sequence Diversity: 1.000
  Models Used: 6
  Model R² - Mean: -7.040, Max: 0.052, Count: 14
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
  GTGCCAAGGCAT
  GACCCTGACGTG
  GATAGCCGATTC
  CGCTCGGATAGA
  AGGTCAGGTCCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.886
  Max reward: 11.358
  With intrinsic bonuses: 9.865

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=1.0725, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5466

=== Surrogate Model Training ===
Total samples: 370

Training on 353 samples (removed 17 outliers)
Reward range: [7.02, 12.74], mean: 9.92
  Created 14 candidate models for data size 353
  rf-tuned-l: R2 = 0.042 (std: 0.129)
  rf-tuned-xl: R2 = 0.072 (std: 0.103)
  gb-tuned-l: R2 = 0.092 (std: 0.100)
  gb-tuned-xl: R2 = 0.092 (std: 0.100)
  xgb-xl: R2 = -0.137 (std: 0.126)
  xgb-l: R2 = -0.137 (std: 0.126)
  mlp-adaptive-xl: R2 = -0.566 (std: 0.270)
  mlp-l: R2 = -0.754 (std: 0.338)
  svr-rbf-xl: R2 = 0.041 (std: 0.069)
  svr-poly-l: R2 = 0.041 (std: 0.069)
  knn-tuned-sqrt: R2 = -0.097 (std: 0.083)
  knn-tuned-l: R2 = -0.097 (std: 0.083)
  ridge: R2 = -0.042 (std: 0.073)
  gp: R2 = -95.820 (std: 31.242)

Model-based training with 6 models
Best R2: 0.092, Mean R2: -6.948
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9630, entropy=1.0166, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7458
  Round 1/3: Mean predicted reward = 10.048
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9677, entropy=0.9673, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8749
  Round 2/3: Mean predicted reward = 10.040
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9740, entropy=0.9173, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8305
  Round 3/3: Mean predicted reward = 10.119

  === Progress Analysis ===
  Status: NORMAL

--- Round 10 Results ---
  Mean Oracle Reward: 9.891
  Min Oracle Reward: 7.370
  Max Oracle Reward: 11.685
  Std Oracle Reward: 1.064
  Sequence Diversity: 1.000
  Models Used: 6
  Model R² - Mean: -6.948, Max: 0.092, Count: 14
  Total Sequences Evaluated: 370

======================================================================
EXPERIMENT ROUND 11/30
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
  GTCAGCACGCTG
  CCGTGTGCGCAA
  GAGCGAGTTCCA
  GTAATCTCGCGA
  AAGGGTCGCTCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.059
  Max reward: 12.778
  With intrinsic bonuses: 10.051

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.8671, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4163

=== Surrogate Model Training ===
Total samples: 402

Training on 385 samples (removed 17 outliers)
Reward range: [7.02, 12.74], mean: 9.93
  Created 14 candidate models for data size 385
  rf-tuned-l: R2 = 0.059 (std: 0.102)
  rf-tuned-xl: R2 = 0.070 (std: 0.120)
  gb-tuned-l: R2 = 0.017 (std: 0.088)
  gb-tuned-xl: R2 = 0.017 (std: 0.088)
  xgb-xl: R2 = -0.158 (std: 0.151)
  xgb-l: R2 = -0.158 (std: 0.151)
  mlp-adaptive-xl: R2 = -0.426 (std: 0.244)
  mlp-l: R2 = -0.493 (std: 0.234)
  svr-rbf-xl: R2 = 0.041 (std: 0.087)
  svr-poly-l: R2 = 0.041 (std: 0.087)
  knn-tuned-sqrt: R2 = -0.092 (std: 0.050)
  knn-tuned-l: R2 = -0.092 (std: 0.050)
  ridge: R2 = -0.033 (std: 0.059)
  gp: R2 = -91.236 (std: 21.443)

Model-based training with 6 models
Best R2: 0.070, Mean R2: -6.603
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9672, entropy=0.8439, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4390
  Round 1/3: Mean predicted reward = 10.022
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9614, entropy=0.8097, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4977
  Round 2/3: Mean predicted reward = 9.892
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.8053, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4460
  Round 3/3: Mean predicted reward = 9.986

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 11 Results ---
  Mean Oracle Reward: 10.055
  Min Oracle Reward: 7.948
  Max Oracle Reward: 12.596
  Std Oracle Reward: 1.151
  Sequence Diversity: 1.000
  Models Used: 6
  Model R² - Mean: -6.603, Max: 0.070, Count: 14
  Total Sequences Evaluated: 402

======================================================================
EXPERIMENT ROUND 12/30
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
  GTGATGCCAAGC
  CGCTCGGATCAG
  GACGCAGTATGC
  CCTGCAGGATCG
  GAAGCCCAGGTT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.923
  Max reward: 12.467
  With intrinsic bonuses: 9.943

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9741, entropy=0.7682, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8543

=== Surrogate Model Training ===
Total samples: 434

Training on 417 samples (removed 17 outliers)
Reward range: [6.90, 12.74], mean: 9.93
  Created 14 candidate models for data size 417
  rf-tuned-l: R2 = 0.045 (std: 0.031)
  rf-tuned-xl: R2 = 0.025 (std: 0.043)
  gb-tuned-l: R2 = 0.024 (std: 0.053)
  gb-tuned-xl: R2 = 0.025 (std: 0.054)
  xgb-xl: R2 = -0.188 (std: 0.125)
  xgb-l: R2 = -0.188 (std: 0.125)
  mlp-adaptive-xl: R2 = -0.483 (std: 0.543)
  mlp-l: R2 = -0.415 (std: 0.238)
  svr-rbf-xl: R2 = 0.031 (std: 0.065)
  svr-poly-l: R2 = 0.031 (std: 0.065)
  knn-tuned-sqrt: R2 = -0.120 (std: 0.132)
  knn-tuned-l: R2 = -0.120 (std: 0.132)
  ridge: R2 = -0.048 (std: 0.045)
  gp: R2 = -90.653 (std: 28.756)

Model-based training with 6 models
Best R2: 0.045, Mean R2: -6.574
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9660, entropy=0.7334, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9736
  Round 1/3: Mean predicted reward = 9.987
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9723, entropy=0.6962, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8955
  Round 2/3: Mean predicted reward = 9.904
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9662, entropy=0.6789, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8954
  Round 3/3: Mean predicted reward = 10.054

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 12 Results ---
  Mean Oracle Reward: 9.897
  Min Oracle Reward: 7.121
  Max Oracle Reward: 12.644
  Std Oracle Reward: 1.263
  Sequence Diversity: 1.000
  Models Used: 6
  Model R² - Mean: -6.574, Max: 0.045, Count: 14
  Total Sequences Evaluated: 434

======================================================================
EXPERIMENT ROUND 13/30
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 434
  Performance plateaued, reducing LR to 0.000055

--- Round 13 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGGAGCTTCAAC
  TAGCACGGTACG
  GAAATCGGGCCT
  CGCCTCGAGGTA
  TGAAAGGCCTTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.186
  Max reward: 12.257
  With intrinsic bonuses: 9.182

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9847, entropy=0.6679, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1430

=== Surrogate Model Training ===
Total samples: 466

Training on 448 samples (removed 18 outliers)
Reward range: [6.73, 12.74], mean: 9.91
  Created 14 candidate models for data size 448
  rf-tuned-l: R2 = 0.044 (std: 0.028)
  rf-tuned-xl: R2 = 0.053 (std: 0.025)
  gb-tuned-l: R2 = -0.013 (std: 0.059)
  gb-tuned-xl: R2 = -0.012 (std: 0.059)
  xgb-xl: R2 = -0.127 (std: 0.094)
  xgb-l: R2 = -0.127 (std: 0.094)
  mlp-adaptive-xl: R2 = -0.452 (std: 0.252)
  mlp-l: R2 = -0.394 (std: 0.291)
  svr-rbf-xl: R2 = 0.017 (std: 0.070)
  svr-poly-l: R2 = 0.017 (std: 0.070)
  knn-tuned-sqrt: R2 = -0.147 (std: 0.034)
  knn-tuned-l: R2 = -0.147 (std: 0.034)
  ridge: R2 = -0.056 (std: 0.044)
  gp: R2 = -80.988 (std: 20.107)

Model-based training with 4 models
Best R2: 0.053, Mean R2: -5.881
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9647, entropy=0.6402, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1968
  Round 1/3: Mean predicted reward = 9.860
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9718, entropy=0.6259, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1907
  Round 2/3: Mean predicted reward = 10.011
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9645, entropy=0.6478, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1707
  Round 3/3: Mean predicted reward = 9.855

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 13 Results ---
  Mean Oracle Reward: 9.180
  Min Oracle Reward: 0.000
  Max Oracle Reward: 12.118
  Std Oracle Reward: 2.605
  Sequence Diversity: 1.000
  Models Used: 4
  Model R² - Mean: -5.881, Max: 0.053, Count: 14
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
  GAGCCCCTATGG
  GTTGCCCCGGAA
  GCGCTCTCAGAG
  GAATGCTACCGT
  GAGCTCGCCAGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.341
  Max reward: 12.003
  With intrinsic bonuses: 9.385

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9771, entropy=0.6416, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0833

=== Surrogate Model Training ===
Total samples: 498

Training on 481 samples (removed 17 outliers)
Reward range: [6.54, 12.74], mean: 9.88
  Created 14 candidate models for data size 481
  rf-tuned-l: R2 = 0.036 (std: 0.063)
  rf-tuned-xl: R2 = 0.047 (std: 0.047)
  gb-tuned-l: R2 = -0.017 (std: 0.044)
  gb-tuned-xl: R2 = -0.017 (std: 0.044)
  xgb-xl: R2 = -0.135 (std: 0.054)
  xgb-l: R2 = -0.135 (std: 0.054)
  mlp-adaptive-xl: R2 = -0.521 (std: 0.266)
  mlp-l: R2 = -0.465 (std: 0.368)
  svr-rbf-xl: R2 = 0.021 (std: 0.048)
  svr-poly-l: R2 = 0.021 (std: 0.048)
  knn-tuned-sqrt: R2 = -0.089 (std: 0.088)
  knn-tuned-l: R2 = -0.089 (std: 0.088)
  ridge: R2 = -0.072 (std: 0.055)
  gp: R2 = -77.496 (std: 22.744)

Model-based training with 4 models
Best R2: 0.047, Mean R2: -5.637
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.6117, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1131
  Round 1/3: Mean predicted reward = 9.756
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9743, entropy=0.6256, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0591
  Round 2/3: Mean predicted reward = 9.914
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.6433, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0748
  Round 3/3: Mean predicted reward = 9.958

  === Progress Analysis ===
  Status: NORMAL

--- Round 14 Results ---
  Mean Oracle Reward: 9.359
  Min Oracle Reward: 3.347
  Max Oracle Reward: 12.135
  Std Oracle Reward: 1.744
  Sequence Diversity: 1.000
  Models Used: 4
  Model R² - Mean: -5.637, Max: 0.047, Count: 14
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
  GATGGCCTCGCA
  ACATCGGGTGCC
  TCGGATAGGCAC
  GGGTCCAGACTA
  ACTACTGCAGGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.556
  Max reward: 12.566
  With intrinsic bonuses: 9.554

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9662, entropy=0.6203, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8424

=== Surrogate Model Training ===
Total samples: 530

Training on 511 samples (removed 19 outliers)
Reward range: [6.54, 12.74], mean: 9.87
  Created 13 candidate models for data size 511
  rf-tuned-l: R2 = 0.033 (std: 0.052)
  rf-tuned-xl: R2 = 0.010 (std: 0.034)
  gb-tuned-l: R2 = -0.047 (std: 0.079)
  gb-tuned-xl: R2 = -0.047 (std: 0.079)
  xgb-xl: R2 = -0.153 (std: 0.110)
  xgb-l: R2 = -0.153 (std: 0.110)
  mlp-adaptive-xl: R2 = -0.310 (std: 0.212)
  mlp-l: R2 = -0.349 (std: 0.236)
  svr-rbf-xl: R2 = 0.006 (std: 0.056)
  svr-poly-l: R2 = 0.006 (std: 0.056)
  knn-tuned-sqrt: R2 = -0.104 (std: 0.110)
  knn-tuned-l: R2 = -0.104 (std: 0.110)
  ridge: R2 = -0.071 (std: 0.036)

Model-based training with 4 models
Best R2: 0.033, Mean R2: -0.099
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9672, entropy=0.6038, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9181
  Round 1/3: Mean predicted reward = 9.913
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9670, entropy=0.5976, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8995
  Round 2/3: Mean predicted reward = 9.927
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.5818, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7770
  Round 3/3: Mean predicted reward = 9.978

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 15 Results ---
  Mean Oracle Reward: 9.530
  Min Oracle Reward: 4.941
  Max Oracle Reward: 12.513
  Std Oracle Reward: 1.508
  Sequence Diversity: 1.000
  Models Used: 4
  Model R² - Mean: -0.099, Max: 0.033, Count: 13
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
  CGGAATCTACGG
  TGAATCCATGCG
  CGATATTGGACC
  CTTGGCGCGAAC
  GCATGACGCTCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.071
  Max reward: 12.682
  With intrinsic bonuses: 10.074

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9716, entropy=0.5598, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0651

=== Surrogate Model Training ===
Total samples: 562

Training on 542 samples (removed 20 outliers)
Reward range: [6.65, 12.74], mean: 9.89
  Created 13 candidate models for data size 542
  rf-tuned-l: R2 = 0.059 (std: 0.082)
  rf-tuned-xl: R2 = 0.038 (std: 0.108)
  gb-tuned-l: R2 = -0.009 (std: 0.083)
  gb-tuned-xl: R2 = -0.009 (std: 0.083)
  xgb-xl: R2 = -0.081 (std: 0.234)
  xgb-l: R2 = -0.081 (std: 0.234)
  mlp-adaptive-xl: R2 = -0.307 (std: 0.307)
  mlp-l: R2 = -0.245 (std: 0.250)
  svr-rbf-xl: R2 = 0.062 (std: 0.048)
  svr-poly-l: R2 = 0.062 (std: 0.048)
  knn-tuned-sqrt: R2 = -0.062 (std: 0.150)
  knn-tuned-l: R2 = -0.062 (std: 0.150)
  ridge: R2 = -0.059 (std: 0.051)

Model-based training with 4 models
Best R2: 0.062, Mean R2: -0.054
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9707, entropy=0.5611, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7298
  Round 1/3: Mean predicted reward = 9.841
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.5858, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6484
  Round 2/3: Mean predicted reward = 9.906
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.5228, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0972
  Round 3/3: Mean predicted reward = 10.044

  === Progress Analysis ===
  Status: NORMAL

--- Round 16 Results ---
  Mean Oracle Reward: 10.074
  Min Oracle Reward: 8.260
  Max Oracle Reward: 12.954
  Std Oracle Reward: 1.099
  Sequence Diversity: 1.000
  Models Used: 4
  Model R² - Mean: -0.054, Max: 0.062, Count: 13
  Total Sequences Evaluated: 562

======================================================================
EXPERIMENT ROUND 17/30
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 562
  Consistent improvement, increasing LR to 0.000240

--- Round 17 Configuration ---
Learning rate: 0.000240
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGACGGTTAAGC
  CTAGCGTCAGGC
  GCTCTCAAGGGC
  TAGGCGACACTT
  CATGGCGCAGCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.694
  Max reward: 12.054
  With intrinsic bonuses: 9.731

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9711, entropy=0.5262, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8511

=== Surrogate Model Training ===
Total samples: 594

Training on 574 samples (removed 20 outliers)
Reward range: [6.54, 12.74], mean: 9.88
  Created 13 candidate models for data size 574
  rf-tuned-l: R2 = 0.078 (std: 0.032)
  rf-tuned-xl: R2 = 0.072 (std: 0.035)
  gb-tuned-l: R2 = 0.043 (std: 0.018)
  gb-tuned-xl: R2 = 0.043 (std: 0.018)
  xgb-xl: R2 = -0.064 (std: 0.133)
  xgb-l: R2 = -0.064 (std: 0.133)
  mlp-adaptive-xl: R2 = -0.128 (std: 0.142)
  mlp-l: R2 = -0.227 (std: 0.170)
  svr-rbf-xl: R2 = 0.087 (std: 0.025)
  svr-poly-l: R2 = 0.087 (std: 0.025)
  knn-tuned-sqrt: R2 = -0.043 (std: 0.057)
  knn-tuned-l: R2 = -0.043 (std: 0.057)
  ridge: R2 = -0.036 (std: 0.033)

Model-based training with 6 models
Best R2: 0.087, Mean R2: -0.015
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9766, entropy=0.5248, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5421
  Round 1/3: Mean predicted reward = 9.769
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.5261, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4895
  Round 2/3: Mean predicted reward = 9.825
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.5182, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6922
  Round 3/3: Mean predicted reward = 9.863

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 17 Results ---
  Mean Oracle Reward: 9.678
  Min Oracle Reward: 4.642
  Max Oracle Reward: 11.833
  Std Oracle Reward: 1.466
  Sequence Diversity: 1.000
  Models Used: 6
  Model R² - Mean: -0.015, Max: 0.087, Count: 13
  Total Sequences Evaluated: 594

======================================================================
EXPERIMENT ROUND 18/30
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 594

--- Round 18 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCGGCAAAGTTG
  TGGGGAAACCCT
  ACGGTCAGATGC
  GTTTCCCGAAAG
  GGTTTGCACCAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.722
  Max reward: 12.323
  With intrinsic bonuses: 9.694

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9707, entropy=0.5135, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2783

=== Surrogate Model Training ===
Total samples: 626

Training on 605 samples (removed 21 outliers)
Reward range: [6.54, 12.74], mean: 9.88
  Created 13 candidate models for data size 605
  rf-tuned-l: R2 = 0.097 (std: 0.040)
  rf-tuned-xl: R2 = 0.098 (std: 0.046)
  gb-tuned-l: R2 = 0.082 (std: 0.067)
  gb-tuned-xl: R2 = 0.084 (std: 0.066)
  xgb-xl: R2 = -0.045 (std: 0.068)
  xgb-l: R2 = -0.045 (std: 0.068)
  mlp-adaptive-xl: R2 = -0.177 (std: 0.183)
  mlp-l: R2 = -0.134 (std: 0.171)
  svr-rbf-xl: R2 = 0.120 (std: 0.058)
  svr-poly-l: R2 = 0.120 (std: 0.058)
  knn-tuned-sqrt: R2 = -0.011 (std: 0.079)
  knn-tuned-l: R2 = -0.011 (std: 0.079)
  ridge: R2 = -0.015 (std: 0.037)

Model-based training with 6 models
Best R2: 0.120, Mean R2: 0.012
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9670, entropy=0.5099, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3283
  Round 1/3: Mean predicted reward = 9.798
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.5087, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2984
  Round 2/3: Mean predicted reward = 9.748
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9711, entropy=0.5105, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3571
  Round 3/3: Mean predicted reward = 9.940

  === Progress Analysis ===
  Status: NORMAL

--- Round 18 Results ---
  Mean Oracle Reward: 9.710
  Min Oracle Reward: 5.721
  Max Oracle Reward: 12.049
  Std Oracle Reward: 1.436
  Sequence Diversity: 1.000
  Models Used: 6
  Model R² - Mean: 0.012, Max: 0.120, Count: 13
  Total Sequences Evaluated: 626

======================================================================
EXPERIMENT ROUND 19/30
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 626

--- Round 19 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCCAGATAGGCT
  ATACGCCTGGCG
  TACGCGTCGGAC
  GCATCGACCTGG
  CGCGAGCCTGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.066
  Max reward: 12.201
  With intrinsic bonuses: 10.071

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9733, entropy=0.5060, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0802

=== Surrogate Model Training ===
Total samples: 658

Training on 636 samples (removed 22 outliers)
Reward range: [6.65, 12.74], mean: 9.89
  Created 13 candidate models for data size 636
  rf-tuned-l: R2 = 0.052 (std: 0.038)
  rf-tuned-xl: R2 = 0.072 (std: 0.062)
  gb-tuned-l: R2 = 0.068 (std: 0.092)
  gb-tuned-xl: R2 = 0.068 (std: 0.092)
  xgb-xl: R2 = -0.084 (std: 0.069)
  xgb-l: R2 = -0.084 (std: 0.069)
  mlp-adaptive-xl: R2 = -0.173 (std: 0.269)
  mlp-l: R2 = -0.176 (std: 0.168)
  svr-rbf-xl: R2 = 0.108 (std: 0.093)
  svr-poly-l: R2 = 0.108 (std: 0.093)
  knn-tuned-sqrt: R2 = -0.070 (std: 0.087)
  knn-tuned-l: R2 = -0.070 (std: 0.087)
  ridge: R2 = -0.042 (std: 0.045)

Model-based training with 6 models
Best R2: 0.108, Mean R2: -0.017
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.4830, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0934
  Round 1/3: Mean predicted reward = 9.869
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9710, entropy=0.4894, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1061
  Round 2/3: Mean predicted reward = 9.811
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9662, entropy=0.4925, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1269
  Round 3/3: Mean predicted reward = 9.913

  === Progress Analysis ===
  Status: NORMAL

--- Round 19 Results ---
  Mean Oracle Reward: 10.075
  Min Oracle Reward: 7.375
  Max Oracle Reward: 12.175
  Std Oracle Reward: 1.151
  Sequence Diversity: 1.000
  Models Used: 6
  Model R² - Mean: -0.017, Max: 0.108, Count: 13
  Total Sequences Evaluated: 658

======================================================================
EXPERIMENT ROUND 20/30
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 658
  Consistent improvement, increasing LR to 0.000360

--- Round 20 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGACCCCTGTGA
  GTAGACCCTGAG
  TCGAGGCGTCCA
  GAACCGCGTCGT
  CGTCGTGACCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.238
  Max reward: 12.510
  With intrinsic bonuses: 10.212

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9712, entropy=0.5221, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0481

=== Surrogate Model Training ===
Total samples: 690

Training on 667 samples (removed 23 outliers)
Reward range: [6.65, 12.74], mean: 9.92
  Created 13 candidate models for data size 667
  rf-tuned-l: R2 = 0.084 (std: 0.059)
  rf-tuned-xl: R2 = 0.090 (std: 0.055)
  gb-tuned-l: R2 = 0.063 (std: 0.082)
  gb-tuned-xl: R2 = 0.063 (std: 0.082)
  xgb-xl: R2 = -0.043 (std: 0.084)
  xgb-l: R2 = -0.043 (std: 0.084)
  mlp-adaptive-xl: R2 = -0.180 (std: 0.156)
  mlp-l: R2 = -0.100 (std: 0.137)
  svr-rbf-xl: R2 = 0.110 (std: 0.118)
  svr-poly-l: R2 = 0.110 (std: 0.118)
  knn-tuned-sqrt: R2 = -0.036 (std: 0.057)
  knn-tuned-l: R2 = -0.036 (std: 0.057)
  ridge: R2 = -0.045 (std: 0.040)

Model-based training with 6 models
Best R2: 0.110, Mean R2: 0.003
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9779, entropy=0.4903, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7935
  Round 1/3: Mean predicted reward = 9.954
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.4743, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0506
  Round 2/3: Mean predicted reward = 9.842
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.4556, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.3332
  Round 3/3: Mean predicted reward = 9.781

  === Progress Analysis ===
  Status: NORMAL

--- Round 20 Results ---
  Mean Oracle Reward: 10.268
  Min Oracle Reward: 5.271
  Max Oracle Reward: 12.913
  Std Oracle Reward: 1.333
  Sequence Diversity: 1.000
  Models Used: 6
  Model R² - Mean: 0.003, Max: 0.110, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 690

======================================================================
EXPERIMENT ROUND 21/30
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
  CCAGTGCTGCAG
  GGGCGATCCATA
  GGGGCAATTCCC
  CGCTACGTGACG
  GTGGAACCGCTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.162
  Max reward: 12.527
  With intrinsic bonuses: 10.178

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9710, entropy=0.4564, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.2060

=== Surrogate Model Training ===
Total samples: 722

Training on 699 samples (removed 23 outliers)
Reward range: [6.65, 12.74], mean: 9.93
  Created 13 candidate models for data size 699
  rf-tuned-l: R2 = 0.131 (std: 0.015)
  rf-tuned-xl: R2 = 0.101 (std: 0.034)
  gb-tuned-l: R2 = 0.074 (std: 0.049)
  gb-tuned-xl: R2 = 0.074 (std: 0.049)
  xgb-xl: R2 = -0.009 (std: 0.035)
  xgb-l: R2 = -0.009 (std: 0.035)
  mlp-adaptive-xl: R2 = -0.107 (std: 0.149)
  mlp-l: R2 = -0.070 (std: 0.119)
  svr-rbf-xl: R2 = 0.131 (std: 0.071)
  svr-poly-l: R2 = 0.131 (std: 0.071)
  knn-tuned-sqrt: R2 = 0.004 (std: 0.043)
  knn-tuned-l: R2 = 0.004 (std: 0.043)
  ridge: R2 = -0.025 (std: 0.028)

Model-based training with 8 models
Best R2: 0.131, Mean R2: 0.033
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9748, entropy=0.4580, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6511
  Round 1/3: Mean predicted reward = 9.716
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9671, entropy=0.4349, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7563
  Round 2/3: Mean predicted reward = 9.932
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9741, entropy=0.4573, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3139
  Round 3/3: Mean predicted reward = 10.014

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 21 Results ---
  Mean Oracle Reward: 10.176
  Min Oracle Reward: 7.842
  Max Oracle Reward: 12.318
  Std Oracle Reward: 1.098
  Sequence Diversity: 1.000
  Models Used: 8
  Model R² - Mean: 0.033, Max: 0.131, Count: 13
  Total Sequences Evaluated: 722

======================================================================
EXPERIMENT ROUND 22/30
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
  GCCAGTCTAGCG
  AGAACTGCGCTG
  CGGCATTGAGCC
  GGGCACCTTAGC
  ACGCTCGAGTAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.977
  Max reward: 12.740
  With intrinsic bonuses: 10.040

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9619, entropy=0.4258, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2037

=== Surrogate Model Training ===
Total samples: 754

Training on 730 samples (removed 24 outliers)
Reward range: [6.65, 12.74], mean: 9.94
  Created 13 candidate models for data size 730
  rf-tuned-l: R2 = 0.150 (std: 0.038)
  rf-tuned-xl: R2 = 0.150 (std: 0.047)
  gb-tuned-l: R2 = 0.086 (std: 0.028)
  gb-tuned-xl: R2 = 0.087 (std: 0.029)
  xgb-xl: R2 = 0.025 (std: 0.073)
  xgb-l: R2 = 0.025 (std: 0.073)
  mlp-adaptive-xl: R2 = -0.097 (std: 0.175)
  mlp-l: R2 = -0.151 (std: 0.173)
  svr-rbf-xl: R2 = 0.143 (std: 0.044)
  svr-poly-l: R2 = 0.143 (std: 0.044)
  knn-tuned-sqrt: R2 = 0.017 (std: 0.049)
  knn-tuned-l: R2 = 0.017 (std: 0.049)
  ridge: R2 = -0.017 (std: 0.022)

Model-based training with 10 models
Best R2: 0.150, Mean R2: 0.044
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9669, entropy=0.4426, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0574
  Round 1/3: Mean predicted reward = 9.704
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.4516, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1149
  Round 2/3: Mean predicted reward = 9.826
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9682, entropy=0.4276, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2303
  Round 3/3: Mean predicted reward = 10.071

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 22 Results ---
  Mean Oracle Reward: 9.972
  Min Oracle Reward: 4.243
  Max Oracle Reward: 12.611
  Std Oracle Reward: 1.607
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: 0.044, Max: 0.150, Count: 13
  Total Sequences Evaluated: 754

======================================================================
EXPERIMENT ROUND 23/30
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 754

--- Round 23 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGGTACCGTCCA
  TGAGACCGATCG
  CGGCTACAGGTC
  CACGGACTGCTG
  CTCAGGAGTGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.432
  Max reward: 12.669
  With intrinsic bonuses: 10.408

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9676, entropy=0.4309, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2908

=== Surrogate Model Training ===
Total samples: 786

Training on 762 samples (removed 24 outliers)
Reward range: [6.65, 12.76], mean: 9.96
  Created 13 candidate models for data size 762
  rf-tuned-l: R2 = 0.127 (std: 0.044)
  rf-tuned-xl: R2 = 0.125 (std: 0.045)
  gb-tuned-l: R2 = 0.094 (std: 0.032)
  gb-tuned-xl: R2 = 0.094 (std: 0.032)
  xgb-xl: R2 = 0.039 (std: 0.109)
  xgb-l: R2 = 0.039 (std: 0.109)
  mlp-adaptive-xl: R2 = -0.055 (std: 0.119)
  mlp-l: R2 = -0.049 (std: 0.104)
  svr-rbf-xl: R2 = 0.128 (std: 0.046)
  svr-poly-l: R2 = 0.128 (std: 0.046)
  knn-tuned-sqrt: R2 = 0.014 (std: 0.038)
  knn-tuned-l: R2 = 0.014 (std: 0.038)
  ridge: R2 = -0.009 (std: 0.021)

Model-based training with 10 models
Best R2: 0.128, Mean R2: 0.053
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9748, entropy=0.4072, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2239
  Round 1/3: Mean predicted reward = 9.771
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9704, entropy=0.4157, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2640
  Round 2/3: Mean predicted reward = 9.819
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9656, entropy=0.4460, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3505
  Round 3/3: Mean predicted reward = 10.042

  === Progress Analysis ===
  Status: NORMAL

--- Round 23 Results ---
  Mean Oracle Reward: 10.401
  Min Oracle Reward: 8.709
  Max Oracle Reward: 12.721
  Std Oracle Reward: 0.920
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: 0.053, Max: 0.128, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 786

======================================================================
EXPERIMENT ROUND 24/30
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 786

--- Round 24 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TAGGCGCCCTGA
  AGGTTCGACCCG
  TCCCAGCGGTAG
  CAACGCCGGTTG
  CCCCTGGTGAGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.279
  Max reward: 13.195
  With intrinsic bonuses: 10.297

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9625, entropy=0.4016, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1718

=== Surrogate Model Training ===
Total samples: 818

Training on 792 samples (removed 26 outliers)
Reward range: [6.68, 13.02], mean: 9.98
  Created 13 candidate models for data size 792
  rf-tuned-l: R2 = 0.144 (std: 0.047)
  rf-tuned-xl: R2 = 0.143 (std: 0.039)
  gb-tuned-l: R2 = 0.125 (std: 0.041)
  gb-tuned-xl: R2 = 0.125 (std: 0.041)
  xgb-xl: R2 = 0.056 (std: 0.082)
  xgb-l: R2 = 0.056 (std: 0.082)
  mlp-adaptive-xl: R2 = -0.040 (std: 0.141)
  mlp-l: R2 = -0.060 (std: 0.116)
  svr-rbf-xl: R2 = 0.142 (std: 0.068)
  svr-poly-l: R2 = 0.142 (std: 0.068)
  knn-tuned-sqrt: R2 = 0.034 (std: 0.053)
  knn-tuned-l: R2 = 0.034 (std: 0.053)
  ridge: R2 = -0.018 (std: 0.045)

Model-based training with 10 models
Best R2: 0.144, Mean R2: 0.068
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9663, entropy=0.4028, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1712
  Round 1/3: Mean predicted reward = 9.850
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9741, entropy=0.4447, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0863
  Round 2/3: Mean predicted reward = 9.920
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9722, entropy=0.4250, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1321
  Round 3/3: Mean predicted reward = 10.072

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 24 Results ---
  Mean Oracle Reward: 10.350
  Min Oracle Reward: 6.236
  Max Oracle Reward: 13.114
  Std Oracle Reward: 1.272
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: 0.068, Max: 0.144, Count: 13
  Total Sequences Evaluated: 818

======================================================================
EXPERIMENT ROUND 25/30
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 818

--- Round 25 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TTACACGGCGGC
  GATCCCCGGGAT
  ACGCGGCTATGA
  GCGGCAAGTCTA
  GATGACCGGTCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.949
  Max reward: 11.623
  With intrinsic bonuses: 9.937

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9677, entropy=0.4139, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0702

=== Surrogate Model Training ===
Total samples: 850

Training on 824 samples (removed 26 outliers)
Reward range: [6.68, 13.02], mean: 9.98
  Created 13 candidate models for data size 824
  rf-tuned-l: R2 = 0.152 (std: 0.044)
  rf-tuned-xl: R2 = 0.156 (std: 0.046)
  gb-tuned-l: R2 = 0.139 (std: 0.054)
  gb-tuned-xl: R2 = 0.139 (std: 0.054)
  xgb-xl: R2 = 0.021 (std: 0.074)
  xgb-l: R2 = 0.021 (std: 0.074)
  mlp-adaptive-xl: R2 = -0.027 (std: 0.081)
  mlp-l: R2 = -0.012 (std: 0.100)
  svr-rbf-xl: R2 = 0.151 (std: 0.069)
  svr-poly-l: R2 = 0.151 (std: 0.069)
  knn-tuned-sqrt: R2 = 0.012 (std: 0.049)
  knn-tuned-l: R2 = 0.012 (std: 0.049)
  ridge: R2 = -0.012 (std: 0.034)

Model-based training with 10 models
Best R2: 0.156, Mean R2: 0.070
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.3846, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7537
  Round 1/3: Mean predicted reward = 9.762
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9713, entropy=0.4194, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6540
  Round 2/3: Mean predicted reward = 9.971
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9714, entropy=0.4105, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5765
  Round 3/3: Mean predicted reward = 9.882

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 25 Results ---
  Mean Oracle Reward: 10.038
  Min Oracle Reward: 6.923
  Max Oracle Reward: 11.729
  Std Oracle Reward: 1.186
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: 0.070, Max: 0.156, Count: 13
  Total Sequences Evaluated: 850

======================================================================
EXPERIMENT ROUND 26/30
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 850

--- Round 26 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGTACAGGCTCG
  TCTGCCGGAGAC
  TCGCCATGAGGC
  TAGGCTCACGCG
  CAATCCGGCGTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.478
  Max reward: 12.971
  With intrinsic bonuses: 10.459

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9632, entropy=0.3843, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8867

=== Surrogate Model Training ===
Total samples: 882

Training on 853 samples (removed 29 outliers)
Reward range: [6.78, 13.02], mean: 10.01
  Created 13 candidate models for data size 853
  rf-tuned-l: R2 = 0.143 (std: 0.061)
  rf-tuned-xl: R2 = 0.131 (std: 0.072)
  gb-tuned-l: R2 = 0.125 (std: 0.052)
  gb-tuned-xl: R2 = 0.125 (std: 0.052)
  xgb-xl: R2 = 0.042 (std: 0.088)
  xgb-l: R2 = 0.042 (std: 0.088)
  mlp-adaptive-xl: R2 = -0.002 (std: 0.044)
  mlp-l: R2 = -0.004 (std: 0.061)
  svr-rbf-xl: R2 = 0.150 (std: 0.073)
  svr-poly-l: R2 = 0.150 (std: 0.073)
  knn-tuned-sqrt: R2 = -0.020 (std: 0.041)
  knn-tuned-l: R2 = -0.020 (std: 0.041)
  ridge: R2 = -0.015 (std: 0.038)

Model-based training with 8 models
Best R2: 0.150, Mean R2: 0.065
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9678, entropy=0.3695, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6811
  Round 1/3: Mean predicted reward = 9.769
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9718, entropy=0.3976, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1288
  Round 2/3: Mean predicted reward = 9.799
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.3931, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2232
  Round 3/3: Mean predicted reward = 10.019

  === Progress Analysis ===
  Status: NORMAL

--- Round 26 Results ---
  Mean Oracle Reward: 10.492
  Min Oracle Reward: 7.284
  Max Oracle Reward: 12.704
  Std Oracle Reward: 1.210
  Sequence Diversity: 1.000
  Models Used: 8
  Model R² - Mean: 0.065, Max: 0.150, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 882

======================================================================
EXPERIMENT ROUND 27/30
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 882

--- Round 27 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCAGCTTGGCCA
  TAACTCGCGGGC
  ATTACGTCACGG
  GCGTTCGCCAGA
  AGCTGCCCGTAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.368
  Max reward: 12.543
  With intrinsic bonuses: 10.364

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9664, entropy=0.3863, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4623

=== Surrogate Model Training ===
Total samples: 914

Training on 882 samples (removed 32 outliers)
Reward range: [6.88, 13.02], mean: 10.03
  Created 13 candidate models for data size 882
  rf-tuned-l: R2 = 0.157 (std: 0.070)
  rf-tuned-xl: R2 = 0.154 (std: 0.060)
  gb-tuned-l: R2 = 0.150 (std: 0.061)
  gb-tuned-xl: R2 = 0.150 (std: 0.061)
  xgb-xl: R2 = 0.084 (std: 0.061)
  xgb-l: R2 = 0.084 (std: 0.061)
  mlp-adaptive-xl: R2 = -0.045 (std: 0.083)
  mlp-l: R2 = -0.033 (std: 0.076)
  svr-rbf-xl: R2 = 0.155 (std: 0.100)
  svr-poly-l: R2 = 0.155 (std: 0.100)
  knn-tuned-sqrt: R2 = 0.002 (std: 0.051)
  knn-tuned-l: R2 = 0.002 (std: 0.051)
  ridge: R2 = -0.008 (std: 0.045)

Model-based training with 10 models
Best R2: 0.157, Mean R2: 0.077
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9750, entropy=0.4115, kl_div=0.0000
    Epoch 1: policy_loss=-0.0415, value_loss=0.9750, entropy=0.4140, kl_div=0.0335
  Round 1/3: Mean predicted reward = 9.979
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9674, entropy=0.4204, kl_div=0.0000
    Epoch 1: policy_loss=0.0551, value_loss=0.9674, entropy=0.4267, kl_div=-0.4065
  Round 2/3: Mean predicted reward = 9.991
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9670, entropy=0.4135, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0621
  Round 3/3: Mean predicted reward = 10.081

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 27 Results ---
  Mean Oracle Reward: 10.379
  Min Oracle Reward: 6.660
  Max Oracle Reward: 12.810
  Std Oracle Reward: 1.198
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: 0.077, Max: 0.157, Count: 13
  Total Sequences Evaluated: 914

======================================================================
EXPERIMENT ROUND 28/30
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 914

--- Round 28 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTCGGTGAACAG
  CGAGGTGCCACT
  TTGCCAGGACGC
  GCCTGCGATACG
  CGCGTACAGGCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.661
  Max reward: 13.167
  With intrinsic bonuses: 10.612

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9628, entropy=0.4202, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1511

=== Surrogate Model Training ===
Total samples: 946

Training on 914 samples (removed 32 outliers)
Reward range: [6.88, 13.02], mean: 10.06
  Created 13 candidate models for data size 914
  rf-tuned-l: R2 = 0.162 (std: 0.059)
  rf-tuned-xl: R2 = 0.151 (std: 0.057)
  gb-tuned-l: R2 = 0.128 (std: 0.046)
  gb-tuned-xl: R2 = 0.128 (std: 0.046)
  xgb-xl: R2 = 0.068 (std: 0.043)
  xgb-l: R2 = 0.068 (std: 0.043)
  mlp-adaptive-xl: R2 = -0.090 (std: 0.115)
  mlp-l: R2 = -0.021 (std: 0.113)
  svr-rbf-xl: R2 = 0.143 (std: 0.095)
  svr-poly-l: R2 = 0.143 (std: 0.095)
  knn-tuned-sqrt: R2 = -0.024 (std: 0.060)
  knn-tuned-l: R2 = -0.024 (std: 0.060)
  ridge: R2 = -0.031 (std: 0.062)

Model-based training with 8 models
Best R2: 0.162, Mean R2: 0.062
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.4207, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1805
  Round 1/3: Mean predicted reward = 9.928
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.4169, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2571
  Round 2/3: Mean predicted reward = 9.947
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9707, entropy=0.4226, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2954
  Round 3/3: Mean predicted reward = 10.087

  === Progress Analysis ===
  Status: NORMAL

--- Round 28 Results ---
  Mean Oracle Reward: 10.636
  Min Oracle Reward: 9.187
  Max Oracle Reward: 12.934
  Std Oracle Reward: 0.834
  Sequence Diversity: 1.000
  Models Used: 8
  Model R² - Mean: 0.062, Max: 0.162, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 946

======================================================================
EXPERIMENT ROUND 29/30
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 946

--- Round 29 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GATCGTCCGGAC
  CAGGGATCAGCT
  TAGATCGCGGAC
  CCAGTGGCAGCT
  GCCCTATGCGAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.492
  Max reward: 13.394
  With intrinsic bonuses: 10.450

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9644, entropy=0.3928, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1682

=== Surrogate Model Training ===
Total samples: 978

Training on 945 samples (removed 33 outliers)
Reward range: [6.88, 13.02], mean: 10.07
  Created 13 candidate models for data size 945
  rf-tuned-l: R2 = 0.166 (std: 0.048)
  rf-tuned-xl: R2 = 0.155 (std: 0.058)
  gb-tuned-l: R2 = 0.149 (std: 0.052)
  gb-tuned-xl: R2 = 0.149 (std: 0.052)
  xgb-xl: R2 = 0.062 (std: 0.076)
  xgb-l: R2 = 0.062 (std: 0.076)
  mlp-adaptive-xl: R2 = -0.059 (std: 0.120)
  mlp-l: R2 = -0.003 (std: 0.077)
  svr-rbf-xl: R2 = 0.149 (std: 0.078)
  svr-poly-l: R2 = 0.149 (std: 0.078)
  knn-tuned-sqrt: R2 = -0.001 (std: 0.080)
  knn-tuned-l: R2 = -0.001 (std: 0.080)
  ridge: R2 = -0.027 (std: 0.045)

Model-based training with 8 models
Best R2: 0.166, Mean R2: 0.073
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9728, entropy=0.4077, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1024
  Round 1/3: Mean predicted reward = 10.008
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9730, entropy=0.4115, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0583
  Round 2/3: Mean predicted reward = 9.918
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9645, entropy=0.3709, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0930
  Round 3/3: Mean predicted reward = 10.193

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 29 Results ---
  Mean Oracle Reward: 10.488
  Min Oracle Reward: 7.307
  Max Oracle Reward: 13.528
  Std Oracle Reward: 1.301
  Sequence Diversity: 1.000
  Models Used: 8
  Model R² - Mean: 0.073, Max: 0.166, Count: 13
  Total Sequences Evaluated: 978

======================================================================
EXPERIMENT ROUND 30/30
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 978

--- Round 30 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTGGCTAGACGC
  CTGATCGGCAGC
  CCAGTCGGAGTA
  TCCTAGGGCAGA
  TAGTACCCGGGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.528
  Max reward: 13.082
  With intrinsic bonuses: 10.485

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9594, entropy=0.3678, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1985

=== Surrogate Model Training ===
Total samples: 1010

Training on 974 samples (removed 36 outliers)
Reward range: [6.90, 13.02], mean: 10.09
  Created 13 candidate models for data size 974
  rf-tuned-l: R2 = 0.188 (std: 0.055)
  rf-tuned-xl: R2 = 0.186 (std: 0.037)
  gb-tuned-l: R2 = 0.143 (std: 0.030)
  gb-tuned-xl: R2 = 0.143 (std: 0.030)
  xgb-xl: R2 = 0.079 (std: 0.044)
  xgb-l: R2 = 0.079 (std: 0.044)
  mlp-adaptive-xl: R2 = 0.030 (std: 0.039)
  mlp-l: R2 = 0.006 (std: 0.083)
  svr-rbf-xl: R2 = 0.169 (std: 0.063)
  svr-poly-l: R2 = 0.169 (std: 0.063)
  knn-tuned-sqrt: R2 = 0.013 (std: 0.050)
  knn-tuned-l: R2 = 0.013 (std: 0.050)
  ridge: R2 = -0.022 (std: 0.034)

Model-based training with 12 models
Best R2: 0.188, Mean R2: 0.092
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.3682, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4639
  Round 1/3: Mean predicted reward = 9.866
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9713, entropy=0.3987, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5144
  Round 2/3: Mean predicted reward = 9.997
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9669, entropy=0.3807, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6859
  Round 3/3: Mean predicted reward = 10.043

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 30 Results ---
  Mean Oracle Reward: 10.507
  Min Oracle Reward: 5.485
  Max Oracle Reward: 13.206
  Std Oracle Reward: 1.579
  Sequence Diversity: 1.000
  Models Used: 12
  Model R² - Mean: 0.092, Max: 0.188, Count: 13
  Total Sequences Evaluated: 1010

======================================================================
DyNA PPO ALGORITHM COMPLETE!
======================================================================
Total rounds executed: 30
Total sequences evaluated: 1010
Best mean reward: 10.636 (achieved at round 28)

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 30
Final Mean Reward: 10.5069
Best Mean Reward: 10.6355
Best Max Reward: 13.5278
Initial Lr: 0.0003
Final Lr: 0.0003
Total Updates: 153
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
  GGCCGCCGTCGT: 11.666
  GGCCGCCGTCGT: 11.400
  GGCCGCCGTCGT: 11.639
  GGCCGCCGTCGT: 11.515
  GGCCGCCGTCGT: 11.391

Stochastic (Exploration):
  GGCGCCGCCTGC: 9.870
  GGGCCGCTCGTC: 11.151
  GGCGCGCTCGCT: 10.237
  GGCGCCGGACCG: 9.127
  GGCCGCGTGCCG: 11.115

Final Performance:
  Mean reward: 10.911
  Max reward: 11.666
  Std reward: 0.822

Best sequence found: GGCCGCCGTCGT
   Reward: 11.666

======================================================================
Training complete! Check 'learning_curves.png' and 'training_metrics.json'
======================================================================
PS C:\Users\linle\OneDrive\2025DirectedStudy\code\project\v2> python .\run2.py
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
  Mean reward: 8.650
  Std reward: 2.681
  Min/Max: 0.000 / 11.698

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
  TGTCATAACTTC
  GGTTGAGTCAGA
  AGATGGGGATGC
  TCTCCGCATTAG
  CTGGATGATATG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.600
  Max reward: 10.825
  With intrinsic bonuses: 9.536

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9757, entropy=1.3843, kl_div=0.0000
    Epoch 2: policy_loss=-0.1789, value_loss=0.9747, entropy=1.3802, kl_div=0.0153
    Epoch 4: policy_loss=-0.2278, value_loss=0.9739, entropy=1.3806, kl_div=-0.0183
    Epoch 6: policy_loss=-0.2326, value_loss=0.9732, entropy=1.3793, kl_div=-0.0500

=== Surrogate Model Training ===
Total samples: 82

Training on 75 samples (removed 7 outliers)
Reward range: [6.33, 11.70], mean: 9.59
  Created 8 candidate models for data size 75
  rf-xs: R2 = -0.245 (std: 0.268)
  rf-s: R2 = -0.287 (std: 0.239)
  knn-xs: R2 = -0.513 (std: 0.257)
  knn-s: R2 = -0.513 (std: 0.257)
  ridge: R2 = -0.042 (std: 0.034)
  gb-xs: R2 = -0.727 (std: 0.409)
  gp: R2 = -90.920 (std: 43.014)
  svr-rbf-s: R2 = -0.048 (std: 0.051)

Model-based training with 2 models
Best R2: -0.042, Mean R2: -11.662
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9784, entropy=1.3784, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.691
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9773, entropy=1.3766, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.723

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 1 Results ---
  Mean Oracle Reward: 9.478
  Min Oracle Reward: 6.563
  Max Oracle Reward: 10.894
  Std Oracle Reward: 1.043
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -11.662, Max: -0.042, Count: 8
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
  TTTTGCCCATGC
  GCCGATGTGAGC
  CGCAAGTGAATG
  ACTATCCAAACT
  AAGTTCGAAACC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.775
  Max reward: 12.440
  With intrinsic bonuses: 9.750

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=1.3720, kl_div=0.0000
    Epoch 2: policy_loss=-0.1098, value_loss=0.9694, entropy=1.3627, kl_div=0.0777
    Epoch 4: policy_loss=-0.1468, value_loss=0.9693, entropy=1.3527, kl_div=0.1840
    Epoch 6: policy_loss=-0.1817, value_loss=0.9691, entropy=1.3507, kl_div=0.2203

=== Surrogate Model Training ===
Total samples: 114

Training on 103 samples (removed 11 outliers)
Reward range: [6.87, 11.70], mean: 9.71
  Created 11 candidate models for data size 103
  rf-m: R2 = -0.436 (std: 0.428)
  rf-l: R2 = -0.444 (std: 0.390)
  gb-m: R2 = -0.724 (std: 0.586)
  gb-l: R2 = -0.707 (std: 0.538)
  xgb-m: R2 = -0.651 (std: 0.796)
  knn-m: R2 = -0.320 (std: 0.200)
  knn-tuned: R2 = -0.320 (std: 0.200)
  mlp-m: R2 = -3.707 (std: 1.987)
  svr-rbf: R2 = -0.291 (std: 0.184)
  svr-poly: R2 = -0.291 (std: 0.184)
  ridge: R2 = -0.156 (std: 0.148)

Model-based training with 1 models
Best R2: -0.156, Mean R2: -0.731
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9767, entropy=1.3556, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.757
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9749, entropy=1.3567, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.744

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 2 Results ---
  Mean Oracle Reward: 9.759
  Min Oracle Reward: 6.480
  Max Oracle Reward: 12.548
  Std Oracle Reward: 1.152
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -0.731, Max: -0.156, Count: 11
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
  CCGCCGCCTACC
  GGCGCAAGCTAT
  GACGGCGGCCCA
  TCTCACTAGGCA
  CCAGCAGCTAGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.906
  Max reward: 11.430
  With intrinsic bonuses: 10.053

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9731, entropy=1.3531, kl_div=0.0000
    Epoch 2: policy_loss=-0.0535, value_loss=0.9730, entropy=1.3500, kl_div=0.0040
    Epoch 4: policy_loss=-0.1063, value_loss=0.9729, entropy=1.3448, kl_div=0.0135
    Epoch 6: policy_loss=-0.1400, value_loss=0.9728, entropy=1.3412, kl_div=0.0152

=== Surrogate Model Training ===
Total samples: 146

Training on 132 samples (removed 14 outliers)
Reward range: [7.02, 11.70], mean: 9.83
  Created 11 candidate models for data size 132
  rf-m: R2 = -0.293 (std: 0.247)
  rf-l: R2 = -0.228 (std: 0.265)
  gb-m: R2 = -0.794 (std: 0.434)
  gb-l: R2 = -0.816 (std: 0.444)
  xgb-m: R2 = -0.772 (std: 0.355)
  knn-m: R2 = -0.295 (std: 0.257)
  knn-tuned: R2 = -0.295 (std: 0.257)
  mlp-m: R2 = -3.300 (std: 1.275)
  svr-rbf: R2 = -0.223 (std: 0.260)
  svr-poly: R2 = -0.223 (std: 0.260)
  ridge: R2 = -0.131 (std: 0.221)

Model-based training with 1 models
Best R2: -0.131, Mean R2: -0.670
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9777, entropy=1.3442, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.996
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9791, entropy=1.3477, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.970

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 3 Results ---
  Mean Oracle Reward: 9.944
  Min Oracle Reward: 7.084
  Max Oracle Reward: 11.746
  Std Oracle Reward: 1.123
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -0.670, Max: -0.131, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 146

======================================================================
EXPERIMENT ROUND 4/30
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.280
Total data collected: 146
  Consistent improvement, increasing LR to 0.000045

--- Round 4 Configuration ---
Learning rate: 0.000045
Entropy coefficient: 0.0100
Exploration rate: 0.280

--- Generated Sequences (Diversity: 1.000) ---
  ACGCTCGTGGAA
  CGCCAGTAAGTG
  TGCGGCCTGACA
  ACTCTGGGCACG
  CTCTGCATGAGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.142
  Max reward: 12.604
  With intrinsic bonuses: 10.297

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9732, entropy=1.3405, kl_div=0.0000
    Epoch 1: policy_loss=-0.0099, value_loss=0.9732, entropy=1.3399, kl_div=0.0028
    Epoch 2: policy_loss=-0.0222, value_loss=0.9732, entropy=1.3391, kl_div=0.0069
    Epoch 3: policy_loss=-0.0363, value_loss=0.9732, entropy=1.3382, kl_div=0.0122

=== Surrogate Model Training ===
Total samples: 178

Training on 164 samples (removed 14 outliers)
Reward range: [7.02, 12.60], mean: 9.95
  Created 11 candidate models for data size 164
  rf-m: R2 = -0.145 (std: 0.131)
  rf-l: R2 = -0.165 (std: 0.159)
  gb-m: R2 = -0.250 (std: 0.206)
  gb-l: R2 = -0.246 (std: 0.195)
  xgb-m: R2 = -0.411 (std: 0.258)
  knn-m: R2 = -0.128 (std: 0.105)
  knn-tuned: R2 = -0.128 (std: 0.105)
  mlp-m: R2 = -2.604 (std: 0.668)
  svr-rbf: R2 = -0.008 (std: 0.079)
  svr-poly: R2 = -0.008 (std: 0.079)
  ridge: R2 = -0.023 (std: 0.136)
  Fallback: Using svr-rbf with R2 = -0.008

Model-based training with 1 models
Best R2: -0.008, Mean R2: -0.374
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9771, entropy=1.3440, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.146
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9741, entropy=1.3429, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.246

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 4 Results ---
  Mean Oracle Reward: 10.141
  Min Oracle Reward: 2.940
  Max Oracle Reward: 12.365
  Std Oracle Reward: 1.597
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -0.374, Max: -0.008, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 178

======================================================================
EXPERIMENT ROUND 5/30
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
  GGAGGTACATCC
  AGCTGTCGAGAC
  AATGCGGGTACC
  ACGATCGTTGCA
  GCGATTGCCGAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.967
  Max reward: 12.817
  With intrinsic bonuses: 10.044

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9712, entropy=1.3361, kl_div=0.0000
    Epoch 1: policy_loss=-0.0449, value_loss=0.9712, entropy=1.3270, kl_div=0.0621
    Epoch 2: policy_loss=-0.0505, value_loss=0.9712, entropy=1.3172, kl_div=0.1326
    Epoch 3: policy_loss=-0.0478, value_loss=0.9711, entropy=1.3088, kl_div=0.1925

=== Surrogate Model Training ===
Total samples: 210

Training on 197 samples (removed 13 outliers)
Reward range: [6.99, 12.60], mean: 9.94
  Created 11 candidate models for data size 197
  rf-m: R2 = -0.077 (std: 0.153)
  rf-l: R2 = -0.074 (std: 0.172)
  gb-m: R2 = -0.239 (std: 0.243)
  gb-l: R2 = -0.236 (std: 0.237)
  xgb-m: R2 = -0.279 (std: 0.337)
  knn-m: R2 = -0.211 (std: 0.189)
  knn-tuned: R2 = -0.211 (std: 0.189)
  mlp-m: R2 = -1.675 (std: 0.682)
  svr-rbf: R2 = -0.005 (std: 0.108)
  svr-poly: R2 = -0.005 (std: 0.108)
  ridge: R2 = -0.037 (std: 0.117)
  Fallback: Using svr-rbf with R2 = -0.005

Model-based training with 1 models
Best R2: -0.005, Mean R2: -0.277
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9781, entropy=1.3126, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.268
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9774, entropy=1.3080, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.215

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 5 Results ---
  Mean Oracle Reward: 9.970
  Min Oracle Reward: 6.823
  Max Oracle Reward: 12.500
  Std Oracle Reward: 1.236
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -0.277, Max: -0.005, Count: 11
  Total Sequences Evaluated: 210

======================================================================
EXPERIMENT ROUND 6/30
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.220
Total data collected: 210
  Performance plateaued, reducing LR to 0.000136

--- Round 6 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0100
Exploration rate: 0.220

--- Generated Sequences (Diversity: 1.000) ---
  GCGATAGCGTAC
  CATCTTGGAAGC
  GATAGCAGTCCT
  CATGAACGTGTC
  TTCGCGCAATAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.733
  Max reward: 11.623
  With intrinsic bonuses: 9.831

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=1.2893, kl_div=0.0000
    Epoch 1: policy_loss=-0.0081, value_loss=0.9696, entropy=1.2859, kl_div=0.0232
    Epoch 2: policy_loss=-0.0254, value_loss=0.9695, entropy=1.2832, kl_div=0.0412
    Epoch 3: policy_loss=-0.0413, value_loss=0.9695, entropy=1.2813, kl_div=0.0538

=== Surrogate Model Training ===
Total samples: 242

Training on 227 samples (removed 15 outliers)
Reward range: [6.99, 12.60], mean: 9.95
  Created 11 candidate models for data size 227
  rf-m: R2 = -0.143 (std: 0.148)
  rf-l: R2 = -0.128 (std: 0.122)
  gb-m: R2 = -0.344 (std: 0.247)
  gb-l: R2 = -0.344 (std: 0.247)
  xgb-m: R2 = -0.391 (std: 0.090)
  knn-m: R2 = -0.250 (std: 0.203)
  knn-tuned: R2 = -0.250 (std: 0.203)
  mlp-m: R2 = -1.804 (std: 0.876)
  svr-rbf: R2 = -0.055 (std: 0.098)
  svr-poly: R2 = -0.055 (std: 0.098)
  ridge: R2 = -0.063 (std: 0.082)
  Fallback: Using svr-rbf with R2 = -0.055

Model-based training with 1 models
Best R2: -0.055, Mean R2: -0.348
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9765, entropy=1.2905, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.229
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9750, entropy=1.2945, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.296

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 6 Results ---
  Mean Oracle Reward: 9.760
  Min Oracle Reward: 6.385
  Max Oracle Reward: 11.684
  Std Oracle Reward: 1.277
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -0.348, Max: -0.055, Count: 11
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
  GCTAGTGCCAAG
  CATGCGTAGCGA
  TAACGGACCGTT
  ATGTAAGCGTCC
  GAAAGGTCCTCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.853
  Max reward: 12.671
  With intrinsic bonuses: 9.843

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9737, entropy=1.2712, kl_div=0.0000
    Epoch 1: policy_loss=-0.0313, value_loss=0.9737, entropy=1.2681, kl_div=0.0250
    Epoch 2: policy_loss=-0.0524, value_loss=0.9736, entropy=1.2650, kl_div=0.0551
    Epoch 3: policy_loss=-0.0709, value_loss=0.9736, entropy=1.2641, kl_div=0.0654

=== Surrogate Model Training ===
Total samples: 274

Training on 256 samples (removed 18 outliers)
Reward range: [6.99, 12.60], mean: 9.98
  Created 11 candidate models for data size 256
  rf-m: R2 = -0.096 (std: 0.152)
  rf-l: R2 = -0.097 (std: 0.183)
  gb-m: R2 = -0.150 (std: 0.187)
  gb-l: R2 = -0.150 (std: 0.187)
  xgb-m: R2 = -0.235 (std: 0.208)
  knn-m: R2 = -0.198 (std: 0.280)
  knn-tuned: R2 = -0.198 (std: 0.280)
  mlp-m: R2 = -0.561 (std: 0.307)
  svr-rbf: R2 = -0.065 (std: 0.142)
  svr-poly: R2 = -0.065 (std: 0.142)
  ridge: R2 = -0.058 (std: 0.048)
  Fallback: Using ridge with R2 = -0.058

Model-based training with 1 models
Best R2: -0.058, Mean R2: -0.170
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9743, entropy=1.2816, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.083
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9759, entropy=1.2849, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.155

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 7 Results ---
  Mean Oracle Reward: 9.753
  Min Oracle Reward: 4.015
  Max Oracle Reward: 12.330
  Std Oracle Reward: 1.716
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -0.170, Max: -0.058, Count: 11
  Total Sequences Evaluated: 274

======================================================================
EXPERIMENT ROUND 8/30
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
  CAGGGCTCACGT
  GTTAAGGTCCCA
  ACAGATCGCGGT
  TAGGCACTCGAT
  GAAGCCTAGGTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.296
  Max reward: 13.007
  With intrinsic bonuses: 10.351

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9679, entropy=1.2686, kl_div=0.0000
    Epoch 1: policy_loss=-0.0037, value_loss=0.9679, entropy=1.2678, kl_div=0.0031

=== Surrogate Model Training ===
Total samples: 306

Training on 285 samples (removed 21 outliers)
Reward range: [7.21, 12.60], mean: 10.04
  Created 11 candidate models for data size 285
  rf-m: R2 = -0.076 (std: 0.092)
  rf-l: R2 = -0.072 (std: 0.065)
  gb-m: R2 = -0.082 (std: 0.080)
  gb-l: R2 = -0.078 (std: 0.082)
  xgb-m: R2 = -0.227 (std: 0.174)
  knn-m: R2 = -0.190 (std: 0.160)
  knn-tuned: R2 = -0.190 (std: 0.160)
  mlp-m: R2 = -0.936 (std: 0.265)
  svr-rbf: R2 = -0.084 (std: 0.047)
  svr-poly: R2 = -0.084 (std: 0.047)
  ridge: R2 = -0.072 (std: 0.036)
  Fallback: Using ridge with R2 = -0.072

Model-based training with 1 models
Best R2: -0.072, Mean R2: -0.190
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9777, entropy=1.2816, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.110
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9758, entropy=1.2813, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.099

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 8 Results ---
  Mean Oracle Reward: 10.354
  Min Oracle Reward: 7.291
  Max Oracle Reward: 12.953
  Std Oracle Reward: 0.970
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -0.190, Max: -0.072, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 306

======================================================================
EXPERIMENT ROUND 9/30
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.065
Total data collected: 306
  Consistent improvement, increasing LR to 0.000045

--- Round 9 Configuration ---
Learning rate: 0.000045
Entropy coefficient: 0.0050
Exploration rate: 0.065

--- Generated Sequences (Diversity: 1.000) ---
  TGCCGCAAAGGT
  GTTGCGCCAGCA
  GCATAAGCTTCG
  CAGGCTTCAGTA
  TAAGGCCGATCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.258
  Max reward: 13.879
  With intrinsic bonuses: 10.313

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9715, entropy=1.2593, kl_div=0.0000
    Epoch 1: policy_loss=-0.0094, value_loss=0.9715, entropy=1.2573, kl_div=0.0179

=== Surrogate Model Training ===
Total samples: 338

Training on 315 samples (removed 23 outliers)
Reward range: [7.21, 12.60], mean: 10.06
  Created 14 candidate models for data size 315
  rf-tuned-l: R2 = -0.071 (std: 0.082)
  rf-tuned-xl: R2 = -0.077 (std: 0.088)
  gb-tuned-l: R2 = -0.104 (std: 0.147)
  gb-tuned-xl: R2 = -0.101 (std: 0.145)
  xgb-xl: R2 = -0.292 (std: 0.064)
  xgb-l: R2 = -0.292 (std: 0.064)
  mlp-adaptive-xl: R2 = -0.804 (std: 0.162)
  mlp-l: R2 = -0.807 (std: 0.168)
  svr-rbf-xl: R2 = -0.047 (std: 0.092)
  svr-poly-l: R2 = -0.047 (std: 0.092)
  knn-tuned-sqrt: R2 = -0.179 (std: 0.108)
  knn-tuned-l: R2 = -0.179 (std: 0.108)
  ridge: R2 = -0.086 (std: 0.044)
  gp: R2 = -114.294 (std: 24.841)
  Fallback: Using svr-rbf-xl with R2 = -0.047

Model-based training with 1 models
Best R2: -0.047, Mean R2: -8.384
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9682, entropy=1.2760, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.945
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9754, entropy=1.2724, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.169

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 9 Results ---
  Mean Oracle Reward: 10.261
  Min Oracle Reward: 6.852
  Max Oracle Reward: 13.654
  Std Oracle Reward: 1.164
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -8.384, Max: -0.047, Count: 14
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
  AGGAGTCTCCAT
  AGTGTGGCCCAA
  CGAGTAATGTCC
  GTCGTACTCGAA
  GACTCACTAGGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.011
  Max reward: 12.177
  With intrinsic bonuses: 10.024

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=1.2501, kl_div=0.0000
    Epoch 1: policy_loss=-0.0053, value_loss=0.9688, entropy=1.2383, kl_div=0.1230

=== Surrogate Model Training ===
Total samples: 370

Training on 347 samples (removed 23 outliers)
Reward range: [7.16, 12.60], mean: 10.05
  Created 14 candidate models for data size 347
  rf-tuned-l: R2 = -0.015 (std: 0.101)
  rf-tuned-xl: R2 = -0.018 (std: 0.111)
  gb-tuned-l: R2 = -0.015 (std: 0.135)
  gb-tuned-xl: R2 = -0.014 (std: 0.132)
  xgb-xl: R2 = -0.186 (std: 0.174)
  xgb-l: R2 = -0.186 (std: 0.174)
  mlp-adaptive-xl: R2 = -0.579 (std: 0.195)
  mlp-l: R2 = -0.507 (std: 0.241)
  svr-rbf-xl: R2 = 0.000 (std: 0.146)
  svr-poly-l: R2 = 0.000 (std: 0.146)
  knn-tuned-sqrt: R2 = -0.083 (std: 0.171)
  knn-tuned-l: R2 = -0.083 (std: 0.171)
  ridge: R2 = -0.022 (std: 0.058)
  gp: R2 = -103.099 (std: 14.886)

Model-based training with 2 models
Best R2: 0.000, Mean R2: -7.486
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9726, entropy=1.2371, kl_div=0.0000
    Epoch 1: policy_loss=-0.0443, value_loss=0.9726, entropy=1.2265, kl_div=0.1008
  Round 1/3: Mean predicted reward = 10.077
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9717, entropy=1.2162, kl_div=0.0000
    Epoch 1: policy_loss=-0.0578, value_loss=0.9717, entropy=1.2017, kl_div=0.1333
  Round 2/3: Mean predicted reward = 10.047
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9720, entropy=1.1906, kl_div=0.0000
    Epoch 1: policy_loss=-0.0463, value_loss=0.9719, entropy=1.1731, kl_div=0.1679
  Round 3/3: Mean predicted reward = 10.017

  === Progress Analysis ===
  Status: NORMAL

--- Round 10 Results ---
  Mean Oracle Reward: 9.994
  Min Oracle Reward: 6.828
  Max Oracle Reward: 11.874
  Std Oracle Reward: 1.279
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -7.486, Max: 0.000, Count: 14
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
  ATATCCCAGGTG
  TCTGCGTGAAAC
  GTGTCCACAGGC
  ACTTGGACCATG
  GAGAACTTCGTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.024
  Max reward: 11.945
  With intrinsic bonuses: 10.086

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9717, entropy=1.1587, kl_div=0.0000
    Epoch 1: policy_loss=-0.0162, value_loss=0.9717, entropy=1.1399, kl_div=0.1913

=== Surrogate Model Training ===
Total samples: 402

Training on 379 samples (removed 23 outliers)
Reward range: [7.16, 12.60], mean: 10.05
  Created 14 candidate models for data size 379
  rf-tuned-l: R2 = -0.037 (std: 0.073)
  rf-tuned-xl: R2 = -0.026 (std: 0.077)
  gb-tuned-l: R2 = -0.011 (std: 0.095)
  gb-tuned-xl: R2 = -0.011 (std: 0.095)
  xgb-xl: R2 = -0.148 (std: 0.091)
  xgb-l: R2 = -0.148 (std: 0.091)
  mlp-adaptive-xl: R2 = -0.722 (std: 0.383)
  mlp-l: R2 = -0.727 (std: 0.393)
  svr-rbf-xl: R2 = 0.006 (std: 0.104)
  svr-poly-l: R2 = 0.006 (std: 0.104)
  knn-tuned-sqrt: R2 = -0.110 (std: 0.175)
  knn-tuned-l: R2 = -0.110 (std: 0.175)
  ridge: R2 = -0.055 (std: 0.092)
  gp: R2 = -107.523 (std: 24.555)

Model-based training with 2 models
Best R2: 0.006, Mean R2: -7.830
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9721, entropy=1.1274, kl_div=0.0000
    Epoch 1: policy_loss=-0.0264, value_loss=0.9720, entropy=1.1229, kl_div=0.0861
  Round 1/3: Mean predicted reward = 10.094
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9749, entropy=1.1345, kl_div=0.0000
    Epoch 1: policy_loss=-0.0337, value_loss=0.9749, entropy=1.1298, kl_div=0.0469
  Round 2/3: Mean predicted reward = 10.090
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9726, entropy=1.1325, kl_div=0.0000
    Epoch 1: policy_loss=-0.0392, value_loss=0.9726, entropy=1.1179, kl_div=0.1292
  Round 3/3: Mean predicted reward = 10.177

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 11 Results ---
  Mean Oracle Reward: 10.060
  Min Oracle Reward: 7.171
  Max Oracle Reward: 12.240
  Std Oracle Reward: 1.085
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -7.830, Max: 0.006, Count: 14
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
  ACGAGATTGCCG
  TAGCACGTGCGA
  AGCTAGCTCAGG
  CTCCGTAATAGG
  GCACCAGGTTAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.131
  Max reward: 11.553
  With intrinsic bonuses: 10.124

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9712, entropy=1.0985, kl_div=0.0000
    Epoch 1: policy_loss=-0.0380, value_loss=0.9712, entropy=1.0893, kl_div=0.1141

=== Surrogate Model Training ===
Total samples: 434

Training on 409 samples (removed 25 outliers)
Reward range: [7.41, 12.60], mean: 10.07
  Created 14 candidate models for data size 409
  rf-tuned-l: R2 = -0.045 (std: 0.092)
  rf-tuned-xl: R2 = -0.042 (std: 0.110)
  gb-tuned-l: R2 = -0.090 (std: 0.134)
  gb-tuned-xl: R2 = -0.091 (std: 0.135)
  xgb-xl: R2 = -0.197 (std: 0.177)
  xgb-l: R2 = -0.197 (std: 0.177)
  mlp-adaptive-xl: R2 = -0.657 (std: 0.107)
  mlp-l: R2 = -0.729 (std: 0.173)
  svr-rbf-xl: R2 = 0.004 (std: 0.124)
  svr-poly-l: R2 = 0.004 (std: 0.124)
  knn-tuned-sqrt: R2 = -0.172 (std: 0.173)
  knn-tuned-l: R2 = -0.172 (std: 0.173)
  ridge: R2 = -0.037 (std: 0.070)
  gp: R2 = -111.351 (std: 11.508)

Model-based training with 2 models
Best R2: 0.004, Mean R2: -8.127
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=1.0777, kl_div=0.0000
    Epoch 1: policy_loss=-0.0556, value_loss=0.9706, entropy=1.0703, kl_div=0.1171
  Round 1/3: Mean predicted reward = 10.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=1.0697, kl_div=0.0000
    Epoch 1: policy_loss=-0.0460, value_loss=0.9693, entropy=1.0609, kl_div=0.1328
  Round 2/3: Mean predicted reward = 10.176
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9718, entropy=1.0494, kl_div=0.0000
    Epoch 1: policy_loss=-0.0191, value_loss=0.9718, entropy=1.0422, kl_div=0.1088
  Round 3/3: Mean predicted reward = 10.055

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 12 Results ---
  Mean Oracle Reward: 10.151
  Min Oracle Reward: 8.113
  Max Oracle Reward: 11.828
  Std Oracle Reward: 0.761
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -8.127, Max: 0.004, Count: 14
  Total Sequences Evaluated: 434

======================================================================
EXPERIMENT ROUND 13/30
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 434
  Performance plateaued, reducing LR to 0.000055

--- Round 13 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GATAGCCCGTAT
  CCGCGGACAGTT
  TGCATGTCAGAC
  CACTGTAGATGC
  CTGAGGACAGCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.347
  Max reward: 11.511
  With intrinsic bonuses: 10.330

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9674, entropy=1.0526, kl_div=0.0000
    Epoch 1: policy_loss=-0.0091, value_loss=0.9674, entropy=1.0530, kl_div=0.0077

=== Surrogate Model Training ===
Total samples: 466

Training on 441 samples (removed 25 outliers)
Reward range: [7.41, 12.60], mean: 10.09
  Created 14 candidate models for data size 441
  rf-tuned-l: R2 = -0.052 (std: 0.082)
  rf-tuned-xl: R2 = -0.050 (std: 0.101)
  gb-tuned-l: R2 = -0.028 (std: 0.130)
  gb-tuned-xl: R2 = -0.029 (std: 0.130)
  xgb-xl: R2 = -0.150 (std: 0.134)
  xgb-l: R2 = -0.150 (std: 0.134)
  mlp-adaptive-xl: R2 = -0.558 (std: 0.147)
  mlp-l: R2 = -0.581 (std: 0.110)
  svr-rbf-xl: R2 = 0.005 (std: 0.127)
  svr-poly-l: R2 = 0.005 (std: 0.127)
  knn-tuned-sqrt: R2 = -0.173 (std: 0.195)
  knn-tuned-l: R2 = -0.173 (std: 0.195)
  ridge: R2 = -0.048 (std: 0.078)
  gp: R2 = -114.909 (std: 13.279)

Model-based training with 2 models
Best R2: 0.005, Mean R2: -8.349
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9726, entropy=1.0474, kl_div=0.0000
    Epoch 1: policy_loss=-0.0112, value_loss=0.9726, entropy=1.0467, kl_div=0.0157
  Round 1/3: Mean predicted reward = 10.231
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9732, entropy=1.0571, kl_div=0.0000
    Epoch 1: policy_loss=-0.0139, value_loss=0.9732, entropy=1.0544, kl_div=0.0255
  Round 2/3: Mean predicted reward = 10.192
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9723, entropy=1.0427, kl_div=0.0000
    Epoch 1: policy_loss=-0.0254, value_loss=0.9723, entropy=1.0383, kl_div=0.0611
  Round 3/3: Mean predicted reward = 10.187

  === Progress Analysis ===
  Status: NORMAL

--- Round 13 Results ---
  Mean Oracle Reward: 10.340
  Min Oracle Reward: 8.175
  Max Oracle Reward: 11.389
  Std Oracle Reward: 0.665
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -8.349, Max: 0.005, Count: 14
  Total Sequences Evaluated: 466

======================================================================
EXPERIMENT ROUND 14/30
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 466
  Consistent improvement, increasing LR to 0.000045

--- Round 14 Configuration ---
Learning rate: 0.000045
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCAGCGATCGGA
  TGCCCGATTGAA
  CACTGGTATAGC
  CAGCGAGTTAGC
  ACACGCATTTGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.489
  Max reward: 12.897
  With intrinsic bonuses: 10.575

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9716, entropy=1.0375, kl_div=0.0000
    Epoch 1: policy_loss=-0.0140, value_loss=0.9716, entropy=1.0332, kl_div=0.0491

=== Surrogate Model Training ===
Total samples: 498

Training on 469 samples (removed 29 outliers)
Reward range: [7.42, 12.60], mean: 10.12
  Created 14 candidate models for data size 469
  rf-tuned-l: R2 = -0.088 (std: 0.118)
  rf-tuned-xl: R2 = -0.081 (std: 0.101)
  gb-tuned-l: R2 = -0.080 (std: 0.136)
  gb-tuned-xl: R2 = -0.080 (std: 0.136)
  xgb-xl: R2 = -0.260 (std: 0.139)
  xgb-l: R2 = -0.260 (std: 0.139)
  mlp-adaptive-xl: R2 = -0.587 (std: 0.379)
  mlp-l: R2 = -0.606 (std: 0.483)
  svr-rbf-xl: R2 = -0.049 (std: 0.160)
  svr-poly-l: R2 = -0.049 (std: 0.160)
  knn-tuned-sqrt: R2 = -0.199 (std: 0.137)
  knn-tuned-l: R2 = -0.199 (std: 0.137)
  ridge: R2 = -0.080 (std: 0.095)
  gp: R2 = -118.448 (std: 20.860)
  Fallback: Using svr-rbf-xl with R2 = -0.049

Model-based training with 1 models
Best R2: -0.049, Mean R2: -8.648
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9658, entropy=1.0847, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.203
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=1.0770, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.348

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 14 Results ---
  Mean Oracle Reward: 10.539
  Min Oracle Reward: 6.418
  Max Oracle Reward: 12.955
  Std Oracle Reward: 1.258
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -8.648, Max: -0.049, Count: 14
  New best mean reward!
  Total Sequences Evaluated: 498

======================================================================
EXPERIMENT ROUND 15/30
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
  TGAAGCAGGTCC
  AATTGAGTCCCG
  CTTCCGATGAGA
  GTCCGGAGACAT
  GTCTGGCATCAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.993
  Max reward: 12.511
  With intrinsic bonuses: 10.064

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=1.0303, kl_div=0.0000
    Epoch 1: policy_loss=-0.0192, value_loss=0.9708, entropy=1.0156, kl_div=0.1798

=== Surrogate Model Training ===
Total samples: 530

Training on 501 samples (removed 29 outliers)
Reward range: [7.41, 12.60], mean: 10.10
  Created 13 candidate models for data size 501
  rf-tuned-l: R2 = -0.001 (std: 0.034)
  rf-tuned-xl: R2 = -0.017 (std: 0.051)
  gb-tuned-l: R2 = -0.016 (std: 0.047)
  gb-tuned-xl: R2 = -0.016 (std: 0.047)
  xgb-xl: R2 = -0.170 (std: 0.115)
  xgb-l: R2 = -0.170 (std: 0.115)
  mlp-adaptive-xl: R2 = -0.558 (std: 0.086)
  mlp-l: R2 = -0.404 (std: 0.130)
  svr-rbf-xl: R2 = -0.011 (std: 0.111)
  svr-poly-l: R2 = -0.011 (std: 0.111)
  knn-tuned-sqrt: R2 = -0.100 (std: 0.134)
  knn-tuned-l: R2 = -0.100 (std: 0.134)
  ridge: R2 = -0.051 (std: 0.082)
  Fallback: Using rf-tuned-l with R2 = -0.001

Model-based training with 1 models
Best R2: -0.001, Mean R2: -0.125
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9738, entropy=1.0549, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.208
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9713, entropy=1.0357, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.282

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 15 Results ---
  Mean Oracle Reward: 10.072
  Min Oracle Reward: 8.192
  Max Oracle Reward: 12.333
  Std Oracle Reward: 0.914
  Sequence Diversity: 1.000
  Models Used: 1
  Model R² - Mean: -0.125, Max: -0.001, Count: 13
  Total Sequences Evaluated: 530

======================================================================
EXPERIMENT ROUND 16/30
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 530

--- Round 16 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GATCACCGATGG
  AAAGCTGCTAGT
  CTTAGGAGACTC
  AACGACGTCTTG
  TGTGGCAAGACC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.897
  Max reward: 12.152
  With intrinsic bonuses: 9.971

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.9631, kl_div=0.0000
    Epoch 1: policy_loss=0.0215, value_loss=0.9706, entropy=0.9413, kl_div=0.3121

=== Surrogate Model Training ===
Total samples: 562

Training on 531 samples (removed 31 outliers)
Reward range: [7.45, 12.60], mean: 10.10
  Created 13 candidate models for data size 531
  rf-tuned-l: R2 = -0.031 (std: 0.055)
  rf-tuned-xl: R2 = -0.017 (std: 0.045)
  gb-tuned-l: R2 = -0.050 (std: 0.050)
  gb-tuned-xl: R2 = -0.049 (std: 0.050)
  xgb-xl: R2 = -0.209 (std: 0.140)
  xgb-l: R2 = -0.209 (std: 0.140)
  mlp-adaptive-xl: R2 = -0.348 (std: 0.120)
  mlp-l: R2 = -0.470 (std: 0.290)
  svr-rbf-xl: R2 = 0.013 (std: 0.078)
  svr-poly-l: R2 = 0.013 (std: 0.078)
  knn-tuned-sqrt: R2 = -0.138 (std: 0.134)
  knn-tuned-l: R2 = -0.138 (std: 0.134)
  ridge: R2 = -0.026 (std: 0.042)

Model-based training with 2 models
Best R2: 0.013, Mean R2: -0.127
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9729, entropy=0.9352, kl_div=0.0000
    Epoch 1: policy_loss=-0.0030, value_loss=0.9729, entropy=0.9215, kl_div=0.1787
  Round 1/3: Mean predicted reward = 9.981
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9745, entropy=0.9081, kl_div=0.0000
    Epoch 1: policy_loss=-0.0295, value_loss=0.9744, entropy=0.8958, kl_div=0.1794
  Round 2/3: Mean predicted reward = 10.124
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9681, entropy=0.9079, kl_div=0.0000
    Epoch 1: policy_loss=-0.0362, value_loss=0.9681, entropy=0.8987, kl_div=0.1505
  Round 3/3: Mean predicted reward = 10.082

  === Progress Analysis ===
  Status: NORMAL

--- Round 16 Results ---
  Mean Oracle Reward: 9.953
  Min Oracle Reward: 7.741
  Max Oracle Reward: 12.047
  Std Oracle Reward: 1.020
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -0.127, Max: 0.013, Count: 13
  Total Sequences Evaluated: 562

======================================================================
EXPERIMENT ROUND 17/30
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 562

--- Round 17 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTCAGTAGTAGC
  TTTCGAGGCACA
  GTATAGGCCGCA
  CGAGGAGTCTCA
  CAAGGTATTGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.245
  Max reward: 14.556
  With intrinsic bonuses: 10.239

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.8966, kl_div=0.0000
    Epoch 1: policy_loss=-0.0536, value_loss=0.9692, entropy=0.8971, kl_div=0.0007

=== Surrogate Model Training ===
Total samples: 594

Training on 561 samples (removed 33 outliers)
Reward range: [7.54, 12.60], mean: 10.11
  Created 13 candidate models for data size 561
  rf-tuned-l: R2 = -0.031 (std: 0.049)
  rf-tuned-xl: R2 = -0.042 (std: 0.035)
  gb-tuned-l: R2 = -0.018 (std: 0.046)
  gb-tuned-xl: R2 = -0.018 (std: 0.046)
  xgb-xl: R2 = -0.267 (std: 0.152)
  xgb-l: R2 = -0.267 (std: 0.152)
  mlp-adaptive-xl: R2 = -0.596 (std: 0.292)
  mlp-l: R2 = -0.343 (std: 0.136)
  svr-rbf-xl: R2 = 0.018 (std: 0.062)
  svr-poly-l: R2 = 0.018 (std: 0.062)
  knn-tuned-sqrt: R2 = -0.192 (std: 0.128)
  knn-tuned-l: R2 = -0.192 (std: 0.128)
  ridge: R2 = -0.027 (std: 0.041)

Model-based training with 2 models
Best R2: 0.018, Mean R2: -0.151
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9731, entropy=0.8913, kl_div=0.0000
    Epoch 1: policy_loss=-0.0312, value_loss=0.9731, entropy=0.8914, kl_div=0.0181
  Round 1/3: Mean predicted reward = 10.201
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9720, entropy=0.9004, kl_div=0.0000
    Epoch 1: policy_loss=-0.0301, value_loss=0.9719, entropy=0.8992, kl_div=-0.0117
  Round 2/3: Mean predicted reward = 10.055
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9733, entropy=0.8940, kl_div=0.0000
    Epoch 1: policy_loss=-0.0346, value_loss=0.9733, entropy=0.8936, kl_div=-0.0410
  Round 3/3: Mean predicted reward = 10.223

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 17 Results ---
  Mean Oracle Reward: 10.303
  Min Oracle Reward: 7.600
  Max Oracle Reward: 14.510
  Std Oracle Reward: 1.173
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -0.151, Max: 0.018, Count: 13
  Total Sequences Evaluated: 594

======================================================================
EXPERIMENT ROUND 18/30
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 594

--- Round 18 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGACGTCGCGAA
  AGAGATGCTCCT
  CTAGGACGTACT
  GAGGCTCGACTC
  CGCGAAACTGTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.638
  Max reward: 11.667
  With intrinsic bonuses: 9.669

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9652, entropy=0.8961, kl_div=0.0000
    Epoch 1: policy_loss=-0.0135, value_loss=0.9652, entropy=0.8981, kl_div=-0.0527

=== Surrogate Model Training ===
Total samples: 626

Training on 592 samples (removed 34 outliers)
Reward range: [7.54, 12.60], mean: 10.09
  Created 13 candidate models for data size 592
  rf-tuned-l: R2 = -0.034 (std: 0.051)
  rf-tuned-xl: R2 = -0.039 (std: 0.047)
  gb-tuned-l: R2 = -0.073 (std: 0.055)
  gb-tuned-xl: R2 = -0.073 (std: 0.055)
  xgb-xl: R2 = -0.152 (std: 0.085)
  xgb-l: R2 = -0.152 (std: 0.085)
  mlp-adaptive-xl: R2 = -0.417 (std: 0.218)
  mlp-l: R2 = -0.446 (std: 0.257)
  svr-rbf-xl: R2 = 0.004 (std: 0.071)
  svr-poly-l: R2 = 0.004 (std: 0.071)
  knn-tuned-sqrt: R2 = -0.186 (std: 0.095)
  knn-tuned-l: R2 = -0.186 (std: 0.095)
  ridge: R2 = -0.047 (std: 0.025)

Model-based training with 2 models
Best R2: 0.004, Mean R2: -0.138
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9715, entropy=0.9006, kl_div=0.0000
    Epoch 1: policy_loss=-0.0044, value_loss=0.9715, entropy=0.9026, kl_div=-0.0425
  Round 1/3: Mean predicted reward = 10.079
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9711, entropy=0.8883, kl_div=0.0000
    Epoch 1: policy_loss=-0.0352, value_loss=0.9711, entropy=0.8852, kl_div=0.0645
  Round 2/3: Mean predicted reward = 10.003
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9695, entropy=0.8935, kl_div=0.0000
    Epoch 1: policy_loss=-0.0269, value_loss=0.9695, entropy=0.8878, kl_div=0.1004
  Round 3/3: Mean predicted reward = 10.184

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 18 Results ---
  Mean Oracle Reward: 9.671
  Min Oracle Reward: 5.029
  Max Oracle Reward: 11.543
  Std Oracle Reward: 1.264
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -0.138, Max: 0.004, Count: 13
  Total Sequences Evaluated: 626

======================================================================
EXPERIMENT ROUND 19/30
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 626

--- Round 19 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCACGGGACTTA
  ATTCAGAGTGCC
  CGCTATGCAGAG
  CGTGCTCAGCGA
  TACACACGGTTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.879
  Max reward: 12.632
  With intrinsic bonuses: 9.909

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9672, entropy=0.8897, kl_div=0.0000
    Epoch 1: policy_loss=-0.0127, value_loss=0.9672, entropy=0.8885, kl_div=0.0232

=== Surrogate Model Training ===
Total samples: 658

Training on 621 samples (removed 37 outliers)
Reward range: [7.45, 12.60], mean: 10.09
  Created 13 candidate models for data size 621
  rf-tuned-l: R2 = 0.023 (std: 0.029)
  rf-tuned-xl: R2 = 0.041 (std: 0.041)
  gb-tuned-l: R2 = -0.013 (std: 0.045)
  gb-tuned-xl: R2 = -0.013 (std: 0.045)
  xgb-xl: R2 = -0.071 (std: 0.156)
  xgb-l: R2 = -0.071 (std: 0.156)
  mlp-adaptive-xl: R2 = -0.349 (std: 0.090)
  mlp-l: R2 = -0.330 (std: 0.082)
  svr-rbf-xl: R2 = 0.064 (std: 0.066)
  svr-poly-l: R2 = 0.064 (std: 0.066)
  knn-tuned-sqrt: R2 = -0.096 (std: 0.108)
  knn-tuned-l: R2 = -0.096 (std: 0.108)
  ridge: R2 = -0.024 (std: 0.036)

Model-based training with 4 models
Best R2: 0.064, Mean R2: -0.067
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9677, entropy=0.8862, kl_div=0.0000
    Epoch 1: policy_loss=-0.0103, value_loss=0.9677, entropy=0.8857, kl_div=0.0076
  Round 1/3: Mean predicted reward = 10.078
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9720, entropy=0.8791, kl_div=0.0000
    Epoch 1: policy_loss=-0.0051, value_loss=0.9720, entropy=0.8783, kl_div=0.0188
  Round 2/3: Mean predicted reward = 10.165
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9720, entropy=0.8859, kl_div=0.0000
    Epoch 1: policy_loss=-0.0094, value_loss=0.9720, entropy=0.8841, kl_div=0.0363
  Round 3/3: Mean predicted reward = 10.117

  === Progress Analysis ===
  Status: NORMAL

--- Round 19 Results ---
  Mean Oracle Reward: 9.852
  Min Oracle Reward: 4.695
  Max Oracle Reward: 12.630
  Std Oracle Reward: 1.605
  Sequence Diversity: 1.000
  Models Used: 4
  Model R² - Mean: -0.067, Max: 0.064, Count: 13
  Total Sequences Evaluated: 658

======================================================================
EXPERIMENT ROUND 20/30
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 658

--- Round 20 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCACCTGGGGTA
  GTGGGAACACTC
  TCGGCACTGGAA
  TCCGAGCTATGA
  TGCACAGTGGAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.820
  Max reward: 11.863
  With intrinsic bonuses: 9.887

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.8719, kl_div=0.0000
    Epoch 1: policy_loss=0.0386, value_loss=0.9690, entropy=0.8511, kl_div=0.4497

=== Surrogate Model Training ===
Total samples: 690

Training on 651 samples (removed 39 outliers)
Reward range: [7.42, 12.60], mean: 10.09
  Created 13 candidate models for data size 651
  rf-tuned-l: R2 = 0.042 (std: 0.063)
  rf-tuned-xl: R2 = 0.051 (std: 0.064)
  gb-tuned-l: R2 = 0.002 (std: 0.081)
  gb-tuned-xl: R2 = 0.002 (std: 0.081)
  xgb-xl: R2 = -0.097 (std: 0.108)
  xgb-l: R2 = -0.097 (std: 0.108)
  mlp-adaptive-xl: R2 = -0.328 (std: 0.229)
  mlp-l: R2 = -0.300 (std: 0.147)
  svr-rbf-xl: R2 = 0.065 (std: 0.069)
  svr-poly-l: R2 = 0.065 (std: 0.069)
  knn-tuned-sqrt: R2 = -0.105 (std: 0.115)
  knn-tuned-l: R2 = -0.105 (std: 0.115)
  ridge: R2 = -0.003 (std: 0.032)

Model-based training with 6 models
Best R2: 0.065, Mean R2: -0.062
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9711, entropy=0.8555, kl_div=0.0000
    Epoch 1: policy_loss=-0.0094, value_loss=0.9710, entropy=0.8421, kl_div=0.3364
  Round 1/3: Mean predicted reward = 10.072
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9711, entropy=0.8359, kl_div=0.0000
    Epoch 1: policy_loss=0.0045, value_loss=0.9711, entropy=0.8254, kl_div=0.2579
  Round 2/3: Mean predicted reward = 10.061
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.8277, kl_div=0.0000
    Epoch 1: policy_loss=-0.0328, value_loss=0.9691, entropy=0.8193, kl_div=0.2204
  Round 3/3: Mean predicted reward = 10.078

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 20 Results ---
  Mean Oracle Reward: 9.899
  Min Oracle Reward: 6.536
  Max Oracle Reward: 11.922
  Std Oracle Reward: 1.363
  Sequence Diversity: 1.000
  Models Used: 6
  Model R² - Mean: -0.062, Max: 0.065, Count: 13
  Total Sequences Evaluated: 690

======================================================================
EXPERIMENT ROUND 21/30
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 690

--- Round 21 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGTAGCTAAGGC
  CAGTGCAATGCT
  ACTGCGAATCGT
  TATGGCGACCAG
  GTCGGCAGACAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.541
  Max reward: 12.890
  With intrinsic bonuses: 10.512

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9708, entropy=0.8253, kl_div=0.0000
    Epoch 1: policy_loss=-0.0293, value_loss=0.9708, entropy=0.8192, kl_div=0.1795

=== Surrogate Model Training ===
Total samples: 722

Training on 681 samples (removed 41 outliers)
Reward range: [7.42, 12.70], mean: 10.12
  Created 13 candidate models for data size 681
  rf-tuned-l: R2 = 0.034 (std: 0.083)
  rf-tuned-xl: R2 = 0.045 (std: 0.074)
  gb-tuned-l: R2 = 0.018 (std: 0.091)
  gb-tuned-xl: R2 = 0.018 (std: 0.091)
  xgb-xl: R2 = -0.147 (std: 0.197)
  xgb-l: R2 = -0.147 (std: 0.197)
  mlp-adaptive-xl: R2 = -0.257 (std: 0.068)
  mlp-l: R2 = -0.207 (std: 0.105)
  svr-rbf-xl: R2 = 0.048 (std: 0.081)
  svr-poly-l: R2 = 0.048 (std: 0.081)
  knn-tuned-sqrt: R2 = -0.063 (std: 0.091)
  knn-tuned-l: R2 = -0.063 (std: 0.091)
  ridge: R2 = -0.004 (std: 0.040)

Model-based training with 6 models
Best R2: 0.048, Mean R2: -0.052
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9730, entropy=0.8134, kl_div=0.0000
    Epoch 1: policy_loss=-0.0489, value_loss=0.9729, entropy=0.8096, kl_div=0.1845
  Round 1/3: Mean predicted reward = 10.156
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.8040, kl_div=0.0000
    Epoch 1: policy_loss=-0.0477, value_loss=0.9685, entropy=0.8027, kl_div=0.1112
  Round 2/3: Mean predicted reward = 10.260
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.7968, kl_div=0.0000
    Epoch 1: policy_loss=-0.0591, value_loss=0.9701, entropy=0.7940, kl_div=0.1276
  Round 3/3: Mean predicted reward = 10.153

  === Progress Analysis ===
  Status: NORMAL

--- Round 21 Results ---
  Mean Oracle Reward: 10.498
  Min Oracle Reward: 6.101
  Max Oracle Reward: 13.110
  Std Oracle Reward: 1.478
  Sequence Diversity: 1.000
  Models Used: 6
  Model R² - Mean: -0.052, Max: 0.048, Count: 13
  Total Sequences Evaluated: 722

======================================================================
EXPERIMENT ROUND 22/30
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 722

--- Round 22 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTTGCGGAGAAC
  TGCGGATGCCAA
  TGTGGCACACTA
  CCCTGTCAGGGA
  ACTCAGGGACTT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.289
  Max reward: 12.299
  With intrinsic bonuses: 10.318

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.7698, kl_div=0.0000
    Epoch 1: policy_loss=-0.0004, value_loss=0.9688, entropy=0.7627, kl_div=0.2380

=== Surrogate Model Training ===
Total samples: 754

Training on 713 samples (removed 41 outliers)
Reward range: [7.42, 12.70], mean: 10.13
  Created 13 candidate models for data size 713
  rf-tuned-l: R2 = 0.003 (std: 0.085)
  rf-tuned-xl: R2 = 0.009 (std: 0.087)
  gb-tuned-l: R2 = 0.011 (std: 0.080)
  gb-tuned-xl: R2 = 0.010 (std: 0.080)
  xgb-xl: R2 = -0.172 (std: 0.163)
  xgb-l: R2 = -0.172 (std: 0.163)
  mlp-adaptive-xl: R2 = -0.284 (std: 0.048)
  mlp-l: R2 = -0.173 (std: 0.096)
  svr-rbf-xl: R2 = 0.050 (std: 0.045)
  svr-poly-l: R2 = 0.050 (std: 0.045)
  knn-tuned-sqrt: R2 = -0.074 (std: 0.067)
  knn-tuned-l: R2 = -0.074 (std: 0.067)
  ridge: R2 = 0.002 (std: 0.037)

Model-based training with 7 models
Best R2: 0.050, Mean R2: -0.063
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9703, entropy=0.7980, kl_div=0.0000
    Epoch 1: policy_loss=-0.0383, value_loss=0.9703, entropy=0.7938, kl_div=0.1534
  Round 1/3: Mean predicted reward = 10.043
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=0.8016, kl_div=0.0000
    Epoch 1: policy_loss=-0.0438, value_loss=0.9709, entropy=0.7982, kl_div=0.1061
  Round 2/3: Mean predicted reward = 10.107
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9668, entropy=0.7718, kl_div=0.0000
    Epoch 1: policy_loss=-0.0189, value_loss=0.9668, entropy=0.7636, kl_div=0.2691
  Round 3/3: Mean predicted reward = 10.267

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 22 Results ---
  Mean Oracle Reward: 10.283
  Min Oracle Reward: 8.678
  Max Oracle Reward: 12.196
  Std Oracle Reward: 0.850
  Sequence Diversity: 1.000
  Models Used: 7
  Model R² - Mean: -0.063, Max: 0.050, Count: 13
  Total Sequences Evaluated: 754

======================================================================
EXPERIMENT ROUND 23/30
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 754

--- Round 23 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTACCCGTGAAG
  CCGGATGAGTAC
  TAACGGCTCGGA
  TCAAAGTGCTGC
  GTACCCCGGAGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.998
  Max reward: 12.198
  With intrinsic bonuses: 10.055

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.7527, kl_div=0.0000
    Epoch 1: policy_loss=-0.0336, value_loss=0.9692, entropy=0.7487, kl_div=0.1518

=== Surrogate Model Training ===
Total samples: 786

Training on 745 samples (removed 41 outliers)
Reward range: [7.41, 12.70], mean: 10.13
  Created 13 candidate models for data size 745
  rf-tuned-l: R2 = 0.048 (std: 0.060)
  rf-tuned-xl: R2 = 0.064 (std: 0.054)
  gb-tuned-l: R2 = 0.035 (std: 0.074)
  gb-tuned-xl: R2 = 0.035 (std: 0.074)
  xgb-xl: R2 = -0.049 (std: 0.086)
  xgb-l: R2 = -0.049 (std: 0.086)
  mlp-adaptive-xl: R2 = -0.192 (std: 0.051)
  mlp-l: R2 = -0.295 (std: 0.073)
  svr-rbf-xl: R2 = 0.076 (std: 0.048)
  svr-poly-l: R2 = 0.076 (std: 0.048)
  knn-tuned-sqrt: R2 = -0.050 (std: 0.101)
  knn-tuned-l: R2 = -0.050 (std: 0.101)
  ridge: R2 = 0.001 (std: 0.035)

Model-based training with 7 models
Best R2: 0.076, Mean R2: -0.027
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9715, entropy=0.7354, kl_div=0.0000
    Epoch 1: policy_loss=-0.0276, value_loss=0.9715, entropy=0.7318, kl_div=0.1250
  Round 1/3: Mean predicted reward = 10.049
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9713, entropy=0.7653, kl_div=0.0000
    Epoch 1: policy_loss=-0.0443, value_loss=0.9713, entropy=0.7620, kl_div=0.0883
  Round 2/3: Mean predicted reward = 10.100
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9714, entropy=0.7499, kl_div=0.0000
    Epoch 1: policy_loss=-0.0619, value_loss=0.9714, entropy=0.7463, kl_div=0.1170
  Round 3/3: Mean predicted reward = 10.228

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 23 Results ---
  Mean Oracle Reward: 10.049
  Min Oracle Reward: 5.608
  Max Oracle Reward: 12.140
  Std Oracle Reward: 1.444
  Sequence Diversity: 1.000
  Models Used: 7
  Model R² - Mean: -0.027, Max: 0.076, Count: 13
  Total Sequences Evaluated: 786

======================================================================
EXPERIMENT ROUND 24/30
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 786

--- Round 24 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGCCTGTAGCGA
  TCGCGTAGCAGC
  GGCTCGACGATA
  TTACACGCCGGG
  TGACCACTATGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.012
  Max reward: 11.629
  With intrinsic bonuses: 9.972

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.7282, kl_div=0.0000
    Epoch 1: policy_loss=-0.0349, value_loss=0.9703, entropy=0.7261, kl_div=0.0673

=== Surrogate Model Training ===
Total samples: 818

Training on 777 samples (removed 41 outliers)
Reward range: [7.41, 12.76], mean: 10.13
  Created 13 candidate models for data size 777
  rf-tuned-l: R2 = 0.060 (std: 0.057)
  rf-tuned-xl: R2 = 0.073 (std: 0.066)
  gb-tuned-l: R2 = 0.064 (std: 0.092)
  gb-tuned-xl: R2 = 0.064 (std: 0.092)
  xgb-xl: R2 = -0.072 (std: 0.106)
  xgb-l: R2 = -0.072 (std: 0.106)
  mlp-adaptive-xl: R2 = -0.163 (std: 0.169)
  mlp-l: R2 = -0.178 (std: 0.118)
  svr-rbf-xl: R2 = 0.102 (std: 0.025)
  svr-poly-l: R2 = 0.102 (std: 0.025)
  knn-tuned-sqrt: R2 = -0.020 (std: 0.086)
  knn-tuned-l: R2 = -0.020 (std: 0.086)
  ridge: R2 = 0.008 (std: 0.045)

Model-based training with 7 models
Best R2: 0.102, Mean R2: -0.004
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.7514, kl_div=0.0000
    Epoch 1: policy_loss=-0.0262, value_loss=0.9705, entropy=0.7486, kl_div=0.0815
  Round 1/3: Mean predicted reward = 10.141
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9708, entropy=0.7294, kl_div=0.0000
    Epoch 1: policy_loss=-0.0483, value_loss=0.9708, entropy=0.7256, kl_div=0.1144
  Round 2/3: Mean predicted reward = 10.216
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9721, entropy=0.7252, kl_div=0.0000
    Epoch 1: policy_loss=-0.0379, value_loss=0.9721, entropy=0.7207, kl_div=0.1136
  Round 3/3: Mean predicted reward = 10.178

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 24 Results ---
  Mean Oracle Reward: 10.007
  Min Oracle Reward: 3.415
  Max Oracle Reward: 11.844
  Std Oracle Reward: 1.473
  Sequence Diversity: 1.000
  Models Used: 7
  Model R² - Mean: -0.004, Max: 0.102, Count: 13
  Total Sequences Evaluated: 818

======================================================================
EXPERIMENT ROUND 25/30
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 818

--- Round 25 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGAAAGCCTGGC
  GGCGAGATATCC
  CAAGCCGGTTCG
  ATCGTTAGACCG
  CTAAGGTCCTAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.814
  Max reward: 12.254
  With intrinsic bonuses: 9.798

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9699, entropy=0.7058, kl_div=0.0000
    Epoch 1: policy_loss=0.0819, value_loss=0.9699, entropy=0.6718, kl_div=1.2327

=== Surrogate Model Training ===
Total samples: 850

Training on 804 samples (removed 46 outliers)
Reward range: [7.42, 12.70], mean: 10.13
  Created 13 candidate models for data size 804
  rf-tuned-l: R2 = 0.035 (std: 0.056)
  rf-tuned-xl: R2 = 0.034 (std: 0.067)
  gb-tuned-l: R2 = 0.029 (std: 0.063)
  gb-tuned-xl: R2 = 0.029 (std: 0.063)
  xgb-xl: R2 = -0.056 (std: 0.080)
  xgb-l: R2 = -0.056 (std: 0.080)
  mlp-adaptive-xl: R2 = -0.235 (std: 0.060)
  mlp-l: R2 = -0.183 (std: 0.111)
  svr-rbf-xl: R2 = 0.093 (std: 0.010)
  svr-poly-l: R2 = 0.093 (std: 0.010)
  knn-tuned-sqrt: R2 = -0.027 (std: 0.069)
  knn-tuned-l: R2 = -0.027 (std: 0.069)
  ridge: R2 = 0.001 (std: 0.038)

Model-based training with 7 models
Best R2: 0.093, Mean R2: -0.021
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.6784, kl_div=0.0000
    Epoch 1: policy_loss=0.0602, value_loss=0.9706, entropy=0.6540, kl_div=0.8539
  Round 1/3: Mean predicted reward = 10.035
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9672, entropy=0.6097, kl_div=0.0000
    Epoch 1: policy_loss=0.1103, value_loss=0.9672, entropy=0.5939, kl_div=0.9232
  Round 2/3: Mean predicted reward = 10.120
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.5866, kl_div=0.0000
    Epoch 1: policy_loss=0.0196, value_loss=0.9706, entropy=0.5719, kl_div=0.6429
  Round 3/3: Mean predicted reward = 10.251

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 25 Results ---
  Mean Oracle Reward: 9.847
  Min Oracle Reward: 6.237
  Max Oracle Reward: 12.107
  Std Oracle Reward: 1.192
  Sequence Diversity: 1.000
  Models Used: 7
  Model R² - Mean: -0.021, Max: 0.093, Count: 13
  Total Sequences Evaluated: 850

======================================================================
EXPERIMENT ROUND 26/30
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
  ACAGTTCGAGGC
  GATGGCATACCT
  CGCGGTATATCA
  CGACGGGTAATC
  CCGTAGAGGCAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.267
  Max reward: 12.339
  With intrinsic bonuses: 10.223

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9708, entropy=0.5712, kl_div=0.0000
    Epoch 1: policy_loss=-0.0046, value_loss=0.9708, entropy=0.5657, kl_div=0.2957

=== Surrogate Model Training ===
Total samples: 882

Training on 837 samples (removed 45 outliers)
Reward range: [7.41, 12.70], mean: 10.13
  Created 13 candidate models for data size 837
  rf-tuned-l: R2 = 0.047 (std: 0.057)
  rf-tuned-xl: R2 = 0.050 (std: 0.064)
  gb-tuned-l: R2 = 0.065 (std: 0.026)
  gb-tuned-xl: R2 = 0.065 (std: 0.026)
  xgb-xl: R2 = -0.102 (std: 0.113)
  xgb-l: R2 = -0.102 (std: 0.113)
  mlp-adaptive-xl: R2 = -0.166 (std: 0.120)
  mlp-l: R2 = -0.165 (std: 0.073)
  svr-rbf-xl: R2 = 0.096 (std: 0.013)
  svr-poly-l: R2 = 0.096 (std: 0.013)
  knn-tuned-sqrt: R2 = -0.029 (std: 0.063)
  knn-tuned-l: R2 = -0.029 (std: 0.063)
  ridge: R2 = 0.022 (std: 0.026)

Model-based training with 7 models
Best R2: 0.096, Mean R2: -0.012
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.5799, kl_div=0.0000
    Epoch 1: policy_loss=-0.0254, value_loss=0.9697, entropy=0.5768, kl_div=0.1302
  Round 1/3: Mean predicted reward = 10.197
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.5659, kl_div=0.0000
    Epoch 1: policy_loss=-0.0495, value_loss=0.9689, entropy=0.5642, kl_div=0.0262
  Round 2/3: Mean predicted reward = 10.046
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9720, entropy=0.5725, kl_div=0.0000
    Epoch 1: policy_loss=-0.0455, value_loss=0.9720, entropy=0.5693, kl_div=0.0924
  Round 3/3: Mean predicted reward = 10.230

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 26 Results ---
  Mean Oracle Reward: 10.181
  Min Oracle Reward: 7.757
  Max Oracle Reward: 12.439
  Std Oracle Reward: 1.058
  Sequence Diversity: 1.000
  Models Used: 7
  Model R² - Mean: -0.012, Max: 0.096, Count: 13
  Total Sequences Evaluated: 882

======================================================================
EXPERIMENT ROUND 27/30
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 882

--- Round 27 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GATATGCCGAGC
  GATTCCTGGCAA
  GACCGTCCGTGA
  GATCCTGCGAGC
  TACGGATGGACC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.476
  Max reward: 11.760
  With intrinsic bonuses: 10.465

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9733, entropy=0.5419, kl_div=0.0000
    Epoch 1: policy_loss=-0.0014, value_loss=0.9733, entropy=0.5354, kl_div=0.3590

=== Surrogate Model Training ===
Total samples: 914

Training on 867 samples (removed 47 outliers)
Reward range: [7.45, 12.76], mean: 10.16
  Created 13 candidate models for data size 867
  rf-tuned-l: R2 = 0.027 (std: 0.071)
  rf-tuned-xl: R2 = 0.042 (std: 0.087)
  gb-tuned-l: R2 = 0.057 (std: 0.057)
  gb-tuned-xl: R2 = 0.057 (std: 0.057)
  xgb-xl: R2 = -0.069 (std: 0.124)
  xgb-l: R2 = -0.069 (std: 0.124)
  mlp-adaptive-xl: R2 = -0.173 (std: 0.058)
  mlp-l: R2 = -0.143 (std: 0.146)
  svr-rbf-xl: R2 = 0.086 (std: 0.029)
  svr-poly-l: R2 = 0.086 (std: 0.029)
  knn-tuned-sqrt: R2 = -0.038 (std: 0.066)
  knn-tuned-l: R2 = -0.038 (std: 0.066)
  ridge: R2 = 0.019 (std: 0.020)

Model-based training with 7 models
Best R2: 0.086, Mean R2: -0.012
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9715, entropy=0.5571, kl_div=0.0000
    Epoch 1: policy_loss=-0.0143, value_loss=0.9715, entropy=0.5531, kl_div=0.2974
  Round 1/3: Mean predicted reward = 10.183
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9715, entropy=0.5289, kl_div=0.0000
    Epoch 1: policy_loss=-0.0170, value_loss=0.9715, entropy=0.5236, kl_div=0.2530
  Round 2/3: Mean predicted reward = 10.288
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9712, entropy=0.5367, kl_div=0.0000
    Epoch 1: policy_loss=-0.0352, value_loss=0.9712, entropy=0.5346, kl_div=0.2089
  Round 3/3: Mean predicted reward = 10.057

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 27 Results ---
  Mean Oracle Reward: 10.470
  Min Oracle Reward: 6.197
  Max Oracle Reward: 11.782
  Std Oracle Reward: 1.027
  Sequence Diversity: 1.000
  Models Used: 7
  Model R² - Mean: -0.012, Max: 0.086, Count: 13
  Total Sequences Evaluated: 914

======================================================================
EXPERIMENT ROUND 28/30
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 914
  Consistent improvement, increasing LR to 0.000132

--- Round 28 Configuration ---
Learning rate: 0.000132
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TTGTACGACGAC
  CGGAGTGTCACA
  CAGATGGCGTCA
  CGCTATGCGCAG
  CACTGGGATTAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.220
  Max reward: 12.079
  With intrinsic bonuses: 10.227

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.5259, kl_div=0.0000
    Epoch 1: policy_loss=-0.0297, value_loss=0.9705, entropy=0.5244, kl_div=0.0795

=== Surrogate Model Training ===
Total samples: 946

Training on 898 samples (removed 48 outliers)
Reward range: [7.50, 12.76], mean: 10.17
  Created 13 candidate models for data size 898
  rf-tuned-l: R2 = 0.055 (std: 0.050)
  rf-tuned-xl: R2 = 0.066 (std: 0.071)
  gb-tuned-l: R2 = 0.081 (std: 0.058)
  gb-tuned-xl: R2 = 0.081 (std: 0.058)
  xgb-xl: R2 = -0.036 (std: 0.082)
  xgb-l: R2 = -0.036 (std: 0.082)
  mlp-adaptive-xl: R2 = -0.203 (std: 0.104)
  mlp-l: R2 = -0.174 (std: 0.103)
  svr-rbf-xl: R2 = 0.100 (std: 0.042)
  svr-poly-l: R2 = 0.100 (std: 0.042)
  knn-tuned-sqrt: R2 = -0.024 (std: 0.061)
  knn-tuned-l: R2 = -0.024 (std: 0.061)
  ridge: R2 = 0.021 (std: 0.026)

Model-based training with 7 models
Best R2: 0.100, Mean R2: 0.001
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9700, entropy=0.5425, kl_div=0.0000
    Epoch 1: policy_loss=-0.0236, value_loss=0.9700, entropy=0.5451, kl_div=-0.1380
  Round 1/3: Mean predicted reward = 10.117
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9717, entropy=0.5076, kl_div=0.0000
    Epoch 1: policy_loss=-0.0414, value_loss=0.9717, entropy=0.5062, kl_div=0.1028
  Round 2/3: Mean predicted reward = 10.186
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9717, entropy=0.5013, kl_div=0.0000
    Epoch 1: policy_loss=-0.0563, value_loss=0.9717, entropy=0.5008, kl_div=0.1061
  Round 3/3: Mean predicted reward = 10.175

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 28 Results ---
  Mean Oracle Reward: 10.212
  Min Oracle Reward: 8.094
  Max Oracle Reward: 11.819
  Std Oracle Reward: 0.972
  Sequence Diversity: 1.000
  Models Used: 7
  Model R² - Mean: 0.001, Max: 0.100, Count: 13
  Total Sequences Evaluated: 946

======================================================================
EXPERIMENT ROUND 29/30
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 946

--- Round 29 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCCGGAGATACT
  GGTCCGTACGAA
  AGATACTGGGCC
  GGGGCACACTTA
  ACGCGCTCAGGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.273
  Max reward: 12.336
  With intrinsic bonuses: 10.274

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9723, entropy=0.5367, kl_div=0.0000
    Epoch 1: policy_loss=-0.0134, value_loss=0.9723, entropy=0.5367, kl_div=0.0240

=== Surrogate Model Training ===
Total samples: 978

Training on 930 samples (removed 48 outliers)
Reward range: [7.50, 12.76], mean: 10.17
  Created 13 candidate models for data size 930
  rf-tuned-l: R2 = 0.076 (std: 0.047)
  rf-tuned-xl: R2 = 0.071 (std: 0.048)
  gb-tuned-l: R2 = 0.073 (std: 0.072)
  gb-tuned-xl: R2 = 0.073 (std: 0.072)
  xgb-xl: R2 = -0.022 (std: 0.081)
  xgb-l: R2 = -0.022 (std: 0.081)
  mlp-adaptive-xl: R2 = -0.134 (std: 0.098)
  mlp-l: R2 = -0.216 (std: 0.131)
  svr-rbf-xl: R2 = 0.104 (std: 0.029)
  svr-poly-l: R2 = 0.104 (std: 0.029)
  knn-tuned-sqrt: R2 = -0.033 (std: 0.055)
  knn-tuned-l: R2 = -0.033 (std: 0.055)
  ridge: R2 = 0.022 (std: 0.029)

Model-based training with 7 models
Best R2: 0.104, Mean R2: 0.005
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9672, entropy=0.5394, kl_div=0.0000
    Epoch 1: policy_loss=-0.0037, value_loss=0.9672, entropy=0.5392, kl_div=0.0162
  Round 1/3: Mean predicted reward = 10.083
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9709, entropy=0.5576, kl_div=0.0000
    Epoch 1: policy_loss=-0.0100, value_loss=0.9709, entropy=0.5571, kl_div=0.0080
  Round 2/3: Mean predicted reward = 10.148
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.5290, kl_div=0.0000
    Epoch 1: policy_loss=-0.0292, value_loss=0.9705, entropy=0.5275, kl_div=0.0527
  Round 3/3: Mean predicted reward = 10.188

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 29 Results ---
  Mean Oracle Reward: 10.296
  Min Oracle Reward: 8.000
  Max Oracle Reward: 12.437
  Std Oracle Reward: 1.037
  Sequence Diversity: 1.000
  Models Used: 7
  Model R² - Mean: 0.005, Max: 0.104, Count: 13
  Total Sequences Evaluated: 978

======================================================================
EXPERIMENT ROUND 30/30
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 978

--- Round 30 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCGATCAGGACT
  GGGACCCATGAT
  GCGCGTCATAAG
  TCACGTCGATGA
  GCATAACCGGTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.221
  Max reward: 12.344
  With intrinsic bonuses: 10.234

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.5683, kl_div=0.0000
    Epoch 1: policy_loss=0.0407, value_loss=0.9695, entropy=0.5471, kl_div=0.9375

=== Surrogate Model Training ===
Total samples: 1010

Training on 962 samples (removed 48 outliers)
Reward range: [7.43, 12.76], mean: 10.17
  Created 13 candidate models for data size 962
  rf-tuned-l: R2 = 0.072 (std: 0.033)
  rf-tuned-xl: R2 = 0.070 (std: 0.041)
  gb-tuned-l: R2 = 0.093 (std: 0.060)
  gb-tuned-xl: R2 = 0.093 (std: 0.060)
  xgb-xl: R2 = -0.055 (std: 0.079)
  xgb-l: R2 = -0.055 (std: 0.079)
  mlp-adaptive-xl: R2 = -0.099 (std: 0.120)
  mlp-l: R2 = -0.126 (std: 0.077)
  svr-rbf-xl: R2 = 0.117 (std: 0.009)
  svr-poly-l: R2 = 0.117 (std: 0.009)
  knn-tuned-sqrt: R2 = -0.072 (std: 0.049)
  knn-tuned-l: R2 = -0.072 (std: 0.049)
  ridge: R2 = 0.019 (std: 0.040)

Model-based training with 7 models
Best R2: 0.117, Mean R2: 0.008
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.5176, kl_div=0.0000
    Epoch 1: policy_loss=0.0317, value_loss=0.9686, entropy=0.5131, kl_div=0.1158
  Round 1/3: Mean predicted reward = 10.094
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9672, entropy=0.5084, kl_div=0.0000
    Epoch 1: policy_loss=-0.0286, value_loss=0.9672, entropy=0.5089, kl_div=-0.1172
  Round 2/3: Mean predicted reward = 10.145
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.5140, kl_div=0.0000
    Epoch 1: policy_loss=-0.0145, value_loss=0.9701, entropy=0.5116, kl_div=0.2009
  Round 3/3: Mean predicted reward = 10.225

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 30 Results ---
  Mean Oracle Reward: 10.202
  Min Oracle Reward: 6.868
  Max Oracle Reward: 12.377
  Std Oracle Reward: 1.311
  Sequence Diversity: 1.000
  Models Used: 7
  Model R² - Mean: 0.008, Max: 0.117, Count: 13
  Total Sequences Evaluated: 1010

======================================================================
DyNA PPO ALGORITHM COMPLETE!
======================================================================
Total rounds executed: 30
Total sequences evaluated: 1010
Best mean reward: 10.539 (achieved at round 14)

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 30
Final Mean Reward: 10.2024
Best Mean Reward: 10.5395
Best Max Reward: 14.5098
Initial Lr: 0.0003
Final Lr: 0.0003
Total Updates: 222
Final Diversity: 1.0000
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
  GCGGCGGCCGAC: 11.273
  GCGGCGGCCGAC: 11.625
  GCGGCGGCCGAC: 11.364
  GCGGCGGCCGAC: 11.443
  GCGGCGGCCGAC: 11.216

Stochastic (Exploration):
  GCGGCGGCCAAC: 11.348
  GGCGGCGACAGC: 10.034
  GCGGCTGGCCGA: 11.933
  CGGGCGGACGAC: 9.187
  GCGGAGCCAAGA: 10.284

Final Performance:
  Mean reward: 10.971
  Max reward: 11.933
  Std reward: 0.810

Best sequence found: GCGGCTGGCCGA
   Reward: 11.933

======================================================================
Training complete! Check 'learning_curves.png' and 'training_metrics.json'
======================================================================