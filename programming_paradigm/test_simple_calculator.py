import unittest

from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calculator.add(2, 6), 8)
        self.assertEqual(self.calculator.add(0, 0), 0)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-5, -3), -8)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)
        self.assertEqual(self.calculator.subtract(0, 0), 0)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
        self.assertEqual(self.calculator.subtract(-5, -3), -2)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(4, 2), 8)
        self.assertEqual(self.calculator.multiply(0, 5), 0)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)
        self.assertEqual(self.calculator.multiply(-3, -3), 9)

    def test_division(self):
        self.assertEqual(self.calculator.divide(8, 2), 4)
        self.assertEqual(self.calculator.divide(-6, 2), -3)
        self.assertEqual(self.calculator.divide(-9, -3), 3)
        self.assertIsNone(self.calculator.divide(5, 0))

