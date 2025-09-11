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
  Mean reward: 9.264
  Std reward: 3.356
  Min/Max: 0.000 / 13.767

Pre-training surrogate models on warm-up data...

Training on 47 samples (removed 3 outliers)
Reward range: [4.41, 13.77], mean: 9.86
  Created 8 candidate models for data size 47
Current R2 threshold: -0.3
  rf-xs: R2 = -0.289 (std: 0.627)
  rf-s: R2 = -0.304 (std: 0.575)
  knn-xs: R2 = -0.310 (std: 0.346)
  knn-s: R2 = -0.310 (std: 0.346)
  ridge: R2 = -0.297 (std: 0.505)
  gb-xs: R2 = -1.117 (std: 1.342)
  gp: R2 = -24.283 (std: 17.036)
  svr-rbf-s: R2 = -0.139 (std: 0.154)
Initial models trained: 3
Initial R2 scores - Mean: -3.381, Max: -0.139

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
  CGATTATGTAGTCAGC
  TTCTGCGGCCTAAACC
  CAAGTTCGCCGCTTCA
  ACCGTTCTACGCGAAG
  AAGTCCGTAGAAATCG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.003
  Max reward: 16.566
  With intrinsic bonuses: 11.016

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9886, entropy=1.3791, kl_div=0.0000
    Epoch 2: policy_loss=-0.1826, value_loss=0.9883, entropy=1.3794, kl_div=0.0372
    Epoch 4: policy_loss=-0.2061, value_loss=0.9881, entropy=1.3782, kl_div=0.0145
    Epoch 6: policy_loss=-0.2107, value_loss=0.9879, entropy=1.3795, kl_div=-0.0310

=== Surrogate Model Training ===
Total samples: 114

Training on 105 samples (removed 9 outliers)
Reward range: [5.13, 13.82], mean: 10.76
  Created 11 candidate models for data size 105
Current R2 threshold: -0.3
  rf-m: R2 = -0.100 (std: 0.226)
  rf-l: R2 = -0.100 (std: 0.289)
  gb-m: R2 = -0.525 (std: 0.533)
  gb-l: R2 = -0.512 (std: 0.511)
  xgb-m: R2 = -0.229 (std: 0.234)
  knn-m: R2 = -0.047 (std: 0.232)
  knn-tuned: R2 = -0.047 (std: 0.232)
  mlp-m: R2 = -1.628 (std: 0.947)
  svr-rbf: R2 = -0.004 (std: 0.151)
  svr-poly: R2 = -0.004 (std: 0.151)
  ridge: R2 = -0.068 (std: 0.120)

Model-based training with 8 models
Best R2: -0.004, Mean R2: -0.297
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9864, entropy=1.3784, kl_div=0.0000
  Round 1/2: Mean predicted reward = 11.090
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9848, entropy=1.3779, kl_div=0.0000
  Round 2/2: Mean predicted reward = 10.959

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 1 Results ---
  Mean Oracle Reward: 11.031
  Min Oracle Reward: 4.037
  Max Oracle Reward: 16.593
  Std Oracle Reward: 2.022
  Sequence Diversity: 1.000
  Models Used: 8
  Model R2 - Mean: -0.297, Max: -0.004, Count: 11
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
  TCTTTGTTGACTTCCG
  ATGAACTGCGATCAGA
  CTTGCGCTGAGTTAGC
  GATGTATCGACAGCTC
  AGCACGCAATCCGCCC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.808
  Max reward: 17.529
  With intrinsic bonuses: 11.800

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9865, entropy=1.3782, kl_div=0.0000
    Epoch 2: policy_loss=-0.1057, value_loss=0.9865, entropy=1.3752, kl_div=0.0262
    Early stopping at epoch 4: KL divergence = 0.0550

=== Surrogate Model Training ===
Total samples: 178

Training on 165 samples (removed 13 outliers)
Reward range: [6.74, 14.62], mean: 11.20
  Created 11 candidate models for data size 165
Current R2 threshold: -0.3
  rf-m: R2 = -0.119 (std: 0.242)
  rf-l: R2 = -0.100 (std: 0.225)
  gb-m: R2 = -0.277 (std: 0.245)
  gb-l: R2 = -0.285 (std: 0.241)
  xgb-m: R2 = -0.254 (std: 0.218)
  knn-m: R2 = -0.114 (std: 0.198)
  knn-tuned: R2 = -0.114 (std: 0.198)
  mlp-m: R2 = -1.444 (std: 0.782)
  svr-rbf: R2 = -0.097 (std: 0.188)
  svr-poly: R2 = -0.097 (std: 0.188)
  ridge: R2 = -0.182 (std: 0.133)

Model-based training with 10 models
Best R2: -0.097, Mean R2: -0.280
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9894, entropy=1.3701, kl_div=0.0000
  Round 1/2: Mean predicted reward = 11.373
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9860, entropy=1.3677, kl_div=0.0000
  Round 2/2: Mean predicted reward = 11.489

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 2 Results ---
  Mean Oracle Reward: 11.774
  Min Oracle Reward: 6.550
  Max Oracle Reward: 17.271
  Std Oracle Reward: 1.809
  Sequence Diversity: 1.000
  Models Used: 10
  Model R2 - Mean: -0.280, Max: -0.097, Count: 11
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
  CTCAGCCCCTTCGACG
  TTATGCTTGAAGTTGT
  TACACCCGACAGGTAA
  CTAGTAGCCGGGGCAC
  CGCACCGTGCAAGCGT
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.758
  Max reward: 14.282
  With intrinsic bonuses: 11.937

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=0.0000, value_loss=0.9833, entropy=1.3646, kl_div=0.0000
    Epoch 2: policy_loss=-0.0720, value_loss=0.9833, entropy=1.3583, kl_div=0.0177
    Epoch 4: policy_loss=-0.1014, value_loss=0.9833, entropy=1.3513, kl_div=0.0483
    Early stopping at epoch 5: KL divergence = 0.0621

=== Surrogate Model Training ===
Total samples: 242

Training on 224 samples (removed 18 outliers)
Reward range: [7.18, 14.62], mean: 11.45
  Created 11 candidate models for data size 224
Current R2 threshold: -0.3
  rf-m: R2 = -0.240 (std: 0.255)
  rf-l: R2 = -0.238 (std: 0.194)
  gb-m: R2 = -0.424 (std: 0.310)
  gb-l: R2 = -0.436 (std: 0.305)
  xgb-m: R2 = -0.480 (std: 0.329)
  knn-m: R2 = -0.200 (std: 0.251)
  knn-tuned: R2 = -0.200 (std: 0.251)
  mlp-m: R2 = -2.109 (std: 1.991)
  svr-rbf: R2 = -0.138 (std: 0.113)
  svr-poly: R2 = -0.138 (std: 0.113)
  ridge: R2 = -0.166 (std: 0.122)

Model-based training with 7 models
Best R2: -0.138, Mean R2: -0.433
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9903, entropy=1.3502, kl_div=0.0000
  Round 1/2: Mean predicted reward = 11.689
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9863, entropy=1.3481, kl_div=0.0000
  Round 2/2: Mean predicted reward = 11.721

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 3 Results ---
  Mean Oracle Reward: 11.748
  Min Oracle Reward: 6.692
  Max Oracle Reward: 14.417
  Std Oracle Reward: 1.456
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: -0.433, Max: -0.138, Count: 11
  Total Sequences Evaluated: 242

======================================================================
EXPERIMENT ROUND 4/40
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.280
Total data collected: 242

--- Round 4 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0100
Exploration rate: 0.280

--- Generated Sequences (Diversity: 1.000) ---
  GGCGCACCTCAGTATG
  CCAGCGTGGGTACTAA
  TAGCGACGACTCGTGC
  AAACATGTCTCGCTGG
  CCTCAGCCGGAGTTGA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.064
  Max reward: 15.999
  With intrinsic bonuses: 12.179

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9869, entropy=1.3448, kl_div=0.0000
    Epoch 1: policy_loss=-0.0086, value_loss=0.9869, entropy=1.3440, kl_div=0.0089
    Epoch 2: policy_loss=-0.0188, value_loss=0.9869, entropy=1.3430, kl_div=0.0193
    Epoch 3: policy_loss=-0.0303, value_loss=0.9869, entropy=1.3420, kl_div=0.0311

=== Surrogate Model Training ===
Total samples: 306

Training on 282 samples (removed 24 outliers)
Reward range: [7.65, 15.26], mean: 11.66
  Created 11 candidate models for data size 282
Current R2 threshold: -0.3
  rf-m: R2 = -0.166 (std: 0.125)
  rf-l: R2 = -0.176 (std: 0.128)
  gb-m: R2 = -0.252 (std: 0.133)
  gb-l: R2 = -0.253 (std: 0.130)
  xgb-m: R2 = -0.339 (std: 0.153)
  knn-m: R2 = -0.175 (std: 0.093)
  knn-tuned: R2 = -0.175 (std: 0.093)
  mlp-m: R2 = -0.784 (std: 0.382)
  svr-rbf: R2 = -0.092 (std: 0.090)
  svr-poly: R2 = -0.092 (std: 0.090)
  ridge: R2 = -0.085 (std: 0.083)

Model-based training with 9 models
Best R2: -0.085, Mean R2: -0.235
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9831, entropy=1.3428, kl_div=0.0000
  Round 1/2: Mean predicted reward = 11.952
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9862, entropy=1.3425, kl_div=0.0000
  Round 2/2: Mean predicted reward = 11.860

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 4 Results ---
  Mean Oracle Reward: 12.065
  Min Oracle Reward: 9.166
  Max Oracle Reward: 15.788
  Std Oracle Reward: 1.292
  Sequence Diversity: 1.000
  Models Used: 9
  Model R2 - Mean: -0.235, Max: -0.085, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 306

======================================================================
EXPERIMENT ROUND 5/40
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.250
Total data collected: 306

--- Round 5 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0100
Exploration rate: 0.250

--- Generated Sequences (Diversity: 1.000) ---
  CAGAGCATCGGTGCTA
  ACAGCACGCGTGTGTA
  ACGACCGGGTGCTTAA
  CACATGGGATGCATGC
  TGATCACAGGGTGCCA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.058
  Max reward: 15.649
  With intrinsic bonuses: 12.207

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9805, entropy=1.3390, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0962

=== Surrogate Model Training ===
Total samples: 370

Training on 341 samples (removed 29 outliers)
Reward range: [8.14, 15.26], mean: 11.77
  Created 14 candidate models for data size 341
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.114 (std: 0.077)
  rf-tuned-xl: R2 = -0.111 (std: 0.084)
  gb-tuned-l: R2 = -0.162 (std: 0.115)
  gb-tuned-xl: R2 = -0.164 (std: 0.117)
  xgb-xl: R2 = -0.391 (std: 0.144)
  xgb-l: R2 = -0.391 (std: 0.144)
  mlp-adaptive-xl: R2 = -0.796 (std: 0.336)
  mlp-l: R2 = -0.588 (std: 0.201)
  svr-rbf-xl: R2 = -0.049 (std: 0.090)
  svr-poly-l: R2 = -0.049 (std: 0.090)
  knn-tuned-sqrt: R2 = -0.218 (std: 0.090)
  knn-tuned-l: R2 = -0.218 (std: 0.090)
  ridge: R2 = -0.042 (std: 0.077)
  gp: R2 = -83.988 (std: 12.238)

Model-based training with 9 models
Best R2: -0.042, Mean R2: -6.234
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9842, entropy=1.3311, kl_div=0.0000
  Round 1/2: Mean predicted reward = 12.002
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9877, entropy=1.3183, kl_div=0.0000
  Round 2/2: Mean predicted reward = 12.059

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 5 Results ---
  Mean Oracle Reward: 12.084
  Min Oracle Reward: 8.355
  Max Oracle Reward: 15.355
  Std Oracle Reward: 1.226
  Sequence Diversity: 1.000
  Models Used: 9
  Model R2 - Mean: -6.234, Max: -0.042, Count: 14
  New best mean reward!
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
  CGCCATGATATGGCCG
  GAAATCTGCGGCCATG
  CTGTTAGCGCCGCGAA
  CACGTGCGAAGCTCGT
  ACCATCAGGGGCGTCT
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.872
  Max reward: 14.520
  With intrinsic bonuses: 11.981

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9902, entropy=1.3012, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1540

