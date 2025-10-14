import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error
from typing import List, Tuple, Optional
import torch
import torch.nn as nn
import torch.optim as optim
from scipy.optimize import minimize

class OptimalEnsembleWeights:
    """
    Learn optimal weights for ensemble predictions using various methods.
    """
    
    """
    Args:
        method: 'validation', 'ridge', 'neural', or 'performance'
        alpha: Regularization strength for ridge regression
    """
    def __init__(self, method='validation', alpha=1.0):

        self.method = method
        self.alpha = alpha
        self.weights = None
        self.weight_history = []
        
    """
    Learn weights using validation set performance.
    Minimize: ||Σ(w_i * f_i(x)) - y||^2

    Finds the mathematically optimal combination of models by solving an optimization problem. 
    It searches for weights that minimize prediction error on a validation set while ensuring weights are non-negative and sum to 1.

    """
    def learn_weights_validation(self, models: List, X_val: np.ndarray, 
                                 y_val: np.ndarray) -> np.ndarray:

        n_models = len(models)
        
        # Step 1: Collect predictions from all models on validation data
        predictions = []
        for _, model, _ in models:
            try:
                pred = model.predict(X_val)
                predictions.append(pred)
            except:
                predictions.append(np.zeros(len(X_val)))
        
        predictions = np.array(predictions).T  # Shape: (n_samples, n_models)
        
        # Step 2: Set up optimization problem to find best weights
        # Solve for optimal weights using least squares with non-negative constraint
        # min ||Pw - y||^2 subject to w >= 0, Σw = 1
        def objective(w):
            # Calculate ensemble prediction: weighted sum of model predictions
            ensemble_pred = predictions @ w
             # Return MSE between ensemble and true values
            return mean_squared_error(y_val, ensemble_pred)
        
        # Step 3: Define constraints for valid weights
        # Constraints: weights sum to 1 and are non-negative
        constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
        bounds = [(0, 1) for _ in range(n_models)]
        
        # Step 4: Initialize optimization with equal weights for all models
        # Initialize with uniform weights
        w0 = np.ones(n_models) / n_models
        
        # Step 5: Run optimization using Sequential Least Squares Programming
        # This finds weights that minimize prediction error on validation set
        # Optimize
        result = minimize(objective, w0, method='SLSQP', bounds=bounds, constraints=constraints)
        
        weights = result.x
        return weights
    
    """
    Learn weights using Ridge regression with L2 regularization.
    This prevents overfitting to training data.

    Uses Ridge regression to learn how to combine model predictions. 
    Ridge adds L2 penalty to prevent overfitting, but can produce negative weights (which get clipped to 0).
    """
    def learn_weights_ridge(self, models: List, X_train: np.ndarray, 
                           y_train: np.ndarray) -> np.ndarray:

        n_models = len(models)
        
        # Step 1: Collect predictions from all models
        # Get predictions from each model
        predictions = []
        for _, model, _ in models:
            try:
                pred = model.predict(X_train)
                predictions.append(pred)
            except:
                predictions.append(np.zeros(len(X_train)))
        
        predictions = np.array(predictions).T  # Shape: (n_samples, n_models)
        
        # Step 2: Use Ridge regression to learn how to combine predictions
        # Ridge regression to find weights
        ridge = Ridge(alpha=self.alpha, fit_intercept=False)
        ridge.fit(predictions, y_train)
        
        # Step 3: Extract and process weights
        # Get weights and normalize to sum to 1
        weights = ridge.coef_
        weights = np.maximum(weights, 0)  # Ensure non-negative

        # Normalize so weights sum to 1 (required for valid ensemble)
        # Add 1e-10 to avoid division by zero if all weights are 0
        weights = weights / (weights.sum() + 1e-10)
        
        return weights
    

    """
    Weight models based on their R2 scores.
    Better performing models get higher weights.
    Simple performance-based weighting. 
    Models with higher R2 scores get exponentially higher weights. 
    """
    # def learn_weights_performance(self, models: List) -> np.ndarray:

    #     scores = []
    #     for _, _, score in models:
    #         # Transform R2 score to weight (handle negative R2)
    #         # Use exponential to emphasize good models
    #         weight = np.exp(max(0, score + 0.5))
    #         scores.append(weight)
        
    #     scores = np.array(scores)
    #     # Normalize weights to sum to 1
    #     weights = scores / scores.sum()
        
    #     return weights
    
    def learn_weights_performance(self, models: List, temperature: float = 0.1) -> np.ndarray:
        scores = np.array([score for _, _, score in models])
        # Lower temperature → more extreme differences
        # Higher temperature → more uniform weights
        exp_scores = np.exp(scores / temperature)
        weights = exp_scores / exp_scores.sum()
        return weights
    


    
    # def learn_weights_neural(self, models: List, X_train: np.ndarray, 
    #                         y_train: np.ndarray, epochs: int = 100) -> np.ndarray:
    #     """
    #     Learn weights using a small neural network.
    #     The network learns to combine model predictions optimally.
    #     """
    #     n_models = len(models)
        
    #     # Get predictions
    #     predictions = []
    #     for _, model, _ in models:
    #         try:
    #             pred = model.predict(X_train)
    #             predictions.append(pred)
    #         except:
    #             predictions.append(np.zeros(len(X_train)))
        
    #     predictions = np.array(predictions).T  # Shape: (n_samples, n_models)
        
    #     # Define weight learning network
    #     class WeightNet(nn.Module):
    #         def __init__(self, n_models):
    #             super().__init__()
    #             self.weights = nn.Parameter(torch.ones(n_models) / n_models)
    #             self.softmax = nn.Softmax(dim=0)
                
    #         def forward(self, x):
    #             w = self.softmax(self.weights)
    #             return x @ w
        
    #     # Convert to torch tensors
    #     X_torch = torch.FloatTensor(predictions)
    #     y_torch = torch.FloatTensor(y_train)
        
    #     # Train network
    #     net = WeightNet(n_models)
    #     optimizer = optim.Adam([net.weights], lr=0.01)
    #     criterion = nn.MSELoss()
        
    #     for epoch in range(epochs):
    #         optimizer.zero_grad()
    #         output = net(X_torch)
    #         loss = criterion(output, y_torch)
    #         loss.backward()
    #         optimizer.step()
        
    #     # Extract learned weights
    #     with torch.no_grad():
    #         weights = net.softmax(net.weights).numpy()
        
    #     return weights