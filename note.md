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
