import unittest
from core import Base15Number

class TestCore(unittest.TestCase):
    def test_addition(self):
        a = Base15Number([1.0, 0.5])
        b = Base15Number([0.5, 0.25])
        c = a + b
        result = c.to_float()
        expected = a.to_float() + b.to_float()
        self.assertAlmostEqual(result, expected, places=5)

    def test_normalization(self):
        a = Base15Number([2.0])
        a.normalize()
        self.assertTrue(all(0 <= d < 1.5 for d in a.digits), "Digits not normalized")

if __name__ == "__main__":
    unittest.main()
