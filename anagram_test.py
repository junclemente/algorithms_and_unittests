import unittest
from anagram import is_anagram


class AnagramTestCase(unittest.TestCase):

    def test_case_does_not_matter(self):
        """ Is 'AD' an anagram of 'udacity' even if capitalized? """
        self.assertTrue(is_anagram('udacity', 'AD'))

    def test_anagram_is_true(self):
        """ Is 'uy' an anagram of 'udacity'? """
        self.assertTrue(is_anagram('udacity', 'uy'))

    def test_anagram_false(self):
        """ If it is not an anagram, it should return false. """
        self.assertFalse(is_anagram('supercalifragilisticexpialidocious',
                                    'exhale'))

    def test_entry_has_more_letters_is_false(self):
        """
        If the test word has more letters, it is not an anagram and return
        false.
        """
        self.assertFalse(is_anagram('edge', 'edges'))

    def test_no_entry_is_false(self):
        """ Blank entries should return false. """
        self.assertFalse(is_anagram('', ''))


if __name__ == '__main__':
    unittest.main()
