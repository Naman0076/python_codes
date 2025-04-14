import unittest


def calculate(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
    else:
        return "Invalid operator!"

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(5, '+', 3), 8)

    def test_subtraction(self):
        self.assertEqual(calculate(10, '-', 4), 6)

    def test_multiplication(self):
        self.assertEqual(calculate(7, '*', 6), 42)

    def test_division(self):
        self.assertEqual(calculate(20, '/', 4), 5.0)

    def test_division_by_zero(self):
        self.assertEqual(calculate(10, '/', 0), "Error! Division by zero.")

    def test_invalid_operator(self):
        self.assertEqual(calculate(2, '%', 3), "Invalid operator!")
if __name__ == '__main__':
    unittest.main()
