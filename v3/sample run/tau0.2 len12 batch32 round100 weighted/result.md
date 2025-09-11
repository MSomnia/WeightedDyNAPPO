msomnia@Leihaos-MacBook-Pro v3 % python3 run2.py 
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
  Mean reward: 8.185
  Std reward: 2.790
  Min/Max: 0.000 / 12.023

Pre-training surrogate models on warm-up data...

Training on 45 samples (removed 5 outliers)
Reward range: [4.48, 12.02], mean: 8.93
  Created 8 candidate models for data size 45
Current R2 threshold: -0.3
  rf-xs: R2 = -0.588 (std: 0.245)
  rf-s: R2 = -0.520 (std: 0.311)
  knn-xs: R2 = -0.413 (std: 0.457)
  knn-s: R2 = -0.413 (std: 0.457)
  ridge: R2 = -0.318 (std: 0.259)
  gb-xs: R2 = -0.933 (std: 0.345)
  gp: R2 = -45.100 (std: 23.256)
  svr-rbf-s: R2 = -0.159 (std: 0.352)
Initial models trained: 1
Initial R2 scores - Mean: -6.055, Max: -0.159

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
  GGGACAGACGTT
  CCTAGATTCCGA
  GCTTATCCCCGT
  CACGGCAGGTCA
  CTCGTTCAGTAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.372
  Max reward: 11.105
  With intrinsic bonuses: 9.315

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9645, entropy=1.3843, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0576

=== Surrogate Model Training ===
Total samples: 82

Training on 73 samples (removed 9 outliers)
Reward range: [5.26, 12.02], mean: 9.37
  Created 8 candidate models for data size 73
Current R2 threshold: -0.3
  rf-xs: R2 = -0.160 (std: 0.244)
  rf-s: R2 = -0.182 (std: 0.268)
  knn-xs: R2 = -0.335 (std: 0.417)
  knn-s: R2 = -0.335 (std: 0.417)
  ridge: R2 = -0.164 (std: 0.163)
  gb-xs: R2 = -0.828 (std: 0.472)
  gp: R2 = -56.950 (std: 27.944)
  svr-rbf-s: R2 = -0.048 (std: 0.148)

Model-based training with 4 models
Best R2: -0.048, Mean R2: -7.375
Running 2 virtual training rounds
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=1.3807, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.264
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9757, entropy=1.3767, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.394

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 1 Results ---
  Mean Oracle Reward: 9.385
  Min Oracle Reward: 4.179
  Max Oracle Reward: 11.584
  Std Oracle Reward: 1.735
  Sequence Diversity: 1.000
  Models Used: 4
  Model R2 - Mean: -7.375, Max: -0.048, Count: 8
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
  ACAGCGCGAGTC
  ATTATCAGGGGA
  AATGCTCTCGGT
  CTGGGTAATATC
  GTGTCCTCTTTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.298
  Max reward: 11.533
  With intrinsic bonuses: 9.328

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9631, entropy=1.3731, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0634

=== Surrogate Model Training ===
Total samples: 114

Training on 105 samples (removed 9 outliers)
Reward range: [5.26, 12.02], mean: 9.34
  Created 11 candidate models for data size 105
Current R2 threshold: -0.3
  rf-m: R2 = -0.386 (std: 0.528)
  rf-l: R2 = -0.367 (std: 0.533)
  gb-m: R2 = -0.644 (std: 0.831)
  gb-l: R2 = -0.632 (std: 0.792)
  xgb-m: R2 = -0.923 (std: 0.733)
  knn-m: R2 = -0.297 (std: 0.451)
  knn-tuned: R2 = -0.297 (std: 0.451)
  mlp-m: R2 = -1.897 (std: 1.788)
  svr-rbf: R2 = -0.202 (std: 0.317)
  svr-poly: R2 = -0.202 (std: 0.317)
  ridge: R2 = -0.187 (std: 0.327)

Model-based training with 5 models
Best R2: -0.187, Mean R2: -0.549
Running 2 virtual training rounds
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9677, entropy=1.3678, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.328
    Using uniform weights (insufficient data)
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9621, entropy=1.3639, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.489

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 2 Results ---
  Mean Oracle Reward: 9.295
  Min Oracle Reward: 7.188
  Max Oracle Reward: 11.600
  Std Oracle Reward: 1.205
  Sequence Diversity: 1.000
  Models Used: 5
  Model R2 - Mean: -0.549, Max: -0.187, Count: 11
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
  CTCAGCAAGTTT
  TCCTCATCATCA
  TTGCTGCGCGCT
  CTCTCCCGCCAG
  ACCCGCCCGTCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.565
  Max reward: 11.619
  With intrinsic bonuses: 9.648

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9770, entropy=1.3604, kl_div=0.0000
    Epoch 2: policy_loss=-0.0508, value_loss=0.9768, entropy=1.3542, kl_div=0.0281
    Early stopping at epoch 4: KL divergence = 0.0681

=== Surrogate Model Training ===
Total samples: 146

Training on 135 samples (removed 11 outliers)
Reward range: [5.60, 12.02], mean: 9.44
  Created 11 candidate models for data size 135
Current R2 threshold: -0.3
  rf-m: R2 = -0.119 (std: 0.241)
  rf-l: R2 = -0.139 (std: 0.239)
  gb-m: R2 = -0.420 (std: 0.238)
  gb-l: R2 = -0.413 (std: 0.242)
  xgb-m: R2 = -0.446 (std: 0.543)
  knn-m: R2 = -0.267 (std: 0.127)
  knn-tuned: R2 = -0.267 (std: 0.127)
  mlp-m: R2 = -1.092 (std: 0.522)
  svr-rbf: R2 = -0.097 (std: 0.118)
  svr-poly: R2 = -0.097 (std: 0.118)
  ridge: R2 = -0.065 (std: 0.070)

Model-based training with 7 models
Best R2: -0.065, Mean R2: -0.311
Running 2 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.147 rf-l:0.144 knn-m:0.127 knn-tuned:0.127 svr-rbf:0.150 svr-poly:0.150 ridge:0.155 
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9774, entropy=1.3458, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.435
    Using performance-based weights
    Model weights: rf-m:0.147 rf-l:0.144 knn-m:0.127 knn-tuned:0.127 svr-rbf:0.150 svr-poly:0.150 ridge:0.155 
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9711, entropy=1.3443, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.508

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 3 Results ---
  Mean Oracle Reward: 9.526
  Min Oracle Reward: 5.574
  Max Oracle Reward: 11.435
  Std Oracle Reward: 1.359
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: -0.311, Max: -0.065, Count: 11
  New best mean reward!
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
  GAGCCAGTTGAC
  GGACTACAGGCT
  CCGATTAGGCTA
  TACGATGCGTCA
  GCAAGTAGGCTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.102
  Max reward: 14.330
  With intrinsic bonuses: 10.294

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9741, entropy=1.3435, kl_div=0.0000
    Epoch 1: policy_loss=-0.0066, value_loss=0.9741, entropy=1.3427, kl_div=0.0080
    Epoch 2: policy_loss=-0.0146, value_loss=0.9741, entropy=1.3420, kl_div=0.0158
    Epoch 3: policy_loss=-0.0239, value_loss=0.9741, entropy=1.3412, kl_div=0.0234

=== Surrogate Model Training ===
Total samples: 178

Training on 165 samples (removed 13 outliers)
Reward range: [5.94, 12.02], mean: 9.57
  Created 11 candidate models for data size 165
Current R2 threshold: -0.3
  rf-m: R2 = -0.198 (std: 0.215)
  rf-l: R2 = -0.206 (std: 0.279)
  gb-m: R2 = -0.481 (std: 0.316)
  gb-l: R2 = -0.485 (std: 0.335)
  xgb-m: R2 = -0.365 (std: 0.363)
  knn-m: R2 = -0.297 (std: 0.287)
  knn-tuned: R2 = -0.297 (std: 0.287)
  mlp-m: R2 = -1.569 (std: 1.348)
  svr-rbf: R2 = -0.101 (std: 0.152)
  svr-poly: R2 = -0.101 (std: 0.152)
  ridge: R2 = -0.100 (std: 0.109)

Model-based training with 7 models
Best R2: -0.100, Mean R2: -0.382
Running 2 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.141 rf-l:0.140 knn-m:0.127 knn-tuned:0.127 svr-rbf:0.155 svr-poly:0.155 ridge:0.155 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9671, entropy=1.3380, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.721
    Using performance-based weights
    Model weights: rf-m:0.141 rf-l:0.140 knn-m:0.127 knn-tuned:0.127 svr-rbf:0.155 svr-poly:0.155 ridge:0.155 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9695, entropy=1.3387, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.696

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 4 Results ---
  Mean Oracle Reward: 10.128
  Min Oracle Reward: 8.237
  Max Oracle Reward: 14.114
  Std Oracle Reward: 1.109
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: -0.382, Max: -0.100, Count: 11
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
  TTGTCAGCAACG
  GTCACTAGCATG
  CGGAGATCTAGC
  CTTCACAGGCGG
  GGTCCAATGAGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.810
  Max reward: 11.295
  With intrinsic bonuses: 9.980

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=1.3391, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0652

=== Surrogate Model Training ===
Total samples: 210

Training on 196 samples (removed 14 outliers)
Reward range: [6.27, 12.02], mean: 9.63
  Created 11 candidate models for data size 196
Current R2 threshold: -0.3
  rf-m: R2 = -0.068 (std: 0.128)
  rf-l: R2 = -0.084 (std: 0.103)
  gb-m: R2 = -0.253 (std: 0.167)
  gb-l: R2 = -0.259 (std: 0.173)
  xgb-m: R2 = -0.331 (std: 0.144)
  knn-m: R2 = -0.308 (std: 0.095)
  knn-tuned: R2 = -0.308 (std: 0.095)
  mlp-m: R2 = -1.700 (std: 1.762)
  svr-rbf: R2 = -0.002 (std: 0.138)
  svr-poly: R2 = -0.002 (std: 0.138)
  ridge: R2 = -0.099 (std: 0.101)

Model-based training with 7 models
Best R2: -0.002, Mean R2: -0.310
Running 2 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.148 rf-l:0.146 gb-m:0.123 gb-l:0.122 svr-rbf:0.158 svr-poly:0.158 ridge:0.144 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=1.3309, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.687
    Using performance-based weights
    Model weights: rf-m:0.148 rf-l:0.146 gb-m:0.123 gb-l:0.122 svr-rbf:0.158 svr-poly:0.158 ridge:0.144 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9667, entropy=1.3238, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.654

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 5 Results ---
  Mean Oracle Reward: 9.820
  Min Oracle Reward: 8.141
  Max Oracle Reward: 11.163
  Std Oracle Reward: 0.728
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: -0.310, Max: -0.002, Count: 11
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
  AGGGTGACCACT
  CGAGGTTACATC
  TGCAAGTCAGCT
  CGTATGATCCGA
  TACTGGCAATGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.792
  Max reward: 11.560
  With intrinsic bonuses: 9.882

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=1.3131, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0873

=== Surrogate Model Training ===
Total samples: 242

Training on 227 samples (removed 15 outliers)
Reward range: [6.27, 12.02], mean: 9.67
  Created 11 candidate models for data size 227
Current R2 threshold: -0.3
  rf-m: R2 = -0.069 (std: 0.144)
  rf-l: R2 = -0.086 (std: 0.166)
  gb-m: R2 = -0.165 (std: 0.184)
  gb-l: R2 = -0.165 (std: 0.183)
  xgb-m: R2 = -0.383 (std: 0.219)
  knn-m: R2 = -0.205 (std: 0.149)
  knn-tuned: R2 = -0.205 (std: 0.149)
  mlp-m: R2 = -1.486 (std: 1.067)
  svr-rbf: R2 = 0.009 (std: 0.120)
  svr-poly: R2 = 0.009 (std: 0.120)
  ridge: R2 = -0.079 (std: 0.077)

Model-based training with 9 models
Best R2: 0.009, Mean R2: -0.257
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.115 rf-l:0.113 gb-m:0.104 gb-l:0.104 knn-m:0.100 knn-tuned:0.100 svr-rbf:0.124 svr-poly:0.124 ridge:0.114 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=1.3025, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1217
  Round 1/3: Mean predicted reward = 9.629
    Using performance-based weights
    Model weights: rf-m:0.115 rf-l:0.113 gb-m:0.104 gb-l:0.104 knn-m:0.100 knn-tuned:0.100 svr-rbf:0.124 svr-poly:0.124 ridge:0.114 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9668, entropy=1.2927, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1116
  Round 2/3: Mean predicted reward = 9.738
    Using performance-based weights
    Model weights: rf-m:0.115 rf-l:0.113 gb-m:0.104 gb-l:0.104 knn-m:0.100 knn-tuned:0.100 svr-rbf:0.124 svr-poly:0.124 ridge:0.114 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9644, entropy=1.2755, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1168
  Round 3/3: Mean predicted reward = 9.778

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 6 Results ---
  Mean Oracle Reward: 9.771
  Min Oracle Reward: 5.194
  Max Oracle Reward: 11.853
  Std Oracle Reward: 1.266
  Sequence Diversity: 1.000
  Models Used: 9
  Model R2 - Mean: -0.257, Max: 0.009, Count: 11
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
  ACTGCCTGAAGT
  ACCTCGGAGTAG
  GGCTGCTAAGCC
  GCTCGAACGAGT
  AGGTTCACAGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.885
  Max reward: 11.961
  With intrinsic bonuses: 9.947

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9652, entropy=1.2603, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0977

=== Surrogate Model Training ===
Total samples: 274

Training on 259 samples (removed 15 outliers)
Reward range: [6.27, 12.02], mean: 9.69
  Created 11 candidate models for data size 259
Current R2 threshold: -0.3
  rf-m: R2 = -0.080 (std: 0.115)
  rf-l: R2 = -0.067 (std: 0.114)
  gb-m: R2 = -0.104 (std: 0.109)
  gb-l: R2 = -0.106 (std: 0.111)
  xgb-m: R2 = -0.368 (std: 0.101)
  knn-m: R2 = -0.246 (std: 0.109)
  knn-tuned: R2 = -0.246 (std: 0.109)
  mlp-m: R2 = -0.727 (std: 0.712)
  svr-rbf: R2 = -0.031 (std: 0.075)
  svr-poly: R2 = -0.031 (std: 0.075)
  ridge: R2 = -0.089 (std: 0.079)

Model-based training with 9 models
Best R2: -0.031, Mean R2: -0.190
Running 2 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.114 rf-l:0.116 gb-m:0.112 gb-l:0.111 knn-m:0.097 knn-tuned:0.097 svr-rbf:0.120 svr-poly:0.120 ridge:0.113 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9699, entropy=1.2498, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.855
    Using performance-based weights
    Model weights: rf-m:0.114 rf-l:0.116 gb-m:0.112 gb-l:0.111 knn-m:0.097 knn-tuned:0.097 svr-rbf:0.120 svr-poly:0.120 ridge:0.113 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9716, entropy=1.2380, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.870

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 7 Results ---
  Mean Oracle Reward: 9.909
  Min Oracle Reward: 6.783
  Max Oracle Reward: 11.877
  Std Oracle Reward: 1.080
  Sequence Diversity: 1.000
  Models Used: 9
  Model R2 - Mean: -0.190, Max: -0.031, Count: 11
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
  AAGGTTCGCCGC
  GTACCGGATCAT
  CAGTTTAACCGG
  GGTCAAACCTGG
  GGCTGAAAGCTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.616
  Max reward: 11.522
  With intrinsic bonuses: 9.663

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9676, entropy=1.2316, kl_div=0.0000
    Epoch 1: policy_loss=-0.0152, value_loss=0.9676, entropy=1.2283, kl_div=0.0325

=== Surrogate Model Training ===
Total samples: 306

Training on 291 samples (removed 15 outliers)
Reward range: [6.27, 12.02], mean: 9.68
  Created 11 candidate models for data size 291
Current R2 threshold: -0.3
  rf-m: R2 = -0.050 (std: 0.090)
  rf-l: R2 = -0.057 (std: 0.073)
  gb-m: R2 = -0.034 (std: 0.144)
  gb-l: R2 = -0.034 (std: 0.144)
  xgb-m: R2 = -0.254 (std: 0.237)
  knn-m: R2 = -0.143 (std: 0.141)
  knn-tuned: R2 = -0.143 (std: 0.141)
  mlp-m: R2 = -0.599 (std: 0.244)
  svr-rbf: R2 = -0.006 (std: 0.056)
  svr-poly: R2 = -0.006 (std: 0.056)
  ridge: R2 = -0.045 (std: 0.035)

Model-based training with 10 models
Best R2: -0.006, Mean R2: -0.125
Running 2 virtual training rounds
    Using performance-based weights
    Model weights: rf-m:0.102 rf-l:0.102 gb-m:0.104 gb-l:0.104 xgb-m:0.084 knn-m:0.093 knn-tuned:0.093 svr-rbf:0.107 svr-poly:0.107 ridge:0.103 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9726, entropy=1.2240, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.883
    Using performance-based weights
    Model weights: rf-m:0.102 rf-l:0.102 gb-m:0.104 gb-l:0.104 xgb-m:0.084 knn-m:0.093 knn-tuned:0.093 svr-rbf:0.107 svr-poly:0.107 ridge:0.103 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9715, entropy=1.2121, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.886

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 8 Results ---
  Mean Oracle Reward: 9.617
  Min Oracle Reward: 6.630
  Max Oracle Reward: 11.654
  Std Oracle Reward: 1.126
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: -0.125, Max: -0.006, Count: 11
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
  AAGTCGTGCAGC
  TACAGGAGCCGT
  AGTGTGCACCAG
  GCGCCGTAAAGT
  GAACGCATTGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.943
  Max reward: 12.347
  With intrinsic bonuses: 10.013

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9711, entropy=1.2143, kl_div=0.0000
    Epoch 1: policy_loss=-0.0112, value_loss=0.9711, entropy=1.2124, kl_div=0.0178

=== Surrogate Model Training ===
Total samples: 338

Training on 321 samples (removed 17 outliers)
Reward range: [6.27, 12.50], mean: 9.74
  Created 14 candidate models for data size 321
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.050 (std: 0.119)
  rf-tuned-xl: R2 = -0.100 (std: 0.155)
  gb-tuned-l: R2 = -0.103 (std: 0.156)
  gb-tuned-xl: R2 = -0.103 (std: 0.156)
  xgb-xl: R2 = -0.339 (std: 0.119)
  xgb-l: R2 = -0.339 (std: 0.119)
  mlp-adaptive-xl: R2 = -0.449 (std: 0.394)
  mlp-l: R2 = -0.524 (std: 0.363)
  svr-rbf-xl: R2 = -0.004 (std: 0.087)
  svr-poly-l: R2 = -0.004 (std: 0.087)
  knn-tuned-sqrt: R2 = -0.107 (std: 0.155)
  knn-tuned-l: R2 = -0.107 (std: 0.155)
  ridge: R2 = -0.058 (std: 0.024)
  gp: R2 = -86.420 (std: 26.192)

Model-based training with 9 models
Best R2: -0.004, Mean R2: -6.336
Running 2 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.113 rf-tuned-xl:0.108 gb-tuned-l:0.107 gb-tuned-xl:0.107 svr-rbf-xl:0.119 svr-poly-l:0.119 knn-tuned-sqrt:0.107 knn-tuned-l:0.107 ridge:0.112 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=1.2126, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.850
    Using performance-based weights
    Model weights: rf-tuned-l:0.113 rf-tuned-xl:0.108 gb-tuned-l:0.107 gb-tuned-xl:0.107 svr-rbf-xl:0.119 svr-poly-l:0.119 knn-tuned-sqrt:0.107 knn-tuned-l:0.107 ridge:0.112 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9726, entropy=1.2122, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.868

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 9 Results ---
  Mean Oracle Reward: 9.947
  Min Oracle Reward: 2.856
  Max Oracle Reward: 12.095
  Std Oracle Reward: 1.784
  Sequence Diversity: 1.000
  Models Used: 9
  Model R2 - Mean: -6.336, Max: -0.004, Count: 14
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
  TCATAACCTGGG
  CACGTGGGAACT
  ACGTAGTACGCT
  AGGCAGTTCGAC
  CGCGGGATTCAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.534
  Max reward: 12.276
  With intrinsic bonuses: 9.535

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9716, entropy=1.2061, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1874

=== Surrogate Model Training ===
Total samples: 370

Training on 350 samples (removed 20 outliers)
Reward range: [6.32, 12.50], mean: 9.76
  Created 14 candidate models for data size 350
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.070 (std: 0.102)
  rf-tuned-xl: R2 = -0.049 (std: 0.107)
  gb-tuned-l: R2 = -0.092 (std: 0.157)
  gb-tuned-xl: R2 = -0.092 (std: 0.157)
  xgb-xl: R2 = -0.310 (std: 0.176)
  xgb-l: R2 = -0.310 (std: 0.176)
  mlp-adaptive-xl: R2 = -0.523 (std: 0.320)
  mlp-l: R2 = -0.598 (std: 0.625)
  svr-rbf-xl: R2 = -0.010 (std: 0.068)
  svr-poly-l: R2 = -0.010 (std: 0.068)
  knn-tuned-sqrt: R2 = -0.088 (std: 0.144)
  knn-tuned-l: R2 = -0.088 (std: 0.144)
  ridge: R2 = -0.026 (std: 0.011)
  gp: R2 = -88.168 (std: 31.032)

Model-based training with 9 models
Best R2: -0.010, Mean R2: -6.459
Running 2 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.110 rf-tuned-xl:0.112 gb-tuned-l:0.107 gb-tuned-xl:0.107 svr-rbf-xl:0.117 svr-poly-l:0.117 knn-tuned-sqrt:0.108 knn-tuned-l:0.108 ridge:0.115 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=1.1898, kl_div=0.0000
  Round 1/2: Mean predicted reward = 9.793
    Using performance-based weights
    Model weights: rf-tuned-l:0.110 rf-tuned-xl:0.112 gb-tuned-l:0.107 gb-tuned-xl:0.107 svr-rbf-xl:0.117 svr-poly-l:0.117 knn-tuned-sqrt:0.108 knn-tuned-l:0.108 ridge:0.115 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9679, entropy=1.1783, kl_div=0.0000
  Round 2/2: Mean predicted reward = 9.837

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 10 Results ---
  Mean Oracle Reward: 9.525
  Min Oracle Reward: 4.630
  Max Oracle Reward: 12.393
  Std Oracle Reward: 1.668
  Sequence Diversity: 1.000
  Models Used: 9
  Model R2 - Mean: -6.459, Max: -0.010, Count: 14
  Total Sequences Evaluated: 370

======================================================================
EXPERIMENT ROUND 11/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 370

--- Round 11 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCCAATTGGAGG
  GCTACAAGTGGC
  ATGATGGCTACC
  GGCGCATAACTT
  GTGCCGATAAGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.630
  Max reward: 11.748
  With intrinsic bonuses: 9.627

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9745, entropy=1.1586, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1672

=== Surrogate Model Training ===
Total samples: 402

Training on 381 samples (removed 21 outliers)
Reward range: [6.42, 12.50], mean: 9.76
  Created 14 candidate models for data size 381
Current R2 threshold: -0.29
  rf-tuned-l: R2 = -0.019 (std: 0.105)
  rf-tuned-xl: R2 = -0.048 (std: 0.118)
  gb-tuned-l: R2 = -0.030 (std: 0.162)
  gb-tuned-xl: R2 = -0.030 (std: 0.162)
  xgb-xl: R2 = -0.237 (std: 0.194)
  xgb-l: R2 = -0.237 (std: 0.194)
  mlp-adaptive-xl: R2 = -0.760 (std: 0.658)
  mlp-l: R2 = -0.478 (std: 0.440)
  svr-rbf-xl: R2 = 0.016 (std: 0.059)
  svr-poly-l: R2 = 0.016 (std: 0.059)
  knn-tuned-sqrt: R2 = -0.050 (std: 0.112)
  knn-tuned-l: R2 = -0.050 (std: 0.112)
  ridge: R2 = -0.038 (std: 0.042)
  gp: R2 = -87.019 (std: 32.216)

Model-based training with 11 models
Best R2: 0.016, Mean R2: -6.354
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.095 rf-tuned-xl:0.092 gb-tuned-l:0.094 gb-tuned-xl:0.094 xgb-xl:0.076 xgb-l:0.076 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.092 knn-tuned-l:0.092 ridge:0.093 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9755, entropy=1.1425, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1534
  Round 1/3: Mean predicted reward = 9.853
    Using performance-based weights
    Model weights: rf-tuned-l:0.095 rf-tuned-xl:0.092 gb-tuned-l:0.094 gb-tuned-xl:0.094 xgb-xl:0.076 xgb-l:0.076 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.092 knn-tuned-l:0.092 ridge:0.093 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9700, entropy=1.1302, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1965
  Round 2/3: Mean predicted reward = 9.813
    Using performance-based weights
    Model weights: rf-tuned-l:0.095 rf-tuned-xl:0.092 gb-tuned-l:0.094 gb-tuned-xl:0.094 xgb-xl:0.076 xgb-l:0.076 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.092 knn-tuned-l:0.092 ridge:0.093 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9750, entropy=1.1052, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2147
  Round 3/3: Mean predicted reward = 9.936

  === Progress Analysis ===
  Status: NORMAL

--- Round 11 Results ---
  Mean Oracle Reward: 9.665
  Min Oracle Reward: 6.110
  Max Oracle Reward: 11.898
  Std Oracle Reward: 1.336
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -6.354, Max: 0.016, Count: 14
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
  CCAGTTGCGAAG
  ATCAGCGGACTT
  TCCAGTGGACAG
  GTCAGCGGTCAA
  ACGGGCGACTTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.012
  Max reward: 12.400
  With intrinsic bonuses: 9.930

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9714, entropy=1.0888, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1922

=== Surrogate Model Training ===
Total samples: 434

Training on 411 samples (removed 23 outliers)
Reward range: [6.66, 12.51], mean: 9.80
  Created 14 candidate models for data size 411
Current R2 threshold: -0.27999999999999997
  rf-tuned-l: R2 = -0.025 (std: 0.109)
  rf-tuned-xl: R2 = -0.050 (std: 0.120)
  gb-tuned-l: R2 = -0.041 (std: 0.140)
  gb-tuned-xl: R2 = -0.041 (std: 0.140)
  xgb-xl: R2 = -0.201 (std: 0.135)
  xgb-l: R2 = -0.201 (std: 0.135)
  mlp-adaptive-xl: R2 = -0.543 (std: 0.430)
  mlp-l: R2 = -0.524 (std: 0.287)
  svr-rbf-xl: R2 = 0.009 (std: 0.088)
  svr-poly-l: R2 = 0.009 (std: 0.088)
  knn-tuned-sqrt: R2 = -0.072 (std: 0.092)
  knn-tuned-l: R2 = -0.072 (std: 0.092)
  ridge: R2 = -0.054 (std: 0.053)
  gp: R2 = -85.818 (std: 19.452)

Model-based training with 11 models
Best R2: 0.009, Mean R2: -6.259
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.095 rf-tuned-xl:0.092 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.090 knn-tuned-l:0.090 ridge:0.092 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=1.0751, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2694
  Round 1/3: Mean predicted reward = 9.756
    Using performance-based weights
    Model weights: rf-tuned-l:0.095 rf-tuned-xl:0.092 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.090 knn-tuned-l:0.090 ridge:0.092 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9717, entropy=1.0559, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2795
  Round 2/3: Mean predicted reward = 9.817
    Using performance-based weights
    Model weights: rf-tuned-l:0.095 rf-tuned-xl:0.092 gb-tuned-l:0.093 gb-tuned-xl:0.093 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.090 knn-tuned-l:0.090 ridge:0.092 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9707, entropy=1.0292, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3155
  Round 3/3: Mean predicted reward = 9.801

  === Progress Analysis ===
  Status: NORMAL

--- Round 12 Results ---
  Mean Oracle Reward: 9.955
  Min Oracle Reward: 2.399
  Max Oracle Reward: 12.418
  Std Oracle Reward: 1.657
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -6.259, Max: 0.009, Count: 14
  Total Sequences Evaluated: 434

======================================================================
EXPERIMENT ROUND 13/100
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
  TTACGTGCCGAA
  CATGGAATGTCC
  AGTCGGTTCAAC
  TGCGATGAGCAC
  GCTCGCAGTAAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.281
  Max reward: 12.254
  With intrinsic bonuses: 10.293

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9662, entropy=1.0017, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2074

=== Surrogate Model Training ===
Total samples: 466

Training on 444 samples (removed 22 outliers)
Reward range: [6.42, 12.51], mean: 9.83
  Created 14 candidate models for data size 444
Current R2 threshold: -0.27
  rf-tuned-l: R2 = 0.013 (std: 0.089)
  rf-tuned-xl: R2 = 0.008 (std: 0.112)
  gb-tuned-l: R2 = 0.022 (std: 0.096)
  gb-tuned-xl: R2 = 0.022 (std: 0.096)
  xgb-xl: R2 = -0.159 (std: 0.123)
  xgb-l: R2 = -0.159 (std: 0.123)
  mlp-adaptive-xl: R2 = -0.372 (std: 0.196)
  mlp-l: R2 = -0.493 (std: 0.088)
  svr-rbf-xl: R2 = 0.055 (std: 0.100)
  svr-poly-l: R2 = 0.055 (std: 0.100)
  knn-tuned-sqrt: R2 = -0.052 (std: 0.094)
  knn-tuned-l: R2 = -0.052 (std: 0.094)
  ridge: R2 = -0.038 (std: 0.067)
  gp: R2 = -81.486 (std: 13.715)

Model-based training with 11 models
Best R2: 0.055, Mean R2: -5.903
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.094 gb-tuned-l:0.095 gb-tuned-xl:0.095 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.088 knn-tuned-l:0.088 ridge:0.090 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.9885, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2301
  Round 1/3: Mean predicted reward = 9.906
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.094 gb-tuned-l:0.095 gb-tuned-xl:0.095 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.088 knn-tuned-l:0.088 ridge:0.090 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9672, entropy=0.9673, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2630
  Round 2/3: Mean predicted reward = 9.796
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.094 gb-tuned-l:0.095 gb-tuned-xl:0.095 xgb-xl:0.079 xgb-l:0.079 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.088 knn-tuned-l:0.088 ridge:0.090 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9672, entropy=0.9496, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2630
  Round 3/3: Mean predicted reward = 9.870

  === Progress Analysis ===
  Status: NORMAL

--- Round 13 Results ---
  Mean Oracle Reward: 10.271
  Min Oracle Reward: 7.662
  Max Oracle Reward: 12.166
  Std Oracle Reward: 1.195
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -5.903, Max: 0.055, Count: 14
  New best mean reward!
  Total Sequences Evaluated: 466

======================================================================
EXPERIMENT ROUND 14/100
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
  CTGAGGCTCGAA
  GAGCTTTCACGA
  GGTACAGCCTCG
  CATTGCAAGCTG
  GAGTCACTTCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.970
  Max reward: 12.128
  With intrinsic bonuses: 9.995

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9678, entropy=0.9332, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1234

=== Surrogate Model Training ===
Total samples: 498

Training on 474 samples (removed 24 outliers)
Reward range: [6.66, 12.51], mean: 9.86
  Created 14 candidate models for data size 474
Current R2 threshold: -0.26
  rf-tuned-l: R2 = 0.003 (std: 0.139)
  rf-tuned-xl: R2 = 0.015 (std: 0.108)
  gb-tuned-l: R2 = 0.019 (std: 0.138)
  gb-tuned-xl: R2 = 0.019 (std: 0.138)
  xgb-xl: R2 = -0.084 (std: 0.144)
  xgb-l: R2 = -0.084 (std: 0.144)
  mlp-adaptive-xl: R2 = -0.417 (std: 0.112)
  mlp-l: R2 = -0.405 (std: 0.358)
  svr-rbf-xl: R2 = 0.058 (std: 0.111)
  svr-poly-l: R2 = 0.058 (std: 0.111)
  knn-tuned-sqrt: R2 = -0.052 (std: 0.134)
  knn-tuned-l: R2 = -0.052 (std: 0.134)
  ridge: R2 = -0.066 (std: 0.096)
  gp: R2 = -86.706 (std: 14.384)

