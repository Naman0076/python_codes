import unittest

def find_equilibrium_indices(arr):
    total_sum = sum(arr)
    left_sum = 0
    equilibrium_indices = []

    for i, num in enumerate(arr):
        total_sum -= num
        if left_sum == total_sum:
            equilibrium_indices.append(i)
        left_sum += num

    return equilibrium_indices

class TestFindEquilibriumIndices(unittest.TestCase):

    def test_single_equilibrium(self):
        self.assertEqual(find_equilibrium_indices([1, 3, 5, 2, 2]), [2])

    def test_multiple_equilibriums(self):
        self.assertEqual(find_equilibrium_indices([0, -3, 5, -4, -2, 3, 1, 0]), [0, 3, 7])

    def test_no_equilibrium(self):
        self.assertEqual(find_equilibrium_indices([1, 2, 3]), [])

if __name__ == '__main__':
    unittest.main()