======================================================================
RUNNING IMPROVED DyNA PPO WITH BETTER SURROGATE LEARNING
======================================================================
======================================================================
IMPROVED DyNA PPO ALGORITHM
======================================================================
Configuration:
  Number of experiment rounds N = 50
  Number of model-based training rounds M = 5
  Minimum model score τ = 0.2
  Batch size B = 32
  Warm-up phase: True
======================================================================

=== WARM-UP PHASE ===
Generating 50 warm-up samples...
Warm-up statistics:
  Mean reward: 6.775
  Std reward: 1.883
  Min/Max: 0.000 / 9.887

======================================================================
EXPERIMENT ROUND 1/50
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.300
Total data collected: 50

--- Round 1 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 0.969) ---
  AGATCGTG
  AGGTCCCC
  GCTTGTAG
  CTCGCTCT
  ACTAAGTG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.988
  Max reward: 10.050
  With intrinsic bonuses: 7.979

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9606, entropy=1.3849, kl_div=0.0000
    Epoch 2: policy_loss=-0.1971, value_loss=0.9609, entropy=1.3821, kl_div=-0.0100
    Epoch 4: policy_loss=-0.2314, value_loss=0.9613, entropy=1.3751, kl_div=0.0450
    Early stopping at epoch 5: KL divergence = 0.0913

=== Surrogate Model Training ===
Total samples: 82

Training on 78 samples (removed 4 outliers)
Reward range: [4.13, 10.02], mean: 7.53
  Created 8 candidate models for data size 78
  rf-xs: R2 = -0.391 (std: 0.353)
  rf-s: R2 = -0.378 (std: 0.344)
  knn-xs: R2 = -0.313 (std: 0.201)
  knn-s: R2 = -0.313 (std: 0.201)
  ridge: R2 = -0.457 (std: 0.392)
  gb-xs: R2 = -0.657 (std: 0.676)
  gp: R2 = -61.363 (std: 41.304)
  svr-rbf-s: R2 = -0.201 (std: 0.268)
  Fallback: Using svr-rbf-s with R2 = -0.201

Model-based training with 1 models
Best R2: -0.201, Mean R2: -8.009
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9553, entropy=1.3731, kl_div=0.0000
  Round 1/2: Mean predicted reward = 7.494
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9721, entropy=1.3669, kl_div=0.0000
  Round 2/2: Mean predicted reward = 7.514

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 1 Results ---
  Mean Oracle Reward: 8.031
  Min Oracle Reward: 5.954
  Max Oracle Reward: 9.977
  Std Oracle Reward: 0.859
  Sequence Diversity: 0.969
  Models Used: 1
  Model R² - Mean: -8.009, Max: -0.201, Count: 8
  New best mean reward!
  Total Sequences Evaluated: 82

======================================================================
EXPERIMENT ROUND 2/50
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.300
Total data collected: 82

--- Round 2 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  TCACCGCT
  TGCGCTGA
  TGGTGACG
  AAATGGAG
  AGATACCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.423
  Max reward: 9.775
  With intrinsic bonuses: 7.459

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9646, entropy=1.3622, kl_div=0.0000
    Early stopping at epoch 2: KL divergence = 0.1003

=== Surrogate Model Training ===
Total samples: 114

Training on 111 samples (removed 3 outliers)
Reward range: [3.33, 10.02], mean: 7.46
  Created 11 candidate models for data size 111
  rf-m: R2 = -0.117 (std: 0.270)
  rf-l: R2 = -0.137 (std: 0.318)
  gb-m: R2 = -0.263 (std: 0.220)
  gb-l: R2 = -0.271 (std: 0.177)
  xgb-m: R2 = -0.286 (std: 0.331)
  knn-m: R2 = -0.132 (std: 0.523)
  knn-tuned: R2 = -0.132 (std: 0.523)
  mlp-m: R2 = -0.981 (std: 1.055)
  svr-rbf: R2 = -0.058 (std: 0.262)
  svr-poly: R2 = -0.058 (std: 0.262)
  ridge: R2 = -0.183 (std: 0.206)

Model-based training with 7 models
Best R2: -0.058, Mean R2: -0.238
Running 2 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9710, entropy=1.3480, kl_div=0.0000
  Round 1/2: Mean predicted reward = 7.624
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9616, entropy=1.3408, kl_div=0.0000
  Round 2/2: Mean predicted reward = 7.478

  === Progress Analysis ===
  Status: WARNING
  • R2 scores negative. Models struggling to learn. Try collecting more diverse data.

--- Round 2 Results ---
  Mean Oracle Reward: 7.482
  Min Oracle Reward: 3.401
  Max Oracle Reward: 9.918
  Std Oracle Reward: 1.558
  Sequence Diversity: 1.000
  Models Used: 7
  Model R² - Mean: -0.238, Max: -0.058, Count: 11
  Total Sequences Evaluated: 114

======================================================================
EXPERIMENT ROUND 3/50
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.300
Total data collected: 114

--- Round 3 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  TGGTTGGG
  AATGGCCC
  CCTCGGAC
  TCCTGGTC
  TAGGACGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.749
  Max reward: 9.811
  With intrinsic bonuses: 7.902

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9746, entropy=1.3339, kl_div=0.0000
    Epoch 2: policy_loss=-0.0439, value_loss=0.9745, entropy=1.3241, kl_div=0.0467
    Early stopping at epoch 3: KL divergence = 0.0695

=== Surrogate Model Training ===
Total samples: 146

Training on 138 samples (removed 8 outliers)
Reward range: [4.83, 10.34], mean: 7.68
  Created 11 candidate models for data size 138
  rf-m: R2 = 0.095 (std: 0.159)
  rf-l: R2 = 0.080 (std: 0.184)
  gb-m: R2 = -0.053 (std: 0.249)
  gb-l: R2 = -0.067 (std: 0.266)
  xgb-m: R2 = -0.043 (std: 0.276)
  knn-m: R2 = -0.003 (std: 0.100)
  knn-tuned: R2 = -0.003 (std: 0.100)
  mlp-m: R2 = -0.769 (std: 0.605)
  svr-rbf: R2 = 0.089 (std: 0.122)
  svr-poly: R2 = 0.089 (std: 0.122)
  ridge: R2 = -0.034 (std: 0.106)

Model-based training with 10 models
Best R2: 0.095, Mean R2: -0.056
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9730, entropy=1.3214, kl_div=0.0000
    Epoch 1: policy_loss=-0.0122, value_loss=0.9730, entropy=1.3169, kl_div=0.0130
  Round 1/3: Mean predicted reward = 7.573
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9617, entropy=1.3121, kl_div=0.0000
    Epoch 1: policy_loss=-0.0117, value_loss=0.9618, entropy=1.3082, kl_div=0.0193
  Round 2/3: Mean predicted reward = 7.675
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9763, entropy=1.3074, kl_div=0.0000
    Epoch 1: policy_loss=-0.0117, value_loss=0.9762, entropy=1.3034, kl_div=0.0103
  Round 3/3: Mean predicted reward = 7.724

  === Progress Analysis ===
  Status: NORMAL

--- Round 3 Results ---
  Mean Oracle Reward: 7.763
  Min Oracle Reward: 4.062
  Max Oracle Reward: 10.242
  Std Oracle Reward: 1.159
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -0.056, Max: 0.095, Count: 11
  Total Sequences Evaluated: 146

======================================================================
EXPERIMENT ROUND 4/50
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.280
Total data collected: 146

--- Round 4 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0100
Exploration rate: 0.280

--- Generated Sequences (Diversity: 1.000) ---
  ACCGTTGA
  GAGATCTC
  GCCATGAT
  CTTGCAGA
  GGTCATAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.988
  Max reward: 9.749
  With intrinsic bonuses: 8.135

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9713, entropy=1.2989, kl_div=0.0000
    Epoch 1: policy_loss=-0.0041, value_loss=0.9712, entropy=1.2975, kl_div=0.0059
    Epoch 2: policy_loss=-0.0092, value_loss=0.9712, entropy=1.2963, kl_div=0.0112
    Epoch 3: policy_loss=-0.0152, value_loss=0.9712, entropy=1.2952, kl_div=0.0159

=== Surrogate Model Training ===
Total samples: 178

Training on 170 samples (removed 8 outliers)
Reward range: [4.83, 10.34], mean: 7.74
  Created 11 candidate models for data size 170
  rf-m: R2 = 0.097 (std: 0.077)
  rf-l: R2 = 0.123 (std: 0.098)
  gb-m: R2 = 0.017 (std: 0.166)
  gb-l: R2 = 0.021 (std: 0.163)
  xgb-m: R2 = -0.016 (std: 0.070)
  knn-m: R2 = 0.059 (std: 0.178)
  knn-tuned: R2 = 0.059 (std: 0.178)
  mlp-m: R2 = -0.656 (std: 0.375)
  svr-rbf: R2 = 0.120 (std: 0.053)
  svr-poly: R2 = 0.120 (std: 0.053)
  ridge: R2 = -0.019 (std: 0.023)

Model-based training with 8 models
Best R2: 0.123, Mean R2: -0.007
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9726, entropy=1.2922, kl_div=0.0000
    Epoch 1: policy_loss=-0.0033, value_loss=0.9726, entropy=1.2915, kl_div=0.0061
  Round 1/3: Mean predicted reward = 7.681
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9647, entropy=1.2900, kl_div=0.0000
    Epoch 1: policy_loss=-0.0022, value_loss=0.9647, entropy=1.2896, kl_div=0.0014
  Round 2/3: Mean predicted reward = 7.822
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9641, entropy=1.2905, kl_div=0.0000
    Epoch 1: policy_loss=-0.0037, value_loss=0.9641, entropy=1.2903, kl_div=0.0002
  Round 3/3: Mean predicted reward = 7.676

  === Progress Analysis ===
  Status: NORMAL

--- Round 4 Results ---
  Mean Oracle Reward: 7.974
  Min Oracle Reward: 5.325
  Max Oracle Reward: 9.799
  Std Oracle Reward: 1.025
  Sequence Diversity: 1.000
  Models Used: 8
  Model R² - Mean: -0.007, Max: 0.123, Count: 11
  Total Sequences Evaluated: 178

======================================================================
EXPERIMENT ROUND 5/50
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
  CGTCATAG
  AATCCGTG
  CCTGTGAA
  TCAGTACG
  GCAGATTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.147
  Max reward: 10.167
  With intrinsic bonuses: 8.235

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9656, entropy=1.2913, kl_div=0.0000
    Epoch 1: policy_loss=-0.0213, value_loss=0.9656, entropy=1.2908, kl_div=0.0036
    Epoch 2: policy_loss=-0.0486, value_loss=0.9657, entropy=1.2908, kl_div=0.0089
    Epoch 3: policy_loss=-0.0622, value_loss=0.9657, entropy=1.2905, kl_div=0.0201

=== Surrogate Model Training ===
Total samples: 210

Training on 202 samples (removed 8 outliers)
Reward range: [4.83, 10.34], mean: 7.80
  Created 11 candidate models for data size 202
  rf-m: R2 = 0.081 (std: 0.154)
  rf-l: R2 = 0.029 (std: 0.161)
  gb-m: R2 = -0.065 (std: 0.166)
  gb-l: R2 = -0.064 (std: 0.165)
  xgb-m: R2 = -0.027 (std: 0.185)
  knn-m: R2 = -0.060 (std: 0.193)
  knn-tuned: R2 = -0.060 (std: 0.193)
  mlp-m: R2 = -0.758 (std: 0.555)
  svr-rbf: R2 = 0.042 (std: 0.162)
  svr-poly: R2 = 0.042 (std: 0.162)
  ridge: R2 = -0.093 (std: 0.103)

Model-based training with 4 models
Best R2: 0.081, Mean R2: -0.085
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9714, entropy=1.2907, kl_div=0.0000
    Epoch 1: policy_loss=-0.0213, value_loss=0.9714, entropy=1.2898, kl_div=0.0098
  Round 1/3: Mean predicted reward = 7.773
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=1.2893, kl_div=0.0000
    Epoch 1: policy_loss=-0.0246, value_loss=0.9685, entropy=1.2850, kl_div=0.0357
  Round 2/3: Mean predicted reward = 7.751
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9665, entropy=1.2772, kl_div=0.0000
    Epoch 1: policy_loss=-0.0337, value_loss=0.9665, entropy=1.2712, kl_div=0.0301
  Round 3/3: Mean predicted reward = 7.712

  === Progress Analysis ===
  Status: NORMAL

--- Round 5 Results ---
  Mean Oracle Reward: 8.155
  Min Oracle Reward: 5.629
  Max Oracle Reward: 9.988
  Std Oracle Reward: 0.924
  Sequence Diversity: 1.000
  Models Used: 4
  Model R² - Mean: -0.085, Max: 0.081, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 210

======================================================================
EXPERIMENT ROUND 6/50
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
  TTCCAGAG
  TCCAGGAT
  GCCATATG
  ATATCGGC
  GGTTACAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.798
  Max reward: 9.918
  With intrinsic bonuses: 7.916

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=1.2702, kl_div=0.0000
    Epoch 1: policy_loss=-0.0226, value_loss=0.9696, entropy=1.2670, kl_div=0.0172
    Epoch 2: policy_loss=-0.0550, value_loss=0.9696, entropy=1.2659, kl_div=0.0193
    Epoch 3: policy_loss=-0.0906, value_loss=0.9696, entropy=1.2681, kl_div=0.0029

=== Surrogate Model Training ===
Total samples: 242

Training on 234 samples (removed 8 outliers)
Reward range: [4.79, 10.34], mean: 7.80
  Created 11 candidate models for data size 234
  rf-m: R2 = 0.067 (std: 0.094)
  rf-l: R2 = 0.043 (std: 0.097)
  gb-m: R2 = 0.076 (std: 0.177)
  gb-l: R2 = 0.083 (std: 0.176)
  xgb-m: R2 = 0.019 (std: 0.093)
  knn-m: R2 = 0.040 (std: 0.174)
  knn-tuned: R2 = 0.040 (std: 0.174)
  mlp-m: R2 = -0.651 (std: 0.367)
  svr-rbf: R2 = 0.053 (std: 0.078)
  svr-poly: R2 = 0.053 (std: 0.078)
  ridge: R2 = -0.047 (std: 0.075)

Model-based training with 9 models
Best R2: 0.083, Mean R2: -0.020
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9654, entropy=1.2672, kl_div=0.0000
    Epoch 1: policy_loss=-0.0543, value_loss=0.9655, entropy=1.2732, kl_div=-0.0339
  Round 1/3: Mean predicted reward = 7.772
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9735, entropy=1.2761, kl_div=0.0000
    Epoch 1: policy_loss=-0.0074, value_loss=0.9734, entropy=1.2795, kl_div=-0.0197
  Round 2/3: Mean predicted reward = 7.813
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9761, entropy=1.2824, kl_div=0.0000
    Epoch 1: policy_loss=-0.0331, value_loss=0.9760, entropy=1.2804, kl_div=0.0134
  Round 3/3: Mean predicted reward = 7.870

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 6 Results ---
  Mean Oracle Reward: 7.819
  Min Oracle Reward: 5.022
  Max Oracle Reward: 10.026
  Std Oracle Reward: 1.068
  Sequence Diversity: 1.000
  Models Used: 9
  Model R² - Mean: -0.020, Max: 0.083, Count: 11
  Total Sequences Evaluated: 242

======================================================================
EXPERIMENT ROUND 7/50
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.190
Total data collected: 242

--- Round 7 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0100
Exploration rate: 0.190

--- Generated Sequences (Diversity: 1.000) ---
  ACGGTAAT
  TAGTGAAC
  ACCTTAGG
  CTACATGG
  GATATCCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.103
  Max reward: 12.214
  With intrinsic bonuses: 8.157

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9662, entropy=1.2753, kl_div=0.0000
    Epoch 1: policy_loss=-0.0265, value_loss=0.9662, entropy=1.2748, kl_div=0.0013
    Epoch 2: policy_loss=-0.0603, value_loss=0.9662, entropy=1.2758, kl_div=-0.0049
    Epoch 3: policy_loss=-0.0810, value_loss=0.9662, entropy=1.2782, kl_div=-0.0214

=== Surrogate Model Training ===
Total samples: 274

