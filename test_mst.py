import unittest
from mst import find_mst


class MinSpanningTreeTestCase(unittest.TestCase):

    def test_small_undirected_graph(self):
        small_undirected_graph = {'A': [('B', 2), ('C', 8)],
                                  'B': [('A', 2), ('C', 5)],
                                  'C': [('A', 8), ('B', 5)]}
        result = {'A': [('B', 2)],
                  'C': [('B', 5)],
                  'B': [('A', 2), ('C', 5)]}
        self.assertEqual(find_mst(small_undirected_graph), result)

    def test_large_undirected_graph(self):
        large_undirected_graph = {'A': [('B', 3), ('F', 4), ('G', 2)],
                                  'B': [('A', 3), ('C', 6), ('D', 4)],
                                  'C': [('B', 6), ('D', 8), ('E', 3),
                                        ('F', 1)],
                                  'D': [('B', 4), ('C', 8), ('E', 5)],
                                  'E': [('C', 3), ('D', 5), ('F', 2)],
                                  'F': [('A', 4), ('C', 1), ('E', 2)],
                                  'G': [('A', 2)]}
        result = {'A': [('G', 2), ('B', 3), ('F', 4)],
                  'C': [('F', 1)],
                  'B': [('A', 3), ('D', 4)],
                  'E': [('F', 2)],
                  'D': [('B', 4)],
                  'G': [('A', 2)],
                  'F': [('C', 1), ('E', 2), ('A', 4)]}
        self.assertEqual(find_mst(large_undirected_graph), result)

    def test_directed_graph_result_is_empty(self):
        directed_graph = {'A': [('B', 1), ('C', 8)],
                          'B': [('A', 3), ('C', 4)],
                          'C': [('A', 5), ('B', 4)]}
        self.assertEqual(find_mst(directed_graph), {})

    def test_empty_graph(self):
        empty_graph = {}
        self.assertEqual(find_mst(empty_graph), {})


if __name__ == '__main__':
    unittest.main()
