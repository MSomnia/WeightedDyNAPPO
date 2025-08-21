============================================================
RUNNING COMPLETE ALGORITHM 1: DyNA PPO
============================================================
Algorithm 1: DyNA PPO
Input: Number of experiment rounds N = 10
Input: Number of model-based training rounds M = 5
Input: Minimum model score τ = 0.1
Input: Batch size B = 64

=========== Experiment Round 1/10 ===========
Learning Rate: 0.000300
Exploration Rate: 0.450

--- Round 1 Generated Sequences ---:
AGACTCGTGTTT CACGTGGATAGA TTGTGACAGACC GGGGAAACTACT AGATCCGTCTGT TCCTGTCGATCG AAAGTTTTGACG TTTCGCGTTAGG CACTGAGGTGAG ACAGCCACGCAC CCCATTAGGCCG TCAATTACTACC TTACCATTTTTT AAGACCTTACAA TAATAAGACTGG TGGCATTTCGAA TTCTTTAGGTAG AAAATATTGAGG TAATGCGGGCCC TTTGCCTTATTA ... (64 total)
Round 1: Using lenient threshold (R2 > 0.0)
Model rf: R2 = -0.647
Model rf: R2 = -0.672
Model rf: R2 = -0.635
Model rf: R2 = -0.776
Model rf: R2 = -0.625
Model gb: R2 = -0.542
Model gb: R2 = -0.871
Model gb: R2 = -0.801
Model knn: R2 = -0.261
Model knn: R2 = -0.366
Model knn: R2 = -0.193
Model knn: R2 = -0.261
Model ridge: R2 = -0.207
Model xgb: R2 = -0.653
Model mlp: R2 = -1.504
Model svr: R2 = -0.297

No models met threshold. Using fallback selection...
Last resort: Using best model knn with R2 = -0.193

Selected 1 reliable models for round 1
Model types: knn
Round 1: Using 1 reliable models
Round 1 Results:
  Mean Oracle Reward: 9.179
  Min Oracle Reward: 1.277
  Max Oracle Reward: 13.266
  Standard Dev. Oracle Reward: 1.865
  Models Used: 1
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 64

=========== Experiment Round 2/10 ===========
Learning Rate: 0.000300
Exploration Rate: 0.400

--- Round 2 Generated Sequences ---:
ACCTTCGGGATA CTCGCGACAATC CCAACGGCCCGA CTTCGCGCGCGG ACGAGGACCTAG TGCTGCACGACG AGGGCTTGCAAA GCTTCTCCGTCC CGGACCGTGCCC ACGGCTTGCGAC ACGCCAGGCAAT CATCCAACGTCA AAAGAGTGGGAG ATTTGCGCCCGT GCGAGGCCGGGG GGCGGATAGAGG GAGCTGGTTGCG CAGTGCGTCAAA GGGACATCGTGC GGCTGCTTATAG ... (64 total)
Round 2: Using lenient threshold (R2 > 0.0)
Model rf: R2 = -0.274
Model rf: R2 = -0.400
Model rf: R2 = -0.330
Model rf: R2 = -0.350
Model rf: R2 = -0.375
Model gb: R2 = -0.504
Model gb: R2 = -0.899
Model gb: R2 = -1.033
Model knn: R2 = -0.058
Model knn: R2 = -0.098
Model knn: R2 = -0.072
Model knn: R2 = -0.058
Model ridge: R2 = -0.218
Model xgb: R2 = -2.120
Model mlp: R2 = -0.957
Model svr: R2 = -0.120

No models met threshold. Using fallback selection...
Last resort: Using best model knn with R2 = -0.058

Selected 1 reliable models for round 2
Model types: knn
Round 2: Using 1 reliable models
Round 2 Results:
  Mean Oracle Reward: 9.735
  Min Oracle Reward: 5.051
  Max Oracle Reward: 12.189
  Standard Dev. Oracle Reward: 1.266
  Models Used: 1
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 128

=========== Experiment Round 3/10 ===========
Learning Rate: 0.000300
Exploration Rate: 0.350

--- Round 3 Generated Sequences ---:
GGTCTGCTTCAC GGGCATGTATAG GGCAGTGGTCAA CCGGAACCGCCT CGCGAGCTAAAG GGGGGACAATCT CACCTGTGAGGT TGCTTGTTAGCT GGATACCACGCG GTCGACTCTTCC CGGCAGCTTGAC CAGCCCCGGCCC GGCGCCGGCCGT TTCGTGATTCTG GGATGCACTGAC GCGGCTTGAGGC CCCTTCCCATTG GCTCGGAACTTC GCTGACGGTTCG GGTCTCGGCTCC ... (64 total)
Round 3: Using moderate threshold (R2 > 0.050)
Model rf: R2 = -0.209
Model rf: R2 = -0.189
Model rf: R2 = -0.187
Model rf: R2 = -0.156
Model rf: R2 = -0.186
Model gb: R2 = -0.347
Model gb: R2 = -0.463
Model gb: R2 = -0.420
Model knn: R2 = -0.092
Model knn: R2 = -0.033
Model knn: R2 = -0.032
Model knn: R2 = -0.092
Model ridge: R2 = -0.202
Model xgb: R2 = -0.917
Model mlp: R2 = -0.618
Model svr: R2 = -0.108

