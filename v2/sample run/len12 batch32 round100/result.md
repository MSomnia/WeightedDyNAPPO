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
  Mean reward: 8.454
  Std reward: 2.676
  Min/Max: 0.000 / 13.219

Pre-training surrogate models on warm-up data...

Training on 47 samples (removed 3 outliers)
Reward range: [3.55, 13.22], mean: 8.89
  Created 8 candidate models for data size 47
Current R2 threshold: -0.3
  rf-xs: R2 = -0.228 (std: 0.183)
  rf-s: R2 = -0.259 (std: 0.175)
  knn-xs: R2 = -0.205 (std: 0.235)
  knn-s: R2 = -0.205 (std: 0.235)
  ridge: R2 = -0.177 (std: 0.130)
  gb-xs: R2 = -0.541 (std: 0.223)
  gp: R2 = -20.965 (std: 7.413)
  svr-rbf-s: R2 = -0.111 (std: 0.249)
Initial models trained: 6
Initial R2 scores - Mean: -2.836, Max: -0.111

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
  GACACGTCCGCC
  CGCTACTATTGG
  CCTCGGGGTGGA
  ATCCTGTTAACT
  CACCGGGGGTAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.444
  Max reward: 12.187
  With intrinsic bonuses: 9.408

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9974, entropy=1.3843, kl_div=0.0000
    Epoch 2: policy_loss=-0.2175, value_loss=0.9948, entropy=1.3808, kl_div=0.0160
    Epoch 4: policy_loss=-0.2404, value_loss=0.9925, entropy=1.3800, kl_div=0.0255
    Epoch 6: policy_loss=-0.2446, value_loss=0.9902, entropy=1.3808, kl_div=-0.0197

=== Surrogate Model Training ===
Total samples: 82

Training on 76 samples (removed 6 outliers)
Reward range: [5.06, 13.22], mean: 9.31
  Created 8 candidate models for data size 76
Current R2 threshold: -0.3
  rf-xs: R2 = -0.137 (std: 0.234)
  rf-s: R2 = -0.170 (std: 0.197)
  knn-xs: R2 = -0.142 (std: 0.129)
  knn-s: R2 = -0.142 (std: 0.129)
  ridge: R2 = -0.110 (std: 0.075)
  gb-xs: R2 = -0.330 (std: 0.309)
  gp: R2 = -45.065 (std: 13.322)
  svr-rbf-s: R2 = -0.043 (std: 0.105)

Model-based training with 6 models
Best R2: -0.043, Mean R2: -5.767
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9870, entropy=1.3804, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.307
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9874, entropy=1.3796, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.245

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 1 Results ---
  Mean Oracle Reward: 9.417
  Min Oracle Reward: 7.203
  Max Oracle Reward: 12.292
  Std Oracle Reward: 1.173
  Sequence Diversity: 1.000
  Models Used: 6
  Model R2 - Mean: -5.767, Max: -0.043, Count: 8
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
  TACAGGAAGCGC
  CGGCGATGCTGT
  ATTGCATCAATG
  TAGTCGTTGTGC
  AGACGCCATACG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.657
  Max reward: 11.946
  With intrinsic bonuses: 9.613

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9934, entropy=1.3777, kl_div=0.0000
    Early stopping at epoch 2: KL divergence = 0.0579

=== Surrogate Model Training ===
Total samples: 114

Training on 107 samples (removed 7 outliers)
Reward range: [5.06, 13.22], mean: 9.46
  Created 11 candidate models for data size 107
Current R2 threshold: -0.3
  rf-m: R2 = -0.206 (std: 0.183)
  rf-l: R2 = -0.179 (std: 0.184)
  gb-m: R2 = -0.454 (std: 0.362)
  gb-l: R2 = -0.448 (std: 0.371)
  xgb-m: R2 = -0.558 (std: 0.728)
  knn-m: R2 = -0.212 (std: 0.215)
  knn-tuned: R2 = -0.212 (std: 0.215)
  mlp-m: R2 = -2.836 (std: 2.140)
  svr-rbf: R2 = -0.098 (std: 0.234)
  svr-poly: R2 = -0.098 (std: 0.234)
  ridge: R2 = -0.178 (std: 0.117)

Model-based training with 7 models
Best R2: -0.098, Mean R2: -0.498
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9837, entropy=1.3729, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.726
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9873, entropy=1.3698, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.806

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 2 Results ---
  Mean Oracle Reward: 9.662
  Min Oracle Reward: 4.216
  Max Oracle Reward: 12.046
  Std Oracle Reward: 1.378
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: -0.498, Max: -0.098, Count: 11
  New best mean reward!
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
  AGATTGCTAAAA
  ATGGTCCACAAT
  CAATCATCTTGA
  ACGTGTCAGGCG
  AGTCTGCCATCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.885
  Max reward: 12.450
  With intrinsic bonuses: 10.045

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9862, entropy=1.3663, kl_div=0.0000
    Epoch 2: policy_loss=-0.0800, value_loss=0.9857, entropy=1.3595, kl_div=0.0442
    Early stopping at epoch 3: KL divergence = 0.0773

=== Surrogate Model Training ===
Total samples: 146

Training on 138 samples (removed 8 outliers)
Reward range: [6.40, 13.22], mean: 9.59
  Created 11 candidate models for data size 138
Current R2 threshold: -0.3
  rf-m: R2 = -0.131 (std: 0.197)
  rf-l: R2 = -0.113 (std: 0.204)
  gb-m: R2 = -0.397 (std: 0.135)
  gb-l: R2 = -0.413 (std: 0.133)
  xgb-m: R2 = -0.373 (std: 0.282)
  knn-m: R2 = -0.159 (std: 0.179)
  knn-tuned: R2 = -0.159 (std: 0.179)
  mlp-m: R2 = -1.906 (std: 1.352)
  svr-rbf: R2 = -0.033 (std: 0.124)
  svr-poly: R2 = -0.033 (std: 0.124)
  ridge: R2 = -0.078 (std: 0.113)

Model-based training with 7 models
Best R2: -0.033, Mean R2: -0.345
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9853, entropy=1.3516, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.929
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9862, entropy=1.3512, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.989

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 3 Results ---
  Mean Oracle Reward: 9.923
  Min Oracle Reward: 6.753
  Max Oracle Reward: 12.444
  Std Oracle Reward: 1.156
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: -0.345, Max: -0.033, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 146

======================================================================
EXPERIMENT ROUND 4/100
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
  CCTGTGGAACGA
  AGTCACCGTTGA
  GTGGGAACTCAC
  ATAGCAGGTCTC
  GGCCACTGAGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.329
  Max reward: 12.308
  With intrinsic bonuses: 10.436

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9816, entropy=1.3454, kl_div=0.0000
    Epoch 1: policy_loss=-0.0064, value_loss=0.9815, entropy=1.3438, kl_div=0.0101
    Epoch 2: policy_loss=-0.0151, value_loss=0.9815, entropy=1.3421, kl_div=0.0206
    Epoch 3: policy_loss=-0.0256, value_loss=0.9814, entropy=1.3404, kl_div=0.0313

=== Surrogate Model Training ===
Total samples: 178

Training on 170 samples (removed 8 outliers)
Reward range: [6.40, 13.22], mean: 9.74
  Created 11 candidate models for data size 170
Current R2 threshold: -0.3
  rf-m: R2 = -0.150 (std: 0.211)
  rf-l: R2 = -0.144 (std: 0.220)
  gb-m: R2 = -0.392 (std: 0.310)
  gb-l: R2 = -0.390 (std: 0.309)
  xgb-m: R2 = -0.489 (std: 0.362)
  knn-m: R2 = -0.296 (std: 0.270)
  knn-tuned: R2 = -0.296 (std: 0.270)
  mlp-m: R2 = -1.252 (std: 0.889)
  svr-rbf: R2 = -0.149 (std: 0.201)
  svr-poly: R2 = -0.149 (std: 0.201)
  ridge: R2 = -0.168 (std: 0.184)

Model-based training with 7 models
Best R2: -0.144, Mean R2: -0.352
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9909, entropy=1.3375, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.036
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9864, entropy=1.3380, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.034

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 4 Results ---
  Mean Oracle Reward: 10.343
  Min Oracle Reward: 7.995
  Max Oracle Reward: 12.529
  Std Oracle Reward: 1.054
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: -0.352, Max: -0.144, Count: 11
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
  GTGCAGCGACTA
  GCGGTATGCAAC
  GATGGGCAATCC
  CCGAGTGCAGTA
  CTCGACAGATTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.017
  Max reward: 11.727
  With intrinsic bonuses: 10.109

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9782, entropy=1.3364, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0842

=== Surrogate Model Training ===
Total samples: 210

Training on 202 samples (removed 8 outliers)
Reward range: [6.24, 13.22], mean: 9.79
  Created 11 candidate models for data size 202
Current R2 threshold: -0.3
  rf-m: R2 = -0.137 (std: 0.234)
  rf-l: R2 = -0.136 (std: 0.244)
  gb-m: R2 = -0.301 (std: 0.411)
  gb-l: R2 = -0.299 (std: 0.407)
  xgb-m: R2 = -0.425 (std: 0.313)
  knn-m: R2 = -0.198 (std: 0.235)
  knn-tuned: R2 = -0.198 (std: 0.235)
  mlp-m: R2 = -1.212 (std: 0.786)
  svr-rbf: R2 = -0.055 (std: 0.103)
  svr-poly: R2 = -0.055 (std: 0.103)
  ridge: R2 = -0.074 (std: 0.080)

Model-based training with 8 models
Best R2: -0.055, Mean R2: -0.281
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9883, entropy=1.3231, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.007
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9856, entropy=1.3113, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.021

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 5 Results ---
  Mean Oracle Reward: 10.020
  Min Oracle Reward: 6.149
  Max Oracle Reward: 11.941
  Std Oracle Reward: 1.277
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: -0.281, Max: -0.055, Count: 11
  Total Sequences Evaluated: 210

======================================================================
EXPERIMENT ROUND 6/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.220
Total data collected: 210

--- Round 6 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0100
Exploration rate: 0.220

--- Generated Sequences (Diversity: 1.000) ---
  TGCACGATCTGA
  ACACTGTACGGG
  GCATCTGAATCG
  AGTTCCGAACTG
  GTAGCAGGACCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.952
  Max reward: 12.283
  With intrinsic bonuses: 10.020

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9784, entropy=1.3005, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1005

=== Surrogate Model Training ===
Total samples: 242

Training on 231 samples (removed 11 outliers)
Reward range: [6.40, 13.22], mean: 9.88
  Created 11 candidate models for data size 231
Current R2 threshold: -0.3
  rf-m: R2 = -0.193 (std: 0.231)
  rf-l: R2 = -0.209 (std: 0.216)
  gb-m: R2 = -0.485 (std: 0.317)
  gb-l: R2 = -0.479 (std: 0.316)
  xgb-m: R2 = -0.464 (std: 0.306)
  knn-m: R2 = -0.291 (std: 0.215)
  knn-tuned: R2 = -0.291 (std: 0.215)
  mlp-m: R2 = -1.184 (std: 0.870)
  svr-rbf: R2 = -0.160 (std: 0.169)
  svr-poly: R2 = -0.160 (std: 0.169)
  ridge: R2 = -0.156 (std: 0.193)

Model-based training with 7 models
Best R2: -0.156, Mean R2: -0.370
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9848, entropy=1.2876, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.087
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9818, entropy=1.2757, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.048

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 6 Results ---
  Mean Oracle Reward: 9.908
  Min Oracle Reward: 1.765
  Max Oracle Reward: 12.131
  Std Oracle Reward: 1.882
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: -0.370, Max: -0.156, Count: 11
  Total Sequences Evaluated: 242

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
  TTAACGAGCGGC
  AGATCACGGGCT
  GGACTGAGTCAC
  CAGTTGACACGT
  CCTGATGCGGAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.231
  Max reward: 12.670
  With intrinsic bonuses: 10.281

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9816, entropy=1.2538, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0969

=== Surrogate Model Training ===
Total samples: 274

Training on 263 samples (removed 11 outliers)
Reward range: [6.40, 13.22], mean: 9.92
  Created 11 candidate models for data size 263
Current R2 threshold: -0.3
  rf-m: R2 = -0.204 (std: 0.055)
  rf-l: R2 = -0.191 (std: 0.096)
  gb-m: R2 = -0.340 (std: 0.220)
  gb-l: R2 = -0.345 (std: 0.204)
  xgb-m: R2 = -0.435 (std: 0.181)
  knn-m: R2 = -0.295 (std: 0.110)
  knn-tuned: R2 = -0.295 (std: 0.110)
  mlp-m: R2 = -0.727 (std: 0.540)
  svr-rbf: R2 = -0.139 (std: 0.051)
  svr-poly: R2 = -0.139 (std: 0.051)
  ridge: R2 = -0.113 (std: 0.092)

Model-based training with 7 models
Best R2: -0.113, Mean R2: -0.293
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9805, entropy=1.2478, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.132
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9795, entropy=1.2423, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.076

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 7 Results ---
  Mean Oracle Reward: 10.259
  Min Oracle Reward: 7.934
  Max Oracle Reward: 12.676
  Std Oracle Reward: 1.195
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: -0.293, Max: -0.113, Count: 11
  Total Sequences Evaluated: 274

======================================================================
EXPERIMENT ROUND 8/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.080
Total data collected: 274

--- Round 8 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.080

--- Generated Sequences (Diversity: 1.000) ---
  CAGTCAAGTGCG
  ACGCATAGCGTG
  CGGGCAGTCTAA
  GCAGTCACTCGG
  TTCGATACCGGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.947
  Max reward: 12.359
  With intrinsic bonuses: 9.978

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9752, entropy=1.2295, kl_div=0.0000
    Epoch 1: policy_loss=-0.0266, value_loss=0.9751, entropy=1.2241, kl_div=0.0494

=== Surrogate Model Training ===
Total samples: 306

Training on 291 samples (removed 15 outliers)
Reward range: [6.64, 13.22], mean: 9.98
  Created 11 candidate models for data size 291
Current R2 threshold: -0.3
  rf-m: R2 = -0.139 (std: 0.069)
  rf-l: R2 = -0.157 (std: 0.037)
  gb-m: R2 = -0.269 (std: 0.062)
  gb-l: R2 = -0.268 (std: 0.062)
  xgb-m: R2 = -0.342 (std: 0.120)
  knn-m: R2 = -0.235 (std: 0.079)
  knn-tuned: R2 = -0.235 (std: 0.079)
  mlp-m: R2 = -0.781 (std: 0.385)
  svr-rbf: R2 = -0.110 (std: 0.091)
  svr-poly: R2 = -0.110 (std: 0.091)
  ridge: R2 = -0.127 (std: 0.093)

Model-based training with 9 models
Best R2: -0.110, Mean R2: -0.252
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9820, entropy=1.2189, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.121
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9843, entropy=1.2175, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.255

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 8 Results ---
  Mean Oracle Reward: 9.913
  Min Oracle Reward: 4.394
  Max Oracle Reward: 12.299
  Std Oracle Reward: 1.715
  Sequence Diversity: 1.000
  Models Used: 9
  Model R2 - Mean: -0.252, Max: -0.110, Count: 11
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
  GTCCCGAGAATG
  AGGCGCGCCTAT
  TTGCACGGAGCC
  GCGAGTCCTAGA
  ACCTGGGTACAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.075
  Max reward: 12.525
  With intrinsic bonuses: 10.098

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9831, entropy=1.2081, kl_div=0.0000
    Epoch 1: policy_loss=-0.0081, value_loss=0.9831, entropy=1.2065, kl_div=0.0129

=== Surrogate Model Training ===
Total samples: 338

Training on 320 samples (removed 18 outliers)
Reward range: [6.71, 12.74], mean: 10.00
  Created 14 candidate models for data size 320
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.093 (std: 0.127)
  rf-tuned-xl: R2 = -0.097 (std: 0.124)
  gb-tuned-l: R2 = -0.123 (std: 0.081)
  gb-tuned-xl: R2 = -0.123 (std: 0.081)
  xgb-xl: R2 = -0.248 (std: 0.132)
  xgb-l: R2 = -0.248 (std: 0.132)
  mlp-adaptive-xl: R2 = -0.645 (std: 0.305)
  mlp-l: R2 = -0.702 (std: 0.122)
  svr-rbf-xl: R2 = -0.035 (std: 0.163)
  svr-poly-l: R2 = -0.035 (std: 0.163)
  knn-tuned-sqrt: R2 = -0.190 (std: 0.102)
  knn-tuned-l: R2 = -0.190 (std: 0.102)
  ridge: R2 = -0.127 (std: 0.145)
  gp: R2 = -79.546 (std: 15.079)

Model-based training with 11 models
Best R2: -0.035, Mean R2: -5.886
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9800, entropy=1.2082, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.217
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9819, entropy=1.2109, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.191

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 9 Results ---
  Mean Oracle Reward: 10.082
  Min Oracle Reward: 7.312
  Max Oracle Reward: 12.480
  Std Oracle Reward: 1.042
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -5.886, Max: -0.035, Count: 14
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
  GGGTCCTAGACC
  AATCAGCGCGTG
  ACTGTCCTAGGA
  CGAATCGTGCAG
  CCTAGACGGGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.369
  Max reward: 12.861
  With intrinsic bonuses: 10.250

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9749, entropy=1.1969, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1028

=== Surrogate Model Training ===
Total samples: 370

Training on 350 samples (removed 20 outliers)
Reward range: [6.79, 12.74], mean: 10.05
  Created 14 candidate models for data size 350
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.048 (std: 0.079)
  rf-tuned-xl: R2 = -0.047 (std: 0.071)
  gb-tuned-l: R2 = -0.036 (std: 0.115)
  gb-tuned-xl: R2 = -0.036 (std: 0.116)
  xgb-xl: R2 = -0.200 (std: 0.103)
  xgb-l: R2 = -0.200 (std: 0.103)
  mlp-adaptive-xl: R2 = -0.432 (std: 0.415)
  mlp-l: R2 = -0.616 (std: 0.347)
  svr-rbf-xl: R2 = -0.027 (std: 0.122)
  svr-poly-l: R2 = -0.027 (std: 0.122)
  knn-tuned-sqrt: R2 = -0.092 (std: 0.066)
  knn-tuned-l: R2 = -0.092 (std: 0.066)
  ridge: R2 = -0.102 (std: 0.126)
  gp: R2 = -85.590 (std: 16.387)

Model-based training with 11 models
Best R2: -0.027, Mean R2: -6.253
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9774, entropy=1.1898, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.149
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9761, entropy=1.1786, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.216

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 10 Results ---
  Mean Oracle Reward: 10.348
  Min Oracle Reward: 8.575
  Max Oracle Reward: 12.877
  Std Oracle Reward: 0.963
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -6.253, Max: -0.027, Count: 14
  New best mean reward!
  Total Sequences Evaluated: 370

======================================================================
EXPERIMENT ROUND 11/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 370
  Consistent improvement, increasing LR to 0.000327

--- Round 11 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCCACGGTGTAA
  TATCGCAACGTG
  CGTAGAGCGTCA
  CGGGCAGCACTT
  ACGTCCATGGAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.113
  Max reward: 11.608
  With intrinsic bonuses: 10.097

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9816, entropy=1.1600, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1552

=== Surrogate Model Training ===
Total samples: 402

Training on 379 samples (removed 23 outliers)
Reward range: [6.91, 12.74], mean: 10.09
  Created 14 candidate models for data size 379
Current R2 threshold: -0.29
  rf-tuned-l: R2 = -0.029 (std: 0.121)
  rf-tuned-xl: R2 = -0.013 (std: 0.120)
  gb-tuned-l: R2 = -0.043 (std: 0.176)
  gb-tuned-xl: R2 = -0.042 (std: 0.175)
  xgb-xl: R2 = -0.235 (std: 0.220)
  xgb-l: R2 = -0.235 (std: 0.220)
  mlp-adaptive-xl: R2 = -0.623 (std: 0.624)
  mlp-l: R2 = -0.704 (std: 0.473)
  svr-rbf-xl: R2 = -0.021 (std: 0.111)
  svr-poly-l: R2 = -0.021 (std: 0.111)
  knn-tuned-sqrt: R2 = -0.095 (std: 0.164)
  knn-tuned-l: R2 = -0.095 (std: 0.164)
  ridge: R2 = -0.089 (std: 0.093)
  gp: R2 = -90.965 (std: 22.107)

Model-based training with 11 models
Best R2: -0.013, Mean R2: -6.658
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9833, entropy=1.1533, kl_div=0.0000
  Round 1/2: Mean predicted reward = 10.319
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9764, entropy=1.1500, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.269

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 11 Results ---
  Mean Oracle Reward: 10.038
  Min Oracle Reward: 5.517
  Max Oracle Reward: 11.506
  Std Oracle Reward: 1.271
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -6.658, Max: -0.013, Count: 14
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
  CTGGAGCCATAT
  GGTCACTCTAGA
  TCAAGTGAGCCG
  CATACGGCGATG
  ATCAGGCATCGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.876
  Max reward: 12.313
  With intrinsic bonuses: 9.913

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9807, entropy=1.1068, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1353

=== Surrogate Model Training ===
Total samples: 434

Training on 410 samples (removed 24 outliers)
Reward range: [6.83, 12.98], mean: 10.08
  Created 14 candidate models for data size 410
Current R2 threshold: -0.27999999999999997
  rf-tuned-l: R2 = 0.006 (std: 0.095)
  rf-tuned-xl: R2 = 0.017 (std: 0.063)
  gb-tuned-l: R2 = 0.023 (std: 0.111)
  gb-tuned-xl: R2 = 0.022 (std: 0.110)
  xgb-xl: R2 = -0.206 (std: 0.200)
  xgb-l: R2 = -0.206 (std: 0.200)
  mlp-adaptive-xl: R2 = -0.403 (std: 0.265)
  mlp-l: R2 = -0.540 (std: 0.416)
  svr-rbf-xl: R2 = 0.014 (std: 0.101)
  svr-poly-l: R2 = 0.014 (std: 0.101)
  knn-tuned-sqrt: R2 = -0.037 (std: 0.055)
  knn-tuned-l: R2 = -0.037 (std: 0.055)
  ridge: R2 = -0.083 (std: 0.111)
  gp: R2 = -86.486 (std: 13.082)

Model-based training with 11 models
Best R2: 0.023, Mean R2: -6.279
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9779, entropy=1.1131, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0915
  Round 1/3: Mean predicted reward = 10.154
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9830, entropy=1.0898, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1407
  Round 2/3: Mean predicted reward = 10.084
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9774, entropy=1.0803, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1911
  Round 3/3: Mean predicted reward = 10.206

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 12 Results ---
  Mean Oracle Reward: 9.905
  Min Oracle Reward: 6.561
  Max Oracle Reward: 12.777
  Std Oracle Reward: 1.342
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -6.279, Max: 0.023, Count: 14
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
  GACCAATGGTGC
  AATGGTAGCGCC
  AGAGTTCAGCGC
  GCAAGTACGTCG
  TTCCTCGAAGGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.004
  Max reward: 12.055
  With intrinsic bonuses: 10.001

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9742, entropy=1.0636, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1432

=== Surrogate Model Training ===
Total samples: 466

Training on 439 samples (removed 27 outliers)
Reward range: [6.91, 12.98], mean: 10.11
  Created 14 candidate models for data size 439
Current R2 threshold: -0.27
  rf-tuned-l: R2 = -0.010 (std: 0.060)
  rf-tuned-xl: R2 = -0.016 (std: 0.049)
  gb-tuned-l: R2 = 0.013 (std: 0.068)
  gb-tuned-xl: R2 = 0.013 (std: 0.068)
  xgb-xl: R2 = -0.212 (std: 0.109)
  xgb-l: R2 = -0.212 (std: 0.109)
  mlp-adaptive-xl: R2 = -0.448 (std: 0.310)
  mlp-l: R2 = -0.465 (std: 0.364)
  svr-rbf-xl: R2 = 0.015 (std: 0.083)
  svr-poly-l: R2 = 0.015 (std: 0.083)
  knn-tuned-sqrt: R2 = -0.097 (std: 0.040)
  knn-tuned-l: R2 = -0.097 (std: 0.040)
  ridge: R2 = -0.070 (std: 0.103)
  gp: R2 = -88.193 (std: 13.405)

Model-based training with 11 models
Best R2: 0.015, Mean R2: -6.412
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9741, entropy=1.0540, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1150
  Round 1/3: Mean predicted reward = 10.050
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9768, entropy=1.0546, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1516
  Round 2/3: Mean predicted reward = 10.189
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9786, entropy=1.0329, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1570
  Round 3/3: Mean predicted reward = 10.207

  === Progress Analysis ===
  Status: NORMAL

--- Round 13 Results ---
  Mean Oracle Reward: 9.995
  Min Oracle Reward: 4.547
  Max Oracle Reward: 12.038
  Std Oracle Reward: 1.599
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -6.412, Max: 0.015, Count: 14
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
  AAGGTGCCATCT
  CAGTGCCCGATG
  AGGCAGTCTCCG
  TAGCGCAAGTGC
  CGGCATGGTCAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.803
  Max reward: 11.545
  With intrinsic bonuses: 9.900

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9810, entropy=1.0137, kl_div=0.0000
    Epoch 1: policy_loss=-0.0041, value_loss=0.9810, entropy=1.0114, kl_div=0.0268

=== Surrogate Model Training ===
Total samples: 498

Training on 471 samples (removed 27 outliers)
Reward range: [6.91, 12.98], mean: 10.09
  Created 14 candidate models for data size 471
Current R2 threshold: -0.26
  rf-tuned-l: R2 = 0.001 (std: 0.020)
  rf-tuned-xl: R2 = 0.016 (std: 0.010)
  gb-tuned-l: R2 = 0.003 (std: 0.036)
  gb-tuned-xl: R2 = 0.003 (std: 0.036)
  xgb-xl: R2 = -0.149 (std: 0.065)
  xgb-l: R2 = -0.149 (std: 0.065)
  mlp-adaptive-xl: R2 = -0.352 (std: 0.216)
  mlp-l: R2 = -0.377 (std: 0.179)
  svr-rbf-xl: R2 = 0.014 (std: 0.043)
  svr-poly-l: R2 = 0.014 (std: 0.043)
  knn-tuned-sqrt: R2 = -0.076 (std: 0.027)
  knn-tuned-l: R2 = -0.076 (std: 0.027)
  ridge: R2 = -0.074 (std: 0.089)
  gp: R2 = -88.259 (std: 12.230)

Model-based training with 11 models
Best R2: 0.016, Mean R2: -6.390
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9752, entropy=1.0128, kl_div=0.0000
    Epoch 1: policy_loss=-0.0085, value_loss=0.9751, entropy=1.0106, kl_div=0.0263
  Round 1/3: Mean predicted reward = 10.189
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9793, entropy=1.0087, kl_div=0.0000
    Epoch 1: policy_loss=-0.0162, value_loss=0.9793, entropy=1.0062, kl_div=0.0320
  Round 2/3: Mean predicted reward = 10.178
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9775, entropy=1.0063, kl_div=0.0000
    Epoch 1: policy_loss=-0.0128, value_loss=0.9775, entropy=1.0033, kl_div=0.0285
  Round 3/3: Mean predicted reward = 10.204

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 14 Results ---
  Mean Oracle Reward: 9.839
  Min Oracle Reward: 7.186
  Max Oracle Reward: 11.439
  Std Oracle Reward: 0.966
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -6.390, Max: 0.016, Count: 14
  Total Sequences Evaluated: 498

======================================================================
EXPERIMENT ROUND 15/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 498
  Performance plateaued, reducing LR to 0.000150

--- Round 15 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTGCGCTAGAAC
  GACATACGCTGG
  ACCACAGGGTTT
  AGCATTCGAGCG
  TCCGAGGTACCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.212
  Max reward: 13.003
  With intrinsic bonuses: 10.208

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9819, entropy=0.9974, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3281

=== Surrogate Model Training ===
Total samples: 530

Training on 503 samples (removed 27 outliers)
Reward range: [6.91, 12.98], mean: 10.10
  Created 13 candidate models for data size 503
Current R2 threshold: -0.25
  rf-tuned-l: R2 = 0.007 (std: 0.036)
  rf-tuned-xl: R2 = 0.001 (std: 0.027)
  gb-tuned-l: R2 = 0.012 (std: 0.064)
  gb-tuned-xl: R2 = 0.012 (std: 0.064)
  xgb-xl: R2 = -0.150 (std: 0.063)
  xgb-l: R2 = -0.150 (std: 0.063)
  mlp-adaptive-xl: R2 = -0.446 (std: 0.269)
  mlp-l: R2 = -0.391 (std: 0.331)
  svr-rbf-xl: R2 = 0.011 (std: 0.061)
  svr-poly-l: R2 = 0.011 (std: 0.061)
  knn-tuned-sqrt: R2 = -0.110 (std: 0.057)
  knn-tuned-l: R2 = -0.110 (std: 0.057)
  ridge: R2 = -0.083 (std: 0.108)

Model-based training with 11 models
Best R2: 0.012, Mean R2: -0.107
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9757, entropy=0.9676, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3307
  Round 1/3: Mean predicted reward = 10.106
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9781, entropy=0.9410, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3916
  Round 2/3: Mean predicted reward = 10.162
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9774, entropy=0.9295, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3770
  Round 3/3: Mean predicted reward = 10.062

  === Progress Analysis ===
  Status: NORMAL

--- Round 15 Results ---
  Mean Oracle Reward: 10.211
  Min Oracle Reward: 7.684
  Max Oracle Reward: 12.779
  Std Oracle Reward: 1.213
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -0.107, Max: 0.012, Count: 13
  Total Sequences Evaluated: 530

