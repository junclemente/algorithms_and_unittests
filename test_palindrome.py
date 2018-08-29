import unittest
from palindrome import find_palindrome


class PalindromeTestCase(unittest.TestCase):

    def test_palindrome_found(self):
        self.assertEqual(find_palindrome("tatoo"), "tat")

    def test_longest_palindrome_returned(self):
        self.assertEqual(find_palindrome("taco cat"), "tacocat")

    def test_word_is_too_short(self):
        self.assertIn("too short", find_palindrome("ab"))

    def test_no_palindromes_found(self):
        self.assertIn("no palindromes found", find_palindrome("a b c d e f g"))

    def test_palindrome_in_long_string(self):
        self.assertEqual(find_palindrome(
            "asdxczviouhewjkbndoxiuamanaplanacanalpanamabnadiouadskbnadsf"),
            "amanaplanacanalpanama")


if __name__ == '__main__':
    unittest.main()
