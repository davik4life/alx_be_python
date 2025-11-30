"""
    Practice Exercises
Exercise 1: Understanding the Importance of Testing

Instruction:

Write a small Python function (e.g., a function to calculate the square of a number) and intentionally introduce a bug (e.g., incorrect calculation logic).

Exercise 2: Writing Basic Unit Tests

Instruction:

Use the unittest module in Python to create a test case for the buggy function from Exercise 1.
Write test methods to check different scenarios (e.g., valid input, invalid input) and verify expected behavior.
"""

import unittest

def square(num):
    # Function to calculate the square of a number
    return num * num  # Intentional bug introduced

class TestSquareFunction(unittest.TestCase):
    def test_square_positive(self):
        self.assertEqual(square(3), 9)

    def test_square_negative(self):
        self.assertEqual(square(-4), 16)

    def test_square_zero(self):
        self.assertEqual(square(0), 0)

if __name__ == '__main__':
    unittest.main()

