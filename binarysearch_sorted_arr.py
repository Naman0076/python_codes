import unittest


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

class TestBinarySearch(unittest.TestCase):

    def test_found_element(self):
        arr = [1, 2, 3, 4, 5]
        x = 3
        self.assertEqual(binary_search(arr, 0, len(arr)-1, x), 2)

    def test_element_not_found(self):
        arr = [10, 20, 30, 40]
        x = 25
        self.assertEqual(binary_search(arr, 0, len(arr)-1, x), -1)

    def test_first_element(self):
        arr = [5, 10, 15, 20]
        x = 5
        self.assertEqual(binary_search(arr, 0, len(arr)-1, x), 0)

    def test_last_element(self):
        arr = [5, 10, 15, 20]
        x = 20
        self.assertEqual(binary_search(arr, 0, len(arr)-1, x), 3)

    def test_single_element_array(self):
        arr = [7]
        x = 7
        self.assertEqual(binary_search(arr, 0, 0, x), 0)

    def test_empty_array(self):
        arr = []
        x = 1
        self.assertEqual(binary_search(arr, 0, len(arr)-1, x), -1)

if __name__ == '__main__':
    unittest.main()
