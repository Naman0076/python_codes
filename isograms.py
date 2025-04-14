import unittest

def char_count(word):
    count_dict = {}
    for char in word.lower():
        count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict

def isogram_check(str1, str2):
    char_count_1 = char_count(str1)
    char_count_2 = char_count(str2)

    values1 = sorted(char_count_1.values())
    values2 = sorted(char_count_2.values())

    return values1 == values2


class TestIsogramMatch(unittest.TestCase):

    def test_matching_frequencies(self):
        self.assertTrue(isogram_check("abcabc", "defdef"))
        self.assertFalse(isogram_check("aabbccd", "ddeefff")) #i habe intentionally included a false one 

if __name__ == '__main__':
    unittest.main()