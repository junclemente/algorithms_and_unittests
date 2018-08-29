
class NodeQ4(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BinaryTreeQ4(object):
    def __init__(self, root = None):
        self.root = NodeQ4(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root, "")[:-1]

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start:
            if start.value == find_val:
                return True
            else:
                return (self.preorder_search(start.left, find_val)
                        or self.preorder_search(start.right, find_val))
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


class LCA(BinaryTreeQ4):
    """ Subclass of BinaryTreeQ4.

    """

    def __init__(self):
        self.nodes = {}

    def get_node(self, node_value):
        """
        Returns node from self.nodes list or creates the node if it doesn't
        exist.
        """
        if node_value in self.nodes:
            # print("Retrieving Node {} in nodes".format(self.nodes[node_value].value))
            return self.nodes[node_value]
        else:
            node = NodeQ4(node_value)
            # print "Adding Node {} to nodes.".format(node.value)
            self.nodes[node_value] = node
            return node

    def check_node(self, node_value):
        """
        Returns node if found in Binary Tree.

        Efficiency: O(log n)
        """
        if self.search(node_value):
            return self.nodes[node_value]
        else:
            return False

    def create_tree(self, matrix, root_value):
        """
        Creates binary tree from matrix.
        If the root_value equals the final node value created, then the
        creation of the binary tree is successful.

        Efficiency: O(n)
        """
        if not matrix:
            print "Please provide a matrix."
            return None
        if root_value < 0:
            print "Please provide a non-negative root value."
            return None

        node_matrix_list = []
        # Create a list of tuples, ordered by sum of each object in matrix list
        for row in range(len(matrix)):
            node_matrix_list.append((row, matrix[row], sum(matrix[row])))
        node_matrix_list = sorted(node_matrix_list, key=lambda r : r[2])

        # Build binary tree from leaf to root
        for n in node_matrix_list:
            # n[0]: Node value; n[1]: Node children list; n[2]: sum of n[1]
            # Find nodes with children
            if n[2] > 0:
                # Get/create node
                node = self.get_node(n[0])
                for c in range(len(n[1])):
                    if n[1][c] >= 1:
                        # Get/create child node
                        child_node = self.get_node(c)
                        # Add orphans to parent node
                        if not child_node.parent:
                            if not node.left:
                                # print ("Assigning child {} to parent {} left".format(child_node.value, node.value)
                                node.left = child_node
                                child_node.parent = node
                            elif not node.right:
                                # print "Assigning child {} to parent {} right".format(child_node.value, node.value)
                                node.right = child_node
                                child_node.parent = node
                            else:
                                return False

        # Final node should equal root_value.
        if node.value == root_value:
            self.root = node
        else:
            # print "root doesn't match"
            self.root = None
        # self.root = node

    def node_to_root_list(self, node_value):
        """
        Creates a list, starting with node_value to root

        Efficiency: O(n)
        """
        node = self.check_node(node_value)
        if node:
            traversal_list = []
            count = 0
            # While loop should not reiterate more than total number of nodes.
            while node.value != self.root.value and count <= len(self.nodes):
                traversal_list.append(node.value)
                node = node.parent
                count += 1
            traversal_list.append(self.root.value)
            return traversal_list
        else:
            print "Error: Node {} does not exist.".format(node_value)
            return False

    def get_least_common_ancestor(self, node1_list, node2_list):
        """
        Returns lowest common ancestor
        """
        # Iterate through shortest list.
        if len(node1_list) < len(node2_list):
            list_1 = node1_list
            list_2 = node2_list
        else:
            list_1 = node2_list
            list_2 = node1_list
        for i in list_1:
            if i in list_2:
                return i


def find_lca(T, r, n1, n2):
    """ Returns Least Common Ancestor (LCA).

    An ancestry matrix is converted to a binary tree. If the binary tree root
    does not equal the root value entered, an error is thrown.

    Efficiency:

    Parameters:
    -----------
    T : list of list
        The ancestry matrix that is used to create the binary tree
    r : int
        A non-negative integer
    n1, n2 : int
        Value of nodes to find the LCA.

    Returns:
    --------
    int
        Least common ancestor for n1, n2 is returned

    None
        Message to console is also printed depending on the error.
            - There was an error creating the binary tree
            - n1 or n2 do not exist in the binary tree
            - Matrix not provided
            - Root is negative
    """
    tree = LCA()
    tree.create_tree(T, r)
    try:
        if tree.check_node(r) and tree.root.value == r:
            node1 = tree.node_to_root_list(n1)
            node2 = tree.node_to_root_list(n2)
            if node1 and node2:
                return tree.get_least_common_ancestor(node1, node2)
            else:
                print "A least common ancestor could not be found."
                return None
        else:
            print "Error: Root node does not match ancestry matrix."
            return None
    except AttributeError:
        print("There has been an error creating the matrix.")
        return None


