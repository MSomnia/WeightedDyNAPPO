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
from xgboost import XGBRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
"""
Wrapper for surrogate models
"""
class SurrogateModel:
    
    def __init__(self, model_type: str, **kwargs):
        self.model_type = model_type
        self.scaler = StandardScaler()
        
        # a list of machine learning models for the surrogate model
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
        elif model_type == 'xgb':
            self.model = XGBRegressor(**kwargs)
        elif model_type == 'mlp':
            self.model = MLPRegressor(**kwargs)
        elif model_type == 'svr':
            self.model = SVR(**kwargs)
        else:
            raise ValueError(f"Unknown model type: {model_type}")
    
    """
    Fit the model
    """
    def fit(self, X: np.ndarray, y: np.ndarray):
        # Scale the input features to have standard normal distribution
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
    
    """
    Make predictions
    """
    def predict(self, X: np.ndarray) -> np.ndarray:
        # Scale the input data using the same scaling parameters from training
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)
    
    """
    Get R2 score using cross-validation
    """
    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        X_scaled = self.scaler.fit_transform(X)
        # Perform 5-fold cross-validation to get R2 scores
        scores = cross_val_score(self.model, X_scaled, y, cv=5, scoring='r2')
        return scores.mean()