Model-based training with 11 models
Best R2: 0.058, Mean R2: -6.264
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.092 rf-tuned-xl:0.094 gb-tuned-l:0.094 gb-tuned-xl:0.094 xgb-xl:0.085 xgb-l:0.085 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.087 knn-tuned-l:0.087 ridge:0.086 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.9301, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1120
  Round 1/3: Mean predicted reward = 9.904
    Using performance-based weights
    Model weights: rf-tuned-l:0.092 rf-tuned-xl:0.094 gb-tuned-l:0.094 gb-tuned-xl:0.094 xgb-xl:0.085 xgb-l:0.085 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.087 knn-tuned-l:0.087 ridge:0.086 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9728, entropy=0.9159, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1056
  Round 2/3: Mean predicted reward = 9.824
    Using performance-based weights
    Model weights: rf-tuned-l:0.092 rf-tuned-xl:0.094 gb-tuned-l:0.094 gb-tuned-xl:0.094 xgb-xl:0.085 xgb-l:0.085 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.087 knn-tuned-l:0.087 ridge:0.086 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.9142, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1332
  Round 3/3: Mean predicted reward = 10.022

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 14 Results ---
  Mean Oracle Reward: 9.971
  Min Oracle Reward: 4.732
  Max Oracle Reward: 11.775
  Std Oracle Reward: 1.270
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -6.264, Max: 0.058, Count: 14
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
  ACCTGTCAGGCG
  CCATAGGATTGC
  AAGCGTGCTCGA
  ATAGGCTGGCAC
  AGGCCTAGTCGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.039
  Max reward: 12.808
  With intrinsic bonuses: 10.098

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9672, entropy=0.9147, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7095

=== Surrogate Model Training ===
Total samples: 530

Training on 506 samples (removed 24 outliers)
Reward range: [6.66, 12.84], mean: 9.87
  Created 13 candidate models for data size 506
Current R2 threshold: -0.25
  rf-tuned-l: R2 = 0.020 (std: 0.130)
  rf-tuned-xl: R2 = 0.032 (std: 0.135)
  gb-tuned-l: R2 = 0.016 (std: 0.167)
  gb-tuned-xl: R2 = 0.016 (std: 0.167)
  xgb-xl: R2 = -0.130 (std: 0.123)
  xgb-l: R2 = -0.130 (std: 0.123)
  mlp-adaptive-xl: R2 = -0.330 (std: 0.152)
  mlp-l: R2 = -0.323 (std: 0.108)
  svr-rbf-xl: R2 = 0.066 (std: 0.119)
  svr-poly-l: R2 = 0.066 (std: 0.119)
  knn-tuned-sqrt: R2 = -0.032 (std: 0.148)
  knn-tuned-l: R2 = -0.032 (std: 0.148)
  ridge: R2 = -0.055 (std: 0.080)

Model-based training with 11 models
Best R2: 0.066, Mean R2: -0.063
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.095 gb-tuned-l:0.094 gb-tuned-xl:0.094 xgb-xl:0.081 xgb-l:0.081 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.089 knn-tuned-l:0.089 ridge:0.087 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.8737, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7170
  Round 1/3: Mean predicted reward = 9.949
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.095 gb-tuned-l:0.094 gb-tuned-xl:0.094 xgb-xl:0.081 xgb-l:0.081 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.089 knn-tuned-l:0.089 ridge:0.087 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9671, entropy=0.8368, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8853
  Round 2/3: Mean predicted reward = 9.726
    Using performance-based weights
    Model weights: rf-tuned-l:0.094 rf-tuned-xl:0.095 gb-tuned-l:0.094 gb-tuned-xl:0.094 xgb-xl:0.081 xgb-l:0.081 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.089 knn-tuned-l:0.089 ridge:0.087 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.8053, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8914
  Round 3/3: Mean predicted reward = 9.826

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 15 Results ---
  Mean Oracle Reward: 10.120
  Min Oracle Reward: 7.078
  Max Oracle Reward: 12.707
  Std Oracle Reward: 1.030
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -0.063, Max: 0.066, Count: 13
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
  CCGAGGTCTACG
  TCGAAAGCCGTT
  TGGCACCATGGA
  GAGGCCTTACCG
  CCATGGCATCGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.864
  Max reward: 12.125
  With intrinsic bonuses: 9.847

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9645, entropy=0.7884, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7918

=== Surrogate Model Training ===
Total samples: 562

Training on 537 samples (removed 25 outliers)
Reward range: [6.66, 12.84], mean: 9.88
  Created 13 candidate models for data size 537
Current R2 threshold: -0.24
  rf-tuned-l: R2 = 0.025 (std: 0.128)
  rf-tuned-xl: R2 = 0.002 (std: 0.111)
  gb-tuned-l: R2 = 0.041 (std: 0.150)
  gb-tuned-xl: R2 = 0.041 (std: 0.150)
  xgb-xl: R2 = -0.195 (std: 0.111)
  xgb-l: R2 = -0.195 (std: 0.111)
  mlp-adaptive-xl: R2 = -0.290 (std: 0.164)
  mlp-l: R2 = -0.361 (std: 0.103)
  svr-rbf-xl: R2 = 0.059 (std: 0.100)
  svr-poly-l: R2 = 0.059 (std: 0.100)
  knn-tuned-sqrt: R2 = -0.024 (std: 0.107)
  knn-tuned-l: R2 = -0.024 (std: 0.107)
  ridge: R2 = -0.037 (std: 0.067)

Model-based training with 11 models
Best R2: 0.059, Mean R2: -0.069
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.095 rf-tuned-xl:0.093 gb-tuned-l:0.096 gb-tuned-xl:0.096 xgb-xl:0.076 xgb-l:0.076 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.090 knn-tuned-l:0.090 ridge:0.089 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9720, entropy=0.7704, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6493
  Round 1/3: Mean predicted reward = 9.785
    Using performance-based weights
    Model weights: rf-tuned-l:0.095 rf-tuned-xl:0.093 gb-tuned-l:0.096 gb-tuned-xl:0.096 xgb-xl:0.076 xgb-l:0.076 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.090 knn-tuned-l:0.090 ridge:0.089 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9678, entropy=0.7468, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6423
  Round 2/3: Mean predicted reward = 9.932
    Using performance-based weights
    Model weights: rf-tuned-l:0.095 rf-tuned-xl:0.093 gb-tuned-l:0.096 gb-tuned-xl:0.096 xgb-xl:0.076 xgb-l:0.076 svr-rbf-xl:0.098 svr-poly-l:0.098 knn-tuned-sqrt:0.090 knn-tuned-l:0.090 ridge:0.089 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.7358, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7435
  Round 3/3: Mean predicted reward = 9.800

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 16 Results ---
  Mean Oracle Reward: 9.860
  Min Oracle Reward: 6.420
  Max Oracle Reward: 11.891
  Std Oracle Reward: 1.247
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -0.069, Max: 0.059, Count: 13
  Total Sequences Evaluated: 562

======================================================================
EXPERIMENT ROUND 17/100
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
  AGTACTGCTCAG
  CCGCGGAGTTAA
  GCCGGATATCGC
  ACGCAGGTGATC
  ATCGACGTGCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.248
  Max reward: 12.049
  With intrinsic bonuses: 9.263

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.7234, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3035

=== Surrogate Model Training ===
Total samples: 594

Training on 567 samples (removed 27 outliers)
Reward range: [6.66, 12.84], mean: 9.86
  Created 13 candidate models for data size 567
Current R2 threshold: -0.22999999999999998
  rf-tuned-l: R2 = 0.043 (std: 0.105)
  rf-tuned-xl: R2 = 0.035 (std: 0.107)
  gb-tuned-l: R2 = 0.066 (std: 0.111)
  gb-tuned-xl: R2 = 0.066 (std: 0.111)
  xgb-xl: R2 = -0.148 (std: 0.143)
  xgb-l: R2 = -0.148 (std: 0.143)
  mlp-adaptive-xl: R2 = -0.295 (std: 0.187)
  mlp-l: R2 = -0.124 (std: 0.149)
  svr-rbf-xl: R2 = 0.085 (std: 0.088)
  svr-poly-l: R2 = 0.085 (std: 0.088)
  knn-tuned-sqrt: R2 = -0.032 (std: 0.085)
  knn-tuned-l: R2 = -0.032 (std: 0.085)
  ridge: R2 = -0.028 (std: 0.049)

Model-based training with 12 models
Best R2: 0.085, Mean R2: -0.033
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.088 rf-tuned-xl:0.087 gb-tuned-l:0.090 gb-tuned-xl:0.090 xgb-xl:0.072 xgb-l:0.072 mlp-l:0.074 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.081 knn-tuned-l:0.081 ridge:0.082 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9651, entropy=0.7215, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2028
  Round 1/3: Mean predicted reward = 9.757
    Using performance-based weights
    Model weights: rf-tuned-l:0.088 rf-tuned-xl:0.087 gb-tuned-l:0.090 gb-tuned-xl:0.090 xgb-xl:0.072 xgb-l:0.072 mlp-l:0.074 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.081 knn-tuned-l:0.081 ridge:0.082 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9675, entropy=0.7152, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1716
  Round 2/3: Mean predicted reward = 9.850
    Using performance-based weights
    Model weights: rf-tuned-l:0.088 rf-tuned-xl:0.087 gb-tuned-l:0.090 gb-tuned-xl:0.090 xgb-xl:0.072 xgb-l:0.072 mlp-l:0.074 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.081 knn-tuned-l:0.081 ridge:0.082 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9667, entropy=0.7132, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1951
  Round 3/3: Mean predicted reward = 9.856

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 17 Results ---
  Mean Oracle Reward: 9.277
  Min Oracle Reward: 5.115
  Max Oracle Reward: 12.232
  Std Oracle Reward: 1.646
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: -0.033, Max: 0.085, Count: 13
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
  TGGCCACAAGTG
  GGGCTCCGAATA
  TCCAGGGAATGC
  AGCTTGACGGCC
  GAGCCGGATTCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.086
  Max reward: 12.435
  With intrinsic bonuses: 10.100

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9660, entropy=0.7048, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1861

=== Surrogate Model Training ===
Total samples: 626

Training on 596 samples (removed 30 outliers)
Reward range: [6.73, 12.84], mean: 9.88
  Created 13 candidate models for data size 596
Current R2 threshold: -0.21999999999999997
  rf-tuned-l: R2 = 0.076 (std: 0.086)
  rf-tuned-xl: R2 = 0.050 (std: 0.091)
  gb-tuned-l: R2 = 0.056 (std: 0.133)
  gb-tuned-xl: R2 = 0.056 (std: 0.133)
  xgb-xl: R2 = -0.134 (std: 0.113)
  xgb-l: R2 = -0.134 (std: 0.113)
  mlp-adaptive-xl: R2 = -0.237 (std: 0.160)
  mlp-l: R2 = -0.199 (std: 0.200)
  svr-rbf-xl: R2 = 0.111 (std: 0.085)
  svr-poly-l: R2 = 0.111 (std: 0.085)
  knn-tuned-sqrt: R2 = -0.009 (std: 0.066)
  knn-tuned-l: R2 = -0.009 (std: 0.066)
  ridge: R2 = -0.038 (std: 0.058)

Model-based training with 12 models
Best R2: 0.111, Mean R2: -0.023
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.090 rf-tuned-xl:0.088 gb-tuned-l:0.088 gb-tuned-xl:0.088 xgb-xl:0.073 xgb-l:0.073 mlp-l:0.068 svr-rbf-xl:0.093 svr-poly-l:0.093 knn-tuned-sqrt:0.083 knn-tuned-l:0.083 ridge:0.080 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9714, entropy=0.7167, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1296
  Round 1/3: Mean predicted reward = 9.761
    Using performance-based weights
    Model weights: rf-tuned-l:0.090 rf-tuned-xl:0.088 gb-tuned-l:0.088 gb-tuned-xl:0.088 xgb-xl:0.073 xgb-l:0.073 mlp-l:0.068 svr-rbf-xl:0.093 svr-poly-l:0.093 knn-tuned-sqrt:0.083 knn-tuned-l:0.083 ridge:0.080 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9712, entropy=0.7067, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1896
  Round 2/3: Mean predicted reward = 9.862
    Using performance-based weights
    Model weights: rf-tuned-l:0.090 rf-tuned-xl:0.088 gb-tuned-l:0.088 gb-tuned-xl:0.088 xgb-xl:0.073 xgb-l:0.073 mlp-l:0.068 svr-rbf-xl:0.093 svr-poly-l:0.093 knn-tuned-sqrt:0.083 knn-tuned-l:0.083 ridge:0.080 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9719, entropy=0.7033, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2189
  Round 3/3: Mean predicted reward = 9.861

  === Progress Analysis ===
  Status: NORMAL

--- Round 18 Results ---
  Mean Oracle Reward: 10.074
  Min Oracle Reward: 7.136
  Max Oracle Reward: 12.161
  Std Oracle Reward: 1.106
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: -0.023, Max: 0.111, Count: 13
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
  TGCGCGAGCACT
  AGTCTGGATCCA
  GACGAATGCTAT
  GGTACTCGCCGA
  GAACGCAGCTTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.959
  Max reward: 13.942
  With intrinsic bonuses: 9.984

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.7075, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0870

=== Surrogate Model Training ===
Total samples: 658

Training on 630 samples (removed 28 outliers)
Reward range: [6.66, 12.84], mean: 9.87
  Created 13 candidate models for data size 630
Current R2 threshold: -0.21
  rf-tuned-l: R2 = 0.090 (std: 0.072)
  rf-tuned-xl: R2 = 0.079 (std: 0.079)
  gb-tuned-l: R2 = 0.088 (std: 0.090)
  gb-tuned-xl: R2 = 0.088 (std: 0.090)
  xgb-xl: R2 = -0.127 (std: 0.110)
  xgb-l: R2 = -0.127 (std: 0.110)
  mlp-adaptive-xl: R2 = -0.126 (std: 0.053)
  mlp-l: R2 = -0.136 (std: 0.148)
  svr-rbf-xl: R2 = 0.107 (std: 0.069)
  svr-poly-l: R2 = 0.107 (std: 0.069)
  knn-tuned-sqrt: R2 = -0.028 (std: 0.063)
  knn-tuned-l: R2 = -0.028 (std: 0.063)
  ridge: R2 = -0.043 (std: 0.058)

Model-based training with 13 models
Best R2: 0.107, Mean R2: -0.004
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.084 rf-tuned-xl:0.083 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.068 mlp-l:0.067 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.074 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.7031, kl_div=0.0000
    Epoch 1: policy_loss=0.0043, value_loss=0.9690, entropy=0.7024, kl_div=0.0488
  Round 1/3: Mean predicted reward = 9.726
    Using performance-based weights
    Model weights: rf-tuned-l:0.084 rf-tuned-xl:0.083 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.068 mlp-l:0.067 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.074 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9700, entropy=0.6962, kl_div=0.0000
    Epoch 1: policy_loss=-0.0111, value_loss=0.9700, entropy=0.6964, kl_div=-0.0119
  Round 2/3: Mean predicted reward = 9.739
    Using performance-based weights
    Model weights: rf-tuned-l:0.084 rf-tuned-xl:0.083 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.068 mlp-l:0.067 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.074 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.7006, kl_div=0.0000
    Epoch 1: policy_loss=-0.0033, value_loss=0.9685, entropy=0.7009, kl_div=-0.0133
  Round 3/3: Mean predicted reward = 9.799

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 19 Results ---
  Mean Oracle Reward: 9.967
  Min Oracle Reward: 7.686
  Max Oracle Reward: 13.807
  Std Oracle Reward: 1.374
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.004, Max: 0.107, Count: 13
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
  CACTATTGGGAC
  ACTTCCGGTGAA
  TCTGACCACGGG
  TTCACGGCGAAG
  AGCCTGTGCGAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.727
  Max reward: 12.277
  With intrinsic bonuses: 9.696

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9674, entropy=0.6995, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2618

=== Surrogate Model Training ===
Total samples: 690

Training on 656 samples (removed 34 outliers)
Reward range: [6.73, 12.84], mean: 9.89
  Created 13 candidate models for data size 656
Current R2 threshold: -0.19999999999999998
  rf-tuned-l: R2 = 0.095 (std: 0.108)
  rf-tuned-xl: R2 = 0.101 (std: 0.104)
  gb-tuned-l: R2 = 0.087 (std: 0.116)
  gb-tuned-xl: R2 = 0.087 (std: 0.116)
  xgb-xl: R2 = -0.113 (std: 0.127)
  xgb-l: R2 = -0.113 (std: 0.127)
  mlp-adaptive-xl: R2 = -0.136 (std: 0.168)
  mlp-l: R2 = -0.141 (std: 0.144)
  svr-rbf-xl: R2 = 0.120 (std: 0.106)
  svr-poly-l: R2 = 0.120 (std: 0.106)
  knn-tuned-sqrt: R2 = 0.016 (std: 0.101)
  knn-tuned-l: R2 = 0.016 (std: 0.101)
  ridge: R2 = -0.034 (std: 0.057)

Model-based training with 13 models
Best R2: 0.120, Mean R2: 0.008
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.084 rf-tuned-xl:0.084 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.066 mlp-l:0.066 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 ridge:0.073 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9667, entropy=0.7007, kl_div=0.0000
    Epoch 1: policy_loss=-0.0460, value_loss=0.9667, entropy=0.7018, kl_div=0.0304
  Round 1/3: Mean predicted reward = 9.737
    Using performance-based weights
    Model weights: rf-tuned-l:0.084 rf-tuned-xl:0.084 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.066 mlp-l:0.066 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 ridge:0.073 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.6954, kl_div=0.0000
    Epoch 1: policy_loss=0.0360, value_loss=0.9703, entropy=0.7023, kl_div=-0.2990
  Round 2/3: Mean predicted reward = 9.893
    Using performance-based weights
    Model weights: rf-tuned-l:0.084 rf-tuned-xl:0.084 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.066 mlp-l:0.066 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 ridge:0.073 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9646, entropy=0.7063, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1332
  Round 3/3: Mean predicted reward = 9.844

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 20 Results ---
  Mean Oracle Reward: 9.725
  Min Oracle Reward: 5.351
  Max Oracle Reward: 11.993
  Std Oracle Reward: 1.550
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.008, Max: 0.120, Count: 13
  Total Sequences Evaluated: 690

======================================================================
EXPERIMENT ROUND 21/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 690

--- Round 21 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GGCTCGATAGCA
  GCGTATAGCATC
  ACAGTGCATGAT
  CCGTTGAAGAGC
  GCAAGTCAATGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.103
  Max reward: 13.280
  With intrinsic bonuses: 10.130

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.7128, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2816

=== Surrogate Model Training ===
Total samples: 722

Training on 685 samples (removed 37 outliers)
Reward range: [6.81, 12.84], mean: 9.91
  Created 13 candidate models for data size 685
Current R2 threshold: -0.19
  rf-tuned-l: R2 = 0.114 (std: 0.115)
  rf-tuned-xl: R2 = 0.113 (std: 0.107)
  gb-tuned-l: R2 = 0.094 (std: 0.130)
  gb-tuned-xl: R2 = 0.094 (std: 0.130)
  xgb-xl: R2 = -0.053 (std: 0.137)
  xgb-l: R2 = -0.053 (std: 0.137)
  mlp-adaptive-xl: R2 = -0.108 (std: 0.103)
  mlp-l: R2 = -0.102 (std: 0.047)
  svr-rbf-xl: R2 = 0.152 (std: 0.109)
  svr-poly-l: R2 = 0.152 (std: 0.109)
  knn-tuned-sqrt: R2 = 0.040 (std: 0.107)
  knn-tuned-l: R2 = 0.040 (std: 0.107)
  ridge: R2 = -0.015 (std: 0.049)

Model-based training with 13 models
Best R2: 0.152, Mean R2: 0.036
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.083 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.066 mlp-l:0.067 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 ridge:0.073 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.7096, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2177
  Round 1/3: Mean predicted reward = 9.807
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.083 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.066 mlp-l:0.067 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 ridge:0.073 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9682, entropy=0.7111, kl_div=0.0000
    Epoch 1: policy_loss=-0.0513, value_loss=0.9682, entropy=0.7109, kl_div=0.0128
  Round 2/3: Mean predicted reward = 9.881
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.083 gb-tuned-l:0.081 gb-tuned-xl:0.081 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.066 mlp-l:0.067 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 ridge:0.073 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9651, entropy=0.7240, kl_div=0.0000
    Epoch 1: policy_loss=-0.0645, value_loss=0.9652, entropy=0.7256, kl_div=-0.1943
  Round 3/3: Mean predicted reward = 9.962

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 21 Results ---
  Mean Oracle Reward: 10.127
  Min Oracle Reward: 5.695
  Max Oracle Reward: 13.365
  Std Oracle Reward: 1.262
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.036, Max: 0.152, Count: 13
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
  CCGCAGGAATGT
  AGGCTGTAGACC
  TTTGCACCAGGA
  CGGGATCATCAT
  CGCGAGCGTTAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.908
  Max reward: 11.635
  With intrinsic bonuses: 9.886

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.7015, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1552

=== Surrogate Model Training ===
Total samples: 754

Training on 717 samples (removed 37 outliers)
Reward range: [6.81, 12.84], mean: 9.91
  Created 13 candidate models for data size 717
Current R2 threshold: -0.18
  rf-tuned-l: R2 = 0.111 (std: 0.133)
  rf-tuned-xl: R2 = 0.124 (std: 0.122)
  gb-tuned-l: R2 = 0.096 (std: 0.141)
  gb-tuned-xl: R2 = 0.096 (std: 0.141)
  xgb-xl: R2 = -0.045 (std: 0.154)
  xgb-l: R2 = -0.045 (std: 0.154)
  mlp-adaptive-xl: R2 = -0.169 (std: 0.153)
  mlp-l: R2 = -0.169 (std: 0.157)
  svr-rbf-xl: R2 = 0.158 (std: 0.116)
  svr-poly-l: R2 = 0.158 (std: 0.116)
  knn-tuned-sqrt: R2 = 0.048 (std: 0.140)
  knn-tuned-l: R2 = 0.048 (std: 0.140)
  ridge: R2 = -0.013 (std: 0.051)

Model-based training with 13 models
Best R2: 0.158, Mean R2: 0.031
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.084 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.071 xgb-l:0.071 mlp-adaptive-xl:0.063 mlp-l:0.063 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.073 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=0.7093, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0803
  Round 1/3: Mean predicted reward = 9.805
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.084 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.071 xgb-l:0.071 mlp-adaptive-xl:0.063 mlp-l:0.063 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.073 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.7033, kl_div=0.0000
    Epoch 1: policy_loss=-0.0515, value_loss=0.9691, entropy=0.7042, kl_div=0.0006
  Round 2/3: Mean predicted reward = 9.934
    Using performance-based weights
    Model weights: rf-tuned-l:0.083 rf-tuned-xl:0.084 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.071 xgb-l:0.071 mlp-adaptive-xl:0.063 mlp-l:0.063 svr-rbf-xl:0.087 svr-poly-l:0.087 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 ridge:0.073 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.7071, kl_div=0.0000
    Epoch 1: policy_loss=-0.0380, value_loss=0.9696, entropy=0.7110, kl_div=-0.0618
  Round 3/3: Mean predicted reward = 9.934

  === Progress Analysis ===
  Status: NORMAL

--- Round 22 Results ---
  Mean Oracle Reward: 9.909
  Min Oracle Reward: 7.392
  Max Oracle Reward: 11.653
  Std Oracle Reward: 1.032
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.031, Max: 0.158, Count: 13
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
  AGGGTCCCACTG
  TACTAGGCGCAT
  TACGAGTGGCAC
  CAGATGCCGTAG
  GCAGTCCATGGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.850
  Max reward: 12.871
  With intrinsic bonuses: 9.879

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9721, entropy=0.7109, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1115

=== Surrogate Model Training ===
Total samples: 786

Training on 748 samples (removed 38 outliers)
Reward range: [6.73, 12.84], mean: 9.91
  Created 13 candidate models for data size 748
Current R2 threshold: -0.16999999999999998
  rf-tuned-l: R2 = 0.110 (std: 0.102)
  rf-tuned-xl: R2 = 0.096 (std: 0.085)
  gb-tuned-l: R2 = 0.125 (std: 0.106)
  gb-tuned-xl: R2 = 0.125 (std: 0.106)
  xgb-xl: R2 = -0.050 (std: 0.131)
  xgb-l: R2 = -0.050 (std: 0.131)
  mlp-adaptive-xl: R2 = -0.067 (std: 0.132)
  mlp-l: R2 = -0.065 (std: 0.041)
  svr-rbf-xl: R2 = 0.159 (std: 0.097)
  svr-poly-l: R2 = 0.159 (std: 0.097)
  knn-tuned-sqrt: R2 = 0.028 (std: 0.100)
  knn-tuned-l: R2 = 0.028 (std: 0.100)
  ridge: R2 = -0.006 (std: 0.048)

Model-based training with 13 models
Best R2: 0.159, Mean R2: 0.046
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.068 mlp-l:0.069 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.073 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9670, entropy=0.7109, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0906
  Round 1/3: Mean predicted reward = 9.799
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.068 mlp-l:0.069 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.073 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.7202, kl_div=0.0000
    Epoch 1: policy_loss=-0.0225, value_loss=0.9705, entropy=0.7226, kl_div=0.0233
  Round 2/3: Mean predicted reward = 9.952
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.068 mlp-l:0.069 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.073 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.7203, kl_div=0.0000
    Epoch 1: policy_loss=-0.0450, value_loss=0.9694, entropy=0.7239, kl_div=-0.0055
  Round 3/3: Mean predicted reward = 10.022

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 23 Results ---
  Mean Oracle Reward: 9.854
  Min Oracle Reward: 3.413
  Max Oracle Reward: 12.985
  Std Oracle Reward: 1.735
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.046, Max: 0.159, Count: 13
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
  CGAAGTGCCGTC
  CGCGAGGACTCT
  TTACTCAGAGCG
  GGCAACGCGTCT
  CGGTAACCCGGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.850
  Max reward: 11.435
  With intrinsic bonuses: 9.841

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.7268, kl_div=0.0000
    Epoch 1: policy_loss=-0.0169, value_loss=0.9690, entropy=0.7273, kl_div=0.0330

=== Surrogate Model Training ===
Total samples: 818

Training on 779 samples (removed 39 outliers)
Reward range: [6.81, 12.84], mean: 9.91
  Created 13 candidate models for data size 779
Current R2 threshold: -0.15999999999999998
  rf-tuned-l: R2 = 0.080 (std: 0.080)
  rf-tuned-xl: R2 = 0.100 (std: 0.078)
  gb-tuned-l: R2 = 0.114 (std: 0.078)
  gb-tuned-xl: R2 = 0.114 (std: 0.078)
  xgb-xl: R2 = -0.110 (std: 0.142)
  xgb-l: R2 = -0.110 (std: 0.142)
  mlp-adaptive-xl: R2 = -0.060 (std: 0.085)
  mlp-l: R2 = -0.059 (std: 0.095)
  svr-rbf-xl: R2 = 0.155 (std: 0.081)
  svr-poly-l: R2 = 0.155 (std: 0.081)
  knn-tuned-sqrt: R2 = 0.033 (std: 0.102)
  knn-tuned-l: R2 = 0.033 (std: 0.102)
  ridge: R2 = -0.007 (std: 0.045)

Model-based training with 13 models
Best R2: 0.155, Mean R2: 0.034
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.082 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.070 mlp-l:0.070 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 ridge:0.074 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=0.7167, kl_div=0.0000
    Epoch 1: policy_loss=-0.0109, value_loss=0.9675, entropy=0.7164, kl_div=0.0335
  Round 1/3: Mean predicted reward = 9.822
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.082 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.070 mlp-l:0.070 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 ridge:0.074 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9716, entropy=0.7374, kl_div=0.0000
    Epoch 1: policy_loss=-0.0099, value_loss=0.9716, entropy=0.7385, kl_div=-0.0122
  Round 2/3: Mean predicted reward = 9.834
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.082 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.066 xgb-l:0.066 mlp-adaptive-xl:0.070 mlp-l:0.070 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 ridge:0.074 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9669, entropy=0.7343, kl_div=0.0000
    Epoch 1: policy_loss=-0.0042, value_loss=0.9669, entropy=0.7352, kl_div=-0.0066
  Round 3/3: Mean predicted reward = 9.874

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 24 Results ---
  Mean Oracle Reward: 9.865
  Min Oracle Reward: 8.027
  Max Oracle Reward: 11.408
  Std Oracle Reward: 0.904
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.034, Max: 0.155, Count: 13
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
  ATCCATCGGGGA
  GCGACCGTTGCA
  TGTGCGAGCCAC
  CCTAGTACGGGC
  ATCGCGTTAAGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.827
  Max reward: 12.218
  With intrinsic bonuses: 9.841

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9673, entropy=0.6978, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2308

=== Surrogate Model Training ===
Total samples: 850

Training on 812 samples (removed 38 outliers)
Reward range: [6.73, 12.84], mean: 9.91
  Created 13 candidate models for data size 812
Current R2 threshold: -0.15
  rf-tuned-l: R2 = 0.114 (std: 0.070)
  rf-tuned-xl: R2 = 0.121 (std: 0.068)
  gb-tuned-l: R2 = 0.142 (std: 0.077)
  gb-tuned-xl: R2 = 0.142 (std: 0.077)
  xgb-xl: R2 = -0.067 (std: 0.081)
  xgb-l: R2 = -0.067 (std: 0.081)
  mlp-adaptive-xl: R2 = -0.011 (std: 0.077)
  mlp-l: R2 = -0.084 (std: 0.104)
  svr-rbf-xl: R2 = 0.168 (std: 0.080)
  svr-poly-l: R2 = 0.168 (std: 0.080)
  knn-tuned-sqrt: R2 = 0.033 (std: 0.086)
  knn-tuned-l: R2 = 0.033 (std: 0.086)
  ridge: R2 = 0.001 (std: 0.040)

Model-based training with 13 models
Best R2: 0.168, Mean R2: 0.053
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.082 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.072 mlp-l:0.067 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.073 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.7307, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1849
  Round 1/3: Mean predicted reward = 9.753
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.082 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.072 mlp-l:0.067 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.073 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.7296, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2724
  Round 2/3: Mean predicted reward = 9.891
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.082 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.072 mlp-l:0.067 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.073 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9721, entropy=0.7133, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2131
  Round 3/3: Mean predicted reward = 9.952

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 25 Results ---
  Mean Oracle Reward: 9.790
  Min Oracle Reward: 7.390
  Max Oracle Reward: 12.232
  Std Oracle Reward: 1.218
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.053, Max: 0.168, Count: 13
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
  AACTTGGGCCGC
  CGCGAGGCTTCA
  CCTGCTCAGGGA
  GAAATTGCGCCG
  AAACGTTGTCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.139
  Max reward: 12.144
  With intrinsic bonuses: 10.094

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.7151, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3046

=== Surrogate Model Training ===
Total samples: 882

Training on 842 samples (removed 40 outliers)
Reward range: [6.81, 12.84], mean: 9.93
  Created 13 candidate models for data size 842
Current R2 threshold: -0.13999999999999999
  rf-tuned-l: R2 = 0.128 (std: 0.065)
  rf-tuned-xl: R2 = 0.120 (std: 0.071)
  gb-tuned-l: R2 = 0.134 (std: 0.087)
  gb-tuned-xl: R2 = 0.134 (std: 0.087)
  xgb-xl: R2 = -0.081 (std: 0.134)
  xgb-l: R2 = -0.081 (std: 0.134)
  mlp-adaptive-xl: R2 = 0.001 (std: 0.098)
  mlp-l: R2 = 0.009 (std: 0.098)
  svr-rbf-xl: R2 = 0.168 (std: 0.075)
  svr-poly-l: R2 = 0.168 (std: 0.075)
  knn-tuned-sqrt: R2 = 0.034 (std: 0.095)
  knn-tuned-l: R2 = 0.034 (std: 0.095)
  ridge: R2 = 0.002 (std: 0.038)

Model-based training with 13 models
Best R2: 0.168, Mean R2: 0.059
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.072 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.072 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.7244, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3277
  Round 1/3: Mean predicted reward = 9.839
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.072 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.072 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9676, entropy=0.7250, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3651
  Round 2/3: Mean predicted reward = 9.712
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.072 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.072 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.6986, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4688
  Round 3/3: Mean predicted reward = 9.794

  === Progress Analysis ===
  Status: NORMAL

