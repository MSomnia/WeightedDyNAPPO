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
  Batch size B = 48
  Warm-up phase: True
======================================================================

=== WARM-UP PHASE ===
Generating 50 warm-up samples...
Warm-up statistics:
  Mean reward: 7.720
  Std reward: 3.049
  Min/Max: 0.000 / 11.491

Pre-training surrogate models on warm-up data...

Round 0: Evaluating 7 models
Data size: 50, Feature dim: 73
Threshold: R² > -0.500, Min models: 1
  knn: R² = 0.026
  knn: R² = 0.131
  knn: R² = 0.181
  rf: R² = 0.684
  rf: R² = 0.708
  gb: R² = 0.635
  ridge: R² = 0.227

Selected 7 models for ensemble
Models: ['knn', 'knn', 'knn', 'rf', 'rf', 'gb', 'ridge']
Scores: ['0.026', '0.131', '0.181', '0.684', '0.708', '0.635', '0.227']
Initial models trained: 7
Initial R² scores - Mean: 0.370, Max: 0.708

======================================================================
EXPERIMENT ROUND 1/15
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.300
Total data collected: 50

--- Round 1 Generated Sequences ---
Temperature: 1.50, Diversity: 1.000
CCCGGCCCATGC TTGTACGCCGAC TGAATAAGACAA CACAGGGCTGCT TACCACCGGCAA TTGTGTTGGTGC AGTAAGAAGGTG GCTAAGCATAAC TGGAAGCTCCCA CCGATGTCTATA ... (48 total)

=== Surrogate Model Training (Round 1) ===
Total training samples: 98

Round 1: Evaluating 7 models
Data size: 98, Feature dim: 58
Threshold: R² > -0.500, Min models: 1
  knn: R² = -1.111
  knn: R² = -0.911
  knn: R² = -0.952
  rf: R² = -0.108
  rf: R² = -0.095
  gb: R² = -0.258
  ridge: R² = -0.743

Selected 3 models for ensemble
Models: ['rf', 'rf', 'gb']
Scores: ['-0.108', '-0.095', '-0.258']

Model-based training: 2 rounds with 3 models
Best model R²: -0.095
  Virtual round 1/2: Mean predicted reward = 0.000

--- Round 1 Results ---
  Mean Oracle Reward: 9.464
  Min Oracle Reward: 4.554
  Max Oracle Reward: 12.289
  Std Oracle Reward: 1.589
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: -0.597, Max: -0.095, Count: 7
   New best mean reward!
  Total Sequences Evaluated: 98

======================================================================
EXPERIMENT ROUND 2/15
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.300
Total data collected: 98

--- Round 2 Generated Sequences ---
Temperature: 1.50, Diversity: 1.000
TGGGCCCGAATC CGCTTCGCAACT GTGTTCCACTAT ACCCCCTGCGCG GACACCGGTTAG AGGTGCTGGTCA GGCCATGATGTA TCGTTCCGGCGG GACCGTCTGGAT TTGGTGTCATTG ... (48 total)

=== Surrogate Model Training (Round 2) ===
Total training samples: 146

Round 2: Evaluating 7 models
Data size: 146, Feature dim: 58
Threshold: R² > -0.500, Min models: 1
  knn: R² = -0.609
  knn: R² = -0.724
  knn: R² = -0.795
  rf: R² = -0.281
  rf: R² = -0.244
  gb: R² = -0.326
  ridge: R² = -0.288

Selected 4 models for ensemble
Models: ['rf', 'rf', 'gb', 'ridge']
Scores: ['-0.281', '-0.244', '-0.326', '-0.288']

Model-based training: 2 rounds with 4 models
Best model R²: -0.244
  Virtual round 1/2: Mean predicted reward = 0.000

--- Round 2 Results ---
  Mean Oracle Reward: 9.932
  Min Oracle Reward: 4.172
  Max Oracle Reward: 12.181
  Std Oracle Reward: 1.513
  Sequence Diversity: 1.000
  Models Used: 4
  Model R² - Mean: -0.467, Max: -0.244, Count: 7
   New best mean reward!
  Total Sequences Evaluated: 146

