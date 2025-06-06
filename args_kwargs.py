import unittest
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def calculate(num1, op, num2):
    logging.info(f"Calculating: {num1} {op} {num2}")
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            logging.error("Division by zero error")
            return "Error! Division by zero."
        result = num1 / num2
    else:
        logging.error(f"Invalid operator: {op}")
        return "Invalid operator!"

    logging.info(f"Result: {result}")
    return result

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
