"""
losses.py
NeuroFraction-of-1.5

Implements common loss functions for base-1.5 neural networks.
"""

from core import Base15Number

class MSELoss:
    """
    Mean Squared Error Loss.
    """
    def __call__(self, prediction: Base15Number, target: float) -> Base15Number:
        """
        Computes the mean squared error between a prediction and the target value.
        """
        target_base15 = Base15Number.from_float(target)
        error = prediction - target_base15
        return (error * error) * Base15Number.from_float(0.5)