======================================================================
EXPERIMENT ROUND 3/15
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.300
Total data collected: 146

--- Round 3 Generated Sequences ---
Temperature: 1.50, Diversity: 1.000
TGCCCGCTCACC TCTCTTGCCATA ATTTAATATCCG GGGGGCCCGACT TGTCCGGCCCAG TGTTCACTGGTG TGTTGCGGCCAA AGGCGAGTGCCA GTATGCGACAGC CAGGGGATCCCG ... (48 total)

=== Surrogate Model Training (Round 3) ===
Total training samples: 194

Round 3: Evaluating 8 models
Data size: 194, Feature dim: 58
Threshold: R² > 0.000, Min models: 2
  knn: R² = -0.555
  knn: R² = -0.525
  knn: R² = -0.542
  rf: R² = -0.018
  rf: R² = -0.033
  gb: R² = -0.071
  ridge: R² = 0.052
  svr: R² = -0.053

Only 1 models met threshold. Using fallback...
  Fallback added: rf (R² = -0.018)

Selected 2 models for ensemble
Models: ['ridge', 'rf']
Scores: ['0.052', '-0.018']

Model-based training: 2 rounds with 2 models
Best model R²: 0.052
  Virtual round 1/2: Mean predicted reward = 0.000

--- Round 3 Results ---
  Mean Oracle Reward: 10.043
  Min Oracle Reward: 6.557
  Max Oracle Reward: 12.019
  Std Oracle Reward: 1.194
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -0.218, Max: 0.052, Count: 8
   New best mean reward!
  Total Sequences Evaluated: 194

======================================================================
EXPERIMENT ROUND 4/15
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.280
Total data collected: 194

--- Round 4 Generated Sequences ---
Temperature: 1.20, Diversity: 1.000
CCCTCGCTATCT CATTTGCTGGCG TCAGTGGGAGAA CCAGTACGCCAG TCTCACGACGGA TGGGACGCCGTT CTGCCCGAACGT TGTGCCAGTTTA GCAAGCCGGGCC CTGCGCGACATA ... (48 total)

=== Surrogate Model Training (Round 4) ===
Total training samples: 242

Round 4: Evaluating 10 models
Data size: 242, Feature dim: 58
Threshold: R² > 0.000, Min models: 2
  knn: R² = -0.891
  knn: R² = -0.773
  knn: R² = -0.753
  rf: R² = -0.097
  rf: R² = -0.181
  gb: R² = -0.462
  xgb: R² = -0.152
  mlp: R² = -0.968
  ridge: R² = -0.292
  svr: R² = -0.248

Only 0 models met threshold. Using fallback...
  Fallback added: rf (R² = -0.097)
  Fallback added: xgb (R² = -0.152)

Selected 2 models for ensemble
Models: ['rf', 'xgb']
Scores: ['-0.097', '-0.152']

Model-based training: 2 rounds with 2 models
Best model R²: -0.097
  Virtual round 1/2: Mean predicted reward = 0.000

--- Round 4 Results ---
  Mean Oracle Reward: 10.303
  Min Oracle Reward: 8.364
  Max Oracle Reward: 11.989
  Std Oracle Reward: 0.893
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -0.482, Max: -0.097, Count: 10
   New best mean reward!
  Total Sequences Evaluated: 242

======================================================================
EXPERIMENT ROUND 5/15
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.250
Total data collected: 242

--- Round 5 Generated Sequences ---
Temperature: 1.20, Diversity: 1.000
TGCTACGTACTT GACCGTTTGTGA GTCGTTCCCGCT GTGTACAGAACC CGTGAATGGGCC ACGCGTGGATTA GTCGGTCGAGTT TTCAGCCCCAAT GGCGGTGCACGT ATCGGCCGTGCG ... (48 total)

=== Surrogate Model Training (Round 5) ===
Total training samples: 290