======================================================================
EXPERIMENT ROUND 16/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 530

--- Round 16 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCAGTCCAGAGT
  ACGCATTGAGGC
  ATCATGGGGCCA
  GCTCGCTGGCAA
  TGCCAGATGCGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.243
  Max reward: 13.238
  With intrinsic bonuses: 10.195

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9814, entropy=0.9046, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6382

=== Surrogate Model Training ===
Total samples: 562

Training on 537 samples (removed 25 outliers)
Reward range: [6.79, 13.22], mean: 10.10
  Created 13 candidate models for data size 537
Current R2 threshold: -0.24
  rf-tuned-l: R2 = 0.037 (std: 0.065)
  rf-tuned-xl: R2 = 0.026 (std: 0.059)
  gb-tuned-l: R2 = 0.030 (std: 0.020)
  gb-tuned-xl: R2 = 0.031 (std: 0.020)
  xgb-xl: R2 = -0.135 (std: 0.146)
  xgb-l: R2 = -0.135 (std: 0.146)
  mlp-adaptive-xl: R2 = -0.344 (std: 0.214)
  mlp-l: R2 = -0.243 (std: 0.164)
  svr-rbf-xl: R2 = 0.063 (std: 0.035)
  svr-poly-l: R2 = 0.063 (std: 0.035)
  knn-tuned-sqrt: R2 = -0.058 (std: 0.075)
  knn-tuned-l: R2 = -0.058 (std: 0.075)
  ridge: R2 = -0.070 (std: 0.084)

Model-based training with 11 models
Best R2: 0.063, Mean R2: -0.061
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9761, entropy=0.8554, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7344
  Round 1/3: Mean predicted reward = 10.165
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9801, entropy=0.8140, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5694
  Round 2/3: Mean predicted reward = 10.128
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9784, entropy=0.7723, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7575
  Round 3/3: Mean predicted reward = 10.108

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 16 Results ---
  Mean Oracle Reward: 10.251
  Min Oracle Reward: 8.410
  Max Oracle Reward: 13.297
  Std Oracle Reward: 1.120
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -0.061, Max: 0.063, Count: 13
  Total Sequences Evaluated: 562

======================================================================
EXPERIMENT ROUND 17/100
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
  GTAGCTGCCACG
  ACCCGCTGGGTA
  CGCTAATGAGCT
  GGCCCCTTAAGG
  ACATAGTGGCGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.944
  Max reward: 11.818
  With intrinsic bonuses: 9.936

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9811, entropy=0.7663, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6651

=== Surrogate Model Training ===
Total samples: 594

Training on 567 samples (removed 27 outliers)
Reward range: [6.83, 13.22], mean: 10.10
  Created 13 candidate models for data size 567
Current R2 threshold: -0.22999999999999998
  rf-tuned-l: R2 = 0.015 (std: 0.024)
  rf-tuned-xl: R2 = 0.024 (std: 0.029)
  gb-tuned-l: R2 = 0.007 (std: 0.054)
  gb-tuned-xl: R2 = 0.007 (std: 0.054)
  xgb-xl: R2 = -0.190 (std: 0.093)
  xgb-l: R2 = -0.190 (std: 0.093)
  mlp-adaptive-xl: R2 = -0.244 (std: 0.155)
  mlp-l: R2 = -0.244 (std: 0.161)
  svr-rbf-xl: R2 = 0.039 (std: 0.022)
  svr-poly-l: R2 = 0.039 (std: 0.022)
  knn-tuned-sqrt: R2 = -0.091 (std: 0.073)
  knn-tuned-l: R2 = -0.091 (std: 0.073)
  ridge: R2 = -0.054 (std: 0.066)

Model-based training with 11 models
Best R2: 0.039, Mean R2: -0.075
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9761, entropy=0.7226, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7747
  Round 1/3: Mean predicted reward = 10.114
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9804, entropy=0.7112, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7923
  Round 2/3: Mean predicted reward = 10.196
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9802, entropy=0.6746, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8845
  Round 3/3: Mean predicted reward = 10.212

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 17 Results ---
  Mean Oracle Reward: 9.949
  Min Oracle Reward: 5.895
  Max Oracle Reward: 11.892
  Std Oracle Reward: 1.206
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -0.075, Max: 0.039, Count: 13
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

--- Generated Sequences (Diversity: 0.969) ---
  AACCGGGTGTCA
  GGACGCGTACTC
  CGATGCGCTAGA
  TGGCTGAACCCG
  ATGCGGCCAGTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.167
  Max reward: 13.367
  With intrinsic bonuses: 10.097

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9782, entropy=0.6435, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3401

=== Surrogate Model Training ===
Total samples: 626

Training on 600 samples (removed 26 outliers)
Reward range: [6.79, 13.22], mean: 10.10
  Created 13 candidate models for data size 600
Current R2 threshold: -0.21999999999999997
  rf-tuned-l: R2 = 0.035 (std: 0.073)
  rf-tuned-xl: R2 = 0.023 (std: 0.070)
  gb-tuned-l: R2 = 0.026 (std: 0.088)
  gb-tuned-xl: R2 = 0.026 (std: 0.088)
  xgb-xl: R2 = -0.153 (std: 0.113)
  xgb-l: R2 = -0.153 (std: 0.113)
  mlp-adaptive-xl: R2 = -0.209 (std: 0.168)
  mlp-l: R2 = -0.238 (std: 0.234)
  svr-rbf-xl: R2 = 0.079 (std: 0.018)
  svr-poly-l: R2 = 0.079 (std: 0.018)
  knn-tuned-sqrt: R2 = -0.044 (std: 0.113)
  knn-tuned-l: R2 = -0.044 (std: 0.113)
  ridge: R2 = -0.036 (std: 0.057)

Model-based training with 12 models
Best R2: 0.079, Mean R2: -0.047
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9772, entropy=0.6367, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4096
  Round 1/3: Mean predicted reward = 9.937
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9791, entropy=0.6361, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2641
  Round 2/3: Mean predicted reward = 10.240
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9783, entropy=0.6306, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3287
  Round 3/3: Mean predicted reward = 10.155

  === Progress Analysis ===
  Status: NORMAL

--- Round 18 Results ---
  Mean Oracle Reward: 10.145
  Min Oracle Reward: 6.760
  Max Oracle Reward: 13.001
  Std Oracle Reward: 1.395
  Sequence Diversity: 0.969
  Models Used: 12
  Model R2 - Mean: -0.047, Max: 0.079, Count: 13
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
  AGCTCGAGCCTG
  CATTGGCCGGCA
  GAGGACACGTCT
  GGACGCTATCAG
  GCTGCGACCAGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.228
  Max reward: 13.047
  With intrinsic bonuses: 10.245

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9769, entropy=0.6350, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0991

=== Surrogate Model Training ===
Total samples: 658

Training on 634 samples (removed 24 outliers)
Reward range: [6.75, 13.31], mean: 10.11
  Created 13 candidate models for data size 634
Current R2 threshold: -0.21
  rf-tuned-l: R2 = 0.034 (std: 0.063)
  rf-tuned-xl: R2 = 0.044 (std: 0.062)
  gb-tuned-l: R2 = 0.032 (std: 0.098)
  gb-tuned-xl: R2 = 0.032 (std: 0.098)
  xgb-xl: R2 = -0.180 (std: 0.180)
  xgb-l: R2 = -0.180 (std: 0.180)
  mlp-adaptive-xl: R2 = -0.187 (std: 0.198)
  mlp-l: R2 = -0.245 (std: 0.260)
  svr-rbf-xl: R2 = 0.095 (std: 0.025)
  svr-poly-l: R2 = 0.095 (std: 0.025)
  knn-tuned-sqrt: R2 = -0.015 (std: 0.145)
  knn-tuned-l: R2 = -0.015 (std: 0.145)
  ridge: R2 = -0.047 (std: 0.062)

Model-based training with 12 models
Best R2: 0.095, Mean R2: -0.041
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9795, entropy=0.6041, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0763
  Round 1/3: Mean predicted reward = 10.074
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9762, entropy=0.6060, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0974
  Round 2/3: Mean predicted reward = 10.100
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9715, entropy=0.6267, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1032
  Round 3/3: Mean predicted reward = 10.225

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 19 Results ---
  Mean Oracle Reward: 10.230
  Min Oracle Reward: 6.914
  Max Oracle Reward: 13.202
  Std Oracle Reward: 1.309
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: -0.041, Max: 0.095, Count: 13
  Total Sequences Evaluated: 658

======================================================================
EXPERIMENT ROUND 20/100
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
  CCCAGGATGCGT
  CACGACGGGCTT
  AAGGCCTGAGTC
  GTGCTAACGGCC
  TAAGATCTGCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.326
  Max reward: 12.272
  With intrinsic bonuses: 10.328

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9828, entropy=0.6055, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0398

=== Surrogate Model Training ===
Total samples: 690

Training on 661 samples (removed 29 outliers)
Reward range: [6.88, 13.22], mean: 10.14
  Created 13 candidate models for data size 661
Current R2 threshold: -0.19999999999999998
  rf-tuned-l: R2 = 0.059 (std: 0.056)
  rf-tuned-xl: R2 = 0.061 (std: 0.065)
  gb-tuned-l: R2 = 0.050 (std: 0.096)
  gb-tuned-xl: R2 = 0.050 (std: 0.096)
  xgb-xl: R2 = -0.124 (std: 0.132)
  xgb-l: R2 = -0.124 (std: 0.132)
  mlp-adaptive-xl: R2 = -0.158 (std: 0.156)
  mlp-l: R2 = -0.224 (std: 0.164)
  svr-rbf-xl: R2 = 0.071 (std: 0.067)
  svr-poly-l: R2 = 0.071 (std: 0.067)
  knn-tuned-sqrt: R2 = -0.023 (std: 0.132)
  knn-tuned-l: R2 = -0.023 (std: 0.132)
  ridge: R2 = -0.052 (std: 0.069)

Model-based training with 12 models
Best R2: 0.071, Mean R2: -0.028
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9776, entropy=0.5897, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1182
  Round 1/3: Mean predicted reward = 10.004
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9762, entropy=0.5744, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9426
  Round 2/3: Mean predicted reward = 10.066
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9760, entropy=0.5276, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1171
  Round 3/3: Mean predicted reward = 10.230

  === Progress Analysis ===
  Status: NORMAL

--- Round 20 Results ---
  Mean Oracle Reward: 10.367
  Min Oracle Reward: 5.254
  Max Oracle Reward: 12.301
  Std Oracle Reward: 1.203
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: -0.028, Max: 0.071, Count: 13
  New best mean reward!
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
  TCAACGGGCTCG
  AGCCGGGACATT
  AGGACGCATTCG
  ATCCCGCGAGGT
  TAACATGCGGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.254
  Max reward: 14.121
  With intrinsic bonuses: 10.197

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9751, entropy=0.5393, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5043

=== Surrogate Model Training ===
Total samples: 722

Training on 692 samples (removed 30 outliers)
Reward range: [6.88, 13.22], mean: 10.13
  Created 13 candidate models for data size 692
Current R2 threshold: -0.19
  rf-tuned-l: R2 = 0.101 (std: 0.051)
  rf-tuned-xl: R2 = 0.096 (std: 0.060)
  gb-tuned-l: R2 = 0.062 (std: 0.062)
  gb-tuned-xl: R2 = 0.063 (std: 0.063)
  xgb-xl: R2 = -0.144 (std: 0.120)
  xgb-l: R2 = -0.144 (std: 0.120)
  mlp-adaptive-xl: R2 = -0.116 (std: 0.101)
  mlp-l: R2 = -0.106 (std: 0.119)
  svr-rbf-xl: R2 = 0.098 (std: 0.055)
  svr-poly-l: R2 = 0.098 (std: 0.055)
  knn-tuned-sqrt: R2 = -0.016 (std: 0.117)
  knn-tuned-l: R2 = -0.016 (std: 0.117)
  ridge: R2 = -0.021 (std: 0.048)

Model-based training with 13 models
Best R2: 0.101, Mean R2: -0.003
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9773, entropy=0.5237, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5246
  Round 1/3: Mean predicted reward = 9.762
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9745, entropy=0.5249, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3933
  Round 2/3: Mean predicted reward = 9.998
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9769, entropy=0.5034, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4842
  Round 3/3: Mean predicted reward = 10.083

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 21 Results ---
  Mean Oracle Reward: 10.190
  Min Oracle Reward: 7.107
  Max Oracle Reward: 14.394
  Std Oracle Reward: 1.420
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.003, Max: 0.101, Count: 13
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
  GTTGAAACCCGT
  TGATCCTCGAAG
  TCACAGGTGCCG
  CCCCGAATGTGG
  AATGTCCCCGGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.957
  Max reward: 12.836
  With intrinsic bonuses: 9.954

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9740, entropy=0.5004, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4876

=== Surrogate Model Training ===
Total samples: 754

Training on 724 samples (removed 30 outliers)
Reward range: [6.83, 13.22], mean: 10.13
  Created 13 candidate models for data size 724
Current R2 threshold: -0.18
  rf-tuned-l: R2 = 0.123 (std: 0.067)
  rf-tuned-xl: R2 = 0.110 (std: 0.067)
  gb-tuned-l: R2 = 0.099 (std: 0.047)
  gb-tuned-xl: R2 = 0.098 (std: 0.047)
  xgb-xl: R2 = -0.097 (std: 0.122)
  xgb-l: R2 = -0.097 (std: 0.122)
  mlp-adaptive-xl: R2 = -0.140 (std: 0.144)
  mlp-l: R2 = -0.071 (std: 0.134)
  svr-rbf-xl: R2 = 0.128 (std: 0.047)
  svr-poly-l: R2 = 0.128 (std: 0.047)
  knn-tuned-sqrt: R2 = 0.026 (std: 0.083)
  knn-tuned-l: R2 = 0.026 (std: 0.083)
  ridge: R2 = -0.005 (std: 0.041)

Model-based training with 13 models
Best R2: 0.128, Mean R2: 0.025
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9804, entropy=0.4888, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2908
  Round 1/3: Mean predicted reward = 9.877
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9772, entropy=0.5190, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1542
  Round 2/3: Mean predicted reward = 9.920
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9769, entropy=0.4945, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0698
  Round 3/3: Mean predicted reward = 9.993

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 22 Results ---
  Mean Oracle Reward: 10.002
  Min Oracle Reward: 6.789
  Max Oracle Reward: 12.651
  Std Oracle Reward: 1.428
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.025, Max: 0.128, Count: 13
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

--- Generated Sequences (Diversity: 0.969) ---
  TGAGGAGCCACT
  GTGACACCTGGA
  GACCCTTGAGAG
  GACCCGGTGCTA
  TACTAAGTCCGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.754
  Max reward: 14.064
  With intrinsic bonuses: 9.772

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9785, entropy=0.5074, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1501

=== Surrogate Model Training ===
Total samples: 786

Training on 753 samples (removed 33 outliers)
Reward range: [6.88, 13.22], mean: 10.12
  Created 13 candidate models for data size 753
Current R2 threshold: -0.16999999999999998
  rf-tuned-l: R2 = 0.115 (std: 0.074)
  rf-tuned-xl: R2 = 0.102 (std: 0.074)
  gb-tuned-l: R2 = 0.118 (std: 0.087)
  gb-tuned-xl: R2 = 0.118 (std: 0.087)
  xgb-xl: R2 = -0.079 (std: 0.103)
  xgb-l: R2 = -0.079 (std: 0.103)
  mlp-adaptive-xl: R2 = -0.164 (std: 0.100)
  mlp-l: R2 = -0.141 (std: 0.196)
  svr-rbf-xl: R2 = 0.138 (std: 0.060)
  svr-poly-l: R2 = 0.138 (std: 0.060)
  knn-tuned-sqrt: R2 = 0.004 (std: 0.111)
  knn-tuned-l: R2 = 0.004 (std: 0.111)
  ridge: R2 = 0.002 (std: 0.044)

Model-based training with 13 models
Best R2: 0.138, Mean R2: 0.021
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9801, entropy=0.5139, kl_div=0.0000
    Epoch 1: policy_loss=-0.0082, value_loss=0.9801, entropy=0.5162, kl_div=0.0047
  Round 1/3: Mean predicted reward = 9.716
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9770, entropy=0.5273, kl_div=0.0000
    Epoch 1: policy_loss=-0.0650, value_loss=0.9770, entropy=0.5329, kl_div=-0.1498
  Round 2/3: Mean predicted reward = 9.884
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9772, entropy=0.5312, kl_div=0.0000
    Epoch 1: policy_loss=0.0150, value_loss=0.9772, entropy=0.5349, kl_div=-0.0749
  Round 3/3: Mean predicted reward = 10.169

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 23 Results ---
  Mean Oracle Reward: 9.813
  Min Oracle Reward: 6.213
  Max Oracle Reward: 13.807
  Std Oracle Reward: 1.376
  Sequence Diversity: 0.969
  Models Used: 13
  Model R2 - Mean: 0.021, Max: 0.138, Count: 13
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
  CACCGTGTCAGG
  TGAAGCTGCGCC
  CACGCGTTGAGC
  TCGCGGACCAGT
  CGATCTCGGGAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.572
  Max reward: 12.872
  With intrinsic bonuses: 9.601

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9772, entropy=0.5067, kl_div=0.0000
    Epoch 1: policy_loss=-0.0100, value_loss=0.9772, entropy=0.5073, kl_div=0.0081

=== Surrogate Model Training ===
Total samples: 818

Training on 783 samples (removed 35 outliers)
Reward range: [6.83, 13.22], mean: 10.11
  Created 13 candidate models for data size 783
Current R2 threshold: -0.15999999999999998
  rf-tuned-l: R2 = 0.108 (std: 0.044)
  rf-tuned-xl: R2 = 0.109 (std: 0.059)
  gb-tuned-l: R2 = 0.133 (std: 0.072)
  gb-tuned-xl: R2 = 0.133 (std: 0.072)
  xgb-xl: R2 = -0.041 (std: 0.053)
  xgb-l: R2 = -0.041 (std: 0.053)
  mlp-adaptive-xl: R2 = 0.021 (std: 0.105)
  mlp-l: R2 = -0.006 (std: 0.132)
  svr-rbf-xl: R2 = 0.144 (std: 0.041)
  svr-poly-l: R2 = 0.144 (std: 0.041)
  knn-tuned-sqrt: R2 = 0.026 (std: 0.096)
  knn-tuned-l: R2 = 0.026 (std: 0.096)
  ridge: R2 = -0.004 (std: 0.047)

Model-based training with 13 models
Best R2: 0.144, Mean R2: 0.058
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9774, entropy=0.5274, kl_div=0.0000
    Epoch 1: policy_loss=-0.0281, value_loss=0.9774, entropy=0.5289, kl_div=-0.0292
  Round 1/3: Mean predicted reward = 9.625
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9779, entropy=0.5226, kl_div=0.0000
    Epoch 1: policy_loss=-0.0107, value_loss=0.9779, entropy=0.5246, kl_div=-0.0718
  Round 2/3: Mean predicted reward = 10.106
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9757, entropy=0.5283, kl_div=0.0000
    Epoch 1: policy_loss=-0.0299, value_loss=0.9757, entropy=0.5304, kl_div=-0.0857
  Round 3/3: Mean predicted reward = 9.944

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 24 Results ---
  Mean Oracle Reward: 9.604
  Min Oracle Reward: 5.042
  Max Oracle Reward: 12.713
  Std Oracle Reward: 1.598
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.058, Max: 0.144, Count: 13
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
  TGGGCCCGACTA
  AGGGCCGCTCTA
  GTGGACCCTGCA
  CTCCAGCATGGG
  GAGCTATCTCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.342
  Max reward: 12.666
  With intrinsic bonuses: 10.334

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9741, entropy=0.5505, kl_div=0.0000
    Epoch 1: policy_loss=0.1948, value_loss=0.9740, entropy=0.5607, kl_div=-0.3547

=== Surrogate Model Training ===
Total samples: 850

Training on 812 samples (removed 38 outliers)
Reward range: [6.91, 13.22], mean: 10.13
  Created 13 candidate models for data size 812
Current R2 threshold: -0.15
  rf-tuned-l: R2 = 0.098 (std: 0.065)
  rf-tuned-xl: R2 = 0.086 (std: 0.067)
  gb-tuned-l: R2 = 0.108 (std: 0.077)
  gb-tuned-xl: R2 = 0.108 (std: 0.077)
  xgb-xl: R2 = -0.135 (std: 0.149)
  xgb-l: R2 = -0.135 (std: 0.149)
  mlp-adaptive-xl: R2 = -0.025 (std: 0.198)
  mlp-l: R2 = -0.059 (std: 0.090)
  svr-rbf-xl: R2 = 0.121 (std: 0.053)
  svr-poly-l: R2 = 0.121 (std: 0.053)
  knn-tuned-sqrt: R2 = 0.005 (std: 0.101)
  knn-tuned-l: R2 = 0.005 (std: 0.101)
  ridge: R2 = 0.002 (std: 0.048)

Model-based training with 13 models
Best R2: 0.121, Mean R2: 0.023
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9779, entropy=0.5620, kl_div=0.0000
    Epoch 1: policy_loss=0.0187, value_loss=0.9778, entropy=0.5717, kl_div=-0.3298
  Round 1/3: Mean predicted reward = 9.907
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9762, entropy=0.5564, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1217
  Round 2/3: Mean predicted reward = 9.913
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9751, entropy=0.5695, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3185
  Round 3/3: Mean predicted reward = 10.212

  === Progress Analysis ===
  Status: NORMAL

--- Round 25 Results ---
  Mean Oracle Reward: 10.390
  Min Oracle Reward: 6.587
  Max Oracle Reward: 12.808
  Std Oracle Reward: 1.196
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.023, Max: 0.121, Count: 13
  New best mean reward!
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
  TGACGTAGCCCG
  GGCCCGGAATCT
  CCGGAGGACTTC
  GCTACAATCGGG
  GGCGCTTCACAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.402
  Max reward: 12.962
  With intrinsic bonuses: 10.425

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9742, entropy=0.5685, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4667

=== Surrogate Model Training ===
Total samples: 882

Training on 842 samples (removed 40 outliers)
Reward range: [7.00, 13.15], mean: 10.14
  Created 13 candidate models for data size 842
Current R2 threshold: -0.13999999999999999
  rf-tuned-l: R2 = 0.139 (std: 0.102)
  rf-tuned-xl: R2 = 0.125 (std: 0.106)
  gb-tuned-l: R2 = 0.101 (std: 0.085)
  gb-tuned-xl: R2 = 0.101 (std: 0.085)
  xgb-xl: R2 = -0.028 (std: 0.107)
  xgb-l: R2 = -0.028 (std: 0.107)
  mlp-adaptive-xl: R2 = -0.050 (std: 0.145)
  mlp-l: R2 = -0.026 (std: 0.132)
  svr-rbf-xl: R2 = 0.145 (std: 0.082)
  svr-poly-l: R2 = 0.145 (std: 0.082)
  knn-tuned-sqrt: R2 = 0.027 (std: 0.116)
  knn-tuned-l: R2 = 0.027 (std: 0.116)
  ridge: R2 = 0.012 (std: 0.053)

Model-based training with 13 models
Best R2: 0.145, Mean R2: 0.053
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9755, entropy=0.5714, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2130
  Round 1/3: Mean predicted reward = 9.977
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9779, entropy=0.5755, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4623
  Round 2/3: Mean predicted reward = 10.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9747, entropy=0.5779, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5058
  Round 3/3: Mean predicted reward = 10.204

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 26 Results ---
  Mean Oracle Reward: 10.426
  Min Oracle Reward: 7.514
  Max Oracle Reward: 12.962
  Std Oracle Reward: 1.211
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.053, Max: 0.145, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 882

======================================================================
EXPERIMENT ROUND 27/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 882
  Consistent improvement, increasing LR to 0.000240

--- Round 27 Configuration ---
Learning rate: 0.000240
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCCTCGGTAAGC
  GCGGTTCACCAG
  GTCGAAGTATCC
  GGCAGACTACTG
  CCGGACGCATTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.146
  Max reward: 12.808
  With intrinsic bonuses: 10.158

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9743, entropy=0.5566, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6635

=== Surrogate Model Training ===
Total samples: 914

Training on 872 samples (removed 42 outliers)
Reward range: [7.09, 13.15], mean: 10.14
  Created 13 candidate models for data size 872
Current R2 threshold: -0.12999999999999998
  rf-tuned-l: R2 = 0.140 (std: 0.083)
  rf-tuned-xl: R2 = 0.143 (std: 0.098)
  gb-tuned-l: R2 = 0.144 (std: 0.076)
  gb-tuned-xl: R2 = 0.144 (std: 0.076)
  xgb-xl: R2 = -0.011 (std: 0.074)
  xgb-l: R2 = -0.011 (std: 0.074)
  mlp-adaptive-xl: R2 = -0.027 (std: 0.083)
  mlp-l: R2 = 0.012 (std: 0.106)
  svr-rbf-xl: R2 = 0.157 (std: 0.071)
  svr-poly-l: R2 = 0.157 (std: 0.071)
  knn-tuned-sqrt: R2 = 0.032 (std: 0.095)
  knn-tuned-l: R2 = 0.032 (std: 0.095)
  ridge: R2 = 0.027 (std: 0.051)

Model-based training with 13 models
Best R2: 0.157, Mean R2: 0.072
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9775, entropy=0.5609, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7378
  Round 1/3: Mean predicted reward = 9.968
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9788, entropy=0.5753, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4333
  Round 2/3: Mean predicted reward = 9.988
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9758, entropy=0.5612, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6221
  Round 3/3: Mean predicted reward = 10.316

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 27 Results ---
  Mean Oracle Reward: 10.100
  Min Oracle Reward: 6.975
  Max Oracle Reward: 12.796
  Std Oracle Reward: 1.173
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.072, Max: 0.157, Count: 13
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
  GTCCTGGACACG
  CGCACTGAGGCT
  GCGCGAAACTTT
  CGGACGCCTAGT
  ACGACGTCCTGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.187
  Max reward: 12.851
  With intrinsic bonuses: 10.223

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9729, entropy=0.5437, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3601

=== Surrogate Model Training ===
Total samples: 946

Training on 904 samples (removed 42 outliers)
Reward range: [7.09, 13.15], mean: 10.15
  Created 13 candidate models for data size 904
Current R2 threshold: -0.12
  rf-tuned-l: R2 = 0.136 (std: 0.121)
  rf-tuned-xl: R2 = 0.141 (std: 0.105)
  gb-tuned-l: R2 = 0.132 (std: 0.107)
  gb-tuned-xl: R2 = 0.132 (std: 0.107)
  xgb-xl: R2 = -0.013 (std: 0.099)
  xgb-l: R2 = -0.013 (std: 0.099)
  mlp-adaptive-xl: R2 = -0.034 (std: 0.138)
  mlp-l: R2 = -0.020 (std: 0.137)
  svr-rbf-xl: R2 = 0.164 (std: 0.079)
  svr-poly-l: R2 = 0.164 (std: 0.079)
  knn-tuned-sqrt: R2 = 0.038 (std: 0.119)
  knn-tuned-l: R2 = 0.038 (std: 0.119)
  ridge: R2 = 0.033 (std: 0.066)

Model-based training with 13 models
Best R2: 0.164, Mean R2: 0.069
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9760, entropy=0.5500, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2023
  Round 1/3: Mean predicted reward = 9.839
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9773, entropy=0.5308, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2700
  Round 2/3: Mean predicted reward = 10.009
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9783, entropy=0.5516, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3541
  Round 3/3: Mean predicted reward = 10.192

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 28 Results ---
  Mean Oracle Reward: 10.230
  Min Oracle Reward: 7.287
  Max Oracle Reward: 12.724
  Std Oracle Reward: 1.275
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.069, Max: 0.164, Count: 13
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
  TGAGCCGTCGAC
  GGTAAGCCTACG
  TCTGGACGGCCA
  TGCCGATGACGC
  GACCGTTCAGGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.168
  Max reward: 12.804
  With intrinsic bonuses: 10.182

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9762, entropy=0.5473, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1645

=== Surrogate Model Training ===
Total samples: 978

Training on 935 samples (removed 43 outliers)
Reward range: [7.09, 13.15], mean: 10.15
  Created 13 candidate models for data size 935
Current R2 threshold: -0.10999999999999999
  rf-tuned-l: R2 = 0.141 (std: 0.112)
  rf-tuned-xl: R2 = 0.142 (std: 0.124)
  gb-tuned-l: R2 = 0.146 (std: 0.110)
  gb-tuned-xl: R2 = 0.146 (std: 0.110)
  xgb-xl: R2 = -0.014 (std: 0.134)
  xgb-l: R2 = -0.014 (std: 0.134)
  mlp-adaptive-xl: R2 = 0.014 (std: 0.155)
  mlp-l: R2 = 0.030 (std: 0.182)
  svr-rbf-xl: R2 = 0.171 (std: 0.078)
  svr-poly-l: R2 = 0.171 (std: 0.078)
  knn-tuned-sqrt: R2 = 0.041 (std: 0.142)
  knn-tuned-l: R2 = 0.041 (std: 0.142)
  ridge: R2 = 0.033 (std: 0.070)

