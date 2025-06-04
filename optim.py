"""
optim.py
NeuroFraction-of-1.5

Implements basic optimizers for base-1.5 neural networks.
"""

from core import Base15Number

class Base15SGD:
    """
    Stochastic Gradient Descent (SGD) optimizer for Base-1.5 numbers.
    """
    def __init__(self, params, lr=0.1):
        self.params = [p for p in params if p.requires_grad]
        self.lr = Base15Number.from_float(lr)

    def step(self):
        """
        Updates all parameters using their gradients.
        """
        for param in self.params:
            if param.gradient is not None:
                param += (param.gradient.value * -self.lr)

    def zero_grad(self):
        """
        Resets all gradients to zero.
        """
        for param in self.params:
            if param.gradient is not None:
                param.gradient.value = Base15Number([0.0])
