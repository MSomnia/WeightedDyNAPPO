============================================================
RUNNING COMPLETE ALGORITHM 1: DyNA PPO
============================================================
Algorithm 1: DyNA PPO
Input: Number of experiment rounds N = 10
Input: Number of model-based training rounds M = 5
Input: Minimum model score τ = 0.1
Input: Batch size B = 32

=== Experiment Round 1/10 ===
Learning Rate: 0.000272
Exploration Rate: 0.450

--- Round 1 Generated Sequences ---:
GGAGATTT GCTTGTGA TTGCCAGC TTAACACA GTCTATAT TCATCTAC AAAGAAAA GCCGCGCG AAAAGTTT GGGATCAT AAAAACAT AGGGAAAG GCGACTCA AACGGCTG CGATGTCT CCCTAAGG TTAAACCC CCGGCAGC TGTGACCG GAACCTAA ... (32 total)
Round 1: Using lenient threshold (R2 > 0.0)
Model rf: R2 = -0.038
Model rf: R2 = -0.103
Model rf: R2 = -0.034
Model rf: R2 = -0.003
Model rf: R2 = -0.033
Model gb: R2 = -0.060
Model gb: R2 = -1.061
Model gb: R2 = -1.240
Model knn: R2 = -0.764
Model knn: R2 = -0.288
Model knn: R2 = -0.764
Model ridge: R2 = -0.417
Model xgb: R2 = -0.237
Model mlp: R2 = -2.166
Model svr: R2 = 0.063
Model svr selected (R2 = 0.063 >= 0.000)

Selected 1 reliable models for round 1
Model types: svr
Round 1: Using 1 reliable models
Round 1 Results:
  Mean Oracle Reward: 6.858
  Min Oracle Reward: 1.154
  Max Oracle Reward: 8.988
  Standard Dev. Oracle Reward: 1.970
  Models Used: 1
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 32

=== Experiment Round 2/10 ===
Learning Rate: 0.000200
Exploration Rate: 0.400

--- Round 2 Generated Sequences ---:
TTTCAAGT TAGGGTCT TATACTGT ACCCGTGG GACTGTGA TAGCTCCC ACTCGGGT AGGTTTCC GCTTGTGG TAGTCCGC TAGGCTCC CCTGTATT TCGTCCAA AGCTGGAA GTGGAACA TTGTGTTA GTTTGTCG TGTTGATG GGGCTAGT TTCCTGTC ... (32 total)
Round 2: Using lenient threshold (R2 > 0.0)
Model rf: R2 = -0.130
Model rf: R2 = -0.100
Model rf: R2 = -0.123
Model rf: R2 = -0.046
Model rf: R2 = -0.130
Model gb: R2 = -0.200
Model gb: R2 = -0.456
Model gb: R2 = -0.456
Model knn: R2 = -0.257
Model knn: R2 = -0.155
Model knn: R2 = -0.257
Model ridge: R2 = -0.681
Model xgb: R2 = -0.194
Model mlp: R2 = -1.177
Model svr: R2 = -0.066

No models met threshold. Using fallback selection...
Last resort: Using best model rf with R2 = -0.046

Selected 1 reliable models for round 2
Model types: rf
Round 2: Using 1 reliable models
Round 2 Results:
  Mean Oracle Reward: 7.609
  Min Oracle Reward: 5.196
  Max Oracle Reward: 9.750
  Standard Dev. Oracle Reward: 0.995
  Models Used: 1
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 64

=== Experiment Round 3/10 ===
Learning Rate: 0.000110
Exploration Rate: 0.350

--- Round 3 Generated Sequences ---:
GTCCTGTT TAGTGGTG GTTCGCGG CCGCTGAT GTTTTTGT TGCGTCTA GACATGTG GTTCGGAG GCTTGCGG CAGATTCT AGCACACT ATGGCGTG GACTTTGC TCGTTCGG GCGACTCG GGGCGAGG TTAGTCGC TGGCCGCT GAGCGAGG GCTAGGGT ... (32 total)
Round 3: Using moderate threshold (R2 > 0.050)
Model rf: R2 = 0.071
Model rf selected (R2 = 0.071 >= 0.050)
Model rf: R2 = 0.009
Model rf: R2 = 0.016
Model rf: R2 = 0.007
Model rf: R2 = -0.002
Model gb: R2 = -0.099
Model gb: R2 = -0.270
Model gb: R2 = -0.263
Model knn: R2 = -0.168
Model knn: R2 = -0.079
Model knn: R2 = -0.168
Model ridge: R2 = -0.116
Model xgb: R2 = -0.155
Model mlp: R2 = -0.640
Model svr: R2 = -0.053

