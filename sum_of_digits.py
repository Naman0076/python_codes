import unittest

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

class TestSumOfDigits(unittest.TestCase):

    def test_sum_true(self):
        self.assertEqual(sum_of_digits(5), 5)
    def test_sum_false(self):
        self.assertNotEqual(sum_of_digits(5),2)

if __name__ == '__main__':
    unittest.main()