=== Surrogate Model Training ===
Total samples: 434

Training on 401 samples (removed 33 outliers)
Reward range: [8.21, 15.26], mean: 11.83
  Created 14 candidate models for data size 401
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.070 (std: 0.054)
  rf-tuned-xl: R2 = -0.105 (std: 0.087)
  gb-tuned-l: R2 = -0.096 (std: 0.083)
  gb-tuned-xl: R2 = -0.096 (std: 0.083)
  xgb-xl: R2 = -0.242 (std: 0.130)
  xgb-l: R2 = -0.242 (std: 0.130)
  mlp-adaptive-xl: R2 = -0.551 (std: 0.286)
  mlp-l: R2 = -0.435 (std: 0.274)
  svr-rbf-xl: R2 = -0.021 (std: 0.075)
  svr-poly-l: R2 = -0.021 (std: 0.075)
  knn-tuned-sqrt: R2 = -0.171 (std: 0.076)
  knn-tuned-l: R2 = -0.171 (std: 0.076)
  ridge: R2 = -0.033 (std: 0.067)
  gp: R2 = -87.349 (std: 13.360)

Model-based training with 11 models
Best R2: -0.021, Mean R2: -6.400
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9890, entropy=1.2880, kl_div=0.0000
  Round 1/2: Mean predicted reward = 12.200
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9846, entropy=1.2732, kl_div=0.0000
  Round 2/2: Mean predicted reward = 12.261

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 6 Results ---
  Mean Oracle Reward: 11.826
  Min Oracle Reward: 5.352
  Max Oracle Reward: 14.349
  Std Oracle Reward: 1.717
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: -6.400, Max: -0.021, Count: 14
  Total Sequences Evaluated: 434

======================================================================
EXPERIMENT ROUND 7/40
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.190
Total data collected: 434
  Performance plateaued, reducing LR to 0.000100

--- Round 7 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0100
Exploration rate: 0.190

--- Generated Sequences (Diversity: 1.000) ---
  ACGTGTCCGCGAGGAC
  CGTAAACGGGCTTCCG
  TAGAGTCCGCGATCCG
  ATGCCACGGAGCGTTA
  GGATATACCCGTGCTA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.991
  Max reward: 14.175
  With intrinsic bonuses: 12.068

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9846, entropy=1.2492, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0780

=== Surrogate Model Training ===
Total samples: 498

Training on 462 samples (removed 36 outliers)
Reward range: [8.47, 14.62], mean: 11.86
  Created 14 candidate models for data size 462
Current R2 threshold: -0.3
  rf-tuned-l: R2 = -0.083 (std: 0.106)
  rf-tuned-xl: R2 = -0.079 (std: 0.142)
  gb-tuned-l: R2 = -0.069 (std: 0.147)
  gb-tuned-xl: R2 = -0.068 (std: 0.144)
  xgb-xl: R2 = -0.338 (std: 0.205)
  xgb-l: R2 = -0.338 (std: 0.205)
  mlp-adaptive-xl: R2 = -0.519 (std: 0.401)
  mlp-l: R2 = -0.506 (std: 0.145)
  svr-rbf-xl: R2 = 0.014 (std: 0.099)
  svr-poly-l: R2 = 0.014 (std: 0.099)
  knn-tuned-sqrt: R2 = -0.181 (std: 0.136)
  knn-tuned-l: R2 = -0.181 (std: 0.136)
  ridge: R2 = -0.023 (std: 0.076)
  gp: R2 = -94.102 (std: 14.595)

Model-based training with 9 models
Best R2: 0.014, Mean R2: -6.890
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9884, entropy=1.2435, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0882
  Round 1/3: Mean predicted reward = 11.965
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9866, entropy=1.2331, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0827
  Round 2/3: Mean predicted reward = 11.976
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9830, entropy=1.2262, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1184
  Round 3/3: Mean predicted reward = 11.863

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 7 Results ---
  Mean Oracle Reward: 11.992
  Min Oracle Reward: 8.421
  Max Oracle Reward: 14.357
  Std Oracle Reward: 1.190
  Sequence Diversity: 1.000
  Models Used: 9
  Model R2 - Mean: -6.890, Max: 0.014, Count: 14
  Total Sequences Evaluated: 498

======================================================================
EXPERIMENT ROUND 8/40
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.080
Total data collected: 498
  Performance plateaued, reducing LR to 0.000055

--- Round 8 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.080

--- Generated Sequences (Diversity: 1.000) ---
  GTAACGTTCGGAGCCA
  ACGTCGAAGACCTTGG
  CGGCGGCAATATTGCA
  GACCGTAAGCCGTGCG
  GGGCTTGTCAAACCAG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.845
  Max reward: 14.078
  With intrinsic bonuses: 11.871

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9840, entropy=1.2153, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0653

=== Surrogate Model Training ===
Total samples: 562

Training on 526 samples (removed 36 outliers)
Reward range: [8.47, 14.62], mean: 11.86
  Created 13 candidate models for data size 526
Current R2 threshold: -0.3
  rf-tuned-l: R2 = 0.023 (std: 0.135)
  rf-tuned-xl: R2 = 0.037 (std: 0.139)
  gb-tuned-l: R2 = 0.016 (std: 0.160)
  gb-tuned-xl: R2 = 0.015 (std: 0.163)
  xgb-xl: R2 = -0.180 (std: 0.230)
  xgb-l: R2 = -0.180 (std: 0.230)
  mlp-adaptive-xl: R2 = -0.331 (std: 0.293)
  mlp-l: R2 = -0.259 (std: 0.273)
  svr-rbf-xl: R2 = 0.075 (std: 0.094)
  svr-poly-l: R2 = 0.075 (std: 0.094)
  knn-tuned-sqrt: R2 = -0.096 (std: 0.136)
  knn-tuned-l: R2 = -0.096 (std: 0.136)
  ridge: R2 = 0.026 (std: 0.067)

Model-based training with 12 models
Best R2: 0.075, Mean R2: -0.067
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9830, entropy=1.2101, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0683
  Round 1/3: Mean predicted reward = 11.896
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9895, entropy=1.2015, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0727
  Round 2/3: Mean predicted reward = 11.889
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9830, entropy=1.1965, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0813
  Round 3/3: Mean predicted reward = 11.909

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 8 Results ---
  Mean Oracle Reward: 11.830
  Min Oracle Reward: 8.886
  Max Oracle Reward: 14.300
  Std Oracle Reward: 1.206
  Sequence Diversity: 1.000
  Models Used: 12
  Model R2 - Mean: -0.067, Max: 0.075, Count: 13
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
  GTGGAACTGCCGCCTA
  GTACGACTGCATGACG
  CGGCATCAGTGGAACT
  ATGGCGCAGCCTCGAT
  TGTGCGGCCACAAGGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.166
  Max reward: 15.553
  With intrinsic bonuses: 12.213

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9852, entropy=1.1918, kl_div=0.0000
    Epoch 1: policy_loss=-0.0092, value_loss=0.9852, entropy=1.1894, kl_div=0.0268

=== Surrogate Model Training ===
Total samples: 626

Training on 590 samples (removed 36 outliers)
Reward range: [8.44, 15.26], mean: 11.89
  Created 13 candidate models for data size 590
Current R2 threshold: -0.3
  rf-tuned-l: R2 = 0.068 (std: 0.084)
  rf-tuned-xl: R2 = 0.051 (std: 0.086)
  gb-tuned-l: R2 = 0.078 (std: 0.103)
  gb-tuned-xl: R2 = 0.078 (std: 0.103)
  xgb-xl: R2 = -0.103 (std: 0.133)
  xgb-l: R2 = -0.103 (std: 0.133)
  mlp-adaptive-xl: R2 = -0.147 (std: 0.071)
  mlp-l: R2 = -0.158 (std: 0.082)
  svr-rbf-xl: R2 = 0.097 (std: 0.073)
  svr-poly-l: R2 = 0.097 (std: 0.073)
  knn-tuned-sqrt: R2 = -0.027 (std: 0.120)
  knn-tuned-l: R2 = -0.027 (std: 0.120)
  ridge: R2 = 0.041 (std: 0.052)

Model-based training with 13 models
Best R2: 0.097, Mean R2: -0.004
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9805, entropy=1.1853, kl_div=0.0000
    Epoch 1: policy_loss=-0.0112, value_loss=0.9805, entropy=1.1828, kl_div=0.0304
  Round 1/3: Mean predicted reward = 12.024
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9852, entropy=1.1836, kl_div=0.0000
    Epoch 1: policy_loss=-0.0149, value_loss=0.9852, entropy=1.1810, kl_div=0.0315
  Round 2/3: Mean predicted reward = 11.976
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9825, entropy=1.1770, kl_div=0.0000
    Epoch 1: policy_loss=-0.0190, value_loss=0.9825, entropy=1.1743, kl_div=0.0311
  Round 3/3: Mean predicted reward = 11.920

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 9 Results ---
  Mean Oracle Reward: 12.189
  Min Oracle Reward: 8.696
  Max Oracle Reward: 15.455
  Std Oracle Reward: 1.373
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.004, Max: 0.097, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 626

======================================================================
EXPERIMENT ROUND 10/40
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 626

--- Round 10 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCCAGCTGAGGATGCC
  GCGGCGTACGTATACC
  GAACCGGCTTCATGTA
  CATAGGTCCACTGGGA
  TCCACTGCGGCATGGA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.087
  Max reward: 15.027
  With intrinsic bonuses: 12.064

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9855, entropy=1.1740, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6312

=== Surrogate Model Training ===
Total samples: 690

Training on 652 samples (removed 38 outliers)
Reward range: [8.44, 15.26], mean: 11.92
  Created 13 candidate models for data size 652
Current R2 threshold: -0.3
  rf-tuned-l: R2 = 0.052 (std: 0.065)
  rf-tuned-xl: R2 = 0.084 (std: 0.056)
  gb-tuned-l: R2 = 0.109 (std: 0.069)
  gb-tuned-xl: R2 = 0.109 (std: 0.069)
  xgb-xl: R2 = -0.143 (std: 0.092)
  xgb-l: R2 = -0.143 (std: 0.092)
  mlp-adaptive-xl: R2 = -0.165 (std: 0.197)
  mlp-l: R2 = -0.159 (std: 0.191)
  svr-rbf-xl: R2 = 0.085 (std: 0.063)
  svr-poly-l: R2 = 0.085 (std: 0.063)
  knn-tuned-sqrt: R2 = -0.005 (std: 0.075)
  knn-tuned-l: R2 = -0.005 (std: 0.075)
  ridge: R2 = 0.025 (std: 0.057)

Model-based training with 13 models
Best R2: 0.109, Mean R2: -0.006
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9823, entropy=1.1253, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8233
  Round 1/3: Mean predicted reward = 11.907
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9805, entropy=1.0766, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7962
  Round 2/3: Mean predicted reward = 12.084
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9788, entropy=1.0249, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1182
  Round 3/3: Mean predicted reward = 12.014

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 10 Results ---
  Mean Oracle Reward: 12.083
  Min Oracle Reward: 7.710
  Max Oracle Reward: 15.012
  Std Oracle Reward: 1.474
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.006, Max: 0.109, Count: 13
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
  AAGGTCTGATGAGCCC
  AGACCGGTTGCGGCCA
  ATCACGCTAGCCGGTG
  CCTGTACGGCAAGATG
  CTAGGCGTCGATAAGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.240
  Max reward: 15.902
  With intrinsic bonuses: 12.277

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9848, entropy=0.9723, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0425