Model-based training with 13 models
Best R2: 0.171, Mean R2: 0.081
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9750, entropy=0.5498, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0879
  Round 1/3: Mean predicted reward = 9.969
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9768, entropy=0.5452, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0648
  Round 2/3: Mean predicted reward = 9.993
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9762, entropy=0.5529, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0821
  Round 3/3: Mean predicted reward = 10.240

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 29 Results ---
  Mean Oracle Reward: 10.223
  Min Oracle Reward: 6.744
  Max Oracle Reward: 12.819
  Std Oracle Reward: 1.247
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.081, Max: 0.171, Count: 13
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
  CGAGGATCCGTA
  CGCATTGACGAG
  GGGCCACTGCTA
  GGAGCATCACTG
  GGAGCCTTGCCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.384
  Max reward: 13.900
  With intrinsic bonuses: 10.334

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9783, entropy=0.5490, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5121

=== Surrogate Model Training ===
Total samples: 1010

Training on 965 samples (removed 45 outliers)
Reward range: [7.09, 13.15], mean: 10.16
  Created 13 candidate models for data size 965
Current R2 threshold: -0.09999999999999998
  rf-tuned-l: R2 = 0.155 (std: 0.112)
  rf-tuned-xl: R2 = 0.165 (std: 0.109)
  gb-tuned-l: R2 = 0.156 (std: 0.093)
  gb-tuned-xl: R2 = 0.156 (std: 0.093)
  xgb-xl: R2 = 0.011 (std: 0.114)
  xgb-l: R2 = 0.011 (std: 0.114)
  mlp-adaptive-xl: R2 = 0.011 (std: 0.124)
  mlp-l: R2 = 0.006 (std: 0.122)
  svr-rbf-xl: R2 = 0.183 (std: 0.071)
  svr-poly-l: R2 = 0.183 (std: 0.071)
  knn-tuned-sqrt: R2 = 0.054 (std: 0.129)
  knn-tuned-l: R2 = 0.054 (std: 0.129)
  ridge: R2 = 0.038 (std: 0.060)

Model-based training with 13 models
Best R2: 0.183, Mean R2: 0.091
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9782, entropy=0.5358, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2207
  Round 1/3: Mean predicted reward = 9.708
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9763, entropy=0.5181, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3288
  Round 2/3: Mean predicted reward = 10.047
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9734, entropy=0.5266, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4218
  Round 3/3: Mean predicted reward = 10.155

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 30 Results ---
  Mean Oracle Reward: 10.280
  Min Oracle Reward: 6.321
  Max Oracle Reward: 14.069
  Std Oracle Reward: 1.476
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.091, Max: 0.183, Count: 13
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
  ACGCCGTGACGT
  GCAACGTGTCCG
  GGACCACTGGCT
  GCACACGTGGTC
  TGAAGCGCTGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.252
  Max reward: 14.040
  With intrinsic bonuses: 10.260

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9741, entropy=0.5076, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4678

=== Surrogate Model Training ===
Total samples: 1042

Training on 995 samples (removed 47 outliers)
Reward range: [7.09, 13.15], mean: 10.16
  Created 13 candidate models for data size 995
Current R2 threshold: -0.09
  rf-tuned-l: R2 = 0.167 (std: 0.127)
  rf-tuned-xl: R2 = 0.171 (std: 0.110)
  gb-tuned-l: R2 = 0.157 (std: 0.090)
  gb-tuned-xl: R2 = 0.157 (std: 0.090)
  xgb-xl: R2 = 0.022 (std: 0.116)
  xgb-l: R2 = 0.022 (std: 0.116)
  mlp-adaptive-xl: R2 = 0.032 (std: 0.135)
  mlp-l: R2 = 0.011 (std: 0.098)
  svr-rbf-xl: R2 = 0.194 (std: 0.078)
  svr-poly-l: R2 = 0.194 (std: 0.078)
  knn-tuned-sqrt: R2 = 0.063 (std: 0.118)
  knn-tuned-l: R2 = 0.063 (std: 0.118)
  ridge: R2 = 0.039 (std: 0.057)

Model-based training with 13 models
Best R2: 0.194, Mean R2: 0.099
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9758, entropy=0.5286, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2945
  Round 1/3: Mean predicted reward = 9.894
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9766, entropy=0.5058, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1247
  Round 2/3: Mean predicted reward = 10.014
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9752, entropy=0.5185, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2384
  Round 3/3: Mean predicted reward = 10.172

  === Progress Analysis ===
  Status: NORMAL

--- Round 31 Results ---
  Mean Oracle Reward: 10.238
  Min Oracle Reward: 7.017
  Max Oracle Reward: 14.051
  Std Oracle Reward: 1.352
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.099, Max: 0.194, Count: 13
  Total Sequences Evaluated: 1042

======================================================================
EXPERIMENT ROUND 32/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1042
  Performance plateaued, reducing LR to 0.000100

--- Round 32 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCCCTGATAGGG
  GCCGCGAACTGT
  TATGCCCGGAAG
  CCGGCACTTAGG
  CGCTGCTGGCAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.063
  Max reward: 12.811
  With intrinsic bonuses: 10.090

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9723, entropy=0.5187, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2233

=== Surrogate Model Training ===
Total samples: 1074

Training on 1028 samples (removed 46 outliers)
Reward range: [7.00, 13.22], mean: 10.17
  Created 13 candidate models for data size 1028
Current R2 threshold: -0.07999999999999999
  rf-tuned-l: R2 = 0.178 (std: 0.125)
  rf-tuned-xl: R2 = 0.186 (std: 0.128)
  gb-tuned-l: R2 = 0.164 (std: 0.103)
  gb-tuned-xl: R2 = 0.164 (std: 0.103)
  xgb-xl: R2 = 0.048 (std: 0.135)
  xgb-l: R2 = 0.048 (std: 0.135)
  mlp-adaptive-xl: R2 = 0.060 (std: 0.126)
  mlp-l: R2 = 0.048 (std: 0.146)
  svr-rbf-xl: R2 = 0.209 (std: 0.097)
  svr-poly-l: R2 = 0.209 (std: 0.097)
  knn-tuned-sqrt: R2 = 0.065 (std: 0.115)
  knn-tuned-l: R2 = 0.065 (std: 0.115)
  ridge: R2 = 0.040 (std: 0.063)

Model-based training with 13 models
Best R2: 0.209, Mean R2: 0.114
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9780, entropy=0.5027, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1432
  Round 1/3: Mean predicted reward = 9.558
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9765, entropy=0.4966, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1519
  Round 2/3: Mean predicted reward = 9.902
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9809, entropy=0.4914, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2992
  Round 3/3: Mean predicted reward = 10.164

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 32 Results ---
  Mean Oracle Reward: 10.035
  Min Oracle Reward: 4.154
  Max Oracle Reward: 13.017
  Std Oracle Reward: 1.875
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.114, Max: 0.209, Count: 13
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
  CGTGCGAATCGC
  GAAGTCCTGCCG
  TGGCCAGAGCTC
  GTTGCCACAGGC
  GGATTCATGCAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.340
  Max reward: 13.205
  With intrinsic bonuses: 10.293

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9717, entropy=0.5147, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3251

=== Surrogate Model Training ===
Total samples: 1106

Training on 1060 samples (removed 46 outliers)
Reward range: [7.00, 13.22], mean: 10.17
  Created 13 candidate models for data size 1060
Current R2 threshold: -0.06999999999999998
  rf-tuned-l: R2 = 0.200 (std: 0.106)
  rf-tuned-xl: R2 = 0.199 (std: 0.115)
  gb-tuned-l: R2 = 0.176 (std: 0.104)
  gb-tuned-xl: R2 = 0.176 (std: 0.104)
  xgb-xl: R2 = 0.043 (std: 0.114)
  xgb-l: R2 = 0.043 (std: 0.114)
  mlp-adaptive-xl: R2 = 0.020 (std: 0.160)
  mlp-l: R2 = 0.131 (std: 0.115)
  svr-rbf-xl: R2 = 0.220 (std: 0.080)
  svr-poly-l: R2 = 0.220 (std: 0.080)
  knn-tuned-sqrt: R2 = 0.083 (std: 0.106)
  knn-tuned-l: R2 = 0.083 (std: 0.106)
  ridge: R2 = 0.047 (std: 0.066)

Model-based training with 13 models
Best R2: 0.220, Mean R2: 0.126
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9804, entropy=0.5297, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1396
  Round 1/3: Mean predicted reward = 9.701
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9751, entropy=0.4859, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0547
  Round 2/3: Mean predicted reward = 9.914
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9730, entropy=0.5011, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1213
  Round 3/3: Mean predicted reward = 10.132

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 33 Results ---
  Mean Oracle Reward: 10.363
  Min Oracle Reward: 8.069
  Max Oracle Reward: 12.925
  Std Oracle Reward: 1.276
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.126, Max: 0.220, Count: 13
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
  CCTGGCAAGTGC
  TGAGCTCGACCG
  CGGCTTACCGGA
  GCTCCCGTGGAA
  GCCGGTGCATAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.956
  Max reward: 12.888
  With intrinsic bonuses: 10.000

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9760, entropy=0.4886, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0804

=== Surrogate Model Training ===
Total samples: 1138

Training on 1088 samples (removed 50 outliers)
Reward range: [7.09, 13.22], mean: 10.18
  Created 13 candidate models for data size 1088
Current R2 threshold: -0.06
  rf-tuned-l: R2 = 0.214 (std: 0.116)
  rf-tuned-xl: R2 = 0.220 (std: 0.110)
  gb-tuned-l: R2 = 0.196 (std: 0.096)
  gb-tuned-xl: R2 = 0.196 (std: 0.096)
  xgb-xl: R2 = 0.077 (std: 0.124)
  xgb-l: R2 = 0.077 (std: 0.124)
  mlp-adaptive-xl: R2 = 0.102 (std: 0.157)
  mlp-l: R2 = 0.122 (std: 0.150)
  svr-rbf-xl: R2 = 0.227 (std: 0.083)
  svr-poly-l: R2 = 0.227 (std: 0.083)
  knn-tuned-sqrt: R2 = 0.074 (std: 0.103)
  knn-tuned-l: R2 = 0.074 (std: 0.103)
  ridge: R2 = 0.056 (std: 0.060)

Model-based training with 13 models
Best R2: 0.227, Mean R2: 0.143
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9783, entropy=0.4872, kl_div=0.0000
    Epoch 1: policy_loss=0.0038, value_loss=0.9783, entropy=0.4868, kl_div=0.0323
  Round 1/3: Mean predicted reward = 9.706
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9771, entropy=0.4768, kl_div=0.0000
    Epoch 1: policy_loss=-0.0229, value_loss=0.9771, entropy=0.4782, kl_div=-0.0510
  Round 2/3: Mean predicted reward = 10.009
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9775, entropy=0.4813, kl_div=0.0000
    Epoch 1: policy_loss=-0.0141, value_loss=0.9775, entropy=0.4836, kl_div=-0.0779
  Round 3/3: Mean predicted reward = 9.950

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 34 Results ---
  Mean Oracle Reward: 9.942
  Min Oracle Reward: 4.728
  Max Oracle Reward: 12.601
  Std Oracle Reward: 1.626
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.143, Max: 0.227, Count: 13
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
  GTCACGAGCTGC
  GGGTCATCCAGA
  GTATGACGCCGC
  GGGCTCACACTG
  CGAGGAGTCCCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.149
  Max reward: 13.124
  With intrinsic bonuses: 10.084

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9767, entropy=0.4903, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0699

=== Surrogate Model Training ===
Total samples: 1170

Training on 1121 samples (removed 49 outliers)
Reward range: [7.00, 13.23], mean: 10.18
  Created 13 candidate models for data size 1121
Current R2 threshold: -0.04999999999999999
  rf-tuned-l: R2 = 0.216 (std: 0.145)
  rf-tuned-xl: R2 = 0.218 (std: 0.146)
  gb-tuned-l: R2 = 0.210 (std: 0.134)
  gb-tuned-xl: R2 = 0.210 (std: 0.134)
  xgb-xl: R2 = 0.092 (std: 0.147)
  xgb-l: R2 = 0.092 (std: 0.147)
  mlp-adaptive-xl: R2 = 0.122 (std: 0.156)
  mlp-l: R2 = 0.098 (std: 0.166)
  svr-rbf-xl: R2 = 0.243 (std: 0.108)
  svr-poly-l: R2 = 0.243 (std: 0.108)
  knn-tuned-sqrt: R2 = 0.105 (std: 0.138)
  knn-tuned-l: R2 = 0.105 (std: 0.138)
  ridge: R2 = 0.061 (std: 0.080)

Model-based training with 13 models
Best R2: 0.243, Mean R2: 0.155
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9792, entropy=0.4963, kl_div=0.0000
    Epoch 1: policy_loss=-0.0517, value_loss=0.9792, entropy=0.5111, kl_div=-0.2913
  Round 1/3: Mean predicted reward = 9.350
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9740, entropy=0.5029, kl_div=0.0000
    Epoch 1: policy_loss=0.0101, value_loss=0.9740, entropy=0.5151, kl_div=-0.4288
  Round 2/3: Mean predicted reward = 9.966
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9751, entropy=0.5216, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1262
  Round 3/3: Mean predicted reward = 9.885

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 35 Results ---
  Mean Oracle Reward: 10.198
  Min Oracle Reward: 5.958
  Max Oracle Reward: 13.527
  Std Oracle Reward: 1.553
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.155, Max: 0.243, Count: 13
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
  CTAGGGCCTGCA
  GCCGTATCGGAC
  GCAAGCCTCGTG
  CATGCGACCGGT
  GGTCCCGCTAAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.387
  Max reward: 12.688
  With intrinsic bonuses: 10.402

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9762, entropy=0.5352, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3168

=== Surrogate Model Training ===
Total samples: 1202

Training on 1150 samples (removed 52 outliers)
Reward range: [7.09, 13.23], mean: 10.20
  Created 13 candidate models for data size 1150
Current R2 threshold: -0.03999999999999998
  rf-tuned-l: R2 = 0.243 (std: 0.138)
  rf-tuned-xl: R2 = 0.246 (std: 0.131)
  gb-tuned-l: R2 = 0.221 (std: 0.116)
  gb-tuned-xl: R2 = 0.221 (std: 0.116)
  xgb-xl: R2 = 0.120 (std: 0.171)
  xgb-l: R2 = 0.120 (std: 0.171)
  mlp-adaptive-xl: R2 = 0.101 (std: 0.183)
  mlp-l: R2 = 0.126 (std: 0.125)
  svr-rbf-xl: R2 = 0.252 (std: 0.111)
  svr-poly-l: R2 = 0.252 (std: 0.111)
  knn-tuned-sqrt: R2 = 0.111 (std: 0.134)
  knn-tuned-l: R2 = 0.111 (std: 0.134)
  ridge: R2 = 0.072 (std: 0.077)

Model-based training with 13 models
Best R2: 0.252, Mean R2: 0.169
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9734, entropy=0.5326, kl_div=0.0000
    Epoch 1: policy_loss=-0.0498, value_loss=0.9733, entropy=0.5374, kl_div=-0.0368
  Round 1/3: Mean predicted reward = 9.848
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9752, entropy=0.5471, kl_div=0.0000
    Epoch 1: policy_loss=0.0985, value_loss=0.9752, entropy=0.5598, kl_div=-0.5613
  Round 2/3: Mean predicted reward = 9.673
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9779, entropy=0.5691, kl_div=0.0000
    Epoch 1: policy_loss=-0.0736, value_loss=0.9778, entropy=0.5714, kl_div=0.0114
  Round 3/3: Mean predicted reward = 10.289

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 36 Results ---
  Mean Oracle Reward: 10.336
  Min Oracle Reward: 6.243
  Max Oracle Reward: 12.751
  Std Oracle Reward: 1.377
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.169, Max: 0.252, Count: 13
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
  GTAGAACGTCGC
  TTGGCGCGCAAC
  GGCCTGAGCACT
  AGCGTCCCTGGA
  CGACAGGCTGTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.205
  Max reward: 12.879
  With intrinsic bonuses: 10.243

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9749, entropy=0.5660, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2131

=== Surrogate Model Training ===
Total samples: 1234

Training on 1181 samples (removed 53 outliers)
Reward range: [7.09, 13.23], mean: 10.20
  Created 13 candidate models for data size 1181
Current R2 threshold: -0.02999999999999997
  rf-tuned-l: R2 = 0.256 (std: 0.122)
  rf-tuned-xl: R2 = 0.250 (std: 0.121)
  gb-tuned-l: R2 = 0.238 (std: 0.098)
  gb-tuned-xl: R2 = 0.238 (std: 0.098)
  xgb-xl: R2 = 0.122 (std: 0.131)
  xgb-l: R2 = 0.122 (std: 0.131)
  mlp-adaptive-xl: R2 = 0.141 (std: 0.110)
  mlp-l: R2 = 0.126 (std: 0.154)
  svr-rbf-xl: R2 = 0.268 (std: 0.100)
  svr-poly-l: R2 = 0.268 (std: 0.100)
  knn-tuned-sqrt: R2 = 0.123 (std: 0.119)
  knn-tuned-l: R2 = 0.123 (std: 0.119)
  ridge: R2 = 0.082 (std: 0.071)

Model-based training with 13 models
Best R2: 0.268, Mean R2: 0.181
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9727, entropy=0.5736, kl_div=0.0000
    Epoch 1: policy_loss=-0.0678, value_loss=0.9727, entropy=0.5774, kl_div=-0.0750
  Round 1/3: Mean predicted reward = 9.933
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9750, entropy=0.5822, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0782
  Round 2/3: Mean predicted reward = 10.141
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9728, entropy=0.5965, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2303
  Round 3/3: Mean predicted reward = 10.125

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 37 Results ---
  Mean Oracle Reward: 10.271
  Min Oracle Reward: 6.591
  Max Oracle Reward: 12.666
  Std Oracle Reward: 1.349
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.181, Max: 0.268, Count: 13
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
  ACACTGGCGTGC
  TAGCGGCCTGAA
  TCGTACGGCCAG
  CGGCGGATCCAT
  CCGAGATCTGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.397
  Max reward: 14.227
  With intrinsic bonuses: 10.322

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9785, entropy=0.5804, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1537

=== Surrogate Model Training ===
Total samples: 1266

Training on 1211 samples (removed 55 outliers)
Reward range: [7.09, 13.23], mean: 10.21
  Created 13 candidate models for data size 1211
Current R2 threshold: -0.019999999999999962
  rf-tuned-l: R2 = 0.243 (std: 0.103)
  rf-tuned-xl: R2 = 0.253 (std: 0.111)
  gb-tuned-l: R2 = 0.219 (std: 0.111)
  gb-tuned-xl: R2 = 0.219 (std: 0.111)
  xgb-xl: R2 = 0.135 (std: 0.128)
  xgb-l: R2 = 0.135 (std: 0.128)
  mlp-adaptive-xl: R2 = 0.134 (std: 0.132)
  mlp-l: R2 = 0.131 (std: 0.143)
  svr-rbf-xl: R2 = 0.264 (std: 0.090)
  svr-poly-l: R2 = 0.264 (std: 0.090)
  knn-tuned-sqrt: R2 = 0.119 (std: 0.129)
  knn-tuned-l: R2 = 0.119 (std: 0.129)
  ridge: R2 = 0.079 (std: 0.067)

Model-based training with 13 models
Best R2: 0.264, Mean R2: 0.178
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9732, entropy=0.5670, kl_div=0.0000
    Epoch 1: policy_loss=-0.0022, value_loss=0.9732, entropy=0.5672, kl_div=0.0355
  Round 1/3: Mean predicted reward = 9.865
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9769, entropy=0.6046, kl_div=0.0000
    Epoch 1: policy_loss=-0.0468, value_loss=0.9769, entropy=0.6052, kl_div=-0.0285
  Round 2/3: Mean predicted reward = 10.054
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9723, entropy=0.5986, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0913
  Round 3/3: Mean predicted reward = 10.160

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 38 Results ---
  Mean Oracle Reward: 10.321
  Min Oracle Reward: 3.282
  Max Oracle Reward: 14.129
  Std Oracle Reward: 1.820
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.178, Max: 0.264, Count: 13
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
  CAGCGCGATCGT
  AGCCTTCAGGCG
  TCCGAGTCAGCG
  AGCATCGTCCGG
  AGGGCACCCGTT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.288
  Max reward: 12.563
  With intrinsic bonuses: 10.311

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9731, entropy=0.5625, kl_div=0.0000
    Epoch 1: policy_loss=-0.0077, value_loss=0.9731, entropy=0.5618, kl_div=0.0135

=== Surrogate Model Training ===
Total samples: 1298

Training on 1243 samples (removed 55 outliers)
Reward range: [7.09, 13.23], mean: 10.21
  Created 13 candidate models for data size 1243
Current R2 threshold: -0.010000000000000009
  rf-tuned-l: R2 = 0.240 (std: 0.109)
  rf-tuned-xl: R2 = 0.239 (std: 0.110)
  gb-tuned-l: R2 = 0.229 (std: 0.091)
  gb-tuned-xl: R2 = 0.229 (std: 0.091)
  xgb-xl: R2 = 0.141 (std: 0.122)
  xgb-l: R2 = 0.141 (std: 0.122)
  mlp-adaptive-xl: R2 = 0.191 (std: 0.103)
  mlp-l: R2 = 0.123 (std: 0.135)
  svr-rbf-xl: R2 = 0.261 (std: 0.083)
  svr-poly-l: R2 = 0.261 (std: 0.083)
  knn-tuned-sqrt: R2 = 0.118 (std: 0.142)
  knn-tuned-l: R2 = 0.118 (std: 0.142)
  ridge: R2 = 0.075 (std: 0.064)

Model-based training with 13 models
Best R2: 0.261, Mean R2: 0.182
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9734, entropy=0.5819, kl_div=0.0000
    Epoch 1: policy_loss=-0.0053, value_loss=0.9734, entropy=0.5818, kl_div=-0.0199
  Round 1/3: Mean predicted reward = 9.957
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9749, entropy=0.5385, kl_div=0.0000
    Epoch 1: policy_loss=-0.0039, value_loss=0.9749, entropy=0.5384, kl_div=-0.0120
  Round 2/3: Mean predicted reward = 10.008
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9758, entropy=0.5670, kl_div=0.0000
    Epoch 1: policy_loss=-0.0107, value_loss=0.9758, entropy=0.5665, kl_div=0.0111
  Round 3/3: Mean predicted reward = 10.152

  === Progress Analysis ===
  Status: NORMAL

--- Round 39 Results ---
  Mean Oracle Reward: 10.319
  Min Oracle Reward: 7.693
  Max Oracle Reward: 12.374
  Std Oracle Reward: 1.125
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.182, Max: 0.261, Count: 13
  Total Sequences Evaluated: 1298

======================================================================
EXPERIMENT ROUND 40/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1298
  Performance plateaued, reducing LR to 0.000150

--- Round 40 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TAGATCCCGCGG
  ACGAGGTGTCCC
  AGCGGTCCGACT
  GCGTACCAGGCT
  AGAGCCAGTTCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.089
  Max reward: 11.958
  With intrinsic bonuses: 10.091

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9730, entropy=0.5629, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2866

=== Surrogate Model Training ===
Total samples: 1330

Training on 1273 samples (removed 57 outliers)
Reward range: [7.09, 13.23], mean: 10.21
  Created 13 candidate models for data size 1273
Current R2 threshold: 0.0
  rf-tuned-l: R2 = 0.241 (std: 0.102)
  rf-tuned-xl: R2 = 0.236 (std: 0.102)
  gb-tuned-l: R2 = 0.227 (std: 0.092)
  gb-tuned-xl: R2 = 0.227 (std: 0.092)
  xgb-xl: R2 = 0.114 (std: 0.095)
  xgb-l: R2 = 0.114 (std: 0.095)
  mlp-adaptive-xl: R2 = 0.170 (std: 0.103)
  mlp-l: R2 = 0.173 (std: 0.101)
  svr-rbf-xl: R2 = 0.253 (std: 0.085)
  svr-poly-l: R2 = 0.253 (std: 0.085)
  knn-tuned-sqrt: R2 = 0.108 (std: 0.136)
  knn-tuned-l: R2 = 0.108 (std: 0.136)
  ridge: R2 = 0.067 (std: 0.066)

Model-based training with 13 models
Best R2: 0.253, Mean R2: 0.176
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9724, entropy=0.5659, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2713
  Round 1/3: Mean predicted reward = 9.973
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9748, entropy=0.5702, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2468
  Round 2/3: Mean predicted reward = 10.062
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9752, entropy=0.5523, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4211
  Round 3/3: Mean predicted reward = 10.145

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 40 Results ---
  Mean Oracle Reward: 10.107
  Min Oracle Reward: 6.704
  Max Oracle Reward: 11.865
  Std Oracle Reward: 1.345
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.176, Max: 0.253, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  CGGTCTCCAGAG
  ATGGACCCTGGC
  AAGGCTCCGGTC
  CCGTGTCCGGAA
  CACGGCTTGCGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.454
  Max reward: 13.066
  With intrinsic bonuses: 10.459

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9726, entropy=0.5372, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8828

=== Surrogate Model Training ===
Total samples: 1362

Training on 1301 samples (removed 61 outliers)
Reward range: [7.10, 13.15], mean: 10.22
  Created 13 candidate models for data size 1301
Current R2 threshold: 0.010000000000000009
  rf-tuned-l: R2 = 0.255 (std: 0.087)
  rf-tuned-xl: R2 = 0.250 (std: 0.094)
  gb-tuned-l: R2 = 0.243 (std: 0.098)
  gb-tuned-xl: R2 = 0.243 (std: 0.098)
  xgb-xl: R2 = 0.140 (std: 0.097)
  xgb-l: R2 = 0.140 (std: 0.097)
  mlp-adaptive-xl: R2 = 0.147 (std: 0.100)
  mlp-l: R2 = 0.186 (std: 0.116)
  svr-rbf-xl: R2 = 0.276 (std: 0.086)
  svr-poly-l: R2 = 0.276 (std: 0.086)
  knn-tuned-sqrt: R2 = 0.132 (std: 0.139)
  knn-tuned-l: R2 = 0.132 (std: 0.139)
  ridge: R2 = 0.079 (std: 0.071)

Model-based training with 13 models
Best R2: 0.276, Mean R2: 0.192
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9764, entropy=0.5126, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6762
  Round 1/3: Mean predicted reward = 9.742
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9756, entropy=0.5322, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5843
  Round 2/3: Mean predicted reward = 9.767
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9721, entropy=0.5177, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7215
  Round 3/3: Mean predicted reward = 10.135

  === Progress Analysis ===
  Status: NORMAL

--- Round 41 Results ---
  Mean Oracle Reward: 10.446
  Min Oracle Reward: 7.629
  Max Oracle Reward: 13.102
  Std Oracle Reward: 1.236
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.192, Max: 0.276, Count: 13
  New best mean reward!
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
  GGATCGTGCCCA
  GGGTCGTCACCA
  CCAGGTAGCCTG
  AGGTCCAGGTCC
  CGCCGGCTAGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.314
  Max reward: 12.119
  With intrinsic bonuses: 10.351

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9757, entropy=0.5065, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7555

=== Surrogate Model Training ===
Total samples: 1394

Training on 1331 samples (removed 63 outliers)
Reward range: [7.21, 13.15], mean: 10.23
  Created 13 candidate models for data size 1331
Current R2 threshold: 0.020000000000000018
  rf-tuned-l: R2 = 0.257 (std: 0.107)
  rf-tuned-xl: R2 = 0.249 (std: 0.102)
  gb-tuned-l: R2 = 0.244 (std: 0.087)
  gb-tuned-xl: R2 = 0.244 (std: 0.087)
  xgb-xl: R2 = 0.146 (std: 0.104)
  xgb-l: R2 = 0.146 (std: 0.104)
  mlp-adaptive-xl: R2 = 0.206 (std: 0.120)
  mlp-l: R2 = 0.177 (std: 0.101)
  svr-rbf-xl: R2 = 0.276 (std: 0.088)
  svr-poly-l: R2 = 0.276 (std: 0.088)
  knn-tuned-sqrt: R2 = 0.139 (std: 0.142)
  knn-tuned-l: R2 = 0.139 (std: 0.142)
  ridge: R2 = 0.082 (std: 0.065)

Model-based training with 13 models
Best R2: 0.276, Mean R2: 0.198
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9734, entropy=0.4950, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4394
  Round 1/3: Mean predicted reward = 9.931
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9738, entropy=0.4858, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2676
  Round 2/3: Mean predicted reward = 10.049
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9733, entropy=0.4808, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4530
  Round 3/3: Mean predicted reward = 10.261

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 42 Results ---
  Mean Oracle Reward: 10.311
  Min Oracle Reward: 7.083
  Max Oracle Reward: 12.023
  Std Oracle Reward: 1.151
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.198, Max: 0.276, Count: 13
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
  GACCTGGCACGT
  CAGACCGTGGTC
  AGGTGTCCACCG
  ACGGCTGACTCG
  TGGCACTGGCCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.316
  Max reward: 12.694
  With intrinsic bonuses: 10.341

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9737, entropy=0.4670, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3454

=== Surrogate Model Training ===
Total samples: 1426

Training on 1363 samples (removed 63 outliers)
Reward range: [7.21, 13.22], mean: 10.23
  Created 13 candidate models for data size 1363
Current R2 threshold: 0.030000000000000027
  rf-tuned-l: R2 = 0.257 (std: 0.095)
  rf-tuned-xl: R2 = 0.253 (std: 0.100)
  gb-tuned-l: R2 = 0.243 (std: 0.093)
  gb-tuned-xl: R2 = 0.243 (std: 0.093)
  xgb-xl: R2 = 0.120 (std: 0.106)
  xgb-l: R2 = 0.120 (std: 0.106)
  mlp-adaptive-xl: R2 = 0.214 (std: 0.090)
  mlp-l: R2 = 0.189 (std: 0.120)
  svr-rbf-xl: R2 = 0.276 (std: 0.088)
  svr-poly-l: R2 = 0.276 (std: 0.088)
  knn-tuned-sqrt: R2 = 0.127 (std: 0.121)
  knn-tuned-l: R2 = 0.127 (std: 0.121)
  ridge: R2 = 0.081 (std: 0.068)

