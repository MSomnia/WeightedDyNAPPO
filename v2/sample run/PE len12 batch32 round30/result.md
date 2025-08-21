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