=== Surrogate Model Training ===
Total samples: 754

Training on 706 samples (removed 48 outliers)
Reward range: [8.65, 15.14], mean: 11.98
  Created 13 candidate models for data size 706
Current R2 threshold: -0.27999999999999997
  rf-tuned-l: R2 = 0.058 (std: 0.055)
  rf-tuned-xl: R2 = 0.054 (std: 0.062)
  gb-tuned-l: R2 = 0.107 (std: 0.062)
  gb-tuned-xl: R2 = 0.106 (std: 0.062)
  xgb-xl: R2 = -0.196 (std: 0.145)
  xgb-l: R2 = -0.196 (std: 0.145)
  mlp-adaptive-xl: R2 = -0.199 (std: 0.130)
  mlp-l: R2 = -0.180 (std: 0.157)
  svr-rbf-xl: R2 = 0.082 (std: 0.041)
  svr-poly-l: R2 = 0.082 (std: 0.041)
  knn-tuned-sqrt: R2 = -0.061 (std: 0.081)
  knn-tuned-l: R2 = -0.061 (std: 0.081)
  ridge: R2 = 0.019 (std: 0.046)

Model-based training with 13 models
Best R2: 0.107, Mean R2: -0.030
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9834, entropy=0.9247, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.2378
  Round 1/3: Mean predicted reward = 11.988
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9813, entropy=0.8807, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1657
  Round 2/3: Mean predicted reward = 12.105
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9819, entropy=0.8369, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.4406
  Round 3/3: Mean predicted reward = 12.111

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 11 Results ---
  Mean Oracle Reward: 12.272
  Min Oracle Reward: 7.721
  Max Oracle Reward: 16.025
  Std Oracle Reward: 1.385
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.030, Max: 0.107, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 754

======================================================================
EXPERIMENT ROUND 12/40
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 754
  Performance plateaued, reducing LR to 0.000100

--- Round 12 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ACTATCGGAGCGTCCG
  GAGCTAGGCGCCCATG
  AGTCCCACGATGGCGG
  TGGACACCGTGGCGAC
  GTGACCTGCAGGGACC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.427
  Max reward: 16.380
  With intrinsic bonuses: 12.400

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9788, entropy=0.8000, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5361

=== Surrogate Model Training ===
Total samples: 818

Training on 765 samples (removed 53 outliers)
Reward range: [8.73, 15.14], mean: 12.01
  Created 13 candidate models for data size 765
Current R2 threshold: -0.26
  rf-tuned-l: R2 = 0.056 (std: 0.071)
  rf-tuned-xl: R2 = 0.047 (std: 0.054)
  gb-tuned-l: R2 = 0.087 (std: 0.048)
  gb-tuned-xl: R2 = 0.087 (std: 0.048)
  xgb-xl: R2 = -0.204 (std: 0.113)
  xgb-l: R2 = -0.204 (std: 0.113)
  mlp-adaptive-xl: R2 = -0.160 (std: 0.152)
  mlp-l: R2 = -0.202 (std: 0.081)
  svr-rbf-xl: R2 = 0.088 (std: 0.060)
  svr-poly-l: R2 = 0.088 (std: 0.060)
  knn-tuned-sqrt: R2 = -0.042 (std: 0.086)
  knn-tuned-l: R2 = -0.042 (std: 0.086)
  ridge: R2 = 0.025 (std: 0.041)

Model-based training with 13 models
Best R2: 0.088, Mean R2: -0.029
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9795, entropy=0.7846, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5778
  Round 1/3: Mean predicted reward = 12.223
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9821, entropy=0.7708, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6127
  Round 2/3: Mean predicted reward = 12.096
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9797, entropy=0.7611, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5976
  Round 3/3: Mean predicted reward = 12.168

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 12 Results ---
  Mean Oracle Reward: 12.416
  Min Oracle Reward: 8.319
  Max Oracle Reward: 16.146
  Std Oracle Reward: 1.505
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: -0.029, Max: 0.088, Count: 13
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
  GTCCCAGAGGCATCGG
  ACGCCTGGCCAAGGTG
  ATGCCACGCTACGGGG
  CCTACGTCCGAGAGGG
  AGGCGTTGCTCACACG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.695
  Max reward: 15.353
  With intrinsic bonuses: 11.731

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9816, entropy=0.7446, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8967

=== Surrogate Model Training ===
Total samples: 882

Training on 827 samples (removed 55 outliers)
Reward range: [8.65, 15.15], mean: 12.01
  Created 13 candidate models for data size 827
Current R2 threshold: -0.24
  rf-tuned-l: R2 = 0.102 (std: 0.057)
  rf-tuned-xl: R2 = 0.111 (std: 0.073)
  gb-tuned-l: R2 = 0.123 (std: 0.071)
  gb-tuned-xl: R2 = 0.123 (std: 0.071)
  xgb-xl: R2 = -0.109 (std: 0.107)
  xgb-l: R2 = -0.109 (std: 0.107)
  mlp-adaptive-xl: R2 = -0.126 (std: 0.042)
  mlp-l: R2 = -0.047 (std: 0.038)
  svr-rbf-xl: R2 = 0.127 (std: 0.078)
  svr-poly-l: R2 = 0.127 (std: 0.078)
  knn-tuned-sqrt: R2 = 0.004 (std: 0.079)
  knn-tuned-l: R2 = 0.004 (std: 0.079)
  ridge: R2 = 0.050 (std: 0.066)

Model-based training with 13 models
Best R2: 0.127, Mean R2: 0.029
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9831, entropy=0.7333, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8440
  Round 1/3: Mean predicted reward = 12.222
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9805, entropy=0.7149, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9026
  Round 2/3: Mean predicted reward = 12.181
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9820, entropy=0.7048, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9730
  Round 3/3: Mean predicted reward = 12.218

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 13 Results ---
  Mean Oracle Reward: 11.706
  Min Oracle Reward: 5.231
  Max Oracle Reward: 15.351
  Std Oracle Reward: 1.934
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.029, Max: 0.127, Count: 13
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
  ATCAATACCTTGGGAG
  TGCGCGGCCTGCTAAA
  CCCCTGGAGGCGATAG
  TCGACCCTAGGGAGTC
  CGCATGGGGGTACCAC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.838
  Max reward: 15.658
  With intrinsic bonuses: 11.776

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9826, entropy=0.6856, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2922

=== Surrogate Model Training ===
Total samples: 946

Training on 886 samples (removed 60 outliers)
Reward range: [8.65, 15.17], mean: 12.01
  Created 13 candidate models for data size 886
Current R2 threshold: -0.21999999999999997
  rf-tuned-l: R2 = 0.081 (std: 0.077)
  rf-tuned-xl: R2 = 0.092 (std: 0.070)
  gb-tuned-l: R2 = 0.128 (std: 0.084)
  gb-tuned-xl: R2 = 0.128 (std: 0.084)
  xgb-xl: R2 = -0.094 (std: 0.107)
  xgb-l: R2 = -0.094 (std: 0.107)
  mlp-adaptive-xl: R2 = -0.066 (std: 0.081)
  mlp-l: R2 = -0.065 (std: 0.135)
  svr-rbf-xl: R2 = 0.140 (std: 0.052)
  svr-poly-l: R2 = 0.140 (std: 0.052)
  knn-tuned-sqrt: R2 = -0.019 (std: 0.084)
  knn-tuned-l: R2 = -0.019 (std: 0.084)
  ridge: R2 = 0.048 (std: 0.066)

Model-based training with 13 models
Best R2: 0.140, Mean R2: 0.031
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9815, entropy=0.6834, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2945
  Round 1/3: Mean predicted reward = 12.127
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9803, entropy=0.6846, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2794
  Round 2/3: Mean predicted reward = 12.118
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9772, entropy=0.6817, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2740
  Round 3/3: Mean predicted reward = 12.147

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 14 Results ---
  Mean Oracle Reward: 11.817
  Min Oracle Reward: 3.459
  Max Oracle Reward: 15.601
  Std Oracle Reward: 2.104
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.031, Max: 0.140, Count: 13
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
  CCGAATGGATTACGCG
  CCACGAGGGCGGTTCA
  ACAGCGAGAGTCTTGC
  CGCACAGCATAGTTGG
  CTCGGACGGATAGGCC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.121
  Max reward: 14.990
  With intrinsic bonuses: 12.132

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9868, entropy=0.6789, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.2059

=== Surrogate Model Training ===
Total samples: 1010

Training on 950 samples (removed 60 outliers)
Reward range: [8.65, 15.26], mean: 12.03
  Created 13 candidate models for data size 950
Current R2 threshold: -0.19999999999999998
  rf-tuned-l: R2 = 0.089 (std: 0.081)
  rf-tuned-xl: R2 = 0.082 (std: 0.081)
  gb-tuned-l: R2 = 0.092 (std: 0.092)
  gb-tuned-xl: R2 = 0.092 (std: 0.092)
  xgb-xl: R2 = -0.074 (std: 0.064)
  xgb-l: R2 = -0.074 (std: 0.064)
  mlp-adaptive-xl: R2 = -0.099 (std: 0.100)
  mlp-l: R2 = -0.106 (std: 0.097)
  svr-rbf-xl: R2 = 0.125 (std: 0.044)
  svr-poly-l: R2 = 0.125 (std: 0.044)
  knn-tuned-sqrt: R2 = -0.032 (std: 0.078)
  knn-tuned-l: R2 = -0.032 (std: 0.078)
  ridge: R2 = 0.029 (std: 0.064)

Model-based training with 13 models
Best R2: 0.125, Mean R2: 0.017
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9833, entropy=0.6520, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.1989
  Round 1/3: Mean predicted reward = 12.098
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9781, entropy=0.6374, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.6956
  Round 2/3: Mean predicted reward = 12.051
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9792, entropy=0.6178, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.8855
  Round 3/3: Mean predicted reward = 12.138

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 15 Results ---
  Mean Oracle Reward: 12.138
  Min Oracle Reward: 8.495
  Max Oracle Reward: 14.619
  Std Oracle Reward: 1.329
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.017, Max: 0.125, Count: 13
  Total Sequences Evaluated: 1010

======================================================================
EXPERIMENT ROUND 16/40
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1010
  Consistent improvement, increasing LR to 0.000327

--- Round 16 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCGAAGCTATCGTGTA
  GCCACGAGGTGCACTG
  CCGCGCAAGGATCTGT
  TTACAAGCAGTTGGCC
  GCTTGCAGGACTGACA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.568
  Max reward: 16.170
  With intrinsic bonuses: 12.558

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9799, entropy=0.5940, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.9839

=== Surrogate Model Training ===
Total samples: 1074

Training on 1007 samples (removed 67 outliers)
Reward range: [8.65, 15.26], mean: 12.05
  Created 13 candidate models for data size 1007
Current R2 threshold: -0.18
  rf-tuned-l: R2 = 0.077 (std: 0.054)
  rf-tuned-xl: R2 = 0.092 (std: 0.048)
  gb-tuned-l: R2 = 0.122 (std: 0.036)
  gb-tuned-xl: R2 = 0.122 (std: 0.036)
  xgb-xl: R2 = -0.113 (std: 0.025)
  xgb-l: R2 = -0.113 (std: 0.025)
  mlp-adaptive-xl: R2 = -0.006 (std: 0.067)
  mlp-l: R2 = -0.071 (std: 0.051)
  svr-rbf-xl: R2 = 0.128 (std: 0.035)
  svr-poly-l: R2 = 0.128 (std: 0.035)
  knn-tuned-sqrt: R2 = -0.037 (std: 0.069)
  knn-tuned-l: R2 = -0.037 (std: 0.069)
  ridge: R2 = 0.041 (std: 0.045)