No models met threshold. Using fallback selection...
Last resort: Using best model knn with R2 = -0.032

Selected 1 reliable models for round 3
Model types: knn
Round 3: Using 1 reliable models
Round 3 Results:
  Mean Oracle Reward: 10.054
  Min Oracle Reward: 6.312
  Max Oracle Reward: 14.054
  Standard Dev. Oracle Reward: 1.178
  Models Used: 1
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 192

=========== Experiment Round 4/10 ===========
Learning Rate: 0.000300
Exploration Rate: 0.300

--- Round 4 Generated Sequences ---:
CGGCACGCAGTG GCCTCCGGTTCT CTCCGTTAATTG GGCGCTGGTCTT CTGCAGTCTCCC GCTGCTTATTAT GCGTCGGAAACG CGCCCCTTGGTC GCGTTCGAGATG GGCGCGGACGCC CGGATGTGCCTC ATCAGCACCCTT CCACGGCGCTGC CAGTTGAGTTCC CGGTTAGTCAAT GCCGCAGCAATA CGACGCGCCGAC CGCCACGTGTCG GCGGCTATCGAT GGCTGGTCTTTC ... (64 total)
Round 4: Using moderate threshold (R2 > 0.050)
Model rf: R2 = -0.083
Model rf: R2 = -0.068
Model rf: R2 = -0.067
Model rf: R2 = -0.106
Model rf: R2 = -0.065
Model gb: R2 = -0.152
Model gb: R2 = -0.145
Model gb: R2 = -0.098
Model knn: R2 = -0.002
Model knn: R2 = 0.027
Model knn: R2 = 0.003
Model knn: R2 = -0.002
Model ridge: R2 = -0.132
Model xgb: R2 = -0.309
Model mlp: R2 = -0.487
Model svr: R2 = -0.051

No models met threshold. Using fallback selection...
Fallback: Using knn with R2 = 0.027
Fallback: Using knn with R2 = 0.003

Selected 2 reliable models for round 4
Model types: knn, knn
Round 4: Using 2 reliable models
Round 4 Results:
  Mean Oracle Reward: 9.973
  Min Oracle Reward: 6.278
  Max Oracle Reward: 12.678
  Standard Dev. Oracle Reward: 1.171
  Models Used: 2
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 256

=========== Experiment Round 5/10 ===========
Learning Rate: 0.000300
Exploration Rate: 0.250

--- Round 5 Generated Sequences ---:
CGGCATGGCATT GCGGCCGATCCG GCGCTAGTTGAC GGCCGCGCTGTA TTCCGAGCGAAT CGCAGCAGAAGT GAGGTAGGGATA GTAGCATCACAC TACGCAGTTGCT CGCAGCGGTTAG GCTGCCGTACGT GCTGCGATCCTC GCTGTCGTTTTT GCCGGCAGCTGT CGAGATCGAGGC GCGGTCGGATGG GCGGCTGCTAGG GCTGTCGCTAGC TCAGCCGGCGAT TGCCGCAGGTTT ... (64 total)
Round 5: Using moderate threshold (R2 > 0.050)
Model rf: R2 = -0.267
Model rf: R2 = -0.282
Model rf: R2 = -0.273
Model rf: R2 = -0.281
Model rf: R2 = -0.294
Model gb: R2 = -0.578
Model gb: R2 = -0.509
Model gb: R2 = -0.497
Model knn: R2 = -0.249
Model knn: R2 = -0.194
Model knn: R2 = -0.187
Model knn: R2 = -0.249
Model ridge: R2 = -0.395
Model xgb: R2 = -0.922
Model mlp: R2 = -0.796
Model svr: R2 = -0.194

No models met threshold. Using fallback selection...
Last resort: Using best model knn with R2 = -0.187

Selected 1 reliable models for round 5
Model types: knn
Round 5: Using 1 reliable models
Round 5 Results:
  Mean Oracle Reward: 10.607
  Min Oracle Reward: 7.178
  Max Oracle Reward: 12.639
  Standard Dev. Oracle Reward: 0.843
  Models Used: 1
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 320

=========== Experiment Round 6/10 ===========
Learning Rate: 0.000300
Exploration Rate: 0.200