--- Round 26 Results ---
  Mean Oracle Reward: 10.132
  Min Oracle Reward: 6.379
  Max Oracle Reward: 12.087
  Std Oracle Reward: 1.262
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.059, Max: 0.168, Count: 13
  Total Sequences Evaluated: 882

======================================================================
EXPERIMENT ROUND 27/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 882

--- Round 27 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TACTAGCGGCCG
  CACGCGTGACGT
  GACGACGCATGT
  CGGTTCGCCAGA
  CGCAGGCGTATC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.963
  Max reward: 12.457
  With intrinsic bonuses: 10.007

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.7091, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6254

=== Surrogate Model Training ===
Total samples: 914

Training on 874 samples (removed 40 outliers)
Reward range: [6.81, 12.84], mean: 9.93
  Created 13 candidate models for data size 874
Current R2 threshold: -0.12999999999999998
  rf-tuned-l: R2 = 0.115 (std: 0.050)
  rf-tuned-xl: R2 = 0.113 (std: 0.055)
  gb-tuned-l: R2 = 0.141 (std: 0.062)
  gb-tuned-xl: R2 = 0.141 (std: 0.062)
  xgb-xl: R2 = -0.055 (std: 0.076)
  xgb-l: R2 = -0.055 (std: 0.076)
  mlp-adaptive-xl: R2 = -0.094 (std: 0.058)
  mlp-l: R2 = -0.004 (std: 0.089)
  svr-rbf-xl: R2 = 0.166 (std: 0.071)
  svr-poly-l: R2 = 0.166 (std: 0.071)
  knn-tuned-sqrt: R2 = 0.034 (std: 0.092)
  knn-tuned-l: R2 = 0.034 (std: 0.092)
  ridge: R2 = -0.001 (std: 0.030)

Model-based training with 13 models
Best R2: 0.166, Mean R2: 0.054
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.066 mlp-l:0.072 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.072 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.7084, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4098
  Round 1/3: Mean predicted reward = 9.688
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.066 mlp-l:0.072 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.072 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.7125, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4394
  Round 2/3: Mean predicted reward = 9.755
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.066 mlp-l:0.072 svr-rbf-xl:0.086 svr-poly-l:0.086 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.072 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.6939, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5639
  Round 3/3: Mean predicted reward = 9.910

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 27 Results ---
  Mean Oracle Reward: 9.996
  Min Oracle Reward: 6.739
  Max Oracle Reward: 12.355
  Std Oracle Reward: 1.217
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.054, Max: 0.166, Count: 13
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
  CCTCGCGGAGAT
  AGACCTTGGCCG
  TCGACGGCGATC
  CGCATCTGAGGC
  CACTTTGCAGGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.762
  Max reward: 12.958
  With intrinsic bonuses: 9.714

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9666, entropy=0.6904, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4086

=== Surrogate Model Training ===
Total samples: 946

Training on 904 samples (removed 42 outliers)
Reward range: [6.81, 12.84], mean: 9.94
  Created 13 candidate models for data size 904
Current R2 threshold: -0.12
  rf-tuned-l: R2 = 0.128 (std: 0.061)
  rf-tuned-xl: R2 = 0.132 (std: 0.058)
  gb-tuned-l: R2 = 0.156 (std: 0.058)
  gb-tuned-xl: R2 = 0.156 (std: 0.058)
  xgb-xl: R2 = -0.039 (std: 0.109)
  xgb-l: R2 = -0.039 (std: 0.109)
  mlp-adaptive-xl: R2 = -0.025 (std: 0.082)
  mlp-l: R2 = 0.017 (std: 0.107)
  svr-rbf-xl: R2 = 0.174 (std: 0.070)
  svr-poly-l: R2 = 0.174 (std: 0.070)
  knn-tuned-sqrt: R2 = 0.045 (std: 0.068)
  knn-tuned-l: R2 = 0.045 (std: 0.068)
  ridge: R2 = 0.002 (std: 0.034)

Model-based training with 13 models
Best R2: 0.174, Mean R2: 0.071
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.070 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.072 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.6862, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2461
  Round 1/3: Mean predicted reward = 9.837
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.070 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.072 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9707, entropy=0.6881, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1723
  Round 2/3: Mean predicted reward = 9.792
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.070 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.072 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9665, entropy=0.6777, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2178
  Round 3/3: Mean predicted reward = 9.967

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 28 Results ---
  Mean Oracle Reward: 9.726
  Min Oracle Reward: 5.005
  Max Oracle Reward: 12.902
  Std Oracle Reward: 1.805
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.071, Max: 0.174, Count: 13
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
  ACGACCGGTTGC
  TACCGACGGCGT
  TGTGCCAGAGAC
  GGCATCCCGAGT
  GGCCATAGCTGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.094
  Max reward: 12.723
  With intrinsic bonuses: 10.122

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.6971, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0843

=== Surrogate Model Training ===
Total samples: 978

Training on 936 samples (removed 42 outliers)
Reward range: [6.81, 12.84], mean: 9.94
  Created 13 candidate models for data size 936
Current R2 threshold: -0.10999999999999999
  rf-tuned-l: R2 = 0.143 (std: 0.054)
  rf-tuned-xl: R2 = 0.145 (std: 0.066)
  gb-tuned-l: R2 = 0.169 (std: 0.028)
  gb-tuned-xl: R2 = 0.169 (std: 0.028)
  xgb-xl: R2 = -0.012 (std: 0.129)
  xgb-l: R2 = -0.012 (std: 0.129)
  mlp-adaptive-xl: R2 = -0.012 (std: 0.113)
  mlp-l: R2 = 0.032 (std: 0.080)
  svr-rbf-xl: R2 = 0.185 (std: 0.077)
  svr-poly-l: R2 = 0.185 (std: 0.077)
  knn-tuned-sqrt: R2 = 0.076 (std: 0.091)
  knn-tuned-l: R2 = 0.076 (std: 0.091)
  ridge: R2 = 0.001 (std: 0.038)

Model-based training with 13 models
Best R2: 0.185, Mean R2: 0.088
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.069 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.070 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9704, entropy=0.6815, kl_div=0.0000
    Epoch 1: policy_loss=0.0027, value_loss=0.9704, entropy=0.6814, kl_div=0.0452
  Round 1/3: Mean predicted reward = 9.722
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.069 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.070 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.6994, kl_div=0.0000
    Epoch 1: policy_loss=-0.0240, value_loss=0.9697, entropy=0.7011, kl_div=-0.0278
  Round 2/3: Mean predicted reward = 9.808
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.069 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.070 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.6930, kl_div=0.0000
    Epoch 1: policy_loss=-0.0117, value_loss=0.9688, entropy=0.6943, kl_div=-0.0054
  Round 3/3: Mean predicted reward = 10.011

  === Progress Analysis ===
  Status: NORMAL

--- Round 29 Results ---
  Mean Oracle Reward: 10.078
  Min Oracle Reward: 8.004
  Max Oracle Reward: 12.631
  Std Oracle Reward: 1.116
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.088, Max: 0.185, Count: 13
  Total Sequences Evaluated: 978

======================================================================
EXPERIMENT ROUND 30/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 978

--- Round 30 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTCGGCGTGCAA
  CGGGATTGACCA
  TGACGTCACGGA
  AGCTAGCCAGTG
  GTGATACGACTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.129
  Max reward: 12.782
  With intrinsic bonuses: 10.130

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9711, entropy=0.6975, kl_div=0.0000
    Epoch 1: policy_loss=-0.0630, value_loss=0.9711, entropy=0.7064, kl_div=-0.0301

=== Surrogate Model Training ===
Total samples: 1010

Training on 966 samples (removed 44 outliers)
Reward range: [6.81, 12.84], mean: 9.95
  Created 13 candidate models for data size 966
Current R2 threshold: -0.09999999999999998
  rf-tuned-l: R2 = 0.118 (std: 0.073)
  rf-tuned-xl: R2 = 0.108 (std: 0.071)
  gb-tuned-l: R2 = 0.156 (std: 0.052)
  gb-tuned-xl: R2 = 0.156 (std: 0.052)
  xgb-xl: R2 = -0.041 (std: 0.139)
  xgb-l: R2 = -0.041 (std: 0.139)
  mlp-adaptive-xl: R2 = 0.014 (std: 0.069)
  mlp-l: R2 = -0.007 (std: 0.102)
  svr-rbf-xl: R2 = 0.168 (std: 0.083)
  svr-poly-l: R2 = 0.168 (std: 0.083)
  knn-tuned-sqrt: R2 = 0.055 (std: 0.099)
  knn-tuned-l: R2 = 0.055 (std: 0.099)
  ridge: R2 = -0.004 (std: 0.038)

Model-based training with 13 models
Best R2: 0.168, Mean R2: 0.070
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.073 mlp-l:0.071 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9722, entropy=0.6967, kl_div=0.0000
    Epoch 1: policy_loss=-0.0761, value_loss=0.9721, entropy=0.7015, kl_div=0.0089
  Round 1/3: Mean predicted reward = 9.739
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.073 mlp-l:0.071 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9682, entropy=0.6904, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0597
  Round 2/3: Mean predicted reward = 9.942
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.073 mlp-l:0.071 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.7082, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3138
  Round 3/3: Mean predicted reward = 10.008

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 30 Results ---
  Mean Oracle Reward: 10.135
  Min Oracle Reward: 6.403
  Max Oracle Reward: 12.966
  Std Oracle Reward: 1.281
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.070, Max: 0.168, Count: 13
  Total Sequences Evaluated: 1010

======================================================================
EXPERIMENT ROUND 31/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1010
  Consistent improvement, increasing LR to 0.000327

--- Round 31 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCCACCTATGGG
  GGTCACTCCGGA
  CGTGGAACTCGC
  GCAACTGCTAGG
  GTGCGTCCAGCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.073
  Max reward: 11.487
  With intrinsic bonuses: 10.107

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9704, entropy=0.6936, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4657

=== Surrogate Model Training ===
Total samples: 1042

Training on 998 samples (removed 44 outliers)
Reward range: [6.81, 13.03], mean: 9.96
  Created 13 candidate models for data size 998
Current R2 threshold: -0.09
  rf-tuned-l: R2 = 0.139 (std: 0.082)
  rf-tuned-xl: R2 = 0.117 (std: 0.082)
  gb-tuned-l: R2 = 0.164 (std: 0.049)
  gb-tuned-xl: R2 = 0.164 (std: 0.049)
  xgb-xl: R2 = -0.036 (std: 0.146)
  xgb-l: R2 = -0.036 (std: 0.146)
  mlp-adaptive-xl: R2 = -0.019 (std: 0.059)
  mlp-l: R2 = -0.018 (std: 0.075)
  svr-rbf-xl: R2 = 0.171 (std: 0.086)
  svr-poly-l: R2 = 0.171 (std: 0.086)
  knn-tuned-sqrt: R2 = 0.069 (std: 0.086)
  knn-tuned-l: R2 = 0.069 (std: 0.086)
  ridge: R2 = -0.002 (std: 0.037)

Model-based training with 13 models
Best R2: 0.171, Mean R2: 0.073
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.070 mlp-l:0.070 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.7082, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0822
  Round 1/3: Mean predicted reward = 9.830
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.070 mlp-l:0.070 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.7062, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2108
  Round 2/3: Mean predicted reward = 9.895
    Using performance-based weights
    Model weights: rf-tuned-l:0.082 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.070 mlp-l:0.070 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.6901, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6616
  Round 3/3: Mean predicted reward = 9.998

  === Progress Analysis ===
  Status: NORMAL

--- Round 31 Results ---
  Mean Oracle Reward: 10.128
  Min Oracle Reward: 5.820
  Max Oracle Reward: 11.638
  Std Oracle Reward: 1.185
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.073, Max: 0.171, Count: 13
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
  GCCACAGGTCTG
  CCGCGATGGATC
  GCCTGACGAGCT
  CCCAGTGCAGTG
  TTGGGGACACCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.738
  Max reward: 12.692
  With intrinsic bonuses: 9.769

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9668, entropy=0.6785, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2119

=== Surrogate Model Training ===
Total samples: 1074

Training on 1030 samples (removed 44 outliers)
Reward range: [6.81, 13.03], mean: 9.95
  Created 13 candidate models for data size 1030
Current R2 threshold: -0.07999999999999999
  rf-tuned-l: R2 = 0.122 (std: 0.051)
  rf-tuned-xl: R2 = 0.121 (std: 0.063)
  gb-tuned-l: R2 = 0.170 (std: 0.049)
  gb-tuned-xl: R2 = 0.170 (std: 0.049)
  xgb-xl: R2 = -0.062 (std: 0.107)
  xgb-l: R2 = -0.062 (std: 0.107)
  mlp-adaptive-xl: R2 = 0.005 (std: 0.066)
  mlp-l: R2 = 0.021 (std: 0.058)
  svr-rbf-xl: R2 = 0.176 (std: 0.064)
  svr-poly-l: R2 = 0.176 (std: 0.064)
  knn-tuned-sqrt: R2 = 0.044 (std: 0.080)
  knn-tuned-l: R2 = 0.044 (std: 0.080)
  ridge: R2 = 0.001 (std: 0.036)

Model-based training with 13 models
Best R2: 0.176, Mean R2: 0.071
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.072 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9671, entropy=0.6774, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2678
  Round 1/3: Mean predicted reward = 9.895
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.072 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9706, entropy=0.6868, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2816
  Round 2/3: Mean predicted reward = 9.974
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.067 xgb-l:0.067 mlp-adaptive-xl:0.072 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.075 knn-tuned-l:0.075 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9659, entropy=0.6789, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3782
  Round 3/3: Mean predicted reward = 9.950

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 32 Results ---
  Mean Oracle Reward: 9.743
  Min Oracle Reward: 6.941
  Max Oracle Reward: 12.626
  Std Oracle Reward: 1.274
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.071, Max: 0.176, Count: 13
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
  CTGCGCGACTAG
  AACGCTCGGGTC
  AGGAGCTACCTG
  GGTGCACGACTC
  AAGCTCTGGCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.206
  Max reward: 12.574
  With intrinsic bonuses: 10.246

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9664, entropy=0.6707, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4397

=== Surrogate Model Training ===
Total samples: 1106

Training on 1061 samples (removed 45 outliers)
Reward range: [6.82, 13.03], mean: 9.96
  Created 13 candidate models for data size 1061
Current R2 threshold: -0.06999999999999998
  rf-tuned-l: R2 = 0.130 (std: 0.054)
  rf-tuned-xl: R2 = 0.131 (std: 0.051)
  gb-tuned-l: R2 = 0.171 (std: 0.045)
  gb-tuned-xl: R2 = 0.171 (std: 0.044)
  xgb-xl: R2 = -0.043 (std: 0.156)
  xgb-l: R2 = -0.043 (std: 0.156)
  mlp-adaptive-xl: R2 = -0.014 (std: 0.074)
  mlp-l: R2 = 0.052 (std: 0.081)
  svr-rbf-xl: R2 = 0.187 (std: 0.054)
  svr-poly-l: R2 = 0.187 (std: 0.054)
  knn-tuned-sqrt: R2 = 0.079 (std: 0.087)
  knn-tuned-l: R2 = 0.079 (std: 0.087)
  ridge: R2 = 0.003 (std: 0.037)

Model-based training with 13 models
Best R2: 0.187, Mean R2: 0.084
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.069 mlp-l:0.074 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9676, entropy=0.6774, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4216
  Round 1/3: Mean predicted reward = 9.807
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.069 mlp-l:0.074 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9717, entropy=0.6759, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4197
  Round 2/3: Mean predicted reward = 9.953
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.069 mlp-l:0.074 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.076 knn-tuned-l:0.076 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9676, entropy=0.6854, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4628
  Round 3/3: Mean predicted reward = 10.042

  === Progress Analysis ===
  Status: NORMAL

--- Round 33 Results ---
  Mean Oracle Reward: 10.228
  Min Oracle Reward: 6.896
  Max Oracle Reward: 12.701
  Std Oracle Reward: 1.196
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.084, Max: 0.187, Count: 13
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
  GCATCATGGCCG
  ATGGGCTACACG
  GGGATTGCACAC
  GCTCGAGACGTC
  CCGGGATTAGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.057
  Max reward: 12.425
  With intrinsic bonuses: 10.042

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9666, entropy=0.6945, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1702

=== Surrogate Model Training ===
Total samples: 1138

Training on 1089 samples (removed 49 outliers)
Reward range: [6.97, 12.84], mean: 9.97
  Created 13 candidate models for data size 1089
Current R2 threshold: -0.06
  rf-tuned-l: R2 = 0.137 (std: 0.047)
  rf-tuned-xl: R2 = 0.138 (std: 0.069)
  gb-tuned-l: R2 = 0.193 (std: 0.041)
  gb-tuned-xl: R2 = 0.193 (std: 0.041)
  xgb-xl: R2 = -0.020 (std: 0.141)
  xgb-l: R2 = -0.020 (std: 0.141)
  mlp-adaptive-xl: R2 = -0.015 (std: 0.089)
  mlp-l: R2 = 0.032 (std: 0.103)
  svr-rbf-xl: R2 = 0.190 (std: 0.075)
  svr-poly-l: R2 = 0.190 (std: 0.075)
  knn-tuned-sqrt: R2 = 0.039 (std: 0.103)
  knn-tuned-l: R2 = 0.039 (std: 0.103)
  ridge: R2 = -0.001 (std: 0.037)

Model-based training with 13 models
Best R2: 0.193, Mean R2: 0.084
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.069 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.070 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9712, entropy=0.6646, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1263
  Round 1/3: Mean predicted reward = 9.756
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.069 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.070 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9668, entropy=0.6907, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1251
  Round 2/3: Mean predicted reward = 9.838
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.069 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.070 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.6636, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1415
  Round 3/3: Mean predicted reward = 9.946

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 34 Results ---
  Mean Oracle Reward: 9.981
  Min Oracle Reward: 5.671
  Max Oracle Reward: 12.505
  Std Oracle Reward: 1.308
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.084, Max: 0.193, Count: 13
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
  ACCCGAGTTGCG
  CGTCGACCATGG
  GGGACGCACTTC
  GGCACCTGGATC
  CGGTGATCGCAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.053
  Max reward: 11.797
  With intrinsic bonuses: 10.051

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.6517, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1854

=== Surrogate Model Training ===
Total samples: 1170

Training on 1120 samples (removed 50 outliers)
Reward range: [6.97, 12.84], mean: 9.98
  Created 13 candidate models for data size 1120
Current R2 threshold: -0.04999999999999999
  rf-tuned-l: R2 = 0.142 (std: 0.055)
  rf-tuned-xl: R2 = 0.141 (std: 0.047)
  gb-tuned-l: R2 = 0.190 (std: 0.036)
  gb-tuned-xl: R2 = 0.191 (std: 0.035)
  xgb-xl: R2 = -0.020 (std: 0.130)
  xgb-l: R2 = -0.020 (std: 0.130)
  mlp-adaptive-xl: R2 = 0.061 (std: 0.068)
  mlp-l: R2 = 0.042 (std: 0.057)
  svr-rbf-xl: R2 = 0.195 (std: 0.065)
  svr-poly-l: R2 = 0.195 (std: 0.065)
  knn-tuned-sqrt: R2 = 0.055 (std: 0.077)
  knn-tuned-l: R2 = 0.055 (std: 0.077)
  ridge: R2 = -0.003 (std: 0.035)

Model-based training with 13 models
Best R2: 0.195, Mean R2: 0.094
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.074 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.070 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.6379, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7604
  Round 1/3: Mean predicted reward = 9.823
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.074 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.070 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.6416, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4290
  Round 2/3: Mean predicted reward = 9.938
    Using performance-based weights
    Model weights: rf-tuned-l:0.080 rf-tuned-xl:0.080 gb-tuned-l:0.084 gb-tuned-xl:0.084 xgb-xl:0.068 xgb-l:0.068 mlp-adaptive-xl:0.074 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.070 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.6573, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8052
  Round 3/3: Mean predicted reward = 9.906

  === Progress Analysis ===
  Status: NORMAL

--- Round 35 Results ---
  Mean Oracle Reward: 10.015
  Min Oracle Reward: 6.431
  Max Oracle Reward: 11.863
  Std Oracle Reward: 1.127
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.094, Max: 0.195, Count: 13
  Total Sequences Evaluated: 1170

======================================================================
EXPERIMENT ROUND 36/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1170
  Performance plateaued, reducing LR to 0.000136

--- Round 36 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CATGGGTGACCA
  CGGTTGGCACAC
  CTGCGGAACTCG
  ACGCATCTGGGC
  GCCCTAGACTGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.205
  Max reward: 13.108
  With intrinsic bonuses: 10.252

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9682, entropy=0.6519, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3188

=== Surrogate Model Training ===
Total samples: 1202

Training on 1152 samples (removed 50 outliers)
Reward range: [6.97, 12.84], mean: 9.98
  Created 13 candidate models for data size 1152
Current R2 threshold: -0.03999999999999998
  rf-tuned-l: R2 = 0.129 (std: 0.057)
  rf-tuned-xl: R2 = 0.121 (std: 0.069)
  gb-tuned-l: R2 = 0.163 (std: 0.034)
  gb-tuned-xl: R2 = 0.163 (std: 0.034)
  xgb-xl: R2 = -0.027 (std: 0.131)
  xgb-l: R2 = -0.027 (std: 0.131)
  mlp-adaptive-xl: R2 = 0.020 (std: 0.058)
  mlp-l: R2 = 0.028 (std: 0.101)
  svr-rbf-xl: R2 = 0.183 (std: 0.061)
  svr-poly-l: R2 = 0.183 (std: 0.061)
  knn-tuned-sqrt: R2 = 0.047 (std: 0.079)
  knn-tuned-l: R2 = 0.047 (std: 0.079)
  ridge: R2 = -0.005 (std: 0.036)

Model-based training with 13 models
Best R2: 0.183, Mean R2: 0.079
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.072 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9674, entropy=0.6453, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2591
  Round 1/3: Mean predicted reward = 9.828
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.072 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9704, entropy=0.6568, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0791
  Round 2/3: Mean predicted reward = 9.902
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.072 mlp-l:0.073 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.074 knn-tuned-l:0.074 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9717, entropy=0.6228, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2753
  Round 3/3: Mean predicted reward = 9.962

  === Progress Analysis ===
  Status: NORMAL

--- Round 36 Results ---
  Mean Oracle Reward: 10.288
  Min Oracle Reward: 7.163
  Max Oracle Reward: 13.175
  Std Oracle Reward: 1.246
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.079, Max: 0.183, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 1202

======================================================================
EXPERIMENT ROUND 37/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1202
  Performance plateaued, reducing LR to 0.000100

--- Round 37 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CAGTAGGGCCTC
  GCGTGTCTAACA
  TCTGAGAACCGG
  TGTCGAGGAACC
  TCCTAGGAGCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.160
  Max reward: 12.402
  With intrinsic bonuses: 10.206

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.6502, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2864

=== Surrogate Model Training ===
Total samples: 1234

Training on 1184 samples (removed 50 outliers)
Reward range: [6.97, 12.84], mean: 9.99
  Created 13 candidate models for data size 1184
Current R2 threshold: -0.02999999999999997
  rf-tuned-l: R2 = 0.137 (std: 0.049)
  rf-tuned-xl: R2 = 0.131 (std: 0.044)
  gb-tuned-l: R2 = 0.165 (std: 0.037)
  gb-tuned-xl: R2 = 0.165 (std: 0.037)
  xgb-xl: R2 = -0.018 (std: 0.100)
  xgb-l: R2 = -0.018 (std: 0.100)
  mlp-adaptive-xl: R2 = 0.071 (std: 0.074)
  mlp-l: R2 = 0.076 (std: 0.036)
  svr-rbf-xl: R2 = 0.185 (std: 0.052)
  svr-poly-l: R2 = 0.185 (std: 0.052)
  knn-tuned-sqrt: R2 = 0.037 (std: 0.080)
  knn-tuned-l: R2 = 0.037 (std: 0.080)
  ridge: R2 = -0.003 (std: 0.033)

Model-based training with 13 models
Best R2: 0.185, Mean R2: 0.089
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.075 mlp-l:0.076 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.070 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9706, entropy=0.6201, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1250
  Round 1/3: Mean predicted reward = 9.748
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.075 mlp-l:0.076 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.070 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9707, entropy=0.6130, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2213
  Round 2/3: Mean predicted reward = 9.771
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.080 gb-tuned-l:0.083 gb-tuned-xl:0.083 xgb-xl:0.069 xgb-l:0.069 mlp-adaptive-xl:0.075 mlp-l:0.076 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.070 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.6348, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2608
  Round 3/3: Mean predicted reward = 10.052

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 37 Results ---
  Mean Oracle Reward: 10.130
  Min Oracle Reward: 7.903
  Max Oracle Reward: 12.665
  Std Oracle Reward: 1.072
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.089, Max: 0.185, Count: 13
  Total Sequences Evaluated: 1234

======================================================================
EXPERIMENT ROUND 38/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1234
  Performance plateaued, reducing LR to 0.000055

--- Round 38 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTGACCGTGGCA
  CACTTAGGCCGG
  CTGACGGGACTC
  AGTGACGGCCCT
  CTCGAGCTGCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.355
  Max reward: 12.916
  With intrinsic bonuses: 10.401

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9703, entropy=0.6255, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1750

=== Surrogate Model Training ===
Total samples: 1266

Training on 1216 samples (removed 50 outliers)
Reward range: [6.97, 12.86], mean: 10.00
  Created 13 candidate models for data size 1216
Current R2 threshold: -0.019999999999999962
  rf-tuned-l: R2 = 0.129 (std: 0.049)
  rf-tuned-xl: R2 = 0.128 (std: 0.053)
  gb-tuned-l: R2 = 0.143 (std: 0.052)
  gb-tuned-xl: R2 = 0.143 (std: 0.052)
  xgb-xl: R2 = -0.009 (std: 0.106)
  xgb-l: R2 = -0.009 (std: 0.106)
  mlp-adaptive-xl: R2 = 0.028 (std: 0.056)
  mlp-l: R2 = 0.040 (std: 0.078)
  svr-rbf-xl: R2 = 0.178 (std: 0.052)
  svr-poly-l: R2 = 0.178 (std: 0.052)
  knn-tuned-sqrt: R2 = 0.024 (std: 0.081)
  knn-tuned-l: R2 = 0.024 (std: 0.081)
  ridge: R2 = -0.004 (std: 0.035)

Model-based training with 13 models
Best R2: 0.178, Mean R2: 0.076
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.073 mlp-l:0.074 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.6202, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1919
  Round 1/3: Mean predicted reward = 9.754
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.073 mlp-l:0.074 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.6292, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0993
  Round 2/3: Mean predicted reward = 9.993
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.081 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.073 mlp-l:0.074 svr-rbf-xl:0.085 svr-poly-l:0.085 knn-tuned-sqrt:0.073 knn-tuned-l:0.073 ridge:0.071 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9702, entropy=0.6108, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1498
  Round 3/3: Mean predicted reward = 9.914

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 38 Results ---
  Mean Oracle Reward: 10.330
  Min Oracle Reward: 8.137
  Max Oracle Reward: 12.773
  Std Oracle Reward: 1.127
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.076, Max: 0.178, Count: 13
  New best mean reward!
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
  AAGGTCCGGTAC
  ATCGTCCGGACG
  GATGCGCTCGAC
  GTGCCGGCATAA
  GTACGCCTCGAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.115
  Max reward: 12.393
  With intrinsic bonuses: 10.114

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.6253, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0710

=== Surrogate Model Training ===
Total samples: 1298

Training on 1248 samples (removed 50 outliers)
Reward range: [6.97, 12.86], mean: 10.00
  Created 13 candidate models for data size 1248
Current R2 threshold: -0.010000000000000009
  rf-tuned-l: R2 = 0.149 (std: 0.045)
  rf-tuned-xl: R2 = 0.155 (std: 0.044)
  gb-tuned-l: R2 = 0.158 (std: 0.040)
  gb-tuned-xl: R2 = 0.158 (std: 0.040)
  xgb-xl: R2 = -0.003 (std: 0.114)
  xgb-l: R2 = -0.003 (std: 0.114)
  mlp-adaptive-xl: R2 = 0.048 (std: 0.078)
  mlp-l: R2 = 0.061 (std: 0.075)
  svr-rbf-xl: R2 = 0.186 (std: 0.058)
  svr-poly-l: R2 = 0.186 (std: 0.058)
  knn-tuned-sqrt: R2 = 0.032 (std: 0.083)
  knn-tuned-l: R2 = 0.032 (std: 0.083)
  ridge: R2 = -0.002 (std: 0.034)

Model-based training with 13 models
Best R2: 0.186, Mean R2: 0.089
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.082 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.074 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.070 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.6327, kl_div=0.0000
    Epoch 1: policy_loss=0.0021, value_loss=0.9680, entropy=0.6325, kl_div=0.0302
  Round 1/3: Mean predicted reward = 9.795
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.082 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.074 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.070 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9681, entropy=0.6032, kl_div=0.0000
    Epoch 1: policy_loss=-0.0165, value_loss=0.9681, entropy=0.6033, kl_div=0.0252
  Round 2/3: Mean predicted reward = 9.923
    Using performance-based weights
    Model weights: rf-tuned-l:0.081 rf-tuned-xl:0.082 gb-tuned-l:0.082 gb-tuned-xl:0.082 xgb-xl:0.070 xgb-l:0.070 mlp-adaptive-xl:0.074 mlp-l:0.075 svr-rbf-xl:0.084 svr-poly-l:0.084 knn-tuned-sqrt:0.072 knn-tuned-l:0.072 ridge:0.070 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9700, entropy=0.6307, kl_div=0.0000
    Epoch 1: policy_loss=-0.0150, value_loss=0.9700, entropy=0.6305, kl_div=0.0439
  Round 3/3: Mean predicted reward = 10.130

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 39 Results ---
  Mean Oracle Reward: 10.155
  Min Oracle Reward: 7.205
  Max Oracle Reward: 13.203
  Std Oracle Reward: 1.296
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.089, Max: 0.186, Count: 13
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
  CTGGACGAGTAC
  GCTCCAGCGAGT
  GGTGAACGTACC
  CTGAACTCTGGA
  GCCGCAAGGTCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.248
  Max reward: 13.298
  With intrinsic bonuses: 10.237

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.6210, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7410

=== Surrogate Model Training ===
Total samples: 1330

Training on 1277 samples (removed 53 outliers)
Reward range: [7.04, 12.86], mean: 10.01
  Created 13 candidate models for data size 1277
Current R2 threshold: 0.0
  rf-tuned-l: R2 = 0.130 (std: 0.037)
  rf-tuned-xl: R2 = 0.131 (std: 0.044)
  gb-tuned-l: R2 = 0.155 (std: 0.050)
  gb-tuned-xl: R2 = 0.155 (std: 0.050)
  xgb-xl: R2 = -0.008 (std: 0.093)
  xgb-l: R2 = -0.008 (std: 0.093)
  mlp-adaptive-xl: R2 = 0.053 (std: 0.100)
  mlp-l: R2 = 0.040 (std: 0.092)
  svr-rbf-xl: R2 = 0.189 (std: 0.053)
  svr-poly-l: R2 = 0.189 (std: 0.053)
  knn-tuned-sqrt: R2 = 0.028 (std: 0.081)
  knn-tuned-l: R2 = 0.028 (std: 0.081)
  ridge: R2 = -0.009 (std: 0.030)

Model-based training with 10 models
Best R2: 0.189, Mean R2: 0.082
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.102 rf-tuned-xl:0.102 gb-tuned-l:0.104 gb-tuned-xl:0.104 mlp-adaptive-xl:0.094 mlp-l:0.093 svr-rbf-xl:0.108 svr-poly-l:0.108 knn-tuned-sqrt:0.092 knn-tuned-l:0.092 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.6145, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3239
  Round 1/3: Mean predicted reward = 9.991
    Using performance-based weights
    Model weights: rf-tuned-l:0.102 rf-tuned-xl:0.102 gb-tuned-l:0.104 gb-tuned-xl:0.104 mlp-adaptive-xl:0.094 mlp-l:0.093 svr-rbf-xl:0.108 svr-poly-l:0.108 knn-tuned-sqrt:0.092 knn-tuned-l:0.092 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.5928, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3513
  Round 2/3: Mean predicted reward = 9.861
    Using performance-based weights
    Model weights: rf-tuned-l:0.102 rf-tuned-xl:0.102 gb-tuned-l:0.104 gb-tuned-xl:0.104 mlp-adaptive-xl:0.094 mlp-l:0.093 svr-rbf-xl:0.108 svr-poly-l:0.108 knn-tuned-sqrt:0.092 knn-tuned-l:0.092 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.6310, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3363
  Round 3/3: Mean predicted reward = 10.135

  === Progress Analysis ===
  Status: NORMAL

