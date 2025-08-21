import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Optional
import json
from datetime import datetime

"""
Track learning rate and other training metrics for DyNA PPO.
"""
class LearningMetricsTracker:
    def __init__(self):
        self.metrics = {
            'round': [],
            'oracle_mean_reward': [],
            'oracle_max_reward': [],
            'oracle_min_reward': [],
            'oracle_std_reward': [],
            'policy_loss': [],
            'value_loss': [],
            'total_loss': [],
            'learning_rate': [],
            'gradient_norm': [],
            'sequence_diversity': [],
            'model_r2_scores': [],
            'model_prediction_error': [],
            'exploration_rate': [],
            'kl_divergence': [],
            'entropy': [],
            'advantage_mean': [],
            'advantage_std': [],
            'value_accuracy': [],
            'timestamp': []
        }
        
        # Per-update metrics (multiple per round)
        self.update_metrics = {
            'update_idx': [],
            'round': [],
            'policy_loss': [],
            'value_loss': [],
            'total_loss': [],
            'gradient_norm': [],
            'kl_divergence': []
        }
    

    """
    Log metrics for a training round.
    """
    def log_round_metrics(self, round_num: int, results: Dict, learning_rate: float, exploration_rate: float = 0.0):
        
        self.metrics['round'].append(round_num)
        self.metrics['oracle_mean_reward'].append(results.get('mean_oracle_reward', 0))
        self.metrics['oracle_max_reward'].append(results.get('max_oracle_reward', 0))
        self.metrics['oracle_min_reward'].append(results.get('min_oracle_reward', 0))
        self.metrics['oracle_std_reward'].append(results.get('std_oracle_reward', 0))
        self.metrics['learning_rate'].append(learning_rate)
        self.metrics['exploration_rate'].append(exploration_rate)
        self.metrics['sequence_diversity'].append(results.get('sequence_diversity', 0))
        self.metrics['timestamp'].append(datetime.now().isoformat())
        
        # Add model R2 scores if available
        if 'model_r2_scores' in results:
            self.metrics['model_r2_scores'].append(results['model_r2_scores'])
        else:
            self.metrics['model_r2_scores'].append([])
    

    """
    Log metrics for a single policy update.
    """
    def log_update_metrics(self, round_num: int, update_idx: int, policy_loss: float, value_loss: float, 
                           total_loss: float, gradient_norm: float,kl_divergence: float = 0.0):
        
        self.update_metrics['round'].append(round_num)
        self.update_metrics['update_idx'].append(update_idx)
        self.update_metrics['policy_loss'].append(policy_loss)
        self.update_metrics['value_loss'].append(value_loss)
        self.update_metrics['total_loss'].append(total_loss)
        self.update_metrics['gradient_norm'].append(gradient_norm)
        self.update_metrics['kl_divergence'].append(kl_divergence)
    

    """
    Generate comprehensive learning curves.
    """
    def plot_learning_curves(self, save_path: Optional[str] = None):
        
        fig, axes = plt.subplots(3, 3, figsize=(15, 12))
        fig.suptitle('DyNA PPO Learning Curves', fontsize=16)
        
        # 1. Rewards over rounds
        ax = axes[0, 0]
        ax.plot(self.metrics['round'], self.metrics['oracle_mean_reward'], 'b-', label='Mean')
        ax.fill_between(self.metrics['round'], 
                       self.metrics['oracle_min_reward'], 
                       self.metrics['oracle_max_reward'], 
                       alpha=0.3, label='Min-Max Range')
        ax.set_xlabel('Round')
        ax.set_ylabel('Oracle Reward')
        ax.set_title('Oracle Rewards')
        ax.legend()
        ax.grid(True)
        
        # 2. Learning rate
        ax = axes[0, 1]
        ax.plot(self.metrics['round'], self.metrics['learning_rate'], 'g-', linewidth=2)
        ax.set_xlabel('Round')
        ax.set_ylabel('Learning Rate')
        ax.set_title('Learning Rate Schedule')
        ax.grid(True)
        
        # 3. Loss over updates
        if self.update_metrics['update_idx']:
            ax = axes[0, 2]
            ax.plot(self.update_metrics['policy_loss'], 'r-', alpha=0.6, label='Policy Loss')
            ax.plot(self.update_metrics['value_loss'], 'b-', alpha=0.6, label='Value Loss')
            ax.plot(self.update_metrics['total_loss'], 'k-', alpha=0.8, label='Total Loss')
            ax.set_xlabel('Update Step')
            ax.set_ylabel('Loss')
            ax.set_title('Training Losses')
            ax.legend()
            ax.grid(True)
        
        # 4. Gradient norms
        if self.update_metrics['gradient_norm']:
            ax = axes[1, 0]
            ax.semilogy(self.update_metrics['gradient_norm'], 'purple')
            ax.set_xlabel('Update Step')
            ax.set_ylabel('Gradient Norm (log scale)')
            ax.set_title('Gradient Magnitude')
            ax.grid(True)
        
        # 5. Sequence diversity
        ax = axes[1, 1]
        ax.plot(self.metrics['round'], self.metrics['sequence_diversity'], 'orange', linewidth=2)
        ax.set_xlabel('Round')
        ax.set_ylabel('Diversity Ratio')
        ax.set_title('Sequence Diversity')
        ax.set_ylim(0, 1.1)
        ax.grid(True)
        
        # 6. Model R2 scores
        ax = axes[1, 2]
        for round_idx, r2_scores in enumerate(self.metrics['model_r2_scores']):
            # if r2_scores:
            #     round_num = self.metrics['round'][round_idx]
            #     ax.scatter([round_num] * len(r2_scores), r2_scores, alpha=0.6)
            if r2_scores:
                round_num = self.metrics['round'][round_idx]
                
                # Filter the scores to only include those greater than -5
                filtered_scores = [score for score in r2_scores if score > -5]
                
                # Only plot if there are scores remaining after the filter
                if filtered_scores:
                    # Create a corresponding list of round numbers for the x-axis
                    x_coords = [round_num] * len(filtered_scores)
                    ax.scatter(x_coords, filtered_scores, alpha=0.6)
                    
        ax.axhline(y=0, color='r', linestyle='--', alpha=0.5)
        ax.set_xlabel('Round')
        ax.set_ylabel('R2 Score')
        ax.set_title('Surrogate Model R2 Scores')
        ax.grid(True)
        
        # 7. KL Divergence
        if any(self.update_metrics['kl_divergence']):
            ax = axes[2, 0]
            ax.plot(self.update_metrics['kl_divergence'], 'cyan')
            ax.set_xlabel('Update Step')
            ax.set_ylabel('KL Divergence')
            ax.set_title('Policy Change (KL)')
            ax.grid(True)
        
        # 8. Exploration rate
        ax = axes[2, 1]
        ax.plot(self.metrics['round'], self.metrics['exploration_rate'], 'brown', linewidth=2)
        ax.set_xlabel('Round')
        ax.set_ylabel('Exploration Rate')
        ax.set_title('Exploration Schedule')
        ax.grid(True)
        
        # 9. Reward statistics
        ax = axes[2, 2]
        if self.metrics['oracle_std_reward']:
            ax.plot(self.metrics['round'], self.metrics['oracle_std_reward'], 'green', linewidth=2)
            ax.set_xlabel('Round')
            ax.set_ylabel('Reward Std Dev')
            ax.set_title('Reward Variance')
            ax.grid(True)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Learning curves saved to {save_path}")
        else:
            plt.show()
    

    """
    Save all metrics to JSON file.
    """
    def save_metrics(self, filepath: str):
        
        with open(filepath, 'w') as f:
            json.dump({
                'round_metrics': self.metrics,
                'update_metrics': self.update_metrics
            }, f, indent=2)
        print(f"Metrics saved to {filepath}")
    

    """
    Get summary statistics of training.
    """
    def get_summary_stats(self) -> Dict:
        
        if not self.metrics['round']:
            return {}
        
        return {
            'total_rounds': len(self.metrics['round']),
            'final_mean_reward': self.metrics['oracle_mean_reward'][-1],
            'best_mean_reward': max(self.metrics['oracle_mean_reward']),
            'best_max_reward': max(self.metrics['oracle_max_reward']),
            'initial_lr': self.metrics['learning_rate'][0],
            'final_lr': self.metrics['learning_rate'][-1],
            'total_updates': len(self.update_metrics['update_idx']),
            'final_diversity': self.metrics['sequence_diversity'][-1] if self.metrics['sequence_diversity'] else 0,
            'convergence_round': self._find_convergence_round()
        }
    
    """
    Find round where learning converged (reward change < threshold).
    """
    def _find_convergence_round(self, threshold: float = 0.01) -> Optional[int]:
        
        rewards = self.metrics['oracle_mean_reward']
        if len(rewards) < 3:
            return None
        
        for i in range(2, len(rewards)):
            recent_change = abs(rewards[i] - rewards[i-1]) / (abs(rewards[i-1]) + 1e-8)
            if recent_change < threshold:
                return self.metrics['round'][i]
        
        return None
    
    """
    Print training summary.
    """
    def print_summary(self):
        
        stats = self.get_summary_stats()
        
        print("\n" + "="*50)
        print("TRAINING SUMMARY")
        print("="*50)
        
        for key, value in stats.items():
            if isinstance(value, float):
                print(f"{key.replace('_', ' ').title()}: {value:.4f}")
            else:
                print(f"{key.replace('_', ' ').title()}: {value}")
        
        print("="*50)