Model-based training with 13 models
Best R2: 0.128, Mean R2: 0.026
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9814, entropy=0.5777, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 3.2159
  Round 1/3: Mean predicted reward = 12.154
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9773, entropy=0.5583, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 3.3787
  Round 2/3: Mean predicted reward = 12.143
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9754, entropy=0.5269, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 3.8679
  Round 3/3: Mean predicted reward = 12.140

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 16 Results ---
  Mean Oracle Reward: 12.562
  Min Oracle Reward: 7.204
  Max Oracle Reward: 16.075
  Std Oracle Reward: 1.751
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.026, Max: 0.128, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 1074

======================================================================
EXPERIMENT ROUND 17/40
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1074
  Consistent improvement, increasing LR to 0.000240

--- Round 17 Configuration ---
Learning rate: 0.000240
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ACGGGCACCGGAGTCT
  AGGCTTCGCCGAGGCA
  CGATCACGCGCGAGTG
  AGAAGCTCCCTGGGGC
  GCCGATACTGCTCGAG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.928
  Max reward: 14.650
  With intrinsic bonuses: 11.925

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9886, entropy=0.5008, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.9066

=== Surrogate Model Training ===
Total samples: 1138

Training on 1071 samples (removed 67 outliers)
Reward range: [8.59, 15.38], mean: 12.07
  Created 13 candidate models for data size 1071
Current R2 threshold: -0.15999999999999998
  rf-tuned-l: R2 = 0.109 (std: 0.087)
  rf-tuned-xl: R2 = 0.106 (std: 0.076)
  gb-tuned-l: R2 = 0.128 (std: 0.058)
  gb-tuned-xl: R2 = 0.128 (std: 0.058)
  xgb-xl: R2 = -0.079 (std: 0.107)
  xgb-l: R2 = -0.079 (std: 0.107)
  mlp-adaptive-xl: R2 = -0.043 (std: 0.123)
  mlp-l: R2 = -0.042 (std: 0.103)
  svr-rbf-xl: R2 = 0.138 (std: 0.069)
  svr-poly-l: R2 = 0.138 (std: 0.069)
  knn-tuned-sqrt: R2 = -0.009 (std: 0.076)
  knn-tuned-l: R2 = -0.009 (std: 0.076)
  ridge: R2 = 0.041 (std: 0.051)

Model-based training with 13 models
Best R2: 0.138, Mean R2: 0.040
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9762, entropy=0.4842, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 3.0160
  Round 1/3: Mean predicted reward = 12.073
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9811, entropy=0.4629, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.9448
  Round 2/3: Mean predicted reward = 12.190
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9779, entropy=0.4496, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 2.5031
  Round 3/3: Mean predicted reward = 12.062

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 17 Results ---
  Mean Oracle Reward: 11.920
  Min Oracle Reward: 0.000
  Max Oracle Reward: 14.825
  Std Oracle Reward: 2.331
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.040, Max: 0.138, Count: 13
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
  CTGGGCATCGACGGAC
  CACGTCGCAGTAGGGC
  AGGCGCAATCGCTGCG
  GGATCGACTGCCGGAC
  GAGCGGCCGATTCCAG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.700
  Max reward: 15.074
  With intrinsic bonuses: 11.704

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9932, entropy=0.4264, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8776

=== Surrogate Model Training ===
Total samples: 1202

Training on 1129 samples (removed 73 outliers)
Reward range: [8.59, 15.38], mean: 12.08
  Created 13 candidate models for data size 1129
Current R2 threshold: -0.13999999999999999
  rf-tuned-l: R2 = 0.127 (std: 0.068)
  rf-tuned-xl: R2 = 0.134 (std: 0.070)
  gb-tuned-l: R2 = 0.138 (std: 0.046)
  gb-tuned-xl: R2 = 0.138 (std: 0.046)
  xgb-xl: R2 = -0.048 (std: 0.119)
  xgb-l: R2 = -0.048 (std: 0.119)
  mlp-adaptive-xl: R2 = 0.016 (std: 0.074)
  mlp-l: R2 = -0.033 (std: 0.078)
  svr-rbf-xl: R2 = 0.155 (std: 0.059)
  svr-poly-l: R2 = 0.155 (std: 0.059)
  knn-tuned-sqrt: R2 = 0.005 (std: 0.067)
  knn-tuned-l: R2 = 0.005 (std: 0.067)
  ridge: R2 = 0.046 (std: 0.043)

Model-based training with 13 models
Best R2: 0.155, Mean R2: 0.061
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9753, entropy=0.4203, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8804
  Round 1/3: Mean predicted reward = 12.175
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9738, entropy=0.4064, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.0098
  Round 2/3: Mean predicted reward = 12.156
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9798, entropy=0.4155, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9603
  Round 3/3: Mean predicted reward = 12.264

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 18 Results ---
  Mean Oracle Reward: 11.699
  Min Oracle Reward: 0.000
  Max Oracle Reward: 15.056
  Std Oracle Reward: 2.435
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.061, Max: 0.155, Count: 13
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
  GCCGCGAGGTCTAACG
  AGTCCGAACGTGCCGT
  GCGCAACCTGGACTGG
  CACTCTGGGAGGCGAC
  CGGAAGTGCAGCCCTG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.262
  Max reward: 16.265
  With intrinsic bonuses: 11.238

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9920, entropy=0.3792, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2505

=== Surrogate Model Training ===
Total samples: 1266

Training on 1186 samples (removed 80 outliers)
Reward range: [8.54, 15.38], mean: 12.07
  Created 13 candidate models for data size 1186
Current R2 threshold: -0.12
  rf-tuned-l: R2 = 0.139 (std: 0.052)
  rf-tuned-xl: R2 = 0.145 (std: 0.054)
  gb-tuned-l: R2 = 0.151 (std: 0.021)
  gb-tuned-xl: R2 = 0.151 (std: 0.021)
  xgb-xl: R2 = -0.048 (std: 0.085)
  xgb-l: R2 = -0.048 (std: 0.085)
  mlp-adaptive-xl: R2 = 0.007 (std: 0.082)
  mlp-l: R2 = 0.034 (std: 0.039)
  svr-rbf-xl: R2 = 0.153 (std: 0.024)
  svr-poly-l: R2 = 0.153 (std: 0.024)
  knn-tuned-sqrt: R2 = -0.003 (std: 0.053)
  knn-tuned-l: R2 = -0.003 (std: 0.053)
  ridge: R2 = 0.041 (std: 0.024)

Model-based training with 13 models
Best R2: 0.153, Mean R2: 0.067
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9818, entropy=0.3908, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2676
  Round 1/3: Mean predicted reward = 12.088
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9757, entropy=0.3876, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3047
  Round 2/3: Mean predicted reward = 12.005
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9826, entropy=0.3797, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3193
  Round 3/3: Mean predicted reward = 12.138

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 19 Results ---
  Mean Oracle Reward: 11.267
  Min Oracle Reward: 2.552
  Max Oracle Reward: 16.207
  Std Oracle Reward: 2.795
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.067, Max: 0.153, Count: 13
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
  GTACCGCGAGCATGCG
  GGATGCATCGCCGCGA
  TCGCCGGTAACCGGGA
  TGCCAGCCTCAGGTAG
  AATTACGGCGCGGGCC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.392
  Max reward: 15.695
  With intrinsic bonuses: 11.380

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9962, entropy=0.3751, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.7543

=== Surrogate Model Training ===
Total samples: 1330

Training on 1245 samples (removed 85 outliers)
Reward range: [8.47, 15.38], mean: 12.06
  Created 13 candidate models for data size 1245
Current R2 threshold: -0.09999999999999998
  rf-tuned-l: R2 = 0.155 (std: 0.044)
  rf-tuned-xl: R2 = 0.164 (std: 0.046)
  gb-tuned-l: R2 = 0.170 (std: 0.030)
  gb-tuned-xl: R2 = 0.170 (std: 0.030)
  xgb-xl: R2 = 0.017 (std: 0.039)
  xgb-l: R2 = 0.017 (std: 0.039)
  mlp-adaptive-xl: R2 = 0.048 (std: 0.055)
  mlp-l: R2 = 0.021 (std: 0.064)
  svr-rbf-xl: R2 = 0.171 (std: 0.021)
  svr-poly-l: R2 = 0.171 (std: 0.021)
  knn-tuned-sqrt: R2 = 0.022 (std: 0.057)
  knn-tuned-l: R2 = 0.022 (std: 0.057)
  ridge: R2 = 0.041 (std: 0.023)

Model-based training with 13 models
Best R2: 0.171, Mean R2: 0.092
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9900, entropy=0.3791, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1128
  Round 1/3: Mean predicted reward = 11.866
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9843, entropy=0.3636, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1310
  Round 2/3: Mean predicted reward = 11.944
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9821, entropy=0.3858, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.2485
  Round 3/3: Mean predicted reward = 12.131

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 20 Results ---
  Mean Oracle Reward: 11.387
  Min Oracle Reward: 4.865
  Max Oracle Reward: 15.690
  Std Oracle Reward: 2.195
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.092, Max: 0.171, Count: 13
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
  AAAGGTCCTCGCGGTC
  CCGTGTGACGAGCACG
  GTGCAGGGCGCACCAT
  TCTGACGGAGGACGCC
  AGTAATCCGAGCTTCG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.958
  Max reward: 15.190
  With intrinsic bonuses: 11.964

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9884, entropy=0.3667, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6954

=== Surrogate Model Training ===
Total samples: 1394

Training on 1307 samples (removed 87 outliers)
Reward range: [8.47, 15.38], mean: 12.06
  Created 13 candidate models for data size 1307
Current R2 threshold: -0.07999999999999999
  rf-tuned-l: R2 = 0.112 (std: 0.054)
  rf-tuned-xl: R2 = 0.117 (std: 0.044)
  gb-tuned-l: R2 = 0.136 (std: 0.037)
  gb-tuned-xl: R2 = 0.136 (std: 0.037)
  xgb-xl: R2 = -0.066 (std: 0.056)
  xgb-l: R2 = -0.066 (std: 0.056)
  mlp-adaptive-xl: R2 = 0.038 (std: 0.063)
  mlp-l: R2 = 0.040 (std: 0.038)
  svr-rbf-xl: R2 = 0.158 (std: 0.016)
  svr-poly-l: R2 = 0.158 (std: 0.016)
  knn-tuned-sqrt: R2 = 0.003 (std: 0.051)
  knn-tuned-l: R2 = 0.003 (std: 0.051)
  ridge: R2 = 0.030 (std: 0.035)

Model-based training with 13 models
Best R2: 0.158, Mean R2: 0.061
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9877, entropy=0.3877, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2711
  Round 1/3: Mean predicted reward = 12.035
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9886, entropy=0.3884, kl_div=0.0000
    Epoch 1: policy_loss=0.0566, value_loss=0.9886, entropy=0.4122, kl_div=-0.0313
  Round 2/3: Mean predicted reward = 11.898
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9864, entropy=0.4354, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3621
  Round 3/3: Mean predicted reward = 12.081

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 21 Results ---
  Mean Oracle Reward: 11.970
  Min Oracle Reward: 6.338
  Max Oracle Reward: 15.460
  Std Oracle Reward: 1.707
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.061, Max: 0.158, Count: 13
  Total Sequences Evaluated: 1394

======================================================================
EXPERIMENT ROUND 22/40
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1394
  Consistent improvement, increasing LR to 0.000240

--- Round 22 Configuration ---
Learning rate: 0.000240
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCAGCGGTGCAGTCAT
  ATCGCCTGCGGGAGAC
  CTTGCGCGGACACATG
  CAGAGTGGGCCCTTAC
  CCCAATCGGGGCATGG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.402
  Max reward: 16.446
  With intrinsic bonuses: 12.386

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9830, entropy=0.4490, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0687

=== Surrogate Model Training ===
Total samples: 1458

Training on 1368 samples (removed 90 outliers)
Reward range: [8.47, 15.56], mean: 12.08
  Created 13 candidate models for data size 1368
