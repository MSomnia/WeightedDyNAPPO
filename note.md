
# DyNA PPO flow
1. Initialize neural network policy π_θ
2. For each round n:

   a. Generate sequences using π_θ

   b. Evaluate with oracle function f(x)

   c. Update π_θ using PPO

   d. Train surrogate models on accumulated data

   e. If reliable models exist:
      - Generate additional sequences using π_θ
      - Predict rewards using surrogate ensemble
      - Update π_θ using predicted rewards
3. Return optimized policy π_θ

# Neural Network and Surrogate Models
## Neural Network (PolicyNetwork)
The neural network serves as the generative policy that learns to create biological sequences. It's an autoregressive model that:

- Uses character embeddings and positional encoding to understand sequence context
- Has two heads: a policy head (predicts next token probabilities) and a value head (estimates sequence quality)
- Generates sequences token-by-token using a sliding context window
- Gets updated using PPO (Proximal Policy Optimization) based on rewards

## Surrogate Models
The surrogate models act as cheap approximations of the expensive oracle function.

- Maintains a diverse ensemble of models (Random Forest, Gradient Boosting, KNN, Ridge regression)
- Converts sequences to one-hot encoded feature vectors
- Uses cross-validation to select only reliable models (score ≥ threshold)
- Combines predictions through ensemble averaging

## Integration Strategy
Alternating training phases:
1. Oracle Phase: Neural network generates sequences → Oracle evaluates them → Policy updates with PPO
2. Model Phase: If surrogate models are reliable → Generate more sequences → Predict rewards with surrogates → Additional policy updates (no oracle needed)

This creates a powerful feedback loop where the neural network learns to generate increasingly better sequences while the surrogate models provide sample-efficient training by reducing expensive oracle calls.


# Reinforcement Learning and Neural Networks
## Neural Networks as Function Approximators
The Core Problem: Classical RL uses lookup tables (Q-tables) to store values for every possible state-action pair. This works for simple problems like tic-tac-toe but completely breaks down for complex environments with millions or infinite states.

The Solution: Neural networks can approximate complex functions from high-dimensional inputs, allowing RL to scale to real-world problems.

## Example: Learn to Drive
### Traditional RL:
Situation 1: Car 10 feet ahead → Brake

Situation 2: Car 20 feet ahead → Maintain speed

Situation 3: Traffic light yellow → Slow down

...

Problem: You'd need to write down EVERY possible situation! That's impossible.

### Neural Network + RL
Instead of a cheat sheet, you learn general rules:

"If something is close, be careful"

"If the light is red, stop"

"If the road curves, turn the wheel"

### How They Work Together
Neural Network = The "Smart Brain"

Think of it as a super-smart pattern recognition system:

Input: What you see (road, cars, signs)

↓

Neural Network: "I recognize this pattern..."

↓

Output: What to do (turn, brake, accelerate)

Reinforcement Learning = The "Learning Method"

This is how the brain gets smarter:
1. Try something
2. See what happens (good or bad)
3. Remember: "That worked well" or "That was terrible"
4. Adjust for next time


# DyNA PPO example
## Initial Exploration
1. Generate DNA Sequences (Policy Network as "Molecular Designer")

The policy network starts with no knowledge, so it generates random sequences:
Sequence 1: ATCGATCG

Sequence 2: GGCCTTAA 

Sequence 3: TACGTACG

... (32 sequences total)


How the Policy Works:

At position 0: "What base?" → 25% A, 25% T, 25% G, 25% C

At position 1: "What base after A?" → Still uniform (no knowledge yet)

2. Lab Testing (Oracle Function)

Artifical test binding affinity:

ATCGATCG: Binding score = 0.3 (weak)

GGCCTTAA: Binding score = 0.1 (very weak)

TACGTACG: Binding score = 0.7 (good!)

GGCGTACC: Binding score = 0.8 (great!)


3. Policy Update (Learning from Data)

The policy network learns:

"Sequences with alternating purines/pyrimidines (like TACGTACG) work well"
"GC-rich sequences in the middle seem important"
"Avoid long stretches of the same base"