Model-based training with 13 models
Best R2: 0.276, Mean R2: 0.194
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9751, entropy=0.4559, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1763
  Round 1/3: Mean predicted reward = 9.672
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9726, entropy=0.4763, kl_div=0.0000
    Epoch 1: policy_loss=-0.0328, value_loss=0.9726, entropy=0.4764, kl_div=0.0053
  Round 2/3: Mean predicted reward = 10.050
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9739, entropy=0.4770, kl_div=0.0000
    Epoch 1: policy_loss=-0.0220, value_loss=0.9739, entropy=0.4772, kl_div=-0.0125
  Round 3/3: Mean predicted reward = 10.133

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 43 Results ---
  Mean Oracle Reward: 10.356
  Min Oracle Reward: 5.981
  Max Oracle Reward: 12.769
  Std Oracle Reward: 1.280
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.194, Max: 0.276, Count: 13
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
  TCCGGGCCTAAG
  AAGGCTTGGCCC
  CGTTCCGGCAGA
  TGGGATCACCCG
  ACGAGTTCCGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.343
  Max reward: 13.356
  With intrinsic bonuses: 10.360

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9754, entropy=0.4599, kl_div=0.0000
    Epoch 1: policy_loss=-0.0232, value_loss=0.9754, entropy=0.4594, kl_div=0.0447

=== Surrogate Model Training ===
Total samples: 1458

Training on 1394 samples (removed 64 outliers)
Reward range: [7.21, 13.22], mean: 10.23
  Created 13 candidate models for data size 1394
Current R2 threshold: 0.040000000000000036
  rf-tuned-l: R2 = 0.252 (std: 0.108)
  rf-tuned-xl: R2 = 0.252 (std: 0.104)
  gb-tuned-l: R2 = 0.242 (std: 0.094)
  gb-tuned-xl: R2 = 0.242 (std: 0.094)
  xgb-xl: R2 = 0.149 (std: 0.098)
  xgb-l: R2 = 0.149 (std: 0.098)
  mlp-adaptive-xl: R2 = 0.175 (std: 0.121)
  mlp-l: R2 = 0.216 (std: 0.093)
  svr-rbf-xl: R2 = 0.287 (std: 0.086)
  svr-poly-l: R2 = 0.287 (std: 0.086)
  knn-tuned-sqrt: R2 = 0.126 (std: 0.139)
  knn-tuned-l: R2 = 0.126 (std: 0.139)
  ridge: R2 = 0.088 (std: 0.074)

Model-based training with 13 models
Best R2: 0.287, Mean R2: 0.199
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9730, entropy=0.4746, kl_div=0.0000
    Epoch 1: policy_loss=-0.0004, value_loss=0.9730, entropy=0.4743, kl_div=0.0316
  Round 1/3: Mean predicted reward = 9.966
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9773, entropy=0.4695, kl_div=0.0000
    Epoch 1: policy_loss=-0.0104, value_loss=0.9773, entropy=0.4698, kl_div=-0.0184
  Round 2/3: Mean predicted reward = 10.048
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9738, entropy=0.4767, kl_div=0.0000
    Epoch 1: policy_loss=-0.0019, value_loss=0.9737, entropy=0.4769, kl_div=-0.0099
  Round 3/3: Mean predicted reward = 10.272

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 44 Results ---
  Mean Oracle Reward: 10.344
  Min Oracle Reward: 8.696
  Max Oracle Reward: 13.202
  Std Oracle Reward: 1.055
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.199, Max: 0.287, Count: 13
  Total Sequences Evaluated: 1458

======================================================================
EXPERIMENT ROUND 45/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1458
  Performance plateaued, reducing LR to 0.000150

--- Round 45 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCCGATATCGCG
  GCGTGCGTAACC
  GGGGCCTCTACA
  GCCTAGGCTAGC
  GGGCTCCTGACA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.884
  Max reward: 13.284
  With intrinsic bonuses: 10.895

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9704, entropy=0.4782, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2197

=== Surrogate Model Training ===
Total samples: 1490

Training on 1425 samples (removed 65 outliers)
Reward range: [7.21, 13.15], mean: 10.25
  Created 13 candidate models for data size 1425
Current R2 threshold: 0.050000000000000044
  rf-tuned-l: R2 = 0.254 (std: 0.100)
  rf-tuned-xl: R2 = 0.258 (std: 0.091)
  gb-tuned-l: R2 = 0.247 (std: 0.083)
  gb-tuned-xl: R2 = 0.247 (std: 0.083)
  xgb-xl: R2 = 0.137 (std: 0.137)
  xgb-l: R2 = 0.137 (std: 0.137)
  mlp-adaptive-xl: R2 = 0.186 (std: 0.092)
  mlp-l: R2 = 0.196 (std: 0.095)
  svr-rbf-xl: R2 = 0.292 (std: 0.078)
  svr-poly-l: R2 = 0.292 (std: 0.078)
  knn-tuned-sqrt: R2 = 0.136 (std: 0.125)
  knn-tuned-l: R2 = 0.136 (std: 0.125)
  ridge: R2 = 0.084 (std: 0.066)

Model-based training with 13 models
Best R2: 0.292, Mean R2: 0.200
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9756, entropy=0.4838, kl_div=0.0000
    Epoch 1: policy_loss=-0.0205, value_loss=0.9756, entropy=0.4837, kl_div=0.0341
  Round 1/3: Mean predicted reward = 9.795
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9748, entropy=0.4473, kl_div=0.0000
    Epoch 1: policy_loss=-0.0549, value_loss=0.9747, entropy=0.4487, kl_div=-0.1173
  Round 2/3: Mean predicted reward = 9.941
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9765, entropy=0.4521, kl_div=0.0000
    Epoch 1: policy_loss=-0.0464, value_loss=0.9764, entropy=0.4525, kl_div=-0.0564
  Round 3/3: Mean predicted reward = 10.128

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 45 Results ---
  Mean Oracle Reward: 10.880
  Min Oracle Reward: 8.474
  Max Oracle Reward: 13.183
  Std Oracle Reward: 1.168
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.200, Max: 0.292, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 1490

======================================================================
EXPERIMENT ROUND 46/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1490
  Consistent improvement, increasing LR to 0.000327

--- Round 46 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGAATCGTCGCC
  TGGACCGACGTC
  CGTAGTCAGCCG
  CACTAGCGCGTG
  CCACTCGGATGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.090
  Max reward: 13.191
  With intrinsic bonuses: 10.030

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9751, entropy=0.4705, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2128

=== Surrogate Model Training ===
Total samples: 1522

Training on 1453 samples (removed 69 outliers)
Reward range: [7.21, 13.15], mean: 10.25
  Created 13 candidate models for data size 1453
Current R2 threshold: 0.06
  rf-tuned-l: R2 = 0.260 (std: 0.107)
  rf-tuned-xl: R2 = 0.250 (std: 0.097)
  gb-tuned-l: R2 = 0.250 (std: 0.089)
  gb-tuned-xl: R2 = 0.250 (std: 0.089)
  xgb-xl: R2 = 0.157 (std: 0.076)
  xgb-l: R2 = 0.157 (std: 0.076)
  mlp-adaptive-xl: R2 = 0.213 (std: 0.076)
  mlp-l: R2 = 0.180 (std: 0.097)
  svr-rbf-xl: R2 = 0.286 (std: 0.076)
  svr-poly-l: R2 = 0.286 (std: 0.076)
  knn-tuned-sqrt: R2 = 0.132 (std: 0.113)
  knn-tuned-l: R2 = 0.132 (std: 0.113)
  ridge: R2 = 0.082 (std: 0.068)

Model-based training with 13 models
Best R2: 0.286, Mean R2: 0.203
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9761, entropy=0.4471, kl_div=0.0000
    Epoch 1: policy_loss=-0.0732, value_loss=0.9761, entropy=0.4516, kl_div=-0.2203
  Round 1/3: Mean predicted reward = 9.850
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9716, entropy=0.4900, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0982
  Round 2/3: Mean predicted reward = 9.989
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9713, entropy=0.4651, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3011
  Round 3/3: Mean predicted reward = 9.981

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 46 Results ---
  Mean Oracle Reward: 10.053
  Min Oracle Reward: 5.614
  Max Oracle Reward: 13.365
  Std Oracle Reward: 1.551
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.203, Max: 0.286, Count: 13
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
  TGCAAGCGGCCT
  GCGTGAACCCGT
  CTAGGAGACGCT
  GACCGGATTGCC
  CGCCAGTTGCGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.956
  Max reward: 13.221
  With intrinsic bonuses: 9.946

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9780, entropy=0.4717, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4757

=== Surrogate Model Training ===
Total samples: 1554

Training on 1482 samples (removed 72 outliers)
Reward range: [7.21, 13.15], mean: 10.25
  Created 13 candidate models for data size 1482
Current R2 threshold: 0.07
  rf-tuned-l: R2 = 0.259 (std: 0.103)
  rf-tuned-xl: R2 = 0.261 (std: 0.100)
  gb-tuned-l: R2 = 0.264 (std: 0.089)
  gb-tuned-xl: R2 = 0.264 (std: 0.089)
  xgb-xl: R2 = 0.150 (std: 0.091)
  xgb-l: R2 = 0.150 (std: 0.091)
  mlp-adaptive-xl: R2 = 0.175 (std: 0.121)
  mlp-l: R2 = 0.177 (std: 0.105)
  svr-rbf-xl: R2 = 0.287 (std: 0.080)
  svr-poly-l: R2 = 0.287 (std: 0.080)
  knn-tuned-sqrt: R2 = 0.137 (std: 0.114)
  knn-tuned-l: R2 = 0.137 (std: 0.114)
  ridge: R2 = 0.091 (std: 0.069)

Model-based training with 13 models
Best R2: 0.287, Mean R2: 0.203
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9764, entropy=0.4157, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1253
  Round 1/3: Mean predicted reward = 9.615
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9721, entropy=0.4786, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1205
  Round 2/3: Mean predicted reward = 10.002
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9735, entropy=0.4549, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2309
  Round 3/3: Mean predicted reward = 10.173

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 47 Results ---
  Mean Oracle Reward: 9.994
  Min Oracle Reward: 3.112
  Max Oracle Reward: 13.101
  Std Oracle Reward: 1.802
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.203, Max: 0.287, Count: 13
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
  AGACGCGTCGCT
  CACGGCAGTTGC
  ACACTTCCGGGG
  GCACGTGCTGCA
  GCTTGGAGCCCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.285
  Max reward: 12.807
  With intrinsic bonuses: 10.172

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9721, entropy=0.4778, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2091

=== Surrogate Model Training ===
Total samples: 1586

Training on 1513 samples (removed 73 outliers)
Reward range: [7.20, 13.15], mean: 10.25
  Created 13 candidate models for data size 1513
Current R2 threshold: 0.08000000000000002
  rf-tuned-l: R2 = 0.259 (std: 0.091)
  rf-tuned-xl: R2 = 0.254 (std: 0.093)
  gb-tuned-l: R2 = 0.270 (std: 0.076)
  gb-tuned-xl: R2 = 0.270 (std: 0.076)
  xgb-xl: R2 = 0.166 (std: 0.105)
  xgb-l: R2 = 0.166 (std: 0.105)
  mlp-adaptive-xl: R2 = 0.194 (std: 0.084)
  mlp-l: R2 = 0.196 (std: 0.108)
  svr-rbf-xl: R2 = 0.290 (std: 0.070)
  svr-poly-l: R2 = 0.290 (std: 0.070)
  knn-tuned-sqrt: R2 = 0.135 (std: 0.111)
  knn-tuned-l: R2 = 0.135 (std: 0.111)
  ridge: R2 = 0.098 (std: 0.061)

Model-based training with 13 models
Best R2: 0.290, Mean R2: 0.210
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9733, entropy=0.4451, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1675
  Round 1/3: Mean predicted reward = 9.981
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9718, entropy=0.4462, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2362
  Round 2/3: Mean predicted reward = 9.992
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9737, entropy=0.4465, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4156
  Round 3/3: Mean predicted reward = 10.243

  === Progress Analysis ===
  Status: NORMAL

--- Round 48 Results ---
  Mean Oracle Reward: 10.220
  Min Oracle Reward: 4.856
  Max Oracle Reward: 12.849
  Std Oracle Reward: 1.747
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.210, Max: 0.290, Count: 13
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
  CGCAGCTTGACG
  AGGGAACTCTGC
  GCACGACTGGTC
  CGCGTAGGATCC
  TTGCCGAGAGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.649
  Max reward: 15.082
  With intrinsic bonuses: 10.684

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9746, entropy=0.4491, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1431

=== Surrogate Model Training ===
Total samples: 1618

Training on 1542 samples (removed 76 outliers)
Reward range: [7.19, 13.15], mean: 10.25
  Created 13 candidate models for data size 1542
Current R2 threshold: 0.09000000000000002
  rf-tuned-l: R2 = 0.260 (std: 0.098)
  rf-tuned-xl: R2 = 0.252 (std: 0.092)
  gb-tuned-l: R2 = 0.263 (std: 0.071)
  gb-tuned-xl: R2 = 0.263 (std: 0.071)
  xgb-xl: R2 = 0.167 (std: 0.119)
  xgb-l: R2 = 0.167 (std: 0.119)
  mlp-adaptive-xl: R2 = 0.215 (std: 0.089)
  mlp-l: R2 = 0.205 (std: 0.096)
  svr-rbf-xl: R2 = 0.285 (std: 0.074)
  svr-poly-l: R2 = 0.285 (std: 0.074)
  knn-tuned-sqrt: R2 = 0.143 (std: 0.115)
  knn-tuned-l: R2 = 0.143 (std: 0.115)
  ridge: R2 = 0.094 (std: 0.063)

Model-based training with 13 models
Best R2: 0.285, Mean R2: 0.211
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9738, entropy=0.4399, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0658
  Round 1/3: Mean predicted reward = 9.775
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9712, entropy=0.4336, kl_div=0.0000
    Epoch 1: policy_loss=-0.0186, value_loss=0.9712, entropy=0.4324, kl_div=0.0496
  Round 2/3: Mean predicted reward = 9.864
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9746, entropy=0.4341, kl_div=0.0000
    Epoch 1: policy_loss=-0.0141, value_loss=0.9745, entropy=0.4338, kl_div=0.0181
  Round 3/3: Mean predicted reward = 10.065

  === Progress Analysis ===
  Status: NORMAL

--- Round 49 Results ---
  Mean Oracle Reward: 10.641
  Min Oracle Reward: 7.245
  Max Oracle Reward: 15.045
  Std Oracle Reward: 1.507
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.211, Max: 0.285, Count: 13
  Total Sequences Evaluated: 1618

======================================================================
EXPERIMENT ROUND 50/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1618
  Consistent improvement, increasing LR to 0.000360

--- Round 50 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AGGTAGCTGCCC
  CTCGAGGTCACG
  TCCCGCGAGATG
  AGATTCGACCGG
  ACGCGCGCAGTT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.429
  Max reward: 12.789
  With intrinsic bonuses: 10.443

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9730, entropy=0.4506, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5808

=== Surrogate Model Training ===
Total samples: 1650

Training on 1574 samples (removed 76 outliers)
Reward range: [7.19, 13.15], mean: 10.26
  Created 13 candidate models for data size 1574
Current R2 threshold: 0.10000000000000003
  rf-tuned-l: R2 = 0.258 (std: 0.092)
  rf-tuned-xl: R2 = 0.254 (std: 0.087)
  gb-tuned-l: R2 = 0.257 (std: 0.073)
  gb-tuned-xl: R2 = 0.257 (std: 0.073)
  xgb-xl: R2 = 0.171 (std: 0.105)
  xgb-l: R2 = 0.171 (std: 0.105)
  mlp-adaptive-xl: R2 = 0.241 (std: 0.076)
  mlp-l: R2 = 0.209 (std: 0.082)
  svr-rbf-xl: R2 = 0.293 (std: 0.078)
  svr-poly-l: R2 = 0.293 (std: 0.078)
  knn-tuned-sqrt: R2 = 0.147 (std: 0.111)
  knn-tuned-l: R2 = 0.147 (std: 0.111)
  ridge: R2 = 0.098 (std: 0.065)

Model-based training with 12 models
Best R2: 0.293, Mean R2: 0.215
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9734, entropy=0.3981, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2672
  Round 1/3: Mean predicted reward = 9.811
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9731, entropy=0.4360, kl_div=0.0000
    Epoch 1: policy_loss=-0.0084, value_loss=0.9730, entropy=0.4437, kl_div=-0.3481
  Round 2/3: Mean predicted reward = 9.987
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9720, entropy=0.4108, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6015
  Round 3/3: Mean predicted reward = 10.187

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 50 Results ---
  Mean Oracle Reward: 10.428
  Min Oracle Reward: 8.735
  Max Oracle Reward: 12.661
  Std Oracle Reward: 0.966
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.215, Max: 0.293, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  CATGGTCACCGG
  TCTGGCGACCGA
  GCGACAGCTCGT
  GTGTAACGGCCC
  GGGCACGCTTCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.608
  Max reward: 12.838
  With intrinsic bonuses: 10.628

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9734, entropy=0.4357, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4666

=== Surrogate Model Training ===
Total samples: 1682

Training on 1603 samples (removed 79 outliers)
Reward range: [7.23, 13.15], mean: 10.27
  Created 13 candidate models for data size 1603
Current R2 threshold: 0.11000000000000004
  rf-tuned-l: R2 = 0.241 (std: 0.097)
  rf-tuned-xl: R2 = 0.253 (std: 0.090)
  gb-tuned-l: R2 = 0.256 (std: 0.064)
  gb-tuned-xl: R2 = 0.256 (std: 0.064)
  xgb-xl: R2 = 0.163 (std: 0.118)
  xgb-l: R2 = 0.163 (std: 0.118)
  mlp-adaptive-xl: R2 = 0.217 (std: 0.085)
  mlp-l: R2 = 0.203 (std: 0.079)
  svr-rbf-xl: R2 = 0.290 (std: 0.072)
  svr-poly-l: R2 = 0.290 (std: 0.072)
  knn-tuned-sqrt: R2 = 0.138 (std: 0.107)
  knn-tuned-l: R2 = 0.138 (std: 0.107)
  ridge: R2 = 0.098 (std: 0.065)

Model-based training with 12 models
Best R2: 0.290, Mean R2: 0.208
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9722, entropy=0.4363, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1356
  Round 1/3: Mean predicted reward = 9.940
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9755, entropy=0.3950, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3124
  Round 2/3: Mean predicted reward = 10.158
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9737, entropy=0.4006, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6904
  Round 3/3: Mean predicted reward = 10.212

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 51 Results ---
  Mean Oracle Reward: 10.628
  Min Oracle Reward: 8.942
  Max Oracle Reward: 12.795
  Std Oracle Reward: 0.937
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.208, Max: 0.290, Count: 13
  Total Sequences Evaluated: 1682

======================================================================
EXPERIMENT ROUND 52/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1682
  Performance plateaued, reducing LR to 0.000100

--- Round 52 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTGTCAACCCGG
  TAAGGCCGTGCC
  GACATGGATCGC
  TCGCCGCTAAGG
  GTGCAATCGGAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.257
  Max reward: 12.227
  With intrinsic bonuses: 10.250

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.4037, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2601

=== Surrogate Model Training ===
Total samples: 1714

Training on 1633 samples (removed 81 outliers)
Reward range: [7.28, 13.15], mean: 10.27
  Created 13 candidate models for data size 1633
Current R2 threshold: 0.12
  rf-tuned-l: R2 = 0.247 (std: 0.100)
  rf-tuned-xl: R2 = 0.241 (std: 0.098)
  gb-tuned-l: R2 = 0.252 (std: 0.068)
  gb-tuned-xl: R2 = 0.252 (std: 0.068)
  xgb-xl: R2 = 0.173 (std: 0.113)
  xgb-l: R2 = 0.173 (std: 0.113)
  mlp-adaptive-xl: R2 = 0.213 (std: 0.079)
  mlp-l: R2 = 0.194 (std: 0.114)
  svr-rbf-xl: R2 = 0.291 (std: 0.075)
  svr-poly-l: R2 = 0.291 (std: 0.075)
  knn-tuned-sqrt: R2 = 0.139 (std: 0.119)
  knn-tuned-l: R2 = 0.139 (std: 0.119)
  ridge: R2 = 0.096 (std: 0.066)

Model-based training with 12 models
Best R2: 0.291, Mean R2: 0.208
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9738, entropy=0.3664, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1195
  Round 1/3: Mean predicted reward = 9.919
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9742, entropy=0.3924, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1906
  Round 2/3: Mean predicted reward = 10.017
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9754, entropy=0.3810, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2077
  Round 3/3: Mean predicted reward = 10.150

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 52 Results ---
  Mean Oracle Reward: 10.243
  Min Oracle Reward: 7.198
  Max Oracle Reward: 12.150
  Std Oracle Reward: 1.108
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.208, Max: 0.291, Count: 13
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
  CACCCTGGGTAG
  CGGGCCCTAGAT
  TGAGCGCCGCAT
  GGAGCGATATCC
  CGGTGGCTACCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.305
  Max reward: 13.546
  With intrinsic bonuses: 10.281

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9737, entropy=0.3859, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3617

=== Surrogate Model Training ===
Total samples: 1746

Training on 1663 samples (removed 83 outliers)
Reward range: [7.28, 13.15], mean: 10.27
  Created 13 candidate models for data size 1663
Current R2 threshold: 0.13
  rf-tuned-l: R2 = 0.248 (std: 0.087)
  rf-tuned-xl: R2 = 0.255 (std: 0.088)
  gb-tuned-l: R2 = 0.253 (std: 0.060)
  gb-tuned-xl: R2 = 0.253 (std: 0.060)
  xgb-xl: R2 = 0.180 (std: 0.100)
  xgb-l: R2 = 0.180 (std: 0.100)
  mlp-adaptive-xl: R2 = 0.208 (std: 0.062)
  mlp-l: R2 = 0.217 (std: 0.063)
  svr-rbf-xl: R2 = 0.292 (std: 0.067)
  svr-poly-l: R2 = 0.292 (std: 0.067)
  knn-tuned-sqrt: R2 = 0.141 (std: 0.095)
  knn-tuned-l: R2 = 0.141 (std: 0.095)
  ridge: R2 = 0.096 (std: 0.066)

Model-based training with 12 models
Best R2: 0.292, Mean R2: 0.212
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9745, entropy=0.4115, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1745
  Round 1/3: Mean predicted reward = 9.998
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9725, entropy=0.4407, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0572
  Round 2/3: Mean predicted reward = 9.948
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9721, entropy=0.4178, kl_div=0.0000
    Epoch 1: policy_loss=-0.0250, value_loss=0.9721, entropy=0.4192, kl_div=-0.0856
  Round 3/3: Mean predicted reward = 10.174

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 53 Results ---
  Mean Oracle Reward: 10.281
  Min Oracle Reward: 3.024
  Max Oracle Reward: 13.495
  Std Oracle Reward: 1.755
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.212, Max: 0.292, Count: 13
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
  GCTCGTAGCACG
  ATCACGGCCTGG
  CGTGCAGCAGTC
  CCAGTACGTCGG
  CTCTCGAAGCGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.603
  Max reward: 12.378
  With intrinsic bonuses: 10.633

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9718, entropy=0.3638, kl_div=0.0000
    Epoch 1: policy_loss=-0.0238, value_loss=0.9718, entropy=0.3636, kl_div=0.0248

=== Surrogate Model Training ===
Total samples: 1778

Training on 1697 samples (removed 81 outliers)
Reward range: [7.28, 13.23], mean: 10.29
  Created 13 candidate models for data size 1697
Current R2 threshold: 0.14
  rf-tuned-l: R2 = 0.276 (std: 0.099)
  rf-tuned-xl: R2 = 0.278 (std: 0.098)
  gb-tuned-l: R2 = 0.255 (std: 0.065)
  gb-tuned-xl: R2 = 0.255 (std: 0.065)
  xgb-xl: R2 = 0.206 (std: 0.110)
  xgb-l: R2 = 0.206 (std: 0.110)
  mlp-adaptive-xl: R2 = 0.206 (std: 0.103)
  mlp-l: R2 = 0.214 (std: 0.092)
  svr-rbf-xl: R2 = 0.303 (std: 0.076)
  svr-poly-l: R2 = 0.303 (std: 0.076)
  knn-tuned-sqrt: R2 = 0.180 (std: 0.123)
  knn-tuned-l: R2 = 0.180 (std: 0.123)
  ridge: R2 = 0.096 (std: 0.063)

Model-based training with 12 models
Best R2: 0.303, Mean R2: 0.227
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9713, entropy=0.3924, kl_div=0.0000
    Epoch 1: policy_loss=-0.0158, value_loss=0.9713, entropy=0.3927, kl_div=-0.0215
  Round 1/5: Mean predicted reward = 9.871
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9734, entropy=0.3682, kl_div=0.0000
    Epoch 1: policy_loss=-0.0080, value_loss=0.9734, entropy=0.3699, kl_div=-0.1229
  Round 2/5: Mean predicted reward = 10.050
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9760, entropy=0.3945, kl_div=0.0000
    Epoch 1: policy_loss=-0.0204, value_loss=0.9760, entropy=0.3949, kl_div=-0.0135
  Round 3/5: Mean predicted reward = 10.158
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9734, entropy=0.3535, kl_div=0.0000
    Epoch 1: policy_loss=-0.0233, value_loss=0.9734, entropy=0.3542, kl_div=-0.0266
  Round 4/5: Mean predicted reward = 10.236
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9727, entropy=0.4157, kl_div=0.0000
    Epoch 1: policy_loss=-0.0394, value_loss=0.9727, entropy=0.4160, kl_div=-0.0151
  Round 5/5: Mean predicted reward = 10.331

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 54 Results ---
  Mean Oracle Reward: 10.677
  Min Oracle Reward: 6.650
  Max Oracle Reward: 12.254
  Std Oracle Reward: 1.190
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.227, Max: 0.303, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  CACGGAGTGTCC
  GGCCAGTTCGCA
  AGAGCGTCTGCA
  AGATGCGGCTCC
  CCAGTGCTAGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.688
  Max reward: 12.326
  With intrinsic bonuses: 10.685

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9789, entropy=0.4463, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2806

=== Surrogate Model Training ===
Total samples: 1810

Training on 1729 samples (removed 81 outliers)
Reward range: [7.23, 13.23], mean: 10.30
  Created 13 candidate models for data size 1729
Current R2 threshold: 0.15000000000000002
  rf-tuned-l: R2 = 0.261 (std: 0.090)
  rf-tuned-xl: R2 = 0.256 (std: 0.088)
  gb-tuned-l: R2 = 0.252 (std: 0.055)
  gb-tuned-xl: R2 = 0.252 (std: 0.055)
  xgb-xl: R2 = 0.198 (std: 0.099)
  xgb-l: R2 = 0.198 (std: 0.099)
  mlp-adaptive-xl: R2 = 0.209 (std: 0.074)
  mlp-l: R2 = 0.204 (std: 0.064)
  svr-rbf-xl: R2 = 0.295 (std: 0.064)
  svr-poly-l: R2 = 0.295 (std: 0.064)
  knn-tuned-sqrt: R2 = 0.166 (std: 0.114)
  knn-tuned-l: R2 = 0.166 (std: 0.114)
  ridge: R2 = 0.091 (std: 0.055)

Model-based training with 12 models
Best R2: 0.295, Mean R2: 0.219
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9724, entropy=0.4300, kl_div=0.0000
    Epoch 1: policy_loss=0.0520, value_loss=0.9723, entropy=0.4356, kl_div=-0.2775
  Round 1/3: Mean predicted reward = 10.018
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9718, entropy=0.4146, kl_div=0.0000
    Epoch 1: policy_loss=-0.0357, value_loss=0.9717, entropy=0.4174, kl_div=-0.0677
  Round 2/3: Mean predicted reward = 10.000
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9760, entropy=0.3933, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7774
  Round 3/3: Mean predicted reward = 10.204

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 55 Results ---
  Mean Oracle Reward: 10.670
  Min Oracle Reward: 6.604
  Max Oracle Reward: 12.423
  Std Oracle Reward: 1.276
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.219, Max: 0.295, Count: 13
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
  ATCTCCGAGGGC
  GCCTTCGAAGGC
  CGCTCAGTACGG
  CATCGGCGGTAC
  CCATCGGCGGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.258
  Max reward: 11.771
  With intrinsic bonuses: 10.266

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9724, entropy=0.3634, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1113

=== Surrogate Model Training ===
Total samples: 1842

Training on 1761 samples (removed 81 outliers)
Reward range: [7.23, 13.23], mean: 10.30
  Created 13 candidate models for data size 1761
Current R2 threshold: 0.16000000000000003
  rf-tuned-l: R2 = 0.273 (std: 0.083)
  rf-tuned-xl: R2 = 0.267 (std: 0.084)
  gb-tuned-l: R2 = 0.245 (std: 0.062)
  gb-tuned-xl: R2 = 0.245 (std: 0.062)
  xgb-xl: R2 = 0.212 (std: 0.083)
  xgb-l: R2 = 0.212 (std: 0.083)
  mlp-adaptive-xl: R2 = 0.215 (std: 0.066)
  mlp-l: R2 = 0.227 (std: 0.084)
  svr-rbf-xl: R2 = 0.298 (std: 0.064)
  svr-poly-l: R2 = 0.298 (std: 0.064)
  knn-tuned-sqrt: R2 = 0.168 (std: 0.100)
  knn-tuned-l: R2 = 0.168 (std: 0.100)
  ridge: R2 = 0.092 (std: 0.056)