Current R2 threshold: -0.06
  rf-tuned-l: R2 = 0.121 (std: 0.061)
  rf-tuned-xl: R2 = 0.122 (std: 0.064)
  gb-tuned-l: R2 = 0.148 (std: 0.043)
  gb-tuned-xl: R2 = 0.148 (std: 0.043)
  xgb-xl: R2 = -0.050 (std: 0.068)
  xgb-l: R2 = -0.050 (std: 0.068)
  mlp-adaptive-xl: R2 = 0.059 (std: 0.047)
  mlp-l: R2 = 0.079 (std: 0.068)
  svr-rbf-xl: R2 = 0.165 (std: 0.026)
  svr-poly-l: R2 = 0.165 (std: 0.026)
  knn-tuned-sqrt: R2 = -0.000 (std: 0.063)
  knn-tuned-l: R2 = -0.000 (std: 0.063)
  ridge: R2 = 0.038 (std: 0.031)

Model-based training with 13 models
Best R2: 0.165, Mean R2: 0.073
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9835, entropy=0.4705, kl_div=0.0000
    Epoch 1: policy_loss=0.0667, value_loss=0.9835, entropy=0.4874, kl_div=-0.0179
  Round 1/3: Mean predicted reward = 12.062
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9802, entropy=0.4756, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2092
  Round 2/3: Mean predicted reward = 12.078
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9805, entropy=0.4637, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3020
  Round 3/3: Mean predicted reward = 12.120

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 22 Results ---
  Mean Oracle Reward: 12.321
  Min Oracle Reward: 0.000
  Max Oracle Reward: 16.168
  Std Oracle Reward: 2.177
  Sequence Diversity: 1.000
  Models Used: 13
  Model R2 - Mean: 0.073, Max: 0.165, Count: 13
  Total Sequences Evaluated: 1458

======================================================================
EXPERIMENT ROUND 23/40
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1458
  Consistent improvement, increasing LR to 0.000132

--- Round 23 Configuration ---
Learning rate: 0.000132
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ACAGCTGCGTGCATCG
  TGGGGGCAATGACCCC
  GCCCAGTGGGCTGAAC
  GCCCAGCGTACGAGGT
  GCTGCGCAGAGTACTC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.494
  Max reward: 15.883
  With intrinsic bonuses: 12.480

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9829, entropy=0.4734, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2543

=== Surrogate Model Training ===
Total samples: 1522

Training on 1426 samples (removed 96 outliers)
Reward range: [8.50, 15.56], mean: 12.10
  Created 13 candidate models for data size 1426
Current R2 threshold: -0.03999999999999998
  rf-tuned-l: R2 = 0.115 (std: 0.072)
  rf-tuned-xl: R2 = 0.110 (std: 0.073)
  gb-tuned-l: R2 = 0.154 (std: 0.036)
  gb-tuned-xl: R2 = 0.154 (std: 0.036)
  xgb-xl: R2 = -0.048 (std: 0.097)
  xgb-l: R2 = -0.048 (std: 0.097)
  mlp-adaptive-xl: R2 = 0.076 (std: 0.058)
  mlp-l: R2 = 0.010 (std: 0.065)
  svr-rbf-xl: R2 = 0.162 (std: 0.032)
  svr-poly-l: R2 = 0.162 (std: 0.032)
  knn-tuned-sqrt: R2 = -0.000 (std: 0.066)
  knn-tuned-l: R2 = -0.000 (std: 0.066)
  ridge: R2 = 0.045 (std: 0.029)

Model-based training with 11 models
Best R2: 0.162, Mean R2: 0.068
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9858, entropy=0.4497, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1285
  Round 1/3: Mean predicted reward = 11.995
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9815, entropy=0.4539, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1531
  Round 2/3: Mean predicted reward = 12.099
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9812, entropy=0.4617, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2204
  Round 3/3: Mean predicted reward = 12.152

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 23 Results ---
  Mean Oracle Reward: 12.518
  Min Oracle Reward: 5.214
  Max Oracle Reward: 15.927
  Std Oracle Reward: 1.968
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: 0.068, Max: 0.162, Count: 13
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
  CATAACGCGGCGCGGT
  CCGGGTGAGAGCTCCA
  AGGGAGCTCCGCTAGC
  CGTCGAACGTCGGGCA
  ACTATGCCGTAGCGCG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.650
  Max reward: 16.976
  With intrinsic bonuses: 12.631

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9808, entropy=0.4546, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0895

=== Surrogate Model Training ===
Total samples: 1586

Training on 1489 samples (removed 97 outliers)
Reward range: [8.47, 15.61], mean: 12.12
  Created 13 candidate models for data size 1489
Current R2 threshold: -0.019999999999999962
  rf-tuned-l: R2 = 0.126 (std: 0.069)
  rf-tuned-xl: R2 = 0.135 (std: 0.072)
  gb-tuned-l: R2 = 0.173 (std: 0.037)
  gb-tuned-xl: R2 = 0.173 (std: 0.037)
  xgb-xl: R2 = -0.023 (std: 0.077)
  xgb-l: R2 = -0.023 (std: 0.077)
  mlp-adaptive-xl: R2 = 0.065 (std: 0.052)
  mlp-l: R2 = 0.079 (std: 0.070)
  svr-rbf-xl: R2 = 0.182 (std: 0.029)
  svr-poly-l: R2 = 0.182 (std: 0.029)
  knn-tuned-sqrt: R2 = 0.019 (std: 0.083)
  knn-tuned-l: R2 = 0.019 (std: 0.083)
  ridge: R2 = 0.053 (std: 0.036)

Model-based training with 11 models
Best R2: 0.182, Mean R2: 0.089
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9856, entropy=0.4449, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0558
  Round 1/3: Mean predicted reward = 12.184
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9844, entropy=0.4379, kl_div=0.0000
    Epoch 1: policy_loss=-0.0147, value_loss=0.9844, entropy=0.4358, kl_div=0.0422
  Round 2/3: Mean predicted reward = 12.065
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9811, entropy=0.4311, kl_div=0.0000
    Epoch 1: policy_loss=-0.0149, value_loss=0.9811, entropy=0.4286, kl_div=0.0427
  Round 3/3: Mean predicted reward = 12.227

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 24 Results ---
  Mean Oracle Reward: 12.665
  Min Oracle Reward: 8.472
  Max Oracle Reward: 16.719
  Std Oracle Reward: 1.834
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: 0.089, Max: 0.182, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 1586

======================================================================
EXPERIMENT ROUND 25/40
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1586
  Consistent improvement, increasing LR to 0.000360

--- Round 25 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCCCGCAGGAGGACTT
  TCGATGGGCCGCCGAA
  TCCCGAGATGGGGCAC
  CGAAGACGCGGTCTCG
  GAATAGCCGGGGCTCC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.467
  Max reward: 16.225
  With intrinsic bonuses: 12.449

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9782, entropy=0.4260, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5993

=== Surrogate Model Training ===
Total samples: 1650

Training on 1549 samples (removed 101 outliers)
Reward range: [8.47, 15.69], mean: 12.15
  Created 13 candidate models for data size 1549
Current R2 threshold: 0.0
  rf-tuned-l: R2 = 0.149 (std: 0.051)
  rf-tuned-xl: R2 = 0.138 (std: 0.045)
  gb-tuned-l: R2 = 0.176 (std: 0.034)
  gb-tuned-xl: R2 = 0.176 (std: 0.034)
  xgb-xl: R2 = -0.012 (std: 0.059)
  xgb-l: R2 = -0.012 (std: 0.059)
  mlp-adaptive-xl: R2 = 0.105 (std: 0.061)
  mlp-l: R2 = 0.088 (std: 0.061)
  svr-rbf-xl: R2 = 0.189 (std: 0.028)
  svr-poly-l: R2 = 0.189 (std: 0.028)
  knn-tuned-sqrt: R2 = 0.030 (std: 0.082)
  knn-tuned-l: R2 = 0.030 (std: 0.082)
  ridge: R2 = 0.055 (std: 0.045)

Model-based training with 11 models
Best R2: 0.189, Mean R2: 0.100
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9854, entropy=0.4061, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5965
  Round 1/3: Mean predicted reward = 12.149
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9840, entropy=0.3795, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8107
  Round 2/3: Mean predicted reward = 12.131
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9812, entropy=0.3639, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9126
  Round 3/3: Mean predicted reward = 12.214

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 25 Results ---
  Mean Oracle Reward: 12.444
  Min Oracle Reward: 1.576
  Max Oracle Reward: 16.128
  Std Oracle Reward: 2.353
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: 0.100, Max: 0.189, Count: 13
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
  CCCGTTGTCGCAGAGA
  GAAACCCTGGGCCTGG
  GCAGAGGCCCGTGCTA
  CAGCGTAGGCTAGCGC
  CTGAGGACAGCGTCGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.496
  Max reward: 15.775
  With intrinsic bonuses: 12.512

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9745, entropy=0.3344, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4997

=== Surrogate Model Training ===
Total samples: 1714

Training on 1610 samples (removed 104 outliers)
Reward range: [8.47, 15.70], mean: 12.17
  Created 13 candidate models for data size 1610
Current R2 threshold: 0.020000000000000018
  rf-tuned-l: R2 = 0.142 (std: 0.067)
  rf-tuned-xl: R2 = 0.143 (std: 0.061)
  gb-tuned-l: R2 = 0.171 (std: 0.051)
  gb-tuned-xl: R2 = 0.171 (std: 0.051)
  xgb-xl: R2 = -0.001 (std: 0.099)
  xgb-l: R2 = -0.001 (std: 0.099)
  mlp-adaptive-xl: R2 = 0.086 (std: 0.074)
  mlp-l: R2 = 0.084 (std: 0.087)
  svr-rbf-xl: R2 = 0.194 (std: 0.043)
  svr-poly-l: R2 = 0.194 (std: 0.043)
  knn-tuned-sqrt: R2 = 0.027 (std: 0.087)
  knn-tuned-l: R2 = 0.027 (std: 0.087)
  ridge: R2 = 0.051 (std: 0.043)

Model-based training with 11 models
Best R2: 0.194, Mean R2: 0.099
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9869, entropy=0.3238, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3141
  Round 1/3: Mean predicted reward = 12.058
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9797, entropy=0.3170, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3761
  Round 2/3: Mean predicted reward = 12.161
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9808, entropy=0.2986, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5313
  Round 3/3: Mean predicted reward = 12.219

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 26 Results ---
  Mean Oracle Reward: 12.547
  Min Oracle Reward: 5.054
  Max Oracle Reward: 16.143
  Std Oracle Reward: 1.882
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: 0.099, Max: 0.194, Count: 13
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
  AGTCGCATCGGCAGCG
  CAGCCCTGGCTAGGAG
  CGCTGCGGAGCAACTG
  AGCCACTGGCGTGACG
  GACCCGGGAAGGCTCT
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.579
  Max reward: 16.698
  With intrinsic bonuses: 12.540

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9760, entropy=0.2846, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3854

=== Surrogate Model Training ===
Total samples: 1778

Training on 1671 samples (removed 107 outliers)
Reward range: [8.44, 15.76], mean: 12.19
  Created 13 candidate models for data size 1671
Current R2 threshold: 0.040000000000000036
  rf-tuned-l: R2 = 0.144 (std: 0.074)
  rf-tuned-xl: R2 = 0.152 (std: 0.065)
  gb-tuned-l: R2 = 0.186 (std: 0.048)
  gb-tuned-xl: R2 = 0.186 (std: 0.048)
  xgb-xl: R2 = 0.011 (std: 0.103)
  xgb-l: R2 = 0.011 (std: 0.103)
  mlp-adaptive-xl: R2 = 0.085 (std: 0.079)
  mlp-l: R2 = 0.097 (std: 0.086)
  svr-rbf-xl: R2 = 0.190 (std: 0.051)
  svr-poly-l: R2 = 0.190 (std: 0.051)
  knn-tuned-sqrt: R2 = 0.036 (std: 0.101)
  knn-tuned-l: R2 = 0.036 (std: 0.101)
  ridge: R2 = 0.054 (std: 0.039)