Round 5: Evaluating 10 models
Data size: 290, Feature dim: 58
Threshold: R² > 0.000, Min models: 2
  knn: R² = -0.666
  knn: R² = -0.514
  knn: R² = -0.543
  rf: R² = -0.049
  rf: R² = -0.036
  gb: R² = -0.224
  xgb: R² = -0.080
  mlp: R² = -1.115
  ridge: R² = -0.146
  svr: R² = -0.132

Only 0 models met threshold. Using fallback...
  Fallback added: rf (R² = -0.036)
  Fallback added: rf (R² = -0.049)

Selected 2 models for ensemble
Models: ['rf', 'rf']
Scores: ['-0.036', '-0.049']

Model-based training: 2 rounds with 2 models
Best model R²: -0.036
  Virtual round 1/2: Mean predicted reward = 0.000

--- Round 5 Results ---
  Mean Oracle Reward: 10.252
  Min Oracle Reward: 8.372
  Max Oracle Reward: 12.565
  Std Oracle Reward: 0.937
  Sequence Diversity: 1.000
  Models Used: 2
  Model R² - Mean: -0.350, Max: -0.036, Count: 10
  Total Sequences Evaluated: 290

======================================================================
EXPERIMENT ROUND 6/15
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.220
Total data collected: 290

--- Round 6 Generated Sequences ---
Temperature: 1.20, Diversity: 1.000
CGAGAGCGATGC CGCGCGGATGAT GGAGAGGGGAGC CCCAACATGCCG GGCGTTCCGTAA CAGCTACCTGAG GAGGCGTGGTTT GTGTATGGTGGC TGAATTCCATAC GGGGCTTCAGCG ... (48 total)

=== Surrogate Model Training (Round 6) ===
Total training samples: 338

Round 6: Evaluating 10 models
Data size: 338, Feature dim: 58
Threshold: R² > 0.120, Min models: 3
  knn: R² = -0.767
  knn: R² = -0.641
  knn: R² = -0.602
  rf: R² = -0.354
  rf: R² = -0.403
  gb: R² = -0.647
  xgb: R² = -0.532
  mlp: R² = -0.932
  ridge: R² = -0.416
  svr: R² = -0.464

Only 0 models met threshold. Using fallback...
  Fallback added: rf (R² = -0.354)
  Fallback added: rf (R² = -0.403)
  Fallback added: ridge (R² = -0.416)

Selected 3 models for ensemble
Models: ['rf', 'rf', 'ridge']
Scores: ['-0.354', '-0.403', '-0.416']

Model-based training: 2 rounds with 3 models
Best model R²: -0.354
  Virtual round 1/2: Mean predicted reward = 0.000

--- Round 6 Results ---
  Mean Oracle Reward: 9.695
  Min Oracle Reward: 6.955
  Max Oracle Reward: 12.559
  Std Oracle Reward: 1.186
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: -0.576, Max: -0.354, Count: 10
  Total Sequences Evaluated: 338

======================================================================
EXPERIMENT ROUND 7/15
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.190
Total data collected: 338

--- Round 7 Generated Sequences ---
Temperature: 1.20, Diversity: 1.000
GCGCCTAGGCGC TGGGCATGCAAT CGTGCGATGTAA CGTGCGACTGAA CACGGCTCGGTC GCGCGATAGAGC CACGTGGCCAGT ATGCAAGCCTGC CGGGATACCCAC GAGCCATCCTGA ... (48 total)

=== Surrogate Model Training (Round 7) ===
Total training samples: 386

Round 7: Evaluating 10 models
Data size: 386, Feature dim: 58
Threshold: R² > 0.140, Min models: 3
  knn: R² = -0.676
  knn: R² = -0.714
  knn: R² = -0.690
  rf: R² = -0.490
  rf: R² = -0.531
  gb: R² = -0.592
  xgb: R² = -0.649
  mlp: R² = -1.359
  ridge: R² = -0.651
  svr: R² = -0.597

Only 0 models met threshold. Using fallback...
  Fallback added: rf (R² = -0.490)
  Fallback added: rf (R² = -0.531)
  Fallback added: gb (R² = -0.592)

Selected 3 models for ensemble
Models: ['rf', 'rf', 'gb']
Scores: ['-0.490', '-0.531', '-0.592']

