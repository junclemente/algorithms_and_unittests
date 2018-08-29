import unittest
from linked_lists import make_linked_list
from linked_lists import linked_list

NODE_LIST1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
NODE_LIST2 = [4, 20, 7, 3, 5, 9]

ll1 = make_linked_list(NODE_LIST1)
ll2 = make_linked_list(NODE_LIST2)


class LinkedListTestCase(unittest.TestCase):

    def test_return_last_number(self):
        self.assertEqual(linked_list(ll1, 1), NODE_LIST1[-1])

    def test_return_first_number(self):
        self.assertEqual(linked_list(ll1, 10), NODE_LIST1[0])

    def test_no_linked_list_returns_none(self):
        self.assertIsNone(linked_list(NODE_LIST1, 1))

    def test_position_is_longer_than_list_length(self):
        self.assertIsNone(linked_list(ll2, 7))


if __name__ == '__main__':
    unittest.main()
