
"""
core.py
"""

from typing import List, Optional

class Base15Number:
    """
    Base-1.5 number system implementation.
    Supports normalization, addition, subtraction, multiplication, and conversion.
    """

    def __init__(self, digits: List[float]):
        self.digits = digits
        self.normalize()

    def normalize(self) -> None:
        """Normalize digits with carry propagation and handle negatives."""
        carry = 0.0
        for i in reversed(range(len(self.digits))):
            self.digits[i] += carry
            carry = int(self.digits[i] // 1.5)
            self.digits[i] %= 1.5
            if self.digits[i] < 0:
                self.digits[i] += 1.5
                carry -= 1

        while carry != 0:
            self.digits.insert(0, carry % 1.5)
            carry = int(carry // 1.5)

        while len(self.digits) > 1 and self.digits[0] == 0:
            self.digits.pop(0)

    def to_float(self) -> float:
        """Convert to decimal (float) representation."""
        return sum(d * (1.5 ** i) for i, d in enumerate(reversed(self.digits)))

    @classmethod
    def from_float(cls, x: float, precision: int = 8) -> 'Base15Number':
        """Convert a float to a Base-1.5 number with given precision."""
        if x == 0:
            return cls([0])
        digits = []
        remaining = abs(x)
        for _ in range(precision):
            digits.append(int(remaining % 1.5))
            remaining = int(remaining // 1.5)
            if remaining == 0:
                break
        if x < 0:
            digits = [-d for d in digits]
        return cls(list(reversed(digits)))

    def __add__(self, other: 'Base15Number') -> 'Base15Number':
        """Addition of two Base-1.5 numbers."""
        max_len = max(len(self.digits), len(other.digits))
        a = self.digits + [0] * (max_len - len(self.digits))
        b = other.digits + [0] * (max_len - len(other.digits))
        result = Base15Number([x + y for x, y in zip(a, b)])
        return result

    def __sub__(self, other: 'Base15Number') -> 'Base15Number':
        """Subtraction of two Base-1.5 numbers."""
        neg_other = Base15Number([-d for d in other.digits])
        return self + neg_other

    def __mul__(self, other: 'Base15Number') -> 'Base15Number':
        """Multiplication of two Base-1.5 numbers."""
        result = [0.0] * (len(self.digits) + len(other.digits))
        for i, d1 in enumerate(reversed(self.digits)):
            for j, d2 in enumerate(reversed(other.digits)):
                result[-(i + j + 1)] += d1 * d2
        return Base15Number(result)

    def __repr__(self) -> str:
        return f"Base15Number({self.digits}) ~ {self.to_float():.4f}"
