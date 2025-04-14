import unittest

def count_characters(s):
    s = s.lower()
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    return count

def get_unique_characters(count):
    unique_char = {char: 1 for char in count if count[char] == 1}
    return unique_char


class TestCharacterCounting(unittest.TestCase):

    def test_count_characters(self):
        s = "aabbbaac"
        expected = {'a': 4, 'b': 3, 'c': 1}
        self.assertEqual(count_characters(s), expected)

    def test_get_unique_characters(self):
        count = {'a': 4, 'b': 3, 'c': 1}
        expected = {'c': 1}
        self.assertEqual(get_unique_characters(count), expected)

    def test_all_unique(self):
        s = "abc"
        count = count_characters(s)
        unique = get_unique_characters(count)
        expected = {'a': 1, 'b': 1, 'c': 1}
        self.assertEqual(unique, expected)

    def test_no_unique(self):
        s = "aabbcc"
        count = count_characters(s)
        unique = get_unique_characters(count)
        expected = {}
        self.assertEqual(unique, expected)

if __name__ == '__main__':
    unittest.main()