Model-based training with 12 models
Best R2: 0.298, Mean R2: 0.225
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9732, entropy=0.3670, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3048
  Round 1/3: Mean predicted reward = 9.928
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9700, entropy=0.4228, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5491
  Round 2/3: Mean predicted reward = 10.271
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9737, entropy=0.3529, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0681
  Round 3/3: Mean predicted reward = 10.186

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 56 Results ---
  Mean Oracle Reward: 10.247
  Min Oracle Reward: 7.965
  Max Oracle Reward: 11.709
  Std Oracle Reward: 0.900
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.225, Max: 0.298, Count: 13
  Total Sequences Evaluated: 1842

======================================================================
EXPERIMENT ROUND 57/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1842

--- Round 57 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGCTACGCGGTA
  CTACGGCGATCG
  AGCCCTGGTACG
  CGATTCCACGGG
  GCCTATCGAGGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.440
  Max reward: 13.275
  With intrinsic bonuses: 10.429

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9743, entropy=0.3374, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9739

=== Surrogate Model Training ===
Total samples: 1874

Training on 1793 samples (removed 81 outliers)
Reward range: [7.23, 13.23], mean: 10.30
  Created 13 candidate models for data size 1793
Current R2 threshold: 0.17000000000000004
  rf-tuned-l: R2 = 0.262 (std: 0.093)
  rf-tuned-xl: R2 = 0.263 (std: 0.092)
  gb-tuned-l: R2 = 0.251 (std: 0.066)
  gb-tuned-xl: R2 = 0.251 (std: 0.066)
  xgb-xl: R2 = 0.187 (std: 0.089)
  xgb-l: R2 = 0.187 (std: 0.089)
  mlp-adaptive-xl: R2 = 0.192 (std: 0.103)
  mlp-l: R2 = 0.222 (std: 0.069)
  svr-rbf-xl: R2 = 0.298 (std: 0.075)
  svr-poly-l: R2 = 0.298 (std: 0.075)
  knn-tuned-sqrt: R2 = 0.167 (std: 0.103)
  knn-tuned-l: R2 = 0.167 (std: 0.103)
  ridge: R2 = 0.094 (std: 0.063)

Model-based training with 10 models
Best R2: 0.298, Mean R2: 0.218
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9724, entropy=0.3558, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3852
  Round 1/3: Mean predicted reward = 10.154
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9723, entropy=0.3577, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5081
  Round 2/3: Mean predicted reward = 10.093
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9745, entropy=0.3486, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7809
  Round 3/3: Mean predicted reward = 10.226

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 57 Results ---
  Mean Oracle Reward: 10.419
  Min Oracle Reward: 7.815
  Max Oracle Reward: 13.221
  Std Oracle Reward: 1.244
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.218, Max: 0.298, Count: 13
  Total Sequences Evaluated: 1874

======================================================================
EXPERIMENT ROUND 58/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1874

--- Round 58 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GAGCCGTGCTAC
  GCGCAGGCATTC
  GTACACCCGTGG
  AGTGGCTGCACC
  GCGCACGGTCAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.395
  Max reward: 12.753
  With intrinsic bonuses: 10.401

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9739, entropy=0.3210, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5551

=== Surrogate Model Training ===
Total samples: 1906

Training on 1826 samples (removed 80 outliers)
Reward range: [7.20, 13.27], mean: 10.30
  Created 13 candidate models for data size 1826
Current R2 threshold: 0.18
  rf-tuned-l: R2 = 0.266 (std: 0.098)
  rf-tuned-xl: R2 = 0.267 (std: 0.098)
  gb-tuned-l: R2 = 0.252 (std: 0.067)
  gb-tuned-xl: R2 = 0.252 (std: 0.067)
  xgb-xl: R2 = 0.194 (std: 0.102)
  xgb-l: R2 = 0.194 (std: 0.102)
  mlp-adaptive-xl: R2 = 0.203 (std: 0.099)
  mlp-l: R2 = 0.241 (std: 0.058)
  svr-rbf-xl: R2 = 0.299 (std: 0.081)
  svr-poly-l: R2 = 0.299 (std: 0.081)
  knn-tuned-sqrt: R2 = 0.162 (std: 0.101)
  knn-tuned-l: R2 = 0.162 (std: 0.101)
  ridge: R2 = 0.092 (std: 0.069)

Model-based training with 10 models
Best R2: 0.299, Mean R2: 0.222
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9712, entropy=0.3237, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2728
  Round 1/3: Mean predicted reward = 9.973
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9734, entropy=0.3292, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3099
  Round 2/3: Mean predicted reward = 10.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9741, entropy=0.3274, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4796
  Round 3/3: Mean predicted reward = 10.390

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 58 Results ---
  Mean Oracle Reward: 10.354
  Min Oracle Reward: 6.636
  Max Oracle Reward: 12.447
  Std Oracle Reward: 1.370
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.222, Max: 0.299, Count: 13
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

--- Generated Sequences (Diversity: 0.938) ---
  AGGTGACCTCGC
  CACAGGTCTCGG
  GGCTTGACCAGC
  GATCGTCCAGCG
  CGCAATTCCGGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.412
  Max reward: 12.061
  With intrinsic bonuses: 10.373

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9733, entropy=0.3137, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0947

=== Surrogate Model Training ===
Total samples: 1938

Training on 1856 samples (removed 82 outliers)
Reward range: [7.23, 13.27], mean: 10.31
  Created 13 candidate models for data size 1856
Current R2 threshold: 0.19
  rf-tuned-l: R2 = 0.258 (std: 0.091)
  rf-tuned-xl: R2 = 0.253 (std: 0.095)
  gb-tuned-l: R2 = 0.244 (std: 0.073)
  gb-tuned-xl: R2 = 0.244 (std: 0.073)
  xgb-xl: R2 = 0.199 (std: 0.090)
  xgb-l: R2 = 0.199 (std: 0.090)
  mlp-adaptive-xl: R2 = 0.210 (std: 0.066)
  mlp-l: R2 = 0.233 (std: 0.078)
  svr-rbf-xl: R2 = 0.295 (std: 0.073)
  svr-poly-l: R2 = 0.295 (std: 0.073)
  knn-tuned-sqrt: R2 = 0.158 (std: 0.096)
  knn-tuned-l: R2 = 0.158 (std: 0.096)
  ridge: R2 = 0.089 (std: 0.076)

Model-based training with 10 models
Best R2: 0.295, Mean R2: 0.218
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9713, entropy=0.3068, kl_div=0.0000
    Epoch 1: policy_loss=0.0128, value_loss=0.9713, entropy=0.3062, kl_div=0.0478
  Round 1/3: Mean predicted reward = 9.864
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9714, entropy=0.2977, kl_div=0.0000
    Epoch 1: policy_loss=-0.0057, value_loss=0.9714, entropy=0.2979, kl_div=-0.0118
  Round 2/3: Mean predicted reward = 9.997
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9731, entropy=0.2988, kl_div=0.0000
    Epoch 1: policy_loss=-0.0052, value_loss=0.9731, entropy=0.2990, kl_div=-0.0104
  Round 3/3: Mean predicted reward = 10.267

  === Progress Analysis ===
  Status: NORMAL

--- Round 59 Results ---
  Mean Oracle Reward: 10.408
  Min Oracle Reward: 8.353
  Max Oracle Reward: 12.397
  Std Oracle Reward: 0.959
  Sequence Diversity: 0.938
  Models Used: 10
  Model R2 - Mean: 0.218, Max: 0.295, Count: 13
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
  AGCCTGTCGGAC
  AGGTCGCCGTAC
  TGCAGGAGCTCC
  CGTACAGGAGTC
  GGCACGTTACGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.270
  Max reward: 12.393
  With intrinsic bonuses: 10.338

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9737, entropy=0.2718, kl_div=0.0000
    Epoch 1: policy_loss=-0.0387, value_loss=0.9737, entropy=0.2723, kl_div=-0.0508

=== Surrogate Model Training ===
Total samples: 1970

Training on 1886 samples (removed 84 outliers)
Reward range: [7.23, 13.27], mean: 10.31
  Created 13 candidate models for data size 1886
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.260 (std: 0.084)
  rf-tuned-xl: R2 = 0.259 (std: 0.080)
  gb-tuned-l: R2 = 0.244 (std: 0.078)
  gb-tuned-xl: R2 = 0.244 (std: 0.078)
  xgb-xl: R2 = 0.182 (std: 0.091)
  xgb-l: R2 = 0.182 (std: 0.091)
  mlp-adaptive-xl: R2 = 0.220 (std: 0.078)
  mlp-l: R2 = 0.205 (std: 0.069)
  svr-rbf-xl: R2 = 0.291 (std: 0.065)
  svr-poly-l: R2 = 0.291 (std: 0.065)
  knn-tuned-sqrt: R2 = 0.155 (std: 0.086)
  knn-tuned-l: R2 = 0.155 (std: 0.086)
  ridge: R2 = 0.088 (std: 0.080)

Model-based training with 8 models
Best R2: 0.291, Mean R2: 0.214
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9703, entropy=0.2896, kl_div=0.0000
    Epoch 1: policy_loss=-0.0705, value_loss=0.9703, entropy=0.2934, kl_div=-0.2954
  Round 1/3: Mean predicted reward = 9.932
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9704, entropy=0.3084, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0712
  Round 2/3: Mean predicted reward = 10.266
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=0.2960, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1858
  Round 3/3: Mean predicted reward = 10.210

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 60 Results ---
  Mean Oracle Reward: 10.283
  Min Oracle Reward: 4.114
  Max Oracle Reward: 12.653
  Std Oracle Reward: 1.634
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: 0.214, Max: 0.291, Count: 13
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
  CCTCGTGGCAAG
  CCGGGTACATGC
  CTGGGCTACGCA
  CTTCGCGACAGG
  GGTCAAGCTGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.397
  Max reward: 12.032
  With intrinsic bonuses: 10.417

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9734, entropy=0.3002, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3639

=== Surrogate Model Training ===
Total samples: 2002

Training on 1918 samples (removed 84 outliers)
Reward range: [7.23, 13.27], mean: 10.32
  Created 13 candidate models for data size 1918
Current R2 threshold: 0.21000000000000002
  rf-tuned-l: R2 = 0.270 (std: 0.072)
  rf-tuned-xl: R2 = 0.256 (std: 0.072)
  gb-tuned-l: R2 = 0.243 (std: 0.069)
  gb-tuned-xl: R2 = 0.243 (std: 0.069)
  xgb-xl: R2 = 0.222 (std: 0.062)
  xgb-l: R2 = 0.222 (std: 0.062)
  mlp-adaptive-xl: R2 = 0.235 (std: 0.084)
  mlp-l: R2 = 0.211 (std: 0.072)
  svr-rbf-xl: R2 = 0.303 (std: 0.063)
  svr-poly-l: R2 = 0.303 (std: 0.063)
  knn-tuned-sqrt: R2 = 0.174 (std: 0.074)
  knn-tuned-l: R2 = 0.174 (std: 0.074)
  ridge: R2 = 0.088 (std: 0.081)

Model-based training with 10 models
Best R2: 0.303, Mean R2: 0.227
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9730, entropy=0.3246, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1047
  Round 1/5: Mean predicted reward = 10.322
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9725, entropy=0.3117, kl_div=0.0000
    Epoch 1: policy_loss=-0.0590, value_loss=0.9724, entropy=0.3125, kl_div=-0.1069
  Round 2/5: Mean predicted reward = 10.001
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9737, entropy=0.2869, kl_div=0.0000
    Epoch 1: policy_loss=-0.0294, value_loss=0.9737, entropy=0.2865, kl_div=0.0003
  Round 3/5: Mean predicted reward = 10.130
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9699, entropy=0.3250, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3574
  Round 4/5: Mean predicted reward = 10.345
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9726, entropy=0.2766, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5907
  Round 5/5: Mean predicted reward = 10.392

  === Progress Analysis ===
  Status: NORMAL

--- Round 61 Results ---
  Mean Oracle Reward: 10.413
  Min Oracle Reward: 7.970
  Max Oracle Reward: 12.160
  Std Oracle Reward: 1.023
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.227, Max: 0.303, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  ACGGTCTACGGA
  TACATGGCCCGG
  TCGGACCCGTAG
  TACCGCGAGCGT
  CGGCAAGCCGTT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.488
  Max reward: 13.438
  With intrinsic bonuses: 10.480

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9736, entropy=0.2766, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5012

=== Surrogate Model Training ===
Total samples: 2034

Training on 1946 samples (removed 88 outliers)
Reward range: [7.28, 13.27], mean: 10.32
  Created 13 candidate models for data size 1946
Current R2 threshold: 0.22000000000000003
  rf-tuned-l: R2 = 0.270 (std: 0.067)
  rf-tuned-xl: R2 = 0.263 (std: 0.073)
  gb-tuned-l: R2 = 0.242 (std: 0.069)
  gb-tuned-xl: R2 = 0.242 (std: 0.069)
  xgb-xl: R2 = 0.216 (std: 0.081)
  xgb-l: R2 = 0.216 (std: 0.081)
  mlp-adaptive-xl: R2 = 0.210 (std: 0.058)
  mlp-l: R2 = 0.232 (std: 0.069)
  svr-rbf-xl: R2 = 0.298 (std: 0.063)
  svr-poly-l: R2 = 0.298 (std: 0.063)
  knn-tuned-sqrt: R2 = 0.167 (std: 0.075)
  knn-tuned-l: R2 = 0.167 (std: 0.075)
  ridge: R2 = 0.082 (std: 0.083)

Model-based training with 7 models
Best R2: 0.298, Mean R2: 0.223
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=0.2961, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3309
  Round 1/3: Mean predicted reward = 9.970
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9728, entropy=0.2501, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4619
  Round 2/3: Mean predicted reward = 10.259
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9741, entropy=0.2627, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5798
  Round 3/3: Mean predicted reward = 10.190

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 62 Results ---
  Mean Oracle Reward: 10.519
  Min Oracle Reward: 6.089
  Max Oracle Reward: 13.396
  Std Oracle Reward: 1.373
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: 0.223, Max: 0.298, Count: 13
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

--- Generated Sequences (Diversity: 0.906) ---
  CCGCTGAAGTCG
  TCGAGAGCGCTC
  CGCTCGCAGAGT
  CAGCAGCGTCTG
  AACGGGCTTGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.577
  Max reward: 13.417
  With intrinsic bonuses: 10.607

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.2667, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3733

=== Surrogate Model Training ===
Total samples: 2066

Training on 1976 samples (removed 90 outliers)
Reward range: [7.27, 13.27], mean: 10.33
  Created 13 candidate models for data size 1976
Current R2 threshold: 0.23000000000000004
  rf-tuned-l: R2 = 0.267 (std: 0.079)
  rf-tuned-xl: R2 = 0.271 (std: 0.084)
  gb-tuned-l: R2 = 0.248 (std: 0.067)
  gb-tuned-xl: R2 = 0.248 (std: 0.067)
  xgb-xl: R2 = 0.217 (std: 0.079)
  xgb-l: R2 = 0.217 (std: 0.079)
  mlp-adaptive-xl: R2 = 0.242 (std: 0.069)
  mlp-l: R2 = 0.237 (std: 0.082)
  svr-rbf-xl: R2 = 0.303 (std: 0.069)
  svr-poly-l: R2 = 0.303 (std: 0.069)
  knn-tuned-sqrt: R2 = 0.178 (std: 0.061)
  knn-tuned-l: R2 = 0.178 (std: 0.061)
  ridge: R2 = 0.082 (std: 0.096)

Model-based training with 8 models
Best R2: 0.303, Mean R2: 0.230
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.2771, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2227
  Round 1/5: Mean predicted reward = 9.976
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9706, entropy=0.2609, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0964
  Round 2/5: Mean predicted reward = 10.086
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9716, entropy=0.2496, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1430
  Round 3/5: Mean predicted reward = 10.079
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9724, entropy=0.2753, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3120
  Round 4/5: Mean predicted reward = 10.407
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9726, entropy=0.2370, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2907
  Round 5/5: Mean predicted reward = 10.312

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 63 Results ---
  Mean Oracle Reward: 10.585
  Min Oracle Reward: 6.886
  Max Oracle Reward: 13.358
  Std Oracle Reward: 1.628
  Sequence Diversity: 0.906
  Models Used: 8
  Model R2 - Mean: 0.230, Max: 0.303, Count: 13
  Total Sequences Evaluated: 2066

======================================================================
EXPERIMENT ROUND 64/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2066
  Performance plateaued, reducing LR to 0.000019

--- Round 64 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.938) ---
  AGCGCATGTCCG
  GATGCCCCGTGA
  CGGAGACGATCT
  GTCCACGACGGT
  CCGGAGTCTGCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.402
  Max reward: 13.442
  With intrinsic bonuses: 10.431

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9727, entropy=0.2214, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1472

=== Surrogate Model Training ===
Total samples: 2098

Training on 2007 samples (removed 91 outliers)
Reward range: [7.27, 13.28], mean: 10.33
  Created 13 candidate models for data size 2007
Current R2 threshold: 0.24000000000000005
  rf-tuned-l: R2 = 0.280 (std: 0.076)
  rf-tuned-xl: R2 = 0.277 (std: 0.085)
  gb-tuned-l: R2 = 0.254 (std: 0.072)
  gb-tuned-xl: R2 = 0.254 (std: 0.072)
  xgb-xl: R2 = 0.227 (std: 0.105)
  xgb-l: R2 = 0.227 (std: 0.105)
  mlp-adaptive-xl: R2 = 0.232 (std: 0.088)
  mlp-l: R2 = 0.247 (std: 0.081)
  svr-rbf-xl: R2 = 0.313 (std: 0.077)
  svr-poly-l: R2 = 0.313 (std: 0.077)
  knn-tuned-sqrt: R2 = 0.198 (std: 0.073)
  knn-tuned-l: R2 = 0.198 (std: 0.073)
  ridge: R2 = 0.079 (std: 0.103)

Model-based training with 7 models
Best R2: 0.313, Mean R2: 0.238
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9724, entropy=0.2203, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0821
  Round 1/5: Mean predicted reward = 9.639
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9724, entropy=0.2359, kl_div=0.0000
    Epoch 1: policy_loss=0.0133, value_loss=0.9724, entropy=0.2357, kl_div=0.0313
  Round 2/5: Mean predicted reward = 9.887
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9720, entropy=0.2177, kl_div=0.0000
    Epoch 1: policy_loss=-0.0310, value_loss=0.9720, entropy=0.2182, kl_div=-0.0476
  Round 3/5: Mean predicted reward = 9.828
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.2226, kl_div=0.0000
    Epoch 1: policy_loss=-0.0136, value_loss=0.9706, entropy=0.2236, kl_div=-0.0617
  Round 4/5: Mean predicted reward = 10.045
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9720, entropy=0.2520, kl_div=0.0000
    Epoch 1: policy_loss=-0.0090, value_loss=0.9720, entropy=0.2520, kl_div=0.0087
  Round 5/5: Mean predicted reward = 10.328

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 64 Results ---
  Mean Oracle Reward: 10.405
  Min Oracle Reward: 6.706
  Max Oracle Reward: 13.400
  Std Oracle Reward: 1.671
  Sequence Diversity: 0.938
  Models Used: 7
  Model R2 - Mean: 0.238, Max: 0.313, Count: 13
  Total Sequences Evaluated: 2098

======================================================================
EXPERIMENT ROUND 65/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2098
  Performance plateaued, reducing LR to 0.000150

--- Round 65 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  ACCGTCGGACTG
  CTCAGCGGTACG
  CTAGGTCACGCG
  CCCGTCGGGAAT
  CTACCGTAGAGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.615
  Max reward: 13.469
  With intrinsic bonuses: 10.618

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9736, entropy=0.2463, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4457

=== Surrogate Model Training ===
Total samples: 2130

Training on 2037 samples (removed 93 outliers)
Reward range: [7.28, 13.28], mean: 10.34
  Created 13 candidate models for data size 2037
Current R2 threshold: 0.25000000000000006
  rf-tuned-l: R2 = 0.281 (std: 0.077)
  rf-tuned-xl: R2 = 0.277 (std: 0.075)
  gb-tuned-l: R2 = 0.258 (std: 0.070)
  gb-tuned-xl: R2 = 0.258 (std: 0.070)
  xgb-xl: R2 = 0.230 (std: 0.095)
  xgb-l: R2 = 0.230 (std: 0.095)
  mlp-adaptive-xl: R2 = 0.259 (std: 0.100)
  mlp-l: R2 = 0.257 (std: 0.096)
  svr-rbf-xl: R2 = 0.316 (std: 0.079)
  svr-poly-l: R2 = 0.316 (std: 0.079)
  knn-tuned-sqrt: R2 = 0.196 (std: 0.077)
  knn-tuned-l: R2 = 0.196 (std: 0.077)
  ridge: R2 = 0.073 (std: 0.105)

Model-based training with 8 models
Best R2: 0.316, Mean R2: 0.242
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9716, entropy=0.2526, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0976
  Round 1/5: Mean predicted reward = 9.489
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9721, entropy=0.2282, kl_div=0.0000
    Epoch 1: policy_loss=-0.0612, value_loss=0.9720, entropy=0.2306, kl_div=-0.1271
  Round 2/5: Mean predicted reward = 9.659
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9726, entropy=0.2526, kl_div=0.0000
    Epoch 1: policy_loss=0.0344, value_loss=0.9725, entropy=0.2569, kl_div=-0.3624
  Round 3/5: Mean predicted reward = 9.985
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9732, entropy=0.2681, kl_div=0.0000
    Epoch 1: policy_loss=0.0599, value_loss=0.9732, entropy=0.2728, kl_div=-0.3659
  Round 4/5: Mean predicted reward = 10.243
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9721, entropy=0.2674, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1032
  Round 5/5: Mean predicted reward = 10.380

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 65 Results ---
  Mean Oracle Reward: 10.545
  Min Oracle Reward: 6.438
  Max Oracle Reward: 13.678
  Std Oracle Reward: 1.495
  Sequence Diversity: 0.969
  Models Used: 8
  Model R2 - Mean: 0.242, Max: 0.316, Count: 13
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

--- Generated Sequences (Diversity: 0.938) ---
  GTTGGGAACCAC
  TTGAGGCCACGC
  GTGGACCATGCC
  AGGCACTGCTCG
  ACTGCTCGGCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.657
  Max reward: 12.544
  With intrinsic bonuses: 10.630

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9735, entropy=0.2702, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1954

=== Surrogate Model Training ===
Total samples: 2162

Training on 2066 samples (removed 96 outliers)
Reward range: [7.30, 13.28], mean: 10.35
  Created 13 candidate models for data size 2066
Current R2 threshold: 0.26000000000000006
  rf-tuned-l: R2 = 0.283 (std: 0.078)
  rf-tuned-xl: R2 = 0.281 (std: 0.075)
  gb-tuned-l: R2 = 0.265 (std: 0.063)
  gb-tuned-xl: R2 = 0.265 (std: 0.063)
  xgb-xl: R2 = 0.228 (std: 0.106)
  xgb-l: R2 = 0.228 (std: 0.106)
  mlp-adaptive-xl: R2 = 0.260 (std: 0.068)
  mlp-l: R2 = 0.228 (std: 0.105)
  svr-rbf-xl: R2 = 0.318 (std: 0.075)
  svr-poly-l: R2 = 0.318 (std: 0.075)
  knn-tuned-sqrt: R2 = 0.191 (std: 0.075)
  knn-tuned-l: R2 = 0.191 (std: 0.075)
  ridge: R2 = 0.066 (std: 0.099)

Model-based training with 7 models
Best R2: 0.318, Mean R2: 0.240
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9720, entropy=0.2284, kl_div=0.0000
    Epoch 1: policy_loss=-0.0095, value_loss=0.9720, entropy=0.2286, kl_div=0.0162
  Round 1/5: Mean predicted reward = 9.305
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9714, entropy=0.2661, kl_div=0.0000
    Epoch 1: policy_loss=-0.0764, value_loss=0.9714, entropy=0.2720, kl_div=-0.4052
  Round 2/5: Mean predicted reward = 9.288
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9713, entropy=0.2475, kl_div=0.0000
    Epoch 1: policy_loss=0.0104, value_loss=0.9713, entropy=0.2539, kl_div=-0.4379
  Round 3/5: Mean predicted reward = 9.848
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2939, kl_div=0.0000
    Epoch 1: policy_loss=0.0215, value_loss=0.9689, entropy=0.3010, kl_div=-0.3043
  Round 4/5: Mean predicted reward = 10.104
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9722, entropy=0.2584, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0661
  Round 5/5: Mean predicted reward = 10.243

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 66 Results ---
  Mean Oracle Reward: 10.672
  Min Oracle Reward: 6.554
  Max Oracle Reward: 12.412
  Std Oracle Reward: 1.275
  Sequence Diversity: 0.938
  Models Used: 7
  Model R2 - Mean: 0.240, Max: 0.318, Count: 13
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
  CTGGGCCATGCA
  CCTCTCGGGGAA
  TGGGCTCACGAC
  TGCGAACGCCGT
  GGCCGTCTAGAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.690
  Max reward: 13.517
  With intrinsic bonuses: 10.715

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9721, entropy=0.2990, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3066

=== Surrogate Model Training ===
Total samples: 2194

Training on 2102 samples (removed 92 outliers)
Reward range: [7.28, 13.31], mean: 10.35
  Created 13 candidate models for data size 2102
Current R2 threshold: 0.2700000000000001
  rf-tuned-l: R2 = 0.296 (std: 0.076)
  rf-tuned-xl: R2 = 0.291 (std: 0.073)
  gb-tuned-l: R2 = 0.273 (std: 0.067)
  gb-tuned-xl: R2 = 0.273 (std: 0.067)
  xgb-xl: R2 = 0.268 (std: 0.112)
  xgb-l: R2 = 0.268 (std: 0.112)
  mlp-adaptive-xl: R2 = 0.256 (std: 0.089)
  mlp-l: R2 = 0.279 (std: 0.089)
  svr-rbf-xl: R2 = 0.331 (std: 0.084)
  svr-poly-l: R2 = 0.331 (std: 0.084)
  knn-tuned-sqrt: R2 = 0.202 (std: 0.083)
  knn-tuned-l: R2 = 0.202 (std: 0.083)
  ridge: R2 = 0.070 (std: 0.105)

Model-based training with 7 models
Best R2: 0.331, Mean R2: 0.257
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=0.2994, kl_div=0.0000
    Epoch 1: policy_loss=-0.0261, value_loss=0.9704, entropy=0.3023, kl_div=0.0387
  Round 1/5: Mean predicted reward = 9.633
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9729, entropy=0.3013, kl_div=0.0000
    Epoch 1: policy_loss=0.1368, value_loss=0.9729, entropy=0.3129, kl_div=-0.5909
  Round 2/5: Mean predicted reward = 9.719
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.2490, kl_div=0.0000
    Epoch 1: policy_loss=0.1091, value_loss=0.9697, entropy=0.2580, kl_div=-0.5492
  Round 3/5: Mean predicted reward = 9.893
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9737, entropy=0.3201, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0698
  Round 4/5: Mean predicted reward = 10.214
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9711, entropy=0.3294, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3902
  Round 5/5: Mean predicted reward = 10.357

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 67 Results ---
  Mean Oracle Reward: 10.684
  Min Oracle Reward: 7.646
  Max Oracle Reward: 13.102
  Std Oracle Reward: 1.458
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: 0.257, Max: 0.331, Count: 13
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
  TCGCCTGAAGGC
  AGTGGTAGCCCC
  CTCTACGGACGG
  GTAAGGCCGCTC
  GTCCCGAGAGTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.578
  Max reward: 13.065
  With intrinsic bonuses: 10.594

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9738, entropy=0.3129, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1742

=== Surrogate Model Training ===
Total samples: 2226

Training on 2134 samples (removed 92 outliers)
Reward range: [7.28, 13.31], mean: 10.36
  Created 13 candidate models for data size 2134
Current R2 threshold: 0.27999999999999997
  rf-tuned-l: R2 = 0.298 (std: 0.073)
  rf-tuned-xl: R2 = 0.305 (std: 0.081)
  gb-tuned-l: R2 = 0.271 (std: 0.062)
  gb-tuned-xl: R2 = 0.271 (std: 0.062)
  xgb-xl: R2 = 0.299 (std: 0.101)
  xgb-l: R2 = 0.299 (std: 0.101)
  mlp-adaptive-xl: R2 = 0.288 (std: 0.090)
  mlp-l: R2 = 0.268 (std: 0.101)
  svr-rbf-xl: R2 = 0.341 (std: 0.084)
  svr-poly-l: R2 = 0.341 (std: 0.084)
  knn-tuned-sqrt: R2 = 0.213 (std: 0.084)
  knn-tuned-l: R2 = 0.213 (std: 0.084)
  ridge: R2 = 0.066 (std: 0.099)

Model-based training with 7 models
Best R2: 0.341, Mean R2: 0.267
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9715, entropy=0.2611, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0826
  Round 1/5: Mean predicted reward = 9.693
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.3031, kl_div=0.0000
    Epoch 1: policy_loss=-0.0151, value_loss=0.9692, entropy=0.3039, kl_div=-0.0150
  Round 2/5: Mean predicted reward = 9.863
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.2977, kl_div=0.0000
    Epoch 1: policy_loss=-0.0298, value_loss=0.9696, entropy=0.3010, kl_div=-0.2069
  Round 3/5: Mean predicted reward = 10.071
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9710, entropy=0.3075, kl_div=0.0000
    Epoch 1: policy_loss=-0.0242, value_loss=0.9710, entropy=0.3098, kl_div=-0.1123
  Round 4/5: Mean predicted reward = 10.071
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.2983, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1106
  Round 5/5: Mean predicted reward = 10.261

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 68 Results ---
  Mean Oracle Reward: 10.561
  Min Oracle Reward: 7.208
  Max Oracle Reward: 13.001
  Std Oracle Reward: 1.341
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: 0.267, Max: 0.341, Count: 13
  Total Sequences Evaluated: 2226