Training on 264 samples (removed 10 outliers)
Reward range: [4.75, 10.34], mean: 7.83
  Created 11 candidate models for data size 264
  rf-m: R2 = 0.059 (std: 0.058)
  rf-l: R2 = 0.060 (std: 0.087)
  gb-m: R2 = 0.030 (std: 0.101)
  gb-l: R2 = 0.030 (std: 0.101)
  xgb-m: R2 = 0.017 (std: 0.119)
  knn-m: R2 = 0.047 (std: 0.176)
  knn-tuned: R2 = 0.047 (std: 0.176)
  mlp-m: R2 = -0.303 (std: 0.235)
  svr-rbf: R2 = 0.079 (std: 0.102)
  svr-poly: R2 = 0.079 (std: 0.102)
  ridge: R2 = -0.061 (std: 0.052)

Model-based training with 9 models
Best R2: 0.079, Mean R2: 0.007
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9720, entropy=1.2825, kl_div=0.0000
    Epoch 1: policy_loss=-0.0175, value_loss=0.9719, entropy=1.2828, kl_div=-0.0017
  Round 1/3: Mean predicted reward = 7.800
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9744, entropy=1.2799, kl_div=0.0000
    Epoch 1: policy_loss=-0.0369, value_loss=0.9744, entropy=1.2772, kl_div=0.0118
  Round 2/3: Mean predicted reward = 7.822
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9645, entropy=1.2788, kl_div=0.0000
    Epoch 1: policy_loss=-0.0353, value_loss=0.9645, entropy=1.2754, kl_div=0.0119
  Round 3/3: Mean predicted reward = 7.911

  === Progress Analysis ===
  Status: NORMAL

--- Round 7 Results ---
  Mean Oracle Reward: 8.094
  Min Oracle Reward: 3.832
  Max Oracle Reward: 11.960
  Std Oracle Reward: 1.420
  Sequence Diversity: 1.000
  Models Used: 9
  Model R² - Mean: 0.007, Max: 0.079, Count: 11
  Total Sequences Evaluated: 274

======================================================================
EXPERIMENT ROUND 8/50
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.080
Total data collected: 274

--- Round 8 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.080

--- Generated Sequences (Diversity: 1.000) ---
  CAGAGTTA
  CCTAGGAT
  GCTATAAG
  ATCCTAGG
  TGCCTGAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.302
  Max reward: 9.779
  With intrinsic bonuses: 8.336

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9668, entropy=1.2648, kl_div=0.0000
    Epoch 1: policy_loss=-0.0174, value_loss=0.9668, entropy=1.2619, kl_div=0.0114

=== Surrogate Model Training ===
Total samples: 306

Training on 294 samples (removed 12 outliers)
Reward range: [4.83, 10.34], mean: 7.90
  Created 11 candidate models for data size 294
  rf-m: R2 = 0.057 (std: 0.078)
  rf-l: R2 = 0.063 (std: 0.069)
  gb-m: R2 = 0.066 (std: 0.095)
  gb-l: R2 = 0.067 (std: 0.096)
  xgb-m: R2 = 0.000 (std: 0.166)
  knn-m: R2 = 0.024 (std: 0.153)
  knn-tuned: R2 = 0.024 (std: 0.153)
  mlp-m: R2 = -0.487 (std: 0.383)
  svr-rbf: R2 = 0.064 (std: 0.072)
  svr-poly: R2 = 0.064 (std: 0.072)
  ridge: R2 = -0.088 (std: 0.111)

Model-based training with 9 models
Best R2: 0.067, Mean R2: -0.013
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9646, entropy=1.2591, kl_div=0.0000
    Epoch 1: policy_loss=-0.0338, value_loss=0.9646, entropy=1.2557, kl_div=0.0260
  Round 1/3: Mean predicted reward = 7.741
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9679, entropy=1.2587, kl_div=0.0000
    Epoch 1: policy_loss=-0.0280, value_loss=0.9679, entropy=1.2551, kl_div=0.0266
  Round 2/3: Mean predicted reward = 7.744
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=1.2408, kl_div=0.0000
    Epoch 1: policy_loss=-0.0136, value_loss=0.9678, entropy=1.2362, kl_div=0.0230
  Round 3/3: Mean predicted reward = 7.936

  === Progress Analysis ===
  Status: NORMAL

--- Round 8 Results ---
  Mean Oracle Reward: 8.326
  Min Oracle Reward: 5.487
  Max Oracle Reward: 9.594
  Std Oracle Reward: 1.016
  Sequence Diversity: 1.000
  Models Used: 9
  Model R² - Mean: -0.013, Max: 0.067, Count: 11
  New best mean reward!
  Total Sequences Evaluated: 306

======================================================================
EXPERIMENT ROUND 9/50
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
  CAACTTGG
  ACGGAATT
  TTGCGAAC
  AGAAGCTT
  ACGCTTAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.908
  Max reward: 9.482
  With intrinsic bonuses: 7.944

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=1.2413, kl_div=0.0000
    Epoch 1: policy_loss=-0.0146, value_loss=0.9689, entropy=1.2395, kl_div=0.0163

=== Surrogate Model Training ===
Total samples: 338

Training on 325 samples (removed 13 outliers)
Reward range: [4.96, 10.34], mean: 7.91
  Created 14 candidate models for data size 325
  rf-tuned-l: R2 = 0.151 (std: 0.080)
  rf-tuned-xl: R2 = 0.162 (std: 0.059)
  gb-tuned-l: R2 = 0.149 (std: 0.057)
  gb-tuned-xl: R2 = 0.149 (std: 0.057)
  xgb-xl: R2 = 0.147 (std: 0.129)
  xgb-l: R2 = 0.147 (std: 0.129)
  mlp-adaptive-xl: R2 = -0.235 (std: 0.309)
  mlp-l: R2 = -0.210 (std: 0.144)
  svr-rbf-xl: R2 = 0.164 (std: 0.053)
  svr-poly-l: R2 = 0.164 (std: 0.053)
  knn-tuned-sqrt: R2 = 0.115 (std: 0.088)
  knn-tuned-l: R2 = 0.115 (std: 0.088)
  ridge: R2 = -0.034 (std: 0.066)
  gp: R2 = -59.745 (std: 13.572)

Model-based training with 10 models
Best R2: 0.164, Mean R2: -4.197
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9682, entropy=1.2352, kl_div=0.0000
    Epoch 1: policy_loss=-0.0074, value_loss=0.9682, entropy=1.2330, kl_div=0.0151
  Round 1/3: Mean predicted reward = 7.787
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9686, entropy=1.2369, kl_div=0.0000
    Epoch 1: policy_loss=-0.0066, value_loss=0.9686, entropy=1.2351, kl_div=0.0033
  Round 2/3: Mean predicted reward = 7.933
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9657, entropy=1.2226, kl_div=0.0000
    Epoch 1: policy_loss=-0.0176, value_loss=0.9657, entropy=1.2199, kl_div=0.0238
  Round 3/3: Mean predicted reward = 7.888

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 9 Results ---
  Mean Oracle Reward: 7.958
  Min Oracle Reward: 5.671
  Max Oracle Reward: 9.570
  Std Oracle Reward: 1.030
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -4.197, Max: 0.164, Count: 14
  Total Sequences Evaluated: 338

======================================================================
EXPERIMENT ROUND 10/50
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 338

--- Round 10 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTCGGTAA
  GAAAGTCT
  TTAGACGC
  TAGCCTAG
  GTGACTCA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.080
  Max reward: 10.299
  With intrinsic bonuses: 8.135

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9643, entropy=1.2280, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1382

=== Surrogate Model Training ===
Total samples: 370

Training on 355 samples (removed 15 outliers)
Reward range: [5.02, 10.34], mean: 7.96
  Created 14 candidate models for data size 355
  rf-tuned-l: R2 = 0.184 (std: 0.063)
  rf-tuned-xl: R2 = 0.189 (std: 0.076)
  gb-tuned-l: R2 = 0.167 (std: 0.104)
  gb-tuned-xl: R2 = 0.167 (std: 0.104)
  xgb-xl: R2 = 0.113 (std: 0.056)
  xgb-l: R2 = 0.113 (std: 0.056)
  mlp-adaptive-xl: R2 = -0.092 (std: 0.115)
  mlp-l: R2 = -0.023 (std: 0.130)
  svr-rbf-xl: R2 = 0.209 (std: 0.084)
  svr-poly-l: R2 = 0.209 (std: 0.084)
  knn-tuned-sqrt: R2 = 0.148 (std: 0.109)
  knn-tuned-l: R2 = 0.148 (std: 0.109)
  ridge: R2 = -0.037 (std: 0.081)
  gp: R2 = -60.468 (std: 9.938)

Model-based training with 10 models
Best R2: 0.209, Mean R2: -4.212
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9647, entropy=1.2111, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1675
  Round 1/3: Mean predicted reward = 7.728
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=1.1953, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1407
  Round 2/3: Mean predicted reward = 7.877
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9703, entropy=1.1746, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2282
  Round 3/3: Mean predicted reward = 8.002

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 10 Results ---
  Mean Oracle Reward: 8.125
  Min Oracle Reward: 0.448
  Max Oracle Reward: 10.117
  Std Oracle Reward: 1.630
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -4.212, Max: 0.209, Count: 14
  Total Sequences Evaluated: 370

======================================================================
EXPERIMENT ROUND 11/50
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 370

--- Round 11 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AACGTCGT
  TATCCGGA
  AGTCCAGT
  TGATCCGA
  GTGCTAAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.140
  Max reward: 9.582
  With intrinsic bonuses: 8.175

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=1.1191, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2120

=== Surrogate Model Training ===
Total samples: 402

Training on 385 samples (removed 17 outliers)
Reward range: [5.26, 10.34], mean: 7.99
  Created 14 candidate models for data size 385
  rf-tuned-l: R2 = 0.184 (std: 0.107)
  rf-tuned-xl: R2 = 0.175 (std: 0.093)
  gb-tuned-l: R2 = 0.185 (std: 0.144)
  gb-tuned-xl: R2 = 0.186 (std: 0.144)
  xgb-xl: R2 = 0.118 (std: 0.159)
  xgb-l: R2 = 0.118 (std: 0.159)
  mlp-adaptive-xl: R2 = -0.147 (std: 0.189)
  mlp-l: R2 = -0.125 (std: 0.152)
  svr-rbf-xl: R2 = 0.223 (std: 0.117)
  svr-poly-l: R2 = 0.223 (std: 0.117)
  knn-tuned-sqrt: R2 = 0.160 (std: 0.101)
  knn-tuned-l: R2 = 0.160 (std: 0.101)
  ridge: R2 = -0.016 (std: 0.071)
  gp: R2 = -64.800 (std: 12.576)

Model-based training with 10 models
Best R2: 0.223, Mean R2: -4.526
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9717, entropy=1.1041, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2325
  Round 1/3: Mean predicted reward = 7.733
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9632, entropy=1.0577, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3046
  Round 2/3: Mean predicted reward = 7.892
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=1.0623, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3604
  Round 3/3: Mean predicted reward = 7.786

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 11 Results ---
  Mean Oracle Reward: 8.158
  Min Oracle Reward: 5.154
  Max Oracle Reward: 9.586
  Std Oracle Reward: 0.916
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -4.526, Max: 0.223, Count: 14
  Total Sequences Evaluated: 402

======================================================================
EXPERIMENT ROUND 12/50
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 402
  Performance plateaued, reducing LR to 0.000100

--- Round 12 Configuration ---
Learning rate: 0.000100
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGTATGCA
  TAGCAGTC
  CACTGTAG
  ATATGGCA
  GAGTTACC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.242
  Max reward: 10.256
  With intrinsic bonuses: 8.251

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9669, entropy=1.0064, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1170

=== Surrogate Model Training ===
Total samples: 434

Training on 417 samples (removed 17 outliers)
Reward range: [5.26, 10.34], mean: 8.01
  Created 14 candidate models for data size 417
  rf-tuned-l: R2 = 0.177 (std: 0.031)
  rf-tuned-xl: R2 = 0.165 (std: 0.026)
  gb-tuned-l: R2 = 0.182 (std: 0.052)
  gb-tuned-xl: R2 = 0.182 (std: 0.052)
  xgb-xl: R2 = 0.128 (std: 0.081)
  xgb-l: R2 = 0.128 (std: 0.081)
  mlp-adaptive-xl: R2 = -0.036 (std: 0.166)
  mlp-l: R2 = -0.048 (std: 0.192)
  svr-rbf-xl: R2 = 0.231 (std: 0.055)
  svr-poly-l: R2 = 0.231 (std: 0.055)
  knn-tuned-sqrt: R2 = 0.117 (std: 0.051)
  knn-tuned-l: R2 = 0.117 (std: 0.051)
  ridge: R2 = -0.008 (std: 0.052)
  gp: R2 = -67.509 (std: 15.210)

Model-based training with 10 models
Best R2: 0.231, Mean R2: -4.710
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9656, entropy=0.9922, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1111
  Round 1/3: Mean predicted reward = 7.786
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9652, entropy=1.0012, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1324
  Round 2/3: Mean predicted reward = 7.763
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9627, entropy=0.9683, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0967
  Round 3/3: Mean predicted reward = 8.208

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 12 Results ---
  Mean Oracle Reward: 8.254
  Min Oracle Reward: 6.002
  Max Oracle Reward: 10.147
  Std Oracle Reward: 0.897
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -4.710, Max: 0.231, Count: 14
  Total Sequences Evaluated: 434

======================================================================
EXPERIMENT ROUND 13/50
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
  TACGTGAA
  ATCAGTCG
  GCATATAG
  GTTGCAAC
  CCATTGAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.273
  Max reward: 10.483
  With intrinsic bonuses: 8.232

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.9684, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0572

=== Surrogate Model Training ===
Total samples: 466

Training on 448 samples (removed 18 outliers)
Reward range: [5.26, 10.62], mean: 8.04
  Created 14 candidate models for data size 448
  rf-tuned-l: R2 = 0.128 (std: 0.122)
  rf-tuned-xl: R2 = 0.110 (std: 0.105)
  gb-tuned-l: R2 = 0.140 (std: 0.125)
  gb-tuned-xl: R2 = 0.139 (std: 0.125)
  xgb-xl: R2 = 0.048 (std: 0.223)
  xgb-l: R2 = 0.048 (std: 0.223)
  mlp-adaptive-xl: R2 = -0.121 (std: 0.248)
  mlp-l: R2 = -0.238 (std: 0.256)
  svr-rbf-xl: R2 = 0.192 (std: 0.106)
  svr-poly-l: R2 = 0.192 (std: 0.106)
  knn-tuned-sqrt: R2 = 0.041 (std: 0.189)
  knn-tuned-l: R2 = 0.041 (std: 0.189)
  ridge: R2 = -0.019 (std: 0.052)
  gp: R2 = -68.130 (std: 15.780)

Model-based training with 10 models
Best R2: 0.192, Mean R2: -4.816
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=0.9763, kl_div=0.0000
    Epoch 1: policy_loss=0.0010, value_loss=0.9704, entropy=0.9717, kl_div=0.0472
  Round 1/3: Mean predicted reward = 7.499
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9718, entropy=0.9548, kl_div=0.0000
    Epoch 1: policy_loss=-0.0198, value_loss=0.9718, entropy=0.9519, kl_div=0.0308
  Round 2/3: Mean predicted reward = 7.770
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9684, entropy=0.9775, kl_div=0.0000
    Epoch 1: policy_loss=-0.0225, value_loss=0.9684, entropy=0.9754, kl_div=0.0306
  Round 3/3: Mean predicted reward = 7.954

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 13 Results ---
  Mean Oracle Reward: 8.267
  Min Oracle Reward: 4.469
  Max Oracle Reward: 10.934
  Std Oracle Reward: 1.136
  Sequence Diversity: 1.000
  Models Used: 10
  Model R² - Mean: -4.816, Max: 0.192, Count: 14
  Total Sequences Evaluated: 466

======================================================================
EXPERIMENT ROUND 14/50
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
  CGATGACT
  AGGATCTC
  GATCGCTA
  GTCAACTG
  TGTAGACC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.194
  Max reward: 10.713
  With intrinsic bonuses: 8.236

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9668, entropy=0.9633, kl_div=0.0000
    Epoch 1: policy_loss=-0.0029, value_loss=0.9668, entropy=0.9626, kl_div=0.0060

=== Surrogate Model Training ===
Total samples: 498