--- Round 40 Results ---
  Mean Oracle Reward: 10.227
  Min Oracle Reward: 6.146
  Max Oracle Reward: 13.250
  Std Oracle Reward: 1.535
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.082, Max: 0.189, Count: 13
  Total Sequences Evaluated: 1330

======================================================================
EXPERIMENT ROUND 41/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1330
  Performance plateaued, reducing LR to 0.000136

--- Round 41 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCCGGTACGCTA
  GCGTGACAGTCC
  TGCGACAGGCTC
  GGATCCGGCACT
  TGTCACCGGACG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.375
  Max reward: 13.749
  With intrinsic bonuses: 10.301

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9665, entropy=0.6144, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2685

=== Surrogate Model Training ===
Total samples: 1362

Training on 1309 samples (removed 53 outliers)
Reward range: [6.97, 12.86], mean: 10.02
  Created 13 candidate models for data size 1309
Current R2 threshold: 0.010000000000000009
  rf-tuned-l: R2 = 0.162 (std: 0.056)
  rf-tuned-xl: R2 = 0.169 (std: 0.048)
  gb-tuned-l: R2 = 0.169 (std: 0.036)
  gb-tuned-xl: R2 = 0.169 (std: 0.036)
  xgb-xl: R2 = 0.048 (std: 0.128)
  xgb-l: R2 = 0.048 (std: 0.128)
  mlp-adaptive-xl: R2 = 0.135 (std: 0.033)
  mlp-l: R2 = 0.089 (std: 0.051)
  svr-rbf-xl: R2 = 0.210 (std: 0.047)
  svr-poly-l: R2 = 0.210 (std: 0.047)
  knn-tuned-sqrt: R2 = 0.051 (std: 0.084)
  knn-tuned-l: R2 = 0.051 (std: 0.084)
  ridge: R2 = -0.006 (std: 0.028)

Model-based training with 12 models
Best R2: 0.210, Mean R2: 0.116
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.087 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.084 mlp-l:0.080 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9708, entropy=0.6167, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0686
  Round 1/3: Mean predicted reward = 9.852
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.087 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.084 mlp-l:0.080 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.6076, kl_div=0.0000
    Epoch 1: policy_loss=-0.0796, value_loss=0.9680, entropy=0.6091, kl_div=-0.0254
  Round 2/3: Mean predicted reward = 10.116
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.087 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.084 mlp-l:0.080 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9685, entropy=0.6214, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0783
  Round 3/3: Mean predicted reward = 10.093

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 41 Results ---
  Mean Oracle Reward: 10.358
  Min Oracle Reward: 8.168
  Max Oracle Reward: 13.985
  Std Oracle Reward: 1.249
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.116, Max: 0.210, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 1362

======================================================================
EXPERIMENT ROUND 42/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1362
  Consistent improvement, increasing LR to 0.000240

--- Round 42 Configuration ---
Learning rate: 0.000240
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGGACGACTGCC
  GGCTCCTGAGAC
  GGTCACTACGGC
  GGTAGTAACCCG
  GAACGGGTCTCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.322
  Max reward: 13.193
  With intrinsic bonuses: 10.317

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.5982, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5095

=== Surrogate Model Training ===
Total samples: 1394

Training on 1338 samples (removed 56 outliers)
Reward range: [7.04, 12.86], mean: 10.02
  Created 13 candidate models for data size 1338
Current R2 threshold: 0.020000000000000018
  rf-tuned-l: R2 = 0.173 (std: 0.048)
  rf-tuned-xl: R2 = 0.164 (std: 0.040)
  gb-tuned-l: R2 = 0.162 (std: 0.031)
  gb-tuned-xl: R2 = 0.162 (std: 0.031)
  xgb-xl: R2 = 0.045 (std: 0.109)
  xgb-l: R2 = 0.045 (std: 0.109)
  mlp-adaptive-xl: R2 = 0.082 (std: 0.081)
  mlp-l: R2 = 0.085 (std: 0.065)
  svr-rbf-xl: R2 = 0.211 (std: 0.035)
  svr-poly-l: R2 = 0.211 (std: 0.035)
  knn-tuned-sqrt: R2 = 0.038 (std: 0.080)
  knn-tuned-l: R2 = 0.038 (std: 0.080)
  ridge: R2 = -0.002 (std: 0.022)

Model-based training with 12 models
Best R2: 0.211, Mean R2: 0.109
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.088 rf-tuned-xl:0.087 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.080 mlp-l:0.080 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9666, entropy=0.5954, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7564
  Round 1/3: Mean predicted reward = 9.924
    Using performance-based weights
    Model weights: rf-tuned-l:0.088 rf-tuned-xl:0.087 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.080 mlp-l:0.080 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.5877, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8789
  Round 2/3: Mean predicted reward = 9.964
    Using performance-based weights
    Model weights: rf-tuned-l:0.088 rf-tuned-xl:0.087 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.080 mlp-l:0.080 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9708, entropy=0.5744, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4728
  Round 3/3: Mean predicted reward = 9.997

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 42 Results ---
  Mean Oracle Reward: 10.316
  Min Oracle Reward: 7.019
  Max Oracle Reward: 13.091
  Std Oracle Reward: 1.364
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.109, Max: 0.211, Count: 13
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
  CCCGGAGCATTG
  AATGCGTCCGCG
  AGGCGTGACTCC
  CGTCTCCGGGAA
  ACCGCGGATCGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.312
  Max reward: 12.885
  With intrinsic bonuses: 10.373

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9673, entropy=0.5901, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2163

=== Surrogate Model Training ===
Total samples: 1426

Training on 1370 samples (removed 56 outliers)
Reward range: [7.04, 13.03], mean: 10.04
  Created 13 candidate models for data size 1370
Current R2 threshold: 0.030000000000000027
  rf-tuned-l: R2 = 0.182 (std: 0.045)
  rf-tuned-xl: R2 = 0.174 (std: 0.035)
  gb-tuned-l: R2 = 0.163 (std: 0.032)
  gb-tuned-xl: R2 = 0.163 (std: 0.032)
  xgb-xl: R2 = 0.039 (std: 0.087)
  xgb-l: R2 = 0.039 (std: 0.087)
  mlp-adaptive-xl: R2 = 0.052 (std: 0.078)
  mlp-l: R2 = 0.085 (std: 0.058)
  svr-rbf-xl: R2 = 0.219 (std: 0.031)
  svr-poly-l: R2 = 0.219 (std: 0.031)
  knn-tuned-sqrt: R2 = 0.055 (std: 0.064)
  knn-tuned-l: R2 = 0.055 (std: 0.064)
  ridge: R2 = -0.005 (std: 0.023)

Model-based training with 12 models
Best R2: 0.219, Mean R2: 0.111
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.088 rf-tuned-xl:0.088 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.078 mlp-l:0.080 svr-rbf-xl:0.092 svr-poly-l:0.092 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9679, entropy=0.5725, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1418
  Round 1/3: Mean predicted reward = 10.054
    Using performance-based weights
    Model weights: rf-tuned-l:0.088 rf-tuned-xl:0.088 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.078 mlp-l:0.080 svr-rbf-xl:0.092 svr-poly-l:0.092 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.5739, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0802
  Round 2/3: Mean predicted reward = 10.009
    Using performance-based weights
    Model weights: rf-tuned-l:0.088 rf-tuned-xl:0.088 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.078 mlp-l:0.080 svr-rbf-xl:0.092 svr-poly-l:0.092 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.5537, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1226
  Round 3/3: Mean predicted reward = 9.999

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 43 Results ---
  Mean Oracle Reward: 10.346
  Min Oracle Reward: 6.586
  Max Oracle Reward: 12.922
  Std Oracle Reward: 1.352
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.111, Max: 0.219, Count: 13
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
  TGGATACCCGCG
  CAATCGTGGAGC
  AACCTGCGCGGT
  GCATAGCTCGGC
  TCGGGCCAATCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.284
  Max reward: 12.542
  With intrinsic bonuses: 10.256

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9671, entropy=0.5770, kl_div=0.0000
    Epoch 1: policy_loss=-0.0149, value_loss=0.9671, entropy=0.5762, kl_div=0.0493

=== Surrogate Model Training ===
Total samples: 1458

Training on 1398 samples (removed 60 outliers)
Reward range: [7.07, 12.95], mean: 10.05
  Created 13 candidate models for data size 1398
Current R2 threshold: 0.040000000000000036
  rf-tuned-l: R2 = 0.169 (std: 0.056)
  rf-tuned-xl: R2 = 0.178 (std: 0.047)
  gb-tuned-l: R2 = 0.168 (std: 0.039)
  gb-tuned-xl: R2 = 0.168 (std: 0.039)
  xgb-xl: R2 = 0.046 (std: 0.097)
  xgb-l: R2 = 0.046 (std: 0.097)
  mlp-adaptive-xl: R2 = 0.112 (std: 0.028)
  mlp-l: R2 = 0.091 (std: 0.073)
  svr-rbf-xl: R2 = 0.220 (std: 0.038)
  svr-poly-l: R2 = 0.220 (std: 0.038)
  knn-tuned-sqrt: R2 = 0.062 (std: 0.062)
  knn-tuned-l: R2 = 0.062 (std: 0.062)
  ridge: R2 = -0.010 (std: 0.029)

Model-based training with 12 models
Best R2: 0.220, Mean R2: 0.118
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.087 rf-tuned-xl:0.087 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.082 mlp-l:0.080 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.5462, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0696
  Round 1/3: Mean predicted reward = 10.057
    Using performance-based weights
    Model weights: rf-tuned-l:0.087 rf-tuned-xl:0.087 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.082 mlp-l:0.080 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9708, entropy=0.5799, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0514
  Round 2/3: Mean predicted reward = 10.022
    Using performance-based weights
    Model weights: rf-tuned-l:0.087 rf-tuned-xl:0.087 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.082 mlp-l:0.080 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9673, entropy=0.5611, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0532
  Round 3/3: Mean predicted reward = 10.149

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 44 Results ---
  Mean Oracle Reward: 10.303
  Min Oracle Reward: 4.270
  Max Oracle Reward: 12.820
  Std Oracle Reward: 1.766
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.118, Max: 0.220, Count: 13
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
  GCCTCGAGTGCA
  TCAGGCATCGCG
  GGACGTCTAGAC
  GCACGGATTGCC
  CGGGTGAACTCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.064
  Max reward: 12.757
  With intrinsic bonuses: 10.060

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9671, entropy=0.5763, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5510

=== Surrogate Model Training ===
Total samples: 1490

Training on 1431 samples (removed 59 outliers)
Reward range: [7.04, 12.95], mean: 10.05
  Created 13 candidate models for data size 1431
Current R2 threshold: 0.050000000000000044
  rf-tuned-l: R2 = 0.170 (std: 0.058)
  rf-tuned-xl: R2 = 0.170 (std: 0.051)
  gb-tuned-l: R2 = 0.168 (std: 0.043)
  gb-tuned-xl: R2 = 0.168 (std: 0.043)
  xgb-xl: R2 = 0.054 (std: 0.096)
  xgb-l: R2 = 0.054 (std: 0.096)
  mlp-adaptive-xl: R2 = 0.089 (std: 0.078)
  mlp-l: R2 = 0.078 (std: 0.086)
  svr-rbf-xl: R2 = 0.225 (std: 0.036)
  svr-poly-l: R2 = 0.225 (std: 0.036)
  knn-tuned-sqrt: R2 = 0.056 (std: 0.051)
  knn-tuned-l: R2 = 0.056 (std: 0.051)
  ridge: R2 = -0.011 (std: 0.026)

Model-based training with 12 models
Best R2: 0.225, Mean R2: 0.116
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.087 rf-tuned-xl:0.087 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.080 mlp-l:0.079 svr-rbf-xl:0.092 svr-poly-l:0.092 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9668, entropy=0.5699, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3685
  Round 1/3: Mean predicted reward = 9.739
    Using performance-based weights
    Model weights: rf-tuned-l:0.087 rf-tuned-xl:0.087 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.080 mlp-l:0.079 svr-rbf-xl:0.092 svr-poly-l:0.092 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9667, entropy=0.5693, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4416
  Round 2/3: Mean predicted reward = 10.029
    Using performance-based weights
    Model weights: rf-tuned-l:0.087 rf-tuned-xl:0.087 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.077 xgb-l:0.077 mlp-adaptive-xl:0.080 mlp-l:0.079 svr-rbf-xl:0.092 svr-poly-l:0.092 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9675, entropy=0.5323, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3941
  Round 3/3: Mean predicted reward = 10.137

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 45 Results ---
  Mean Oracle Reward: 10.047
  Min Oracle Reward: 6.959
  Max Oracle Reward: 12.688
  Std Oracle Reward: 1.249
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.116, Max: 0.225, Count: 13
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
  CAGTGGCCCGAT
  GTGTAGCACCCG
  CGTCGGTAACCG
  TGGTCCAGCAGC
  CGCGACCAGTGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.957
  Max reward: 11.793
  With intrinsic bonuses: 9.948

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9666, entropy=0.5395, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9579

=== Surrogate Model Training ===
Total samples: 1522

Training on 1463 samples (removed 59 outliers)
Reward range: [7.04, 12.95], mean: 10.05
  Created 13 candidate models for data size 1463
Current R2 threshold: 0.06
  rf-tuned-l: R2 = 0.180 (std: 0.044)
  rf-tuned-xl: R2 = 0.168 (std: 0.040)
  gb-tuned-l: R2 = 0.194 (std: 0.046)
  gb-tuned-xl: R2 = 0.194 (std: 0.046)
  xgb-xl: R2 = 0.061 (std: 0.099)
  xgb-l: R2 = 0.061 (std: 0.099)
  mlp-adaptive-xl: R2 = 0.123 (std: 0.080)
  mlp-l: R2 = 0.138 (std: 0.074)
  svr-rbf-xl: R2 = 0.241 (std: 0.044)
  svr-poly-l: R2 = 0.241 (std: 0.044)
  knn-tuned-sqrt: R2 = 0.078 (std: 0.060)
  knn-tuned-l: R2 = 0.078 (std: 0.060)
  ridge: R2 = -0.001 (std: 0.025)

Model-based training with 12 models
Best R2: 0.241, Mean R2: 0.135
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.085 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.076 xgb-l:0.076 mlp-adaptive-xl:0.081 mlp-l:0.082 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9677, entropy=0.5144, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5871
  Round 1/3: Mean predicted reward = 9.881
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.085 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.076 xgb-l:0.076 mlp-adaptive-xl:0.081 mlp-l:0.082 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9700, entropy=0.4969, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4691
  Round 2/3: Mean predicted reward = 9.980
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.085 gb-tuned-l:0.087 gb-tuned-xl:0.087 xgb-xl:0.076 xgb-l:0.076 mlp-adaptive-xl:0.081 mlp-l:0.082 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9702, entropy=0.4798, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6598
  Round 3/3: Mean predicted reward = 10.188

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 46 Results ---
  Mean Oracle Reward: 9.972
  Min Oracle Reward: 7.676
  Max Oracle Reward: 11.929
  Std Oracle Reward: 1.165
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.135, Max: 0.241, Count: 13
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
  CGAACCTCGGTG
  CAGGTCGAGTCC
  CCGATGCGGTAC
  GTATGGCCCGCA
  GCCCGGCTATGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.150
  Max reward: 12.629
  With intrinsic bonuses: 10.143

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.4670, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6963

=== Surrogate Model Training ===
Total samples: 1554

Training on 1491 samples (removed 63 outliers)
Reward range: [7.07, 12.95], mean: 10.06
  Created 13 candidate models for data size 1491
Current R2 threshold: 0.07
  rf-tuned-l: R2 = 0.180 (std: 0.053)
  rf-tuned-xl: R2 = 0.185 (std: 0.053)
  gb-tuned-l: R2 = 0.182 (std: 0.050)
  gb-tuned-xl: R2 = 0.182 (std: 0.050)
  xgb-xl: R2 = 0.119 (std: 0.090)
  xgb-l: R2 = 0.119 (std: 0.090)
  mlp-adaptive-xl: R2 = 0.097 (std: 0.070)
  mlp-l: R2 = 0.099 (std: 0.086)
  svr-rbf-xl: R2 = 0.235 (std: 0.047)
  svr-poly-l: R2 = 0.235 (std: 0.047)
  knn-tuned-sqrt: R2 = 0.076 (std: 0.070)
  knn-tuned-l: R2 = 0.076 (std: 0.070)
  ridge: R2 = -0.002 (std: 0.021)

Model-based training with 12 models
Best R2: 0.235, Mean R2: 0.137
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.081 xgb-l:0.081 mlp-adaptive-xl:0.079 mlp-l:0.079 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.4704, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3976
  Round 1/3: Mean predicted reward = 10.045
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.081 xgb-l:0.081 mlp-adaptive-xl:0.079 mlp-l:0.079 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9674, entropy=0.4389, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0691
  Round 2/3: Mean predicted reward = 9.994
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.086 gb-tuned-xl:0.086 xgb-xl:0.081 xgb-l:0.081 mlp-adaptive-xl:0.079 mlp-l:0.079 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.4484, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2248
  Round 3/3: Mean predicted reward = 10.207

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 47 Results ---
  Mean Oracle Reward: 10.166
  Min Oracle Reward: 5.313
  Max Oracle Reward: 12.762
  Std Oracle Reward: 1.471
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.137, Max: 0.235, Count: 13
  Total Sequences Evaluated: 1554

======================================================================
EXPERIMENT ROUND 48/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1554
  Performance plateaued, reducing LR to 0.000055

--- Round 48 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTCATGGCGCGA
  TAGTTACGACCG
  GTCACATGGCCG
  ACCATCGTGAGG
  CCCGAGGCTGTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.994
  Max reward: 12.404
  With intrinsic bonuses: 9.984

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9669, entropy=0.4170, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0930

=== Surrogate Model Training ===
Total samples: 1586

Training on 1521 samples (removed 65 outliers)
Reward range: [7.07, 12.95], mean: 10.06
  Created 13 candidate models for data size 1521
Current R2 threshold: 0.08000000000000002
  rf-tuned-l: R2 = 0.192 (std: 0.052)
  rf-tuned-xl: R2 = 0.192 (std: 0.054)
  gb-tuned-l: R2 = 0.180 (std: 0.060)
  gb-tuned-xl: R2 = 0.180 (std: 0.060)
  xgb-xl: R2 = 0.118 (std: 0.074)
  xgb-l: R2 = 0.118 (std: 0.074)
  mlp-adaptive-xl: R2 = 0.093 (std: 0.053)
  mlp-l: R2 = 0.130 (std: 0.071)
  svr-rbf-xl: R2 = 0.239 (std: 0.051)
  svr-poly-l: R2 = 0.239 (std: 0.051)
  knn-tuned-sqrt: R2 = 0.089 (std: 0.073)
  knn-tuned-l: R2 = 0.089 (std: 0.073)
  ridge: R2 = 0.008 (std: 0.032)

Model-based training with 12 models
Best R2: 0.239, Mean R2: 0.144
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.080 xgb-l:0.080 mlp-adaptive-xl:0.078 mlp-l:0.081 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.4398, kl_div=0.0000
    Epoch 1: policy_loss=-0.0154, value_loss=0.9692, entropy=0.4398, kl_div=0.0191
  Round 1/3: Mean predicted reward = 9.907
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.080 xgb-l:0.080 mlp-adaptive-xl:0.078 mlp-l:0.081 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.4611, kl_div=0.0000
    Epoch 1: policy_loss=-0.0325, value_loss=0.9684, entropy=0.4640, kl_div=-0.0839
  Round 2/3: Mean predicted reward = 9.832
    Using performance-based weights
    Model weights: rf-tuned-l:0.086 rf-tuned-xl:0.086 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.080 xgb-l:0.080 mlp-adaptive-xl:0.078 mlp-l:0.081 svr-rbf-xl:0.091 svr-poly-l:0.091 knn-tuned-sqrt:0.078 knn-tuned-l:0.078 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9678, entropy=0.4535, kl_div=0.0000
    Epoch 1: policy_loss=-0.0115, value_loss=0.9678, entropy=0.4537, kl_div=-0.0086
  Round 3/3: Mean predicted reward = 10.035

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 48 Results ---
  Mean Oracle Reward: 10.008
  Min Oracle Reward: 6.917
  Max Oracle Reward: 12.611
  Std Oracle Reward: 1.263
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.144, Max: 0.239, Count: 13
  Total Sequences Evaluated: 1586

======================================================================
EXPERIMENT ROUND 49/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1586
  Performance plateaued, reducing LR to 0.000019

--- Round 49 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CAGGCACCTTGG
  CCCAAGGGCTTG
  TTGACGCCGACG
  TCGAGCCTGAGC
  CTAACTGGCGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.943
  Max reward: 12.579
  With intrinsic bonuses: 9.975

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9675, entropy=0.4581, kl_div=0.0000
    Epoch 1: policy_loss=-0.0107, value_loss=0.9675, entropy=0.4582, kl_div=-0.0019

=== Surrogate Model Training ===
Total samples: 1618

Training on 1553 samples (removed 65 outliers)
Reward range: [7.05, 12.95], mean: 10.06
  Created 13 candidate models for data size 1553
Current R2 threshold: 0.09000000000000002
  rf-tuned-l: R2 = 0.190 (std: 0.062)
  rf-tuned-xl: R2 = 0.191 (std: 0.061)
  gb-tuned-l: R2 = 0.194 (std: 0.059)
  gb-tuned-xl: R2 = 0.194 (std: 0.059)
  xgb-xl: R2 = 0.149 (std: 0.094)
  xgb-l: R2 = 0.149 (std: 0.094)
  mlp-adaptive-xl: R2 = 0.163 (std: 0.061)
  mlp-l: R2 = 0.154 (std: 0.090)
  svr-rbf-xl: R2 = 0.244 (std: 0.063)
  svr-poly-l: R2 = 0.244 (std: 0.063)
  knn-tuned-sqrt: R2 = 0.094 (std: 0.090)
  knn-tuned-l: R2 = 0.094 (std: 0.090)
  ridge: R2 = 0.013 (std: 0.033)

Model-based training with 12 models
Best R2: 0.244, Mean R2: 0.160
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.085 rf-tuned-xl:0.085 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.081 xgb-l:0.081 mlp-adaptive-xl:0.083 mlp-l:0.082 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.4496, kl_div=0.0000
    Epoch 1: policy_loss=-0.0135, value_loss=0.9697, entropy=0.4506, kl_div=-0.0350
  Round 1/3: Mean predicted reward = 9.896
    Using performance-based weights
    Model weights: rf-tuned-l:0.085 rf-tuned-xl:0.085 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.081 xgb-l:0.081 mlp-adaptive-xl:0.083 mlp-l:0.082 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.4642, kl_div=0.0000
    Epoch 1: policy_loss=-0.0372, value_loss=0.9692, entropy=0.4661, kl_div=-0.0763
  Round 2/3: Mean predicted reward = 10.049
    Using performance-based weights
    Model weights: rf-tuned-l:0.085 rf-tuned-xl:0.085 gb-tuned-l:0.085 gb-tuned-xl:0.085 xgb-xl:0.081 xgb-l:0.081 mlp-adaptive-xl:0.083 mlp-l:0.082 svr-rbf-xl:0.090 svr-poly-l:0.090 knn-tuned-sqrt:0.077 knn-tuned-l:0.077 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9666, entropy=0.4333, kl_div=0.0000
    Epoch 1: policy_loss=0.0005, value_loss=0.9666, entropy=0.4344, kl_div=-0.0385
  Round 3/3: Mean predicted reward = 10.007

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 49 Results ---
  Mean Oracle Reward: 10.005
  Min Oracle Reward: 6.858
  Max Oracle Reward: 12.303
  Std Oracle Reward: 1.286
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: 0.160, Max: 0.244, Count: 13
  Total Sequences Evaluated: 1618

======================================================================
EXPERIMENT ROUND 50/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1618
  Performance plateaued, reducing LR to 0.000150

--- Round 50 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGTGGCTACCGA
  AGTCGTCACCGG
  GAATGTGGCCCC
  AGTGATCCGCAG
  GGTCTCCACGAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.243
  Max reward: 12.423
  With intrinsic bonuses: 10.211

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9664, entropy=0.4668, kl_div=0.0000
    Epoch 1: policy_loss=-0.0150, value_loss=0.9664, entropy=0.4671, kl_div=-0.0081

=== Surrogate Model Training ===
Total samples: 1650

Training on 1582 samples (removed 68 outliers)
Reward range: [7.09, 12.95], mean: 10.07
  Created 13 candidate models for data size 1582
Current R2 threshold: 0.10000000000000003
  rf-tuned-l: R2 = 0.200 (std: 0.059)
  rf-tuned-xl: R2 = 0.201 (std: 0.055)
  gb-tuned-l: R2 = 0.205 (std: 0.064)
  gb-tuned-xl: R2 = 0.205 (std: 0.064)
  xgb-xl: R2 = 0.123 (std: 0.117)
  xgb-l: R2 = 0.123 (std: 0.117)
  mlp-adaptive-xl: R2 = 0.131 (std: 0.079)
  mlp-l: R2 = 0.161 (std: 0.035)
  svr-rbf-xl: R2 = 0.249 (std: 0.060)
  svr-poly-l: R2 = 0.249 (std: 0.060)
  knn-tuned-sqrt: R2 = 0.097 (std: 0.091)
  knn-tuned-l: R2 = 0.097 (std: 0.091)
  ridge: R2 = 0.013 (std: 0.035)

Model-based training with 10 models
Best R2: 0.249, Mean R2: 0.158
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.102 gb-tuned-l:0.102 gb-tuned-xl:0.102 xgb-xl:0.094 xgb-l:0.094 mlp-adaptive-xl:0.095 mlp-l:0.098 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=0.4453, kl_div=0.0000
    Epoch 1: policy_loss=-0.0571, value_loss=0.9675, entropy=0.4467, kl_div=-0.0604
  Round 1/3: Mean predicted reward = 9.792
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.102 gb-tuned-l:0.102 gb-tuned-xl:0.102 xgb-xl:0.094 xgb-l:0.094 mlp-adaptive-xl:0.095 mlp-l:0.098 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.4245, kl_div=0.0000
    Epoch 1: policy_loss=-0.0328, value_loss=0.9687, entropy=0.4253, kl_div=-0.1095
  Round 2/3: Mean predicted reward = 9.925
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.102 gb-tuned-l:0.102 gb-tuned-xl:0.102 xgb-xl:0.094 xgb-l:0.094 mlp-adaptive-xl:0.095 mlp-l:0.098 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9678, entropy=0.4565, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2750
  Round 3/3: Mean predicted reward = 10.244

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 50 Results ---
  Mean Oracle Reward: 10.186
  Min Oracle Reward: 6.577
  Max Oracle Reward: 12.353
  Std Oracle Reward: 1.233
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.158, Max: 0.249, Count: 13
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
  GCGAGTCCCTAG
  GCTGGAGTCACA
  ACCGGCACTGGT
  TGACGCGGTCCA
  GCGCATGGACCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.194
  Max reward: 13.111
  With intrinsic bonuses: 10.209

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9672, entropy=0.4383, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1241

=== Surrogate Model Training ===
Total samples: 1682

Training on 1611 samples (removed 71 outliers)
Reward range: [7.11, 13.00], mean: 10.08
  Created 13 candidate models for data size 1611
Current R2 threshold: 0.11000000000000004
  rf-tuned-l: R2 = 0.195 (std: 0.065)
  rf-tuned-xl: R2 = 0.189 (std: 0.062)
  gb-tuned-l: R2 = 0.191 (std: 0.068)
  gb-tuned-xl: R2 = 0.191 (std: 0.068)
  xgb-xl: R2 = 0.142 (std: 0.116)
  xgb-l: R2 = 0.142 (std: 0.116)
  mlp-adaptive-xl: R2 = 0.178 (std: 0.055)
  mlp-l: R2 = 0.160 (std: 0.041)
  svr-rbf-xl: R2 = 0.245 (std: 0.054)
  svr-poly-l: R2 = 0.245 (std: 0.054)
  knn-tuned-sqrt: R2 = 0.091 (std: 0.086)
  knn-tuned-l: R2 = 0.091 (std: 0.086)
  ridge: R2 = 0.014 (std: 0.028)

Model-based training with 10 models
Best R2: 0.245, Mean R2: 0.160
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.100 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.099 mlp-l:0.097 svr-rbf-xl:0.106 svr-poly-l:0.106 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9682, entropy=0.4327, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1458
  Round 1/3: Mean predicted reward = 9.999
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.100 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.099 mlp-l:0.097 svr-rbf-xl:0.106 svr-poly-l:0.106 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.4151, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5110
  Round 2/3: Mean predicted reward = 9.991
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.100 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.099 mlp-l:0.097 svr-rbf-xl:0.106 svr-poly-l:0.106 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.4084, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2528
  Round 3/3: Mean predicted reward = 10.123

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 51 Results ---
  Mean Oracle Reward: 10.168
  Min Oracle Reward: 6.038
  Max Oracle Reward: 13.011
  Std Oracle Reward: 1.344
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.160, Max: 0.245, Count: 13
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
  AACTTGCGGATC
  ATTGCCCGAGCG
  CTAGCGTTCAGA
  AGCTTCCAGTAG
  GCTGCGCTAGAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.816
  Max reward: 11.847
  With intrinsic bonuses: 9.850

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.3671, kl_div=0.0000
    Epoch 1: policy_loss=-0.0795, value_loss=0.9683, entropy=0.3683, kl_div=-0.0504

=== Surrogate Model Training ===
Total samples: 1714

Training on 1644 samples (removed 70 outliers)
Reward range: [7.09, 13.00], mean: 10.07
  Created 13 candidate models for data size 1644
Current R2 threshold: 0.12
  rf-tuned-l: R2 = 0.200 (std: 0.043)
  rf-tuned-xl: R2 = 0.204 (std: 0.055)
  gb-tuned-l: R2 = 0.207 (std: 0.059)
  gb-tuned-xl: R2 = 0.207 (std: 0.059)
  xgb-xl: R2 = 0.172 (std: 0.099)
  xgb-l: R2 = 0.172 (std: 0.099)
  mlp-adaptive-xl: R2 = 0.159 (std: 0.097)
  mlp-l: R2 = 0.163 (std: 0.074)
  svr-rbf-xl: R2 = 0.255 (std: 0.056)
  svr-poly-l: R2 = 0.255 (std: 0.056)
  knn-tuned-sqrt: R2 = 0.103 (std: 0.069)
  knn-tuned-l: R2 = 0.103 (std: 0.069)
  ridge: R2 = 0.015 (std: 0.029)

