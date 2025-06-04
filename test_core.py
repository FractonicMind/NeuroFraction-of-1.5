
# tests/test_core.py

import unittest
from core import Base15Number

class TestBase15Number(unittest.TestCase):
    def test_addition(self):
        a = Base15Number([1, 0.5])
        b = Base15Number([0.5, 1])
        result = a + b
        self.assertAlmostEqual(result.to_float(), a.to_float() + b.to_float(), places=5)

    def test_subtraction(self):
        a = Base15Number([1, 0.5])
        b = Base15Number([0.5, 1])
        result = a - b
        self.assertAlmostEqual(result.to_float(), a.to_float() - b.to_float(), places=5)

    def test_multiplication(self):
        a = Base15Number([1])
        b = Base15Number([0.5])
        result = a * b
        self.assertAlmostEqual(result.to_float(), a.to_float() * b.to_float(), places=5)