--- Round 6 Generated Sequences ---:
GCATCCAATCGA AGTCGCGGAAGA GTCGAACGCTGT TTCGACCGCCGA GACGCAGCTCGA GGCTGCACTTGA GCTAGCGCTGCA GCATGCGGCTGC GAGCCAGCAGCT GCAGTCGTTGGT GGCTGCAGCTTA AGCAGCAGCTGC AGCTGCAGCACG GCCTGCATATCG TGCGGATGCTCG GCGCTCGATCGC GGCTGCTAGCAG GCAGCCAGCCGT GTACGGCGCCGA CGGCCGGTTGCC ... (64 total)
Round 6: Using full threshold (R2 > 0.100)
Model rf: R2 = -0.307
Model rf: R2 = -0.232
Model rf: R2 = -0.221
Model rf: R2 = -0.244
Model rf: R2 = -0.220
Model gb: R2 = -0.461
Model gb: R2 = -0.282
Model gb: R2 = -0.283
Model knn: R2 = -0.231
Model knn: R2 = -0.257
Model knn: R2 = -0.234
Model knn: R2 = -0.231
Model ridge: R2 = -0.470
Model xgb: R2 = -0.915
Model mlp: R2 = -0.698
Model svr: R2 = -0.200

No models met threshold. Using fallback selection...
Last resort: Using best model svr with R2 = -0.200

Selected 1 reliable models for round 6
Model types: svr
Round 6: Using 1 reliable models
Round 6 Results:
  Mean Oracle Reward: 10.886
  Min Oracle Reward: 8.474
  Max Oracle Reward: 12.884
  Standard Dev. Oracle Reward: 0.773
  Models Used: 1
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 384

=========== Experiment Round 7/10 ===========
Learning Rate: 0.000300
Exploration Rate: 0.150

--- Round 7 Generated Sequences ---:
GCAGCCGGCTGC GCCGCTGCGAGA GCTGCTGGCTAC GCTTGCGAGCCG CAGCGATCGCCA GCTGCTGCCGAT CGAGATGGCATC GCTGCCGCTTAC GAGGCTCTAGAA GCAGCTGGCCGG GCTGGCGATCGA GCCGTTGAGCAC GCGCTCGAAGCT GAGTCGGCTACC GAGCAGGCAGTC GTCGCCGGATCA GAGACAGCGATC TGCGGCTGCAAA GCGGACGGCACT GCAAGCGATCGT ... (64 total)
Round 7: Using full threshold (R2 > 0.100)
Model rf: R2 = -0.320
Model rf: R2 = -0.217
Model rf: R2 = -0.213
Model rf: R2 = -0.204
Model rf: R2 = -0.206
Model gb: R2 = -0.361
Model gb: R2 = -0.326
Model gb: R2 = -0.361
Model knn: R2 = -0.253
Model knn: R2 = -0.213
Model knn: R2 = -0.202
Model knn: R2 = -0.253
Model ridge: R2 = -0.455
Model xgb: R2 = -0.691
Model mlp: R2 = -0.776
Model svr: R2 = -0.158

No models met threshold. Using fallback selection...
Last resort: Using best model svr with R2 = -0.158

Selected 1 reliable models for round 7
Model types: svr
Round 7: Using 1 reliable models
Round 7 Results:
  Mean Oracle Reward: 10.805
  Min Oracle Reward: 7.905
  Max Oracle Reward: 13.042
  Standard Dev. Oracle Reward: 0.784
  Models Used: 1
  Sequence Diversity: 0.984
  Total Sequences Evaluated: 448

=========== Experiment Round 8/10 ===========
Learning Rate: 0.000300
Exploration Rate: 0.100

--- Round 8 Generated Sequences ---:
GATAGCGAACGA TCGAGCGAGCGA AGCTCGCGATAA GAAGGCTGCCAA GCTAGAGATTGA GCTAGCGAGCAA GCTAGCGCACGA GCTAGCCATCGA GCTAGCGAGCGA GCAGGCTATCAA AGCCGGCGATCG GCTCGTGCGAAT GCTAGCGAAGAA GGCTCGAGCGCT CGATTCGATCGA GCTGGCGATCGA GCTGCTGCCAGT GCTCGCGATCGA GCTAGCGATAGA AGATAGCGCTCG ... (64 total)
Round 8: Using full threshold (R2 > 0.100)
Model rf: R2 = -0.290
Model rf: R2 = -0.261
Model rf: R2 = -0.254
Model rf: R2 = -0.272
Model rf: R2 = -0.253
Model gb: R2 = -0.392
Model gb: R2 = -0.367
Model gb: R2 = -0.356
Model knn: R2 = -0.245
Model knn: R2 = -0.199
Model knn: R2 = -0.209
Model knn: R2 = -0.245
Model ridge: R2 = -0.432
Model xgb: R2 = -0.529
Model mlp: R2 = -0.648
Model svr: R2 = -0.216