Model-based training with 9 models
Best R2: 0.190, Mean R2: 0.106
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9876, entropy=0.2968, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2650
  Round 1/3: Mean predicted reward = 11.888
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9835, entropy=0.2868, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3458
  Round 2/3: Mean predicted reward = 12.109
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9775, entropy=0.2826, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3982
  Round 3/3: Mean predicted reward = 12.258

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 27 Results ---
  Mean Oracle Reward: 12.579
  Min Oracle Reward: 7.299
  Max Oracle Reward: 16.727
  Std Oracle Reward: 1.992
  Sequence Diversity: 1.000
  Models Used: 9
  Model R2 - Mean: 0.106, Max: 0.190, Count: 13
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
  GTGGCACAGAGCTGCC
  GCGACGCGTACGCTGA
  TACGGGGGCCAGCACT
  AACCGCTAGGCCGGGT
  AGGCCTGAGGCAGTCC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.634
  Max reward: 16.421
  With intrinsic bonuses: 12.638

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9745, entropy=0.2712, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2728

=== Surrogate Model Training ===
Total samples: 1842

Training on 1735 samples (removed 107 outliers)
Reward range: [8.44, 15.81], mean: 12.20
  Created 13 candidate models for data size 1735
Current R2 threshold: 0.06
  rf-tuned-l: R2 = 0.186 (std: 0.077)
  rf-tuned-xl: R2 = 0.180 (std: 0.071)
  gb-tuned-l: R2 = 0.193 (std: 0.063)
  gb-tuned-xl: R2 = 0.193 (std: 0.063)
  xgb-xl: R2 = 0.057 (std: 0.082)
  xgb-l: R2 = 0.057 (std: 0.082)
  mlp-adaptive-xl: R2 = 0.143 (std: 0.072)
  mlp-l: R2 = 0.120 (std: 0.087)
  svr-rbf-xl: R2 = 0.202 (std: 0.063)
  svr-poly-l: R2 = 0.202 (std: 0.063)
  knn-tuned-sqrt: R2 = 0.081 (std: 0.088)
  knn-tuned-l: R2 = 0.081 (std: 0.088)
  ridge: R2 = 0.069 (std: 0.046)

Model-based training with 11 models
Best R2: 0.202, Mean R2: 0.136
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9941, entropy=0.2605, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1973
  Round 1/3: Mean predicted reward = 11.825
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9864, entropy=0.2574, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1054
  Round 2/3: Mean predicted reward = 12.015
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9800, entropy=0.2559, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1677
  Round 3/3: Mean predicted reward = 12.175

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 28 Results ---
  Mean Oracle Reward: 12.643
  Min Oracle Reward: 9.010
  Max Oracle Reward: 16.351
  Std Oracle Reward: 1.620
  Sequence Diversity: 1.000
  Models Used: 11
  Model R2 - Mean: 0.136, Max: 0.202, Count: 13
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
  GCCACTGCAGAGGGTC
  GGAGCCCAGTTGCCAG
  ATGCCACTGGGCCGGA
  GCCAGTAAGCTGCGGC
  GGATCCCTCAAGGGGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.272
  Max reward: 16.711
  With intrinsic bonuses: 12.280

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9769, entropy=0.2555, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0711

=== Surrogate Model Training ===
Total samples: 1906

Training on 1796 samples (removed 110 outliers)
Reward range: [8.44, 15.81], mean: 12.21
  Created 13 candidate models for data size 1796
Current R2 threshold: 0.08000000000000002
  rf-tuned-l: R2 = 0.181 (std: 0.095)
  rf-tuned-xl: R2 = 0.174 (std: 0.089)
  gb-tuned-l: R2 = 0.208 (std: 0.070)
  gb-tuned-xl: R2 = 0.208 (std: 0.070)
  xgb-xl: R2 = 0.046 (std: 0.122)
  xgb-l: R2 = 0.046 (std: 0.122)
  mlp-adaptive-xl: R2 = 0.158 (std: 0.080)
  mlp-l: R2 = 0.156 (std: 0.103)
  svr-rbf-xl: R2 = 0.218 (std: 0.074)
  svr-poly-l: R2 = 0.218 (std: 0.074)
  knn-tuned-sqrt: R2 = 0.111 (std: 0.098)
  knn-tuned-l: R2 = 0.111 (std: 0.098)
  ridge: R2 = 0.086 (std: 0.052)

Model-based training with 11 models
Best R2: 0.218, Mean R2: 0.148
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9946, entropy=0.2642, kl_div=0.0000
    Epoch 1: policy_loss=0.0127, value_loss=0.9946, entropy=0.2636, kl_div=0.0310
  Round 1/3: Mean predicted reward = 11.702
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9890, entropy=0.2603, kl_div=0.0000
    Epoch 1: policy_loss=-0.0028, value_loss=0.9890, entropy=0.2605, kl_div=-0.0077
  Round 2/3: Mean predicted reward = 12.008
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9788, entropy=0.2722, kl_div=0.0000
    Epoch 1: policy_loss=-0.0064, value_loss=0.9788, entropy=0.2725, kl_div=-0.0097
  Round 3/3: Mean predicted reward = 12.277

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 29 Results ---
  Mean Oracle Reward: 12.290
  Min Oracle Reward: 0.352
  Max Oracle Reward: 16.883
  Std Oracle Reward: 2.320
  Sequence Diversity: 0.984
  Models Used: 11
  Model R2 - Mean: 0.148, Max: 0.218, Count: 13
  Total Sequences Evaluated: 1906

======================================================================
EXPERIMENT ROUND 30/40
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1906

--- Round 30 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  GAGCAGCCGGCACTGT
  GGGAGCCATGCGACCT
  ATTCCGGCGGCGAACG
  CCGAGGCATCACGGGT
  TAGGGAGTGGCCACCC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.754
  Max reward: 16.626
  With intrinsic bonuses: 12.703

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9758, entropy=0.2574, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3921

=== Surrogate Model Training ===
Total samples: 1970

Training on 1859 samples (removed 111 outliers)
Reward range: [8.38, 15.81], mean: 12.22
  Created 13 candidate models for data size 1859
Current R2 threshold: 0.10000000000000003
  rf-tuned-l: R2 = 0.182 (std: 0.099)
  rf-tuned-xl: R2 = 0.191 (std: 0.102)
  gb-tuned-l: R2 = 0.224 (std: 0.079)
  gb-tuned-xl: R2 = 0.224 (std: 0.079)
  xgb-xl: R2 = 0.081 (std: 0.114)
  xgb-l: R2 = 0.081 (std: 0.114)
  mlp-adaptive-xl: R2 = 0.176 (std: 0.117)
  mlp-l: R2 = 0.156 (std: 0.134)
  svr-rbf-xl: R2 = 0.242 (std: 0.082)
  svr-poly-l: R2 = 0.242 (std: 0.082)
  knn-tuned-sqrt: R2 = 0.111 (std: 0.113)
  knn-tuned-l: R2 = 0.111 (std: 0.113)
  ridge: R2 = 0.094 (std: 0.063)

Model-based training with 10 models
Best R2: 0.242, Mean R2: 0.163
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9935, entropy=0.2539, kl_div=0.0000
    Epoch 1: policy_loss=-0.0035, value_loss=0.9935, entropy=0.2555, kl_div=-0.0174
  Round 1/3: Mean predicted reward = 11.658
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9919, entropy=0.2598, kl_div=0.0000
    Epoch 1: policy_loss=0.0531, value_loss=0.9919, entropy=0.2672, kl_div=-0.4803
  Round 2/3: Mean predicted reward = 11.846
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9804, entropy=0.2893, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1454
  Round 3/3: Mean predicted reward = 12.219

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 30 Results ---
  Mean Oracle Reward: 12.744
  Min Oracle Reward: 9.335
  Max Oracle Reward: 16.896
  Std Oracle Reward: 1.635
  Sequence Diversity: 0.984
  Models Used: 10
  Model R2 - Mean: 0.163, Max: 0.242, Count: 13
  New best mean reward!
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

--- Generated Sequences (Diversity: 0.984) ---
  GGCGCGAACTGCCAGT
  AGCGCCCATAGGGGCT
  GGTGAGCGACACCGCT
  TGCCGTGCGAGCCGAA
  GCTAACTGACCGGGCG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.519
  Max reward: 16.134
  With intrinsic bonuses: 12.506

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9777, entropy=0.2632, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3825

=== Surrogate Model Training ===
Total samples: 2034

Training on 1918 samples (removed 116 outliers)
Reward range: [8.45, 15.81], mean: 12.24
  Created 13 candidate models for data size 1918
Current R2 threshold: 0.12
  rf-tuned-l: R2 = 0.201 (std: 0.105)
  rf-tuned-xl: R2 = 0.197 (std: 0.096)
  gb-tuned-l: R2 = 0.229 (std: 0.095)
  gb-tuned-xl: R2 = 0.229 (std: 0.095)
  xgb-xl: R2 = 0.096 (std: 0.146)
  xgb-l: R2 = 0.096 (std: 0.146)
  mlp-adaptive-xl: R2 = 0.187 (std: 0.097)
  mlp-l: R2 = 0.203 (std: 0.093)
  svr-rbf-xl: R2 = 0.254 (std: 0.089)
  svr-poly-l: R2 = 0.254 (std: 0.089)
  knn-tuned-sqrt: R2 = 0.112 (std: 0.124)
  knn-tuned-l: R2 = 0.112 (std: 0.124)
  ridge: R2 = 0.105 (std: 0.069)

Model-based training with 8 models
Best R2: 0.254, Mean R2: 0.175
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9911, entropy=0.2763, kl_div=0.0000
    Epoch 1: policy_loss=-0.0143, value_loss=0.9911, entropy=0.2748, kl_div=0.0370
  Round 1/3: Mean predicted reward = 11.759
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9851, entropy=0.2726, kl_div=0.0000
    Epoch 1: policy_loss=0.1784, value_loss=0.9851, entropy=0.2765, kl_div=-0.4698
  Round 2/3: Mean predicted reward = 11.935
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9831, entropy=0.2873, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1313
  Round 3/3: Mean predicted reward = 12.107

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 31 Results ---
  Mean Oracle Reward: 12.512
  Min Oracle Reward: 6.521
  Max Oracle Reward: 15.925
  Std Oracle Reward: 1.728
  Sequence Diversity: 0.984
  Models Used: 8
  Model R2 - Mean: 0.175, Max: 0.254, Count: 13
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

--- Generated Sequences (Diversity: 0.984) ---
  TGCGACGCACTAGGGC
  CGTACGTGGAACGGCC
  CTAAGCCACGCTGGGT
  CTGGCAACCCGGGATG
  AGGTGTCGAGCACCGC
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.616
  Max reward: 15.941
  With intrinsic bonuses: 12.562

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9785, entropy=0.2713, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2648

=== Surrogate Model Training ===
Total samples: 2098

Training on 1983 samples (removed 115 outliers)
Reward range: [8.44, 15.92], mean: 12.26
  Created 13 candidate models for data size 1983
Current R2 threshold: 0.14
  rf-tuned-l: R2 = 0.222 (std: 0.105)
  rf-tuned-xl: R2 = 0.211 (std: 0.103)
  gb-tuned-l: R2 = 0.235 (std: 0.098)
  gb-tuned-xl: R2 = 0.235 (std: 0.098)
  xgb-xl: R2 = 0.110 (std: 0.150)
  xgb-l: R2 = 0.110 (std: 0.150)
  mlp-adaptive-xl: R2 = 0.183 (std: 0.123)
  mlp-l: R2 = 0.161 (std: 0.130)
  svr-rbf-xl: R2 = 0.257 (std: 0.099)
  svr-poly-l: R2 = 0.257 (std: 0.099)
  knn-tuned-sqrt: R2 = 0.114 (std: 0.126)
  knn-tuned-l: R2 = 0.114 (std: 0.126)
  ridge: R2 = 0.102 (std: 0.089)