Training on 480 samples (removed 18 outliers)
Reward range: [5.26, 10.62], mean: 8.05
  Created 14 candidate models for data size 480
  rf-tuned-l: R2 = 0.211 (std: 0.072)
  rf-tuned-xl: R2 = 0.209 (std: 0.084)
  gb-tuned-l: R2 = 0.200 (std: 0.112)
  gb-tuned-xl: R2 = 0.201 (std: 0.112)
  xgb-xl: R2 = 0.169 (std: 0.168)
  xgb-l: R2 = 0.169 (std: 0.168)
  mlp-adaptive-xl: R2 = -0.052 (std: 0.095)
  mlp-l: R2 = -0.014 (std: 0.184)
  svr-rbf-xl: R2 = 0.245 (std: 0.093)
  svr-poly-l: R2 = 0.245 (std: 0.093)
  knn-tuned-sqrt: R2 = 0.128 (std: 0.123)
  knn-tuned-l: R2 = 0.128 (std: 0.123)
  ridge: R2 = 0.002 (std: 0.060)
  gp: R2 = -64.706 (std: 9.139)

Model-based training with 11 models
Best R2: 0.245, Mean R2: -4.490
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9719, entropy=0.9335, kl_div=0.0000
    Epoch 1: policy_loss=-0.0049, value_loss=0.9719, entropy=0.9332, kl_div=0.0032
  Round 1/3: Mean predicted reward = 7.507
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.9512, kl_div=0.0000
    Epoch 1: policy_loss=-0.0043, value_loss=0.9697, entropy=0.9515, kl_div=-0.0033
  Round 2/3: Mean predicted reward = 7.724
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9671, entropy=0.9595, kl_div=0.0000
    Epoch 1: policy_loss=-0.0017, value_loss=0.9671, entropy=0.9595, kl_div=0.0003
  Round 3/3: Mean predicted reward = 7.956

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 14 Results ---
  Mean Oracle Reward: 8.218
  Min Oracle Reward: 5.232
  Max Oracle Reward: 10.555
  Std Oracle Reward: 1.209
  Sequence Diversity: 1.000
  Models Used: 11
  Model R² - Mean: -4.490, Max: 0.245, Count: 14
  Total Sequences Evaluated: 498

======================================================================
EXPERIMENT ROUND 15/50
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
  CGTTGACA
  GTACAGCT
  GACGCTAT
  AGCATTCG
  AGACTCGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.224
  Max reward: 10.359
  With intrinsic bonuses: 8.167

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9732, entropy=0.9691, kl_div=0.0000
    Epoch 1: policy_loss=-0.0612, value_loss=0.9731, entropy=0.9681, kl_div=0.0432

=== Surrogate Model Training ===
Total samples: 530

Training on 512 samples (removed 18 outliers)
Reward range: [5.26, 10.62], mean: 8.06
  Created 13 candidate models for data size 512
  rf-tuned-l: R2 = 0.229 (std: 0.067)
  rf-tuned-xl: R2 = 0.222 (std: 0.048)
  gb-tuned-l: R2 = 0.216 (std: 0.082)
  gb-tuned-xl: R2 = 0.216 (std: 0.082)
  xgb-xl: R2 = 0.230 (std: 0.110)
  xgb-l: R2 = 0.230 (std: 0.110)
  mlp-adaptive-xl: R2 = 0.002 (std: 0.146)
  mlp-l: R2 = 0.060 (std: 0.073)
  svr-rbf-xl: R2 = 0.285 (std: 0.067)
  svr-poly-l: R2 = 0.285 (std: 0.067)
  knn-tuned-sqrt: R2 = 0.146 (std: 0.069)
  knn-tuned-l: R2 = 0.146 (std: 0.069)
  ridge: R2 = 0.008 (std: 0.066)

Model-based training with 13 models
Best R2: 0.285, Mean R2: 0.175
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9718, entropy=0.9600, kl_div=0.0000
    Epoch 1: policy_loss=-0.0548, value_loss=0.9718, entropy=0.9637, kl_div=-0.0267
  Round 1/3: Mean predicted reward = 7.578
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9655, entropy=0.9749, kl_div=0.0000
    Epoch 1: policy_loss=-0.0563, value_loss=0.9655, entropy=0.9805, kl_div=-0.0126
  Round 2/3: Mean predicted reward = 7.748
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=0.9784, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0534
  Round 3/3: Mean predicted reward = 7.958

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 15 Results ---
  Mean Oracle Reward: 8.195
  Min Oracle Reward: 5.215
  Max Oracle Reward: 10.461
  Std Oracle Reward: 1.045
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.175, Max: 0.285, Count: 13
  Total Sequences Evaluated: 530

======================================================================
EXPERIMENT ROUND 16/50
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 530
  Performance plateaued, reducing LR to 0.000136

--- Round 16 Configuration ---
Learning rate: 0.000136
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ATAGTCAG
  AAGAGTTC
  ACTCTGAG
  GGACAATT
  AGATACGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.102
  Max reward: 10.420
  With intrinsic bonuses: 8.139

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9632, entropy=0.9313, kl_div=0.0000
    Epoch 1: policy_loss=0.0028, value_loss=0.9633, entropy=0.9271, kl_div=0.0300

=== Surrogate Model Training ===
Total samples: 562

Training on 543 samples (removed 19 outliers)
Reward range: [5.26, 10.62], mean: 8.07
  Created 13 candidate models for data size 543
  rf-tuned-l: R2 = 0.235 (std: 0.085)
  rf-tuned-xl: R2 = 0.230 (std: 0.076)
  gb-tuned-l: R2 = 0.254 (std: 0.051)
  gb-tuned-xl: R2 = 0.254 (std: 0.051)
  xgb-xl: R2 = 0.231 (std: 0.125)
  xgb-l: R2 = 0.231 (std: 0.125)
  mlp-adaptive-xl: R2 = 0.068 (std: 0.206)
  mlp-l: R2 = 0.088 (std: 0.101)
  svr-rbf-xl: R2 = 0.310 (std: 0.047)
  svr-poly-l: R2 = 0.310 (std: 0.047)
  knn-tuned-sqrt: R2 = 0.157 (std: 0.072)
  knn-tuned-l: R2 = 0.157 (std: 0.072)
  ridge: R2 = -0.000 (std: 0.054)

Model-based training with 12 models
Best R2: 0.310, Mean R2: 0.194
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.9609, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1033
  Round 1/5: Mean predicted reward = 7.547
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9706, entropy=0.9274, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1310
  Round 2/5: Mean predicted reward = 7.704
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9660, entropy=0.9295, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1298
  Round 3/5: Mean predicted reward = 7.746
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9686, entropy=0.9451, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1538
  Round 4/5: Mean predicted reward = 7.987
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.9089, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1384
  Round 5/5: Mean predicted reward = 8.085

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 16 Results ---
  Mean Oracle Reward: 8.121
  Min Oracle Reward: 4.265
  Max Oracle Reward: 10.243
  Std Oracle Reward: 1.196
  Sequence Diversity: 1.000
  Models Used: 12
  Model R² - Mean: 0.194, Max: 0.310, Count: 13
  Total Sequences Evaluated: 562

======================================================================
EXPERIMENT ROUND 17/50
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
  ACCGTGAT
  ACGTGATA
  CAAGCGTT
  ATTGAACG
  ATGAGACT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.160
  Max reward: 10.356
  With intrinsic bonuses: 8.172

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9700, entropy=0.8836, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1348

=== Surrogate Model Training ===
Total samples: 594

Training on 574 samples (removed 20 outliers)
Reward range: [5.32, 10.62], mean: 8.08
  Created 13 candidate models for data size 574
  rf-tuned-l: R2 = 0.193 (std: 0.101)
  rf-tuned-xl: R2 = 0.197 (std: 0.094)
  gb-tuned-l: R2 = 0.204 (std: 0.111)
  gb-tuned-xl: R2 = 0.204 (std: 0.111)
  xgb-xl: R2 = 0.261 (std: 0.168)
  xgb-l: R2 = 0.261 (std: 0.168)
  mlp-adaptive-xl: R2 = 0.073 (std: 0.111)
  mlp-l: R2 = 0.116 (std: 0.131)
  svr-rbf-xl: R2 = 0.296 (std: 0.074)
  svr-poly-l: R2 = 0.296 (std: 0.074)
  knn-tuned-sqrt: R2 = 0.088 (std: 0.127)
  knn-tuned-l: R2 = 0.088 (std: 0.127)
  ridge: R2 = -0.008 (std: 0.045)

Model-based training with 12 models
Best R2: 0.296, Mean R2: 0.175
Running 3 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.8821, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1249
  Round 1/3: Mean predicted reward = 7.509
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9734, entropy=0.8928, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0606
  Round 2/3: Mean predicted reward = 7.724
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9700, entropy=0.8686, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1306
  Round 3/3: Mean predicted reward = 7.992

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 17 Results ---
  Mean Oracle Reward: 8.245
  Min Oracle Reward: 5.698
  Max Oracle Reward: 10.298
  Std Oracle Reward: 0.917
  Sequence Diversity: 1.000
  Models Used: 12
  Model R² - Mean: 0.175, Max: 0.296, Count: 13
  Total Sequences Evaluated: 594

======================================================================
EXPERIMENT ROUND 18/50
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 594
  Performance plateaued, reducing LR to 0.000055

--- Round 18 Configuration ---
Learning rate: 0.000055
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GACGATTC
  GCTAGAAT
  TAAGGATC
  TAATGGAC
  ATTGGCAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.170
  Max reward: 10.611
  With intrinsic bonuses: 8.105

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.8588, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0535

=== Surrogate Model Training ===
Total samples: 626

Training on 603 samples (removed 23 outliers)
Reward range: [5.34, 10.62], mean: 8.09
  Created 13 candidate models for data size 603
  rf-tuned-l: R2 = 0.222 (std: 0.078)
  rf-tuned-xl: R2 = 0.235 (std: 0.082)
  gb-tuned-l: R2 = 0.222 (std: 0.072)
  gb-tuned-xl: R2 = 0.222 (std: 0.072)
  xgb-xl: R2 = 0.254 (std: 0.044)
  xgb-l: R2 = 0.254 (std: 0.044)
  mlp-adaptive-xl: R2 = 0.086 (std: 0.130)
  mlp-l: R2 = 0.158 (std: 0.132)
  svr-rbf-xl: R2 = 0.310 (std: 0.080)
  svr-poly-l: R2 = 0.310 (std: 0.080)
  knn-tuned-sqrt: R2 = 0.123 (std: 0.122)
  knn-tuned-l: R2 = 0.123 (std: 0.122)
  ridge: R2 = -0.003 (std: 0.042)

Model-based training with 12 models
Best R2: 0.310, Mean R2: 0.194
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9718, entropy=0.8449, kl_div=0.0000
    Epoch 1: policy_loss=-0.0068, value_loss=0.9718, entropy=0.8433, kl_div=0.0304
  Round 1/5: Mean predicted reward = 7.329
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9707, entropy=0.8868, kl_div=0.0000
    Epoch 1: policy_loss=-0.0128, value_loss=0.9707, entropy=0.8877, kl_div=-0.0162
  Round 2/5: Mean predicted reward = 7.530
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9657, entropy=0.8503, kl_div=0.0000
    Epoch 1: policy_loss=-0.0033, value_loss=0.9657, entropy=0.8506, kl_div=-0.0095
  Round 3/5: Mean predicted reward = 7.774
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9720, entropy=0.8642, kl_div=0.0000
    Epoch 1: policy_loss=-0.0111, value_loss=0.9720, entropy=0.8623, kl_div=0.0268
  Round 4/5: Mean predicted reward = 7.933
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.8556, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0564
  Round 5/5: Mean predicted reward = 8.131

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 18 Results ---
  Mean Oracle Reward: 8.175
  Min Oracle Reward: 3.082
  Max Oracle Reward: 10.700
  Std Oracle Reward: 1.348
  Sequence Diversity: 1.000
  Models Used: 12
  Model R² - Mean: 0.194, Max: 0.310, Count: 13
  Total Sequences Evaluated: 626

======================================================================
EXPERIMENT ROUND 19/50
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
  GCCAGTAT
  TGAAGCCT
  AATGTCGC
  TACAAGTG
  CGTCGTAA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.027
  Max reward: 10.750
  With intrinsic bonuses: 8.023

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9700, entropy=0.8520, kl_div=0.0000
    Epoch 1: policy_loss=-0.0065, value_loss=0.9700, entropy=0.8509, kl_div=0.0162

=== Surrogate Model Training ===
Total samples: 658

Training on 632 samples (removed 26 outliers)
Reward range: [5.39, 10.62], mean: 8.10
  Created 13 candidate models for data size 632
  rf-tuned-l: R2 = 0.231 (std: 0.100)
  rf-tuned-xl: R2 = 0.239 (std: 0.086)
  gb-tuned-l: R2 = 0.227 (std: 0.086)
  gb-tuned-xl: R2 = 0.227 (std: 0.086)
  xgb-xl: R2 = 0.244 (std: 0.108)
  xgb-l: R2 = 0.244 (std: 0.108)
  mlp-adaptive-xl: R2 = 0.107 (std: 0.116)
  mlp-l: R2 = 0.112 (std: 0.118)
  svr-rbf-xl: R2 = 0.315 (std: 0.089)
  svr-poly-l: R2 = 0.315 (std: 0.089)
  knn-tuned-sqrt: R2 = 0.121 (std: 0.123)
  knn-tuned-l: R2 = 0.121 (std: 0.123)
  ridge: R2 = 0.005 (std: 0.059)

Model-based training with 13 models
Best R2: 0.315, Mean R2: 0.193
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9732, entropy=0.8483, kl_div=0.0000
    Epoch 1: policy_loss=0.0024, value_loss=0.9732, entropy=0.8478, kl_div=0.0080
  Round 1/5: Mean predicted reward = 7.166
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9722, entropy=0.8758, kl_div=0.0000
    Epoch 1: policy_loss=-0.0035, value_loss=0.9722, entropy=0.8761, kl_div=-0.0067
  Round 2/5: Mean predicted reward = 7.496
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9700, entropy=0.8464, kl_div=0.0000
    Epoch 1: policy_loss=-0.0129, value_loss=0.9700, entropy=0.8473, kl_div=-0.0131
  Round 3/5: Mean predicted reward = 7.549
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.8563, kl_div=0.0000
    Epoch 1: policy_loss=-0.0033, value_loss=0.9681, entropy=0.8573, kl_div=-0.0166
  Round 4/5: Mean predicted reward = 7.874
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.8635, kl_div=0.0000
    Epoch 1: policy_loss=-0.0054, value_loss=0.9691, entropy=0.8640, kl_div=-0.0096
  Round 5/5: Mean predicted reward = 8.011

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 19 Results ---
  Mean Oracle Reward: 8.069
  Min Oracle Reward: 4.544
  Max Oracle Reward: 10.350
  Std Oracle Reward: 1.278
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.193, Max: 0.315, Count: 13
  Total Sequences Evaluated: 658

======================================================================
EXPERIMENT ROUND 20/50
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
  AACTCGGG
  CGGCAATT
  CTACATGG
  AGCCTGAG
  CATGCGTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.126
  Max reward: 9.420
  With intrinsic bonuses: 8.083

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.8314, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0597

=== Surrogate Model Training ===
Total samples: 690

Training on 662 samples (removed 28 outliers)
Reward range: [5.47, 10.62], mean: 8.12
  Created 13 candidate models for data size 662
  rf-tuned-l: R2 = 0.225 (std: 0.060)
  rf-tuned-xl: R2 = 0.225 (std: 0.073)
  gb-tuned-l: R2 = 0.224 (std: 0.081)
  gb-tuned-xl: R2 = 0.224 (std: 0.081)
  xgb-xl: R2 = 0.257 (std: 0.098)
  xgb-l: R2 = 0.257 (std: 0.098)
  mlp-adaptive-xl: R2 = 0.104 (std: 0.051)
  mlp-l: R2 = 0.082 (std: 0.136)
  svr-rbf-xl: R2 = 0.319 (std: 0.072)
  svr-poly-l: R2 = 0.319 (std: 0.072)
  knn-tuned-sqrt: R2 = 0.124 (std: 0.120)
  knn-tuned-l: R2 = 0.124 (std: 0.120)
  ridge: R2 = 0.004 (std: 0.059)

Model-based training with 13 models
Best R2: 0.319, Mean R2: 0.191
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.8596, kl_div=0.0000
    Epoch 1: policy_loss=0.0160, value_loss=0.9698, entropy=0.8594, kl_div=0.0051
  Round 1/5: Mean predicted reward = 7.118
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9710, entropy=0.8840, kl_div=0.0000
    Epoch 1: policy_loss=-0.0448, value_loss=0.9710, entropy=0.8869, kl_div=-0.0256
  Round 2/5: Mean predicted reward = 7.334
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9679, entropy=0.8703, kl_div=0.0000
    Epoch 1: policy_loss=-0.0104, value_loss=0.9679, entropy=0.8785, kl_div=-0.1438
  Round 3/5: Mean predicted reward = 7.743
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.8549, kl_div=0.0000
    Epoch 1: policy_loss=-0.0305, value_loss=0.9696, entropy=0.8588, kl_div=-0.0423
  Round 4/5: Mean predicted reward = 7.758
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9702, entropy=0.8908, kl_div=0.0000
    Epoch 1: policy_loss=-0.0136, value_loss=0.9702, entropy=0.8903, kl_div=0.0098
  Round 5/5: Mean predicted reward = 8.083

  === Progress Analysis ===
  Status: NORMAL