Model-based training with 10 models
Best R2: 0.255, Mean R2: 0.171
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.100 rf-tuned-xl:0.100 gb-tuned-l:0.101 gb-tuned-xl:0.101 xgb-xl:0.097 xgb-l:0.097 mlp-adaptive-xl:0.096 mlp-l:0.096 svr-rbf-xl:0.106 svr-poly-l:0.106 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.3853, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2203
  Round 1/3: Mean predicted reward = 9.909
    Using performance-based weights
    Model weights: rf-tuned-l:0.100 rf-tuned-xl:0.100 gb-tuned-l:0.101 gb-tuned-xl:0.101 xgb-xl:0.097 xgb-l:0.097 mlp-adaptive-xl:0.096 mlp-l:0.096 svr-rbf-xl:0.106 svr-poly-l:0.106 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.4441, kl_div=0.0000
    Epoch 1: policy_loss=-0.0788, value_loss=0.9694, entropy=0.4453, kl_div=0.0208
  Round 2/3: Mean predicted reward = 10.082
    Using performance-based weights
    Model weights: rf-tuned-l:0.100 rf-tuned-xl:0.100 gb-tuned-l:0.101 gb-tuned-xl:0.101 xgb-xl:0.097 xgb-l:0.097 mlp-adaptive-xl:0.096 mlp-l:0.096 svr-rbf-xl:0.106 svr-poly-l:0.106 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9677, entropy=0.4320, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1084
  Round 3/3: Mean predicted reward = 10.220

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 52 Results ---
  Mean Oracle Reward: 9.736
  Min Oracle Reward: 6.752
  Max Oracle Reward: 11.567
  Std Oracle Reward: 1.135
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.171, Max: 0.255, Count: 13
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
  GCGCTTACAGGA
  TCGGCTCAAGGC
  GGCCATTGGCAC
  GCCTGTACCGGA
  CCTCGTGAGGCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.178
  Max reward: 11.803
  With intrinsic bonuses: 10.184

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9641, entropy=0.3803, kl_div=0.0000
    Epoch 1: policy_loss=-0.0433, value_loss=0.9641, entropy=0.3795, kl_div=0.0069

=== Surrogate Model Training ===
Total samples: 1746

Training on 1673 samples (removed 73 outliers)
Reward range: [7.11, 13.00], mean: 10.08
  Created 13 candidate models for data size 1673
Current R2 threshold: 0.13
  rf-tuned-l: R2 = 0.203 (std: 0.044)
  rf-tuned-xl: R2 = 0.214 (std: 0.040)
  gb-tuned-l: R2 = 0.205 (std: 0.049)
  gb-tuned-xl: R2 = 0.205 (std: 0.049)
  xgb-xl: R2 = 0.146 (std: 0.108)
  xgb-l: R2 = 0.146 (std: 0.108)
  mlp-adaptive-xl: R2 = 0.179 (std: 0.085)
  mlp-l: R2 = 0.147 (std: 0.075)
  svr-rbf-xl: R2 = 0.254 (std: 0.056)
  svr-poly-l: R2 = 0.254 (std: 0.056)
  knn-tuned-sqrt: R2 = 0.104 (std: 0.078)
  knn-tuned-l: R2 = 0.104 (std: 0.078)
  ridge: R2 = 0.017 (std: 0.033)

Model-based training with 10 models
Best R2: 0.254, Mean R2: 0.168
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.102 gb-tuned-l:0.101 gb-tuned-xl:0.101 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.098 mlp-l:0.095 svr-rbf-xl:0.106 svr-poly-l:0.106 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.4254, kl_div=0.0000
    Epoch 1: policy_loss=-0.0051, value_loss=0.9701, entropy=0.4254, kl_div=0.0472
  Round 1/3: Mean predicted reward = 10.205
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.102 gb-tuned-l:0.101 gb-tuned-xl:0.101 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.098 mlp-l:0.095 svr-rbf-xl:0.106 svr-poly-l:0.106 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.3844, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3010
  Round 2/3: Mean predicted reward = 10.031
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.102 gb-tuned-l:0.101 gb-tuned-xl:0.101 xgb-xl:0.095 xgb-l:0.095 mlp-adaptive-xl:0.098 mlp-l:0.095 svr-rbf-xl:0.106 svr-poly-l:0.106 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9664, entropy=0.4134, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4072
  Round 3/3: Mean predicted reward = 10.353

  === Progress Analysis ===
  Status: NORMAL

--- Round 53 Results ---
  Mean Oracle Reward: 10.162
  Min Oracle Reward: 4.865
  Max Oracle Reward: 12.027
  Std Oracle Reward: 1.280
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.168, Max: 0.254, Count: 13
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
  CATGCACGGGTC
  ATCGACGGCGTC
  GTAACGCTGCCG
  ACAGCGCGGTTC
  ACCGCGCTTAGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.398
  Max reward: 12.478
  With intrinsic bonuses: 10.385

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.3897, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0710

=== Surrogate Model Training ===
Total samples: 1778

Training on 1702 samples (removed 76 outliers)
Reward range: [7.13, 12.96], mean: 10.08
  Created 13 candidate models for data size 1702
Current R2 threshold: 0.14
  rf-tuned-l: R2 = 0.202 (std: 0.055)
  rf-tuned-xl: R2 = 0.190 (std: 0.048)
  gb-tuned-l: R2 = 0.195 (std: 0.051)
  gb-tuned-xl: R2 = 0.195 (std: 0.051)
  xgb-xl: R2 = 0.151 (std: 0.049)
  xgb-l: R2 = 0.151 (std: 0.049)
  mlp-adaptive-xl: R2 = 0.153 (std: 0.060)
  mlp-l: R2 = 0.181 (std: 0.069)
  svr-rbf-xl: R2 = 0.252 (std: 0.055)
  svr-poly-l: R2 = 0.252 (std: 0.055)
  knn-tuned-sqrt: R2 = 0.094 (std: 0.070)
  knn-tuned-l: R2 = 0.094 (std: 0.070)
  ridge: R2 = 0.014 (std: 0.032)

Model-based training with 10 models
Best R2: 0.252, Mean R2: 0.163
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.100 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.096 xgb-l:0.096 mlp-adaptive-xl:0.096 mlp-l:0.099 svr-rbf-xl:0.106 svr-poly-l:0.106 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9669, entropy=0.3392, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1279
  Round 1/3: Mean predicted reward = 9.878
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.100 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.096 xgb-l:0.096 mlp-adaptive-xl:0.096 mlp-l:0.099 svr-rbf-xl:0.106 svr-poly-l:0.106 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.3409, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0925
  Round 2/3: Mean predicted reward = 10.145
    Using performance-based weights
    Model weights: rf-tuned-l:0.101 rf-tuned-xl:0.100 gb-tuned-l:0.100 gb-tuned-xl:0.100 xgb-xl:0.096 xgb-l:0.096 mlp-adaptive-xl:0.096 mlp-l:0.099 svr-rbf-xl:0.106 svr-poly-l:0.106 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.3816, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1343
  Round 3/3: Mean predicted reward = 10.219

  === Progress Analysis ===
  Status: NORMAL

--- Round 54 Results ---
  Mean Oracle Reward: 10.383
  Min Oracle Reward: 8.706
  Max Oracle Reward: 12.724
  Std Oracle Reward: 0.874
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.163, Max: 0.252, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  AATCTGGGCAGC
  AGCGTCCGACGT
  GACGGACTTGCC
  CGTAAGCGTCCG
  ATCTGCGAGCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.100
  Max reward: 12.406
  With intrinsic bonuses: 10.046

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.3796, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5475

=== Surrogate Model Training ===
Total samples: 1810

Training on 1730 samples (removed 80 outliers)
Reward range: [7.23, 12.96], mean: 10.09
  Created 13 candidate models for data size 1730
Current R2 threshold: 0.15000000000000002
  rf-tuned-l: R2 = 0.205 (std: 0.056)
  rf-tuned-xl: R2 = 0.200 (std: 0.058)
  gb-tuned-l: R2 = 0.178 (std: 0.049)
  gb-tuned-xl: R2 = 0.178 (std: 0.049)
  xgb-xl: R2 = 0.137 (std: 0.079)
  xgb-l: R2 = 0.137 (std: 0.079)
  mlp-adaptive-xl: R2 = 0.159 (std: 0.065)
  mlp-l: R2 = 0.145 (std: 0.034)
  svr-rbf-xl: R2 = 0.245 (std: 0.046)
  svr-poly-l: R2 = 0.245 (std: 0.046)
  knn-tuned-sqrt: R2 = 0.102 (std: 0.078)
  knn-tuned-l: R2 = 0.102 (std: 0.078)
  ridge: R2 = 0.013 (std: 0.037)

Model-based training with 7 models
Best R2: 0.245, Mean R2: 0.157
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.143 rf-tuned-xl:0.143 gb-tuned-l:0.139 gb-tuned-xl:0.139 mlp-adaptive-xl:0.137 svr-rbf-xl:0.149 svr-poly-l:0.149 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9668, entropy=0.3564, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5310
  Round 1/3: Mean predicted reward = 9.979
    Using performance-based weights
    Model weights: rf-tuned-l:0.143 rf-tuned-xl:0.143 gb-tuned-l:0.139 gb-tuned-xl:0.139 mlp-adaptive-xl:0.137 svr-rbf-xl:0.149 svr-poly-l:0.149 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.3552, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8075
  Round 2/3: Mean predicted reward = 9.928
    Using performance-based weights
    Model weights: rf-tuned-l:0.143 rf-tuned-xl:0.143 gb-tuned-l:0.139 gb-tuned-xl:0.139 mlp-adaptive-xl:0.137 svr-rbf-xl:0.149 svr-poly-l:0.149 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9672, entropy=0.3449, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.2031
  Round 3/3: Mean predicted reward = 10.212

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 55 Results ---
  Mean Oracle Reward: 10.111
  Min Oracle Reward: 6.929
  Max Oracle Reward: 12.147
  Std Oracle Reward: 0.997
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: 0.157, Max: 0.245, Count: 13
  Total Sequences Evaluated: 1810

======================================================================
EXPERIMENT ROUND 56/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1810

--- Round 56 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGGCCAACTGAG
  GCAGTCTACGCG
  CAGATCGTCGCG
  TCGCCGGAATGC
  TACGACTCGCGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.348
  Max reward: 11.913
  With intrinsic bonuses: 10.343

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.3372, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4354

=== Surrogate Model Training ===
Total samples: 1842

Training on 1758 samples (removed 84 outliers)
Reward range: [7.23, 12.90], mean: 10.09
  Created 13 candidate models for data size 1758
Current R2 threshold: 0.16000000000000003
  rf-tuned-l: R2 = 0.190 (std: 0.041)
  rf-tuned-xl: R2 = 0.193 (std: 0.047)
  gb-tuned-l: R2 = 0.178 (std: 0.040)
  gb-tuned-xl: R2 = 0.178 (std: 0.040)
  xgb-xl: R2 = 0.144 (std: 0.080)
  xgb-l: R2 = 0.144 (std: 0.080)
  mlp-adaptive-xl: R2 = 0.124 (std: 0.054)
  mlp-l: R2 = 0.147 (std: 0.057)
  svr-rbf-xl: R2 = 0.234 (std: 0.037)
  svr-poly-l: R2 = 0.234 (std: 0.037)
  knn-tuned-sqrt: R2 = 0.091 (std: 0.066)
  knn-tuned-l: R2 = 0.091 (std: 0.066)
  ridge: R2 = 0.012 (std: 0.036)

Model-based training with 6 models
Best R2: 0.234, Mean R2: 0.151
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.165 rf-tuned-xl:0.165 gb-tuned-l:0.163 gb-tuned-xl:0.163 svr-rbf-xl:0.172 svr-poly-l:0.172 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.3169, kl_div=0.0000
    Epoch 1: policy_loss=-0.0097, value_loss=0.9684, entropy=0.3149, kl_div=0.0394
  Round 1/3: Mean predicted reward = 9.692
    Using performance-based weights
    Model weights: rf-tuned-l:0.165 rf-tuned-xl:0.165 gb-tuned-l:0.163 gb-tuned-xl:0.163 svr-rbf-xl:0.172 svr-poly-l:0.172 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.3404, kl_div=0.0000
    Epoch 1: policy_loss=0.1292, value_loss=0.9692, entropy=0.3471, kl_div=-0.6522
  Round 2/3: Mean predicted reward = 9.994
    Using performance-based weights
    Model weights: rf-tuned-l:0.165 rf-tuned-xl:0.165 gb-tuned-l:0.163 gb-tuned-xl:0.163 svr-rbf-xl:0.172 svr-poly-l:0.172 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9661, entropy=0.3466, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1035
  Round 3/3: Mean predicted reward = 10.035

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 56 Results ---
  Mean Oracle Reward: 10.302
  Min Oracle Reward: 7.024
  Max Oracle Reward: 11.988
  Std Oracle Reward: 1.072
  Sequence Diversity: 1.000
  Models Used: 6
  Model R2 - Mean: 0.151, Max: 0.234, Count: 13
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
  CGGTTAGCACCG
  TACCCGTGACGG
  GATTCCCGACGG
  ACGGCTTCGCGA
  AGTGCCGCTCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.341
  Max reward: 12.977
  With intrinsic bonuses: 10.370

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9665, entropy=0.3402, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2255

=== Surrogate Model Training ===
Total samples: 1874

Training on 1793 samples (removed 81 outliers)
Reward range: [7.23, 12.96], mean: 10.10
  Created 13 candidate models for data size 1793
Current R2 threshold: 0.17000000000000004
  rf-tuned-l: R2 = 0.193 (std: 0.065)
  rf-tuned-xl: R2 = 0.194 (std: 0.060)
  gb-tuned-l: R2 = 0.174 (std: 0.047)
  gb-tuned-xl: R2 = 0.174 (std: 0.047)
  xgb-xl: R2 = 0.152 (std: 0.091)
  xgb-l: R2 = 0.152 (std: 0.091)
  mlp-adaptive-xl: R2 = 0.141 (std: 0.066)
  mlp-l: R2 = 0.116 (std: 0.059)
  svr-rbf-xl: R2 = 0.238 (std: 0.045)
  svr-poly-l: R2 = 0.238 (std: 0.045)
  knn-tuned-sqrt: R2 = 0.088 (std: 0.082)
  knn-tuned-l: R2 = 0.088 (std: 0.082)
  ridge: R2 = 0.005 (std: 0.031)

Model-based training with 6 models
Best R2: 0.238, Mean R2: 0.150
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.165 rf-tuned-xl:0.165 gb-tuned-l:0.162 gb-tuned-xl:0.162 svr-rbf-xl:0.173 svr-poly-l:0.173 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.3389, kl_div=0.0000
    Epoch 1: policy_loss=-0.0262, value_loss=0.9691, entropy=0.3386, kl_div=-0.0139
  Round 1/3: Mean predicted reward = 9.903
    Using performance-based weights
    Model weights: rf-tuned-l:0.165 rf-tuned-xl:0.165 gb-tuned-l:0.162 gb-tuned-xl:0.162 svr-rbf-xl:0.173 svr-poly-l:0.173 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9685, entropy=0.3157, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1867
  Round 2/3: Mean predicted reward = 9.754
    Using performance-based weights
    Model weights: rf-tuned-l:0.165 rf-tuned-xl:0.165 gb-tuned-l:0.162 gb-tuned-xl:0.162 svr-rbf-xl:0.173 svr-poly-l:0.173 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9678, entropy=0.3625, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3373
  Round 3/3: Mean predicted reward = 10.166

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 57 Results ---
  Mean Oracle Reward: 10.340
  Min Oracle Reward: 7.630
  Max Oracle Reward: 12.856
  Std Oracle Reward: 1.179
  Sequence Diversity: 1.000
  Models Used: 6
  Model R2 - Mean: 0.150, Max: 0.238, Count: 13
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
  CTCATCGCGAGG
  CCCGACTGAGGT
  ATCGGTGCGCCA
  CTCAGGTGCCAG
  GGGTGCCCAATC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.110
  Max reward: 12.171
  With intrinsic bonuses: 10.062

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9673, entropy=0.3213, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3140

=== Surrogate Model Training ===
Total samples: 1906

Training on 1825 samples (removed 81 outliers)
Reward range: [7.23, 12.96], mean: 10.10
  Created 13 candidate models for data size 1825
Current R2 threshold: 0.18
  rf-tuned-l: R2 = 0.173 (std: 0.049)
  rf-tuned-xl: R2 = 0.174 (std: 0.049)
  gb-tuned-l: R2 = 0.156 (std: 0.046)
  gb-tuned-xl: R2 = 0.156 (std: 0.046)
  xgb-xl: R2 = 0.121 (std: 0.068)
  xgb-l: R2 = 0.121 (std: 0.068)
  mlp-adaptive-xl: R2 = 0.146 (std: 0.064)
  mlp-l: R2 = 0.116 (std: 0.056)
  svr-rbf-xl: R2 = 0.233 (std: 0.038)
  svr-poly-l: R2 = 0.233 (std: 0.038)
  knn-tuned-sqrt: R2 = 0.087 (std: 0.068)
  knn-tuned-l: R2 = 0.087 (std: 0.068)
  ridge: R2 = 0.003 (std: 0.038)

Model-based training with 2 models
Best R2: 0.233, Mean R2: 0.139
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.3269, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1501
  Round 1/3: Mean predicted reward = 10.088
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9679, entropy=0.3113, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3921
  Round 2/3: Mean predicted reward = 9.967
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9679, entropy=0.3090, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5146
  Round 3/3: Mean predicted reward = 10.113

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 58 Results ---
  Mean Oracle Reward: 10.120
  Min Oracle Reward: 7.412
  Max Oracle Reward: 12.133
  Std Oracle Reward: 1.259
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.139, Max: 0.233, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  CTCCTGGGAGCA
  CAGCACCGGTTG
  TACGCGCGGATA
  GTCGTAGGAACC
  CACGACGTTCGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.418
  Max reward: 12.921
  With intrinsic bonuses: 10.394

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9673, entropy=0.3358, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2180

=== Surrogate Model Training ===
Total samples: 1938

Training on 1858 samples (removed 80 outliers)
Reward range: [7.23, 13.00], mean: 10.11
  Created 13 candidate models for data size 1858
Current R2 threshold: 0.19
  rf-tuned-l: R2 = 0.176 (std: 0.045)
  rf-tuned-xl: R2 = 0.179 (std: 0.054)
  gb-tuned-l: R2 = 0.154 (std: 0.046)
  gb-tuned-xl: R2 = 0.154 (std: 0.046)
  xgb-xl: R2 = 0.124 (std: 0.095)
  xgb-l: R2 = 0.124 (std: 0.095)
  mlp-adaptive-xl: R2 = 0.145 (std: 0.084)
  mlp-l: R2 = 0.137 (std: 0.066)
  svr-rbf-xl: R2 = 0.234 (std: 0.041)
  svr-poly-l: R2 = 0.234 (std: 0.041)
  knn-tuned-sqrt: R2 = 0.083 (std: 0.066)
  knn-tuned-l: R2 = 0.083 (std: 0.066)
  ridge: R2 = -0.004 (std: 0.034)

Model-based training with 2 models
Best R2: 0.234, Mean R2: 0.140
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.3077, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1605
  Round 1/3: Mean predicted reward = 10.131
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9676, entropy=0.3404, kl_div=0.0000
    Epoch 1: policy_loss=0.0075, value_loss=0.9676, entropy=0.3398, kl_div=0.0464
  Round 2/3: Mean predicted reward = 10.281
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9671, entropy=0.3265, kl_div=0.0000
    Epoch 1: policy_loss=-0.0130, value_loss=0.9671, entropy=0.3264, kl_div=0.0246
  Round 3/3: Mean predicted reward = 10.298

  === Progress Analysis ===
  Status: NORMAL

--- Round 59 Results ---
  Mean Oracle Reward: 10.423
  Min Oracle Reward: 8.280
  Max Oracle Reward: 12.894
  Std Oracle Reward: 1.082
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.140, Max: 0.234, Count: 13
  New best mean reward!
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

--- Generated Sequences (Diversity: 0.969) ---
  CGGTGATGCCAC
  AGGTTCCGCAGC
  TCAAGGGTCCGA
  GTCGGCAATGCC
  GAGGCTCTCGCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.520
  Max reward: 12.923
  With intrinsic bonuses: 10.550

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9678, entropy=0.3304, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7008

=== Surrogate Model Training ===
Total samples: 1970

Training on 1890 samples (removed 80 outliers)
Reward range: [7.23, 13.00], mean: 10.12
  Created 13 candidate models for data size 1890
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.177 (std: 0.052)
  rf-tuned-xl: R2 = 0.175 (std: 0.059)
  gb-tuned-l: R2 = 0.159 (std: 0.046)
  gb-tuned-xl: R2 = 0.159 (std: 0.046)
  xgb-xl: R2 = 0.155 (std: 0.094)
  xgb-l: R2 = 0.155 (std: 0.094)
  mlp-adaptive-xl: R2 = 0.169 (std: 0.083)
  mlp-l: R2 = 0.154 (std: 0.054)
  svr-rbf-xl: R2 = 0.239 (std: 0.042)
  svr-poly-l: R2 = 0.239 (std: 0.042)
  knn-tuned-sqrt: R2 = 0.083 (std: 0.068)
  knn-tuned-l: R2 = 0.083 (std: 0.068)
  ridge: R2 = -0.006 (std: 0.038)

Model-based training with 2 models
Best R2: 0.239, Mean R2: 0.149
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.2974, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0982
  Round 1/3: Mean predicted reward = 9.850
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.2974, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2474
  Round 2/3: Mean predicted reward = 10.001
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9656, entropy=0.3142, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6904
  Round 3/3: Mean predicted reward = 10.254

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 60 Results ---
  Mean Oracle Reward: 10.567
  Min Oracle Reward: 8.407
  Max Oracle Reward: 13.022
  Std Oracle Reward: 1.078
  Sequence Diversity: 0.969
  Models Used: 2
  Model R2 - Mean: 0.149, Max: 0.239, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 1970

======================================================================
EXPERIMENT ROUND 61/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1970
  Consistent improvement, increasing LR to 0.000327

--- Round 61 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCGGAGCCGTAT
  CCTACGTAGCGG
  GACCACGCTGTG
  AGTCACTCGGCG
  TCCACGGCGATG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.226
  Max reward: 12.409
  With intrinsic bonuses: 10.253

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9695, entropy=0.2973, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4381

=== Surrogate Model Training ===
Total samples: 2002

Training on 1921 samples (removed 81 outliers)
Reward range: [7.23, 13.03], mean: 10.12
  Created 13 candidate models for data size 1921
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.182 (std: 0.055)
  rf-tuned-xl: R2 = 0.176 (std: 0.057)
  gb-tuned-l: R2 = 0.168 (std: 0.055)
  gb-tuned-xl: R2 = 0.168 (std: 0.055)
  xgb-xl: R2 = 0.147 (std: 0.077)
  xgb-l: R2 = 0.147 (std: 0.077)
  mlp-adaptive-xl: R2 = 0.164 (std: 0.067)
  mlp-l: R2 = 0.167 (std: 0.044)
  svr-rbf-xl: R2 = 0.247 (std: 0.046)
  svr-poly-l: R2 = 0.247 (std: 0.046)
  knn-tuned-sqrt: R2 = 0.098 (std: 0.061)
  knn-tuned-l: R2 = 0.098 (std: 0.061)
  ridge: R2 = -0.003 (std: 0.047)

Model-based training with 2 models
Best R2: 0.247, Mean R2: 0.154
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2819, kl_div=0.0000
    Epoch 1: policy_loss=-0.0790, value_loss=0.9687, entropy=0.2820, kl_div=-0.1105
  Round 1/3: Mean predicted reward = 9.822
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.3263, kl_div=0.0000
    Epoch 1: policy_loss=-0.0304, value_loss=0.9692, entropy=0.3310, kl_div=-0.4542
  Round 2/3: Mean predicted reward = 10.098
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.2948, kl_div=0.0000
    Epoch 1: policy_loss=0.0206, value_loss=0.9680, entropy=0.2976, kl_div=-0.3042
  Round 3/3: Mean predicted reward = 10.193

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 61 Results ---
  Mean Oracle Reward: 10.238
  Min Oracle Reward: 5.906
  Max Oracle Reward: 12.545
  Std Oracle Reward: 1.368
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.154, Max: 0.247, Count: 13
  Total Sequences Evaluated: 2002

======================================================================
EXPERIMENT ROUND 62/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2002

--- Round 62 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  CTTAAGCGGACG
  GACCCTGTAGGC
  TCGCGACTGAAT
  CGGATGCACGCT
  GCTCGAGCCAGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.019
  Max reward: 11.554
  With intrinsic bonuses: 9.999

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.3228, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3082

=== Surrogate Model Training ===
Total samples: 2034

Training on 1952 samples (removed 82 outliers)
Reward range: [7.23, 13.03], mean: 10.12
  Created 13 candidate models for data size 1952
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.191 (std: 0.065)
  rf-tuned-xl: R2 = 0.178 (std: 0.068)
  gb-tuned-l: R2 = 0.173 (std: 0.058)
  gb-tuned-xl: R2 = 0.173 (std: 0.058)
  xgb-xl: R2 = 0.155 (std: 0.097)
  xgb-l: R2 = 0.155 (std: 0.097)
  mlp-adaptive-xl: R2 = 0.174 (std: 0.061)
  mlp-l: R2 = 0.175 (std: 0.053)
  svr-rbf-xl: R2 = 0.247 (std: 0.045)
  svr-poly-l: R2 = 0.247 (std: 0.045)
  knn-tuned-sqrt: R2 = 0.099 (std: 0.063)
  knn-tuned-l: R2 = 0.099 (std: 0.063)
  ridge: R2 = 0.002 (std: 0.046)

Model-based training with 2 models
Best R2: 0.247, Mean R2: 0.159
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.2818, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1144
  Round 1/3: Mean predicted reward = 9.780
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.3078, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0604
  Round 2/3: Mean predicted reward = 10.111
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9675, entropy=0.2889, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0779
  Round 3/3: Mean predicted reward = 10.253

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 62 Results ---
  Mean Oracle Reward: 10.015
  Min Oracle Reward: 5.948
  Max Oracle Reward: 11.721
  Std Oracle Reward: 1.108
  Sequence Diversity: 0.969
  Models Used: 2
  Model R2 - Mean: 0.159, Max: 0.247, Count: 13
  Total Sequences Evaluated: 2034

======================================================================
EXPERIMENT ROUND 63/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2034

--- Round 63 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGCGAACCTGGA
  CTACGGTCAGGC
  GCTAAGCCTGGC
  GCCACTGGTCGA
  GCTAGAGCGTCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.993
  Max reward: 11.792
  With intrinsic bonuses: 9.955

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2776, kl_div=0.0000
    Epoch 1: policy_loss=-0.0355, value_loss=0.9690, entropy=0.2772, kl_div=0.0013

=== Surrogate Model Training ===
Total samples: 2066

Training on 1982 samples (removed 84 outliers)
Reward range: [7.23, 13.00], mean: 10.12
  Created 13 candidate models for data size 1982
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.175 (std: 0.060)
  rf-tuned-xl: R2 = 0.179 (std: 0.048)
  gb-tuned-l: R2 = 0.169 (std: 0.049)
  gb-tuned-xl: R2 = 0.169 (std: 0.049)
  xgb-xl: R2 = 0.165 (std: 0.075)
  xgb-l: R2 = 0.165 (std: 0.075)
  mlp-adaptive-xl: R2 = 0.161 (std: 0.058)
  mlp-l: R2 = 0.143 (std: 0.059)
  svr-rbf-xl: R2 = 0.246 (std: 0.040)
  svr-poly-l: R2 = 0.246 (std: 0.040)
  knn-tuned-sqrt: R2 = 0.098 (std: 0.056)
  knn-tuned-l: R2 = 0.098 (std: 0.056)
  ridge: R2 = -0.000 (std: 0.048)

Model-based training with 2 models
Best R2: 0.246, Mean R2: 0.155
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.2783, kl_div=0.0000
    Epoch 1: policy_loss=-0.0648, value_loss=0.9688, entropy=0.2779, kl_div=-0.0474
  Round 1/3: Mean predicted reward = 9.860
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.2666, kl_div=0.0000
    Epoch 1: policy_loss=0.0276, value_loss=0.9684, entropy=0.2687, kl_div=-0.1779
  Round 2/3: Mean predicted reward = 9.930
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9681, entropy=0.3114, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1003
  Round 3/3: Mean predicted reward = 10.088

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 63 Results ---
  Mean Oracle Reward: 9.991
  Min Oracle Reward: 5.062
  Max Oracle Reward: 11.788
  Std Oracle Reward: 1.268
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.155, Max: 0.246, Count: 13
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
  GCGCAGGCATCT
  TACCTCCGGGAG
  CGTTAAGGCGCC
  CGACTGAGGCCT
  GTCTGCGCCAGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.006
  Max reward: 12.171
  With intrinsic bonuses: 9.979

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.3147, kl_div=0.0000
    Epoch 1: policy_loss=-0.0185, value_loss=0.9697, entropy=0.3143, kl_div=0.0005

=== Surrogate Model Training ===
Total samples: 2098

Training on 2013 samples (removed 85 outliers)
Reward range: [7.23, 13.00], mean: 10.12
  Created 13 candidate models for data size 2013
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.193 (std: 0.066)
  rf-tuned-xl: R2 = 0.193 (std: 0.066)
  gb-tuned-l: R2 = 0.173 (std: 0.056)
  gb-tuned-xl: R2 = 0.173 (std: 0.056)
  xgb-xl: R2 = 0.141 (std: 0.106)
  xgb-l: R2 = 0.141 (std: 0.106)
  mlp-adaptive-xl: R2 = 0.156 (std: 0.073)
  mlp-l: R2 = 0.135 (std: 0.095)
  svr-rbf-xl: R2 = 0.248 (std: 0.051)
  svr-poly-l: R2 = 0.248 (std: 0.051)
  knn-tuned-sqrt: R2 = 0.106 (std: 0.073)
  knn-tuned-l: R2 = 0.106 (std: 0.073)
  ridge: R2 = 0.009 (std: 0.051)

Model-based training with 2 models
Best R2: 0.248, Mean R2: 0.155
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.2763, kl_div=0.0000
    Epoch 1: policy_loss=-0.0447, value_loss=0.9701, entropy=0.2763, kl_div=-0.0777
  Round 1/3: Mean predicted reward = 9.754
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.3030, kl_div=0.0000
    Epoch 1: policy_loss=0.0024, value_loss=0.9680, entropy=0.3039, kl_div=-0.1465
  Round 2/3: Mean predicted reward = 9.862
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9715, entropy=0.2678, kl_div=0.0000
    Epoch 1: policy_loss=-0.0157, value_loss=0.9715, entropy=0.2692, kl_div=-0.1285
  Round 3/3: Mean predicted reward = 9.975

  === Progress Analysis ===
  Status: NORMAL

--- Round 64 Results ---
  Mean Oracle Reward: 10.016
  Min Oracle Reward: 6.196
  Max Oracle Reward: 12.126
  Std Oracle Reward: 1.169
  Sequence Diversity: 0.969
  Models Used: 2
  Model R2 - Mean: 0.155, Max: 0.248, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  ACCGGCCTGATG
  GCCTGAGCACTG
  GACCTGAGCTGA
  GGGATCATCAGC
  TCTGACAGCGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.818
  Max reward: 11.864
  With intrinsic bonuses: 9.751

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.3116, kl_div=0.0000
    Epoch 1: policy_loss=0.1350, value_loss=0.9690, entropy=0.3174, kl_div=-0.3518

=== Surrogate Model Training ===
Total samples: 2130

Training on 2043 samples (removed 87 outliers)
Reward range: [7.23, 13.00], mean: 10.12
  Created 13 candidate models for data size 2043
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.178 (std: 0.078)
  rf-tuned-xl: R2 = 0.179 (std: 0.073)
  gb-tuned-l: R2 = 0.186 (std: 0.052)
  gb-tuned-xl: R2 = 0.186 (std: 0.052)
  xgb-xl: R2 = 0.148 (std: 0.092)
  xgb-l: R2 = 0.148 (std: 0.092)
  mlp-adaptive-xl: R2 = 0.199 (std: 0.076)
  mlp-l: R2 = 0.191 (std: 0.079)
  svr-rbf-xl: R2 = 0.258 (std: 0.055)
  svr-poly-l: R2 = 0.258 (std: 0.055)
  knn-tuned-sqrt: R2 = 0.101 (std: 0.071)
  knn-tuned-l: R2 = 0.101 (std: 0.071)
  ridge: R2 = 0.011 (std: 0.054)