======================================================================
EXPERIMENT ROUND 69/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2226
  Performance plateaued, reducing LR to 0.000019

--- Round 69 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ATGTGCGACCGC
  ATTGGGCCCCGA
  TCAGTGGCACCG
  CCGACTGGTAGC
  AGTACCCGGGCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.575
  Max reward: 13.581
  With intrinsic bonuses: 10.588

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9727, entropy=0.3185, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0524

=== Surrogate Model Training ===
Total samples: 2258

Training on 2166 samples (removed 92 outliers)
Reward range: [7.28, 13.34], mean: 10.36
  Created 13 candidate models for data size 2166
Current R2 threshold: 0.29
  rf-tuned-l: R2 = 0.310 (std: 0.096)
  rf-tuned-xl: R2 = 0.310 (std: 0.090)
  gb-tuned-l: R2 = 0.282 (std: 0.075)
  gb-tuned-xl: R2 = 0.282 (std: 0.075)
  xgb-xl: R2 = 0.307 (std: 0.115)
  xgb-l: R2 = 0.307 (std: 0.115)
  mlp-adaptive-xl: R2 = 0.295 (std: 0.115)
  mlp-l: R2 = 0.286 (std: 0.116)
  svr-rbf-xl: R2 = 0.345 (std: 0.095)
  svr-poly-l: R2 = 0.345 (std: 0.095)
  knn-tuned-sqrt: R2 = 0.222 (std: 0.086)
  knn-tuned-l: R2 = 0.222 (std: 0.086)
  ridge: R2 = 0.067 (std: 0.096)

Model-based training with 7 models
Best R2: 0.345, Mean R2: 0.275
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=0.2859, kl_div=0.0000
    Epoch 1: policy_loss=0.0014, value_loss=0.9709, entropy=0.2857, kl_div=0.0146
  Round 1/5: Mean predicted reward = 9.826
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.3216, kl_div=0.0000
    Epoch 1: policy_loss=-0.0197, value_loss=0.9693, entropy=0.3224, kl_div=-0.0431
  Round 2/5: Mean predicted reward = 9.857
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.3053, kl_div=0.0000
    Epoch 1: policy_loss=-0.0050, value_loss=0.9690, entropy=0.3060, kl_div=-0.0501
  Round 3/5: Mean predicted reward = 9.888
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.2785, kl_div=0.0000
    Epoch 1: policy_loss=-0.0100, value_loss=0.9703, entropy=0.2786, kl_div=0.0010
  Round 4/5: Mean predicted reward = 10.096
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9717, entropy=0.3039, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0572
  Round 5/5: Mean predicted reward = 10.212

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 69 Results ---
  Mean Oracle Reward: 10.587
  Min Oracle Reward: 7.377
  Max Oracle Reward: 13.471
  Std Oracle Reward: 1.421
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: 0.275, Max: 0.345, Count: 13
  Total Sequences Evaluated: 2258

======================================================================
EXPERIMENT ROUND 70/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2258
  Performance plateaued, reducing LR to 0.000150

--- Round 70 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  TACGCAGTGGCC
  GAGTTCACCGCG
  GCGCCATTGACG
  CGCACTCTGAGG
  CAGGCCCGATGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.630
  Max reward: 12.982
  With intrinsic bonuses: 10.615

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.3383, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6410

=== Surrogate Model Training ===
Total samples: 2290

Training on 2198 samples (removed 92 outliers)
Reward range: [7.27, 13.34], mean: 10.36
  Created 13 candidate models for data size 2198
Current R2 threshold: 0.3
  rf-tuned-l: R2 = 0.292 (std: 0.086)
  rf-tuned-xl: R2 = 0.297 (std: 0.085)
  gb-tuned-l: R2 = 0.283 (std: 0.060)
  gb-tuned-xl: R2 = 0.283 (std: 0.060)
  xgb-xl: R2 = 0.289 (std: 0.113)
  xgb-l: R2 = 0.289 (std: 0.113)
  mlp-adaptive-xl: R2 = 0.271 (std: 0.079)
  mlp-l: R2 = 0.270 (std: 0.116)
  svr-rbf-xl: R2 = 0.341 (std: 0.083)
  svr-poly-l: R2 = 0.341 (std: 0.083)
  knn-tuned-sqrt: R2 = 0.221 (std: 0.081)
  knn-tuned-l: R2 = 0.221 (std: 0.081)
  ridge: R2 = 0.069 (std: 0.090)

Model-based training with 2 models
Best R2: 0.341, Mean R2: 0.267
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.2983, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3632
  Round 1/5: Mean predicted reward = 9.674
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9700, entropy=0.2863, kl_div=0.0000
    Epoch 1: policy_loss=-0.0337, value_loss=0.9700, entropy=0.2862, kl_div=0.0070
  Round 2/5: Mean predicted reward = 9.666
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=0.2906, kl_div=0.0000
    Epoch 1: policy_loss=-0.0393, value_loss=0.9704, entropy=0.2907, kl_div=0.0123
  Round 3/5: Mean predicted reward = 10.088
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9734, entropy=0.2885, kl_div=0.0000
    Epoch 1: policy_loss=-0.0590, value_loss=0.9734, entropy=0.2925, kl_div=-0.1577
  Round 4/5: Mean predicted reward = 10.288
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9727, entropy=0.3080, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3019
  Round 5/5: Mean predicted reward = 10.327

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 70 Results ---
  Mean Oracle Reward: 10.668
  Min Oracle Reward: 5.472
  Max Oracle Reward: 12.618
  Std Oracle Reward: 1.576
  Sequence Diversity: 0.969
  Models Used: 2
  Model R2 - Mean: 0.267, Max: 0.341, Count: 13
  Total Sequences Evaluated: 2290

======================================================================
EXPERIMENT ROUND 71/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2290
  Performance plateaued, reducing LR to 0.000136

--- Round 71 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGCATAACCGGT
  CCCGGGTAGATC
  GGCTCAGCTGAC
  CCTTACCGAGGG
  GGGGTCATCCAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.481
  Max reward: 13.778
  With intrinsic bonuses: 10.496

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9751, entropy=0.2880, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5072

=== Surrogate Model Training ===
Total samples: 2322

Training on 2231 samples (removed 91 outliers)
Reward range: [7.26, 13.37], mean: 10.37
  Created 13 candidate models for data size 2231
Current R2 threshold: 0.31
  rf-tuned-l: R2 = 0.315 (std: 0.103)
  rf-tuned-xl: R2 = 0.311 (std: 0.095)
  gb-tuned-l: R2 = 0.291 (std: 0.066)
  gb-tuned-xl: R2 = 0.291 (std: 0.066)
  xgb-xl: R2 = 0.329 (std: 0.120)
  xgb-l: R2 = 0.329 (std: 0.120)
  mlp-adaptive-xl: R2 = 0.277 (std: 0.135)
  mlp-l: R2 = 0.295 (std: 0.113)
  svr-rbf-xl: R2 = 0.348 (std: 0.090)
  svr-poly-l: R2 = 0.348 (std: 0.090)
  knn-tuned-sqrt: R2 = 0.229 (std: 0.097)
  knn-tuned-l: R2 = 0.229 (std: 0.097)
  ridge: R2 = 0.069 (std: 0.087)

Model-based training with 6 models
Best R2: 0.348, Mean R2: 0.281
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9716, entropy=0.2783, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1363
  Round 1/5: Mean predicted reward = 9.657
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9717, entropy=0.2849, kl_div=0.0000
    Epoch 1: policy_loss=-0.0652, value_loss=0.9716, entropy=0.2873, kl_div=-0.1346
  Round 2/5: Mean predicted reward = 9.563
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9700, entropy=0.2863, kl_div=0.0000
    Epoch 1: policy_loss=-0.0444, value_loss=0.9700, entropy=0.2925, kl_div=-0.2983
  Round 3/5: Mean predicted reward = 9.885
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9730, entropy=0.2853, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1311
  Round 4/5: Mean predicted reward = 10.119
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.2960, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2288
  Round 5/5: Mean predicted reward = 10.402

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 71 Results ---
  Mean Oracle Reward: 10.441
  Min Oracle Reward: 7.732
  Max Oracle Reward: 13.515
  Std Oracle Reward: 1.459
  Sequence Diversity: 1.000
  Models Used: 6
  Model R2 - Mean: 0.281, Max: 0.348, Count: 13
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
  CGTAAGGCGCCT
  CAGTCATGCGGC
  AGCCGATGCCTG
  GACCAAGGGTTC
  TCCGGACTACGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.850
  Max reward: 12.798
  With intrinsic bonuses: 10.874

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9718, entropy=0.2940, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4087

=== Surrogate Model Training ===
Total samples: 2354

Training on 2261 samples (removed 93 outliers)
Reward range: [7.28, 13.37], mean: 10.38
  Created 13 candidate models for data size 2261
Current R2 threshold: 0.32
  rf-tuned-l: R2 = 0.321 (std: 0.104)
  rf-tuned-xl: R2 = 0.323 (std: 0.104)
  gb-tuned-l: R2 = 0.293 (std: 0.066)
  gb-tuned-xl: R2 = 0.293 (std: 0.066)
  xgb-xl: R2 = 0.318 (std: 0.146)
  xgb-l: R2 = 0.318 (std: 0.146)
  mlp-adaptive-xl: R2 = 0.292 (std: 0.089)
  mlp-l: R2 = 0.285 (std: 0.119)
  svr-rbf-xl: R2 = 0.354 (std: 0.096)
  svr-poly-l: R2 = 0.354 (std: 0.096)
  knn-tuned-sqrt: R2 = 0.226 (std: 0.106)
  knn-tuned-l: R2 = 0.226 (std: 0.106)
  ridge: R2 = 0.068 (std: 0.082)

Model-based training with 4 models
Best R2: 0.354, Mean R2: 0.282
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9714, entropy=0.3147, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1410
  Round 1/5: Mean predicted reward = 9.547
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9708, entropy=0.2712, kl_div=0.0000
    Epoch 1: policy_loss=-0.0434, value_loss=0.9708, entropy=0.2724, kl_div=-0.0395
  Round 2/5: Mean predicted reward = 9.983
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.3012, kl_div=0.0000
    Epoch 1: policy_loss=-0.0249, value_loss=0.9703, entropy=0.3076, kl_div=-0.4164
  Round 3/5: Mean predicted reward = 9.917
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9728, entropy=0.3188, kl_div=0.0000
    Epoch 1: policy_loss=0.0136, value_loss=0.9728, entropy=0.3244, kl_div=-0.2030
  Round 4/5: Mean predicted reward = 10.028
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9717, entropy=0.2960, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0802
  Round 5/5: Mean predicted reward = 10.264

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 72 Results ---
  Mean Oracle Reward: 10.851
  Min Oracle Reward: 8.199
  Max Oracle Reward: 12.824
  Std Oracle Reward: 1.143
  Sequence Diversity: 1.000
  Models Used: 4
  Model R2 - Mean: 0.282, Max: 0.354, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  GGTGAACCAGCT
  TCAGACGCGCGT
  CCAGCTAGCGGT
  TCCAGCGCGGAT
  CAGCTTGGGCAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.219
  Max reward: 12.923
  With intrinsic bonuses: 10.266

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.2823, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2682

=== Surrogate Model Training ===
Total samples: 2386

Training on 2291 samples (removed 95 outliers)
Reward range: [7.27, 13.37], mean: 10.38
  Created 13 candidate models for data size 2291
Current R2 threshold: 0.33
  rf-tuned-l: R2 = 0.329 (std: 0.117)
  rf-tuned-xl: R2 = 0.330 (std: 0.110)
  gb-tuned-l: R2 = 0.291 (std: 0.067)
  gb-tuned-xl: R2 = 0.291 (std: 0.067)
  xgb-xl: R2 = 0.322 (std: 0.132)
  xgb-l: R2 = 0.322 (std: 0.132)
  mlp-adaptive-xl: R2 = 0.305 (std: 0.121)
  mlp-l: R2 = 0.305 (std: 0.124)
  svr-rbf-xl: R2 = 0.359 (std: 0.102)
  svr-poly-l: R2 = 0.359 (std: 0.102)
  knn-tuned-sqrt: R2 = 0.236 (std: 0.109)
  knn-tuned-l: R2 = 0.236 (std: 0.109)
  ridge: R2 = 0.071 (std: 0.092)

Model-based training with 3 models
Best R2: 0.359, Mean R2: 0.289
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9717, entropy=0.3021, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0629
  Round 1/5: Mean predicted reward = 9.646
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9727, entropy=0.3298, kl_div=0.0000
    Epoch 1: policy_loss=-0.0454, value_loss=0.9727, entropy=0.3332, kl_div=-0.1026
  Round 2/5: Mean predicted reward = 9.985
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9718, entropy=0.2739, kl_div=0.0000
    Epoch 1: policy_loss=-0.0275, value_loss=0.9718, entropy=0.2783, kl_div=-0.2013
  Round 3/5: Mean predicted reward = 9.944
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9722, entropy=0.3556, kl_div=0.0000
    Epoch 1: policy_loss=-0.0519, value_loss=0.9722, entropy=0.3592, kl_div=-0.0728
  Round 4/5: Mean predicted reward = 10.417
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9714, entropy=0.2883, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2705
  Round 5/5: Mean predicted reward = 10.350

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 73 Results ---
  Mean Oracle Reward: 10.264
  Min Oracle Reward: 4.980
  Max Oracle Reward: 12.662
  Std Oracle Reward: 1.953
  Sequence Diversity: 1.000
  Models Used: 3
  Model R2 - Mean: 0.289, Max: 0.359, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  TAACGCCGCTGG
  GATCCCACGGTG
  CCCTGGGACAGT
  AACGGCGCCTTG
  GTGTCCGGACAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.533
  Max reward: 13.606
  With intrinsic bonuses: 10.581

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9751, entropy=0.2872, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1572

=== Surrogate Model Training ===
Total samples: 2418

Training on 2323 samples (removed 95 outliers)
Reward range: [7.26, 13.42], mean: 10.39
  Created 13 candidate models for data size 2323
Current R2 threshold: 0.34
  rf-tuned-l: R2 = 0.331 (std: 0.106)
  rf-tuned-xl: R2 = 0.323 (std: 0.103)
  gb-tuned-l: R2 = 0.294 (std: 0.061)
  gb-tuned-xl: R2 = 0.294 (std: 0.061)
  xgb-xl: R2 = 0.310 (std: 0.143)
  xgb-l: R2 = 0.310 (std: 0.143)
  mlp-adaptive-xl: R2 = 0.300 (std: 0.123)
  mlp-l: R2 = 0.285 (std: 0.133)
  svr-rbf-xl: R2 = 0.360 (std: 0.096)
  svr-poly-l: R2 = 0.360 (std: 0.096)
  knn-tuned-sqrt: R2 = 0.242 (std: 0.113)
  knn-tuned-l: R2 = 0.242 (std: 0.113)
  ridge: R2 = 0.069 (std: 0.090)

Model-based training with 2 models
Best R2: 0.360, Mean R2: 0.286
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9734, entropy=0.3511, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0610
  Round 1/5: Mean predicted reward = 9.555
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.3243, kl_div=0.0000
    Epoch 1: policy_loss=-0.0104, value_loss=0.9705, entropy=0.3251, kl_div=-0.0233
  Round 2/5: Mean predicted reward = 9.731
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9721, entropy=0.2933, kl_div=0.0000
    Epoch 1: policy_loss=-0.0241, value_loss=0.9721, entropy=0.2957, kl_div=-0.1083
  Round 3/5: Mean predicted reward = 10.114
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9723, entropy=0.3105, kl_div=0.0000
    Epoch 1: policy_loss=-0.0354, value_loss=0.9723, entropy=0.3118, kl_div=-0.0306
  Round 4/5: Mean predicted reward = 10.068
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9722, entropy=0.3325, kl_div=0.0000
    Epoch 1: policy_loss=-0.0385, value_loss=0.9722, entropy=0.3334, kl_div=-0.0288
  Round 5/5: Mean predicted reward = 10.588

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 74 Results ---
  Mean Oracle Reward: 10.605
  Min Oracle Reward: 4.893
  Max Oracle Reward: 13.605
  Std Oracle Reward: 1.840
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.286, Max: 0.360, Count: 13
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

--- Generated Sequences (Diversity: 0.969) ---
  GATGGCCAGCCT
  GGCTAATGGCCC
  ACGTGGACTCCG
  AGCGCTTGGCCA
  CACCTCTAGGGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.987
  Max reward: 12.571
  With intrinsic bonuses: 10.953

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9731, entropy=0.3369, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9918

=== Surrogate Model Training ===
Total samples: 2450

Training on 2355 samples (removed 95 outliers)
Reward range: [7.26, 13.42], mean: 10.39
  Created 13 candidate models for data size 2355
Current R2 threshold: 0.35000000000000003
  rf-tuned-l: R2 = 0.334 (std: 0.102)
  rf-tuned-xl: R2 = 0.327 (std: 0.111)
  gb-tuned-l: R2 = 0.305 (std: 0.073)
  gb-tuned-xl: R2 = 0.305 (std: 0.073)
  xgb-xl: R2 = 0.333 (std: 0.142)
  xgb-l: R2 = 0.333 (std: 0.142)
  mlp-adaptive-xl: R2 = 0.309 (std: 0.130)
  mlp-l: R2 = 0.294 (std: 0.141)
  svr-rbf-xl: R2 = 0.368 (std: 0.102)
  svr-poly-l: R2 = 0.368 (std: 0.102)
  knn-tuned-sqrt: R2 = 0.246 (std: 0.109)
  knn-tuned-l: R2 = 0.246 (std: 0.109)
  ridge: R2 = 0.074 (std: 0.096)

Model-based training with 2 models
Best R2: 0.368, Mean R2: 0.295
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=0.3147, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1700
  Round 1/5: Mean predicted reward = 9.369
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9700, entropy=0.2772, kl_div=0.0000
    Epoch 1: policy_loss=0.1617, value_loss=0.9700, entropy=0.2674, kl_div=-0.2123
  Round 2/5: Mean predicted reward = 9.749
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9752, entropy=0.2949, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4143
  Round 3/5: Mean predicted reward = 10.402
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9729, entropy=0.2859, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3886
  Round 4/5: Mean predicted reward = 10.219
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9727, entropy=0.2778, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7183
  Round 5/5: Mean predicted reward = 10.329

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 75 Results ---
  Mean Oracle Reward: 10.972
  Min Oracle Reward: 8.217
  Max Oracle Reward: 12.669
  Std Oracle Reward: 1.099
  Sequence Diversity: 0.969
  Models Used: 2
  Model R2 - Mean: 0.295, Max: 0.368, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 2450

======================================================================
EXPERIMENT ROUND 76/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2450
  Consistent improvement, increasing LR to 0.000327

--- Round 76 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCGGCTCGATCA
  CTCCGGGACTAG
  CCGAAGCCGGTT
  GACTCTCGAGCG
  AGAAGCCTCGGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.105
  Max reward: 11.547
  With intrinsic bonuses: 10.102

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9753, entropy=0.2677, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7366

=== Surrogate Model Training ===
Total samples: 2482

Training on 2385 samples (removed 97 outliers)
Reward range: [7.27, 13.42], mean: 10.39
  Created 13 candidate models for data size 2385
Current R2 threshold: 0.36000000000000004
  rf-tuned-l: R2 = 0.324 (std: 0.119)
  rf-tuned-xl: R2 = 0.325 (std: 0.113)
  gb-tuned-l: R2 = 0.292 (std: 0.079)
  gb-tuned-xl: R2 = 0.292 (std: 0.079)
  xgb-xl: R2 = 0.329 (std: 0.131)
  xgb-l: R2 = 0.329 (std: 0.131)
  mlp-adaptive-xl: R2 = 0.312 (std: 0.119)
  mlp-l: R2 = 0.297 (std: 0.141)
  svr-rbf-xl: R2 = 0.367 (std: 0.107)
  svr-poly-l: R2 = 0.367 (std: 0.107)
  knn-tuned-sqrt: R2 = 0.244 (std: 0.107)
  knn-tuned-l: R2 = 0.244 (std: 0.107)
  ridge: R2 = 0.072 (std: 0.101)

Model-based training with 2 models
Best R2: 0.367, Mean R2: 0.292
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9704, entropy=0.2759, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3391
  Round 1/5: Mean predicted reward = 9.892
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9707, entropy=0.2903, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1412
  Round 2/5: Mean predicted reward = 10.092
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9724, entropy=0.2589, kl_div=0.0000
    Epoch 1: policy_loss=0.1369, value_loss=0.9724, entropy=0.2586, kl_div=-0.0217
  Round 3/5: Mean predicted reward = 10.282
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9721, entropy=0.2548, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8329
  Round 4/5: Mean predicted reward = 10.402
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9728, entropy=0.2630, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6089
  Round 5/5: Mean predicted reward = 10.309

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 76 Results ---
  Mean Oracle Reward: 10.107
  Min Oracle Reward: 4.080
  Max Oracle Reward: 11.649
  Std Oracle Reward: 1.285
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.292, Max: 0.367, Count: 13
  Total Sequences Evaluated: 2482

======================================================================
EXPERIMENT ROUND 77/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2482

--- Round 77 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGCGGCCTGATA
  GTCGTGACAGCC
  TGGGGCACACTC
  GGTCCGCCGAAT
  CTAGTACGGCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.077
  Max reward: 12.576
  With intrinsic bonuses: 10.032

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9706, entropy=0.2581, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3447

=== Surrogate Model Training ===
Total samples: 2514

Training on 2412 samples (removed 102 outliers)
Reward range: [7.29, 13.37], mean: 10.40
  Created 13 candidate models for data size 2412
Current R2 threshold: 0.37000000000000005
  rf-tuned-l: R2 = 0.322 (std: 0.116)
  rf-tuned-xl: R2 = 0.326 (std: 0.109)
  gb-tuned-l: R2 = 0.296 (std: 0.076)
  gb-tuned-xl: R2 = 0.296 (std: 0.076)
  xgb-xl: R2 = 0.307 (std: 0.135)
  xgb-l: R2 = 0.307 (std: 0.135)
  mlp-adaptive-xl: R2 = 0.301 (std: 0.134)
  mlp-l: R2 = 0.293 (std: 0.111)
  svr-rbf-xl: R2 = 0.361 (std: 0.107)
  svr-poly-l: R2 = 0.361 (std: 0.107)
  knn-tuned-sqrt: R2 = 0.237 (std: 0.103)
  knn-tuned-l: R2 = 0.237 (std: 0.103)
  ridge: R2 = 0.072 (std: 0.092)
  Fallback: Using svr-rbf-xl with R2 = 0.361

Model-based training with 1 models
Best R2: 0.361, Mean R2: 0.286
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9702, entropy=0.2476, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1708
  Round 1/5: Mean predicted reward = 10.116
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9717, entropy=0.2185, kl_div=0.0000
    Epoch 1: policy_loss=-0.0294, value_loss=0.9717, entropy=0.2194, kl_div=-0.0313
  Round 2/5: Mean predicted reward = 10.124
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9724, entropy=0.2350, kl_div=0.0000
    Epoch 1: policy_loss=-0.0301, value_loss=0.9724, entropy=0.2364, kl_div=-0.0540
  Round 3/5: Mean predicted reward = 10.079
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9732, entropy=0.2344, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2969
  Round 4/5: Mean predicted reward = 10.257
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9706, entropy=0.2497, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3947
  Round 5/5: Mean predicted reward = 10.146

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 77 Results ---
  Mean Oracle Reward: 10.093
  Min Oracle Reward: 4.101
  Max Oracle Reward: 12.588
  Std Oracle Reward: 1.447
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.286, Max: 0.361, Count: 13
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
  CGGCACTGACGT
  CGTCCGGCGAAT
  GTCCCTGGCAGA
  TCGCCAGTGGAC
  TCACTCGGACGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.351
  Max reward: 12.354
  With intrinsic bonuses: 10.354

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9706, entropy=0.2325, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2940

=== Surrogate Model Training ===
Total samples: 2546

Training on 2442 samples (removed 104 outliers)
Reward range: [7.30, 13.34], mean: 10.40
  Created 13 candidate models for data size 2442
Current R2 threshold: 0.38000000000000006
  rf-tuned-l: R2 = 0.329 (std: 0.111)
  rf-tuned-xl: R2 = 0.335 (std: 0.111)
  gb-tuned-l: R2 = 0.298 (std: 0.073)
  gb-tuned-xl: R2 = 0.298 (std: 0.073)
  xgb-xl: R2 = 0.324 (std: 0.128)
  xgb-l: R2 = 0.324 (std: 0.128)
  mlp-adaptive-xl: R2 = 0.293 (std: 0.100)
  mlp-l: R2 = 0.308 (std: 0.115)
  svr-rbf-xl: R2 = 0.359 (std: 0.107)
  svr-poly-l: R2 = 0.359 (std: 0.107)
  knn-tuned-sqrt: R2 = 0.232 (std: 0.101)
  knn-tuned-l: R2 = 0.232 (std: 0.101)
  ridge: R2 = 0.074 (std: 0.091)
  Fallback: Using svr-rbf-xl with R2 = 0.359

Model-based training with 1 models
Best R2: 0.359, Mean R2: 0.289
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.2244, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0627
  Round 1/5: Mean predicted reward = 9.634
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2390, kl_div=0.0000
    Epoch 1: policy_loss=-0.0268, value_loss=0.9687, entropy=0.2400, kl_div=0.0146
  Round 2/5: Mean predicted reward = 10.050
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2466, kl_div=0.0000
    Epoch 1: policy_loss=-0.0538, value_loss=0.9689, entropy=0.2496, kl_div=-0.1242
  Round 3/5: Mean predicted reward = 9.934
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.2592, kl_div=0.0000
    Epoch 1: policy_loss=-0.0343, value_loss=0.9692, entropy=0.2623, kl_div=-0.1578
  Round 4/5: Mean predicted reward = 10.351
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9718, entropy=0.2641, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0886
  Round 5/5: Mean predicted reward = 10.311

  === Progress Analysis ===
  Status: NORMAL

--- Round 78 Results ---
  Mean Oracle Reward: 10.375
  Min Oracle Reward: 8.185
  Max Oracle Reward: 12.704
  Std Oracle Reward: 0.875
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.289, Max: 0.359, Count: 13
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

--- Generated Sequences (Diversity: 0.969) ---
  GCTAGGTCGACC
  CATGGTCGCCAG
  GACTGCGCCGAT
  GCGAGTCACCGT
  CATGTCGGCCGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.195
  Max reward: 12.063
  With intrinsic bonuses: 10.188

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9738, entropy=0.2516, kl_div=0.0000
    Epoch 1: policy_loss=-0.0254, value_loss=0.9738, entropy=0.2514, kl_div=0.0047

=== Surrogate Model Training ===
Total samples: 2578

Training on 2473 samples (removed 105 outliers)
Reward range: [7.30, 13.34], mean: 10.39
  Created 13 candidate models for data size 2473
Current R2 threshold: 0.39000000000000007
  rf-tuned-l: R2 = 0.343 (std: 0.102)
  rf-tuned-xl: R2 = 0.339 (std: 0.109)
  gb-tuned-l: R2 = 0.305 (std: 0.079)
  gb-tuned-xl: R2 = 0.305 (std: 0.079)
  xgb-xl: R2 = 0.327 (std: 0.120)
  xgb-l: R2 = 0.327 (std: 0.120)
  mlp-adaptive-xl: R2 = 0.328 (std: 0.131)
  mlp-l: R2 = 0.316 (std: 0.114)
  svr-rbf-xl: R2 = 0.369 (std: 0.110)
  svr-poly-l: R2 = 0.369 (std: 0.110)
  knn-tuned-sqrt: R2 = 0.238 (std: 0.101)
  knn-tuned-l: R2 = 0.238 (std: 0.101)
  ridge: R2 = 0.082 (std: 0.091)
  Fallback: Using svr-rbf-xl with R2 = 0.369

Model-based training with 1 models
Best R2: 0.369, Mean R2: 0.299
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9709, entropy=0.2440, kl_div=0.0000
    Epoch 1: policy_loss=-0.0446, value_loss=0.9709, entropy=0.2446, kl_div=-0.0349
  Round 1/5: Mean predicted reward = 9.553
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9710, entropy=0.2492, kl_div=0.0000
    Epoch 1: policy_loss=-0.0485, value_loss=0.9710, entropy=0.2511, kl_div=-0.1388
  Round 2/5: Mean predicted reward = 9.904
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9714, entropy=0.2289, kl_div=0.0000
    Epoch 1: policy_loss=-0.0280, value_loss=0.9714, entropy=0.2303, kl_div=-0.1255
  Round 3/5: Mean predicted reward = 9.993
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.2539, kl_div=0.0000
    Epoch 1: policy_loss=-0.0188, value_loss=0.9697, entropy=0.2551, kl_div=-0.0576
  Round 4/5: Mean predicted reward = 10.146
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9724, entropy=0.2345, kl_div=0.0000
    Epoch 1: policy_loss=-0.0142, value_loss=0.9724, entropy=0.2347, kl_div=0.0275
  Round 5/5: Mean predicted reward = 10.270

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 79 Results ---
  Mean Oracle Reward: 10.168
  Min Oracle Reward: 5.307
  Max Oracle Reward: 12.166
  Std Oracle Reward: 1.386
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.299, Max: 0.369, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  ACGTGCTGCGAC
  GGCGGCCTACTA
  CGTGGCAGTACC
  CGGGCTAGCTAC
  CCCGTTAGCGGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.450
  Max reward: 12.132
  With intrinsic bonuses: 10.395

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.2509, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3042