--- Round 20 Results ---
  Mean Oracle Reward: 8.070
  Min Oracle Reward: 3.782
  Max Oracle Reward: 9.604
  Std Oracle Reward: 0.998
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.191, Max: 0.319, Count: 13
  Total Sequences Evaluated: 690

======================================================================
EXPERIMENT ROUND 21/50
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
  ATGTCCAG
  TGCAGTAC
  CCGTGTAA
  TTAGCAAG
  GTGTACAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.556
  Max reward: 10.431
  With intrinsic bonuses: 8.483

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9670, entropy=0.8973, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0690

=== Surrogate Model Training ===
Total samples: 722

Training on 694 samples (removed 28 outliers)
Reward range: [5.47, 10.62], mean: 8.13
  Created 13 candidate models for data size 694
  rf-tuned-l: R2 = 0.238 (std: 0.061)
  rf-tuned-xl: R2 = 0.237 (std: 0.064)
  gb-tuned-l: R2 = 0.243 (std: 0.053)
  gb-tuned-xl: R2 = 0.243 (std: 0.053)
  xgb-xl: R2 = 0.301 (std: 0.120)
  xgb-l: R2 = 0.301 (std: 0.120)
  mlp-adaptive-xl: R2 = 0.167 (std: 0.101)
  mlp-l: R2 = 0.106 (std: 0.114)
  svr-rbf-xl: R2 = 0.338 (std: 0.060)
  svr-poly-l: R2 = 0.338 (std: 0.060)
  knn-tuned-sqrt: R2 = 0.129 (std: 0.054)
  knn-tuned-l: R2 = 0.129 (std: 0.054)
  ridge: R2 = 0.003 (std: 0.053)

Model-based training with 13 models
Best R2: 0.338, Mean R2: 0.213
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9755, entropy=0.8779, kl_div=0.0000
    Epoch 1: policy_loss=-0.0090, value_loss=0.9755, entropy=0.8774, kl_div=0.0131
  Round 1/5: Mean predicted reward = 7.024
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.9164, kl_div=0.0000
    Epoch 1: policy_loss=-0.0330, value_loss=0.9688, entropy=0.9170, kl_div=-0.0254
  Round 2/5: Mean predicted reward = 7.481
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.8777, kl_div=0.0000
    Epoch 1: policy_loss=-0.0462, value_loss=0.9688, entropy=0.8780, kl_div=-0.0073
  Round 3/5: Mean predicted reward = 7.530
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.9138, kl_div=0.0000
    Epoch 1: policy_loss=-0.0504, value_loss=0.9684, entropy=0.9164, kl_div=-0.0746
  Round 4/5: Mean predicted reward = 7.897
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.9039, kl_div=0.0000
    Epoch 1: policy_loss=-0.0193, value_loss=0.9694, entropy=0.9056, kl_div=-0.0173
  Round 5/5: Mean predicted reward = 8.020

  === Progress Analysis ===
  Status: NORMAL

--- Round 21 Results ---
  Mean Oracle Reward: 8.477
  Min Oracle Reward: 6.095
  Max Oracle Reward: 10.330
  Std Oracle Reward: 0.925
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.213, Max: 0.338, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 722

======================================================================
EXPERIMENT ROUND 22/50
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 722
  Consistent improvement, increasing LR to 0.000240

--- Round 22 Configuration ---
Learning rate: 0.000240
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTAGCTAG
  TTAGAGCC
  AAGGTCCT
  ATTAGGCA
  GATGCCAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.381
  Max reward: 10.366
  With intrinsic bonuses: 8.379

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9671, entropy=0.8914, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0786

=== Surrogate Model Training ===
Total samples: 754

Training on 726 samples (removed 28 outliers)
Reward range: [5.47, 10.62], mean: 8.14
  Created 13 candidate models for data size 726
  rf-tuned-l: R2 = 0.265 (std: 0.071)
  rf-tuned-xl: R2 = 0.264 (std: 0.082)
  gb-tuned-l: R2 = 0.281 (std: 0.048)
  gb-tuned-xl: R2 = 0.281 (std: 0.048)
  xgb-xl: R2 = 0.321 (std: 0.111)
  xgb-l: R2 = 0.321 (std: 0.111)
  mlp-adaptive-xl: R2 = 0.145 (std: 0.068)
  mlp-l: R2 = 0.219 (std: 0.066)
  svr-rbf-xl: R2 = 0.353 (std: 0.052)
  svr-poly-l: R2 = 0.353 (std: 0.052)
  knn-tuned-sqrt: R2 = 0.137 (std: 0.042)
  knn-tuned-l: R2 = 0.137 (std: 0.042)
  ridge: R2 = 0.015 (std: 0.040)

Model-based training with 13 models
Best R2: 0.353, Mean R2: 0.238
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9707, entropy=0.9157, kl_div=0.0000
    Epoch 1: policy_loss=-0.0448, value_loss=0.9707, entropy=0.9161, kl_div=-0.0320
  Round 1/5: Mean predicted reward = 7.037
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9713, entropy=0.9138, kl_div=0.0000
    Epoch 1: policy_loss=-0.0828, value_loss=0.9713, entropy=0.9201, kl_div=-0.1334
  Round 2/5: Mean predicted reward = 7.345
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.9350, kl_div=0.0000
    Epoch 1: policy_loss=-0.1069, value_loss=0.9705, entropy=0.9404, kl_div=-0.0544
  Round 3/5: Mean predicted reward = 7.460
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9674, entropy=0.9207, kl_div=0.0000
    Epoch 1: policy_loss=-0.0234, value_loss=0.9674, entropy=0.9211, kl_div=-0.0181
  Round 4/5: Mean predicted reward = 7.696
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.9027, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1303
  Round 5/5: Mean predicted reward = 8.156

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 22 Results ---
  Mean Oracle Reward: 8.386
  Min Oracle Reward: 5.994
  Max Oracle Reward: 10.207
  Std Oracle Reward: 0.900
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.238, Max: 0.353, Count: 13
  Total Sequences Evaluated: 754

======================================================================
EXPERIMENT ROUND 23/50
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 754

--- Round 23 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TATGGACA
  AGCTCTGA
  GTCAGATC
  CGAGTTAC
  GTGACTAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.290
  Max reward: 9.508
  With intrinsic bonuses: 8.220

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9661, entropy=0.9327, kl_div=0.0000
    Epoch 1: policy_loss=-0.0410, value_loss=0.9661, entropy=0.9278, kl_div=0.0456

=== Surrogate Model Training ===
Total samples: 786

Training on 757 samples (removed 29 outliers)
Reward range: [5.47, 10.62], mean: 8.15
  Created 13 candidate models for data size 757
  rf-tuned-l: R2 = 0.247 (std: 0.047)
  rf-tuned-xl: R2 = 0.252 (std: 0.059)
  gb-tuned-l: R2 = 0.262 (std: 0.059)
  gb-tuned-xl: R2 = 0.262 (std: 0.059)
  xgb-xl: R2 = 0.290 (std: 0.116)
  xgb-l: R2 = 0.290 (std: 0.116)
  mlp-adaptive-xl: R2 = 0.093 (std: 0.158)
  mlp-l: R2 = 0.128 (std: 0.093)
  svr-rbf-xl: R2 = 0.345 (std: 0.054)
  svr-poly-l: R2 = 0.345 (std: 0.054)
  knn-tuned-sqrt: R2 = 0.115 (std: 0.034)
  knn-tuned-l: R2 = 0.115 (std: 0.034)
  ridge: R2 = 0.018 (std: 0.036)

Model-based training with 13 models
Best R2: 0.345, Mean R2: 0.212
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.9152, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0654
  Round 1/5: Mean predicted reward = 7.103
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9723, entropy=0.9064, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0657
  Round 2/5: Mean predicted reward = 7.460
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9735, entropy=0.8738, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0615
  Round 3/5: Mean predicted reward = 7.661
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.9062, kl_div=0.0000
    Epoch 1: policy_loss=-0.0449, value_loss=0.9691, entropy=0.9008, kl_div=0.0284
  Round 4/5: Mean predicted reward = 7.887
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.8728, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1213
  Round 5/5: Mean predicted reward = 8.026

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 23 Results ---
  Mean Oracle Reward: 8.285
  Min Oracle Reward: 5.477
  Max Oracle Reward: 9.405
  Std Oracle Reward: 0.972
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.212, Max: 0.345, Count: 13
  Total Sequences Evaluated: 786

======================================================================
EXPERIMENT ROUND 24/50
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 786

--- Round 24 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTGAATGA
  AGTGTCAC
  TACGTAGC
  CGGACATT
  GACAGTCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.258
  Max reward: 10.489
  With intrinsic bonuses: 8.227

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.8756, kl_div=0.0000
    Epoch 1: policy_loss=-0.0269, value_loss=0.9688, entropy=0.8726, kl_div=0.0398

=== Surrogate Model Training ===
Total samples: 818

Training on 783 samples (removed 35 outliers)
Reward range: [5.62, 10.62], mean: 8.18
  Created 13 candidate models for data size 783
  rf-tuned-l: R2 = 0.217 (std: 0.048)
  rf-tuned-xl: R2 = 0.211 (std: 0.048)
  gb-tuned-l: R2 = 0.273 (std: 0.019)
  gb-tuned-xl: R2 = 0.273 (std: 0.019)
  xgb-xl: R2 = 0.276 (std: 0.085)
  xgb-l: R2 = 0.276 (std: 0.085)
  mlp-adaptive-xl: R2 = 0.184 (std: 0.081)
  mlp-l: R2 = 0.212 (std: 0.097)
  svr-rbf-xl: R2 = 0.327 (std: 0.047)
  svr-poly-l: R2 = 0.327 (std: 0.047)
  knn-tuned-sqrt: R2 = 0.086 (std: 0.029)
  knn-tuned-l: R2 = 0.086 (std: 0.029)
  ridge: R2 = 0.014 (std: 0.050)

Model-based training with 13 models
Best R2: 0.327, Mean R2: 0.213
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9709, entropy=0.8621, kl_div=0.0000
    Epoch 1: policy_loss=0.0115, value_loss=0.9709, entropy=0.8598, kl_div=0.0278
  Round 1/5: Mean predicted reward = 6.993
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9702, entropy=0.8520, kl_div=0.0000
    Epoch 1: policy_loss=-0.0034, value_loss=0.9702, entropy=0.8509, kl_div=0.0124
  Round 2/5: Mean predicted reward = 7.249
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9718, entropy=0.8390, kl_div=0.0000
    Epoch 1: policy_loss=-0.0136, value_loss=0.9718, entropy=0.8381, kl_div=0.0081
  Round 3/5: Mean predicted reward = 7.484
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9673, entropy=0.8431, kl_div=0.0000
    Epoch 1: policy_loss=-0.0195, value_loss=0.9673, entropy=0.8419, kl_div=0.0079
  Round 4/5: Mean predicted reward = 7.938
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9706, entropy=0.8670, kl_div=0.0000
    Epoch 1: policy_loss=-0.0334, value_loss=0.9706, entropy=0.8643, kl_div=0.0231
  Round 5/5: Mean predicted reward = 8.050

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 24 Results ---
  Mean Oracle Reward: 8.236
  Min Oracle Reward: 4.655
  Max Oracle Reward: 10.548
  Std Oracle Reward: 1.168
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.213, Max: 0.327, Count: 13
  Total Sequences Evaluated: 818

======================================================================
EXPERIMENT ROUND 25/50
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
  GCTGCAAT
  CTGGTCAA
  GATCGCAT
  ACGGTCAT
  GATAGCCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.176
  Max reward: 10.275
  With intrinsic bonuses: 8.098

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9681, entropy=0.8587, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1501

=== Surrogate Model Training ===
Total samples: 850

Training on 812 samples (removed 38 outliers)
Reward range: [5.62, 10.62], mean: 8.19
  Created 13 candidate models for data size 812
  rf-tuned-l: R2 = 0.237 (std: 0.045)
  rf-tuned-xl: R2 = 0.226 (std: 0.054)
  gb-tuned-l: R2 = 0.271 (std: 0.046)
  gb-tuned-xl: R2 = 0.271 (std: 0.046)
  xgb-xl: R2 = 0.212 (std: 0.080)
  xgb-l: R2 = 0.212 (std: 0.080)
  mlp-adaptive-xl: R2 = 0.205 (std: 0.081)
  mlp-l: R2 = 0.242 (std: 0.059)
  svr-rbf-xl: R2 = 0.336 (std: 0.038)
  svr-poly-l: R2 = 0.336 (std: 0.038)
  knn-tuned-sqrt: R2 = 0.073 (std: 0.053)
  knn-tuned-l: R2 = 0.073 (std: 0.053)
  ridge: R2 = 0.009 (std: 0.045)

Model-based training with 13 models
Best R2: 0.336, Mean R2: 0.208
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.8537, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0834
  Round 1/5: Mean predicted reward = 7.081
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9714, entropy=0.8280, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1539
  Round 2/5: Mean predicted reward = 7.414
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9724, entropy=0.8136, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1677
  Round 3/5: Mean predicted reward = 7.537
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9703, entropy=0.7855, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2055
  Round 4/5: Mean predicted reward = 7.719
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.7910, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1750
  Round 5/5: Mean predicted reward = 8.032

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 25 Results ---
  Mean Oracle Reward: 8.093
  Min Oracle Reward: 3.675
  Max Oracle Reward: 10.202
  Std Oracle Reward: 1.415
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.208, Max: 0.336, Count: 13
  Total Sequences Evaluated: 850

======================================================================
EXPERIMENT ROUND 26/50
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
  GACCATTG
  CATGAGCT
  GTACTACG
  CACATGTG
  ACTTGACG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.137
  Max reward: 10.393
  With intrinsic bonuses: 8.136

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9672, entropy=0.7732, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2307

=== Surrogate Model Training ===
Total samples: 882

Training on 845 samples (removed 37 outliers)
Reward range: [5.52, 10.62], mean: 8.18
  Created 13 candidate models for data size 845
  rf-tuned-l: R2 = 0.240 (std: 0.038)
  rf-tuned-xl: R2 = 0.244 (std: 0.042)
  gb-tuned-l: R2 = 0.284 (std: 0.029)
  gb-tuned-xl: R2 = 0.284 (std: 0.029)
  xgb-xl: R2 = 0.316 (std: 0.028)
  xgb-l: R2 = 0.316 (std: 0.028)
  mlp-adaptive-xl: R2 = 0.225 (std: 0.120)
  mlp-l: R2 = 0.195 (std: 0.080)
  svr-rbf-xl: R2 = 0.353 (std: 0.044)
  svr-poly-l: R2 = 0.353 (std: 0.044)
  knn-tuned-sqrt: R2 = 0.076 (std: 0.057)
  knn-tuned-l: R2 = 0.076 (std: 0.057)
  ridge: R2 = 0.025 (std: 0.050)

Model-based training with 13 models
Best R2: 0.353, Mean R2: 0.230
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9668, entropy=0.7498, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1510
  Round 1/5: Mean predicted reward = 6.924
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9710, entropy=0.7308, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0556
  Round 2/5: Mean predicted reward = 7.232
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.7558, kl_div=0.0000
    Epoch 1: policy_loss=-0.0166, value_loss=0.9696, entropy=0.7529, kl_div=-0.0235
  Round 3/5: Mean predicted reward = 7.569
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9727, entropy=0.7101, kl_div=0.0000
    Epoch 1: policy_loss=-0.0290, value_loss=0.9727, entropy=0.7076, kl_div=0.0430
  Round 4/5: Mean predicted reward = 7.611
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9678, entropy=0.7170, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0937
  Round 5/5: Mean predicted reward = 8.026

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 26 Results ---
  Mean Oracle Reward: 8.120
  Min Oracle Reward: 5.920
  Max Oracle Reward: 10.197
  Std Oracle Reward: 1.011
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.230, Max: 0.353, Count: 13
  Total Sequences Evaluated: 882