Model-based training: 2 rounds with 3 models
Best model R²: -0.490
  Virtual round 1/2: Mean predicted reward = 0.000

--- Round 7 Results ---
  Mean Oracle Reward: 10.422
  Min Oracle Reward: 6.641
  Max Oracle Reward: 12.153
  Std Oracle Reward: 1.028
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: -0.695, Max: -0.490, Count: 10
   New best mean reward!
  Total Sequences Evaluated: 386

======================================================================
EXPERIMENT ROUND 8/15
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.080
Total data collected: 386

--- Round 8 Generated Sequences ---
Temperature: 1.00, Diversity: 1.000
GGTGGCCGCGCG TCGATAGAGGCC TTAGGGCGTAGG GACGAAGGCGCG CAGCTACTACGG AACCTTGCAGGT CCCGAACTAGTA AGCTGCCGAGCG GTACACCGACCA TAGCCCTCCTAG ... (48 total)

=== Surrogate Model Training (Round 8) ===
Total training samples: 434

Round 8: Evaluating 10 models
Data size: 434, Feature dim: 58
Threshold: R² > 0.160, Min models: 3
  knn: R² = -0.608
  knn: R² = -0.649
  knn: R² = -0.672
  rf: R² = -0.549
  rf: R² = -0.557
  gb: R² = -0.699
  xgb: R² = -0.588
  mlp: R² = -1.061
  ridge: R² = -0.622
  svr: R² = -0.583

Only 0 models met threshold. Using fallback...
  Fallback added: rf (R² = -0.549)
  Fallback added: rf (R² = -0.557)
  Fallback added: svr (R² = -0.583)

Selected 3 models for ensemble
Models: ['rf', 'rf', 'svr']
Scores: ['-0.549', '-0.557', '-0.583']

Model-based training: 2 rounds with 3 models
Best model R²: -0.549
  Virtual round 1/2: Mean predicted reward = 0.000

--- Round 8 Results ---
  Mean Oracle Reward: 10.404
  Min Oracle Reward: 7.467
  Max Oracle Reward: 14.761
  Std Oracle Reward: 1.186
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: -0.659, Max: -0.549, Count: 10
  Total Sequences Evaluated: 434

======================================================================
EXPERIMENT ROUND 9/15
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.065
Total data collected: 434

--- Round 9 Generated Sequences ---
Temperature: 1.00, Diversity: 1.000
GGCCCCGTTCGC GGCCCAGACAGC AGCAGGCCGGTC GCGCCTGTGTCG CTATCCAATCGT GCAGTTACGTGG TGTGCGCCAAGC GCAACCCAAGGT TCTGGCTGACGG CGGTCTTTCAGC ... (48 total)

=== Surrogate Model Training (Round 9) ===
Total training samples: 482

Round 9: Evaluating 10 models
Data size: 482, Feature dim: 58
Threshold: R² > 0.180, Min models: 3
  knn: R² = -1.133
  knn: R² = -1.035
  knn: R² = -1.021
  rf: R² = -0.919
  rf: R² = -0.902
  gb: R² = -1.012
  xgb: R² = -0.998
  mlp: R² = -1.527
  ridge: R² = -0.940
  svr: R² = -0.961

Only 0 models met threshold. Using fallback...
  Fallback added: rf (R² = -0.902)
  Fallback added: rf (R² = -0.919)
  Fallback added: ridge (R² = -0.940)

Selected 3 models for ensemble
Models: ['rf', 'rf', 'ridge']
Scores: ['-0.902', '-0.919', '-0.940']

Model-based training: 2 rounds with 3 models
Best model R²: -0.902
  Virtual round 1/2: Mean predicted reward = 0.000

--- Round 9 Results ---
  Mean Oracle Reward: 10.321
  Min Oracle Reward: 6.826
  Max Oracle Reward: 13.765
  Std Oracle Reward: 1.170
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: -1.045, Max: -0.902, Count: 10
  Total Sequences Evaluated: 482

======================================================================
EXPERIMENT ROUND 10/15
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 482

