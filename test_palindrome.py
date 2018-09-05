import unittest
from palindrome import find_palindrome

"""
Question 2: Find the longest palindromic substring in a string.

First, I made an assumption that a word has to be at least 3 characters long.
This can be adjusted by changing the value of the static variable:
MIN_PALINDROME_LENGTH. Another assumption is that spaces do not matter so all
spaces are removed before processing.

I started by creating a hash of all characters in the given string and create
a list of their indices. I iterate through the hash and compare words larger
than the last recorded palindrome.

Creating the hash is done in linear time O(n) but checking for palindromes
takes O(n^2).
"""


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
