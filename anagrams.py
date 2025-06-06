import unittest
import logging

def char_count(string):
    char_count = {}
    for char in string.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def anagrams(str1, str2):
    logging.info("Str 1 is", str1=str1)
    logging.info("Str 2 is", str2=str2)
    return char_count(str1) == char_count(str2)

class TestAnagramFunction(unittest.TestCase):

    def test_valid_anagrams(self):
        self.assertTrue(anagrams("Naman", "Manan"))
        self.assertTrue(anagrams("Race", "Care"))
        self.assertFalse(anagrams("sea", "ace"))

if __name__ == '__main__':
    unittest.main()