Model-based training with 8 models
Best R2: 0.257, Mean R2: 0.178
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9904, entropy=0.2592, kl_div=0.0000
    Epoch 1: policy_loss=-0.0045, value_loss=0.9904, entropy=0.2577, kl_div=0.0498
  Round 1/3: Mean predicted reward = 11.657
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9890, entropy=0.2625, kl_div=0.0000
    Epoch 1: policy_loss=-0.0021, value_loss=0.9890, entropy=0.2641, kl_div=-0.3476
  Round 2/3: Mean predicted reward = 11.820
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9846, entropy=0.2814, kl_div=0.0000
    Epoch 1: policy_loss=-0.0304, value_loss=0.9846, entropy=0.2797, kl_div=0.0302
  Round 3/3: Mean predicted reward = 12.122

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 32 Results ---
  Mean Oracle Reward: 12.624
  Min Oracle Reward: 7.033
  Max Oracle Reward: 16.001
  Std Oracle Reward: 1.795
  Sequence Diversity: 0.984
  Models Used: 8
  Model R2 - Mean: 0.178, Max: 0.257, Count: 13
  Total Sequences Evaluated: 2098

======================================================================
EXPERIMENT ROUND 33/40
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2098
  Performance plateaued, reducing LR to 0.000055

--- Round 33 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  CTGGAGCAGTCGACCG
  TAGTCCGGCGACGACG
  CCCCGAGTATCGGGGA
  GTATCCACGGCGGCAG
  CCGTACCGGGCGATGA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.198
  Max reward: 15.750
  With intrinsic bonuses: 12.197

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9830, entropy=0.2729, kl_div=0.0000
    Epoch 1: policy_loss=-0.0126, value_loss=0.9830, entropy=0.2723, kl_div=0.0235

=== Surrogate Model Training ===
Total samples: 2162

Training on 2045 samples (removed 117 outliers)
Reward range: [8.45, 15.89], mean: 12.25
  Created 13 candidate models for data size 2045
Current R2 threshold: 0.16000000000000003
  rf-tuned-l: R2 = 0.230 (std: 0.100)
  rf-tuned-xl: R2 = 0.224 (std: 0.101)
  gb-tuned-l: R2 = 0.239 (std: 0.105)
  gb-tuned-xl: R2 = 0.239 (std: 0.105)
  xgb-xl: R2 = 0.132 (std: 0.137)
  xgb-l: R2 = 0.132 (std: 0.137)
  mlp-adaptive-xl: R2 = 0.174 (std: 0.128)
  mlp-l: R2 = 0.181 (std: 0.119)
  svr-rbf-xl: R2 = 0.262 (std: 0.104)
  svr-poly-l: R2 = 0.262 (std: 0.104)
  knn-tuned-sqrt: R2 = 0.117 (std: 0.116)
  knn-tuned-l: R2 = 0.117 (std: 0.116)
  ridge: R2 = 0.107 (std: 0.106)

Model-based training with 8 models
Best R2: 0.262, Mean R2: 0.186
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9901, entropy=0.2701, kl_div=0.0000
    Epoch 1: policy_loss=-0.0043, value_loss=0.9901, entropy=0.2697, kl_div=0.0051
  Round 1/3: Mean predicted reward = 11.658
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9866, entropy=0.2678, kl_div=0.0000
    Epoch 1: policy_loss=-0.0343, value_loss=0.9866, entropy=0.2680, kl_div=-0.0933
  Round 2/3: Mean predicted reward = 11.902
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9822, entropy=0.2498, kl_div=0.0000
    Epoch 1: policy_loss=-0.0075, value_loss=0.9822, entropy=0.2500, kl_div=-0.0758
  Round 3/3: Mean predicted reward = 12.186

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 33 Results ---
  Mean Oracle Reward: 12.203
  Min Oracle Reward: 9.211
  Max Oracle Reward: 15.974
  Std Oracle Reward: 1.326
  Sequence Diversity: 0.984
  Models Used: 8
  Model R2 - Mean: 0.186, Max: 0.262, Count: 13
  Total Sequences Evaluated: 2162

======================================================================
EXPERIMENT ROUND 34/40
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 2162

--- Round 34 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GAGTCGCCGCGACTGA
  GGCAGAATGTGCCGCC
  GCCACTTAGACGGGGC
  GCGCCACGAGGACTTG
  ACACGAGGTCGCCGTG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.676
  Max reward: 15.183
  With intrinsic bonuses: 12.653

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9799, entropy=0.2840, kl_div=0.0000
    Epoch 1: policy_loss=-0.0289, value_loss=0.9799, entropy=0.2835, kl_div=0.0156

=== Surrogate Model Training ===
Total samples: 2226

Training on 2109 samples (removed 117 outliers)
Reward range: [8.45, 15.92], mean: 12.27
  Created 13 candidate models for data size 2109
Current R2 threshold: 0.18
  rf-tuned-l: R2 = 0.222 (std: 0.112)
  rf-tuned-xl: R2 = 0.217 (std: 0.111)
  gb-tuned-l: R2 = 0.229 (std: 0.123)
  gb-tuned-xl: R2 = 0.229 (std: 0.123)
  xgb-xl: R2 = 0.115 (std: 0.129)
  xgb-l: R2 = 0.115 (std: 0.129)
  mlp-adaptive-xl: R2 = 0.173 (std: 0.152)
  mlp-l: R2 = 0.194 (std: 0.134)
  svr-rbf-xl: R2 = 0.261 (std: 0.114)
  svr-poly-l: R2 = 0.261 (std: 0.114)
  knn-tuned-sqrt: R2 = 0.106 (std: 0.141)
  knn-tuned-l: R2 = 0.106 (std: 0.141)
  ridge: R2 = 0.107 (std: 0.116)

Model-based training with 7 models
Best R2: 0.261, Mean R2: 0.180
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9891, entropy=0.2679, kl_div=0.0000
    Epoch 1: policy_loss=-0.0066, value_loss=0.9891, entropy=0.2678, kl_div=0.0005
  Round 1/3: Mean predicted reward = 11.569
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9912, entropy=0.2604, kl_div=0.0000
    Epoch 1: policy_loss=-0.0461, value_loss=0.9912, entropy=0.2607, kl_div=-0.0763
  Round 2/3: Mean predicted reward = 11.832
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9853, entropy=0.2869, kl_div=0.0000
    Epoch 1: policy_loss=0.0001, value_loss=0.9853, entropy=0.2871, kl_div=-0.0727
  Round 3/3: Mean predicted reward = 12.152

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 34 Results ---
  Mean Oracle Reward: 12.711
  Min Oracle Reward: 7.913
  Max Oracle Reward: 15.142
  Std Oracle Reward: 1.290
  Sequence Diversity: 1.000
  Models Used: 7
  Model R2 - Mean: 0.180, Max: 0.261, Count: 13
  Total Sequences Evaluated: 2226

======================================================================
EXPERIMENT ROUND 35/40
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 2226

--- Round 35 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  CCTCTGCAGGGCGGAA
  TCCGGCGTAGACAGGC
  CAATGGCGGACGCGTC
  TCCAGGAAGCGGCTGC
  GGACAGTCACCCGTGG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 11.817
  Max reward: 15.559
  With intrinsic bonuses: 11.770

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9802, entropy=0.2704, kl_div=0.0000
    Epoch 1: policy_loss=-0.0484, value_loss=0.9802, entropy=0.2697, kl_div=-0.0272

=== Surrogate Model Training ===
Total samples: 2290

Training on 2170 samples (removed 120 outliers)
Reward range: [8.44, 15.92], mean: 12.26
  Created 13 candidate models for data size 2170
Current R2 threshold: 0.2
  rf-tuned-l: R2 = 0.212 (std: 0.108)
  rf-tuned-xl: R2 = 0.220 (std: 0.103)
  gb-tuned-l: R2 = 0.231 (std: 0.116)
  gb-tuned-xl: R2 = 0.231 (std: 0.116)
  xgb-xl: R2 = 0.136 (std: 0.125)
  xgb-l: R2 = 0.136 (std: 0.125)
  mlp-adaptive-xl: R2 = 0.193 (std: 0.126)
  mlp-l: R2 = 0.193 (std: 0.126)
  svr-rbf-xl: R2 = 0.261 (std: 0.105)
  svr-poly-l: R2 = 0.261 (std: 0.105)
  knn-tuned-sqrt: R2 = 0.125 (std: 0.118)
  knn-tuned-l: R2 = 0.125 (std: 0.118)
  ridge: R2 = 0.106 (std: 0.108)

Model-based training with 6 models
Best R2: 0.261, Mean R2: 0.187
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9921, entropy=0.2565, kl_div=0.0000
    Epoch 1: policy_loss=-0.0965, value_loss=0.9920, entropy=0.2575, kl_div=-0.2801
  Round 1/3: Mean predicted reward = 11.339
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9879, entropy=0.2708, kl_div=0.0000
    Epoch 1: policy_loss=0.0439, value_loss=0.9879, entropy=0.2741, kl_div=-0.8378
  Round 2/3: Mean predicted reward = 11.856
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9859, entropy=0.2880, kl_div=0.0000
    Epoch 1: policy_loss=-0.0227, value_loss=0.9859, entropy=0.2870, kl_div=-0.0803
  Round 3/3: Mean predicted reward = 12.160

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 35 Results ---
  Mean Oracle Reward: 11.754
  Min Oracle Reward: 5.680
  Max Oracle Reward: 15.551
  Std Oracle Reward: 1.935
  Sequence Diversity: 0.984
  Models Used: 6
  Model R2 - Mean: 0.187, Max: 0.261, Count: 13
  Total Sequences Evaluated: 2290

======================================================================
EXPERIMENT ROUND 36/40
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 2290

--- Round 36 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.984) ---
  CTACAGCGGGAGTCCG
  AGCCTGGAGACGCTCG
  TATCCGGCCGGGAACG
  TTACACGGGGGACGCC
  GACGTGGGCCTCCAAG
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.615
  Max reward: 17.109
  With intrinsic bonuses: 12.587

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9832, entropy=0.2800, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4354

=== Surrogate Model Training ===
Total samples: 2354

Training on 2232 samples (removed 122 outliers)
Reward range: [8.44, 15.98], mean: 12.27
  Created 13 candidate models for data size 2232
Current R2 threshold: 0.22000000000000003
  rf-tuned-l: R2 = 0.225 (std: 0.123)
  rf-tuned-xl: R2 = 0.223 (std: 0.123)
  gb-tuned-l: R2 = 0.235 (std: 0.139)
  gb-tuned-xl: R2 = 0.235 (std: 0.139)
  xgb-xl: R2 = 0.139 (std: 0.150)
  xgb-l: R2 = 0.139 (std: 0.150)
  mlp-adaptive-xl: R2 = 0.194 (std: 0.156)
  mlp-l: R2 = 0.207 (std: 0.146)
  svr-rbf-xl: R2 = 0.270 (std: 0.122)
  svr-poly-l: R2 = 0.270 (std: 0.122)
  knn-tuned-sqrt: R2 = 0.126 (std: 0.130)
  knn-tuned-l: R2 = 0.126 (std: 0.130)
  ridge: R2 = 0.115 (std: 0.116)

Model-based training with 6 models
Best R2: 0.270, Mean R2: 0.193
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9869, entropy=0.2855, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0605
  Round 1/3: Mean predicted reward = 11.720
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9865, entropy=0.2710, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1727
  Round 2/3: Mean predicted reward = 12.159
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9841, entropy=0.2676, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3549
  Round 3/3: Mean predicted reward = 12.323

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 36 Results ---
  Mean Oracle Reward: 12.604
  Min Oracle Reward: 5.895
  Max Oracle Reward: 17.072
  Std Oracle Reward: 2.011
  Sequence Diversity: 0.984
  Models Used: 6
  Model R2 - Mean: 0.193, Max: 0.270, Count: 13
  Total Sequences Evaluated: 2354

