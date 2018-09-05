import unittest
from anagram import is_anagram

"""
Question 1: Determine if t is an anagram of s.

The function needs to check if string "s" has enough letters to create
string "t". There were no parameters provided other than t and s are strings.
Therefore I made an assumption that only string characters that are part of the
American alphabet will be used. I also made the assumption that case does not
matter.

Two hashes were created, one for each "t" and "s" string because searching
through through hashes are done in real time O(1). Creating the hash takes O(n)
though since it has to iterate through all values of the string.

UPDATE: Based on the reviewer's comments, I updated the function to ensure that
the word "t" does not exist in the word "s", even though the project description
does not specify that "uda" in "udacity" should return False. Based on the
definition of an anagram, that should return True.
"""


class AnagramTestCase(unittest.TestCase):

    def test_case_does_not_matter(self):
        self.assertTrue(is_anagram('udacity', 'AD'))

    def test_anagram_is_true(self):
        self.assertTrue(is_anagram('udacity', 'uy'))

    def test_anagram_is_false(self):
        self.assertFalse(is_anagram('supercalifragilisticexpialidocious',
                                    'exhale'))

    def test_entry_has_more_letters_is_false(self):
        self.assertFalse(is_anagram('edge', 'edges'))

    def test_no_entry_is_false(self):
        self.assertFalse(is_anagram('', ''))

    def test_adjacent_letters_is_false(self):
        self.assertFalse(is_anagram('hello', 'll'))


if __name__ == '__main__':
    unittest.main()
