import unittest

def left(arr, start, end, x):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            if mid == 0 or arr[mid - 1] != x:  
                return mid
            end = mid - 1
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def right(arr, start, end, x):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            if mid == end or arr[mid + 1] != x: 
                return mid
            start = mid + 1
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def first_and_last_index(arr, x):
    l = left(arr, 0, len(arr) - 1, x)
    r = right(arr, 0, len(arr) - 1, x)
    return (l, r)

class TestFirstAndLastIndex(unittest.TestCase):

    def test_found_middle(self):
        arr = [1, 2, 2, 2, 3, 4, 5]
        self.assertEqual(first_and_last_index(arr, 2), (1, 3))

    def test_found_edges(self):
        arr = [7, 7, 7, 8, 9]
        self.assertEqual(first_and_last_index(arr, 7), (0, 2))

    def test_single_occurrence(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(first_and_last_index(arr, 4), (3, 3))

if __name__ == "__main__":
    unittest.main()