Selected 1 reliable models for round 3
Model types: rf
Round 3: Using 1 reliable models
Round 3 Results:
  Mean Oracle Reward: 7.563
  Min Oracle Reward: 2.357
  Max Oracle Reward: 10.396
  Standard Dev. Oracle Reward: 1.496
  Models Used: 1
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 96

=== Experiment Round 4/10 ===
Learning Rate: 0.000038
Exploration Rate: 0.300

--- Round 4 Generated Sequences ---:
ATTCCTCA AATCTTAC CATGGCTT TGAGATCG CCCGCTGG TTGCTAAC ATGTTGAA TTGTGGCC CATGGTCC GTATGCGC CCGTTGCG CTTCGGGC GCATTCCG TCGGCCTT TCCCCCCA CTTCGCGC CGCGCTCG CGCTCCTG GCACCAAT AGTTCCCT ... (32 total)
Round 4: Using moderate threshold (R2 > 0.050)
Model rf: R2 = -0.138
Model rf: R2 = -0.153
Model rf: R2 = -0.130
Model rf: R2 = -0.114
Model rf: R2 = -0.107
Model gb: R2 = -0.154
Model gb: R2 = -0.302
Model gb: R2 = -0.286
Model knn: R2 = -0.109
Model knn: R2 = -0.032
Model knn: R2 = -0.109
Model ridge: R2 = -0.121
Model xgb: R2 = -0.554
Model mlp: R2 = -0.383
Model svr: R2 = -0.015

No models met threshold. Using fallback selection...
Last resort: Using best model svr with R2 = -0.015

Selected 1 reliable models for round 4
Model types: svr
Round 4: Using 1 reliable models
Round 4 Results:
  Mean Oracle Reward: 7.410
  Min Oracle Reward: 2.280
  Max Oracle Reward: 9.941
  Standard Dev. Oracle Reward: 1.419
  Models Used: 1
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 128

=== Experiment Round 5/10 ===
Learning Rate: 0.000300
Exploration Rate: 0.250

--- Round 5 Generated Sequences ---:
TATCGCCC CACTGGGC TCGACGGG TATACTCG ATTGATGG TGCCCGCC GTCTCCGT TTATCGCG CGTGCGGT TTCACGCC TTGTAGCT TGCCAGGC TCTGACCG TTCGGGCG TTGCTTGC TTATGTGG TCGCGCCC GTTACGCC TTTGCTTC GAGGGTTG ... (32 total)
Round 5: Using moderate threshold (R2 > 0.050)
Model rf: R2 = -0.132
Model rf: R2 = -0.113
Model rf: R2 = -0.132
Model rf: R2 = -0.144
Model rf: R2 = -0.106
Model gb: R2 = -0.191
Model gb: R2 = -0.240
Model gb: R2 = -0.202
Model knn: R2 = -0.026
Model knn: R2 = -0.069
Model knn: R2 = -0.026
Model ridge: R2 = -0.145
Model xgb: R2 = -0.245
Model mlp: R2 = -0.517
Model svr: R2 = -0.075

No models met threshold. Using fallback selection...
Last resort: Using best model knn with R2 = -0.026

Selected 1 reliable models for round 5
Model types: knn
Round 5: Using 1 reliable models
Round 5 Results:
  Mean Oracle Reward: 7.463
  Min Oracle Reward: 3.888
  Max Oracle Reward: 9.363
  Standard Dev. Oracle Reward: 1.216
  Models Used: 1
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 160

=== Experiment Round 6/10 ===
Learning Rate: 0.000272
Exploration Rate: 0.200