======================================================================
EXPERIMENT ROUND 27/50
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
  GTCCATGA
  TTCGCAGA
  TCATCGAG
  TATGACGC
  CCATTGAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.465
  Max reward: 10.645
  With intrinsic bonuses: 8.467

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.7177, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0836

=== Surrogate Model Training ===
Total samples: 914

Training on 880 samples (removed 34 outliers)
Reward range: [5.50, 10.81], mean: 8.19
  Created 13 candidate models for data size 880
  rf-tuned-l: R2 = 0.265 (std: 0.030)
  rf-tuned-xl: R2 = 0.258 (std: 0.022)
  gb-tuned-l: R2 = 0.263 (std: 0.030)
  gb-tuned-xl: R2 = 0.263 (std: 0.030)
  xgb-xl: R2 = 0.264 (std: 0.040)
  xgb-l: R2 = 0.264 (std: 0.040)
  mlp-adaptive-xl: R2 = 0.238 (std: 0.046)
  mlp-l: R2 = 0.240 (std: 0.050)
  svr-rbf-xl: R2 = 0.369 (std: 0.035)
  svr-poly-l: R2 = 0.369 (std: 0.035)
  knn-tuned-sqrt: R2 = 0.117 (std: 0.041)
  knn-tuned-l: R2 = 0.117 (std: 0.041)
  ridge: R2 = 0.011 (std: 0.053)

Model-based training with 13 models
Best R2: 0.369, Mean R2: 0.234
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.7127, kl_div=0.0000
    Epoch 1: policy_loss=-0.0159, value_loss=0.9694, entropy=0.7099, kl_div=0.0361
  Round 1/5: Mean predicted reward = 6.959
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.7385, kl_div=0.0000
    Epoch 1: policy_loss=-0.0482, value_loss=0.9694, entropy=0.7412, kl_div=-0.0674
  Round 2/5: Mean predicted reward = 7.143
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.7237, kl_div=0.0000
    Epoch 1: policy_loss=-0.0209, value_loss=0.9690, entropy=0.7294, kl_div=-0.0310
  Round 3/5: Mean predicted reward = 7.314
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9667, entropy=0.7372, kl_div=0.0000
    Epoch 1: policy_loss=0.0050, value_loss=0.9667, entropy=0.7431, kl_div=-0.0837
  Round 4/5: Mean predicted reward = 7.654
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.7626, kl_div=0.0000
    Epoch 1: policy_loss=-0.0318, value_loss=0.9690, entropy=0.7621, kl_div=0.0179
  Round 5/5: Mean predicted reward = 8.074

  === Progress Analysis ===
  Status: NORMAL

--- Round 27 Results ---
  Mean Oracle Reward: 8.503
  Min Oracle Reward: 6.037
  Max Oracle Reward: 10.500
  Std Oracle Reward: 1.005
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.234, Max: 0.369, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 914

======================================================================
EXPERIMENT ROUND 28/50
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 914

--- Round 28 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  AGGATTCC
  TAGCATGC
  GGCTAAAT
  GGTCCAGA
  TAACGCGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.195
  Max reward: 11.293
  With intrinsic bonuses: 8.220

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.7400, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1068

=== Surrogate Model Training ===
Total samples: 946

Training on 911 samples (removed 35 outliers)
Reward range: [5.50, 10.81], mean: 8.19
  Created 13 candidate models for data size 911
  rf-tuned-l: R2 = 0.283 (std: 0.040)
  rf-tuned-xl: R2 = 0.291 (std: 0.037)
  gb-tuned-l: R2 = 0.274 (std: 0.028)
  gb-tuned-xl: R2 = 0.274 (std: 0.028)
  xgb-xl: R2 = 0.328 (std: 0.050)
  xgb-l: R2 = 0.328 (std: 0.050)
  mlp-adaptive-xl: R2 = 0.243 (std: 0.059)
  mlp-l: R2 = 0.230 (std: 0.028)
  svr-rbf-xl: R2 = 0.392 (std: 0.055)
  svr-poly-l: R2 = 0.392 (std: 0.055)
  knn-tuned-sqrt: R2 = 0.139 (std: 0.034)
  knn-tuned-l: R2 = 0.139 (std: 0.034)
  ridge: R2 = 0.017 (std: 0.061)

Model-based training with 13 models
Best R2: 0.392, Mean R2: 0.256
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9668, entropy=0.7527, kl_div=0.0000
    Epoch 1: policy_loss=-0.0109, value_loss=0.9668, entropy=0.7500, kl_div=0.0474
  Round 1/5: Mean predicted reward = 6.646
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.7333, kl_div=0.0000
    Epoch 1: policy_loss=-0.0496, value_loss=0.9698, entropy=0.7369, kl_div=-0.0264
  Round 2/5: Mean predicted reward = 7.047
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9704, entropy=0.7505, kl_div=0.0000
    Epoch 1: policy_loss=-0.0398, value_loss=0.9704, entropy=0.7585, kl_div=-0.1160
  Round 3/5: Mean predicted reward = 7.412
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.7752, kl_div=0.0000
    Epoch 1: policy_loss=-0.0397, value_loss=0.9696, entropy=0.7783, kl_div=-0.0153
  Round 4/5: Mean predicted reward = 7.603
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.7719, kl_div=0.0000
    Epoch 1: policy_loss=-0.0132, value_loss=0.9698, entropy=0.7735, kl_div=-0.0271
  Round 5/5: Mean predicted reward = 7.982

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 28 Results ---
  Mean Oracle Reward: 8.191
  Min Oracle Reward: 5.142
  Max Oracle Reward: 11.103
  Std Oracle Reward: 1.063
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.256, Max: 0.392, Count: 13
  Total Sequences Evaluated: 946

======================================================================
EXPERIMENT ROUND 29/50
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 946

--- Round 29 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CGTACTAG
  ATTAAGCG
  GAACAGTT
  GACAGTTC
  GTGTACAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.329
  Max reward: 9.917
  With intrinsic bonuses: 8.317

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9661, entropy=0.7602, kl_div=0.0000
    Epoch 1: policy_loss=-0.0199, value_loss=0.9661, entropy=0.7587, kl_div=0.0235

=== Surrogate Model Training ===
Total samples: 978

Training on 938 samples (removed 40 outliers)
Reward range: [5.54, 10.81], mean: 8.21
  Created 13 candidate models for data size 938
  rf-tuned-l: R2 = 0.283 (std: 0.028)
  rf-tuned-xl: R2 = 0.278 (std: 0.028)
  gb-tuned-l: R2 = 0.274 (std: 0.025)
  gb-tuned-xl: R2 = 0.274 (std: 0.025)
  xgb-xl: R2 = 0.306 (std: 0.039)
  xgb-l: R2 = 0.306 (std: 0.039)
  mlp-adaptive-xl: R2 = 0.230 (std: 0.053)
  mlp-l: R2 = 0.211 (std: 0.052)
  svr-rbf-xl: R2 = 0.382 (std: 0.042)
  svr-poly-l: R2 = 0.382 (std: 0.042)
  knn-tuned-sqrt: R2 = 0.123 (std: 0.016)
  knn-tuned-l: R2 = 0.123 (std: 0.016)
  ridge: R2 = 0.015 (std: 0.061)

Model-based training with 13 models
Best R2: 0.382, Mean R2: 0.245
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9679, entropy=0.7888, kl_div=0.0000
    Epoch 1: policy_loss=0.0010, value_loss=0.9679, entropy=0.7873, kl_div=0.0132
  Round 1/5: Mean predicted reward = 6.708
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9683, entropy=0.7493, kl_div=0.0000
    Epoch 1: policy_loss=-0.0133, value_loss=0.9683, entropy=0.7492, kl_div=0.0089
  Round 2/5: Mean predicted reward = 7.020
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9695, entropy=0.7765, kl_div=0.0000
    Epoch 1: policy_loss=-0.0197, value_loss=0.9695, entropy=0.7789, kl_div=-0.0260
  Round 3/5: Mean predicted reward = 7.385
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.8011, kl_div=0.0000
    Epoch 1: policy_loss=0.0020, value_loss=0.9684, entropy=0.8035, kl_div=-0.0465
  Round 4/5: Mean predicted reward = 7.593
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9669, entropy=0.7472, kl_div=0.0000
    Epoch 1: policy_loss=-0.0084, value_loss=0.9669, entropy=0.7476, kl_div=0.0011
  Round 5/5: Mean predicted reward = 7.927

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 29 Results ---
  Mean Oracle Reward: 8.343
  Min Oracle Reward: 5.500
  Max Oracle Reward: 9.682
  Std Oracle Reward: 0.992
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.245, Max: 0.382, Count: 13
  Total Sequences Evaluated: 978

======================================================================
EXPERIMENT ROUND 30/50
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 978

--- Round 30 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GACGGATC
  TGCTAACG
  CTATAAGG
  GTATGAAC
  CTTAACGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.442
  Max reward: 9.573
  With intrinsic bonuses: 8.471

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.7904, kl_div=0.0000
    Epoch 1: policy_loss=-0.0344, value_loss=0.9698, entropy=0.7897, kl_div=-0.0373

=== Surrogate Model Training ===
Total samples: 1010

Training on 968 samples (removed 42 outliers)
Reward range: [5.62, 10.62], mean: 8.22
  Created 13 candidate models for data size 968
  rf-tuned-l: R2 = 0.291 (std: 0.051)
  rf-tuned-xl: R2 = 0.296 (std: 0.044)
  gb-tuned-l: R2 = 0.273 (std: 0.043)
  gb-tuned-xl: R2 = 0.273 (std: 0.043)
  xgb-xl: R2 = 0.335 (std: 0.056)
  xgb-l: R2 = 0.335 (std: 0.056)
  mlp-adaptive-xl: R2 = 0.247 (std: 0.066)
  mlp-l: R2 = 0.249 (std: 0.074)
  svr-rbf-xl: R2 = 0.387 (std: 0.050)
  svr-poly-l: R2 = 0.387 (std: 0.050)
  knn-tuned-sqrt: R2 = 0.140 (std: 0.033)
  knn-tuned-l: R2 = 0.140 (std: 0.033)
  ridge: R2 = 0.015 (std: 0.063)

Model-based training with 13 models
Best R2: 0.387, Mean R2: 0.259
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.7511, kl_div=0.0000
    Epoch 1: policy_loss=-0.0236, value_loss=0.9706, entropy=0.7530, kl_div=-0.0319
  Round 1/5: Mean predicted reward = 6.585
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9707, entropy=0.7666, kl_div=0.0000
    Epoch 1: policy_loss=0.0069, value_loss=0.9707, entropy=0.7815, kl_div=-0.3016
  Round 2/5: Mean predicted reward = 6.922
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9673, entropy=0.7882, kl_div=0.0000
    Epoch 1: policy_loss=-0.0523, value_loss=0.9673, entropy=0.7933, kl_div=-0.0459
  Round 3/5: Mean predicted reward = 7.290
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.7605, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2931
  Round 4/5: Mean predicted reward = 7.640
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.8501, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2230
  Round 5/5: Mean predicted reward = 8.011

  === Progress Analysis ===
  Status: NORMAL

--- Round 30 Results ---
  Mean Oracle Reward: 8.455
  Min Oracle Reward: 6.925
  Max Oracle Reward: 9.594
  Std Oracle Reward: 0.615
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.259, Max: 0.387, Count: 13
  Total Sequences Evaluated: 1010

======================================================================
EXPERIMENT ROUND 31/50
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
  ATGCTGAA
  TCGAAGTC
  CAGATGTC
  AGGCGTAC
  GAGCCTAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.126
  Max reward: 10.108
  With intrinsic bonuses: 8.163

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9700, entropy=0.7903, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3370

=== Surrogate Model Training ===
Total samples: 1042

Training on 998 samples (removed 44 outliers)
Reward range: [5.58, 10.62], mean: 8.22
  Created 13 candidate models for data size 998
  rf-tuned-l: R2 = 0.300 (std: 0.053)
  rf-tuned-xl: R2 = 0.317 (std: 0.050)
  gb-tuned-l: R2 = 0.282 (std: 0.049)
  gb-tuned-xl: R2 = 0.282 (std: 0.049)
  xgb-xl: R2 = 0.362 (std: 0.035)
  xgb-l: R2 = 0.362 (std: 0.035)
  mlp-adaptive-xl: R2 = 0.235 (std: 0.069)
  mlp-l: R2 = 0.275 (std: 0.032)
  svr-rbf-xl: R2 = 0.403 (std: 0.052)
  svr-poly-l: R2 = 0.403 (std: 0.052)
  knn-tuned-sqrt: R2 = 0.158 (std: 0.029)
  knn-tuned-l: R2 = 0.158 (std: 0.029)
  ridge: R2 = 0.028 (std: 0.061)

Model-based training with 13 models
Best R2: 0.403, Mean R2: 0.274
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9709, entropy=0.8048, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1357
  Round 1/5: Mean predicted reward = 6.531
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.7730, kl_div=0.0000
    Epoch 1: policy_loss=-0.0591, value_loss=0.9701, entropy=0.7766, kl_div=-0.0242
  Round 2/5: Mean predicted reward = 6.911
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9707, entropy=0.7670, kl_div=0.0000
    Epoch 1: policy_loss=-0.0319, value_loss=0.9707, entropy=0.7848, kl_div=-0.3099
  Round 3/5: Mean predicted reward = 7.264
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9711, entropy=0.8365, kl_div=0.0000
    Epoch 1: policy_loss=-0.0322, value_loss=0.9711, entropy=0.8466, kl_div=-0.0443
  Round 4/5: Mean predicted reward = 7.672
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9700, entropy=0.8420, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2195
  Round 5/5: Mean predicted reward = 8.002

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 31 Results ---
  Mean Oracle Reward: 8.125
  Min Oracle Reward: 2.447
  Max Oracle Reward: 9.684
  Std Oracle Reward: 1.489
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.274, Max: 0.403, Count: 13
  Total Sequences Evaluated: 1042

======================================================================
EXPERIMENT ROUND 32/50
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1042

--- Round 32 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CACAGTGT
  ATAGGCTC
  AGTAGTCC
  TGCTGAAC
  TGGAACTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.559
  Max reward: 10.559
  With intrinsic bonuses: 8.602

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9659, entropy=0.8197, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2947

=== Surrogate Model Training ===
Total samples: 1074

Training on 1028 samples (removed 46 outliers)
Reward range: [5.62, 10.62], mean: 8.24
  Created 13 candidate models for data size 1028
  rf-tuned-l: R2 = 0.307 (std: 0.042)
  rf-tuned-xl: R2 = 0.305 (std: 0.038)
  gb-tuned-l: R2 = 0.296 (std: 0.039)
  gb-tuned-xl: R2 = 0.296 (std: 0.039)
  xgb-xl: R2 = 0.346 (std: 0.016)
  xgb-l: R2 = 0.346 (std: 0.016)
  mlp-adaptive-xl: R2 = 0.266 (std: 0.058)
  mlp-l: R2 = 0.271 (std: 0.081)
  svr-rbf-xl: R2 = 0.407 (std: 0.041)
  svr-poly-l: R2 = 0.407 (std: 0.041)
  knn-tuned-sqrt: R2 = 0.164 (std: 0.030)
  knn-tuned-l: R2 = 0.164 (std: 0.030)
  ridge: R2 = 0.019 (std: 0.059)

Model-based training with 13 models
Best R2: 0.407, Mean R2: 0.276
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9714, entropy=0.8544, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1493
  Round 1/5: Mean predicted reward = 6.657
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.8405, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1642
  Round 2/5: Mean predicted reward = 7.232
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=0.8566, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1580
  Round 3/5: Mean predicted reward = 7.333
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.8113, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2689
  Round 4/5: Mean predicted reward = 7.657
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9708, entropy=0.8144, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3843
  Round 5/5: Mean predicted reward = 8.067

  === Progress Analysis ===
  Status: NORMAL

--- Round 32 Results ---
  Mean Oracle Reward: 8.601
  Min Oracle Reward: 4.228
  Max Oracle Reward: 10.401
  Std Oracle Reward: 1.000
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.276, Max: 0.407, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 1074

======================================================================
EXPERIMENT ROUND 33/50
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1074

--- Round 33 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TCAGCTAG
  AGAGATCT
  GGAAACTT
  TCAGACGT
  CTCAGAGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.336
  Max reward: 9.750
  With intrinsic bonuses: 8.392

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.7961, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2839

=== Surrogate Model Training ===
Total samples: 1106

