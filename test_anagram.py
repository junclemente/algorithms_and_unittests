import unittest
from anagram import is_anagram


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
