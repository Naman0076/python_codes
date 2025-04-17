import unittest

def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

class TestFactorialRecursive(unittest.TestCase):

    def test_factorial_zero(self):
        self.assertEqual(factorial_recursive(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial_recursive(1), 1)

    def test_factorial_small_number(self):
        self.assertEqual(factorial_recursive(4), 24)

if __name__ == '__main__':
    unittest.main()