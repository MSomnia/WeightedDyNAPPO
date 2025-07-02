#   FILE: SurrogateModel.py
#   PROJECT: Optimal Ensemble Weights DyNA PPO
#   AUTHOR: Eric Lin
#   This file contains the reinforcement learning surrogate model part of the project.

import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler

class SurrogateModel:
    """Wrapper for surrogate models."""
    
    def __init__(self, model_type: str, **kwargs):
        self.model_type = model_type
        self.scaler = StandardScaler()
        
        if model_type == 'rf':
            self.model = RandomForestRegressor(**kwargs)
        elif model_type == 'gb':
            self.model = GradientBoostingRegressor(**kwargs)
        elif model_type == 'gp':
            self.model = GaussianProcessRegressor(**kwargs)
        elif model_type == 'knn':
            self.model = KNeighborsRegressor(**kwargs)
        elif model_type == 'ridge':
            self.model = BayesianRidge(**kwargs)
        else:
            raise ValueError(f"Unknown model type: {model_type}")
    
    def fit(self, X: np.ndarray, y: np.ndarray):
        """Fit the model."""
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Make predictions."""
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)
    
    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """Get R2 score using cross-validation."""
        X_scaled = self.scaler.fit_transform(X)
        scores = cross_val_score(self.model, X_scaled, y, cv=5, scoring='r2')
        return scores.mean()