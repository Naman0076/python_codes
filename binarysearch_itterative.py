import unittest
import logging
import configure_logging


logging.info("BInary search program")
def binary_search(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return -1


class TestBinarySearch(unittest.TestCase):

    def test_element_found(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search(arr, 5), 2)
        self.assertEqual(binary_search(arr, 9), 4)
        logging.info(f"Testing element found in the array: {arr}")

    def test_element_not_found(self):
        arr = [2, 4, 6, 8]
        self.assertEqual(binary_search(arr, 1), -1)
        self.assertEqual(binary_search(arr, 9), -1)
        logging.info(f"Testing element found in the array: {arr}")

    def test_empty_array(self):
        self.assertEqual(binary_search([], 3), -1)
        logging.info(f"Testing element found in the array: {self}")

    def test_single_element(self):
        self.assertEqual(binary_search([10], 10), 0)
        self.assertEqual(binary_search([10], 5), -1)
        logging.info(f"Testing element found in the array: {self}")

if __name__ == '__main__':
    unittest.main()