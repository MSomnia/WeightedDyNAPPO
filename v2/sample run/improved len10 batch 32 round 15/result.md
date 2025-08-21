======================================================================
RUNNING IMPROVED DyNA PPO WITH BETTER SURROGATE LEARNING
======================================================================
======================================================================
IMPROVED DyNA PPO ALGORITHM
======================================================================
Configuration:
  Number of experiment rounds N = 15
  Number of model-based training rounds M = 5
  Minimum model score τ = 0.2
  Batch size B = 32
  Warm-up phase: True
======================================================================

=== WARM-UP PHASE ===
Generating 50 warm-up samples...
Warm-up statistics:
  Mean reward: 6.478
  Std reward: 1.907
  Min/Max: 0.000 / 9.099

Pre-training surrogate models on warm-up data...

Round 0: Evaluating 7 models
Data size: 50, Feature dim: 57
Threshold: R² > -0.500, Min models: 1
  knn: R² = 0.411
  knn: R² = 0.279
  knn: R² = 0.232
  rf: R² = 0.710
  rf: R² = 0.761
  gb: R² = 0.729
  ridge: R² = 0.424

Selected 7 models for ensemble
Models: ['knn', 'knn', 'knn', 'rf', 'rf', 'gb', 'ridge']
Scores: ['0.411', '0.279', '0.232', '0.710', '0.761', '0.729', '0.424']
Initial models trained: 7
Initial R² scores - Mean: 0.507, Max: 0.761

======================================================================
EXPERIMENT ROUND 1/15
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.300
Total data collected: 50

--- Round 1 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  GAGAATGA
  GCTCGCAT
  TATGCTGA
  AGCAGTCG
  CACATGAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.670
  Max reward: 10.195
  With intrinsic bonuses: 7.601

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9863, entropy=1.3853, kl_div=0.0000
    Epoch 2: policy_loss=-0.1946, value_loss=0.9850, entropy=1.3809, kl_div=0.0397
    Epoch 4: policy_loss=-0.2193, value_loss=0.9839, entropy=1.3784, kl_div=0.0201
    Epoch 6: policy_loss=-0.2244, value_loss=0.9828, entropy=1.3772, kl_div=0.0006

=== Surrogate Model Training ===
Total samples: 82