--- Round 10 Generated Sequences ---
Temperature: 1.00, Diversity: 1.000
GCTACCCGACTC GCGAGAGATCTG TGGGATACTTCA GGCTATCGTACA CTAAGTCGCCAT AGGCTATGGCTG CGGCCTGGCGAC GTCCGGCGCCTG CGTACCACAGGT GTGGCGCTAGCG ... (48 total)

=== Surrogate Model Training (Round 10) ===
Total training samples: 530

Round 10: Evaluating 10 models
Data size: 530, Feature dim: 58
Threshold: R² > 0.200, Min models: 3
  knn: R² = -0.471
  knn: R² = -0.437
  knn: R² = -0.438
  rf: R² = -0.354
  rf: R² = -0.334
  gb: R² = -0.382
  xgb: R² = -0.430
  mlp: R² = -0.965
  ridge: R² = -0.316
  svr: R² = -0.364

Only 0 models met threshold. Using fallback...
  Fallback added: ridge (R² = -0.316)
  Fallback added: rf (R² = -0.334)
  Fallback added: rf (R² = -0.354)

Selected 3 models for ensemble
Models: ['ridge', 'rf', 'rf']
Scores: ['-0.316', '-0.334', '-0.354']

Model-based training: 2 rounds with 3 models
Best model R²: -0.316
  Virtual round 1/2: Mean predicted reward = 0.000

--- Round 10 Results ---
  Mean Oracle Reward: 10.475
  Min Oracle Reward: 7.167
  Max Oracle Reward: 13.363
  Std Oracle Reward: 0.971
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: -0.449, Max: -0.316, Count: 10
   New best mean reward!
  Total Sequences Evaluated: 530

======================================================================
EXPERIMENT ROUND 11/15
======================================================================
Learning Rate: 0.000272
Exploration Rate: 0.050
Total data collected: 530

--- Round 11 Generated Sequences ---
Temperature: 1.00, Diversity: 1.000
GCGACTGTACAG CCGACCAGATGC AAGTGATAGAAA ATCCCGCGCCTT TCCATGTTGATA TGGCCAGCGAGA TAGCGGGCCGAG GTACCTATATGC AGGACGACGTAA GCGCCCTAGCAT ... (48 total)

=== Surrogate Model Training (Round 11) ===
Total training samples: 578

Round 11: Evaluating 10 models
Data size: 578, Feature dim: 58
Threshold: R² > 0.220, Min models: 3
  knn: R² = -0.355
  knn: R² = -0.345
  knn: R² = -0.344
  rf: R² = -0.249
  rf: R² = -0.245
  gb: R² = -0.327
  xgb: R² = -0.346
  mlp: R² = -0.841
  ridge: R² = -0.292
  svr: R² = -0.246

Only 0 models met threshold. Using fallback...
  Fallback added: rf (R² = -0.245)
  Fallback added: svr (R² = -0.246)
  Fallback added: rf (R² = -0.249)

Selected 3 models for ensemble
Models: ['rf', 'svr', 'rf']
Scores: ['-0.245', '-0.246', '-0.249']

Model-based training: 2 rounds with 3 models
Best model R²: -0.245
  Virtual round 1/2: Mean predicted reward = 0.000

--- Round 11 Results ---
  Mean Oracle Reward: 10.576
  Min Oracle Reward: 6.533
  Max Oracle Reward: 12.786
  Std Oracle Reward: 1.228
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: -0.359, Max: -0.245, Count: 10
   New best mean reward!
  Total Sequences Evaluated: 578

======================================================================
EXPERIMENT ROUND 12/15
======================================================================
Learning Rate: 0.000200
Exploration Rate: 0.050
Total data collected: 578

--- Round 12 Generated Sequences ---
Temperature: 1.00, Diversity: 1.000
GGCTGCCTTCCC AACCGTACGGCC CCGGCAGCCACG AATATGACTCAG GGCCAGCGTATC GCGCCAGGACAT GCTGCTGCGCTA GTCCATTAGACA GCGCTGGCCTGC GGGCCAGATACT ... (48 total)