Training on 1059 samples (removed 47 outliers)
Reward range: [5.62, 10.62], mean: 8.25
  Created 13 candidate models for data size 1059
  rf-tuned-l: R2 = 0.311 (std: 0.034)
  rf-tuned-xl: R2 = 0.316 (std: 0.038)
  gb-tuned-l: R2 = 0.293 (std: 0.047)
  gb-tuned-xl: R2 = 0.293 (std: 0.047)
  xgb-xl: R2 = 0.369 (std: 0.032)
  xgb-l: R2 = 0.369 (std: 0.032)
  mlp-adaptive-xl: R2 = 0.331 (std: 0.042)
  mlp-l: R2 = 0.320 (std: 0.045)
  svr-rbf-xl: R2 = 0.412 (std: 0.049)
  svr-poly-l: R2 = 0.412 (std: 0.049)
  knn-tuned-sqrt: R2 = 0.171 (std: 0.052)
  knn-tuned-l: R2 = 0.171 (std: 0.052)
  ridge: R2 = 0.009 (std: 0.076)

Model-based training with 13 models
Best R2: 0.412, Mean R2: 0.290
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.7900, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3662
  Round 1/5: Mean predicted reward = 6.997
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9687, entropy=0.7924, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2840
  Round 2/5: Mean predicted reward = 7.062
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9695, entropy=0.7574, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4889
  Round 3/5: Mean predicted reward = 7.399
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9664, entropy=0.7284, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5584
  Round 4/5: Mean predicted reward = 7.688
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9712, entropy=0.7302, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5136
  Round 5/5: Mean predicted reward = 7.937

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 33 Results ---
  Mean Oracle Reward: 8.330
  Min Oracle Reward: 4.994
  Max Oracle Reward: 9.904
  Std Oracle Reward: 1.118
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.290, Max: 0.412, Count: 13
  Total Sequences Evaluated: 1106

======================================================================
EXPERIMENT ROUND 34/50
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1106

--- Round 34 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CTAATGCG
  CTATACGG
  GTTACAGC
  ATACTAGG
  CGCAGTTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.978
  Max reward: 10.256
  With intrinsic bonuses: 8.022

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9673, entropy=0.6995, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2227

=== Surrogate Model Training ===
Total samples: 1138

Training on 1088 samples (removed 50 outliers)
Reward range: [5.62, 10.62], mean: 8.25
  Created 13 candidate models for data size 1088
  rf-tuned-l: R2 = 0.317 (std: 0.049)
  rf-tuned-xl: R2 = 0.311 (std: 0.051)
  gb-tuned-l: R2 = 0.290 (std: 0.056)
  gb-tuned-xl: R2 = 0.290 (std: 0.056)
  xgb-xl: R2 = 0.368 (std: 0.034)
  xgb-l: R2 = 0.368 (std: 0.034)
  mlp-adaptive-xl: R2 = 0.286 (std: 0.065)
  mlp-l: R2 = 0.317 (std: 0.072)
  svr-rbf-xl: R2 = 0.403 (std: 0.061)
  svr-poly-l: R2 = 0.403 (std: 0.061)
  knn-tuned-sqrt: R2 = 0.135 (std: 0.069)
  knn-tuned-l: R2 = 0.135 (std: 0.069)
  ridge: R2 = 0.001 (std: 0.091)

Model-based training with 13 models
Best R2: 0.403, Mean R2: 0.279
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.7126, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1727
  Round 1/5: Mean predicted reward = 6.930
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.7340, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1714
  Round 2/5: Mean predicted reward = 7.158
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=0.7169, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1967
  Round 3/5: Mean predicted reward = 7.430
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9707, entropy=0.6753, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2547
  Round 4/5: Mean predicted reward = 7.662
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9719, entropy=0.7158, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1263
  Round 5/5: Mean predicted reward = 7.912

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 34 Results ---
  Mean Oracle Reward: 7.955
  Min Oracle Reward: 4.599
  Max Oracle Reward: 10.351
  Std Oracle Reward: 1.382
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.279, Max: 0.403, Count: 13
  Total Sequences Evaluated: 1138

======================================================================
EXPERIMENT ROUND 35/50
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1138

--- Round 35 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GATTACGC
  TAGCGTAA
  TCCGAGAT
  GTGACTAC
  CGTATCGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.289
  Max reward: 10.176
  With intrinsic bonuses: 8.317

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.6504, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.2815

=== Surrogate Model Training ===
Total samples: 1170

Training on 1118 samples (removed 52 outliers)
Reward range: [5.69, 10.62], mean: 8.26
  Created 13 candidate models for data size 1118
  rf-tuned-l: R2 = 0.320 (std: 0.040)
  rf-tuned-xl: R2 = 0.325 (std: 0.028)
  gb-tuned-l: R2 = 0.293 (std: 0.047)
  gb-tuned-xl: R2 = 0.293 (std: 0.047)
  xgb-xl: R2 = 0.377 (std: 0.037)
  xgb-l: R2 = 0.377 (std: 0.037)
  mlp-adaptive-xl: R2 = 0.279 (std: 0.046)
  mlp-l: R2 = 0.271 (std: 0.057)
  svr-rbf-xl: R2 = 0.414 (std: 0.059)
  svr-poly-l: R2 = 0.414 (std: 0.059)
  knn-tuned-sqrt: R2 = 0.148 (std: 0.057)
  knn-tuned-l: R2 = 0.148 (std: 0.057)
  ridge: R2 = 0.001 (std: 0.096)

Model-based training with 13 models
Best R2: 0.414, Mean R2: 0.282
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.6275, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9996
  Round 1/5: Mean predicted reward = 6.841
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.5893, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.5560
  Round 2/5: Mean predicted reward = 7.021
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.5626, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.5153
  Round 3/5: Mean predicted reward = 7.231
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9682, entropy=0.5059, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.5077
  Round 4/5: Mean predicted reward = 7.484
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9711, entropy=0.4590, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8474
  Round 5/5: Mean predicted reward = 7.846

  === Progress Analysis ===
  Status: NORMAL

--- Round 35 Results ---
  Mean Oracle Reward: 8.309
  Min Oracle Reward: 6.323
  Max Oracle Reward: 10.068
  Std Oracle Reward: 0.815
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.282, Max: 0.414, Count: 13
  Total Sequences Evaluated: 1170

======================================================================
EXPERIMENT ROUND 36/50
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1170

--- Round 36 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TAGTGACC
  GAGTCCAT
  ATGTACCG
  CAGTGTAC
  AGATCGCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.133
  Max reward: 10.421
  With intrinsic bonuses: 8.140

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.4197, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.7850

=== Surrogate Model Training ===
Total samples: 1202

Training on 1148 samples (removed 54 outliers)
Reward range: [5.69, 10.62], mean: 8.25
  Created 13 candidate models for data size 1148
  rf-tuned-l: R2 = 0.313 (std: 0.050)
  rf-tuned-xl: R2 = 0.312 (std: 0.042)
  gb-tuned-l: R2 = 0.310 (std: 0.055)
  gb-tuned-xl: R2 = 0.310 (std: 0.055)
  xgb-xl: R2 = 0.389 (std: 0.033)
  xgb-l: R2 = 0.389 (std: 0.033)
  mlp-adaptive-xl: R2 = 0.284 (std: 0.071)
  mlp-l: R2 = 0.320 (std: 0.048)
  svr-rbf-xl: R2 = 0.425 (std: 0.056)
  svr-poly-l: R2 = 0.425 (std: 0.056)
  knn-tuned-sqrt: R2 = 0.153 (std: 0.055)
  knn-tuned-l: R2 = 0.153 (std: 0.055)
  ridge: R2 = 0.010 (std: 0.091)

Model-based training with 13 models
Best R2: 0.425, Mean R2: 0.292
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9695, entropy=0.4157, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4039
  Round 1/5: Mean predicted reward = 6.699
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9715, entropy=0.4245, kl_div=0.0000
    Epoch 1: policy_loss=-0.0478, value_loss=0.9715, entropy=0.4309, kl_div=-0.0422
  Round 2/5: Mean predicted reward = 6.934
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9713, entropy=0.4249, kl_div=0.0000
    Epoch 1: policy_loss=-0.0806, value_loss=0.9713, entropy=0.4311, kl_div=-0.0826
  Round 3/5: Mean predicted reward = 7.248
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9694, entropy=0.4801, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5863
  Round 4/5: Mean predicted reward = 7.448
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9723, entropy=0.4540, kl_div=0.0000
    Epoch 1: policy_loss=-0.0858, value_loss=0.9723, entropy=0.4586, kl_div=0.0401
  Round 5/5: Mean predicted reward = 7.852

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 36 Results ---
  Mean Oracle Reward: 8.112
  Min Oracle Reward: 5.324
  Max Oracle Reward: 10.742
  Std Oracle Reward: 1.139
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.292, Max: 0.425, Count: 13
  Total Sequences Evaluated: 1202

======================================================================
EXPERIMENT ROUND 37/50
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1202

--- Round 37 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TTAGAGCA
  ATGGCCAT
  GGCTATAC
  TCCGGATA
  TAAGCCGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.223
  Max reward: 10.659
  With intrinsic bonuses: 8.222

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.4397, kl_div=0.0000
    Epoch 1: policy_loss=0.1127, value_loss=0.9697, entropy=0.4539, kl_div=-0.5767

=== Surrogate Model Training ===
Total samples: 1234

Training on 1177 samples (removed 57 outliers)
Reward range: [5.69, 10.62], mean: 8.26
  Created 13 candidate models for data size 1177
  rf-tuned-l: R2 = 0.306 (std: 0.036)
  rf-tuned-xl: R2 = 0.310 (std: 0.032)
  gb-tuned-l: R2 = 0.305 (std: 0.044)
  gb-tuned-xl: R2 = 0.305 (std: 0.044)
  xgb-xl: R2 = 0.386 (std: 0.033)
  xgb-l: R2 = 0.386 (std: 0.033)
  mlp-adaptive-xl: R2 = 0.282 (std: 0.029)
  mlp-l: R2 = 0.314 (std: 0.062)
  svr-rbf-xl: R2 = 0.426 (std: 0.042)
  svr-poly-l: R2 = 0.426 (std: 0.042)
  knn-tuned-sqrt: R2 = 0.164 (std: 0.047)
  knn-tuned-l: R2 = 0.164 (std: 0.047)
  ridge: R2 = 0.010 (std: 0.085)

Model-based training with 13 models
Best R2: 0.426, Mean R2: 0.291
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.4588, kl_div=0.0000
    Epoch 1: policy_loss=0.1563, value_loss=0.9699, entropy=0.4708, kl_div=-0.4837
  Round 1/5: Mean predicted reward = 6.462
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9708, entropy=0.5029, kl_div=0.0000
    Epoch 1: policy_loss=0.0664, value_loss=0.9708, entropy=0.5120, kl_div=-0.3343
  Round 2/5: Mean predicted reward = 6.821
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9710, entropy=0.4546, kl_div=0.0000
    Epoch 1: policy_loss=0.0557, value_loss=0.9710, entropy=0.4648, kl_div=-0.3643
  Round 3/5: Mean predicted reward = 7.221
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.4840, kl_div=0.0000
    Epoch 1: policy_loss=-0.0066, value_loss=0.9699, entropy=0.4909, kl_div=-0.2716
  Round 4/5: Mean predicted reward = 7.450
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9708, entropy=0.4825, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0972
  Round 5/5: Mean predicted reward = 7.862

  === Progress Analysis ===
  Status: NORMAL

--- Round 37 Results ---
  Mean Oracle Reward: 8.217
  Min Oracle Reward: 3.507
  Max Oracle Reward: 10.534
  Std Oracle Reward: 1.348
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.291, Max: 0.426, Count: 13
  Total Sequences Evaluated: 1234

======================================================================
EXPERIMENT ROUND 38/50
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
  CAGTATGC
  TTAAGCCG
  ACGATCTG
  GGCTAACT
  CAGCTTAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.735
  Max reward: 9.768
  With intrinsic bonuses: 7.768

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9691, entropy=0.4887, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0555

=== Surrogate Model Training ===
Total samples: 1266

Training on 1206 samples (removed 60 outliers)
Reward range: [5.69, 10.62], mean: 8.26
  Created 13 candidate models for data size 1206
  rf-tuned-l: R2 = 0.320 (std: 0.023)
  rf-tuned-xl: R2 = 0.316 (std: 0.030)
  gb-tuned-l: R2 = 0.296 (std: 0.039)
  gb-tuned-xl: R2 = 0.296 (std: 0.039)
  xgb-xl: R2 = 0.391 (std: 0.050)
  xgb-l: R2 = 0.391 (std: 0.050)
  mlp-adaptive-xl: R2 = 0.293 (std: 0.048)
  mlp-l: R2 = 0.308 (std: 0.080)
  svr-rbf-xl: R2 = 0.433 (std: 0.039)
  svr-poly-l: R2 = 0.433 (std: 0.039)
  knn-tuned-sqrt: R2 = 0.170 (std: 0.048)
  knn-tuned-l: R2 = 0.170 (std: 0.048)
  ridge: R2 = 0.007 (std: 0.077)

Model-based training with 13 models
Best R2: 0.433, Mean R2: 0.294
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9696, entropy=0.4750, kl_div=0.0000
    Epoch 1: policy_loss=-0.0188, value_loss=0.9696, entropy=0.4761, kl_div=-0.0326
  Round 1/5: Mean predicted reward = 6.334
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9702, entropy=0.4760, kl_div=0.0000
    Epoch 1: policy_loss=-0.0436, value_loss=0.9702, entropy=0.4817, kl_div=-0.1958
  Round 2/5: Mean predicted reward = 6.790
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.5082, kl_div=0.0000
    Epoch 1: policy_loss=-0.0570, value_loss=0.9698, entropy=0.5135, kl_div=-0.1493
  Round 3/5: Mean predicted reward = 7.004
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9707, entropy=0.5016, kl_div=0.0000
    Epoch 1: policy_loss=-0.0441, value_loss=0.9707, entropy=0.5080, kl_div=-0.1906
  Round 4/5: Mean predicted reward = 7.489
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9702, entropy=0.5430, kl_div=0.0000
    Epoch 1: policy_loss=-0.0144, value_loss=0.9702, entropy=0.5502, kl_div=-0.1774
  Round 5/5: Mean predicted reward = 7.902

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 38 Results ---
  Mean Oracle Reward: 7.759
  Min Oracle Reward: 0.924
  Max Oracle Reward: 9.683
  Std Oracle Reward: 1.744
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.294, Max: 0.433, Count: 13
  Total Sequences Evaluated: 1266

======================================================================
EXPERIMENT ROUND 39/50
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1266

--- Round 39 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ACTTGGCA
  GCGCAGAT
  ACATGATG
  CAGAAGTT
  AAATGGTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.804
  Max reward: 8.976
  With intrinsic bonuses: 7.835

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.5538, kl_div=0.0000
    Epoch 1: policy_loss=-0.0068, value_loss=0.9696, entropy=0.5546, kl_div=-0.0126

=== Surrogate Model Training ===
Total samples: 1298

Training on 1237 samples (removed 61 outliers)
Reward range: [5.69, 10.62], mean: 8.25
  Created 13 candidate models for data size 1237
  rf-tuned-l: R2 = 0.325 (std: 0.020)
  rf-tuned-xl: R2 = 0.334 (std: 0.023)
  gb-tuned-l: R2 = 0.296 (std: 0.037)
  gb-tuned-xl: R2 = 0.296 (std: 0.037)
  xgb-xl: R2 = 0.371 (std: 0.045)
  xgb-l: R2 = 0.371 (std: 0.045)
  mlp-adaptive-xl: R2 = 0.290 (std: 0.057)
  mlp-l: R2 = 0.293 (std: 0.027)
  svr-rbf-xl: R2 = 0.432 (std: 0.033)
  svr-poly-l: R2 = 0.432 (std: 0.033)
  knn-tuned-sqrt: R2 = 0.167 (std: 0.057)
  knn-tuned-l: R2 = 0.167 (std: 0.057)
  ridge: R2 = 0.014 (std: 0.071)

Model-based training with 13 models
Best R2: 0.432, Mean R2: 0.291
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9694, entropy=0.5291, kl_div=0.0000
    Epoch 1: policy_loss=-0.0299, value_loss=0.9694, entropy=0.5307, kl_div=-0.0431
  Round 1/5: Mean predicted reward = 6.025
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.5214, kl_div=0.0000
    Epoch 1: policy_loss=-0.0520, value_loss=0.9705, entropy=0.5262, kl_div=-0.1324
  Round 2/5: Mean predicted reward = 6.587
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9697, entropy=0.5385, kl_div=0.0000
    Epoch 1: policy_loss=-0.0287, value_loss=0.9697, entropy=0.5438, kl_div=-0.1516
  Round 3/5: Mean predicted reward = 6.930
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.5835, kl_div=0.0000
    Epoch 1: policy_loss=-0.0412, value_loss=0.9685, entropy=0.5891, kl_div=-0.1260
  Round 4/5: Mean predicted reward = 7.421
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.5249, kl_div=0.0000
    Epoch 1: policy_loss=-0.0112, value_loss=0.9692, entropy=0.5293, kl_div=-0.1350
  Round 5/5: Mean predicted reward = 7.803

  === Progress Analysis ===
  Status: NORMAL