======================================================================
EXPERIMENT ROUND 37/40
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 2354

--- Round 37 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCGGGCCGAACATGCT
  GCGAGCGGCATGTACC
  AGAGGCCGGTCAGCCT
  CCAGCGAGTTGGACGC
  CTCAGGGCGATGCCGA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.607
  Max reward: 18.322
  With intrinsic bonuses: 12.583

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9817, entropy=0.2723, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5148

=== Surrogate Model Training ===
Total samples: 2418

Training on 2296 samples (removed 122 outliers)
Reward range: [8.38, 16.03], mean: 12.28
  Created 13 candidate models for data size 2296
Current R2 threshold: 0.24000000000000005
  rf-tuned-l: R2 = 0.239 (std: 0.121)
  rf-tuned-xl: R2 = 0.240 (std: 0.121)
  gb-tuned-l: R2 = 0.243 (std: 0.130)
  gb-tuned-xl: R2 = 0.243 (std: 0.130)
  xgb-xl: R2 = 0.149 (std: 0.149)
  xgb-l: R2 = 0.149 (std: 0.149)
  mlp-adaptive-xl: R2 = 0.225 (std: 0.128)
  mlp-l: R2 = 0.203 (std: 0.136)
  svr-rbf-xl: R2 = 0.278 (std: 0.119)
  svr-poly-l: R2 = 0.278 (std: 0.119)
  knn-tuned-sqrt: R2 = 0.129 (std: 0.136)
  knn-tuned-l: R2 = 0.129 (std: 0.136)
  ridge: R2 = 0.117 (std: 0.111)

Model-based training with 4 models
Best R2: 0.278, Mean R2: 0.202
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9890, entropy=0.2730, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2027
  Round 1/3: Mean predicted reward = 11.628
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9868, entropy=0.2716, kl_div=0.0000
    Epoch 1: policy_loss=-0.0591, value_loss=0.9868, entropy=0.2700, kl_div=-0.0938
  Round 2/3: Mean predicted reward = 12.040
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9835, entropy=0.2616, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1885
  Round 3/3: Mean predicted reward = 12.075

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 37 Results ---
  Mean Oracle Reward: 12.586
  Min Oracle Reward: 8.946
  Max Oracle Reward: 18.506
  Std Oracle Reward: 1.925
  Sequence Diversity: 1.000
  Models Used: 4
  Model R2 - Mean: 0.202, Max: 0.278, Count: 13
  Total Sequences Evaluated: 2418

======================================================================
EXPERIMENT ROUND 38/40
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 2418

--- Round 38 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCAGGCCGATAGGGCC
  AGACGCGTGCCGACGT
  GGAAAGCGTGCCGCTC
  CTCGGGAGCCAGTAGC
  GATGAGGGCCGCACCT
  ... (64 total)

Oracle Evaluation:
  Mean reward: 13.171
  Max reward: 17.237
  With intrinsic bonuses: 13.217

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9801, entropy=0.2588, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1957

=== Surrogate Model Training ===
Total samples: 2482

Training on 2360 samples (removed 122 outliers)
Reward range: [8.37, 16.11], mean: 12.30
  Created 13 candidate models for data size 2360
Current R2 threshold: 0.26000000000000006
  rf-tuned-l: R2 = 0.245 (std: 0.121)
  rf-tuned-xl: R2 = 0.251 (std: 0.112)
  gb-tuned-l: R2 = 0.257 (std: 0.125)
  gb-tuned-xl: R2 = 0.257 (std: 0.125)
  xgb-xl: R2 = 0.178 (std: 0.133)
  xgb-l: R2 = 0.178 (std: 0.133)
  mlp-adaptive-xl: R2 = 0.213 (std: 0.141)
  mlp-l: R2 = 0.237 (std: 0.146)
  svr-rbf-xl: R2 = 0.285 (std: 0.122)
  svr-poly-l: R2 = 0.285 (std: 0.122)
  knn-tuned-sqrt: R2 = 0.139 (std: 0.138)
  knn-tuned-l: R2 = 0.139 (std: 0.138)
  ridge: R2 = 0.125 (std: 0.113)

Model-based training with 2 models
Best R2: 0.285, Mean R2: 0.214
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9867, entropy=0.2508, kl_div=0.0000
    Epoch 1: policy_loss=-0.0025, value_loss=0.9867, entropy=0.2496, kl_div=0.0488
  Round 1/3: Mean predicted reward = 11.572
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9869, entropy=0.2593, kl_div=0.0000
    Epoch 1: policy_loss=-0.0176, value_loss=0.9869, entropy=0.2590, kl_div=-0.2167
  Round 2/3: Mean predicted reward = 12.041
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9833, entropy=0.2611, kl_div=0.0000
    Epoch 1: policy_loss=-0.0414, value_loss=0.9833, entropy=0.2601, kl_div=-0.0026
  Round 3/3: Mean predicted reward = 12.263

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 38 Results ---
  Mean Oracle Reward: 13.177
  Min Oracle Reward: 7.221
  Max Oracle Reward: 17.285
  Std Oracle Reward: 1.989
  Sequence Diversity: 1.000
  Models Used: 2
  Model R2 - Mean: 0.214, Max: 0.285, Count: 13
  New best mean reward!
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
  TCGCACAGGGGCTCGA
  GCCCGATCATGGGCAG
  GCGTCACTGAAGGCGC
  AGCGGCGCAGGTCCAT
  GGGACTGCCCGAGCAT
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.820
  Max reward: 18.594
  With intrinsic bonuses: 12.842

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9809, entropy=0.2464, kl_div=0.0000
    Epoch 1: policy_loss=-0.0090, value_loss=0.9809, entropy=0.2459, kl_div=0.0127

=== Surrogate Model Training ===
Total samples: 2546

Training on 2419 samples (removed 127 outliers)
Reward range: [8.37, 16.18], mean: 12.31
  Created 13 candidate models for data size 2419
Current R2 threshold: 0.27999999999999997
  rf-tuned-l: R2 = 0.254 (std: 0.122)
  rf-tuned-xl: R2 = 0.257 (std: 0.123)
  gb-tuned-l: R2 = 0.259 (std: 0.122)
  gb-tuned-xl: R2 = 0.259 (std: 0.122)
  xgb-xl: R2 = 0.196 (std: 0.144)
  xgb-l: R2 = 0.196 (std: 0.144)
  mlp-adaptive-xl: R2 = 0.230 (std: 0.133)
  mlp-l: R2 = 0.241 (std: 0.133)
  svr-rbf-xl: R2 = 0.288 (std: 0.120)
  svr-poly-l: R2 = 0.288 (std: 0.120)
  knn-tuned-sqrt: R2 = 0.145 (std: 0.134)
  knn-tuned-l: R2 = 0.145 (std: 0.134)
  ridge: R2 = 0.131 (std: 0.116)

Model-based training with 2 models
Best R2: 0.288, Mean R2: 0.222
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9888, entropy=0.2456, kl_div=0.0000
    Epoch 1: policy_loss=-0.0045, value_loss=0.9888, entropy=0.2451, kl_div=0.0065
  Round 1/3: Mean predicted reward = 11.545
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9895, entropy=0.2491, kl_div=0.0000
    Epoch 1: policy_loss=-0.0412, value_loss=0.9895, entropy=0.2489, kl_div=-0.0953
  Round 2/3: Mean predicted reward = 11.925
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9843, entropy=0.2540, kl_div=0.0000
    Epoch 1: policy_loss=-0.0024, value_loss=0.9843, entropy=0.2538, kl_div=-0.0814
  Round 3/3: Mean predicted reward = 12.285

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 39 Results ---
  Mean Oracle Reward: 12.844
  Min Oracle Reward: 8.135
  Max Oracle Reward: 18.690
  Std Oracle Reward: 2.182
  Sequence Diversity: 0.984
  Models Used: 2
  Model R2 - Mean: 0.222, Max: 0.288, Count: 13
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
  CGGAACTCTGCGCGAG
  AGGGGCACGCCTTGAC
  AGTGCTACCGGCACGG
  GAGCGGCGACCGCATT
  TCGCGGAATGCCGCGA
  ... (64 total)

Oracle Evaluation:
  Mean reward: 12.696
  Max reward: 16.929
  With intrinsic bonuses: 12.683

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9831, entropy=0.2682, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1805

=== Surrogate Model Training ===
Total samples: 2610

Training on 2477 samples (removed 133 outliers)
Reward range: [8.30, 16.21], mean: 12.31
  Created 13 candidate models for data size 2477
Current R2 threshold: 0.3
  rf-tuned-l: R2 = 0.267 (std: 0.118)
  rf-tuned-xl: R2 = 0.271 (std: 0.119)
  gb-tuned-l: R2 = 0.271 (std: 0.123)
  gb-tuned-xl: R2 = 0.271 (std: 0.123)
  xgb-xl: R2 = 0.208 (std: 0.161)
  xgb-l: R2 = 0.208 (std: 0.161)
  mlp-adaptive-xl: R2 = 0.246 (std: 0.124)
  mlp-l: R2 = 0.236 (std: 0.129)
  svr-rbf-xl: R2 = 0.294 (std: 0.118)
  svr-poly-l: R2 = 0.294 (std: 0.118)
  knn-tuned-sqrt: R2 = 0.150 (std: 0.135)
  knn-tuned-l: R2 = 0.150 (std: 0.135)
  ridge: R2 = 0.136 (std: 0.114)
  Fallback: Using svr-rbf-xl with R2 = 0.294

Model-based training with 1 models
Best R2: 0.294, Mean R2: 0.231
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9895, entropy=0.2418, kl_div=0.0000
    Epoch 1: policy_loss=-0.0377, value_loss=0.9895, entropy=0.2387, kl_div=-0.1982
  Round 1/3: Mean predicted reward = 11.649
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9828, entropy=0.2435, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3769
  Round 2/3: Mean predicted reward = 11.925
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9827, entropy=0.2448, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5674
  Round 3/3: Mean predicted reward = 12.259

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 40 Results ---
  Mean Oracle Reward: 12.706
  Min Oracle Reward: 7.745
  Max Oracle Reward: 16.920
  Std Oracle Reward: 2.073
  Sequence Diversity: 0.969
  Models Used: 1
  Model R2 - Mean: 0.231, Max: 0.294, Count: 13
  Total Sequences Evaluated: 2610

======================================================================
DyNA PPO ALGORITHM COMPLETE!
======================================================================
Total rounds executed: 40
Total sequences evaluated: 2610
Best mean reward: 13.177 (achieved at round 38)

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 40
Final Mean Reward: 12.7063
Best Mean Reward: 13.1775
Best Max Reward: 18.6903
Initial Lr: 0.0003
Final Lr: 0.0003
Total Updates: 210
Final Diversity: 0.9688
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
  GGCCGCCGGCCGGCCG: 17.059
  GGCCGCCGGCCGGCCG: 17.229
  GGCCGCCGGCCGGCCG: 17.350
  GGCCGCCGGCCGGCCG: 17.245
  GGCCGCCGGCCGGCCG: 17.134

Stochastic (Exploration):
  GGCCGCCGCGCGCCGG: 13.182
  GGCGCCCGGCCGGCCG: 15.297
  GGCCCGCGCCGCCGGC: 13.857
  GGCCGCCGGCCGCGGC: 15.892
  GGCCGCCGCGCGCCCG: 12.911

Final Performance:
  Mean reward: 15.715
  Max reward: 17.350
  Std reward: 1.705

Best sequence found: GGCCGCCGGCCGGCCG
   Reward: 17.350

======================================================================
Training complete! Check 'learning_curves.png' and 'training_metrics.json'
======================================================================