=== Surrogate Model Training (Round 12) ===
Total training samples: 626

Round 12: Evaluating 10 models
Data size: 626, Feature dim: 58
Threshold: R² > 0.240, Min models: 3
  knn: R² = -0.557
  knn: R² = -0.470
  knn: R² = -0.436
  rf: R² = -0.403
  rf: R² = -0.377
  gb: R² = -0.408
  xgb: R² = -0.410
  mlp: R² = -0.920
  ridge: R² = -0.425
  svr: R² = -0.417

Only 0 models met threshold. Using fallback...
  Fallback added: rf (R² = -0.377)
  Fallback added: rf (R² = -0.403)
  Fallback added: gb (R² = -0.408)

Selected 3 models for ensemble
Models: ['rf', 'rf', 'gb']
Scores: ['-0.377', '-0.403', '-0.408']

Model-based training: 2 rounds with 3 models
Best model R²: -0.377
  Virtual round 1/2: Mean predicted reward = 0.000

--- Round 12 Results ---
  Mean Oracle Reward: 10.731
  Min Oracle Reward: 7.227
  Max Oracle Reward: 12.588
  Std Oracle Reward: 1.023
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: -0.482, Max: -0.377, Count: 10
   New best mean reward!
  Total Sequences Evaluated: 626

======================================================================
EXPERIMENT ROUND 13/15
======================================================================
Learning Rate: 0.000110
Exploration Rate: 0.050
Total data collected: 626

--- Round 13 Generated Sequences ---
Temperature: 1.00, Diversity: 1.000
TGCCATAGACCG GCCGCAGCTTTC GGCCGCTAGTAC GGTCCGCATAAG GCGCGACAAGGC GCGTGCCTATAA GCTCGGCTGACT GGAGCCGAATTG CGGCCGTCAGAA GTCGCCTAGACC ... (48 total)

=== Surrogate Model Training (Round 13) ===
Total training samples: 674

Round 13: Evaluating 10 models
Data size: 674, Feature dim: 58
Threshold: R² > 0.260, Min models: 3
  knn: R² = -0.467
  knn: R² = -0.413
  knn: R² = -0.393
  rf: R² = -0.371
  rf: R² = -0.355
  gb: R² = -0.365
  xgb: R² = -0.349
  mlp: R² = -0.868
  ridge: R² = -0.406
  svr: R² = -0.356

Only 0 models met threshold. Using fallback...
  Fallback added: xgb (R² = -0.349)
  Fallback added: rf (R² = -0.355)
  Fallback added: svr (R² = -0.356)

Selected 3 models for ensemble
Models: ['xgb', 'rf', 'svr']
Scores: ['-0.349', '-0.355', '-0.356']

Model-based training: 2 rounds with 3 models
Best model R²: -0.349
  Virtual round 1/2: Mean predicted reward = 0.000

--- Round 13 Results ---
  Mean Oracle Reward: 11.054
  Min Oracle Reward: 7.909
  Max Oracle Reward: 13.645
  Std Oracle Reward: 1.148
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: -0.434, Max: -0.349, Count: 10
   New best mean reward!
  Total Sequences Evaluated: 674

======================================================================
EXPERIMENT ROUND 14/15
======================================================================
Learning Rate: 0.000038
Exploration Rate: 0.050
Total data collected: 674

--- Round 14 Generated Sequences ---
Temperature: 1.00, Diversity: 1.000
GCTTGCCCATAT GGCTGCATAAGA AGCCCGTAACTC GGCCGTACCAGG GCTCGTCAATAG GCGTCTCCTTAA AGACGAGACAGC GGCAGGCCAATA GCCGGCCGAGCC GCGATCGATTAG ... (48 total)

=== Surrogate Model Training (Round 14) ===
Total training samples: 722

Round 14: Evaluating 10 models
Data size: 722, Feature dim: 58
Threshold: R² > 0.280, Min models: 3
  knn: R² = -0.638
  knn: R² = -0.539
  knn: R² = -0.554
  rf: R² = -0.569
  rf: R² = -0.552
  gb: R² = -0.577
  xgb: R² = -0.512
  mlp: R² = -1.191
  ridge: R² = -0.587
  svr: R² = -0.549