--- Round 6 Generated Sequences ---:
TGAGGGCA ATTGGTTC ACGGGCCT TGGCCCGC CTGGTGGG TGGATGGC TGATCGCG TAGCGCGA ACGATGTA CTTGGCTT TGGTAGGC ATCGCGGC TGTAGCTG AGCGTCGT TACTGCTG TGTCCGGC TTGGACCC CTGTGTGC TTGTTGTG TGCCGAAC ... (32 total)
Round 6: Using full threshold (R2 > 0.100)
Model rf: R2 = -0.096
Model rf: R2 = -0.126
Model rf: R2 = -0.095
Model rf: R2 = -0.138
Model rf: R2 = -0.068
Model gb: R2 = -0.191
Model gb: R2 = -0.270
Model gb: R2 = -0.272
Model knn: R2 = 0.081
Model knn: R2 = 0.009
Model knn: R2 = 0.081
Model ridge: R2 = -0.121
Model xgb: R2 = -0.370
Model mlp: R2 = -0.429
Model svr: R2 = -0.004

No models met threshold. Using fallback selection...
Fallback: Using knn with R2 = 0.081
Fallback: Using knn with R2 = 0.081
Fallback: Using knn with R2 = 0.009

Selected 3 reliable models for round 6
Model types: knn, knn, knn
Round 6: Using 3 reliable models
Round 6 Results:
  Mean Oracle Reward: 7.705
  Min Oracle Reward: 5.465
  Max Oracle Reward: 10.180
  Standard Dev. Oracle Reward: 1.202
  Models Used: 3
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 192

=== Experiment Round 7/10 ===
Learning Rate: 0.000200
Exploration Rate: 0.150

--- Round 7 Generated Sequences ---:
TCTAACAG AATGTGTG TGACAGGA TCATGGTC TATCAGAG AATATTAG TGCAGGTG GTACTCGA TATAGCGA TTTAGCCA TCGTATGG TAATATTG CTATTAGC TTGTAGAT GATGGGGA TATTGATC TATATGGT TTGTATGA TCGCATCA TTGCGCCG ... (32 total)
Round 7: Using full threshold (R2 > 0.100)
Model rf: R2 = 0.023
Model rf: R2 = 0.067
Model rf: R2 = 0.068
Model rf: R2 = 0.033
Model rf: R2 = 0.041
Model gb: R2 = 0.056
Model gb: R2 = -0.001
Model gb: R2 = -0.023
Model knn: R2 = 0.082
Model knn: R2 = 0.108
Model knn selected (R2 = 0.108 >= 0.100)
Model knn: R2 = 0.082
Model ridge: R2 = -0.089
Model xgb: R2 = -0.111
Model mlp: R2 = -0.195
Model svr: R2 = 0.034

Selected 1 reliable models for round 7
Model types: knn
Round 7: Using 1 reliable models
Round 7 Results:
  Mean Oracle Reward: 7.050
  Min Oracle Reward: 3.611
  Max Oracle Reward: 10.119
  Standard Dev. Oracle Reward: 1.501
  Models Used: 1
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 224

=== Experiment Round 8/10 ===
Learning Rate: 0.000110
Exploration Rate: 0.100

--- Round 8 Generated Sequences ---:
TCATAGCG TACAGAGC TGGTGGTG ACCACGGA AGACATCA TACAATGA GGTCCGGG TCGACGAT TGGACGCC TATCCCCC GATCGAAC ATCGATGA CGCCGCCT GACTTCGG TATGGCGC TGTAGGGA ATATGGCA TATATAGG GGGCATAG CGCCTGCA ... (32 total)
Round 8: Using full threshold (R2 > 0.100)
Model rf: R2 = -0.080
Model rf: R2 = -0.015
Model rf: R2 = -0.010
Model rf: R2 = 0.006
Model rf: R2 = 0.013
Model gb: R2 = -0.008
Model gb: R2 = 0.020
Model gb: R2 = -0.030
Model knn: R2 = 0.060
Model knn: R2 = 0.066
Model knn: R2 = 0.060
Model ridge: R2 = -0.067
Model xgb: R2 = -0.226
Model mlp: R2 = -0.113
Model svr: R2 = 0.048

No models met threshold. Using fallback selection...
Fallback: Using knn with R2 = 0.066
Fallback: Using knn with R2 = 0.060
Fallback: Using knn with R2 = 0.060

Selected 3 reliable models for round 8
Model types: knn, knn, knn
Round 8: Using 3 reliable models
Round 8 Results:
  Mean Oracle Reward: 7.524
  Min Oracle Reward: 5.258
  Max Oracle Reward: 9.700
  Standard Dev. Oracle Reward: 1.206
  Models Used: 3
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 256

