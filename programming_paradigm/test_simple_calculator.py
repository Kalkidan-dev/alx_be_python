# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(6, 2), 8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6, 2), 4)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, 2), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertIsNone(self.calc.divide(6, 0))  # Test division by zero

if __name__ == '__main__':
    unittest.main()