=== Surrogate Model Training ===
Total samples: 2610

Training on 2503 samples (removed 107 outliers)
Reward range: [7.33, 13.34], mean: 10.40
  Created 13 candidate models for data size 2503
Current R2 threshold: 0.4000000000000001
  rf-tuned-l: R2 = 0.339 (std: 0.109)
  rf-tuned-xl: R2 = 0.337 (std: 0.114)
  gb-tuned-l: R2 = 0.310 (std: 0.086)
  gb-tuned-xl: R2 = 0.310 (std: 0.086)
  xgb-xl: R2 = 0.313 (std: 0.113)
  xgb-l: R2 = 0.313 (std: 0.113)
  mlp-adaptive-xl: R2 = 0.291 (std: 0.114)
  mlp-l: R2 = 0.292 (std: 0.113)
  svr-rbf-xl: R2 = 0.369 (std: 0.105)
  svr-poly-l: R2 = 0.369 (std: 0.105)
  knn-tuned-sqrt: R2 = 0.246 (std: 0.100)
  knn-tuned-l: R2 = 0.246 (std: 0.100)
  ridge: R2 = 0.087 (std: 0.092)
  Fallback: Using svr-rbf-xl with R2 = 0.369

Model-based training with 1 models
Best R2: 0.369, Mean R2: 0.294
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2315, kl_div=0.0000
    Epoch 1: policy_loss=-0.0509, value_loss=0.9689, entropy=0.2334, kl_div=-0.1193
  Round 1/5: Mean predicted reward = 9.879
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9703, entropy=0.2763, kl_div=0.0000
    Epoch 1: policy_loss=0.0074, value_loss=0.9703, entropy=0.2827, kl_div=-0.3344
  Round 2/5: Mean predicted reward = 10.017
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9713, entropy=0.2573, kl_div=0.0000
    Epoch 1: policy_loss=-0.0051, value_loss=0.9712, entropy=0.2551, kl_div=-0.0144
  Round 3/5: Mean predicted reward = 10.268
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9711, entropy=0.2247, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3406
  Round 4/5: Mean predicted reward = 10.134
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9711, entropy=0.2351, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5268
  Round 5/5: Mean predicted reward = 10.360

  === Progress Analysis ===
  Status: NORMAL

--- Round 80 Results ---
  Mean Oracle Reward: 10.491
  Min Oracle Reward: 8.689
  Max Oracle Reward: 12.350
  Std Oracle Reward: 0.801
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.294, Max: 0.369, Count: 13
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

--- Generated Sequences (Diversity: 0.969) ---
  TCCCGGATAGGC
  CACGGCACGTGT
  CGGTGACATCGC
  AACTGGTGCCGC
  CCGACGGTGATC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.304
  Max reward: 12.082
  With intrinsic bonuses: 10.294

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9710, entropy=0.2444, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4033

=== Surrogate Model Training ===
Total samples: 2642

Training on 2533 samples (removed 109 outliers)
Reward range: [7.33, 13.33], mean: 10.40
  Created 13 candidate models for data size 2533
Current R2 threshold: 0.41
  rf-tuned-l: R2 = 0.336 (std: 0.109)
  rf-tuned-xl: R2 = 0.345 (std: 0.106)
  gb-tuned-l: R2 = 0.306 (std: 0.076)
  gb-tuned-xl: R2 = 0.306 (std: 0.076)
  xgb-xl: R2 = 0.332 (std: 0.120)
  xgb-l: R2 = 0.332 (std: 0.120)
  mlp-adaptive-xl: R2 = 0.311 (std: 0.089)
  mlp-l: R2 = 0.317 (std: 0.090)
  svr-rbf-xl: R2 = 0.368 (std: 0.099)
  svr-poly-l: R2 = 0.368 (std: 0.099)
  knn-tuned-sqrt: R2 = 0.247 (std: 0.091)
  knn-tuned-l: R2 = 0.247 (std: 0.091)
  ridge: R2 = 0.090 (std: 0.088)
  Fallback: Using svr-rbf-xl with R2 = 0.368

Model-based training with 1 models
Best R2: 0.368, Mean R2: 0.300
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.2265, kl_div=0.0000
    Epoch 1: policy_loss=0.0186, value_loss=0.9698, entropy=0.2249, kl_div=0.0406
  Round 1/5: Mean predicted reward = 10.010
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9716, entropy=0.2236, kl_div=0.0000
    Epoch 1: policy_loss=-0.0003, value_loss=0.9715, entropy=0.2250, kl_div=-0.0834
  Round 2/5: Mean predicted reward = 10.004
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.2323, kl_div=0.0000
    Epoch 1: policy_loss=-0.0450, value_loss=0.9701, entropy=0.2328, kl_div=-0.1286
  Round 3/5: Mean predicted reward = 9.803
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=0.2294, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2286
  Round 4/5: Mean predicted reward = 10.213
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.2407, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3353
  Round 5/5: Mean predicted reward = 10.440

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 81 Results ---
  Mean Oracle Reward: 10.267
  Min Oracle Reward: 5.505
  Max Oracle Reward: 12.402
  Std Oracle Reward: 1.155
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.300, Max: 0.368, Count: 13
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

--- Generated Sequences (Diversity: 0.938) ---
  CGTGAAGTGCCC
  TCAGCGTACGGC
  GCCGGAGTCTCA
  GACACGGCGTTC
  TGTCGGAACCGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.203
  Max reward: 11.655
  With intrinsic bonuses: 10.291

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9707, entropy=0.2109, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3055

=== Surrogate Model Training ===
Total samples: 2674

Training on 2563 samples (removed 111 outliers)
Reward range: [7.35, 13.33], mean: 10.40
  Created 13 candidate models for data size 2563
Current R2 threshold: 0.42
  rf-tuned-l: R2 = 0.337 (std: 0.098)
  rf-tuned-xl: R2 = 0.339 (std: 0.106)
  gb-tuned-l: R2 = 0.307 (std: 0.075)
  gb-tuned-xl: R2 = 0.307 (std: 0.075)
  xgb-xl: R2 = 0.321 (std: 0.091)
  xgb-l: R2 = 0.321 (std: 0.091)
  mlp-adaptive-xl: R2 = 0.301 (std: 0.116)
  mlp-l: R2 = 0.305 (std: 0.106)
  svr-rbf-xl: R2 = 0.364 (std: 0.093)
  svr-poly-l: R2 = 0.364 (std: 0.093)
  knn-tuned-sqrt: R2 = 0.246 (std: 0.081)
  knn-tuned-l: R2 = 0.246 (std: 0.081)
  ridge: R2 = 0.090 (std: 0.087)
  Fallback: Using svr-rbf-xl with R2 = 0.364

Model-based training with 1 models
Best R2: 0.364, Mean R2: 0.296
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.1986, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0891
  Round 1/5: Mean predicted reward = 9.486
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9711, entropy=0.2127, kl_div=0.0000
    Epoch 1: policy_loss=-0.0386, value_loss=0.9711, entropy=0.2180, kl_div=-0.1367
  Round 2/5: Mean predicted reward = 9.798
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9728, entropy=0.2255, kl_div=0.0000
    Epoch 1: policy_loss=0.0497, value_loss=0.9728, entropy=0.2278, kl_div=-0.3025
  Round 3/5: Mean predicted reward = 9.876
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.2635, kl_div=0.0000
    Epoch 1: policy_loss=-0.0978, value_loss=0.9701, entropy=0.2651, kl_div=-0.2112
  Round 4/5: Mean predicted reward = 10.127
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9715, entropy=0.2615, kl_div=0.0000
    Epoch 1: policy_loss=-0.0041, value_loss=0.9715, entropy=0.2585, kl_div=-0.0372
  Round 5/5: Mean predicted reward = 10.363

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 82 Results ---
  Mean Oracle Reward: 10.209
  Min Oracle Reward: 6.015
  Max Oracle Reward: 11.593
  Std Oracle Reward: 1.188
  Sequence Diversity: 0.938
  Models Used: 1
  Model R2 - Mean: 0.296, Max: 0.364, Count: 13
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
  GCCTAGCGTGAC
  CGCAGCGTCATG
  GCCGGGCTATAA
  GTCGCCAGTGCA
  TCCACTGGCGAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.085
  Max reward: 11.833
  With intrinsic bonuses: 10.090

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9722, entropy=0.2268, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0635

=== Surrogate Model Training ===
Total samples: 2706

Training on 2596 samples (removed 110 outliers)
Reward range: [7.33, 13.34], mean: 10.40
  Created 13 candidate models for data size 2596
Current R2 threshold: 0.43
  rf-tuned-l: R2 = 0.334 (std: 0.110)
  rf-tuned-xl: R2 = 0.339 (std: 0.107)
  gb-tuned-l: R2 = 0.313 (std: 0.079)
  gb-tuned-xl: R2 = 0.313 (std: 0.079)
  xgb-xl: R2 = 0.324 (std: 0.111)
  xgb-l: R2 = 0.324 (std: 0.111)
  mlp-adaptive-xl: R2 = 0.312 (std: 0.104)
  mlp-l: R2 = 0.296 (std: 0.105)
  svr-rbf-xl: R2 = 0.363 (std: 0.093)
  svr-poly-l: R2 = 0.363 (std: 0.093)
  knn-tuned-sqrt: R2 = 0.249 (std: 0.081)
  knn-tuned-l: R2 = 0.249 (std: 0.081)
  ridge: R2 = 0.093 (std: 0.091)
  Fallback: Using svr-rbf-xl with R2 = 0.363

Model-based training with 1 models
Best R2: 0.363, Mean R2: 0.298
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.2316, kl_div=0.0000
    Epoch 1: policy_loss=-0.0703, value_loss=0.9698, entropy=0.2319, kl_div=-0.1157
  Round 1/5: Mean predicted reward = 9.632
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.2247, kl_div=0.0000
    Epoch 1: policy_loss=-0.0186, value_loss=0.9691, entropy=0.2267, kl_div=-0.1787
  Round 2/5: Mean predicted reward = 10.033
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2364, kl_div=0.0000
    Epoch 1: policy_loss=-0.0199, value_loss=0.9687, entropy=0.2379, kl_div=-0.1701
  Round 3/5: Mean predicted reward = 10.178
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.2398, kl_div=0.0000
    Epoch 1: policy_loss=-0.0809, value_loss=0.9691, entropy=0.2416, kl_div=-0.0251
  Round 4/5: Mean predicted reward = 10.027
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9700, entropy=0.2751, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1811
  Round 5/5: Mean predicted reward = 10.523

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 83 Results ---
  Mean Oracle Reward: 10.104
  Min Oracle Reward: 2.361
  Max Oracle Reward: 12.568
  Std Oracle Reward: 1.755
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.298, Max: 0.363, Count: 13
  Total Sequences Evaluated: 2706

======================================================================
EXPERIMENT ROUND 84/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2706
  Performance plateaued, reducing LR to 0.000019

--- Round 84 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  TCCGCATGGAGC
  TTCCGCAGGCAG
  TTGGAACGCCCG
  CGTCACATGCGG
  CCCGATCATGGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.337
  Max reward: 12.702
  With intrinsic bonuses: 10.299

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=0.2388, kl_div=0.0000
    Epoch 1: policy_loss=-0.0071, value_loss=0.9709, entropy=0.2390, kl_div=0.0191

=== Surrogate Model Training ===
Total samples: 2738

Training on 2626 samples (removed 112 outliers)
Reward range: [7.33, 13.34], mean: 10.40
  Created 13 candidate models for data size 2626
Current R2 threshold: 0.44
  rf-tuned-l: R2 = 0.341 (std: 0.100)
  rf-tuned-xl: R2 = 0.344 (std: 0.100)
  gb-tuned-l: R2 = 0.314 (std: 0.083)
  gb-tuned-xl: R2 = 0.314 (std: 0.083)
  xgb-xl: R2 = 0.328 (std: 0.095)
  xgb-l: R2 = 0.328 (std: 0.095)
  mlp-adaptive-xl: R2 = 0.309 (std: 0.094)
  mlp-l: R2 = 0.322 (std: 0.098)
  svr-rbf-xl: R2 = 0.372 (std: 0.092)
  svr-poly-l: R2 = 0.372 (std: 0.092)
  knn-tuned-sqrt: R2 = 0.241 (std: 0.080)
  knn-tuned-l: R2 = 0.241 (std: 0.080)
  ridge: R2 = 0.092 (std: 0.091)
  Fallback: Using svr-rbf-xl with R2 = 0.372

Model-based training with 1 models
Best R2: 0.372, Mean R2: 0.301
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.2323, kl_div=0.0000
    Epoch 1: policy_loss=-0.0067, value_loss=0.9692, entropy=0.2330, kl_div=-0.0074
  Round 1/5: Mean predicted reward = 9.330
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.2572, kl_div=0.0000
    Epoch 1: policy_loss=-0.0215, value_loss=0.9703, entropy=0.2582, kl_div=-0.0257
  Round 2/5: Mean predicted reward = 9.855
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9707, entropy=0.2521, kl_div=0.0000
    Epoch 1: policy_loss=-0.0396, value_loss=0.9707, entropy=0.2536, kl_div=-0.0697
  Round 3/5: Mean predicted reward = 9.846
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=0.2637, kl_div=0.0000
    Epoch 1: policy_loss=0.0063, value_loss=0.9709, entropy=0.2645, kl_div=-0.0389
  Round 4/5: Mean predicted reward = 10.004
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9711, entropy=0.2618, kl_div=0.0000
    Epoch 1: policy_loss=-0.0031, value_loss=0.9711, entropy=0.2625, kl_div=-0.0208
  Round 5/5: Mean predicted reward = 10.333

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 84 Results ---
  Mean Oracle Reward: 10.313
  Min Oracle Reward: 6.697
  Max Oracle Reward: 12.320
  Std Oracle Reward: 1.409
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.301, Max: 0.372, Count: 13
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
  TACACGTCCGGG
  GCAGCGTTACGA
  CGGTCGATAGCC
  TGCGCACCAGTG
  GCGACCAGGTCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.554
  Max reward: 12.368
  With intrinsic bonuses: 10.543

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.2647, kl_div=0.0000
    Epoch 1: policy_loss=-0.0465, value_loss=0.9703, entropy=0.2702, kl_div=-0.0312

=== Surrogate Model Training ===
Total samples: 2770

Training on 2658 samples (removed 112 outliers)
Reward range: [7.33, 13.34], mean: 10.40
  Created 13 candidate models for data size 2658
Current R2 threshold: 0.45
  rf-tuned-l: R2 = 0.346 (std: 0.092)
  rf-tuned-xl: R2 = 0.342 (std: 0.095)
  gb-tuned-l: R2 = 0.313 (std: 0.074)
  gb-tuned-xl: R2 = 0.313 (std: 0.074)
  xgb-xl: R2 = 0.312 (std: 0.103)
  xgb-l: R2 = 0.312 (std: 0.103)
  mlp-adaptive-xl: R2 = 0.299 (std: 0.108)
  mlp-l: R2 = 0.320 (std: 0.096)
  svr-rbf-xl: R2 = 0.370 (std: 0.089)
  svr-poly-l: R2 = 0.370 (std: 0.089)
  knn-tuned-sqrt: R2 = 0.242 (std: 0.075)
  knn-tuned-l: R2 = 0.242 (std: 0.075)
  ridge: R2 = 0.090 (std: 0.084)
  Fallback: Using svr-rbf-xl with R2 = 0.370

Model-based training with 1 models
Best R2: 0.370, Mean R2: 0.298
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.2570, kl_div=0.0000
    Epoch 1: policy_loss=-0.0413, value_loss=0.9701, entropy=0.2581, kl_div=-0.3788
  Round 1/5: Mean predicted reward = 9.501
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.2368, kl_div=0.0000
    Epoch 1: policy_loss=-0.0056, value_loss=0.9691, entropy=0.2358, kl_div=-0.2223
  Round 2/5: Mean predicted reward = 9.696
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9717, entropy=0.2406, kl_div=0.0000
    Epoch 1: policy_loss=-0.0190, value_loss=0.9716, entropy=0.2416, kl_div=-0.2246
  Round 3/5: Mean predicted reward = 10.121
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9715, entropy=0.2373, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2770
  Round 4/5: Mean predicted reward = 10.171
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9712, entropy=0.2563, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2411
  Round 5/5: Mean predicted reward = 10.419

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 85 Results ---
  Mean Oracle Reward: 10.603
  Min Oracle Reward: 8.593
  Max Oracle Reward: 12.227
  Std Oracle Reward: 0.830
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.298, Max: 0.370, Count: 13
  Total Sequences Evaluated: 2770

======================================================================
EXPERIMENT ROUND 86/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2770
  Consistent improvement, increasing LR to 0.000327

--- Round 86 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  AGGTCGCCACTG
  TCAGACTCGGGC
  AGGTGCTCCGCA
  CGGCCTTCGAGA
  ACTCGGACCGTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.086
  Max reward: 12.475
  With intrinsic bonuses: 10.086

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=0.2230, kl_div=0.0000
    Epoch 1: policy_loss=-0.0321, value_loss=0.9678, entropy=0.2227, kl_div=0.0475

=== Surrogate Model Training ===
Total samples: 2802

Training on 2687 samples (removed 115 outliers)
Reward range: [7.33, 13.34], mean: 10.40
  Created 13 candidate models for data size 2687
Current R2 threshold: 0.46
  rf-tuned-l: R2 = 0.343 (std: 0.091)
  rf-tuned-xl: R2 = 0.343 (std: 0.094)
  gb-tuned-l: R2 = 0.308 (std: 0.075)
  gb-tuned-xl: R2 = 0.308 (std: 0.075)
  xgb-xl: R2 = 0.314 (std: 0.098)
  xgb-l: R2 = 0.314 (std: 0.098)
  mlp-adaptive-xl: R2 = 0.311 (std: 0.101)
  mlp-l: R2 = 0.315 (std: 0.089)
  svr-rbf-xl: R2 = 0.364 (std: 0.084)
  svr-poly-l: R2 = 0.364 (std: 0.084)
  knn-tuned-sqrt: R2 = 0.238 (std: 0.067)
  knn-tuned-l: R2 = 0.238 (std: 0.067)
  ridge: R2 = 0.087 (std: 0.083)
  Fallback: Using svr-rbf-xl with R2 = 0.364

Model-based training with 1 models
Best R2: 0.364, Mean R2: 0.296
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.2365, kl_div=0.0000
    Epoch 1: policy_loss=-0.1176, value_loss=0.9703, entropy=0.2456, kl_div=-0.2304
  Round 1/5: Mean predicted reward = 9.494
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.2489, kl_div=0.0000
    Epoch 1: policy_loss=0.1141, value_loss=0.9696, entropy=0.2540, kl_div=-0.4927
  Round 2/5: Mean predicted reward = 9.837
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.2528, kl_div=0.0000
    Epoch 1: policy_loss=-0.0803, value_loss=0.9705, entropy=0.2531, kl_div=-0.1668
  Round 3/5: Mean predicted reward = 10.014
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9711, entropy=0.2541, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3247
  Round 4/5: Mean predicted reward = 10.203
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9702, entropy=0.2580, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5795
  Round 5/5: Mean predicted reward = 10.305

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 86 Results ---
  Mean Oracle Reward: 10.078
  Min Oracle Reward: 3.361
  Max Oracle Reward: 12.395
  Std Oracle Reward: 1.721
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.296, Max: 0.364, Count: 13
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

--- Generated Sequences (Diversity: 0.938) ---
  CGCTGGACAGTC
  CGGACGTGTACC
  TGCGGCTCAACG
  GGGAACTGTCAC
  GGGATTCCACGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.534
  Max reward: 12.634
  With intrinsic bonuses: 10.567

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9703, entropy=0.2345, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5783

=== Surrogate Model Training ===
Total samples: 2834

Training on 2717 samples (removed 117 outliers)
Reward range: [7.35, 13.34], mean: 10.41
  Created 13 candidate models for data size 2717
Current R2 threshold: 0.47000000000000003
  rf-tuned-l: R2 = 0.339 (std: 0.093)
  rf-tuned-xl: R2 = 0.341 (std: 0.093)
  gb-tuned-l: R2 = 0.297 (std: 0.064)
  gb-tuned-xl: R2 = 0.297 (std: 0.064)
  xgb-xl: R2 = 0.338 (std: 0.095)
  xgb-l: R2 = 0.338 (std: 0.095)
  mlp-adaptive-xl: R2 = 0.301 (std: 0.081)
  mlp-l: R2 = 0.314 (std: 0.107)
  svr-rbf-xl: R2 = 0.359 (std: 0.077)
  svr-poly-l: R2 = 0.359 (std: 0.077)
  knn-tuned-sqrt: R2 = 0.236 (std: 0.067)
  knn-tuned-l: R2 = 0.236 (std: 0.067)
  ridge: R2 = 0.080 (std: 0.076)
  Fallback: Using svr-rbf-xl with R2 = 0.359

Model-based training with 1 models
Best R2: 0.359, Mean R2: 0.295
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.2648, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2993
  Round 1/5: Mean predicted reward = 9.874
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.2350, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3356
  Round 2/5: Mean predicted reward = 9.863
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.2242, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3162
  Round 3/5: Mean predicted reward = 9.818
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.2463, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1130
  Round 4/5: Mean predicted reward = 10.179
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.2266, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2124
  Round 5/5: Mean predicted reward = 10.203

  === Progress Analysis ===
  Status: NORMAL

--- Round 87 Results ---
  Mean Oracle Reward: 10.611
  Min Oracle Reward: 6.740
  Max Oracle Reward: 12.534
  Std Oracle Reward: 1.180
  Sequence Diversity: 0.938
  Models Used: 1
  Model R2 - Mean: 0.295, Max: 0.359, Count: 13
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
  CACGCCGTGTGA
  ATGCTCCGGGAC
  CGTGGGCTAACC
  TGCGCAGCGCAT
  AGCTGCGCGACT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.038
  Max reward: 12.207
  With intrinsic bonuses: 10.047

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2349, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1242

=== Surrogate Model Training ===
Total samples: 2866

Training on 2747 samples (removed 119 outliers)
Reward range: [7.35, 13.33], mean: 10.40
  Created 13 candidate models for data size 2747
Current R2 threshold: 0.48000000000000004
  rf-tuned-l: R2 = 0.334 (std: 0.091)
  rf-tuned-xl: R2 = 0.335 (std: 0.089)
  gb-tuned-l: R2 = 0.303 (std: 0.073)
  gb-tuned-xl: R2 = 0.303 (std: 0.073)
  xgb-xl: R2 = 0.327 (std: 0.087)
  xgb-l: R2 = 0.327 (std: 0.087)
  mlp-adaptive-xl: R2 = 0.315 (std: 0.115)
  mlp-l: R2 = 0.323 (std: 0.090)
  svr-rbf-xl: R2 = 0.355 (std: 0.076)
  svr-poly-l: R2 = 0.355 (std: 0.076)
  knn-tuned-sqrt: R2 = 0.231 (std: 0.066)
  knn-tuned-l: R2 = 0.231 (std: 0.066)
  ridge: R2 = 0.081 (std: 0.079)
  Fallback: Using svr-rbf-xl with R2 = 0.355

Model-based training with 1 models
Best R2: 0.355, Mean R2: 0.294
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.2476, kl_div=0.0000
    Epoch 1: policy_loss=-0.0061, value_loss=0.9697, entropy=0.2457, kl_div=0.0013
  Round 1/5: Mean predicted reward = 9.477
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.2473, kl_div=0.0000
    Epoch 1: policy_loss=-0.0494, value_loss=0.9692, entropy=0.2504, kl_div=-0.1284
  Round 2/5: Mean predicted reward = 9.816
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.2138, kl_div=0.0000
    Epoch 1: policy_loss=-0.0090, value_loss=0.9684, entropy=0.2171, kl_div=-0.2221
  Round 3/5: Mean predicted reward = 9.867
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9704, entropy=0.2216, kl_div=0.0000
    Epoch 1: policy_loss=-0.0264, value_loss=0.9704, entropy=0.2239, kl_div=-0.1065
  Round 4/5: Mean predicted reward = 10.094
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.2323, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1581
  Round 5/5: Mean predicted reward = 10.457

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 88 Results ---
  Mean Oracle Reward: 10.028
  Min Oracle Reward: 6.923
  Max Oracle Reward: 12.364
  Std Oracle Reward: 1.188
  Sequence Diversity: 0.938
  Models Used: 1
  Model R2 - Mean: 0.294, Max: 0.355, Count: 13
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
  CAGTCGGTAACG
  CGACCCGGATGT
  TCGACTCAGGGC
  CAATGCGGGTCC
  GGCTAACCTGGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.130
  Max reward: 12.200
  With intrinsic bonuses: 10.226

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9700, entropy=0.2285, kl_div=0.0000
    Epoch 1: policy_loss=-0.0052, value_loss=0.9700, entropy=0.2278, kl_div=0.0413

=== Surrogate Model Training ===
Total samples: 2898

Training on 2777 samples (removed 121 outliers)
Reward range: [7.35, 13.31], mean: 10.40
  Created 13 candidate models for data size 2777
Current R2 threshold: 0.49000000000000005
  rf-tuned-l: R2 = 0.326 (std: 0.086)
  rf-tuned-xl: R2 = 0.329 (std: 0.084)
  gb-tuned-l: R2 = 0.291 (std: 0.065)
  gb-tuned-xl: R2 = 0.291 (std: 0.065)
  xgb-xl: R2 = 0.315 (std: 0.069)
  xgb-l: R2 = 0.315 (std: 0.069)
  mlp-adaptive-xl: R2 = 0.288 (std: 0.100)
  mlp-l: R2 = 0.289 (std: 0.094)
  svr-rbf-xl: R2 = 0.345 (std: 0.069)
  svr-poly-l: R2 = 0.345 (std: 0.069)
  knn-tuned-sqrt: R2 = 0.219 (std: 0.065)
  knn-tuned-l: R2 = 0.219 (std: 0.065)
  ridge: R2 = 0.076 (std: 0.081)
  Fallback: Using svr-rbf-xl with R2 = 0.345

Model-based training with 1 models
Best R2: 0.345, Mean R2: 0.281
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.2281, kl_div=0.0000
    Epoch 1: policy_loss=-0.0139, value_loss=0.9694, entropy=0.2284, kl_div=-0.0187
  Round 1/5: Mean predicted reward = 9.645
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.2488, kl_div=0.0000
    Epoch 1: policy_loss=-0.0316, value_loss=0.9683, entropy=0.2502, kl_div=-0.0752
  Round 2/5: Mean predicted reward = 9.754
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9709, entropy=0.2405, kl_div=0.0000
    Epoch 1: policy_loss=-0.0479, value_loss=0.9709, entropy=0.2422, kl_div=-0.0875
  Round 3/5: Mean predicted reward = 9.642
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.2283, kl_div=0.0000
    Epoch 1: policy_loss=-0.0120, value_loss=0.9681, entropy=0.2301, kl_div=-0.0681
  Round 4/5: Mean predicted reward = 10.219
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2211, kl_div=0.0000
    Epoch 1: policy_loss=-0.0104, value_loss=0.9687, entropy=0.2219, kl_div=-0.0404
  Round 5/5: Mean predicted reward = 10.317

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 89 Results ---
  Mean Oracle Reward: 10.215
  Min Oracle Reward: 3.501
  Max Oracle Reward: 12.258
  Std Oracle Reward: 1.452
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.281, Max: 0.345, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  GCCAGGGACTTC
  ACTTGGGACCGC
  CGCAAGGTCATG
  TGCACCAGGTCG
  GGTCGTCCGAAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.094
  Max reward: 12.286
  With intrinsic bonuses: 10.121

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9699, entropy=0.2150, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1052

=== Surrogate Model Training ===
Total samples: 2930

Training on 2808 samples (removed 122 outliers)
Reward range: [7.35, 13.31], mean: 10.40
  Created 13 candidate models for data size 2808
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.324 (std: 0.089)
  rf-tuned-xl: R2 = 0.328 (std: 0.088)
  gb-tuned-l: R2 = 0.306 (std: 0.064)
  gb-tuned-xl: R2 = 0.306 (std: 0.064)
  xgb-xl: R2 = 0.290 (std: 0.076)
  xgb-l: R2 = 0.290 (std: 0.076)
  mlp-adaptive-xl: R2 = 0.292 (std: 0.081)
  mlp-l: R2 = 0.294 (std: 0.105)
  svr-rbf-xl: R2 = 0.346 (std: 0.069)
  svr-poly-l: R2 = 0.346 (std: 0.069)
  knn-tuned-sqrt: R2 = 0.203 (std: 0.062)
  knn-tuned-l: R2 = 0.203 (std: 0.062)
  ridge: R2 = 0.078 (std: 0.077)
  Fallback: Using svr-rbf-xl with R2 = 0.346