No models met threshold. Using fallback selection...
Last resort: Using best model knn with R2 = -0.199

Selected 1 reliable models for round 8
Model types: knn
Round 8: Using 1 reliable models
Round 8 Results:
  Mean Oracle Reward: 9.529
  Min Oracle Reward: 4.553
  Max Oracle Reward: 12.096
  Standard Dev. Oracle Reward: 2.237
  Models Used: 1
  Sequence Diversity: 0.875
  Total Sequences Evaluated: 512

=========== Experiment Round 9/10 ===========
Learning Rate: 0.000300
Exploration Rate: 0.100

--- Round 9 Generated Sequences ---:
AGATAGAGCACA CAATAAAGCGAT GATAACGATCGA AGATAGCGCAAG AGATAGCGCGCG AGAAAGGAATCA AATAAAGAAATC GAAAGCGATCGA AGATAGAGATCG CAAAATGATAGA AGATAAGATAGC GCATATAGAGTC AGATAGCGCTCG GATAGAGCAACA ATCATACATCTA AAGAAGATAGTG AAAAAGAAAACA AGATAGAGCGAG GAACGCAGATCG AACAAGATAAAG ... (64 total)
Round 9: Using full threshold (R2 > 0.100)
Model rf: R2 = -0.208
Model rf: R2 = -0.164
Model rf: R2 = -0.168
Model rf: R2 = -0.166
Model rf: R2 = -0.161
Model gb: R2 = -0.217
Model gb: R2 = -0.200
Model gb: R2 = -0.245
Model knn: R2 = -0.179
Model knn: R2 = -0.128
Model knn: R2 = -0.141
Model knn: R2 = -0.179
Model ridge: R2 = -0.298
Model xgb: R2 = -0.346
Model mlp: R2 = -0.410
Model svr: R2 = -0.077

No models met threshold. Using fallback selection...
Last resort: Using best model svr with R2 = -0.077

Selected 1 reliable models for round 9
Model types: svr
Round 9: Using 1 reliable models
Round 9 Results:
  Mean Oracle Reward: 9.101
  Min Oracle Reward: -0.100
  Max Oracle Reward: 12.437
  Standard Dev. Oracle Reward: 2.428
  Models Used: 1
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 576

=========== Experiment Round 10/10 ===========
Learning Rate: 0.000300
Exploration Rate: 0.100

--- Round 10 Generated Sequences ---:
GATCGAGCTTCC GAATCCTCTAGC GATCTCGTCCAT TAGACTCAGCTA GATCGCGATAGA GCTCGGCTACAC AGATCGCGCGCT GCTCGCTGCATC ACTCGCTAGATC GATAGTCTGCAC GATCGCTCGATC GCTCGATCGATG ATCTAGAGCTCG TCAGACGATCTA GCTCGCTCTCGA GATCGCGCGATC GATCGCGCGCTC TAGCTCGCTCCG GATCGAGCGCGC AAGATCGTCCTC ... (64 total)
Round 10: Using full threshold (R2 > 0.100)
Model rf: R2 = -0.272
Model rf: R2 = -0.281
Model rf: R2 = -0.315
Model rf: R2 = -0.304
Model rf: R2 = -0.290
Model gb: R2 = -0.297
Model gb: R2 = -0.357
Model gb: R2 = -0.321
Model knn: R2 = -0.445
Model knn: R2 = -0.231
Model knn: R2 = -0.169
Model knn: R2 = -0.445
Model ridge: R2 = -0.385
Model xgb: R2 = -0.372
Model mlp: R2 = -0.461
Model svr: R2 = -0.116

No models met threshold. Using fallback selection...
Last resort: Using best model svr with R2 = -0.116

Selected 1 reliable models for round 10
Model types: svr
Round 10: Using 1 reliable models
Round 10 Results:
  Mean Oracle Reward: 10.537
  Min Oracle Reward: 7.785
  Max Oracle Reward: 13.368
  Standard Dev. Oracle Reward: 1.160
  Models Used: 1
  Sequence Diversity: 0.906
  Total Sequences Evaluated: 640

DyNA PPO Algorithm Complete!
Total rounds executed: 10
Total sequences evaluated: 640

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 10
Final Mean Reward: 10.5368
Best Mean Reward: 10.8861
Best Max Reward: 14.0540
Initial Lr: 0.0003
Final Lr: 0.0003
Total Updates: 140
Final Diversity: 0.9062
Convergence Round: 4
==================================================
Learning curves saved to learning_curves.png
Metrics saved to training_metrics.json

Final optimized sequences generated (from the policy trained):
  TATAGATCGCTC: 13.323
  TCTCTCGCTTCA: 9.991
  GTCTGCTACGCT: 11.398
  TCTCTCGATCTC: 9.767
  TCTAGCTCATCG: 12.310

============================================================