Only 0 models met threshold. Using fallback...
  Fallback added: xgb (R² = -0.512)
  Fallback added: knn (R² = -0.539)
  Fallback added: svr (R² = -0.549)

Selected 3 models for ensemble
Models: ['xgb', 'knn', 'svr']
Scores: ['-0.512', '-0.539', '-0.549']

Model-based training: 2 rounds with 3 models
Best model R²: -0.512
  Virtual round 1/2: Mean predicted reward = 0.000

--- Round 14 Results ---
  Mean Oracle Reward: 11.101
  Min Oracle Reward: 9.289
  Max Oracle Reward: 13.275
  Std Oracle Reward: 0.981
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: -0.627, Max: -0.512, Count: 10
   New best mean reward!
  Total Sequences Evaluated: 722

======================================================================
EXPERIMENT ROUND 15/15
======================================================================
Learning Rate: 0.000300
Exploration Rate: 0.050
Total data collected: 722

--- Round 15 Generated Sequences ---
Temperature: 1.00, Diversity: 1.000
CCGATCGAAACG GGGCCGTGCTTA GGGCGGCACTAT GCGCGTGCGTAC GGCCACGGACAG GCCGAGCAAGTC AGCGCGCGCAGA GCGTCCAATCCG GCGCCGCGTCTA GCAACGGCAAGT ... (48 total)

=== Surrogate Model Training (Round 15) ===
Total training samples: 770

Round 15: Evaluating 10 models
Data size: 770, Feature dim: 58
Threshold: R² > 0.300, Min models: 3
  knn: R² = -0.258
  knn: R² = -0.208
  knn: R² = -0.230
  rf: R² = -0.128
  rf: R² = -0.119
  gb: R² = -0.155
  xgb: R² = -0.165
  mlp: R² = -0.786
  ridge: R² = -0.197
  svr: R² = -0.148

Only 0 models met threshold. Using fallback...
  Fallback added: rf (R² = -0.119)
  Fallback added: rf (R² = -0.128)
  Fallback added: svr (R² = -0.148)

Selected 3 models for ensemble
Models: ['rf', 'rf', 'svr']
Scores: ['-0.119', '-0.128', '-0.148']

Model-based training: 2 rounds with 3 models
Best model R²: -0.119
  Virtual round 1/2: Mean predicted reward = 0.000

--- Round 15 Results ---
  Mean Oracle Reward: 10.797
  Min Oracle Reward: 5.314
  Max Oracle Reward: 12.950
  Std Oracle Reward: 1.163
  Sequence Diversity: 1.000
  Models Used: 3
  Model R² - Mean: -0.239, Max: -0.119, Count: 10
  Total Sequences Evaluated: 770

======================================================================
DyNA PPO ALGORITHM COMPLETE!
======================================================================
Total rounds executed: 15
Total sequences evaluated: 770
Best mean reward: 11.101 (achieved at round 14)

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 15
Final Mean Reward: 10.7968
Best Mean Reward: 11.1008
Best Max Reward: 14.7613
Initial Lr: 0.0003
Final Lr: 0.0003
Total Updates: 96
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
  GGCCGGCCATAG: 12.954
  GGCCGGCCATAG: 13.366
  GGCCGGCCATAG: 13.093
  GGCCGGCCATAG: 13.085
  GGCCGGCCATAG: 13.275

Stochastic (Exploration):
  GGCGGCTGCTAT: 11.055
  GGCCGGCGCGAC: 11.474
  GAGCTGTCAGTA: 11.136
  GGCCAGTGCCTA: 12.513
  GCGAGCCGTTAC: 10.746

Final Performance:
  Mean reward: 12.270
  Max reward: 13.366
  Std reward: 0.990

   Best sequence found: GGCCGGCCATAG
   Reward: 13.366

======================================================================
Training complete! Check 'learning_curves.png' and 'training_metrics.json'
======================================================================