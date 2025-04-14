import unittest

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False


class TestIsPalindrome(unittest.TestCase):

    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("madam"))

    def test_mixed_case_palindrome(self):
        self.assertTrue(is_palindrome("RaceCar".lower()))

    def test_not_a_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_even_length_palindrome(self):
        self.assertTrue(is_palindrome("noon"))

    def test_special_characters(self):
        self.assertFalse(is_palindrome("A man, a plan, a canal, Panama"))  # without cleanup

if __name__ == '__main__': 
    unittest.main()