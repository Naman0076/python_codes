import unittest

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

class FactorialOfNumber(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial_iterative(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial_iterative(1), 1)
    
    def test_factorial_positive(self):
        self.assertEqual(factorial_iterative(5), 120)
        self.assertEqual(factorial_iterative(7), 5040)

if __name__ == '__main__':
    unittest.main()