Model-based training with 2 models
Best R2: 0.258, Mean R2: 0.165
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.2676, kl_div=0.0000
    Epoch 1: policy_loss=-0.0630, value_loss=0.9699, entropy=0.2734, kl_div=-0.4526
  Round 1/3: Mean predicted reward = 9.413
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.2917, kl_div=0.0000
    Epoch 1: policy_loss=0.1085, value_loss=0.9705, entropy=0.2973, kl_div=-0.3396
  Round 2/3: Mean predicted reward = 9.917
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.3495, kl_div=0.0000
    Epoch 1: policy_loss=0.0380, value_loss=0.9693, entropy=0.3556, kl_div=-0.3319
  Round 3/3: Mean predicted reward = 10.307

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 65 Results ---
  Mean Oracle Reward: 9.749
  Min Oracle Reward: 5.576
  Max Oracle Reward: 11.988
  Std Oracle Reward: 1.407
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.165, Max: 0.258, Count: 13
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
  TCATGGCGGCAC
  CACAGGCGGTCT
  TACTGCAGCGGC
  CGCCGGACGATT
  CCGAGCTGTCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.869
  Max reward: 12.160
  With intrinsic bonuses: 9.944

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.3391, kl_div=0.0000
    Epoch 1: policy_loss=-0.0442, value_loss=0.9681, entropy=0.3413, kl_div=-0.0145

=== Surrogate Model Training ===
Total samples: 2162

Training on 2073 samples (removed 89 outliers)
Reward range: [7.23, 12.96], mean: 10.12
  Created 13 candidate models for data size 2073
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.204 (std: 0.059)
  rf-tuned-xl: R2 = 0.200 (std: 0.059)
  gb-tuned-l: R2 = 0.202 (std: 0.043)
  gb-tuned-xl: R2 = 0.202 (std: 0.043)
  xgb-xl: R2 = 0.141 (std: 0.078)
  xgb-l: R2 = 0.141 (std: 0.078)
  mlp-adaptive-xl: R2 = 0.194 (std: 0.053)
  mlp-l: R2 = 0.210 (std: 0.060)
  svr-rbf-xl: R2 = 0.268 (std: 0.053)
  svr-poly-l: R2 = 0.268 (std: 0.053)
  knn-tuned-sqrt: R2 = 0.119 (std: 0.062)
  knn-tuned-l: R2 = 0.119 (std: 0.062)
  ridge: R2 = 0.022 (std: 0.056)

Model-based training with 7 models
Best R2: 0.268, Mean R2: 0.176
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.140 rf-tuned-xl:0.140 gb-tuned-l:0.140 gb-tuned-xl:0.140 mlp-l:0.141 svr-rbf-xl:0.150 svr-poly-l:0.150 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.2826, kl_div=0.0000
    Epoch 1: policy_loss=-0.0581, value_loss=0.9686, entropy=0.2850, kl_div=-0.0733
  Round 1/3: Mean predicted reward = 9.725
    Using performance-based weights
    Model weights: rf-tuned-l:0.140 rf-tuned-xl:0.140 gb-tuned-l:0.140 gb-tuned-xl:0.140 mlp-l:0.141 svr-rbf-xl:0.150 svr-poly-l:0.150 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.2980, kl_div=0.0000
    Epoch 1: policy_loss=-0.0346, value_loss=0.9696, entropy=0.3063, kl_div=-0.1694
  Round 2/3: Mean predicted reward = 9.759
    Using performance-based weights
    Model weights: rf-tuned-l:0.140 rf-tuned-xl:0.140 gb-tuned-l:0.140 gb-tuned-xl:0.140 mlp-l:0.141 svr-rbf-xl:0.150 svr-poly-l:0.150 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.3589, kl_div=0.0000
    Epoch 1: policy_loss=0.0078, value_loss=0.9703, entropy=0.3658, kl_div=-0.1704
  Round 3/3: Mean predicted reward = 9.945

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 66 Results ---
  Mean Oracle Reward: 9.887
  Min Oracle Reward: 6.197
  Max Oracle Reward: 12.252
  Std Oracle Reward: 1.175
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: 0.176, Max: 0.268, Count: 13
  Total Sequences Evaluated: 2162

======================================================================
EXPERIMENT ROUND 67/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2162
  Performance plateaued, reducing LR to 0.000100

--- Round 67 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CAGCGTTACGCG
  GTCATCCGACGG
  GGGAGTCCTCCA
  ACGCTGTGCCGA
  GTGCGCCCAATG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.052
  Max reward: 11.811
  With intrinsic bonuses: 10.067

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9678, entropy=0.3709, kl_div=0.0000
    Epoch 1: policy_loss=-0.0502, value_loss=0.9678, entropy=0.3736, kl_div=-0.0557

=== Surrogate Model Training ===
Total samples: 2194

Training on 2104 samples (removed 90 outliers)
Reward range: [7.23, 12.96], mean: 10.12
  Created 13 candidate models for data size 2104
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.207 (std: 0.063)
  rf-tuned-xl: R2 = 0.209 (std: 0.058)
  gb-tuned-l: R2 = 0.205 (std: 0.048)
  gb-tuned-xl: R2 = 0.205 (std: 0.048)
  xgb-xl: R2 = 0.170 (std: 0.072)
  xgb-l: R2 = 0.170 (std: 0.072)
  mlp-adaptive-xl: R2 = 0.198 (std: 0.068)
  mlp-l: R2 = 0.178 (std: 0.055)
  svr-rbf-xl: R2 = 0.272 (std: 0.052)
  svr-poly-l: R2 = 0.272 (std: 0.052)
  knn-tuned-sqrt: R2 = 0.123 (std: 0.055)
  knn-tuned-l: R2 = 0.123 (std: 0.055)
  ridge: R2 = 0.025 (std: 0.058)

Model-based training with 6 models
Best R2: 0.272, Mean R2: 0.181
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.163 rf-tuned-xl:0.163 gb-tuned-l:0.163 gb-tuned-xl:0.163 svr-rbf-xl:0.174 svr-poly-l:0.174 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.3533, kl_div=0.0000
    Epoch 1: policy_loss=-0.0356, value_loss=0.9687, entropy=0.3565, kl_div=-0.1091
  Round 1/3: Mean predicted reward = 9.822
    Using performance-based weights
    Model weights: rf-tuned-l:0.163 rf-tuned-xl:0.163 gb-tuned-l:0.163 gb-tuned-xl:0.163 svr-rbf-xl:0.174 svr-poly-l:0.174 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.3946, kl_div=0.0000
    Epoch 1: policy_loss=-0.0132, value_loss=0.9691, entropy=0.3989, kl_div=-0.2293
  Round 2/3: Mean predicted reward = 10.093
    Using performance-based weights
    Model weights: rf-tuned-l:0.163 rf-tuned-xl:0.163 gb-tuned-l:0.163 gb-tuned-xl:0.163 svr-rbf-xl:0.174 svr-poly-l:0.174 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.3600, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1175
  Round 3/3: Mean predicted reward = 10.097

  === Progress Analysis ===
  Status: NORMAL

--- Round 67 Results ---
  Mean Oracle Reward: 10.058
  Min Oracle Reward: 5.838
  Max Oracle Reward: 11.880
  Std Oracle Reward: 1.121
  Sequence Diversity: 1.000
  Models Used: 6
  Model R2 - Mean: 0.181, Max: 0.272, Count: 13
  Total Sequences Evaluated: 2194

======================================================================
EXPERIMENT ROUND 68/100
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2194
  Consistent improvement, increasing LR to 0.000132

--- Round 68 Configuration ---
Learning rate: 0.000132
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  TGTGGACAACTC
  GGACGCCAGTTC
  CAGCCGCAGTTG
  CGAGGTACGTAC
  ACTACCTGGGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.740
  Max reward: 12.373
  With intrinsic bonuses: 9.644

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=0.3716, kl_div=0.0000
    Epoch 1: policy_loss=-0.0272, value_loss=0.9678, entropy=0.3734, kl_div=-0.0584

=== Surrogate Model Training ===
Total samples: 2226

Training on 2132 samples (removed 94 outliers)
Reward range: [7.24, 12.96], mean: 10.12
  Created 13 candidate models for data size 2132
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.211 (std: 0.049)
  rf-tuned-xl: R2 = 0.218 (std: 0.047)
  gb-tuned-l: R2 = 0.201 (std: 0.048)
  gb-tuned-xl: R2 = 0.201 (std: 0.048)
  xgb-xl: R2 = 0.160 (std: 0.062)
  xgb-l: R2 = 0.160 (std: 0.062)
  mlp-adaptive-xl: R2 = 0.184 (std: 0.062)
  mlp-l: R2 = 0.196 (std: 0.048)
  svr-rbf-xl: R2 = 0.265 (std: 0.049)
  svr-poly-l: R2 = 0.265 (std: 0.049)
  knn-tuned-sqrt: R2 = 0.119 (std: 0.041)
  knn-tuned-l: R2 = 0.119 (std: 0.041)
  ridge: R2 = 0.028 (std: 0.064)

Model-based training with 6 models
Best R2: 0.265, Mean R2: 0.179
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.164 rf-tuned-xl:0.165 gb-tuned-l:0.162 gb-tuned-xl:0.162 svr-rbf-xl:0.173 svr-poly-l:0.173 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=0.3437, kl_div=0.0000
    Epoch 1: policy_loss=0.0137, value_loss=0.9704, entropy=0.3451, kl_div=-0.3139
  Round 1/3: Mean predicted reward = 9.753
    Using performance-based weights
    Model weights: rf-tuned-l:0.164 rf-tuned-xl:0.165 gb-tuned-l:0.162 gb-tuned-xl:0.162 svr-rbf-xl:0.173 svr-poly-l:0.173 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9700, entropy=0.3627, kl_div=0.0000
    Epoch 1: policy_loss=-0.0365, value_loss=0.9700, entropy=0.3611, kl_div=-0.2309
  Round 2/3: Mean predicted reward = 9.911
    Using performance-based weights
    Model weights: rf-tuned-l:0.164 rf-tuned-xl:0.165 gb-tuned-l:0.162 gb-tuned-xl:0.162 svr-rbf-xl:0.173 svr-poly-l:0.173 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.4026, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1579
  Round 3/3: Mean predicted reward = 10.119

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 68 Results ---
  Mean Oracle Reward: 9.688
  Min Oracle Reward: 4.259
  Max Oracle Reward: 12.524
  Std Oracle Reward: 1.667
  Sequence Diversity: 0.969
  Models Used: 6
  Model R2 - Mean: 0.179, Max: 0.265, Count: 13
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
  ATCTGGCCGAAG
  GCGGCATCGTCA
  GTACATGCAGCG
  TCACGCCGGGAT
  ATCGTCCGGAGC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.306
  Max reward: 12.385
  With intrinsic bonuses: 10.276

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9675, entropy=0.3626, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0761

=== Surrogate Model Training ===
Total samples: 2258

Training on 2158 samples (removed 100 outliers)
Reward range: [7.26, 12.90], mean: 10.12
  Created 13 candidate models for data size 2158
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.214 (std: 0.040)
  rf-tuned-xl: R2 = 0.212 (std: 0.047)
  gb-tuned-l: R2 = 0.199 (std: 0.050)
  gb-tuned-xl: R2 = 0.199 (std: 0.050)
  xgb-xl: R2 = 0.161 (std: 0.069)
  xgb-l: R2 = 0.161 (std: 0.069)
  mlp-adaptive-xl: R2 = 0.180 (std: 0.054)
  mlp-l: R2 = 0.208 (std: 0.059)
  svr-rbf-xl: R2 = 0.263 (std: 0.048)
  svr-poly-l: R2 = 0.263 (std: 0.048)
  knn-tuned-sqrt: R2 = 0.116 (std: 0.030)
  knn-tuned-l: R2 = 0.116 (std: 0.030)
  ridge: R2 = 0.025 (std: 0.062)

Model-based training with 5 models
Best R2: 0.263, Mean R2: 0.178
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.196 rf-tuned-xl:0.196 mlp-l:0.195 svr-rbf-xl:0.206 svr-poly-l:0.206 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.3729, kl_div=0.0000
    Epoch 1: policy_loss=-0.0106, value_loss=0.9690, entropy=0.3723, kl_div=0.0390
  Round 1/3: Mean predicted reward = 10.013
    Using performance-based weights
    Model weights: rf-tuned-l:0.196 rf-tuned-xl:0.196 mlp-l:0.195 svr-rbf-xl:0.206 svr-poly-l:0.206 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.3689, kl_div=0.0000
    Epoch 1: policy_loss=-0.0332, value_loss=0.9686, entropy=0.3679, kl_div=-0.0307
  Round 2/3: Mean predicted reward = 9.970
    Using performance-based weights
    Model weights: rf-tuned-l:0.196 rf-tuned-xl:0.196 mlp-l:0.195 svr-rbf-xl:0.206 svr-poly-l:0.206 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3651, kl_div=0.0000
    Epoch 1: policy_loss=0.0039, value_loss=0.9689, entropy=0.3644, kl_div=-0.0463
  Round 3/3: Mean predicted reward = 10.228

  === Progress Analysis ===
  Status: NORMAL

--- Round 69 Results ---
  Mean Oracle Reward: 10.260
  Min Oracle Reward: 6.505
  Max Oracle Reward: 12.344
  Std Oracle Reward: 1.129
  Sequence Diversity: 1.000
  Models Used: 5
  Model R2 - Mean: 0.178, Max: 0.263, Count: 13
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
  GCGGCGCCATTA
  TCTGCAGCATGA
  GCGCTGACGATC
  CGCAGGCTGTCA
  TGCAGCCGCTAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.251
  Max reward: 12.279
  With intrinsic bonuses: 10.271

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9667, entropy=0.4139, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4870

=== Surrogate Model Training ===
Total samples: 2290

Training on 2186 samples (removed 104 outliers)
Reward range: [7.28, 12.90], mean: 10.13
  Created 13 candidate models for data size 2186
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.204 (std: 0.037)
  rf-tuned-xl: R2 = 0.205 (std: 0.034)
  gb-tuned-l: R2 = 0.199 (std: 0.047)
  gb-tuned-xl: R2 = 0.199 (std: 0.047)
  xgb-xl: R2 = 0.159 (std: 0.063)
  xgb-l: R2 = 0.159 (std: 0.063)
  mlp-adaptive-xl: R2 = 0.194 (std: 0.072)
  mlp-l: R2 = 0.174 (std: 0.046)
  svr-rbf-xl: R2 = 0.257 (std: 0.046)
  svr-poly-l: R2 = 0.257 (std: 0.046)
  knn-tuned-sqrt: R2 = 0.114 (std: 0.037)
  knn-tuned-l: R2 = 0.114 (std: 0.037)
  ridge: R2 = 0.021 (std: 0.066)

Model-based training with 4 models
Best R2: 0.257, Mean R2: 0.174
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.243 rf-tuned-xl:0.243 svr-rbf-xl:0.257 svr-poly-l:0.257 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.3764, kl_div=0.0000
    Epoch 1: policy_loss=-0.0662, value_loss=0.9690, entropy=0.3739, kl_div=-0.0501
  Round 1/3: Mean predicted reward = 9.941
    Using performance-based weights
    Model weights: rf-tuned-l:0.243 rf-tuned-xl:0.243 svr-rbf-xl:0.257 svr-poly-l:0.257 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9676, entropy=0.3650, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1160
  Round 2/3: Mean predicted reward = 10.079
    Using performance-based weights
    Model weights: rf-tuned-l:0.243 rf-tuned-xl:0.243 svr-rbf-xl:0.257 svr-poly-l:0.257 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.3524, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0840
  Round 3/3: Mean predicted reward = 10.174

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 70 Results ---
  Mean Oracle Reward: 10.244
  Min Oracle Reward: 6.281
  Max Oracle Reward: 12.260
  Std Oracle Reward: 1.204
  Sequence Diversity: 1.000
  Models Used: 4
  Model R2 - Mean: 0.174, Max: 0.257, Count: 13
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
  CTCCGCAGGGTA
  GGTCTACAGCGC
  CCGGCCGAGATT
  CTACGCGCTAGG
  GACTTCCCGGGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.179
  Max reward: 12.829
  With intrinsic bonuses: 10.217

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3471, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5688

=== Surrogate Model Training ===
Total samples: 2322

Training on 2217 samples (removed 105 outliers)
Reward range: [7.28, 12.90], mean: 10.13
  Created 13 candidate models for data size 2217
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.206 (std: 0.030)
  rf-tuned-xl: R2 = 0.208 (std: 0.037)
  gb-tuned-l: R2 = 0.203 (std: 0.049)
  gb-tuned-xl: R2 = 0.203 (std: 0.049)
  xgb-xl: R2 = 0.141 (std: 0.061)
  xgb-l: R2 = 0.141 (std: 0.061)
  mlp-adaptive-xl: R2 = 0.183 (std: 0.049)
  mlp-l: R2 = 0.191 (std: 0.055)
  svr-rbf-xl: R2 = 0.260 (std: 0.049)
  svr-poly-l: R2 = 0.260 (std: 0.049)
  knn-tuned-sqrt: R2 = 0.119 (std: 0.046)
  knn-tuned-l: R2 = 0.119 (std: 0.046)
  ridge: R2 = 0.021 (std: 0.059)

Model-based training with 6 models
Best R2: 0.260, Mean R2: 0.174
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.164 rf-tuned-xl:0.164 gb-tuned-l:0.163 gb-tuned-xl:0.163 svr-rbf-xl:0.173 svr-poly-l:0.173 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.3354, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5102
  Round 1/3: Mean predicted reward = 9.749
    Using performance-based weights
    Model weights: rf-tuned-l:0.164 rf-tuned-xl:0.164 gb-tuned-l:0.163 gb-tuned-xl:0.163 svr-rbf-xl:0.173 svr-poly-l:0.173 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9673, entropy=0.3224, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7236
  Round 2/3: Mean predicted reward = 10.029
    Using performance-based weights
    Model weights: rf-tuned-l:0.164 rf-tuned-xl:0.164 gb-tuned-l:0.163 gb-tuned-xl:0.163 svr-rbf-xl:0.173 svr-poly-l:0.173 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.3299, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6094
  Round 3/3: Mean predicted reward = 10.179

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 71 Results ---
  Mean Oracle Reward: 10.204
  Min Oracle Reward: 7.240
  Max Oracle Reward: 12.751
  Std Oracle Reward: 1.236
  Sequence Diversity: 1.000
  Models Used: 6
  Model R2 - Mean: 0.174, Max: 0.260, Count: 13
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

--- Generated Sequences (Diversity: 0.969) ---
  CCGCGTAGACTG
  CTGGTAAGACCG
  GCGACGGCTCAT
  GCATTACGGAGC
  CAGTGGAGCCCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.876
  Max reward: 11.576
  With intrinsic bonuses: 9.900

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9682, entropy=0.3283, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0932

=== Surrogate Model Training ===
Total samples: 2354

Training on 2242 samples (removed 112 outliers)
Reward range: [7.31, 12.90], mean: 10.14
  Created 13 candidate models for data size 2242
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.201 (std: 0.047)
  rf-tuned-xl: R2 = 0.199 (std: 0.039)
  gb-tuned-l: R2 = 0.198 (std: 0.046)
  gb-tuned-xl: R2 = 0.198 (std: 0.046)
  xgb-xl: R2 = 0.110 (std: 0.101)
  xgb-l: R2 = 0.110 (std: 0.101)
  mlp-adaptive-xl: R2 = 0.148 (std: 0.063)
  mlp-l: R2 = 0.154 (std: 0.045)
  svr-rbf-xl: R2 = 0.249 (std: 0.041)
  svr-poly-l: R2 = 0.249 (std: 0.041)
  knn-tuned-sqrt: R2 = 0.114 (std: 0.043)
  knn-tuned-l: R2 = 0.114 (std: 0.043)
  ridge: R2 = 0.018 (std: 0.061)

Model-based training with 3 models
Best R2: 0.249, Mean R2: 0.159
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.323 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.3334, kl_div=0.0000
    Epoch 1: policy_loss=-0.0241, value_loss=0.9696, entropy=0.3320, kl_div=0.0323
  Round 1/3: Mean predicted reward = 9.830
    Using performance-based weights
    Model weights: rf-tuned-l:0.323 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.3249, kl_div=0.0000
    Epoch 1: policy_loss=0.0149, value_loss=0.9688, entropy=0.3259, kl_div=-0.3176
  Round 2/3: Mean predicted reward = 9.965
    Using performance-based weights
    Model weights: rf-tuned-l:0.323 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9676, entropy=0.3227, kl_div=0.0000
    Epoch 1: policy_loss=-0.0390, value_loss=0.9676, entropy=0.3235, kl_div=-0.0260
  Round 3/3: Mean predicted reward = 9.977

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 72 Results ---
  Mean Oracle Reward: 9.873
  Min Oracle Reward: 5.220
  Max Oracle Reward: 11.748
  Std Oracle Reward: 1.439
  Sequence Diversity: 0.969
  Models Used: 3
  Model R2 - Mean: 0.159, Max: 0.249, Count: 13
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
  CTAGGGCCTCAG
  CTAGGACCTGCG
  GGTCCCGATGCA
  GCATCCGAGGCT
  GCACCTCGGGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.880
  Max reward: 12.260
  With intrinsic bonuses: 9.910

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9677, entropy=0.3060, kl_div=0.0000
    Epoch 1: policy_loss=-0.0565, value_loss=0.9677, entropy=0.3087, kl_div=0.0222

=== Surrogate Model Training ===
Total samples: 2386

Training on 2274 samples (removed 112 outliers)
Reward range: [7.31, 12.90], mean: 10.14
  Created 13 candidate models for data size 2274
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.199 (std: 0.055)
  rf-tuned-xl: R2 = 0.202 (std: 0.050)
  gb-tuned-l: R2 = 0.196 (std: 0.055)
  gb-tuned-xl: R2 = 0.196 (std: 0.055)
  xgb-xl: R2 = 0.129 (std: 0.080)
  xgb-l: R2 = 0.129 (std: 0.080)
  mlp-adaptive-xl: R2 = 0.182 (std: 0.077)
  mlp-l: R2 = 0.166 (std: 0.049)
  svr-rbf-xl: R2 = 0.253 (std: 0.046)
  svr-poly-l: R2 = 0.253 (std: 0.046)
  knn-tuned-sqrt: R2 = 0.116 (std: 0.044)
  knn-tuned-l: R2 = 0.116 (std: 0.044)
  ridge: R2 = 0.024 (std: 0.066)

Model-based training with 3 models
Best R2: 0.253, Mean R2: 0.166
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-xl:0.322 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3324, kl_div=0.0000
    Epoch 1: policy_loss=-0.0189, value_loss=0.9689, entropy=0.3355, kl_div=-0.1659
  Round 1/3: Mean predicted reward = 9.906
    Using performance-based weights
    Model weights: rf-tuned-xl:0.322 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.3398, kl_div=0.0000
    Epoch 1: policy_loss=-0.0157, value_loss=0.9691, entropy=0.3423, kl_div=-0.2298
  Round 2/3: Mean predicted reward = 9.903
    Using performance-based weights
    Model weights: rf-tuned-xl:0.322 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.3251, kl_div=0.0000
    Epoch 1: policy_loss=-0.0445, value_loss=0.9684, entropy=0.3270, kl_div=0.0298
  Round 3/3: Mean predicted reward = 10.013

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 73 Results ---
  Mean Oracle Reward: 9.929
  Min Oracle Reward: 7.304
  Max Oracle Reward: 12.113
  Std Oracle Reward: 1.244
  Sequence Diversity: 1.000
  Models Used: 3
  Model R2 - Mean: 0.166, Max: 0.253, Count: 13
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
  CTGGCCAGTAGC
  CAGCCGCGATGT
  GCGAGTAGTCCC
  GTCCCGAGATCG
  CTGGCGTCGCAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.125
  Max reward: 12.222
  With intrinsic bonuses: 10.178

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.3562, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0548

=== Surrogate Model Training ===
Total samples: 2418

Training on 2303 samples (removed 115 outliers)
Reward range: [7.32, 12.90], mean: 10.14
  Created 13 candidate models for data size 2303
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.192 (std: 0.058)
  rf-tuned-xl: R2 = 0.203 (std: 0.059)
  gb-tuned-l: R2 = 0.193 (std: 0.056)
  gb-tuned-xl: R2 = 0.193 (std: 0.056)
  xgb-xl: R2 = 0.120 (std: 0.082)
  xgb-l: R2 = 0.120 (std: 0.082)
  mlp-adaptive-xl: R2 = 0.180 (std: 0.059)
  mlp-l: R2 = 0.155 (std: 0.060)
  svr-rbf-xl: R2 = 0.256 (std: 0.045)
  svr-poly-l: R2 = 0.256 (std: 0.045)
  knn-tuned-sqrt: R2 = 0.112 (std: 0.041)
  knn-tuned-l: R2 = 0.112 (std: 0.041)
  ridge: R2 = 0.021 (std: 0.061)

Model-based training with 3 models
Best R2: 0.256, Mean R2: 0.162
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-xl:0.322 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.3269, kl_div=0.0000
    Epoch 1: policy_loss=-0.0174, value_loss=0.9684, entropy=0.3284, kl_div=-0.0016
  Round 1/3: Mean predicted reward = 9.889
    Using performance-based weights
    Model weights: rf-tuned-xl:0.322 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.3664, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0614
  Round 2/3: Mean predicted reward = 9.902
    Using performance-based weights
    Model weights: rf-tuned-xl:0.322 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.3322, kl_div=0.0000
    Epoch 1: policy_loss=-0.0259, value_loss=0.9705, entropy=0.3324, kl_div=0.0496
  Round 3/3: Mean predicted reward = 10.118

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 74 Results ---
  Mean Oracle Reward: 10.127
  Min Oracle Reward: 6.355
  Max Oracle Reward: 12.387
  Std Oracle Reward: 1.271
  Sequence Diversity: 0.969
  Models Used: 3
  Model R2 - Mean: 0.162, Max: 0.256, Count: 13
  Total Sequences Evaluated: 2418

======================================================================
EXPERIMENT ROUND 75/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2418
  Consistent improvement, increasing LR to 0.000360

--- Round 75 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTAAAGCGCTCG
  GGGCCTGCACTA
  CCGCATCGAGTG
  CGTACCGGTACG
  CGCAAGGTTCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 9.870
  Max reward: 12.732
  With intrinsic bonuses: 9.856

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9672, entropy=0.3213, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4285

=== Surrogate Model Training ===
Total samples: 2450

Training on 2332 samples (removed 118 outliers)
Reward range: [7.32, 12.90], mean: 10.14
  Created 13 candidate models for data size 2332
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.194 (std: 0.072)
  rf-tuned-xl: R2 = 0.192 (std: 0.077)
  gb-tuned-l: R2 = 0.193 (std: 0.051)
  gb-tuned-xl: R2 = 0.193 (std: 0.051)
  xgb-xl: R2 = 0.112 (std: 0.115)
  xgb-l: R2 = 0.112 (std: 0.115)
  mlp-adaptive-xl: R2 = 0.178 (std: 0.070)
  mlp-l: R2 = 0.179 (std: 0.058)
  svr-rbf-xl: R2 = 0.258 (std: 0.050)
  svr-poly-l: R2 = 0.258 (std: 0.050)
  knn-tuned-sqrt: R2 = 0.112 (std: 0.049)
  knn-tuned-l: R2 = 0.112 (std: 0.049)
  ridge: R2 = 0.021 (std: 0.060)

Model-based training with 2 models
Best R2: 0.258, Mean R2: 0.163
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3260, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0609
  Round 1/3: Mean predicted reward = 9.938
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.3886, kl_div=0.0000
    Epoch 1: policy_loss=0.0218, value_loss=0.9684, entropy=0.3921, kl_div=-0.1812
  Round 2/3: Mean predicted reward = 9.971
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.3511, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5023
  Round 3/3: Mean predicted reward = 10.156

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 75 Results ---
  Mean Oracle Reward: 9.872
  Min Oracle Reward: 0.946
  Max Oracle Reward: 13.066
  Std Oracle Reward: 2.025
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.163, Max: 0.258, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  CGTACTGGAAGC
  CAAGGGGTCCTA
  ACCGCAGCGTGT
  GGTCGATGCCAC
  TCCATGGGCCGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.268
  Max reward: 11.897
  With intrinsic bonuses: 10.264

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9673, entropy=0.3227, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7757

=== Surrogate Model Training ===
Total samples: 2482

Training on 2364 samples (removed 118 outliers)
Reward range: [7.32, 12.90], mean: 10.14
  Created 13 candidate models for data size 2364
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.197 (std: 0.065)
  rf-tuned-xl: R2 = 0.201 (std: 0.057)
  gb-tuned-l: R2 = 0.193 (std: 0.046)
  gb-tuned-xl: R2 = 0.193 (std: 0.046)
  xgb-xl: R2 = 0.118 (std: 0.106)
  xgb-l: R2 = 0.118 (std: 0.106)
  mlp-adaptive-xl: R2 = 0.181 (std: 0.061)
  mlp-l: R2 = 0.180 (std: 0.065)
  svr-rbf-xl: R2 = 0.255 (std: 0.050)
  svr-poly-l: R2 = 0.255 (std: 0.050)
  knn-tuned-sqrt: R2 = 0.106 (std: 0.031)
  knn-tuned-l: R2 = 0.106 (std: 0.031)
  ridge: R2 = 0.018 (std: 0.057)

Model-based training with 3 models
Best R2: 0.255, Mean R2: 0.163
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-xl:0.321 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.3432, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3020
  Round 1/3: Mean predicted reward = 9.740
    Using performance-based weights
    Model weights: rf-tuned-xl:0.321 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.3174, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1365
  Round 2/3: Mean predicted reward = 10.008
    Using performance-based weights
    Model weights: rf-tuned-xl:0.321 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9666, entropy=0.3317, kl_div=0.0000
    Epoch 1: policy_loss=-0.0581, value_loss=0.9666, entropy=0.3331, kl_div=-0.0441
  Round 3/3: Mean predicted reward = 10.038

  === Progress Analysis ===
  Status: NORMAL

--- Round 76 Results ---
  Mean Oracle Reward: 10.216
  Min Oracle Reward: 8.238
  Max Oracle Reward: 11.537
  Std Oracle Reward: 0.803
  Sequence Diversity: 1.000
  Models Used: 3
  Model R2 - Mean: 0.163, Max: 0.255, Count: 13
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
  CCAGTGGACTCG
  CACGCGTCGTAG
  AGGGTCGTCCAC
  CAGCTCTGGAGC
  CTGACAGGCGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.223
  Max reward: 11.145
  With intrinsic bonuses: 10.201

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.3382, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3519

=== Surrogate Model Training ===
Total samples: 2514

Training on 2393 samples (removed 121 outliers)
Reward range: [7.33, 12.88], mean: 10.14
  Created 13 candidate models for data size 2393
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.205 (std: 0.053)
  rf-tuned-xl: R2 = 0.203 (std: 0.054)
  gb-tuned-l: R2 = 0.188 (std: 0.038)
  gb-tuned-xl: R2 = 0.188 (std: 0.038)
  xgb-xl: R2 = 0.114 (std: 0.097)
  xgb-l: R2 = 0.114 (std: 0.097)
  mlp-adaptive-xl: R2 = 0.174 (std: 0.063)
  mlp-l: R2 = 0.159 (std: 0.094)
  svr-rbf-xl: R2 = 0.251 (std: 0.035)
  svr-poly-l: R2 = 0.251 (std: 0.035)
  knn-tuned-sqrt: R2 = 0.103 (std: 0.021)
  knn-tuned-l: R2 = 0.103 (std: 0.021)
  ridge: R2 = 0.020 (std: 0.054)

Model-based training with 4 models
Best R2: 0.251, Mean R2: 0.160
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.244 rf-tuned-xl:0.244 svr-rbf-xl:0.256 svr-poly-l:0.256 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.3517, kl_div=0.0000
    Epoch 1: policy_loss=-0.0438, value_loss=0.9694, entropy=0.3547, kl_div=-0.1083
  Round 1/3: Mean predicted reward = 9.890
    Using performance-based weights
    Model weights: rf-tuned-l:0.244 rf-tuned-xl:0.244 svr-rbf-xl:0.256 svr-poly-l:0.256 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.3193, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1349
  Round 2/3: Mean predicted reward = 9.876
    Using performance-based weights
    Model weights: rf-tuned-l:0.244 rf-tuned-xl:0.244 svr-rbf-xl:0.256 svr-poly-l:0.256 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.3343, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1952
  Round 3/3: Mean predicted reward = 10.117

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 77 Results ---
  Mean Oracle Reward: 10.274
  Min Oracle Reward: 8.463
  Max Oracle Reward: 11.232
  Std Oracle Reward: 0.736
  Sequence Diversity: 1.000
  Models Used: 4
  Model R2 - Mean: 0.160, Max: 0.251, Count: 13
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
  ATAGCGGCTAGC
  AAGCGCGGTTCC
  CCGGTTAGCGAC
  GTAGCCTCGCAG
  GTCACCTGGACG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.317
  Max reward: 12.703
  With intrinsic bonuses: 10.306

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9679, entropy=0.3116, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2500