=== Experiment Round 9/10 ===
Learning Rate: 0.000038
Exploration Rate: 0.100

--- Round 9 Generated Sequences ---:
TGACGAAT GCACGGAT GACTGCCC GCAAAACG CGATCAAG TGACGACA CGGCACAG CGAATGAG CGACCCCT AGGCAGAC CGAGACCT GCGACCGT AGGGACGG GCAAGACG TGCACGCT TGATGGAC TATCGCGG GACAGACG TGTGGGCA TGAAGAAT ... (32 total)
Round 9: Using full threshold (R2 > 0.100)
Model rf: R2 = 0.021
Model rf: R2 = 0.099
Model rf: R2 = 0.086
Model rf: R2 = 0.066
Model rf: R2 = 0.090
Model gb: R2 = 0.060
Model gb: R2 = -0.025
Model gb: R2 = -0.063
Model knn: R2 = 0.092
Model knn: R2 = 0.087
Model knn: R2 = 0.092
Model ridge: R2 = -0.072
Model xgb: R2 = -0.227
Model mlp: R2 = 0.131
Model mlp selected (R2 = 0.131 >= 0.100)
Model svr: R2 = 0.077

Selected 1 reliable models for round 9
Model types: mlp
Round 9: Using 1 reliable models
Round 9 Results:
  Mean Oracle Reward: 7.580
  Min Oracle Reward: 5.299
  Max Oracle Reward: 8.794
  Standard Dev. Oracle Reward: 0.892
  Models Used: 1
  Sequence Diversity: 0.969
  Total Sequences Evaluated: 288

=== Experiment Round 10/10 ===
Learning Rate: 0.000300
Exploration Rate: 0.100

--- Round 10 Generated Sequences ---:
TGAAGCGA GGCAGTCA TGAAGCTG TGGAAGTC TGAATGGC TCGCGGTA TGGACTGG GGAGGAAT TTGGGGAC GGATGGAT TAGAGCAC CCAGACCC GAGAGGGC TTGGGCTG TGGCCGAC GGACGCCA GCCCTAGA GACAGCTA GACAGACG TGGAAGAT ... (32 total)
Round 10: Using full threshold (R2 > 0.100)
Model rf: R2 = 0.020
Model rf: R2 = 0.110
Model rf selected (R2 = 0.110 >= 0.100)
Model rf: R2 = 0.101
Model rf selected (R2 = 0.101 >= 0.100)
Model rf: R2 = 0.089
Model rf: R2 = 0.120
Model rf selected (R2 = 0.120 >= 0.100)
Model gb: R2 = 0.090
Model gb: R2 = 0.072
Model gb: R2 = 0.004
Model knn: R2 = 0.097
Model knn: R2 = 0.140
Model knn selected (R2 = 0.140 >= 0.100)
Model knn: R2 = 0.097
Model ridge: R2 = -0.043
Model xgb: R2 = -0.220
Model mlp: R2 = 0.154
Model mlp selected (R2 = 0.154 >= 0.100)
Model svr: R2 = 0.126
Model svr selected (R2 = 0.126 >= 0.100)

Selected 6 reliable models for round 10
Model types: rf, rf, rf, knn, mlp, svr
Round 10: Using 6 reliable models
Round 10 Results:
  Mean Oracle Reward: 7.496
  Min Oracle Reward: 5.777
  Max Oracle Reward: 9.657
  Standard Dev. Oracle Reward: 0.883
  Models Used: 6
  Sequence Diversity: 1.000
  Total Sequences Evaluated: 320

DyNA PPO Algorithm Complete!
Total rounds executed: 10
Total sequences evaluated: 320

==================================================
TRAINING SUMMARY
==================================================
Total Rounds: 10
Final Mean Reward: 7.4957
Best Mean Reward: 7.7054
Best Max Reward: 10.3956
Initial Lr: 0.0003
Final Lr: 0.0003
Total Updates: 140
Final Diversity: 1.0000
Convergence Round: 3
==================================================
Learning curves saved to learning_curves.png
Metrics saved to training_metrics.json

Final optimized sequences:
  GCATCGAC: 10.155
  GCATCGAC: 10.230
  GCATCGAC: 10.434
  GCATCGAC: 10.177
  GCATCGAC: 10.285

============================================================