Model-based training with 1 models
Best R2: 0.346, Mean R2: 0.277
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.2392, kl_div=0.0000
    Epoch 1: policy_loss=-0.0393, value_loss=0.9694, entropy=0.2458, kl_div=-0.2202
  Round 1/5: Mean predicted reward = 9.509
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.2492, kl_div=0.0000
    Epoch 1: policy_loss=-0.0727, value_loss=0.9696, entropy=0.2605, kl_div=-0.5093
  Round 2/5: Mean predicted reward = 9.534
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.2754, kl_div=0.0000
    Epoch 1: policy_loss=-0.0069, value_loss=0.9699, entropy=0.2818, kl_div=-0.2967
  Round 3/5: Mean predicted reward = 10.072
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.2870, kl_div=0.0000
    Epoch 1: policy_loss=0.0321, value_loss=0.9701, entropy=0.2906, kl_div=-0.1395
  Round 4/5: Mean predicted reward = 10.305
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.2706, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1755
  Round 5/5: Mean predicted reward = 10.423

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 90 Results ---
  Mean Oracle Reward: 10.111
  Min Oracle Reward: 4.602
  Max Oracle Reward: 12.330
  Std Oracle Reward: 1.409
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.277, Max: 0.346, Count: 13
  Total Sequences Evaluated: 2930

======================================================================
EXPERIMENT ROUND 91/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2930
  Performance plateaued, reducing LR to 0.000136

--- Round 91 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  AGCCCGGATCGT
  TAGCCCCGGATG
  GGATCGCCCATG
  CTGACCGAGCTG
  TGCTGGCGAACC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.398
  Max reward: 12.579
  With intrinsic bonuses: 10.406

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.2737, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1610

=== Surrogate Model Training ===
Total samples: 2962

Training on 2839 samples (removed 123 outliers)
Reward range: [7.35, 13.31], mean: 10.40
  Created 13 candidate models for data size 2839
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.315 (std: 0.081)
  rf-tuned-xl: R2 = 0.320 (std: 0.085)
  gb-tuned-l: R2 = 0.301 (std: 0.069)
  gb-tuned-xl: R2 = 0.301 (std: 0.069)
  xgb-xl: R2 = 0.301 (std: 0.080)
  xgb-l: R2 = 0.301 (std: 0.080)
  mlp-adaptive-xl: R2 = 0.287 (std: 0.081)
  mlp-l: R2 = 0.293 (std: 0.076)
  svr-rbf-xl: R2 = 0.341 (std: 0.071)
  svr-poly-l: R2 = 0.341 (std: 0.071)
  knn-tuned-sqrt: R2 = 0.201 (std: 0.060)
  knn-tuned-l: R2 = 0.201 (std: 0.060)
  ridge: R2 = 0.078 (std: 0.076)
  Fallback: Using svr-rbf-xl with R2 = 0.341

Model-based training with 1 models
Best R2: 0.341, Mean R2: 0.276
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.2766, kl_div=0.0000
    Epoch 1: policy_loss=-0.0421, value_loss=0.9684, entropy=0.2775, kl_div=-0.0437
  Round 1/5: Mean predicted reward = 9.694
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.2581, kl_div=0.0000
    Epoch 1: policy_loss=-0.0546, value_loss=0.9691, entropy=0.2643, kl_div=-0.1396
  Round 2/5: Mean predicted reward = 9.861
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.2947, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0640
  Round 3/5: Mean predicted reward = 10.300
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.2765, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2057
  Round 4/5: Mean predicted reward = 9.965
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.3171, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3164
  Round 5/5: Mean predicted reward = 10.475

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 91 Results ---
  Mean Oracle Reward: 10.455
  Min Oracle Reward: 7.035
  Max Oracle Reward: 12.665
  Std Oracle Reward: 1.259
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.276, Max: 0.341, Count: 13
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
  CGCTGACGTACG
  CAGGCGCGTATC
  ACGCCTGAGCGT
  AGACCTACTGGG
  CATGCGTCGAGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.461
  Max reward: 12.627
  With intrinsic bonuses: 10.419

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.2925, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8052

=== Surrogate Model Training ===
Total samples: 2994

Training on 2870 samples (removed 124 outliers)
Reward range: [7.35, 13.31], mean: 10.40
  Created 13 candidate models for data size 2870
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.312 (std: 0.087)
  rf-tuned-xl: R2 = 0.315 (std: 0.084)
  gb-tuned-l: R2 = 0.297 (std: 0.061)
  gb-tuned-xl: R2 = 0.297 (std: 0.061)
  xgb-xl: R2 = 0.296 (std: 0.088)
  xgb-l: R2 = 0.296 (std: 0.088)
  mlp-adaptive-xl: R2 = 0.306 (std: 0.101)
  mlp-l: R2 = 0.294 (std: 0.092)
  svr-rbf-xl: R2 = 0.339 (std: 0.071)
  svr-poly-l: R2 = 0.339 (std: 0.071)
  knn-tuned-sqrt: R2 = 0.197 (std: 0.067)
  knn-tuned-l: R2 = 0.197 (std: 0.067)
  ridge: R2 = 0.074 (std: 0.069)
  Fallback: Using svr-rbf-xl with R2 = 0.339

Model-based training with 1 models
Best R2: 0.339, Mean R2: 0.274
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.2756, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4012
  Round 1/5: Mean predicted reward = 9.882
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.2596, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1616
  Round 2/5: Mean predicted reward = 9.926
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.2576, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1024
  Round 3/5: Mean predicted reward = 9.939
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.2114, kl_div=0.0000
    Epoch 1: policy_loss=-0.0095, value_loss=0.9694, entropy=0.2103, kl_div=0.0456
  Round 4/5: Mean predicted reward = 10.042
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2632, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1795
  Round 5/5: Mean predicted reward = 10.309

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 92 Results ---
  Mean Oracle Reward: 10.459
  Min Oracle Reward: 5.851
  Max Oracle Reward: 12.692
  Std Oracle Reward: 1.325
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.274, Max: 0.339, Count: 13
  Total Sequences Evaluated: 2994

======================================================================
EXPERIMENT ROUND 93/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2994
  Consistent improvement, increasing LR to 0.000132

--- Round 93 Configuration ---
Learning rate: 0.000132
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGCGCGCATATC
  AGGCCTACGCGT
  GAATACGCTGCG
  GGCCGTCCATGA
  TGTCCGACAGGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.744
  Max reward: 13.030
  With intrinsic bonuses: 10.757

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9695, entropy=0.2447, kl_div=0.0000
    Epoch 1: policy_loss=-0.0347, value_loss=0.9695, entropy=0.2455, kl_div=0.0252

=== Surrogate Model Training ===
Total samples: 3026

Training on 2902 samples (removed 124 outliers)
Reward range: [7.33, 13.34], mean: 10.41
  Created 13 candidate models for data size 2902
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.314 (std: 0.088)
  rf-tuned-xl: R2 = 0.305 (std: 0.082)
  gb-tuned-l: R2 = 0.292 (std: 0.062)
  gb-tuned-xl: R2 = 0.292 (std: 0.062)
  xgb-xl: R2 = 0.296 (std: 0.075)
  xgb-l: R2 = 0.296 (std: 0.075)
  mlp-adaptive-xl: R2 = 0.277 (std: 0.108)
  mlp-l: R2 = 0.285 (std: 0.110)
  svr-rbf-xl: R2 = 0.338 (std: 0.075)
  svr-poly-l: R2 = 0.338 (std: 0.075)
  knn-tuned-sqrt: R2 = 0.196 (std: 0.085)
  knn-tuned-l: R2 = 0.196 (std: 0.085)
  ridge: R2 = 0.071 (std: 0.080)
  Fallback: Using svr-rbf-xl with R2 = 0.338

Model-based training with 1 models
Best R2: 0.338, Mean R2: 0.269
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=0.2645, kl_div=0.0000
    Epoch 1: policy_loss=-0.0641, value_loss=0.9704, entropy=0.2725, kl_div=-0.2526
  Round 1/5: Mean predicted reward = 9.317
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.2414, kl_div=0.0000
    Epoch 1: policy_loss=-0.0449, value_loss=0.9694, entropy=0.2460, kl_div=-0.0905
  Round 2/5: Mean predicted reward = 9.590
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.2613, kl_div=0.0000
    Epoch 1: policy_loss=-0.0572, value_loss=0.9697, entropy=0.2636, kl_div=-0.1220
  Round 3/5: Mean predicted reward = 9.966
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.2682, kl_div=0.0000
    Epoch 1: policy_loss=-0.0382, value_loss=0.9691, entropy=0.2687, kl_div=-0.0378
  Round 4/5: Mean predicted reward = 10.316
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.2634, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1320
  Round 5/5: Mean predicted reward = 10.381

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 93 Results ---
  Mean Oracle Reward: 10.801
  Min Oracle Reward: 6.240
  Max Oracle Reward: 13.163
  Std Oracle Reward: 1.744
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.269, Max: 0.338, Count: 13
  Total Sequences Evaluated: 3026

======================================================================
EXPERIMENT ROUND 94/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 3026
  Consistent improvement, increasing LR to 0.000045

--- Round 94 Configuration ---
Learning rate: 0.000045
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTAAGCGCCGTC
  GGGCGTATCACC
  GCTCAGATGGCC
  TCGCGTAGCCGA
  CCCGAGCTATGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.553
  Max reward: 12.511
  With intrinsic bonuses: 10.565

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9682, entropy=0.2776, kl_div=0.0000
    Epoch 1: policy_loss=-0.0231, value_loss=0.9682, entropy=0.2763, kl_div=0.0478

=== Surrogate Model Training ===
Total samples: 3058

Training on 2934 samples (removed 124 outliers)
Reward range: [7.33, 13.37], mean: 10.42
  Created 13 candidate models for data size 2934
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.305 (std: 0.088)
  rf-tuned-xl: R2 = 0.306 (std: 0.088)
  gb-tuned-l: R2 = 0.292 (std: 0.060)
  gb-tuned-xl: R2 = 0.292 (std: 0.060)
  xgb-xl: R2 = 0.302 (std: 0.096)
  xgb-l: R2 = 0.302 (std: 0.096)
  mlp-adaptive-xl: R2 = 0.289 (std: 0.080)
  mlp-l: R2 = 0.291 (std: 0.083)
  svr-rbf-xl: R2 = 0.339 (std: 0.074)
  svr-poly-l: R2 = 0.339 (std: 0.074)
  knn-tuned-sqrt: R2 = 0.196 (std: 0.090)
  knn-tuned-l: R2 = 0.196 (std: 0.090)
  ridge: R2 = 0.072 (std: 0.082)
  Fallback: Using svr-rbf-xl with R2 = 0.339

Model-based training with 1 models
Best R2: 0.339, Mean R2: 0.271
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2497, kl_div=0.0000
    Epoch 1: policy_loss=0.0129, value_loss=0.9689, entropy=0.2490, kl_div=0.0201
  Round 1/5: Mean predicted reward = 9.536
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.2667, kl_div=0.0000
    Epoch 1: policy_loss=-0.0300, value_loss=0.9684, entropy=0.2662, kl_div=-0.0765
  Round 2/5: Mean predicted reward = 9.761
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.2597, kl_div=0.0000
    Epoch 1: policy_loss=-0.0364, value_loss=0.9683, entropy=0.2600, kl_div=-0.0554
  Round 3/5: Mean predicted reward = 9.957
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9699, entropy=0.2367, kl_div=0.0000
    Epoch 1: policy_loss=-0.0096, value_loss=0.9699, entropy=0.2376, kl_div=-0.0802
  Round 4/5: Mean predicted reward = 10.005
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.2641, kl_div=0.0000
    Epoch 1: policy_loss=-0.0152, value_loss=0.9692, entropy=0.2641, kl_div=-0.0505
  Round 5/5: Mean predicted reward = 10.306

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 94 Results ---
  Mean Oracle Reward: 10.589
  Min Oracle Reward: 5.620
  Max Oracle Reward: 12.678
  Std Oracle Reward: 1.447
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.271, Max: 0.339, Count: 13
  Total Sequences Evaluated: 3058

======================================================================
EXPERIMENT ROUND 95/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 3058

--- Round 95 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GAGGGCCATCCT
  AGGGCTCACTGC
  TACCGTCCGGAG
  GGGCCTGATCCA
  AGCTGCTGCGCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.778
  Max reward: 13.266
  With intrinsic bonuses: 10.798

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.2964, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0869

=== Surrogate Model Training ===
Total samples: 3090

Training on 2966 samples (removed 124 outliers)
Reward range: [7.33, 13.37], mean: 10.42
  Created 13 candidate models for data size 2966
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.317 (std: 0.102)
  rf-tuned-xl: R2 = 0.321 (std: 0.100)
  gb-tuned-l: R2 = 0.303 (std: 0.061)
  gb-tuned-xl: R2 = 0.303 (std: 0.061)
  xgb-xl: R2 = 0.317 (std: 0.109)
  xgb-l: R2 = 0.317 (std: 0.109)
  mlp-adaptive-xl: R2 = 0.293 (std: 0.097)
  mlp-l: R2 = 0.304 (std: 0.098)
  svr-rbf-xl: R2 = 0.351 (std: 0.080)
  svr-poly-l: R2 = 0.351 (std: 0.080)
  knn-tuned-sqrt: R2 = 0.211 (std: 0.101)
  knn-tuned-l: R2 = 0.211 (std: 0.101)
  ridge: R2 = 0.081 (std: 0.086)
  Fallback: Using svr-rbf-xl with R2 = 0.351

Model-based training with 1 models
Best R2: 0.351, Mean R2: 0.283
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.2564, kl_div=0.0000
    Epoch 1: policy_loss=-0.0201, value_loss=0.9691, entropy=0.2582, kl_div=-0.3547
  Round 1/5: Mean predicted reward = 9.707
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.2525, kl_div=0.0000
    Epoch 1: policy_loss=0.0528, value_loss=0.9683, entropy=0.2556, kl_div=-0.2536
  Round 2/5: Mean predicted reward = 9.511
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.2519, kl_div=0.0000
    Epoch 1: policy_loss=-0.0306, value_loss=0.9697, entropy=0.2590, kl_div=-0.0936
  Round 3/5: Mean predicted reward = 9.919
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.2522, kl_div=0.0000
    Epoch 1: policy_loss=-0.0303, value_loss=0.9693, entropy=0.2510, kl_div=-0.0396
  Round 4/5: Mean predicted reward = 10.103
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.2761, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2894
  Round 5/5: Mean predicted reward = 10.314

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 95 Results ---
  Mean Oracle Reward: 10.769
  Min Oracle Reward: 7.859
  Max Oracle Reward: 13.039
  Std Oracle Reward: 1.296
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.283, Max: 0.351, Count: 13
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
  ATCCCTGGGACG
  AGTCGCCGGCAT
  GGTCAGACCTGC
  CAGGGTACCCGT
  GTATGACCGCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.251
  Max reward: 12.181
  With intrinsic bonuses: 10.226

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9699, entropy=0.2748, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0889

=== Surrogate Model Training ===
Total samples: 3122

Training on 2997 samples (removed 125 outliers)
Reward range: [7.33, 13.37], mean: 10.42
  Created 13 candidate models for data size 2997
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.320 (std: 0.099)
  rf-tuned-xl: R2 = 0.324 (std: 0.096)
  gb-tuned-l: R2 = 0.310 (std: 0.062)
  gb-tuned-xl: R2 = 0.310 (std: 0.062)
  xgb-xl: R2 = 0.333 (std: 0.104)
  xgb-l: R2 = 0.333 (std: 0.104)
  mlp-adaptive-xl: R2 = 0.322 (std: 0.097)
  mlp-l: R2 = 0.307 (std: 0.100)
  svr-rbf-xl: R2 = 0.360 (std: 0.085)
  svr-poly-l: R2 = 0.360 (std: 0.085)
  knn-tuned-sqrt: R2 = 0.218 (std: 0.104)
  knn-tuned-l: R2 = 0.218 (std: 0.104)
  ridge: R2 = 0.082 (std: 0.083)
  Fallback: Using svr-rbf-xl with R2 = 0.360

Model-based training with 1 models
Best R2: 0.360, Mean R2: 0.292
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.2411, kl_div=0.0000
    Epoch 1: policy_loss=-0.0477, value_loss=0.9693, entropy=0.2412, kl_div=0.0140
  Round 1/5: Mean predicted reward = 9.365
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.2513, kl_div=0.0000
    Epoch 1: policy_loss=-0.0641, value_loss=0.9701, entropy=0.2541, kl_div=-0.1719
  Round 2/5: Mean predicted reward = 9.400
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2892, kl_div=0.0000
    Epoch 1: policy_loss=-0.0229, value_loss=0.9687, entropy=0.2952, kl_div=-0.3713
  Round 3/5: Mean predicted reward = 9.756
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9700, entropy=0.3021, kl_div=0.0000
    Epoch 1: policy_loss=0.0383, value_loss=0.9700, entropy=0.3070, kl_div=-0.2368
  Round 4/5: Mean predicted reward = 10.359
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.2978, kl_div=0.0000
    Epoch 1: policy_loss=-0.0521, value_loss=0.9683, entropy=0.2983, kl_div=-0.0726
  Round 5/5: Mean predicted reward = 10.490

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 96 Results ---
  Mean Oracle Reward: 10.241
  Min Oracle Reward: 6.065
  Max Oracle Reward: 12.011
  Std Oracle Reward: 1.370
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.292, Max: 0.360, Count: 13
  Total Sequences Evaluated: 3122

======================================================================
EXPERIMENT ROUND 97/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 3122

--- Round 97 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCTCCAAGGTGC
  AAGCCTGCCGGT
  GAGACTCCCGTG
  ACAGGTCCCGTG
  CAGTGCGTGCCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.592
  Max reward: 11.996
  With intrinsic bonuses: 10.562

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.2874, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2634

=== Surrogate Model Training ===
Total samples: 3154

Training on 3028 samples (removed 126 outliers)
Reward range: [7.35, 13.37], mean: 10.42
  Created 13 candidate models for data size 3028
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.320 (std: 0.102)
  rf-tuned-xl: R2 = 0.318 (std: 0.107)
  gb-tuned-l: R2 = 0.314 (std: 0.071)
  gb-tuned-xl: R2 = 0.314 (std: 0.071)
  xgb-xl: R2 = 0.330 (std: 0.115)
  xgb-l: R2 = 0.330 (std: 0.115)
  mlp-adaptive-xl: R2 = 0.328 (std: 0.092)
  mlp-l: R2 = 0.311 (std: 0.097)
  svr-rbf-xl: R2 = 0.367 (std: 0.089)
  svr-poly-l: R2 = 0.367 (std: 0.089)
  knn-tuned-sqrt: R2 = 0.215 (std: 0.103)
  knn-tuned-l: R2 = 0.215 (std: 0.103)
  ridge: R2 = 0.087 (std: 0.082)
  Fallback: Using svr-rbf-xl with R2 = 0.367

Model-based training with 1 models
Best R2: 0.367, Mean R2: 0.293
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.2416, kl_div=0.0000
    Epoch 1: policy_loss=-0.0330, value_loss=0.9701, entropy=0.2425, kl_div=0.0207
  Round 1/5: Mean predicted reward = 9.081
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.2953, kl_div=0.0000
    Epoch 1: policy_loss=-0.0694, value_loss=0.9685, entropy=0.3020, kl_div=-0.3018
  Round 2/5: Mean predicted reward = 9.753
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.3069, kl_div=0.0000
    Epoch 1: policy_loss=-0.0344, value_loss=0.9681, entropy=0.3162, kl_div=-0.1780
  Round 3/5: Mean predicted reward = 10.113
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.3208, kl_div=0.0000
    Epoch 1: policy_loss=-0.0085, value_loss=0.9690, entropy=0.3248, kl_div=-0.1567
  Round 4/5: Mean predicted reward = 10.148
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.2614, kl_div=0.0000
    Epoch 1: policy_loss=-0.0586, value_loss=0.9690, entropy=0.2602, kl_div=0.0050
  Round 5/5: Mean predicted reward = 10.144

  === Progress Analysis ===
  Status: NORMAL

--- Round 97 Results ---
  Mean Oracle Reward: 10.563
  Min Oracle Reward: 8.935
  Max Oracle Reward: 11.872
  Std Oracle Reward: 0.730
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.293, Max: 0.367, Count: 13
  Total Sequences Evaluated: 3154

======================================================================
EXPERIMENT ROUND 98/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 3154

--- Round 98 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGAATCCCGGTC
  CTTAGCGACGCG
  TGGCGCGCACAT
  CCATATCGGCGG
  CGGACCGTGCTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.112
  Max reward: 12.827
  With intrinsic bonuses: 10.123

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2896, kl_div=0.0000
    Epoch 1: policy_loss=-0.0476, value_loss=0.9687, entropy=0.2903, kl_div=-0.0319

=== Surrogate Model Training ===
Total samples: 3186

Training on 3058 samples (removed 128 outliers)
Reward range: [7.35, 13.37], mean: 10.42
  Created 13 candidate models for data size 3058
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.321 (std: 0.106)
  rf-tuned-xl: R2 = 0.321 (std: 0.104)
  gb-tuned-l: R2 = 0.316 (std: 0.077)
  gb-tuned-xl: R2 = 0.316 (std: 0.077)
  xgb-xl: R2 = 0.338 (std: 0.100)
  xgb-l: R2 = 0.338 (std: 0.100)
  mlp-adaptive-xl: R2 = 0.330 (std: 0.107)
  mlp-l: R2 = 0.334 (std: 0.095)
  svr-rbf-xl: R2 = 0.370 (std: 0.088)
  svr-poly-l: R2 = 0.370 (std: 0.088)
  knn-tuned-sqrt: R2 = 0.227 (std: 0.096)
  knn-tuned-l: R2 = 0.227 (std: 0.096)
  ridge: R2 = 0.087 (std: 0.081)
  Fallback: Using svr-rbf-xl with R2 = 0.370

Model-based training with 1 models
Best R2: 0.370, Mean R2: 0.300
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.2968, kl_div=0.0000
    Epoch 1: policy_loss=-0.0167, value_loss=0.9701, entropy=0.2976, kl_div=-0.0154
  Round 1/5: Mean predicted reward = 9.524
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2976, kl_div=0.0000
    Epoch 1: policy_loss=-0.0334, value_loss=0.9688, entropy=0.2998, kl_div=-0.0884
  Round 2/5: Mean predicted reward = 9.946
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.2739, kl_div=0.0000
    Epoch 1: policy_loss=-0.0559, value_loss=0.9683, entropy=0.2754, kl_div=-0.0660
  Round 3/5: Mean predicted reward = 9.900
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.3106, kl_div=0.0000
    Epoch 1: policy_loss=-0.0483, value_loss=0.9683, entropy=0.3109, kl_div=-0.0578
  Round 4/5: Mean predicted reward = 10.148
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.3146, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0615
  Round 5/5: Mean predicted reward = 10.415

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 98 Results ---
  Mean Oracle Reward: 10.125
  Min Oracle Reward: 4.846
  Max Oracle Reward: 12.913
  Std Oracle Reward: 1.610
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.300, Max: 0.370, Count: 13
  Total Sequences Evaluated: 3186

======================================================================
EXPERIMENT ROUND 99/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 3186

--- Round 99 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TTCAGGCGCGCA
  TGAGGACCGTCC
  CAGACCGCTTGG
  GTGACAGCTCCG
  CCAGGTCCTGGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.566
  Max reward: 11.892
  With intrinsic bonuses: 10.583

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.3144, kl_div=0.0000
    Epoch 1: policy_loss=-0.0315, value_loss=0.9691, entropy=0.3135, kl_div=0.0445

=== Surrogate Model Training ===
Total samples: 3218

Training on 3088 samples (removed 130 outliers)
Reward range: [7.37, 13.37], mean: 10.43
  Created 13 candidate models for data size 3088
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.319 (std: 0.120)
  rf-tuned-xl: R2 = 0.326 (std: 0.119)
  gb-tuned-l: R2 = 0.320 (std: 0.079)
  gb-tuned-xl: R2 = 0.320 (std: 0.079)
  xgb-xl: R2 = 0.340 (std: 0.102)
  xgb-l: R2 = 0.340 (std: 0.102)
  mlp-adaptive-xl: R2 = 0.326 (std: 0.101)
  mlp-l: R2 = 0.337 (std: 0.115)
  svr-rbf-xl: R2 = 0.372 (std: 0.092)
  svr-poly-l: R2 = 0.372 (std: 0.092)
  knn-tuned-sqrt: R2 = 0.215 (std: 0.104)
  knn-tuned-l: R2 = 0.215 (std: 0.104)
  ridge: R2 = 0.088 (std: 0.088)
  Fallback: Using svr-rbf-xl with R2 = 0.372

Model-based training with 1 models
Best R2: 0.372, Mean R2: 0.299
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.2898, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0528
  Round 1/5: Mean predicted reward = 9.390
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.3257, kl_div=0.0000
    Epoch 1: policy_loss=-0.0105, value_loss=0.9686, entropy=0.3256, kl_div=0.0215
  Round 2/5: Mean predicted reward = 9.886
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.3239, kl_div=0.0000
    Epoch 1: policy_loss=-0.0280, value_loss=0.9692, entropy=0.3250, kl_div=-0.0119
  Round 3/5: Mean predicted reward = 10.047
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.3340, kl_div=0.0000
    Epoch 1: policy_loss=-0.0223, value_loss=0.9680, entropy=0.3356, kl_div=-0.0739
  Round 4/5: Mean predicted reward = 10.063
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.3001, kl_div=0.0000
    Epoch 1: policy_loss=-0.0107, value_loss=0.9692, entropy=0.3007, kl_div=0.0195
  Round 5/5: Mean predicted reward = 10.176

  === Progress Analysis ===
  Status: NORMAL

--- Round 99 Results ---
  Mean Oracle Reward: 10.520
  Min Oracle Reward: 8.203
  Max Oracle Reward: 11.847
  Std Oracle Reward: 0.879
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.299, Max: 0.372, Count: 13
  Total Sequences Evaluated: 3218

======================================================================
EXPERIMENT ROUND 100/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 3218

--- Round 100 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCGCAGTGGATC
  CGTGGTCCAGCA
  ATGCCGGATCCG
  AGCCGCACGTGT
  TGCGCGCAGACT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.384
  Max reward: 14.191
  With intrinsic bonuses: 10.403

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.3350, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4720

=== Surrogate Model Training ===
Total samples: 3250

Training on 3117 samples (removed 133 outliers)
Reward range: [7.35, 13.37], mean: 10.43
  Created 13 candidate models for data size 3117
Current R2 threshold: 0.5
  rf-tuned-l: R2 = 0.330 (std: 0.118)
  rf-tuned-xl: R2 = 0.333 (std: 0.119)
  gb-tuned-l: R2 = 0.312 (std: 0.082)
  gb-tuned-xl: R2 = 0.312 (std: 0.082)
  xgb-xl: R2 = 0.338 (std: 0.102)
  xgb-l: R2 = 0.338 (std: 0.102)
  mlp-adaptive-xl: R2 = 0.330 (std: 0.100)
  mlp-l: R2 = 0.322 (std: 0.099)
  svr-rbf-xl: R2 = 0.379 (std: 0.095)
  svr-poly-l: R2 = 0.379 (std: 0.095)
  knn-tuned-sqrt: R2 = 0.221 (std: 0.107)
  knn-tuned-l: R2 = 0.221 (std: 0.107)
  ridge: R2 = 0.087 (std: 0.093)
  Fallback: Using svr-rbf-xl with R2 = 0.379

Model-based training with 1 models
Best R2: 0.379, Mean R2: 0.300
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.3202, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1516
  Round 1/5: Mean predicted reward = 9.127
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2949, kl_div=0.0000
    Epoch 1: policy_loss=-0.0481, value_loss=0.9688, entropy=0.2994, kl_div=-0.0820
  Round 2/5: Mean predicted reward = 9.543
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.3158, kl_div=0.0000
    Epoch 1: policy_loss=-0.0714, value_loss=0.9690, entropy=0.3224, kl_div=-0.1696
  Round 3/5: Mean predicted reward = 9.993
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.3573, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1110
  Round 4/5: Mean predicted reward = 10.303
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9677, entropy=0.3700, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2268
  Round 5/5: Mean predicted reward = 10.402

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 100 Results ---
  Mean Oracle Reward: 10.421
  Min Oracle Reward: 5.850
  Max Oracle Reward: 14.517
  Std Oracle Reward: 1.661
  Sequence Diversity: 1.000
  Models Used: 1
  Model R2 - Mean: 0.300, Max: 0.379, Count: 13
  Total Sequences Evaluated: 3250

======================================================================
DyNA PPO ALGORITHM COMPLETE!
======================================================================
Total rounds executed: 100
Total sequences evaluated: 3250
Best mean reward: 10.972 (achieved at round 75)

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 100
Final Mean Reward: 10.4206
Best Mean Reward: 10.9724
Best Max Reward: 15.0453
Initial Lr: 0.0003
Final Lr: 0.0003
Total Updates: 672
Final Diversity: 1.0000
Convergence Round: 13
==================================================

Generating learning curves...
Learning curves saved to learning_curves.png
Saving training metrics...
Metrics saved to training_metrics.json

======================================================================
FINAL OPTIMIZED SEQUENCES
======================================================================

Deterministic (Exploitation):
  GCGCGATGCAGC: 11.391
  GCGCGATGCAGC: 11.193
  GCGCGATGCAGC: 11.150
  GCGCGATGCAGC: 11.447
  GCGCGATGCAGC: 11.379

Stochastic (Exploration):
  GCGCGATGCATG: 11.401
  GCGACGATCGAC: 12.417
  GCGCAGCTAGCG: 11.245
  GCGCAGACAGCA: 11.258
  GCGCGATGCAGC: 11.436

Final Performance:
  Mean reward: 11.432
  Max reward: 12.417
  Std reward: 0.343

Best sequence found: GCGACGATCGAC
   Reward: 12.417

======================================================================
Training complete! Check 'learning_curves.png' and 'training_metrics.json'
======================================================================