Now the policy might generate:

At position 3: After "TAC" → 60% G, 30% C, 10% others

## Building a Predictive Model

1. Generate Smarter Sequences

With updated policy:

Sequence 33: CGCGTACG (similar to good ones)

Sequence 34: TACGCGTA (variation of winner)

Sequence 35: GCGCTATA (trying GC-rich core)

2. Train Surrogate Models

With 64 sequences tested, we train multiple models:

Random Forest: "I see patterns in GC content and positions 3-5"

Cross-validation R² = 0.72 ✓ (Reliable!)

Neural Network: "Everything correlates with everything!"

Cross-validation R² = 0.31 ✗ (Not reliable)

K-Nearest Neighbors: "Sequences similar to GGCGTACC are good"

Cross-validation R² = 0.68 ✓ (Reliable!)

3. Virtual Screening (Model-Based Training)

Since we have reliable models, we can now:

Generate 500 virtual sequences:

Virtual 1: CGCGTACG → Predicted binding = 0.75

Virtual 2: GGCGTAGC → Predicted binding = 0.82

Virtual 3: AAAAGGGG → Predicted binding = 0.15

Update policy based on predictions (no lab work!):

Reinforces: GC-rich centers are good

Learns: Position 4 should usually be G

Discovers: CGC at start predicts high binding

## Advanced Learning

Model Evolution

As more data accumulates:

Round 3 (96 sequences):

Models discover: "GCG motif at positions 3-5 is critical"

New pattern: "Complementary bases at positions 1&8 help"


Round 4 (128 sequences):

Models can predict novel combinations

Identifies exception: "ATCGTACG breaks the rules but works!"


Round 5 (160 sequences):

Models are experts

Can predict 90% of binding scores accurately

Generate 1000s of virtual candidates


Diversity Mechanism in Action

Without diversity penalty:

Top sequences found: GGCGTACC, GGCGTACG, GGCGTACT

(All nearly identical - risky if lab conditions change!)


With diversity penalty:

Top diverse sequences:
- GGCGTACC (the champion)
- TACGTACG (alternative mechanism) 
- CGCGCGCG (different pattern)
- ATCGTACG (rule breaker)


This diversity is crucial because:

Different binding mechanisms might work in vivo

Provides backup options

Reveals multiple solutions to the problem


# DyNA PPO Guide
## create_surrogate_models()
Create a diverse pool of machine learning models that will learn to predict sequence performance.

## generate_sequence()
Generates a single sequence by making decisions at each position based on learned probabilities.

At each position, asks the policy network "what should come next?"

## generate_batch()
Generate multiple sequences at once for efficient batch testing.

## compute_rewards()
Evaluate sequences using the oracle function and applies diversity bonus.

get the true score from the lab testing.

## update_policy()
Update the neural network based on which sequences performed well or poorly.

Use PPO, update both policy network and value network.

- computes current log probabilities for each sequence
- calculates advantages: rewards - baseline values
- computes PPO loss with clipping to prevent large updates
- updates both policy and value networds

## fit_surrogate_models()
Trains multiple models to predict sequence performance.
- test each model type using cv
- only keeps models that R2 is greater than the threshold

## predict_with_ensemble()
Use multiple trained models to predict sequence performance.
- each reliable model makes a prediction
- average all prediction - where we want to customize

## train_round()
Execute one complete round of DyNA PPO.
Combine and use the functions above.

E[R(s_{1:T})|s_0, θ]

One complete cycle of:
   1. Generate DNA sequences
   2. Test in lab (expensive)
   3. Learn from results
   4. Use models for virtual testing
   5. Learn more from virtual results

### Phase 1 - REAL LAB
- Generates sequences using current policy
- Tests them with expensive oracle function
- Updates policy based on real results

### Phase 2 - Virtual Testing
- Trains surrogate models on all historical data
- If models are reliable:
   - Generates many more sequences
   - Tests them virtually
   - Updates policy based on predictions






1. Try different types of oracle function: classification
2. batch size, sequence length, number of round
3. dynamic tau
4. scatter plot 