--- Round 39 Results ---
  Mean Oracle Reward: 7.856
  Min Oracle Reward: 5.081
  Max Oracle Reward: 9.256
  Std Oracle Reward: 0.897
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.291, Max: 0.432, Count: 13
  Total Sequences Evaluated: 1298

======================================================================
EXPERIMENT ROUND 40/50
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1298

--- Round 40 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ATATGGCC
  TGCTGCAA
  TACGTGCA
  CTGACAGT
  TAGCTCAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.492
  Max reward: 10.165
  With intrinsic bonuses: 8.510

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9682, entropy=0.5566, kl_div=0.0000
    Epoch 1: policy_loss=0.6642, value_loss=0.9682, entropy=0.5882, kl_div=-0.8047

=== Surrogate Model Training ===
Total samples: 1330

Training on 1269 samples (removed 61 outliers)
Reward range: [5.69, 10.62], mean: 8.26
  Created 13 candidate models for data size 1269
  rf-tuned-l: R2 = 0.324 (std: 0.025)
  rf-tuned-xl: R2 = 0.316 (std: 0.028)
  gb-tuned-l: R2 = 0.272 (std: 0.026)
  gb-tuned-xl: R2 = 0.272 (std: 0.026)
  xgb-xl: R2 = 0.411 (std: 0.057)
  xgb-l: R2 = 0.411 (std: 0.057)
  mlp-adaptive-xl: R2 = 0.280 (std: 0.034)
  mlp-l: R2 = 0.327 (std: 0.022)
  svr-rbf-xl: R2 = 0.431 (std: 0.023)
  svr-poly-l: R2 = 0.431 (std: 0.023)
  knn-tuned-sqrt: R2 = 0.142 (std: 0.042)
  knn-tuned-l: R2 = 0.142 (std: 0.042)
  ridge: R2 = 0.001 (std: 0.072)

Model-based training with 13 models
Best R2: 0.431, Mean R2: 0.289
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9672, entropy=0.5869, kl_div=0.0000
    Epoch 1: policy_loss=-0.1088, value_loss=0.9672, entropy=0.6106, kl_div=-0.6534
  Round 1/5: Mean predicted reward = 6.040
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9689, entropy=0.6095, kl_div=0.0000
    Epoch 1: policy_loss=0.1447, value_loss=0.9689, entropy=0.6400, kl_div=-0.8023
  Round 2/5: Mean predicted reward = 6.706
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9679, entropy=0.6705, kl_div=0.0000
    Epoch 1: policy_loss=-0.0300, value_loss=0.9679, entropy=0.6866, kl_div=-0.3591
  Round 3/5: Mean predicted reward = 7.002
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9679, entropy=0.6850, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2914
  Round 4/5: Mean predicted reward = 7.557
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9706, entropy=0.6417, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.5787
  Round 5/5: Mean predicted reward = 7.860

  === Progress Analysis ===
  Status: NORMAL

--- Round 40 Results ---
  Mean Oracle Reward: 8.505
  Min Oracle Reward: 6.083
  Max Oracle Reward: 10.283
  Std Oracle Reward: 0.983
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.289, Max: 0.431, Count: 13
  Total Sequences Evaluated: 1330

======================================================================
EXPERIMENT ROUND 41/50
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
  TAACGTGC
  ATAGTCGC
  TGAGCCTA
  ACCGGTAT
  TAAGGGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.305
  Max reward: 10.008
  With intrinsic bonuses: 8.299

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9687, entropy=0.6295, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.8746

=== Surrogate Model Training ===
Total samples: 1362

Training on 1300 samples (removed 62 outliers)
Reward range: [5.69, 10.62], mean: 8.26
  Created 13 candidate models for data size 1300
  rf-tuned-l: R2 = 0.334 (std: 0.049)
  rf-tuned-xl: R2 = 0.327 (std: 0.043)
  gb-tuned-l: R2 = 0.281 (std: 0.025)
  gb-tuned-xl: R2 = 0.281 (std: 0.025)
  xgb-xl: R2 = 0.413 (std: 0.025)
  xgb-l: R2 = 0.413 (std: 0.025)
  mlp-adaptive-xl: R2 = 0.322 (std: 0.050)
  mlp-l: R2 = 0.348 (std: 0.038)
  svr-rbf-xl: R2 = 0.449 (std: 0.034)
  svr-poly-l: R2 = 0.449 (std: 0.034)
  knn-tuned-sqrt: R2 = 0.169 (std: 0.024)
  knn-tuned-l: R2 = 0.169 (std: 0.024)
  ridge: R2 = 0.011 (std: 0.071)

Model-based training with 13 models
Best R2: 0.449, Mean R2: 0.305
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.6304, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3808
  Round 1/5: Mean predicted reward = 6.192
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9688, entropy=0.6053, kl_div=0.0000
    Epoch 1: policy_loss=0.0181, value_loss=0.9688, entropy=0.5978, kl_div=-0.0533
  Round 2/5: Mean predicted reward = 6.633
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9698, entropy=0.5356, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2105
  Round 3/5: Mean predicted reward = 7.127
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.5181, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4518
  Round 4/5: Mean predicted reward = 7.486
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9673, entropy=0.5085, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2663
  Round 5/5: Mean predicted reward = 7.819

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 41 Results ---
  Mean Oracle Reward: 8.262
  Min Oracle Reward: 3.507
  Max Oracle Reward: 9.925
  Std Oracle Reward: 1.175
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.305, Max: 0.449, Count: 13
  Total Sequences Evaluated: 1362

======================================================================
EXPERIMENT ROUND 42/50
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1362

--- Round 42 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.938) ---
  GAACCTTG
  ATAAGCTG
  CAGTGCTA
  CCAGATGT
  AGTCTCGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.671
  Max reward: 11.018
  With intrinsic bonuses: 8.628

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9693, entropy=0.5191, kl_div=0.0000
    Epoch 1: policy_loss=-0.0621, value_loss=0.9693, entropy=0.5157, kl_div=0.0449

=== Surrogate Model Training ===
Total samples: 1394

Training on 1329 samples (removed 65 outliers)
Reward range: [5.69, 10.62], mean: 8.27
  Created 13 candidate models for data size 1329
  rf-tuned-l: R2 = 0.340 (std: 0.017)
  rf-tuned-xl: R2 = 0.348 (std: 0.013)
  gb-tuned-l: R2 = 0.295 (std: 0.030)
  gb-tuned-xl: R2 = 0.295 (std: 0.030)
  xgb-xl: R2 = 0.422 (std: 0.030)
  xgb-l: R2 = 0.422 (std: 0.030)
  mlp-adaptive-xl: R2 = 0.353 (std: 0.064)
  mlp-l: R2 = 0.345 (std: 0.019)
  svr-rbf-xl: R2 = 0.454 (std: 0.025)
  svr-poly-l: R2 = 0.454 (std: 0.025)
  knn-tuned-sqrt: R2 = 0.187 (std: 0.026)
  knn-tuned-l: R2 = 0.187 (std: 0.026)
  ridge: R2 = 0.016 (std: 0.068)

Model-based training with 13 models
Best R2: 0.454, Mean R2: 0.317
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.4561, kl_div=0.0000
    Epoch 1: policy_loss=0.0744, value_loss=0.9696, entropy=0.4660, kl_div=-0.6583
  Round 1/5: Mean predicted reward = 6.286
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.5364, kl_div=0.0000
    Epoch 1: policy_loss=0.0403, value_loss=0.9705, entropy=0.5479, kl_div=-0.3440
  Round 2/5: Mean predicted reward = 6.757
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9695, entropy=0.5380, kl_div=0.0000
    Epoch 1: policy_loss=-0.0363, value_loss=0.9695, entropy=0.5458, kl_div=-0.2777
  Round 3/5: Mean predicted reward = 7.110
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9709, entropy=0.5524, kl_div=0.0000
    Epoch 1: policy_loss=0.0475, value_loss=0.9709, entropy=0.5583, kl_div=-0.1893
  Round 4/5: Mean predicted reward = 7.421
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.5630, kl_div=0.0000
    Epoch 1: policy_loss=-0.0459, value_loss=0.9698, entropy=0.5645, kl_div=-0.0465
  Round 5/5: Mean predicted reward = 7.794

  === Progress Analysis ===
  Status: NORMAL

--- Round 42 Results ---
  Mean Oracle Reward: 8.639
  Min Oracle Reward: 5.169
  Max Oracle Reward: 11.083
  Std Oracle Reward: 1.258
  Sequence Diversity: 0.938
  Models Used: 13
  Model R² - Mean: 0.317, Max: 0.454, Count: 13
  New best mean reward!
  Total Sequences Evaluated: 1394

======================================================================
EXPERIMENT ROUND 43/50
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1394

--- Round 43 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TATCCGAG
  TCGCAATG
  AGCAGCTT
  GTACGTAC
  GCGAATTC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.032
  Max reward: 12.534
  With intrinsic bonuses: 8.076

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9705, entropy=0.5603, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2085

=== Surrogate Model Training ===
Total samples: 1426

Training on 1355 samples (removed 71 outliers)
Reward range: [5.69, 10.62], mean: 8.27
  Created 13 candidate models for data size 1355
  rf-tuned-l: R2 = 0.341 (std: 0.009)
  rf-tuned-xl: R2 = 0.346 (std: 0.020)
  gb-tuned-l: R2 = 0.297 (std: 0.029)
  gb-tuned-xl: R2 = 0.297 (std: 0.029)
  xgb-xl: R2 = 0.427 (std: 0.032)
  xgb-l: R2 = 0.427 (std: 0.032)
  mlp-adaptive-xl: R2 = 0.318 (std: 0.037)
  mlp-l: R2 = 0.349 (std: 0.053)
  svr-rbf-xl: R2 = 0.460 (std: 0.023)
  svr-poly-l: R2 = 0.460 (std: 0.023)
  knn-tuned-sqrt: R2 = 0.186 (std: 0.039)
  knn-tuned-l: R2 = 0.186 (std: 0.039)
  ridge: R2 = 0.018 (std: 0.065)

Model-based training with 13 models
Best R2: 0.460, Mean R2: 0.316
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.5237, kl_div=0.0000
    Epoch 1: policy_loss=-0.0098, value_loss=0.9701, entropy=0.5241, kl_div=0.0265
  Round 1/5: Mean predicted reward = 6.013
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.5089, kl_div=0.0000
    Epoch 1: policy_loss=-0.0104, value_loss=0.9701, entropy=0.5194, kl_div=-0.2528
  Round 2/5: Mean predicted reward = 6.692
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=0.5517, kl_div=0.0000
    Epoch 1: policy_loss=-0.0232, value_loss=0.9704, entropy=0.5622, kl_div=-0.2440
  Round 3/5: Mean predicted reward = 7.081
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.6078, kl_div=0.0000
    Epoch 1: policy_loss=-0.0278, value_loss=0.9692, entropy=0.6116, kl_div=-0.0723
  Round 4/5: Mean predicted reward = 7.415
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9697, entropy=0.6178, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0820
  Round 5/5: Mean predicted reward = 7.944

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 43 Results ---
  Mean Oracle Reward: 8.016
  Min Oracle Reward: 4.217
  Max Oracle Reward: 12.130
  Std Oracle Reward: 1.769
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.316, Max: 0.460, Count: 13
  Total Sequences Evaluated: 1426

======================================================================
EXPERIMENT ROUND 44/50
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1426

--- Round 44 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCTAATCG
  GCTAAGCT
  CAGTTACG
  GATAGTCA
  ACCTGGAT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.565
  Max reward: 10.230
  With intrinsic bonuses: 8.531

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9681, entropy=0.5781, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0715

=== Surrogate Model Training ===
Total samples: 1458

Training on 1386 samples (removed 72 outliers)
Reward range: [5.69, 10.62], mean: 8.28
  Created 13 candidate models for data size 1386
  rf-tuned-l: R2 = 0.362 (std: 0.019)
  rf-tuned-xl: R2 = 0.360 (std: 0.019)
  gb-tuned-l: R2 = 0.301 (std: 0.037)
  gb-tuned-xl: R2 = 0.301 (std: 0.037)
  xgb-xl: R2 = 0.442 (std: 0.024)
  xgb-l: R2 = 0.442 (std: 0.024)
  mlp-adaptive-xl: R2 = 0.386 (std: 0.044)
  mlp-l: R2 = 0.363 (std: 0.052)
  svr-rbf-xl: R2 = 0.467 (std: 0.029)
  svr-poly-l: R2 = 0.467 (std: 0.029)
  knn-tuned-sqrt: R2 = 0.197 (std: 0.049)
  knn-tuned-l: R2 = 0.197 (std: 0.049)
  ridge: R2 = 0.009 (std: 0.063)

Model-based training with 13 models
Best R2: 0.467, Mean R2: 0.330
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9706, entropy=0.5491, kl_div=0.0000
    Epoch 1: policy_loss=0.0061, value_loss=0.9706, entropy=0.5487, kl_div=0.0133
  Round 1/5: Mean predicted reward = 6.140
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9710, entropy=0.5747, kl_div=0.0000
    Epoch 1: policy_loss=-0.0287, value_loss=0.9710, entropy=0.5782, kl_div=-0.0794
  Round 2/5: Mean predicted reward = 6.510
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.5985, kl_div=0.0000
    Epoch 1: policy_loss=-0.0354, value_loss=0.9698, entropy=0.6016, kl_div=-0.0998
  Round 3/5: Mean predicted reward = 6.899
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.5991, kl_div=0.0000
    Epoch 1: policy_loss=-0.0028, value_loss=0.9695, entropy=0.6049, kl_div=-0.1336
  Round 4/5: Mean predicted reward = 7.480
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.5783, kl_div=0.0000
    Epoch 1: policy_loss=-0.0085, value_loss=0.9695, entropy=0.5803, kl_div=-0.0570
  Round 5/5: Mean predicted reward = 7.796

  === Progress Analysis ===
  Status: NORMAL

--- Round 44 Results ---
  Mean Oracle Reward: 8.519
  Min Oracle Reward: 5.927
  Max Oracle Reward: 10.256
  Std Oracle Reward: 0.955
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.330, Max: 0.467, Count: 13
  Total Sequences Evaluated: 1458

======================================================================
EXPERIMENT ROUND 45/50
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1458

--- Round 45 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  TGCAATCG
  AATGTGAC
  GGTCATAC
  CAAGTCTG
  GTACCTAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.486
  Max reward: 10.467
  With intrinsic bonuses: 8.501

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9675, entropy=0.6341, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0519

=== Surrogate Model Training ===
Total samples: 1490

Training on 1417 samples (removed 73 outliers)
Reward range: [5.69, 10.62], mean: 8.29
  Created 13 candidate models for data size 1417
  rf-tuned-l: R2 = 0.371 (std: 0.033)
  rf-tuned-xl: R2 = 0.368 (std: 0.033)
  gb-tuned-l: R2 = 0.308 (std: 0.037)
  gb-tuned-xl: R2 = 0.308 (std: 0.037)
  xgb-xl: R2 = 0.474 (std: 0.040)
  xgb-l: R2 = 0.474 (std: 0.040)
  mlp-adaptive-xl: R2 = 0.385 (std: 0.045)
  mlp-l: R2 = 0.386 (std: 0.038)
  svr-rbf-xl: R2 = 0.466 (std: 0.026)
  svr-poly-l: R2 = 0.466 (std: 0.026)
  knn-tuned-sqrt: R2 = 0.206 (std: 0.045)
  knn-tuned-l: R2 = 0.206 (std: 0.045)
  ridge: R2 = 0.002 (std: 0.067)