=== Surrogate Model Training ===
Total samples: 2546

Training on 2422 samples (removed 124 outliers)
Reward range: [7.34, 12.88], mean: 10.15
  Created 13 candidate models for data size 2422
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.197 (std: 0.042)
  rf-tuned-xl: R2 = 0.188 (std: 0.045)
  gb-tuned-l: R2 = 0.182 (std: 0.025)
  gb-tuned-xl: R2 = 0.182 (std: 0.025)
  xgb-xl: R2 = 0.129 (std: 0.069)
  xgb-l: R2 = 0.129 (std: 0.069)
  mlp-adaptive-xl: R2 = 0.159 (std: 0.034)
  mlp-l: R2 = 0.152 (std: 0.063)
  svr-rbf-xl: R2 = 0.253 (std: 0.037)
  svr-poly-l: R2 = 0.253 (std: 0.037)
  knn-tuned-sqrt: R2 = 0.089 (std: 0.023)
  knn-tuned-l: R2 = 0.089 (std: 0.023)
  ridge: R2 = 0.017 (std: 0.051)

Model-based training with 2 models
Best R2: 0.253, Mean R2: 0.156
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.3447, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0984
  Round 1/3: Mean predicted reward = 9.773
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.3413, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0878
  Round 2/3: Mean predicted reward = 9.951
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.3006, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3144
  Round 3/3: Mean predicted reward = 9.989

  === Progress Analysis ===
  Status: NORMAL

--- Round 78 Results ---
  Mean Oracle Reward: 10.283
  Min Oracle Reward: 7.659
  Max Oracle Reward: 12.927
  Std Oracle Reward: 0.900
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.156, Max: 0.253, Count: 13
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
  TGGATCCCCGGA
  ATCCAGTCCGGG
  CGGTAACGTCCG
  GTTGCAGAACCG
  GCGCCTTAGGAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.362
  Max reward: 12.689
  With intrinsic bonuses: 10.348

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.3092, kl_div=0.0000
    Epoch 1: policy_loss=-0.0099, value_loss=0.9680, entropy=0.3088, kl_div=0.0419

=== Surrogate Model Training ===
Total samples: 2578

Training on 2451 samples (removed 127 outliers)
Reward range: [7.37, 12.86], mean: 10.15
  Created 13 candidate models for data size 2451
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.191 (std: 0.028)
  rf-tuned-xl: R2 = 0.184 (std: 0.028)
  gb-tuned-l: R2 = 0.183 (std: 0.029)
  gb-tuned-xl: R2 = 0.183 (std: 0.029)
  xgb-xl: R2 = 0.142 (std: 0.068)
  xgb-l: R2 = 0.142 (std: 0.068)
  mlp-adaptive-xl: R2 = 0.163 (std: 0.051)
  mlp-l: R2 = 0.167 (std: 0.027)
  svr-rbf-xl: R2 = 0.248 (std: 0.034)
  svr-poly-l: R2 = 0.248 (std: 0.034)
  knn-tuned-sqrt: R2 = 0.090 (std: 0.030)
  knn-tuned-l: R2 = 0.090 (std: 0.030)
  ridge: R2 = 0.018 (std: 0.048)

Model-based training with 2 models
Best R2: 0.248, Mean R2: 0.158
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.2811, kl_div=0.0000
    Epoch 1: policy_loss=-0.0020, value_loss=0.9680, entropy=0.2811, kl_div=0.0112
  Round 1/3: Mean predicted reward = 9.684
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.3334, kl_div=0.0000
    Epoch 1: policy_loss=-0.0080, value_loss=0.9684, entropy=0.3338, kl_div=-0.0184
  Round 2/3: Mean predicted reward = 9.951
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.3273, kl_div=0.0000
    Epoch 1: policy_loss=-0.0041, value_loss=0.9693, entropy=0.3275, kl_div=-0.0128
  Round 3/3: Mean predicted reward = 10.188

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 79 Results ---
  Mean Oracle Reward: 10.330
  Min Oracle Reward: 7.547
  Max Oracle Reward: 12.793
  Std Oracle Reward: 1.038
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.158, Max: 0.248, Count: 13
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
  CCGTGCACTGAG
  CACGAGCGTGTC
  GAGTCCCCGTAG
  GCACAGTTGCGA
  ATGGTCCACCGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.297
  Max reward: 11.973
  With intrinsic bonuses: 10.302

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.3112, kl_div=0.0000
    Epoch 1: policy_loss=-0.0324, value_loss=0.9694, entropy=0.3104, kl_div=-0.0307

=== Surrogate Model Training ===
Total samples: 2610

Training on 2480 samples (removed 130 outliers)
Reward range: [7.40, 12.86], mean: 10.16
  Created 13 candidate models for data size 2480
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.193 (std: 0.032)
  rf-tuned-xl: R2 = 0.188 (std: 0.031)
  gb-tuned-l: R2 = 0.181 (std: 0.038)
  gb-tuned-xl: R2 = 0.181 (std: 0.038)
  xgb-xl: R2 = 0.113 (std: 0.049)
  xgb-l: R2 = 0.113 (std: 0.049)
  mlp-adaptive-xl: R2 = 0.183 (std: 0.036)
  mlp-l: R2 = 0.150 (std: 0.045)
  svr-rbf-xl: R2 = 0.250 (std: 0.040)
  svr-poly-l: R2 = 0.250 (std: 0.040)
  knn-tuned-sqrt: R2 = 0.090 (std: 0.029)
  knn-tuned-l: R2 = 0.090 (std: 0.029)
  ridge: R2 = 0.019 (std: 0.051)

Model-based training with 2 models
Best R2: 0.250, Mean R2: 0.154
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.3342, kl_div=0.0000
    Epoch 1: policy_loss=-0.0481, value_loss=0.9681, entropy=0.3347, kl_div=0.0045
  Round 1/3: Mean predicted reward = 9.952
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9673, entropy=0.3240, kl_div=0.0000
    Epoch 1: policy_loss=-0.0559, value_loss=0.9673, entropy=0.3262, kl_div=-0.0006
  Round 2/3: Mean predicted reward = 9.968
    Using performance-based weights
    Model weights: svr-rbf-xl:0.500 svr-poly-l:0.500 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.3311, kl_div=0.0000
    Epoch 1: policy_loss=-0.0409, value_loss=0.9691, entropy=0.3317, kl_div=-0.0705
  Round 3/3: Mean predicted reward = 10.301

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 80 Results ---
  Mean Oracle Reward: 10.300
  Min Oracle Reward: 6.027
  Max Oracle Reward: 11.726
  Std Oracle Reward: 1.086
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.154, Max: 0.250, Count: 13
  Total Sequences Evaluated: 2610

======================================================================
EXPERIMENT ROUND 81/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2610
  Performance plateaued, reducing LR to 0.000136

--- Round 81 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  TGGACAGATCCG
  TACGGCCAATGG
  GAGCGTAACTGC
  CGCGCGGCATAT
  GCTCGAATGCGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.350
  Max reward: 11.964
  With intrinsic bonuses: 10.348

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9674, entropy=0.3269, kl_div=0.0000
    Epoch 1: policy_loss=-0.0604, value_loss=0.9674, entropy=0.3253, kl_div=0.0054

=== Surrogate Model Training ===
Total samples: 2642

Training on 2511 samples (removed 131 outliers)
Reward range: [7.40, 12.86], mean: 10.16
  Created 13 candidate models for data size 2511
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.203 (std: 0.030)
  rf-tuned-xl: R2 = 0.203 (std: 0.029)
  gb-tuned-l: R2 = 0.172 (std: 0.035)
  gb-tuned-xl: R2 = 0.172 (std: 0.035)
  xgb-xl: R2 = 0.116 (std: 0.061)
  xgb-l: R2 = 0.116 (std: 0.061)
  mlp-adaptive-xl: R2 = 0.170 (std: 0.028)
  mlp-l: R2 = 0.167 (std: 0.041)
  svr-rbf-xl: R2 = 0.249 (std: 0.034)
  svr-poly-l: R2 = 0.249 (std: 0.034)
  knn-tuned-sqrt: R2 = 0.084 (std: 0.033)
  knn-tuned-l: R2 = 0.084 (std: 0.033)
  ridge: R2 = 0.012 (std: 0.050)

Model-based training with 4 models
Best R2: 0.249, Mean R2: 0.154
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.244 rf-tuned-xl:0.244 svr-rbf-xl:0.256 svr-poly-l:0.256 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.3616, kl_div=0.0000
    Epoch 1: policy_loss=-0.0404, value_loss=0.9679, entropy=0.3611, kl_div=-0.0344
  Round 1/3: Mean predicted reward = 9.822
    Using performance-based weights
    Model weights: rf-tuned-l:0.244 rf-tuned-xl:0.244 svr-rbf-xl:0.256 svr-poly-l:0.256 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.3164, kl_div=0.0000
    Epoch 1: policy_loss=-0.0666, value_loss=0.9693, entropy=0.3165, kl_div=-0.0870
  Round 2/3: Mean predicted reward = 9.848
    Using performance-based weights
    Model weights: rf-tuned-l:0.244 rf-tuned-xl:0.244 svr-rbf-xl:0.256 svr-poly-l:0.256 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.3339, kl_div=0.0000
    Epoch 1: policy_loss=-0.0281, value_loss=0.9694, entropy=0.3368, kl_div=-0.2285
  Round 3/3: Mean predicted reward = 10.174

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 81 Results ---
  Mean Oracle Reward: 10.329
  Min Oracle Reward: 6.249
  Max Oracle Reward: 12.163
  Std Oracle Reward: 1.019
  Sequence Diversity: 0.969
  Models Used: 4
  Model R2 - Mean: 0.154, Max: 0.249, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  AGGCTCGGCAAT
  ACGTGACTCGGA
  ATCCGATCGCGG
  GCTTCGAGCCGA
  CAGAGGTGCTCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.148
  Max reward: 11.816
  With intrinsic bonuses: 10.142

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.3351, kl_div=0.0000
    Epoch 1: policy_loss=-0.0103, value_loss=0.9683, entropy=0.3356, kl_div=-0.1174

=== Surrogate Model Training ===
Total samples: 2674

Training on 2541 samples (removed 133 outliers)
Reward range: [7.40, 12.84], mean: 10.16
  Created 13 candidate models for data size 2541
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.200 (std: 0.029)
  rf-tuned-xl: R2 = 0.202 (std: 0.034)
  gb-tuned-l: R2 = 0.183 (std: 0.034)
  gb-tuned-xl: R2 = 0.183 (std: 0.034)
  xgb-xl: R2 = 0.131 (std: 0.053)
  xgb-l: R2 = 0.131 (std: 0.053)
  mlp-adaptive-xl: R2 = 0.152 (std: 0.053)
  mlp-l: R2 = 0.187 (std: 0.033)
  svr-rbf-xl: R2 = 0.254 (std: 0.034)
  svr-poly-l: R2 = 0.254 (std: 0.034)
  knn-tuned-sqrt: R2 = 0.084 (std: 0.034)
  knn-tuned-l: R2 = 0.084 (std: 0.034)
  ridge: R2 = 0.013 (std: 0.049)

Model-based training with 3 models
Best R2: 0.254, Mean R2: 0.158
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-xl:0.322 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.3553, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0737
  Round 1/3: Mean predicted reward = 9.918
    Using performance-based weights
    Model weights: rf-tuned-xl:0.322 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.3286, kl_div=0.0000
    Epoch 1: policy_loss=-0.0461, value_loss=0.9680, entropy=0.3271, kl_div=0.0423
  Round 2/3: Mean predicted reward = 9.912
    Using performance-based weights
    Model weights: rf-tuned-xl:0.322 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.3567, kl_div=0.0000
    Epoch 1: policy_loss=-0.0346, value_loss=0.9697, entropy=0.3552, kl_div=-0.0881
  Round 3/3: Mean predicted reward = 10.044

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 82 Results ---
  Mean Oracle Reward: 10.141
  Min Oracle Reward: 5.133
  Max Oracle Reward: 11.764
  Std Oracle Reward: 1.242
  Sequence Diversity: 1.000
  Models Used: 3
  Model R2 - Mean: 0.158, Max: 0.254, Count: 13
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
  AGCGCCAGTGTA
  CGCGAGCATCTG
  GCTCCGACGGTA
  TACGGCACTGCG
  AGCGGCACCGTT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.145
  Max reward: 12.237
  With intrinsic bonuses: 10.151

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.3252, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1002

=== Surrogate Model Training ===
Total samples: 2706

Training on 2573 samples (removed 133 outliers)
Reward range: [7.40, 12.86], mean: 10.16
  Created 13 candidate models for data size 2573
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.205 (std: 0.027)
  rf-tuned-xl: R2 = 0.198 (std: 0.036)
  gb-tuned-l: R2 = 0.175 (std: 0.041)
  gb-tuned-xl: R2 = 0.175 (std: 0.041)
  xgb-xl: R2 = 0.137 (std: 0.053)
  xgb-l: R2 = 0.137 (std: 0.053)
  mlp-adaptive-xl: R2 = 0.174 (std: 0.032)
  mlp-l: R2 = 0.183 (std: 0.032)
  svr-rbf-xl: R2 = 0.252 (std: 0.031)
  svr-poly-l: R2 = 0.252 (std: 0.031)
  knn-tuned-sqrt: R2 = 0.087 (std: 0.032)
  knn-tuned-l: R2 = 0.087 (std: 0.032)
  ridge: R2 = 0.017 (std: 0.053)

Model-based training with 3 models
Best R2: 0.252, Mean R2: 0.160
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.323 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9677, entropy=0.3429, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1204
  Round 1/3: Mean predicted reward = 9.802
    Using performance-based weights
    Model weights: rf-tuned-l:0.323 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3599, kl_div=0.0000
    Epoch 1: policy_loss=0.0076, value_loss=0.9689, entropy=0.3597, kl_div=0.0113
  Round 2/3: Mean predicted reward = 10.013
    Using performance-based weights
    Model weights: rf-tuned-l:0.323 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.3586, kl_div=0.0000
    Epoch 1: policy_loss=-0.0464, value_loss=0.9685, entropy=0.3575, kl_div=-0.0100
  Round 3/3: Mean predicted reward = 10.120

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 83 Results ---
  Mean Oracle Reward: 10.093
  Min Oracle Reward: 6.517
  Max Oracle Reward: 12.119
  Std Oracle Reward: 1.338
  Sequence Diversity: 1.000
  Models Used: 3
  Model R2 - Mean: 0.160, Max: 0.252, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  GGGTCGATACCC
  ATGTGACGAGCC
  GCTCGGAACCGT
  GTCAGCCACTGG
  TCGCAGGCGACT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.106
  Max reward: 12.148
  With intrinsic bonuses: 10.148

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.3126, kl_div=0.0000
    Epoch 1: policy_loss=-0.0098, value_loss=0.9681, entropy=0.3121, kl_div=0.0130

=== Surrogate Model Training ===
Total samples: 2738

Training on 2604 samples (removed 134 outliers)
Reward range: [7.40, 12.86], mean: 10.16
  Created 13 candidate models for data size 2604
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.199 (std: 0.038)
  rf-tuned-xl: R2 = 0.208 (std: 0.035)
  gb-tuned-l: R2 = 0.178 (std: 0.040)
  gb-tuned-xl: R2 = 0.178 (std: 0.040)
  xgb-xl: R2 = 0.154 (std: 0.047)
  xgb-l: R2 = 0.154 (std: 0.047)
  mlp-adaptive-xl: R2 = 0.185 (std: 0.032)
  mlp-l: R2 = 0.168 (std: 0.034)
  svr-rbf-xl: R2 = 0.257 (std: 0.029)
  svr-poly-l: R2 = 0.257 (std: 0.029)
  knn-tuned-sqrt: R2 = 0.084 (std: 0.031)
  knn-tuned-l: R2 = 0.084 (std: 0.031)
  ridge: R2 = 0.014 (std: 0.052)

Model-based training with 3 models
Best R2: 0.257, Mean R2: 0.163
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-xl:0.323 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.3013, kl_div=0.0000
    Epoch 1: policy_loss=-0.0090, value_loss=0.9687, entropy=0.3012, kl_div=-0.0069
  Round 1/3: Mean predicted reward = 9.670
    Using performance-based weights
    Model weights: rf-tuned-xl:0.323 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.3394, kl_div=0.0000
    Epoch 1: policy_loss=-0.0057, value_loss=0.9684, entropy=0.3399, kl_div=-0.0203
  Round 2/3: Mean predicted reward = 9.879
    Using performance-based weights
    Model weights: rf-tuned-xl:0.323 svr-rbf-xl:0.339 svr-poly-l:0.339 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.3209, kl_div=0.0000
    Epoch 1: policy_loss=-0.0266, value_loss=0.9687, entropy=0.3221, kl_div=-0.0565
  Round 3/3: Mean predicted reward = 10.081

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 84 Results ---
  Mean Oracle Reward: 10.148
  Min Oracle Reward: 6.752
  Max Oracle Reward: 12.301
  Std Oracle Reward: 1.159
  Sequence Diversity: 1.000
  Models Used: 3
  Model R2 - Mean: 0.163, Max: 0.257, Count: 13
  Total Sequences Evaluated: 2738

======================================================================
EXPERIMENT ROUND 85/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2738
  Performance plateaued, reducing LR to 0.000150

--- Round 85 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCGCGCCATGGA
  TGGTACACCCGG
  TACCGGGACGTC
  TGGAGCCACTGC
  TCACCGTCGAGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.091
  Max reward: 11.582
  With intrinsic bonuses: 10.052

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9682, entropy=0.3112, kl_div=0.0000
    Epoch 1: policy_loss=0.0798, value_loss=0.9682, entropy=0.3173, kl_div=-0.3850

=== Surrogate Model Training ===
Total samples: 2770

Training on 2632 samples (removed 138 outliers)
Reward range: [7.43, 12.84], mean: 10.16
  Created 13 candidate models for data size 2632
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.209 (std: 0.034)
  rf-tuned-xl: R2 = 0.203 (std: 0.033)
  gb-tuned-l: R2 = 0.179 (std: 0.036)
  gb-tuned-xl: R2 = 0.179 (std: 0.036)
  xgb-xl: R2 = 0.160 (std: 0.023)
  xgb-l: R2 = 0.160 (std: 0.023)
  mlp-adaptive-xl: R2 = 0.170 (std: 0.026)
  mlp-l: R2 = 0.153 (std: 0.048)
  svr-rbf-xl: R2 = 0.265 (std: 0.039)
  svr-poly-l: R2 = 0.265 (std: 0.039)
  knn-tuned-sqrt: R2 = 0.087 (std: 0.028)
  knn-tuned-l: R2 = 0.087 (std: 0.028)
  ridge: R2 = 0.015 (std: 0.055)

Model-based training with 4 models
Best R2: 0.265, Mean R2: 0.164
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.243 rf-tuned-xl:0.242 svr-rbf-xl:0.257 svr-poly-l:0.257 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.3753, kl_div=0.0000
    Epoch 1: policy_loss=-0.0202, value_loss=0.9687, entropy=0.3798, kl_div=-0.2058
  Round 1/3: Mean predicted reward = 9.852
    Using performance-based weights
    Model weights: rf-tuned-l:0.243 rf-tuned-xl:0.242 svr-rbf-xl:0.257 svr-poly-l:0.257 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.3667, kl_div=0.0000
    Epoch 1: policy_loss=0.0088, value_loss=0.9680, entropy=0.3693, kl_div=-0.3000
  Round 2/3: Mean predicted reward = 9.921
    Using performance-based weights
    Model weights: rf-tuned-l:0.243 rf-tuned-xl:0.242 svr-rbf-xl:0.257 svr-poly-l:0.257 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.3217, kl_div=0.0000
    Epoch 1: policy_loss=-0.0235, value_loss=0.9688, entropy=0.3223, kl_div=0.0435
  Round 3/3: Mean predicted reward = 10.134

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 85 Results ---
  Mean Oracle Reward: 10.075
  Min Oracle Reward: 6.375
  Max Oracle Reward: 11.438
  Std Oracle Reward: 1.214
  Sequence Diversity: 1.000
  Models Used: 4
  Model R2 - Mean: 0.164, Max: 0.265, Count: 13
  Total Sequences Evaluated: 2770

======================================================================
EXPERIMENT ROUND 86/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2770
  Performance plateaued, reducing LR to 0.000136

--- Round 86 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ATGCGCCCGTAG
  CGATCGTGACGA
  GCGGCTACGCTA
  AGCACTCGTCGG
  CCCAGTGCGGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.342
  Max reward: 12.217
  With intrinsic bonuses: 10.351

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.3876, kl_div=0.0000
    Epoch 1: policy_loss=-0.0550, value_loss=0.9683, entropy=0.3876, kl_div=-0.0002

=== Surrogate Model Training ===
Total samples: 2802

Training on 2660 samples (removed 142 outliers)
Reward range: [7.44, 12.79], mean: 10.17
  Created 13 candidate models for data size 2660
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.207 (std: 0.050)
  rf-tuned-xl: R2 = 0.197 (std: 0.044)
  gb-tuned-l: R2 = 0.188 (std: 0.038)
  gb-tuned-xl: R2 = 0.188 (std: 0.038)
  xgb-xl: R2 = 0.173 (std: 0.043)
  xgb-l: R2 = 0.173 (std: 0.043)
  mlp-adaptive-xl: R2 = 0.203 (std: 0.042)
  mlp-l: R2 = 0.190 (std: 0.034)
  svr-rbf-xl: R2 = 0.268 (std: 0.038)
  svr-poly-l: R2 = 0.268 (std: 0.038)
  knn-tuned-sqrt: R2 = 0.096 (std: 0.042)
  knn-tuned-l: R2 = 0.096 (std: 0.042)
  ridge: R2 = 0.014 (std: 0.057)

Model-based training with 4 models
Best R2: 0.268, Mean R2: 0.174
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.243 mlp-adaptive-xl:0.242 svr-rbf-xl:0.258 svr-poly-l:0.258 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9682, entropy=0.3358, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2264
  Round 1/3: Mean predicted reward = 9.825
    Using performance-based weights
    Model weights: rf-tuned-l:0.243 mlp-adaptive-xl:0.242 svr-rbf-xl:0.258 svr-poly-l:0.258 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.3416, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2600
  Round 2/3: Mean predicted reward = 10.061
    Using performance-based weights
    Model weights: rf-tuned-l:0.243 mlp-adaptive-xl:0.242 svr-rbf-xl:0.258 svr-poly-l:0.258 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.3339, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3774
  Round 3/3: Mean predicted reward = 10.013

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 86 Results ---
  Mean Oracle Reward: 10.346
  Min Oracle Reward: 7.358
  Max Oracle Reward: 12.081
  Std Oracle Reward: 1.160
  Sequence Diversity: 1.000
  Models Used: 4
  Model R2 - Mean: 0.174, Max: 0.268, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  CGCTGCAGGTCA
  CGCGGGACCATT
  TCACCTGGGGCA
  CAGCTGCGGCTA
  CCCAGCTAGGTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.049
  Max reward: 11.622
  With intrinsic bonuses: 10.097

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.3320, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5232

=== Surrogate Model Training ===
Total samples: 2834

Training on 2689 samples (removed 145 outliers)
Reward range: [7.45, 12.79], mean: 10.17
  Created 13 candidate models for data size 2689
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.199 (std: 0.048)
  rf-tuned-xl: R2 = 0.204 (std: 0.051)
  gb-tuned-l: R2 = 0.187 (std: 0.043)
  gb-tuned-xl: R2 = 0.187 (std: 0.043)
  xgb-xl: R2 = 0.183 (std: 0.044)
  xgb-l: R2 = 0.183 (std: 0.044)
  mlp-adaptive-xl: R2 = 0.188 (std: 0.021)
  mlp-l: R2 = 0.181 (std: 0.043)
  svr-rbf-xl: R2 = 0.276 (std: 0.040)
  svr-poly-l: R2 = 0.276 (std: 0.040)
  knn-tuned-sqrt: R2 = 0.096 (std: 0.048)
  knn-tuned-l: R2 = 0.096 (std: 0.048)
  ridge: R2 = 0.017 (std: 0.056)

Model-based training with 3 models
Best R2: 0.276, Mean R2: 0.175
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-xl:0.317 svr-rbf-xl:0.341 svr-poly-l:0.341 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9685, entropy=0.3387, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4488
  Round 1/3: Mean predicted reward = 9.868
    Using performance-based weights
    Model weights: rf-tuned-xl:0.317 svr-rbf-xl:0.341 svr-poly-l:0.341 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.2977, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6771
  Round 2/3: Mean predicted reward = 10.035
    Using performance-based weights
    Model weights: rf-tuned-xl:0.317 svr-rbf-xl:0.341 svr-poly-l:0.341 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3529, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4258
  Round 3/3: Mean predicted reward = 10.075

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 87 Results ---
  Mean Oracle Reward: 10.103
  Min Oracle Reward: 6.409
  Max Oracle Reward: 11.984
  Std Oracle Reward: 1.002
  Sequence Diversity: 1.000
  Models Used: 3
  Model R2 - Mean: 0.175, Max: 0.276, Count: 13
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
  CGATCGCGAGTC
  CTTGACGGCGAC
  GTAGTGGACCCC
  CACATTGGCCGG
  ACGCGACGGCTT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.111
  Max reward: 12.342
  With intrinsic bonuses: 10.113

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.3377, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1431

=== Surrogate Model Training ===
Total samples: 2866

Training on 2719 samples (removed 147 outliers)
Reward range: [7.45, 12.79], mean: 10.17
  Created 13 candidate models for data size 2719
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.215 (std: 0.059)
  rf-tuned-xl: R2 = 0.227 (std: 0.056)
  gb-tuned-l: R2 = 0.182 (std: 0.048)
  gb-tuned-xl: R2 = 0.182 (std: 0.048)
  xgb-xl: R2 = 0.185 (std: 0.051)
  xgb-l: R2 = 0.185 (std: 0.051)
  mlp-adaptive-xl: R2 = 0.197 (std: 0.025)
  mlp-l: R2 = 0.202 (std: 0.035)
  svr-rbf-xl: R2 = 0.284 (std: 0.044)
  svr-poly-l: R2 = 0.284 (std: 0.044)
  knn-tuned-sqrt: R2 = 0.108 (std: 0.046)
  knn-tuned-l: R2 = 0.108 (std: 0.046)
  ridge: R2 = 0.020 (std: 0.058)

Model-based training with 5 models
Best R2: 0.284, Mean R2: 0.183
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.194 rf-tuned-xl:0.197 mlp-l:0.192 svr-rbf-xl:0.208 svr-poly-l:0.208 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.3066, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0906
  Round 1/3: Mean predicted reward = 9.772
    Using performance-based weights
    Model weights: rf-tuned-l:0.194 rf-tuned-xl:0.197 mlp-l:0.192 svr-rbf-xl:0.208 svr-poly-l:0.208 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.2628, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0731
  Round 2/3: Mean predicted reward = 9.734
    Using performance-based weights
    Model weights: rf-tuned-l:0.194 rf-tuned-xl:0.197 mlp-l:0.192 svr-rbf-xl:0.208 svr-poly-l:0.208 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.3193, kl_div=0.0000
    Epoch 1: policy_loss=-0.0337, value_loss=0.9693, entropy=0.3186, kl_div=0.0308
  Round 3/3: Mean predicted reward = 9.988

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 88 Results ---
  Mean Oracle Reward: 10.159
  Min Oracle Reward: 4.139
  Max Oracle Reward: 12.636
  Std Oracle Reward: 1.604
  Sequence Diversity: 1.000
  Models Used: 5
  Model R2 - Mean: 0.183, Max: 0.284, Count: 13
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
  CTCGGGTCAACG
  CGGAACTCGCGT
  AGCTAGCCGTAT
  AGGGAGTTCCAC
  GCTACGGACTCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.019
  Max reward: 11.946
  With intrinsic bonuses: 10.003

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9673, entropy=0.2746, kl_div=0.0000
    Epoch 1: policy_loss=-0.0074, value_loss=0.9673, entropy=0.2748, kl_div=-0.0158

=== Surrogate Model Training ===
Total samples: 2898

Training on 2752 samples (removed 146 outliers)
Reward range: [7.44, 12.84], mean: 10.18
  Created 13 candidate models for data size 2752
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.212 (std: 0.046)
  rf-tuned-xl: R2 = 0.205 (std: 0.043)
  gb-tuned-l: R2 = 0.189 (std: 0.047)
  gb-tuned-xl: R2 = 0.189 (std: 0.047)
  xgb-xl: R2 = 0.168 (std: 0.048)
  xgb-l: R2 = 0.168 (std: 0.048)
  mlp-adaptive-xl: R2 = 0.145 (std: 0.035)
  mlp-l: R2 = 0.137 (std: 0.037)
  svr-rbf-xl: R2 = 0.284 (std: 0.045)
  svr-poly-l: R2 = 0.284 (std: 0.045)
  knn-tuned-sqrt: R2 = 0.101 (std: 0.043)
  knn-tuned-l: R2 = 0.101 (std: 0.043)
  ridge: R2 = 0.020 (std: 0.056)

Model-based training with 4 models
Best R2: 0.284, Mean R2: 0.170
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.241 rf-tuned-xl:0.240 svr-rbf-xl:0.259 svr-poly-l:0.259 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.2978, kl_div=0.0000
    Epoch 1: policy_loss=-0.0261, value_loss=0.9693, entropy=0.2985, kl_div=-0.0653
  Round 1/3: Mean predicted reward = 9.986
    Using performance-based weights
    Model weights: rf-tuned-l:0.241 rf-tuned-xl:0.240 svr-rbf-xl:0.259 svr-poly-l:0.259 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.2992, kl_div=0.0000
    Epoch 1: policy_loss=-0.0324, value_loss=0.9686, entropy=0.2999, kl_div=-0.0806
  Round 2/3: Mean predicted reward = 9.945
    Using performance-based weights
    Model weights: rf-tuned-l:0.241 rf-tuned-xl:0.240 svr-rbf-xl:0.259 svr-poly-l:0.259 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.2973, kl_div=0.0000
    Epoch 1: policy_loss=-0.0052, value_loss=0.9688, entropy=0.2985, kl_div=-0.0868
  Round 3/3: Mean predicted reward = 10.023

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 89 Results ---
  Mean Oracle Reward: 9.978
  Min Oracle Reward: 5.395
  Max Oracle Reward: 12.120
  Std Oracle Reward: 1.594
  Sequence Diversity: 1.000
  Models Used: 4
  Model R2 - Mean: 0.170, Max: 0.284, Count: 13
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
  CGACGTGGTACC
  TCGTGGACACCG
  TTGAGCACCCGG
  AGCCGTCCTGAG
  CCCCAGGAGGTT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.029
  Max reward: 13.329
  With intrinsic bonuses: 9.966

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9681, entropy=0.2919, kl_div=0.0000
    Epoch 1: policy_loss=0.0246, value_loss=0.9681, entropy=0.2963, kl_div=-0.2705

=== Surrogate Model Training ===
Total samples: 2930

Training on 2777 samples (removed 153 outliers)
Reward range: [7.45, 12.84], mean: 10.18
  Created 13 candidate models for data size 2777
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.207 (std: 0.057)
  rf-tuned-xl: R2 = 0.202 (std: 0.056)
  gb-tuned-l: R2 = 0.192 (std: 0.049)
  gb-tuned-xl: R2 = 0.192 (std: 0.049)
  xgb-xl: R2 = 0.205 (std: 0.040)
  xgb-l: R2 = 0.205 (std: 0.040)
  mlp-adaptive-xl: R2 = 0.204 (std: 0.051)
  mlp-l: R2 = 0.207 (std: 0.041)
  svr-rbf-xl: R2 = 0.287 (std: 0.052)
  svr-poly-l: R2 = 0.287 (std: 0.052)
  knn-tuned-sqrt: R2 = 0.105 (std: 0.041)
  knn-tuned-l: R2 = 0.105 (std: 0.041)
  ridge: R2 = 0.023 (std: 0.055)

