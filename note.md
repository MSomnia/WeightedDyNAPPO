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