Training on 80 samples (removed 2 outliers)
Reward range: [3.36, 10.20], mean: 7.09
  rf_simple: R² = 0.542 (std: 0.141)
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\gaussian_process\kernels.py:442: ConvergenceWarning: The optimal value found for dimension 0 of parameter k2__length_scale is close to the specified lower bound 1e-05. Decreasing the bound and calling fit again may find a better value.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\gaussian_process\kernels.py:442: ConvergenceWarning: The optimal value found for dimension 0 of parameter k2__length_scale is close to the specified lower bound 1e-05. Decreasing the bound and calling fit again may find a better value.
  warnings.warn(
C:\Users\linle\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\gaussian_process\kernels.py:442: ConvergenceWarning: The optimal value found for dimension 0 of parameter k2__length_scale is close to the specified lower bound 1e-05. Decreasing the bound and calling fit again may find a better value.
  warnings.warn(
  gp: R² = -31.029 (std: 26.364)
  poly_ridge: R² = 0.369 (std: 0.086)

Model-based training with 2 models
Best R²: 0.542, Mean R²: -10.040
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9777, entropy=1.3757, kl_div=0.0000
    Epoch 1: policy_loss=-0.0754, value_loss=0.9773, entropy=1.3725, kl_div=0.0156
  Round 1/5: Mean predicted reward = 7.361
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9773, entropy=1.3662, kl_div=0.0000
    Epoch 1: policy_loss=-0.0668, value_loss=0.9770, entropy=1.3572, kl_div=0.0476
  Round 2/5: Mean predicted reward = 7.351
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9798, entropy=1.3476, kl_div=0.0000
    Epoch 1: policy_loss=-0.0878, value_loss=0.9795, entropy=1.3323, kl_div=0.0462
  Round 3/5: Mean predicted reward = 7.372
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9792, entropy=1.3161, kl_div=0.0000
    Epoch 1: policy_loss=-0.0077, value_loss=0.9789, entropy=1.3000, kl_div=0.0459
  Round 4/5: Mean predicted reward = 7.515
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9807, entropy=1.2879, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0657
  Round 5/5: Mean predicted reward = 7.481

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 1 Results ---
  Mean Oracle Reward: 7.683
  Min Oracle Reward: 5.414
  Max Oracle Reward: 10.180
  Std Oracle Reward: 1.170
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -10.040, Max: 0.542, Count: 3
New best mean reward!
  Total Sequences Evaluated: 82

======================================================================
EXPERIMENT ROUND 2/15
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.300
Total data collected: 82

--- Round 2 Configuration ---
Learning rate: 0.000200
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  GATTACTC
  GCCGCGGA
  AGAGCAGG
  ATGTACAT
  CTCCCATC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.577
  Max reward: 11.226
  With intrinsic bonuses: 7.570

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9787, entropy=1.2761, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0644

=== Surrogate Model Training ===
Total samples: 114

Training on 110 samples (removed 4 outliers)
Reward range: [3.35, 10.20], mean: 7.24
  rf_tuned: R² = 0.639 (std: 0.047)
  gb_tuned: R² = 0.834 (std: 0.056)
  ensemble: R² = 0.822 (std: 0.053)

Model-based training with 3 models
Best R²: 0.834, Mean R²: 0.765
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9805, entropy=1.2725, kl_div=0.0000
    Epoch 1: policy_loss=-0.0136, value_loss=0.9803, entropy=1.2677, kl_div=0.0134
  Round 1/5: Mean predicted reward = 7.444
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9805, entropy=1.2594, kl_div=0.0000
    Epoch 1: policy_loss=-0.0467, value_loss=0.9803, entropy=1.2571, kl_div=0.0116
  Round 2/5: Mean predicted reward = 7.612
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9799, entropy=1.2593, kl_div=0.0000
    Epoch 1: policy_loss=-0.0454, value_loss=0.9797, entropy=1.2566, kl_div=0.0194
  Round 3/5: Mean predicted reward = 7.432
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9791, entropy=1.2618, kl_div=0.0000
    Epoch 1: policy_loss=-0.0475, value_loss=0.9789, entropy=1.2588, kl_div=0.0370
  Round 4/5: Mean predicted reward = 7.346
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9817, entropy=1.2550, kl_div=0.0000
    Epoch 1: policy_loss=-0.0581, value_loss=0.9816, entropy=1.2509, kl_div=0.0292
  Round 5/5: Mean predicted reward = 7.670

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 2 Results ---
  Mean Oracle Reward: 7.568
  Min Oracle Reward: 1.317
  Max Oracle Reward: 11.142
  Std Oracle Reward: 1.699
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: 0.765, Max: 0.834, Count: 3
  Total Sequences Evaluated: 114

======================================================================
EXPERIMENT ROUND 3/15
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.300
Total data collected: 114

--- Round 3 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0200
Exploration rate: 0.300

--- Generated Sequences (Diversity: 1.000) ---
  CGCGGCTT
  AACCTACT
  GCGCTTAT
  CCGCTGCC
  TTGCTTAG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 7.950
  Max reward: 9.347
  With intrinsic bonuses: 8.105

Policy Update:
  Adaptive update: clip_ratio=0.30, entropy_coef=0.020
    Epoch 0: policy_loss=-0.0000, value_loss=0.9778, entropy=1.2443, kl_div=0.0000
    Early stopping at epoch 2: KL divergence = 0.0522

=== Surrogate Model Training ===
Total samples: 146

Training on 138 samples (removed 8 outliers)
Reward range: [4.14, 10.20], mean: 7.52
  rf_tuned: R² = 0.631 (std: 0.082)
  gb_tuned: R² = 0.797 (std: 0.069)
  ensemble: R² = 0.729 (std: 0.128)

Model-based training with 3 models
Best R²: 0.797, Mean R²: 0.719
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9782, entropy=1.2356, kl_div=0.0000
    Epoch 1: policy_loss=-0.0234, value_loss=0.9781, entropy=1.2289, kl_div=0.0323
  Round 1/5: Mean predicted reward = 7.906
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9766, entropy=1.2291, kl_div=0.0000
    Epoch 1: policy_loss=-0.0298, value_loss=0.9766, entropy=1.2220, kl_div=0.0322
  Round 2/5: Mean predicted reward = 7.371
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9749, entropy=1.2036, kl_div=0.0000
    Epoch 1: policy_loss=-0.0301, value_loss=0.9749, entropy=1.1975, kl_div=0.0438
  Round 3/5: Mean predicted reward = 7.865
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9771, entropy=1.1873, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0591
  Round 4/5: Mean predicted reward = 7.656
  Adaptive update: clip_ratio=0.30, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9773, entropy=1.1928, kl_div=0.0000
    Epoch 1: policy_loss=-0.0364, value_loss=0.9772, entropy=1.1871, kl_div=0.0451
  Round 5/5: Mean predicted reward = 7.659

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 3 Results ---
  Mean Oracle Reward: 7.974
  Min Oracle Reward: 6.349
  Max Oracle Reward: 9.287
  Std Oracle Reward: 0.722
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: 0.719, Max: 0.797, Count: 3
New best mean reward!
  Total Sequences Evaluated: 146

======================================================================
EXPERIMENT ROUND 4/15
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.280
Total data collected: 146

--- Round 4 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0100
Exploration rate: 0.280

--- Generated Sequences (Diversity: 1.000) ---
  GTACGCAT
  CGAGATCT
  TGATGACC
  TTGACAGC
  CACGTGTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.295
  Max reward: 9.945
  With intrinsic bonuses: 8.437

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9776, entropy=1.1795, kl_div=0.0000
    Epoch 1: policy_loss=-0.0035, value_loss=0.9775, entropy=1.1777, kl_div=0.0118
    Epoch 2: policy_loss=-0.0093, value_loss=0.9775, entropy=1.1757, kl_div=0.0246
    Epoch 3: policy_loss=-0.0171, value_loss=0.9775, entropy=1.1737, kl_div=0.0382

=== Surrogate Model Training ===
Total samples: 178

Training on 168 samples (removed 10 outliers)
Reward range: [4.55, 10.20], mean: 7.71
  rf_tuned: R² = 0.705 (std: 0.054)
  gb_tuned: R² = 0.828 (std: 0.028)
  ensemble: R² = 0.763 (std: 0.066)

Model-based training with 3 models
Best R²: 0.828, Mean R²: 0.765
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9762, entropy=1.1526, kl_div=0.0000
    Epoch 1: policy_loss=-0.0148, value_loss=0.9762, entropy=1.1502, kl_div=0.0230
  Round 1/5: Mean predicted reward = 7.724
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9770, entropy=1.1560, kl_div=0.0000
    Epoch 1: policy_loss=-0.0143, value_loss=0.9770, entropy=1.1534, kl_div=0.0240
  Round 2/5: Mean predicted reward = 7.935
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9806, entropy=1.1482, kl_div=0.0000
    Epoch 1: policy_loss=0.0009, value_loss=0.9806, entropy=1.1461, kl_div=0.0189
  Round 3/5: Mean predicted reward = 7.954
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9748, entropy=1.1457, kl_div=0.0000
    Epoch 1: policy_loss=-0.0152, value_loss=0.9748, entropy=1.1440, kl_div=0.0173
  Round 4/5: Mean predicted reward = 7.912
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9818, entropy=1.1476, kl_div=0.0000
    Epoch 1: policy_loss=-0.0031, value_loss=0.9817, entropy=1.1463, kl_div=0.0097
  Round 5/5: Mean predicted reward = 8.121

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 4 Results ---
  Mean Oracle Reward: 8.298
  Min Oracle Reward: 6.290
  Max Oracle Reward: 9.778
  Std Oracle Reward: 0.848
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: 0.765, Max: 0.828, Count: 3
New best mean reward!
  Total Sequences Evaluated: 178

======================================================================
EXPERIMENT ROUND 5/15
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
  ATGCCAGT
  GGTAACCT
  GGACATGC
  GTAGCAGC
  TCCGAAGG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.125
  Max reward: 9.812
  With intrinsic bonuses: 8.237

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9760, entropy=1.1451, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0700

=== Surrogate Model Training ===
Total samples: 210

Training on 198 samples (removed 12 outliers)
Reward range: [4.71, 10.20], mean: 7.81
  rf_tuned: R² = 0.702 (std: 0.062)
  gb_tuned: R² = 0.803 (std: 0.077)
  ensemble: R² = 0.730 (std: 0.085)

Model-based training with 3 models
Best R²: 0.803, Mean R²: 0.745
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9803, entropy=1.1402, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0683
  Round 1/5: Mean predicted reward = 7.764
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9790, entropy=1.1245, kl_div=0.0000
    Epoch 1: policy_loss=-0.0472, value_loss=0.9789, entropy=1.1215, kl_div=0.0367
  Round 2/5: Mean predicted reward = 7.778
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9773, entropy=1.1290, kl_div=0.0000
    Epoch 1: policy_loss=-0.0696, value_loss=0.9773, entropy=1.1303, kl_div=-0.0136
  Round 3/5: Mean predicted reward = 7.899
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9765, entropy=1.1453, kl_div=0.0000
    Epoch 1: policy_loss=-0.0772, value_loss=0.9764, entropy=1.1472, kl_div=-0.0059
  Round 4/5: Mean predicted reward = 8.139
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9782, entropy=1.1529, kl_div=0.0000
    Epoch 1: policy_loss=-0.0093, value_loss=0.9781, entropy=1.1524, kl_div=-0.0448
  Round 5/5: Mean predicted reward = 8.277

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 5 Results ---
  Mean Oracle Reward: 8.124
  Min Oracle Reward: 4.134
  Max Oracle Reward: 9.839
  Std Oracle Reward: 1.125
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: 0.745, Max: 0.803, Count: 3
  Total Sequences Evaluated: 210

======================================================================
EXPERIMENT ROUND 6/15
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.220
Total data collected: 210

--- Round 6 Configuration ---
Learning rate: 0.000272
Entropy coefficient: 0.0100
Exploration rate: 0.220

--- Generated Sequences (Diversity: 1.000) ---
  ACTGGACT
  GATTAGCC
  CACGTAGT
  CGGTAACT
  CATGTACG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.162
  Max reward: 9.579
  With intrinsic bonuses: 8.344

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=-0.0000, value_loss=0.9775, entropy=1.1305, kl_div=0.0000
    Epoch 1: policy_loss=-0.0431, value_loss=0.9775, entropy=1.1256, kl_div=0.0386
    Early stopping at epoch 2: KL divergence = 0.1071

=== Surrogate Model Training ===
Total samples: 242

Training on 229 samples (removed 13 outliers)
Reward range: [4.76, 10.20], mean: 7.88
  rf_tuned: R² = 0.738 (std: 0.043)
  gb_tuned: R² = 0.830 (std: 0.030)
  ensemble: R² = 0.757 (std: 0.037)

Model-based training with 3 models
Best R²: 0.830, Mean R²: 0.775
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9766, entropy=1.1262, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0801
  Round 1/5: Mean predicted reward = 7.887
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9825, entropy=1.1129, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0649
  Round 2/5: Mean predicted reward = 7.975
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9764, entropy=1.1122, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0664
  Round 3/5: Mean predicted reward = 8.185
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9740, entropy=1.0838, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1299
  Round 4/5: Mean predicted reward = 8.285
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9757, entropy=1.0803, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1821
  Round 5/5: Mean predicted reward = 7.964

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 6 Results ---
  Mean Oracle Reward: 8.209
  Min Oracle Reward: 5.635
  Max Oracle Reward: 9.529
  Std Oracle Reward: 0.934
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: 0.775, Max: 0.830, Count: 3
  Total Sequences Evaluated: 242

======================================================================
EXPERIMENT ROUND 7/15
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
  ATGCCTGA
  CATGCAGT
  CTAATGCG
  TGACAGCT
  TCAGCGTA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.407
  Max reward: 9.590
  With intrinsic bonuses: 8.452

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.010
    Epoch 0: policy_loss=0.0000, value_loss=0.9733, entropy=1.0606, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0864

=== Surrogate Model Training ===
Total samples: 274

Training on 260 samples (removed 14 outliers)
Reward range: [5.00, 10.20], mean: 7.96
  rf_tuned: R² = 0.767 (std: 0.035)
  gb_tuned: R² = 0.854 (std: 0.037)
  ensemble: R² = 0.797 (std: 0.027)

Model-based training with 3 models
Best R²: 0.854, Mean R²: 0.806
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9807, entropy=1.0648, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0558
  Round 1/5: Mean predicted reward = 7.890
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9735, entropy=1.0430, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0610
  Round 2/5: Mean predicted reward = 7.892
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9785, entropy=1.0447, kl_div=0.0000
    Epoch 1: policy_loss=-0.0162, value_loss=0.9784, entropy=1.0396, kl_div=0.0391
  Round 3/5: Mean predicted reward = 8.141
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9740, entropy=1.0279, kl_div=0.0000
    Epoch 1: policy_loss=-0.0289, value_loss=0.9739, entropy=1.0226, kl_div=0.0438
  Round 4/5: Mean predicted reward = 8.011
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9750, entropy=1.0142, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0793
  Round 5/5: Mean predicted reward = 8.212

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 7 Results ---
  Mean Oracle Reward: 8.410
  Min Oracle Reward: 5.958
  Max Oracle Reward: 9.746
  Std Oracle Reward: 0.923
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: 0.806, Max: 0.854, Count: 3
New best mean reward!
  Total Sequences Evaluated: 274

======================================================================
EXPERIMENT ROUND 8/15
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.080
Total data collected: 274
  Consistent improvement, increasing LR to 0.000132

--- Round 8 Configuration ---
Learning rate: 0.000132
Entropy coefficient: 0.0050
Exploration rate: 0.080

--- Generated Sequences (Diversity: 1.000) ---
  GTCCGTAA
  AACCTGGT
  CGATTACG
  TCGCGGAA
  CAAGTGCT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.297
  Max reward: 11.688
  With intrinsic bonuses: 8.311

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9754, entropy=0.9940, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1233

=== Surrogate Model Training ===
Total samples: 306

Training on 287 samples (removed 19 outliers)
Reward range: [5.35, 10.20], mean: 8.01
  rf_tuned: R² = 0.755 (std: 0.038)
  gb_tuned: R² = 0.847 (std: 0.051)
  ensemble: R² = 0.783 (std: 0.048)

Model-based training with 3 models
Best R²: 0.847, Mean R²: 0.795
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9760, entropy=1.0115, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0886
  Round 1/5: Mean predicted reward = 7.917
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9708, entropy=0.9750, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1537
  Round 2/5: Mean predicted reward = 7.863
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9746, entropy=0.9959, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1602
  Round 3/5: Mean predicted reward = 7.851
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9737, entropy=0.9686, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1631
  Round 4/5: Mean predicted reward = 8.119
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9745, entropy=0.9461, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1467
  Round 5/5: Mean predicted reward = 8.190

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 8 Results ---
  Mean Oracle Reward: 8.321
  Min Oracle Reward: 2.669
  Max Oracle Reward: 11.981
  Std Oracle Reward: 1.457
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: 0.795, Max: 0.847, Count: 3
  Total Sequences Evaluated: 306

======================================================================
EXPERIMENT ROUND 9/15
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.065
Total data collected: 306

--- Round 9 Configuration ---
Learning rate: 0.000038
Entropy coefficient: 0.0050
Exploration rate: 0.065

--- Generated Sequences (Diversity: 1.000) ---
  TGAACTCG
  AGCCATGT
  TGGATCAC
  GTACGCGA
  TGCCTAGA
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.412
  Max reward: 9.576
  With intrinsic bonuses: 8.453

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9766, entropy=0.9569, kl_div=0.0000
    Epoch 1: policy_loss=-0.0222, value_loss=0.9766, entropy=0.9537, kl_div=0.0498

=== Surrogate Model Training ===
Total samples: 338

Training on 319 samples (removed 19 outliers)
Reward range: [5.35, 10.20], mean: 8.05
  rf_tuned: R² = 0.765 (std: 0.057)
  gb_tuned: R² = 0.856 (std: 0.062)
  ensemble: R² = 0.789 (std: 0.042)

Model-based training with 3 models
Best R²: 0.856, Mean R²: 0.803
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9780, entropy=0.9513, kl_div=0.0000
    Epoch 1: policy_loss=-0.0036, value_loss=0.9780, entropy=0.9479, kl_div=0.0480
  Round 1/5: Mean predicted reward = 7.696
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9796, entropy=0.9290, kl_div=0.0000
    Epoch 1: policy_loss=0.0077, value_loss=0.9796, entropy=0.9268, kl_div=0.0276
  Round 2/5: Mean predicted reward = 7.820
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9744, entropy=0.9336, kl_div=0.0000
    Epoch 1: policy_loss=-0.0147, value_loss=0.9744, entropy=0.9322, kl_div=0.0189
  Round 3/5: Mean predicted reward = 7.858
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9759, entropy=0.9313, kl_div=0.0000
    Epoch 1: policy_loss=-0.0129, value_loss=0.9759, entropy=0.9294, kl_div=0.0257
  Round 4/5: Mean predicted reward = 8.041
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9734, entropy=0.9155, kl_div=0.0000
    Epoch 1: policy_loss=-0.0286, value_loss=0.9734, entropy=0.9130, kl_div=0.0440
  Round 5/5: Mean predicted reward = 7.965

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.

--- Round 9 Results ---
  Mean Oracle Reward: 8.484
  Min Oracle Reward: 5.821
  Max Oracle Reward: 9.823
  Std Oracle Reward: 0.970
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: 0.803, Max: 0.856, Count: 3
New best mean reward!
  Total Sequences Evaluated: 338

======================================================================
EXPERIMENT ROUND 10/15
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 338
  Performance plateaued, reducing LR to 0.000150

--- Round 10 Configuration ---
Learning rate: 0.000150
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 0.969) ---
  GCGACATG
  GTACGGAC
  CATAGCTG
  TAATCGGC
  ATGCGACT
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.459
  Max reward: 9.705
  With intrinsic bonuses: 8.400

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9789, entropy=0.9423, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1647

=== Surrogate Model Training ===
Total samples: 370

Training on 350 samples (removed 20 outliers)
Reward range: [5.35, 10.20], mean: 8.10
  rf_tuned: R² = 0.761 (std: 0.034)
  gb_tuned: R² = 0.868 (std: 0.034)
  ensemble: R² = 0.778 (std: 0.033)

Model-based training with 3 models
Best R²: 0.868, Mean R²: 0.802
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9785, entropy=0.8696, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2170
  Round 1/5: Mean predicted reward = 7.633
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9759, entropy=0.8993, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2339
  Round 2/5: Mean predicted reward = 7.584
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9764, entropy=0.8924, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1731
  Round 3/5: Mean predicted reward = 7.828
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9729, entropy=0.8668, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2283
  Round 4/5: Mean predicted reward = 7.896
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9762, entropy=0.8515, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2927
  Round 5/5: Mean predicted reward = 8.082

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 10 Results ---
  Mean Oracle Reward: 8.481
  Min Oracle Reward: 4.997
  Max Oracle Reward: 9.739
  Std Oracle Reward: 0.990
  Sequence Diversity: 0.969
  Models Used: 3
  Model R² - Mean: 0.802, Max: 0.868, Count: 3
  Total Sequences Evaluated: 370

======================================================================
EXPERIMENT ROUND 11/15
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
  GCATACGT
  CGATGTAC
  GCTCATAG
  GTCGACTA
  ATCAGGCG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.270
  Max reward: 9.953
  With intrinsic bonuses: 8.292

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9766, entropy=0.8658, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2343

=== Surrogate Model Training ===
Total samples: 402

Training on 377 samples (removed 25 outliers)
Reward range: [5.44, 10.20], mean: 8.15
  rf_tuned: R² = 0.743 (std: 0.044)
  gb_tuned: R² = 0.855 (std: 0.033)
  ensemble: R² = 0.758 (std: 0.026)

Model-based training with 3 models
Best R²: 0.855, Mean R²: 0.785
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9763, entropy=0.8182, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2203
  Round 1/5: Mean predicted reward = 7.444
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9756, entropy=0.8402, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1489
  Round 2/5: Mean predicted reward = 7.587
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9775, entropy=0.8086, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0731
  Round 3/5: Mean predicted reward = 7.734
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9798, entropy=0.8185, kl_div=0.0000
    Epoch 1: policy_loss=-0.0149, value_loss=0.9798, entropy=0.8171, kl_div=0.0232
  Round 4/5: Mean predicted reward = 8.005
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9744, entropy=0.8254, kl_div=0.0000
    Epoch 1: policy_loss=-0.0658, value_loss=0.9744, entropy=0.8274, kl_div=-0.0264
  Round 5/5: Mean predicted reward = 8.145

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 11 Results ---
  Mean Oracle Reward: 8.199
  Min Oracle Reward: 5.120
  Max Oracle Reward: 9.920
  Std Oracle Reward: 0.924
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: 0.785, Max: 0.855, Count: 3
  Total Sequences Evaluated: 402

======================================================================
EXPERIMENT ROUND 12/15
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
  ATACGGTC
  ACTTGGAC
  CATAGCTG
  ATTCGAGC
  GATTCACG
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.139
  Max reward: 9.496
  With intrinsic bonuses: 8.159

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=0.0000, value_loss=0.9733, entropy=0.7916, kl_div=0.0000
    Epoch 1: policy_loss=-0.0200, value_loss=0.9733, entropy=0.7898, kl_div=0.0354

=== Surrogate Model Training ===
Total samples: 434

Training on 407 samples (removed 27 outliers)
Reward range: [5.62, 10.20], mean: 8.17
  rf_tuned: R² = 0.732 (std: 0.053)
  gb_tuned: R² = 0.860 (std: 0.038)
  ensemble: R² = 0.752 (std: 0.032)

Model-based training with 3 models
Best R²: 0.860, Mean R²: 0.781
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9752, entropy=0.8068, kl_div=0.0000
    Epoch 1: policy_loss=0.0044, value_loss=0.9752, entropy=0.8062, kl_div=0.0183
  Round 1/5: Mean predicted reward = 7.392
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9724, entropy=0.7982, kl_div=0.0000
    Epoch 1: policy_loss=-0.0387, value_loss=0.9724, entropy=0.7981, kl_div=0.0079
  Round 2/5: Mean predicted reward = 7.406
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9755, entropy=0.8164, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0799
  Round 3/5: Mean predicted reward = 7.680
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9734, entropy=0.7719, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1627
  Round 4/5: Mean predicted reward = 7.781
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9731, entropy=0.7836, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1769
  Round 5/5: Mean predicted reward = 8.095

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 12 Results ---
  Mean Oracle Reward: 8.198
  Min Oracle Reward: 4.046
  Max Oracle Reward: 9.495
  Std Oracle Reward: 1.116
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: 0.781, Max: 0.860, Count: 3
  Total Sequences Evaluated: 434

======================================================================
EXPERIMENT ROUND 13/15
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 434

--- Round 13 Configuration ---
Learning rate: 0.000110
Entropy coefficient: 0.0050
Exploration rate: 0.050

--- Generated Sequences (Diversity: 1.000) ---
  CCTTGGAA
  CAGAGTAT
  CGATATCG
  TCACTGAG
  TAGTAGCC
  ... (32 total)

Oracle Evaluation:
  Mean reward: 8.232
  Max reward: 10.240
  With intrinsic bonuses: 8.280

Policy Update:
  Adaptive update: clip_ratio=0.20, entropy_coef=0.005
    Epoch 0: policy_loss=-0.0000, value_loss=0.9761, entropy=0.7552, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.2523

=== Surrogate Model Training ===
Total samples: 466

Training on 439 samples (removed 27 outliers)
Reward range: [5.62, 10.49], mean: 8.17
  rf_tuned: R² = 0.760 (std: 0.028)
  gb_tuned: R² = 0.880 (std: 0.034)
  ensemble: R² = 0.783 (std: 0.031)

Model-based training with 3 models
Best R²: 0.880, Mean R²: 0.808
Running 5 virtual training rounds
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9772, entropy=0.7916, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.1045
  Round 1/5: Mean predicted reward = 7.326
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9760, entropy=0.7531, kl_div=0.0000
    Early stopping at epoch 1: KL divergence = 0.0550
  Round 2/5: Mean predicted reward = 7.313
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9760, entropy=0.7612, kl_div=0.0000
    Epoch 1: policy_loss=-0.0384, value_loss=0.9760, entropy=0.7630, kl_div=-0.0328
  Round 3/5: Mean predicted reward = 7.750
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=0.0000, value_loss=0.9750, entropy=0.7519, kl_div=0.0000
    Epoch 1: policy_loss=-0.0383, value_loss=0.9750, entropy=0.7579, kl_div=-0.0912
  Round 4/5: Mean predicted reward = 7.976
  Adaptive update: clip_ratio=0.20, entropy_coef=0.003
    Epoch 0: policy_loss=-0.0000, value_loss=0.9740, entropy=0.8112, kl_div=0.0000
    Epoch 1: policy_loss=-0.0323, value_loss=0.9740, entropy=0.8128, kl_div=0.0098
  Round 5/5: Mean predicted reward = 7.990

  === Progress Analysis ===
  Status: EXCELLENT
  • Models learning well. Can increase model-based training.
  • Reward trend declining. Consider resetting exploration parameters.

--- Round 13 Results ---
  Mean Oracle Reward: 8.230
  Min Oracle Reward: 5.750
  Max Oracle Reward: 10.054
  Std Oracle Reward: 1.140
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: 0.808, Max: 0.880, Count: 3
  Total Sequences Evaluated: 466

⚡ Early stopping: Converged at round 13

======================================================================
DyNA PPO ALGORITHM COMPLETE!
======================================================================
Total rounds executed: 13
Total sequences evaluated: 466
Best mean reward: 8.484 (achieved at round 9)

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 13
Final Mean Reward: 8.2300
Best Mean Reward: 8.4840
Best Max Reward: 11.9813
Initial Lr: 0.0003
Final Lr: 0.0001
Total Updates: 128
Final Diversity: 1.0000
Convergence Round: 10
==================================================

Generating learning curves...
Learning curves saved to learning_curves.png
Saving training metrics...
Metrics saved to training_metrics.json

======================================================================
FINAL OPTIMIZED SEQUENCES
======================================================================

Deterministic (Exploitation):
  GCGCATGC: 8.854
  GCGCATGC: 8.651
  GCGCATGC: 8.941
  GCGCATGC: 8.931
  GCGCATGC: 8.816

Stochastic (Exploration):
  GGCTGCAT: 9.560
  GGCCTGCT: 9.669
  GCTGCAGT: 9.235
  GCGCATAG: 9.078
  GGCATCGC: 9.291

Final Performance:
  Mean reward: 9.103
  Max reward: 9.669
  Std reward: 0.314

Best sequence found: GGCCTGCT
   Reward: 9.669

======================================================================
Training complete! Check 'learning_curves.png' and 'training_metrics.json'
======================================================================