Model-based training with 13 models
Best R2: 0.474, Mean R2: 0.340
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9708, entropy=0.5977, kl_div=0.0000
    Epoch 1: policy_loss=0.0079, value_loss=0.9708, entropy=0.6134, kl_div=-0.4933
  Round 1/5: Mean predicted reward = 6.078
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9704, entropy=0.5827, kl_div=0.0000
    Epoch 1: policy_loss=-0.0728, value_loss=0.9704, entropy=0.5950, kl_div=-0.3174
  Round 2/5: Mean predicted reward = 6.164
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9705, entropy=0.6342, kl_div=0.0000
    Epoch 1: policy_loss=-0.0310, value_loss=0.9704, entropy=0.6476, kl_div=-0.3066
  Round 3/5: Mean predicted reward = 6.890
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9698, entropy=0.6177, kl_div=0.0000
    Epoch 1: policy_loss=0.0007, value_loss=0.9698, entropy=0.6236, kl_div=-0.1745
  Round 4/5: Mean predicted reward = 7.357
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9692, entropy=0.6170, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6247
  Round 5/5: Mean predicted reward = 7.852

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 45 Results ---
  Mean Oracle Reward: 8.470
  Min Oracle Reward: 5.690
  Max Oracle Reward: 10.426
  Std Oracle Reward: 1.005
  Sequence Diversity: 1.000
  Models Used: 13
  Model R² - Mean: 0.340, Max: 0.474, Count: 13
  Total Sequences Evaluated: 1490

======================================================================
EXPERIMENT ROUND 46/50
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 1490

--- Round 46 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  AATGCGTC
  GACGACTT
  ATCGGCAT
  GATCTGAA
  AGTCGTAC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.274
  Max reward: 10.235
  With intrinsic bonuses: 8.331

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9684, entropy=0.6523, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4981

=== Surrogate Model Training ===
Total samples: 1522

Training on 1445 samples (removed 77 outliers)
Reward range: [5.73, 10.62], mean: 8.30
  Created 13 candidate models for data size 1445
  rf-tuned-l: R2 = 0.388 (std: 0.048)
  rf-tuned-xl: R2 = 0.380 (std: 0.047)
  gb-tuned-l: R2 = 0.314 (std: 0.049)
  gb-tuned-xl: R2 = 0.314 (std: 0.049)
  xgb-xl: R2 = 0.483 (std: 0.043)
  xgb-l: R2 = 0.483 (std: 0.043)
  mlp-adaptive-xl: R2 = 0.381 (std: 0.010)
  mlp-l: R2 = 0.378 (std: 0.026)
  svr-rbf-xl: R2 = 0.470 (std: 0.037)
  svr-poly-l: R2 = 0.470 (std: 0.037)
  knn-tuned-sqrt: R2 = 0.204 (std: 0.062)
  knn-tuned-l: R2 = 0.204 (std: 0.062)
  ridge: R2 = -0.004 (std: 0.071)

Model-based training with 12 models
Best R2: 0.483, Mean R2: 0.343
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.5711, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2005
  Round 1/5: Mean predicted reward = 5.758
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9706, entropy=0.5538, kl_div=0.0000
    Epoch 1: policy_loss=-0.0750, value_loss=0.9706, entropy=0.5606, kl_div=-0.1205
  Round 2/5: Mean predicted reward = 6.556
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9701, entropy=0.6161, kl_div=0.0000
    Epoch 1: policy_loss=-0.0535, value_loss=0.9701, entropy=0.6364, kl_div=-0.4054
  Round 3/5: Mean predicted reward = 6.750
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9693, entropy=0.6618, kl_div=0.0000
    Epoch 1: policy_loss=-0.0300, value_loss=0.9693, entropy=0.6631, kl_div=-0.0922
  Round 4/5: Mean predicted reward = 7.478
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9689, entropy=0.6135, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4602
  Round 5/5: Mean predicted reward = 7.825

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 46 Results ---
  Mean Oracle Reward: 8.311
  Min Oracle Reward: 2.624
  Max Oracle Reward: 10.542
  Std Oracle Reward: 1.399
  Sequence Diversity: 0.969
  Models Used: 12
  Model R² - Mean: 0.343, Max: 0.483, Count: 13
  Total Sequences Evaluated: 1522

======================================================================
EXPERIMENT ROUND 47/50
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 1522

--- Round 47 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  ACCGTATG
  TAATACGG
  GCATATGC
  AAGTGCTC
  ATTAGGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.510
  Max reward: 10.260
  With intrinsic bonuses: 8.513

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9700, entropy=0.6122, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.4790

=== Surrogate Model Training ===
Total samples: 1554

Training on 1479 samples (removed 75 outliers)
Reward range: [5.69, 10.79], mean: 8.30
  Created 13 candidate models for data size 1479
  rf-tuned-l: R2 = 0.376 (std: 0.039)
  rf-tuned-xl: R2 = 0.377 (std: 0.032)
  gb-tuned-l: R2 = 0.306 (std: 0.050)
  gb-tuned-xl: R2 = 0.306 (std: 0.050)
  xgb-xl: R2 = 0.503 (std: 0.060)
  xgb-l: R2 = 0.503 (std: 0.060)
  mlp-adaptive-xl: R2 = 0.357 (std: 0.024)
  mlp-l: R2 = 0.371 (std: 0.032)
  svr-rbf-xl: R2 = 0.478 (std: 0.029)
  svr-poly-l: R2 = 0.478 (std: 0.029)
  knn-tuned-sqrt: R2 = 0.203 (std: 0.061)
  knn-tuned-l: R2 = 0.203 (std: 0.061)
  ridge: R2 = -0.006 (std: 0.070)

Model-based training with 12 models
Best R2: 0.503, Mean R2: 0.343
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9704, entropy=0.6070, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2415
  Round 1/5: Mean predicted reward = 5.845
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=0.6089, kl_div=0.0000
    Epoch 1: policy_loss=-0.0412, value_loss=0.9709, entropy=0.6128, kl_div=-0.0581
  Round 2/5: Mean predicted reward = 6.483
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9702, entropy=0.6042, kl_div=0.0000
    Epoch 1: policy_loss=-0.0760, value_loss=0.9702, entropy=0.6158, kl_div=-0.4013
  Round 3/5: Mean predicted reward = 6.715
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9695, entropy=0.6680, kl_div=0.0000
    Epoch 1: policy_loss=0.0116, value_loss=0.9695, entropy=0.6715, kl_div=-0.1600
  Round 4/5: Mean predicted reward = 7.379
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.6058, kl_div=0.0000
    Epoch 1: policy_loss=-0.0038, value_loss=0.9691, entropy=0.6023, kl_div=0.0412
  Round 5/5: Mean predicted reward = 7.880

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 47 Results ---
  Mean Oracle Reward: 8.529
  Min Oracle Reward: 4.216
  Max Oracle Reward: 10.290
  Std Oracle Reward: 1.310
  Sequence Diversity: 1.000
  Models Used: 12
  Model R² - Mean: 0.343, Max: 0.503, Count: 13
  Total Sequences Evaluated: 1554

======================================================================
EXPERIMENT ROUND 48/50
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 1554

--- Round 48 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GACCTTAG
  GGTACACG
  AGTACTGC
  GCTGAATC
  ATACGAGT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.225
  Max reward: 10.653
  With intrinsic bonuses: 7.209

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9662, entropy=0.6591, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1068

=== Surrogate Model Training ===
Total samples: 1586

Training on 1507 samples (removed 79 outliers)
Reward range: [5.69, 10.81], mean: 8.30
  Created 13 candidate models for data size 1507
  rf-tuned-l: R2 = 0.386 (std: 0.040)
  rf-tuned-xl: R2 = 0.393 (std: 0.030)
  gb-tuned-l: R2 = 0.302 (std: 0.040)
  gb-tuned-xl: R2 = 0.302 (std: 0.040)
  xgb-xl: R2 = 0.495 (std: 0.040)
  xgb-l: R2 = 0.495 (std: 0.040)
  mlp-adaptive-xl: R2 = 0.338 (std: 0.041)
  mlp-l: R2 = 0.326 (std: 0.057)
  svr-rbf-xl: R2 = 0.488 (std: 0.027)
  svr-poly-l: R2 = 0.488 (std: 0.027)
  knn-tuned-sqrt: R2 = 0.202 (std: 0.052)
  knn-tuned-l: R2 = 0.202 (std: 0.052)
  ridge: R2 = -0.005 (std: 0.064)

Model-based training with 12 models
Best R2: 0.495, Mean R2: 0.339
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9700, entropy=0.6550, kl_div=0.0000
    Epoch 1: policy_loss=-0.0242, value_loss=0.9700, entropy=0.6568, kl_div=-0.0233
  Round 1/5: Mean predicted reward = 5.815
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9709, entropy=0.6507, kl_div=0.0000
    Epoch 1: policy_loss=-0.0628, value_loss=0.9709, entropy=0.6515, kl_div=-0.1068
  Round 2/5: Mean predicted reward = 6.392
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9703, entropy=0.6163, kl_div=0.0000
    Epoch 1: policy_loss=0.0363, value_loss=0.9703, entropy=0.6186, kl_div=-0.4368
  Round 3/5: Mean predicted reward = 6.931
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9690, entropy=0.5756, kl_div=0.0000
    Epoch 1: policy_loss=0.0506, value_loss=0.9690, entropy=0.5780, kl_div=-0.3541
  Round 4/5: Mean predicted reward = 7.261
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9683, entropy=0.6431, kl_div=0.0000
    Epoch 1: policy_loss=-0.0037, value_loss=0.9683, entropy=0.6473, kl_div=-0.1082
  Round 5/5: Mean predicted reward = 7.884

  === Progress Analysis ===
  Status: NORMAL
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 48 Results ---
  Mean Oracle Reward: 7.200
  Min Oracle Reward: 0.000
  Max Oracle Reward: 10.407
  Std Oracle Reward: 2.372
  Sequence Diversity: 1.000
  Models Used: 12
  Model R² - Mean: 0.339, Max: 0.495, Count: 13
  Total Sequences Evaluated: 1586

======================================================================
EXPERIMENT ROUND 49/50
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 1586

--- Round 49 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  GCTCGTAA
  CCGATAGT
  TCTACGGA
  TGCACATG
  CGCGAATT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 6.877
  Max reward: 10.205
  With intrinsic bonuses: 6.893

Policy Update:
  Adaptive update: clip_ratio=0.10, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9664, entropy=0.6860, kl_div=0.0000
    Epoch 1: policy_loss=-0.0250, value_loss=0.9664, entropy=0.6894, kl_div=-0.0143

=== Surrogate Model Training ===
Total samples: 1618

Training on 1534 samples (removed 84 outliers)
Reward range: [5.61, 10.81], mean: 8.29
  Created 13 candidate models for data size 1534
  rf-tuned-l: R2 = 0.387 (std: 0.034)
  rf-tuned-xl: R2 = 0.372 (std: 0.032)
  gb-tuned-l: R2 = 0.302 (std: 0.035)
  gb-tuned-xl: R2 = 0.302 (std: 0.035)
  xgb-xl: R2 = 0.487 (std: 0.058)
  xgb-l: R2 = 0.487 (std: 0.058)
  mlp-adaptive-xl: R2 = 0.420 (std: 0.058)
  mlp-l: R2 = 0.416 (std: 0.053)
  svr-rbf-xl: R2 = 0.491 (std: 0.025)
  svr-poly-l: R2 = 0.491 (std: 0.025)
  knn-tuned-sqrt: R2 = 0.203 (std: 0.066)
  knn-tuned-l: R2 = 0.203 (std: 0.066)
  ridge: R2 = -0.003 (std: 0.066)

Model-based training with 12 models
Best R2: 0.491, Mean R2: 0.351
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9688, entropy=0.6398, kl_div=0.0000
    Epoch 1: policy_loss=-0.0389, value_loss=0.9688, entropy=0.6440, kl_div=-0.0118
  Round 1/5: Mean predicted reward = 6.164
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9700, entropy=0.6804, kl_div=0.0000
    Epoch 1: policy_loss=-0.0011, value_loss=0.9700, entropy=0.6835, kl_div=-0.0122
  Round 2/5: Mean predicted reward = 6.378
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9701, entropy=0.6252, kl_div=0.0000
    Epoch 1: policy_loss=-0.0312, value_loss=0.9701, entropy=0.6273, kl_div=-0.0322
  Round 3/5: Mean predicted reward = 7.034
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9685, entropy=0.6814, kl_div=0.0000
    Epoch 1: policy_loss=0.0020, value_loss=0.9685, entropy=0.6819, kl_div=-0.0040
  Round 4/5: Mean predicted reward = 7.315
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9699, entropy=0.6696, kl_div=0.0000
    Epoch 1: policy_loss=-0.0244, value_loss=0.9699, entropy=0.6707, kl_div=0.0129
  Round 5/5: Mean predicted reward = 7.936

  === Progress Analysis ===
  Status: NORMAL

--- Round 49 Results ---
  Mean Oracle Reward: 6.870
  Min Oracle Reward: 0.000
  Max Oracle Reward: 9.981
  Std Oracle Reward: 2.451
  Sequence Diversity: 1.000
  Models Used: 12
  Model R² - Mean: 0.351, Max: 0.491, Count: 13
  Total Sequences Evaluated: 1618

======================================================================
EXPERIMENT ROUND 50/50
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 1618

--- Round 50 Configuration ---
Learning rate: 0.000300
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  TTCACGGA
  TAGGACTC
  GAACTGTC
  GCGTACTA
  TGCACTAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.685
  Max reward: 10.243
  With intrinsic bonuses: 7.705

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9680, entropy=0.6840, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2176

=== Surrogate Model Training ===
Total samples: 1650

Training on 1564 samples (removed 86 outliers)
Reward range: [5.61, 10.81], mean: 8.29
  Created 13 candidate models for data size 1564
  rf-tuned-l: R2 = 0.395 (std: 0.029)
  rf-tuned-xl: R2 = 0.401 (std: 0.027)
  gb-tuned-l: R2 = 0.308 (std: 0.034)
  gb-tuned-xl: R2 = 0.308 (std: 0.034)
  xgb-xl: R2 = 0.492 (std: 0.064)
  xgb-l: R2 = 0.492 (std: 0.064)
  mlp-adaptive-xl: R2 = 0.419 (std: 0.060)
  mlp-l: R2 = 0.419 (std: 0.025)
  svr-rbf-xl: R2 = 0.502 (std: 0.025)
  svr-poly-l: R2 = 0.502 (std: 0.025)
  knn-tuned-sqrt: R2 = 0.199 (std: 0.070)
  knn-tuned-l: R2 = 0.199 (std: 0.070)
  ridge: R2 = 0.000 (std: 0.070)

Model-based training with 13 models
Best R2: 0.502, Mean R2: 0.357
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9691, entropy=0.6613, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1123
  Round 1/5: Mean predicted reward = 5.692
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9706, entropy=0.6499, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.3568
  Round 2/5: Mean predicted reward = 6.420
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9696, entropy=0.6904, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.6531
  Round 3/5: Mean predicted reward = 6.852
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9710, entropy=0.6189, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.9185
  Round 4/5: Mean predicted reward = 7.371
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9692, entropy=0.5954, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 1.1849
  Round 5/5: Mean predicted reward = 7.762

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 50 Results ---
  Mean Oracle Reward: 7.770
  Min Oracle Reward: 4.304
  Max Oracle Reward: 10.334
  Std Oracle Reward: 1.516
  Sequence Diversity: 0.969
  Models Used: 13
  Model R² - Mean: 0.357, Max: 0.502, Count: 13
  Total Sequences Evaluated: 1650

======================================================================
DyNA PPO ALGORITHM COMPLETE!
======================================================================
Total rounds executed: 50
Total sequences evaluated: 1650
Best mean reward: 8.639 (achieved at round 42)

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 50
Final Mean Reward: 7.7703
Best Mean Reward: 8.6389
Best Max Reward: 12.1302
Initial Lr: 0.0003
Final Lr: 0.0003
Total Updates: 437
Final Diversity: 0.9688
Convergence Round: 11
==================================================

Generating learning curves...
Learning curves saved to learning_curves.png
Saving training metrics...
Metrics saved to training_metrics.json

======================================================================
FINAL OPTIMIZED SEQUENCES
======================================================================

Deterministic (Exploitation):
  GCGAGCGC: 7.918
  GCGAGCGC: 8.189
  GCGAGCGC: 8.198
  GCGAGCGC: 8.139
  GCGAGCGC: 7.958

Stochastic (Exploration):
  GCGGACGT: 8.196
  GACGTCGC: 8.388
  GACGTCGG: 7.708
  AGCGGAGG: 7.538
  GCATGCGC: 9.084

Final Performance:
  Mean reward: 8.132
  Max reward: 9.084
  Std reward: 0.399

Best sequence found: GCATGCGC
   Reward: 9.084

======================================================================
Training complete! Check 'learning_curves.png' and 'training_metrics.json'
======================================================================