Model-based training with 8 models
Best R2: 0.287, Mean R2: 0.186
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.123 rf-tuned-xl:0.122 xgb-xl:0.122 xgb-l:0.122 mlp-adaptive-xl:0.122 mlp-l:0.123 svr-rbf-xl:0.133 svr-poly-l:0.133 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.3340, kl_div=0.0000
    Epoch 1: policy_loss=-0.0416, value_loss=0.9684, entropy=0.3382, kl_div=-0.2961
  Round 1/3: Mean predicted reward = 9.757
    Using performance-based weights
    Model weights: rf-tuned-l:0.123 rf-tuned-xl:0.122 xgb-xl:0.122 xgb-l:0.122 mlp-adaptive-xl:0.122 mlp-l:0.123 svr-rbf-xl:0.133 svr-poly-l:0.133 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.2964, kl_div=0.0000
    Epoch 1: policy_loss=-0.0180, value_loss=0.9692, entropy=0.2983, kl_div=-0.0837
  Round 2/3: Mean predicted reward = 9.913
    Using performance-based weights
    Model weights: rf-tuned-l:0.123 rf-tuned-xl:0.122 xgb-xl:0.122 xgb-l:0.122 mlp-adaptive-xl:0.122 mlp-l:0.123 svr-rbf-xl:0.133 svr-poly-l:0.133 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.2893, kl_div=0.0000
    Epoch 1: policy_loss=-0.0528, value_loss=0.9683, entropy=0.2901, kl_div=-0.0174
  Round 3/3: Mean predicted reward = 9.998

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 90 Results ---
  Mean Oracle Reward: 9.995
  Min Oracle Reward: 5.063
  Max Oracle Reward: 13.318
  Std Oracle Reward: 1.739
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: 0.186, Max: 0.287, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  GCGCTGAACTAG
  TACTGCCCAGGG
  CCGTCAGAGATG
  GGCTACGCGTAC
  TAGGCCGTGCCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.296
  Max reward: 13.038
  With intrinsic bonuses: 10.269

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9682, entropy=0.3298, kl_div=0.0000
    Epoch 1: policy_loss=-0.0646, value_loss=0.9682, entropy=0.3303, kl_div=-0.0330

=== Surrogate Model Training ===
Total samples: 2962

Training on 2808 samples (removed 154 outliers)
Reward range: [7.44, 12.84], mean: 10.18
  Created 13 candidate models for data size 2808
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.201 (std: 0.052)
  rf-tuned-xl: R2 = 0.204 (std: 0.059)
  gb-tuned-l: R2 = 0.195 (std: 0.045)
  gb-tuned-xl: R2 = 0.195 (std: 0.045)
  xgb-xl: R2 = 0.186 (std: 0.055)
  xgb-l: R2 = 0.186 (std: 0.055)
  mlp-adaptive-xl: R2 = 0.206 (std: 0.045)
  mlp-l: R2 = 0.206 (std: 0.040)
  svr-rbf-xl: R2 = 0.290 (std: 0.055)
  svr-poly-l: R2 = 0.290 (std: 0.055)
  knn-tuned-sqrt: R2 = 0.111 (std: 0.041)
  knn-tuned-l: R2 = 0.111 (std: 0.041)
  ridge: R2 = 0.022 (std: 0.058)

Model-based training with 6 models
Best R2: 0.290, Mean R2: 0.185
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.161 rf-tuned-xl:0.162 mlp-adaptive-xl:0.162 mlp-l:0.162 svr-rbf-xl:0.176 svr-poly-l:0.176 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.3244, kl_div=0.0000
    Epoch 1: policy_loss=-0.0423, value_loss=0.9690, entropy=0.3256, kl_div=-0.1895
  Round 1/3: Mean predicted reward = 9.720
    Using performance-based weights
    Model weights: rf-tuned-l:0.161 rf-tuned-xl:0.162 mlp-adaptive-xl:0.162 mlp-l:0.162 svr-rbf-xl:0.176 svr-poly-l:0.176 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.2855, kl_div=0.0000
    Epoch 1: policy_loss=-0.0145, value_loss=0.9686, entropy=0.2879, kl_div=-0.1468
  Round 2/3: Mean predicted reward = 9.945
    Using performance-based weights
    Model weights: rf-tuned-l:0.161 rf-tuned-xl:0.162 mlp-adaptive-xl:0.162 mlp-l:0.162 svr-rbf-xl:0.176 svr-poly-l:0.176 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.3082, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1384
  Round 3/3: Mean predicted reward = 10.037

  === Progress Analysis ===
  Status: NORMAL

--- Round 91 Results ---
  Mean Oracle Reward: 10.315
  Min Oracle Reward: 6.941
  Max Oracle Reward: 13.502
  Std Oracle Reward: 1.396
  Sequence Diversity: 1.000
  Models Used: 6
  Model R2 - Mean: 0.185, Max: 0.290, Count: 13
  Total Sequences Evaluated: 2962

======================================================================
EXPERIMENT ROUND 92/100
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2962
  Consistent improvement, increasing LR to 0.000240

--- Round 92 Configuration ---
Learning rate: 0.000240
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CACACCTTGGGG
  CCCTAGAGGATG
  AGTGGCCGCATC
  GGTACCGCGTAC
  CGTACTGGACCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.188
  Max reward: 12.707
  With intrinsic bonuses: 10.133

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.2890, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4923

=== Surrogate Model Training ===
Total samples: 2994

Training on 2841 samples (removed 153 outliers)
Reward range: [7.44, 12.84], mean: 10.18
  Created 13 candidate models for data size 2841
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.202 (std: 0.056)
  rf-tuned-xl: R2 = 0.209 (std: 0.052)
  gb-tuned-l: R2 = 0.201 (std: 0.053)
  gb-tuned-xl: R2 = 0.201 (std: 0.053)
  xgb-xl: R2 = 0.173 (std: 0.040)
  xgb-l: R2 = 0.173 (std: 0.040)
  mlp-adaptive-xl: R2 = 0.235 (std: 0.054)
  mlp-l: R2 = 0.196 (std: 0.050)
  svr-rbf-xl: R2 = 0.293 (std: 0.058)
  svr-poly-l: R2 = 0.293 (std: 0.058)
  knn-tuned-sqrt: R2 = 0.114 (std: 0.044)
  knn-tuned-l: R2 = 0.114 (std: 0.044)
  ridge: R2 = 0.022 (std: 0.063)

Model-based training with 7 models
Best R2: 0.293, Mean R2: 0.187
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.138 rf-tuned-xl:0.139 gb-tuned-l:0.138 gb-tuned-xl:0.138 mlp-adaptive-xl:0.143 svr-rbf-xl:0.152 svr-poly-l:0.152 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.2985, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2039
  Round 1/3: Mean predicted reward = 9.732
    Using performance-based weights
    Model weights: rf-tuned-l:0.138 rf-tuned-xl:0.139 gb-tuned-l:0.138 gb-tuned-xl:0.138 mlp-adaptive-xl:0.143 svr-rbf-xl:0.152 svr-poly-l:0.152 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.3150, kl_div=0.0000
    Epoch 1: policy_loss=-0.0473, value_loss=0.9686, entropy=0.3097, kl_div=-0.1480
  Round 2/3: Mean predicted reward = 9.915
    Using performance-based weights
    Model weights: rf-tuned-l:0.138 rf-tuned-xl:0.139 gb-tuned-l:0.138 gb-tuned-xl:0.138 mlp-adaptive-xl:0.143 svr-rbf-xl:0.152 svr-poly-l:0.152 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.3076, kl_div=0.0000
    Epoch 1: policy_loss=-0.0337, value_loss=0.9683, entropy=0.3097, kl_div=-0.1121
  Round 3/3: Mean predicted reward = 10.046

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 92 Results ---
  Mean Oracle Reward: 10.209
  Min Oracle Reward: 7.862
  Max Oracle Reward: 12.708
  Std Oracle Reward: 1.080
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: 0.187, Max: 0.293, Count: 13
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

--- Generated Sequences (Diversity: 1.000) ---
  TGACAGGGTCCC
  GGATAGACCTTC
  GTCAGTCGCCAG
  CAGCGGTGACCT
  GCGAGCTTGACA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.266
  Max reward: 12.321
  With intrinsic bonuses: 10.208

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9680, entropy=0.3160, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0567

=== Surrogate Model Training ===
Total samples: 3026

Training on 2870 samples (removed 156 outliers)
Reward range: [7.45, 12.84], mean: 10.18
  Created 13 candidate models for data size 2870
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.205 (std: 0.049)
  rf-tuned-xl: R2 = 0.219 (std: 0.052)
  gb-tuned-l: R2 = 0.204 (std: 0.057)
  gb-tuned-xl: R2 = 0.204 (std: 0.057)
  xgb-xl: R2 = 0.199 (std: 0.053)
  xgb-l: R2 = 0.199 (std: 0.053)
  mlp-adaptive-xl: R2 = 0.218 (std: 0.050)
  mlp-l: R2 = 0.208 (std: 0.040)
  svr-rbf-xl: R2 = 0.297 (std: 0.062)
  svr-poly-l: R2 = 0.297 (std: 0.062)
  knn-tuned-sqrt: R2 = 0.121 (std: 0.053)
  knn-tuned-l: R2 = 0.121 (std: 0.053)
  ridge: R2 = 0.023 (std: 0.068)

Model-based training with 8 models
Best R2: 0.297, Mean R2: 0.194
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.122 rf-tuned-xl:0.123 gb-tuned-l:0.122 gb-tuned-xl:0.122 mlp-adaptive-xl:0.123 mlp-l:0.122 svr-rbf-xl:0.133 svr-poly-l:0.133 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9673, entropy=0.2919, kl_div=0.0000
    Epoch 1: policy_loss=-0.0393, value_loss=0.9673, entropy=0.2960, kl_div=-0.0632
  Round 1/3: Mean predicted reward = 9.786
    Using performance-based weights
    Model weights: rf-tuned-l:0.122 rf-tuned-xl:0.123 gb-tuned-l:0.122 gb-tuned-xl:0.122 mlp-adaptive-xl:0.123 mlp-l:0.122 svr-rbf-xl:0.133 svr-poly-l:0.133 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.2942, kl_div=0.0000
    Epoch 1: policy_loss=0.0248, value_loss=0.9679, entropy=0.2973, kl_div=-0.1950
  Round 2/3: Mean predicted reward = 9.799
    Using performance-based weights
    Model weights: rf-tuned-l:0.122 rf-tuned-xl:0.123 gb-tuned-l:0.122 gb-tuned-xl:0.122 mlp-adaptive-xl:0.123 mlp-l:0.122 svr-rbf-xl:0.133 svr-poly-l:0.133 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.3319, kl_div=0.0000
    Epoch 1: policy_loss=-0.0427, value_loss=0.9686, entropy=0.3327, kl_div=0.0321
  Round 3/3: Mean predicted reward = 10.130

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 93 Results ---
  Mean Oracle Reward: 10.249
  Min Oracle Reward: 7.081
  Max Oracle Reward: 12.251
  Std Oracle Reward: 1.049
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: 0.194, Max: 0.297, Count: 13
  Total Sequences Evaluated: 3026

======================================================================
EXPERIMENT ROUND 94/100
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 3026
  Performance plateaued, reducing LR to 0.000019

--- Round 94 Configuration ---
Learning rate: 0.000019
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGCGATACCGGC
  GTGGACCCTCGA
  ACCTGCGGGATC
  TGCATGACGCGC
  CGCCTGGAGTCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.296
  Max reward: 12.499
  With intrinsic bonuses: 10.348

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3290, kl_div=0.0000
    Epoch 1: policy_loss=-0.0099, value_loss=0.9689, entropy=0.3293, kl_div=-0.0021

=== Surrogate Model Training ===
Total samples: 3058

Training on 2898 samples (removed 160 outliers)
Reward range: [7.46, 12.84], mean: 10.19
  Created 13 candidate models for data size 2898
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.215 (std: 0.053)
  rf-tuned-xl: R2 = 0.216 (std: 0.054)
  gb-tuned-l: R2 = 0.210 (std: 0.055)
  gb-tuned-xl: R2 = 0.210 (std: 0.055)
  xgb-xl: R2 = 0.196 (std: 0.062)
  xgb-l: R2 = 0.196 (std: 0.062)
  mlp-adaptive-xl: R2 = 0.224 (std: 0.053)
  mlp-l: R2 = 0.203 (std: 0.051)
  svr-rbf-xl: R2 = 0.299 (std: 0.061)
  svr-poly-l: R2 = 0.299 (std: 0.061)
  knn-tuned-sqrt: R2 = 0.117 (std: 0.055)
  knn-tuned-l: R2 = 0.117 (std: 0.055)
  ridge: R2 = 0.020 (std: 0.070)

Model-based training with 8 models
Best R2: 0.299, Mean R2: 0.194
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.122 rf-tuned-xl:0.123 gb-tuned-l:0.122 gb-tuned-xl:0.122 mlp-adaptive-xl:0.124 mlp-l:0.121 svr-rbf-xl:0.133 svr-poly-l:0.133 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.3352, kl_div=0.0000
    Epoch 1: policy_loss=-0.0163, value_loss=0.9683, entropy=0.3355, kl_div=0.0005
  Round 1/3: Mean predicted reward = 9.818
    Using performance-based weights
    Model weights: rf-tuned-l:0.122 rf-tuned-xl:0.123 gb-tuned-l:0.122 gb-tuned-xl:0.122 mlp-adaptive-xl:0.124 mlp-l:0.121 svr-rbf-xl:0.133 svr-poly-l:0.133 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.3285, kl_div=0.0000
    Epoch 1: policy_loss=-0.0109, value_loss=0.9681, entropy=0.3290, kl_div=-0.0205
  Round 2/3: Mean predicted reward = 10.071
    Using performance-based weights
    Model weights: rf-tuned-l:0.122 rf-tuned-xl:0.123 gb-tuned-l:0.122 gb-tuned-xl:0.122 mlp-adaptive-xl:0.124 mlp-l:0.121 svr-rbf-xl:0.133 svr-poly-l:0.133 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.3286, kl_div=0.0000
    Epoch 1: policy_loss=-0.0168, value_loss=0.9683, entropy=0.3287, kl_div=-0.0101
  Round 3/3: Mean predicted reward = 10.123

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 94 Results ---
  Mean Oracle Reward: 10.283
  Min Oracle Reward: 6.954
  Max Oracle Reward: 12.267
  Std Oracle Reward: 1.367
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: 0.194, Max: 0.299, Count: 13
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
  GACGGTCCGTCA
  CGAGCTGGCCTA
  CGGGCCGATATC
  CCCGGGAGTCAT
  GTATGCACGGAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.609
  Max reward: 12.678
  With intrinsic bonuses: 10.675

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=0.3465, kl_div=0.0000
    Epoch 1: policy_loss=0.0544, value_loss=0.9678, entropy=0.3417, kl_div=-0.0205

=== Surrogate Model Training ===
Total samples: 3090

Training on 2928 samples (removed 162 outliers)
Reward range: [7.47, 12.84], mean: 10.19
  Created 13 candidate models for data size 2928
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.212 (std: 0.048)
  rf-tuned-xl: R2 = 0.210 (std: 0.055)
  gb-tuned-l: R2 = 0.207 (std: 0.056)
  gb-tuned-xl: R2 = 0.207 (std: 0.056)
  xgb-xl: R2 = 0.191 (std: 0.045)
  xgb-l: R2 = 0.191 (std: 0.045)
  mlp-adaptive-xl: R2 = 0.210 (std: 0.036)
  mlp-l: R2 = 0.235 (std: 0.062)
  svr-rbf-xl: R2 = 0.295 (std: 0.057)
  svr-poly-l: R2 = 0.295 (std: 0.057)
  knn-tuned-sqrt: R2 = 0.115 (std: 0.053)
  knn-tuned-l: R2 = 0.115 (std: 0.053)
  ridge: R2 = 0.017 (std: 0.069)

Model-based training with 8 models
Best R2: 0.295, Mean R2: 0.192
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.122 rf-tuned-xl:0.122 gb-tuned-l:0.122 gb-tuned-xl:0.122 mlp-adaptive-xl:0.122 mlp-l:0.125 svr-rbf-xl:0.133 svr-poly-l:0.133 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.3167, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1425
  Round 1/3: Mean predicted reward = 9.767
    Using performance-based weights
    Model weights: rf-tuned-l:0.122 rf-tuned-xl:0.122 gb-tuned-l:0.122 gb-tuned-xl:0.122 mlp-adaptive-xl:0.122 mlp-l:0.125 svr-rbf-xl:0.133 svr-poly-l:0.133 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.3211, kl_div=0.0000
    Epoch 1: policy_loss=-0.0213, value_loss=0.9683, entropy=0.3215, kl_div=0.0151
  Round 2/3: Mean predicted reward = 9.797
    Using performance-based weights
    Model weights: rf-tuned-l:0.122 rf-tuned-xl:0.122 gb-tuned-l:0.122 gb-tuned-xl:0.122 mlp-adaptive-xl:0.122 mlp-l:0.125 svr-rbf-xl:0.133 svr-poly-l:0.133 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.2956, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2060
  Round 3/3: Mean predicted reward = 10.082

  === Progress Analysis ===
  Status: NORMAL

--- Round 95 Results ---
  Mean Oracle Reward: 10.572
  Min Oracle Reward: 7.552
  Max Oracle Reward: 12.563
  Std Oracle Reward: 1.063
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: 0.192, Max: 0.295, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 3090

======================================================================
EXPERIMENT ROUND 96/100
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 3090
  Consistent improvement, increasing LR to 0.000327

--- Round 96 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTCCATGGCACG
  CGACGCGGATCT
  GTGAGCCTGCAC
  CCTTAGGGCGCA
  ATGGGTGCCCAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.394
  Max reward: 12.583
  With intrinsic bonuses: 10.471

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.3409, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6927

=== Surrogate Model Training ===
Total samples: 3122

Training on 2960 samples (removed 162 outliers)
Reward range: [7.47, 12.86], mean: 10.20
  Created 13 candidate models for data size 2960
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.223 (std: 0.053)
  rf-tuned-xl: R2 = 0.211 (std: 0.055)
  gb-tuned-l: R2 = 0.210 (std: 0.051)
  gb-tuned-xl: R2 = 0.210 (std: 0.051)
  xgb-xl: R2 = 0.201 (std: 0.055)
  xgb-l: R2 = 0.201 (std: 0.055)
  mlp-adaptive-xl: R2 = 0.228 (std: 0.056)
  mlp-l: R2 = 0.209 (std: 0.067)
  svr-rbf-xl: R2 = 0.296 (std: 0.059)
  svr-poly-l: R2 = 0.296 (std: 0.059)
  knn-tuned-sqrt: R2 = 0.109 (std: 0.055)
  knn-tuned-l: R2 = 0.109 (std: 0.055)
  ridge: R2 = 0.017 (std: 0.067)

Model-based training with 10 models
Best R2: 0.296, Mean R2: 0.194
Running 3 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.099 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.097 xgb-l:0.097 mlp-adaptive-xl:0.100 mlp-l:0.098 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.3177, kl_div=0.0000
    Epoch 1: policy_loss=-0.0393, value_loss=0.9682, entropy=0.3177, kl_div=-0.0109
  Round 1/3: Mean predicted reward = 9.671
    Using performance-based weights
    Model weights: rf-tuned-l:0.099 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.097 xgb-l:0.097 mlp-adaptive-xl:0.100 mlp-l:0.098 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=0.3598, kl_div=0.0000
    Epoch 1: policy_loss=0.0346, value_loss=0.9686, entropy=0.3650, kl_div=-0.3270
  Round 2/3: Mean predicted reward = 10.096
    Using performance-based weights
    Model weights: rf-tuned-l:0.099 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.097 xgb-l:0.097 mlp-adaptive-xl:0.100 mlp-l:0.098 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.3306, kl_div=0.0000
    Epoch 1: policy_loss=-0.0439, value_loss=0.9682, entropy=0.3325, kl_div=0.0206
  Round 3/3: Mean predicted reward = 10.163

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 96 Results ---
  Mean Oracle Reward: 10.460
  Min Oracle Reward: 6.927
  Max Oracle Reward: 12.395
  Std Oracle Reward: 1.160
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.194, Max: 0.296, Count: 13
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

--- Generated Sequences (Diversity: 0.969) ---
  CGGACTCCGAGT
  CGAGCTGCTGAC
  ACGCTTGACCGG
  TCGGCCGAGTAA
  CTCCCGTGGAAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.296
  Max reward: 13.001
  With intrinsic bonuses: 10.296

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.3155, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1586

=== Surrogate Model Training ===
Total samples: 3154

Training on 2991 samples (removed 163 outliers)
Reward range: [7.46, 12.86], mean: 10.20
  Created 13 candidate models for data size 2991
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.222 (std: 0.055)
  rf-tuned-xl: R2 = 0.219 (std: 0.058)
  gb-tuned-l: R2 = 0.215 (std: 0.052)
  gb-tuned-xl: R2 = 0.215 (std: 0.052)
  xgb-xl: R2 = 0.219 (std: 0.063)
  xgb-l: R2 = 0.219 (std: 0.063)
  mlp-adaptive-xl: R2 = 0.235 (std: 0.040)
  mlp-l: R2 = 0.229 (std: 0.052)
  svr-rbf-xl: R2 = 0.303 (std: 0.060)
  svr-poly-l: R2 = 0.303 (std: 0.060)
  knn-tuned-sqrt: R2 = 0.117 (std: 0.056)
  knn-tuned-l: R2 = 0.117 (std: 0.056)
  ridge: R2 = 0.018 (std: 0.070)

Model-based training with 10 models
Best R2: 0.303, Mean R2: 0.203
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.100 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.3279, kl_div=0.0000
    Epoch 1: policy_loss=0.1182, value_loss=0.9695, entropy=0.3229, kl_div=-0.3075
  Round 1/5: Mean predicted reward = 9.745
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.100 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3001, kl_div=0.0000
    Epoch 1: policy_loss=0.0270, value_loss=0.9689, entropy=0.2986, kl_div=-0.1778
  Round 2/5: Mean predicted reward = 9.730
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.100 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.2995, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0718
  Round 3/5: Mean predicted reward = 9.901
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.100 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.2921, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0732
  Round 4/5: Mean predicted reward = 10.086
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.100 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.2713, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2024
  Round 5/5: Mean predicted reward = 10.160

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 97 Results ---
  Mean Oracle Reward: 10.348
  Min Oracle Reward: 7.084
  Max Oracle Reward: 13.367
  Std Oracle Reward: 1.439
  Sequence Diversity: 0.969
  Models Used: 10
  Model R2 - Mean: 0.203, Max: 0.303, Count: 13
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
  GATGCTCGCAAG
  GCGCCTTACAGG
  GGCTCAAGAGCT
  GCGCTAAGGTCC
  CCAGCCGATGGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.576
  Max reward: 12.259
  With intrinsic bonuses: 10.548

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.3338, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2466

=== Surrogate Model Training ===
Total samples: 3186

Training on 3026 samples (removed 160 outliers)
Reward range: [7.44, 12.90], mean: 10.20
  Created 13 candidate models for data size 3026
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.215 (std: 0.065)
  rf-tuned-xl: R2 = 0.219 (std: 0.058)
  gb-tuned-l: R2 = 0.216 (std: 0.052)
  gb-tuned-xl: R2 = 0.216 (std: 0.052)
  xgb-xl: R2 = 0.218 (std: 0.057)
  xgb-l: R2 = 0.218 (std: 0.057)
  mlp-adaptive-xl: R2 = 0.214 (std: 0.058)
  mlp-l: R2 = 0.233 (std: 0.073)
  svr-rbf-xl: R2 = 0.304 (std: 0.058)
  svr-poly-l: R2 = 0.304 (std: 0.058)
  knn-tuned-sqrt: R2 = 0.113 (std: 0.064)
  knn-tuned-l: R2 = 0.113 (std: 0.064)
  ridge: R2 = 0.016 (std: 0.076)

Model-based training with 10 models
Best R2: 0.304, Mean R2: 0.200
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.098 mlp-l:0.100 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9690, entropy=0.3024, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0665
  Round 1/5: Mean predicted reward = 9.836
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.098 mlp-l:0.100 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.2953, kl_div=0.0000
    Epoch 1: policy_loss=-0.0368, value_loss=0.9685, entropy=0.2952, kl_div=-0.0371
  Round 2/5: Mean predicted reward = 9.977
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.098 mlp-l:0.100 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.3098, kl_div=0.0000
    Epoch 1: policy_loss=-0.0523, value_loss=0.9686, entropy=0.3145, kl_div=0.0014
  Round 3/5: Mean predicted reward = 10.065
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.098 mlp-l:0.100 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.3298, kl_div=0.0000
    Epoch 1: policy_loss=-0.0056, value_loss=0.9685, entropy=0.3303, kl_div=0.0248
  Round 4/5: Mean predicted reward = 10.132
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.098 mlp-l:0.100 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.3175, kl_div=0.0000
    Epoch 1: policy_loss=-0.0347, value_loss=0.9683, entropy=0.3165, kl_div=0.0409
  Round 5/5: Mean predicted reward = 10.359

  === Progress Analysis ===
  Status: NORMAL

--- Round 98 Results ---
  Mean Oracle Reward: 10.585
  Min Oracle Reward: 6.511
  Max Oracle Reward: 12.521
  Std Oracle Reward: 1.275
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.200, Max: 0.304, Count: 13
  New best mean reward!
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
  GTGCTCACCAGG
  CGCGGCTACTGA
  GCTACCGCATGG
  TACCCGCGTGGA
  ATCGGCTGCAAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.615
  Max reward: 12.509
  With intrinsic bonuses: 10.570

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.2988, kl_div=0.0000
    Epoch 1: policy_loss=-0.0316, value_loss=0.9684, entropy=0.2981, kl_div=0.0320

=== Surrogate Model Training ===
Total samples: 3218

Training on 3059 samples (removed 159 outliers)
Reward range: [7.44, 12.90], mean: 10.21
  Created 13 candidate models for data size 3059
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.218 (std: 0.064)
  rf-tuned-xl: R2 = 0.213 (std: 0.057)
  gb-tuned-l: R2 = 0.222 (std: 0.053)
  gb-tuned-xl: R2 = 0.222 (std: 0.053)
  xgb-xl: R2 = 0.216 (std: 0.058)
  xgb-l: R2 = 0.216 (std: 0.058)
  mlp-adaptive-xl: R2 = 0.223 (std: 0.057)
  mlp-l: R2 = 0.229 (std: 0.049)
  svr-rbf-xl: R2 = 0.303 (std: 0.055)
  svr-poly-l: R2 = 0.303 (std: 0.055)
  knn-tuned-sqrt: R2 = 0.112 (std: 0.070)
  knn-tuned-l: R2 = 0.112 (std: 0.070)
  ridge: R2 = 0.013 (std: 0.077)

Model-based training with 10 models
Best R2: 0.303, Mean R2: 0.200
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.099 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.3392, kl_div=0.0000
    Epoch 1: policy_loss=-0.0046, value_loss=0.9685, entropy=0.3384, kl_div=0.0246
  Round 1/5: Mean predicted reward = 9.794
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.099 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.3258, kl_div=0.0000
    Epoch 1: policy_loss=-0.0260, value_loss=0.9693, entropy=0.3263, kl_div=-0.0726
  Round 2/5: Mean predicted reward = 9.723
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.099 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.3335, kl_div=0.0000
    Epoch 1: policy_loss=-0.0126, value_loss=0.9689, entropy=0.3334, kl_div=-0.0139
  Round 3/5: Mean predicted reward = 10.144
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.099 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9677, entropy=0.3137, kl_div=0.0000
    Epoch 1: policy_loss=-0.0116, value_loss=0.9677, entropy=0.3137, kl_div=-0.0062
  Round 4/5: Mean predicted reward = 10.117
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.099 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.2948, kl_div=0.0000
    Epoch 1: policy_loss=-0.0275, value_loss=0.9686, entropy=0.2947, kl_div=0.0307
  Round 5/5: Mean predicted reward = 10.196

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 99 Results ---
  Mean Oracle Reward: 10.606
  Min Oracle Reward: 7.601
  Max Oracle Reward: 12.391
  Std Oracle Reward: 1.299
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.200, Max: 0.303, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 3218

======================================================================
EXPERIMENT ROUND 100/100
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 3218
  Consistent improvement, increasing LR to 0.000360

--- Round 100 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GTCGAACGGACT
  GGCACTCACGTG
  CCACTCGGGGTA
  GACTGCGACCTG
  CGCAGATGGTCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 10.415
  Max reward: 12.541
  With intrinsic bonuses: 10.453

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9685, entropy=0.2860, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0701

=== Surrogate Model Training ===
Total samples: 3250

Training on 3090 samples (removed 160 outliers)
Reward range: [7.44, 12.90], mean: 10.21
  Created 13 candidate models for data size 3090
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.219 (std: 0.055)
  rf-tuned-xl: R2 = 0.215 (std: 0.058)
  gb-tuned-l: R2 = 0.221 (std: 0.059)
  gb-tuned-xl: R2 = 0.221 (std: 0.059)
  xgb-xl: R2 = 0.215 (std: 0.046)
  xgb-l: R2 = 0.215 (std: 0.046)
  mlp-adaptive-xl: R2 = 0.220 (std: 0.056)
  mlp-l: R2 = 0.229 (std: 0.058)
  svr-rbf-xl: R2 = 0.303 (std: 0.053)
  svr-poly-l: R2 = 0.303 (std: 0.053)
  knn-tuned-sqrt: R2 = 0.114 (std: 0.065)
  knn-tuned-l: R2 = 0.114 (std: 0.065)
  ridge: R2 = 0.009 (std: 0.076)

Model-based training with 10 models
Best R2: 0.303, Mean R2: 0.200
Running 5 virtual training rounds
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.098 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.2856, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4984
  Round 1/5: Mean predicted reward = 9.680
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.098 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.2961, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1161
  Round 2/5: Mean predicted reward = 9.792
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.098 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.2862, kl_div=0.0000
    Epoch 1: policy_loss=-0.0776, value_loss=0.9687, entropy=0.2878, kl_div=-0.2921
  Round 3/5: Mean predicted reward = 10.019
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.098 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.2999, kl_div=0.0000
    Epoch 1: policy_loss=-0.0479, value_loss=0.9681, entropy=0.3002, kl_div=-0.0738
  Round 4/5: Mean predicted reward = 10.183
    Using performance-based weights
    Model weights: rf-tuned-l:0.098 rf-tuned-xl:0.098 gb-tuned-l:0.098 gb-tuned-xl:0.098 xgb-xl:0.098 xgb-l:0.098 mlp-adaptive-xl:0.098 mlp-l:0.099 svr-rbf-xl:0.107 svr-poly-l:0.107 
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.2972, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3614
  Round 5/5: Mean predicted reward = 10.278

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 100 Results ---
  Mean Oracle Reward: 10.434
  Min Oracle Reward: 6.487
  Max Oracle Reward: 12.325
  Std Oracle Reward: 1.133
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: 0.200, Max: 0.303, Count: 13
  Total Sequences Evaluated: 3250

======================================================================
DyNA PPO ALGORITHM COMPLETE!
======================================================================
Total rounds executed: 100
Total sequences evaluated: 3250
Best mean reward: 10.606 (achieved at round 99)

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 100
Final Mean Reward: 10.4336
Best Mean Reward: 10.6058
Best Max Reward: 14.1138
Initial Lr: 0.0003
Final Lr: 0.0003
Total Updates: 557
Final Diversity: 1.0000
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
  CGCGCTGCTGCG: 11.121
  CGCGCTGCTGCG: 10.706
  CGCGCTGCTGCG: 10.873
  CGCGCTGCTGCG: 10.908
  CGCGCTGCTGCG: 10.808

Stochastic (Exploration):
  CGCGCAAGCGAC: 10.764
  CGCGCTTGCGCG: 10.487
  CGCGCTAGCGCA: 11.606
  CGGCCAGCAAGC: 12.004
  CGCGCATGCGCT: 11.632

Final Performance:
  Mean reward: 11.091
  Max reward: 12.004
  Std reward: 0.466

Best sequence found: CGGCCAGCAAGC
   Reward: 12.004

======================================================================
Training complete! Check 'learning_curves.png' and 'training_metrics.json'
======================================================================
