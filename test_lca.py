import unittest
from lca import find_lca

BAD_MATRIX = [[0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 0, 0, 0, 0, 1, 1],
              [0, 0, 0, 0, 0, 1, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0]]

GOOD_MATRIX = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]


class LeastCommonAncestorTestCase(unittest.TestCase):

    def test_bad_matrix_returns_none(self):
        root = 4
        n1 = 0
        n2 = 3
        self.assertIsNone(find_lca(BAD_MATRIX, root, n1, n2))

    def test_given_root_is_wrong_returns_none(self):
        wrong_root = 8
        n1 = 10
        n2 = 5
        self.assertIsNone(find_lca(GOOD_MATRIX, wrong_root, n1, n2))

    def test_nonexistent_node_returns_none(self):
        root = 6
        bad_node = 12
        node = 2
        self.assertIsNone(find_lca(GOOD_MATRIX, root, bad_node, node))

    def test_lca_is_root(self):
        root = 6
        n1, n2 = 9, 10
        self.assertEqual(find_lca(GOOD_MATRIX, root, n1, n2), root)

    def test_empty_matrix_returns_none(self):
        empty_matrix = []
        root = 6
        n1, n2 = 9, 10
        self.assertIsNone(find_lca(empty_matrix, root, n1, n2))

    def test_negative_root_value_returns_none(self):
        negative_root = -1
        n1, n2, = 9, 10
        self.assertIsNone(find_lca(GOOD_MATRIX, negative_root, n1, n2))


if __name__ == '__main__':
    unittest.main()
