import unittest


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

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

from bubblesort import bubble_sort, binary_search  

class TestSearchAndSort(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([4, 2, 5, 1]), [1, 2, 4, 5])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([3, 3, 2]), [2, 3, 3])

    def test_binary_search_found(self):
        arr = [1, 2, 4, 5, 7]
        self.assertEqual(binary_search(arr, 4), 2)
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search(arr, 7), 4)

    def test_binary_search_not_found(self):
        arr = [1, 3, 5, 7]
        self.assertEqual(binary_search(arr, 6), -1)
        self.assertEqual(binary_search(arr, 10), -1)

    def test_binary_search_empty_array(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_binary_search_single_element(self):
        self.assertEqual(binary_search([2], 2), 0)
        self.assertEqual(binary_search([2], 3), -1)

if __name__ == '__main__':
    unittest.main()
