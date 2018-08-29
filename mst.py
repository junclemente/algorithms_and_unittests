
class NodeQ3(object):
    """ Node class for Question 3."""
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False


class EdgeQ3(object):
    """ Edge class for Question 3."""
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class GraphQ3(object):
    """ Graph class for Question 3 provided by Udacity."""
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []

    def insert_node(self, new_node_val):
        new_node = NodeQ3(new_node_val)
        self.nodes.append(new_node)

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found is None:
            from_found = NodeQ3(node_from_val)
            self.nodes.append(from_found)
        if to_found is None:
            to_found = NodeQ3(node_to_val)
            self.nodes.append(to_found)
        new_edge = EdgeQ3(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        list_of_edges = []
        for edge in self.edges:
            list_of_edges.append((edge.value,
                                  edge.node_from.value,
                                  edge.node_to.value))
        return list_of_edges

    def get_adjacency_list(self):
        adj_list = {}
        for e in self.edges:
            if e.node_from.value in adj_list:
                adj_list[e.node_from.value].append((e.node_to.value, e.value))
            else:
                adj_list[e.node_from.value] = [(e.node_to.value, e.value)]
        return adj_list


class MinimumSpanningTree(GraphQ3):
    """ Subclass of GraphQ3."""

    def get_unique_edges(self, adjacency_list):
        """Returns a list of unique edges from adjacency list.

        Calls function is_undirected_graph to check for undirectedness. Creates
        a list from dict provided by is_undirected_graph.

        Efficiency: O(n log n)

        Parameters:
        -----------
        adjacency_list : dict

        Returns:
        --------
        unique_edges : list
            List of unique edges from graph G ordered by weight.

        None : NoneType
            Returned when provided graph G is not an undirected graph.
        """
        if len(adjacency_list) < 1:
            print "Please provide an undirected graph."
            return None
        unique_edges = []
        undirected_graph = self.is_undirected_graph(adjacency_list)
        if undirected_graph:
            for node_set in undirected_graph:
                new_edge = undirected_graph[node_set]
                unique_edges.append((new_edge[0], new_edge[1], new_edge[2]))
                unique_edges = sorted(unique_edges, key=lambda u:u[0])
            return unique_edges
        else:
            return None

    def is_undirected_graph(self, adjacency_list):
        """Checks if graph is undirectional.

        Compares weight of node1 to node2 and node2 to node1 to determine
        undirectedness.

        Efficiency: O(n)

        Parameters:
        -----------
        adjacency_list : dict

        Returns:
        --------
        boolean
            If graph is not undirected, False is returned

        edges_hash : dict
            A hash of all unique edges found in the Graph, ie: "A to B"
            and "B to A" stored as "A to B"
        """
        edges_hash = {}
        for key in adjacency_list:
            for node_to in adjacency_list[key]:
                node_pair = sorted([key, node_to[0]])
                node_set = node_pair[0] + node_pair[1]
                if node_set not in edges_hash:
                    edges_hash[node_set] = (node_to[1], node_pair[0],
                                            node_pair[1])
                else:
                    node_set_weight = edges_hash[node_set][0]
                    if node_set_weight != node_to[1]:
                        print "The graph provided is not an undirected graph."
                        return False
        return edges_hash

    def insert_undirected_edges(self, edge_list):
        """ Inserts undirected edges.

        It checks the current graph for cycles and removes the edge is a
        cycle is created.

        Efficiency: O(n)
        """
        for each in edge_list:
            self.insert_edge(each[0], each[1], each[2])
            self.insert_edge(each[0], each[2], each[1])
            if self.check_cycle(each[1]):
                self.remove_edge(each[0], each[1], each[2])
                self.remove_edge(each[0], each[2], each[1])

    def remove_edge(self, value, node_from, node_to):
        # find edge in self.edges
        edge = self.find_edge(value, node_from, node_to)
        # Find edge index and pop off of list
        self.edges.pop(self.edges.index(edge))

        # Find node_from node
        node = self.find_node(node_from)
        # Go through node's edges and find edge that corresponds to node_to
        for n_edge in node.edges:
            if n_edge.node_to.value == node_to:
                node.edges.pop(node.edges.index(n_edge))

    def find_edge(self, value, node_from, node_to):
        """
        Efficiency: O(n)
        """
        for edge in self.edges:
            if (edge.value == value
               and edge.node_from.value == node_from
               and edge.node_to.value == node_to):
                    return edge

    def find_node(self, start_node):
        """
        Efficiency: O(n)
        """
        for node in self.nodes:
            if node.value == start_node:
                return node

    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False

    def check_cycle(self, start_node):
        """
        Efficiency:O(|V| + |E|); Worst-case: O|V|
        """
        self._clear_visited()
        start_node = self.find_node(start_node)
        cycle_found = False
        return self.cycle_helper(cycle_found, start_node)

    def cycle_helper(self, cycle_found, start_node):
        start_node.visited = True
        edges_out = [e for e in start_node.edges
                     if e.node_to.value != start_node.value]
        for edge in edges_out:
            if edge.node_to.visited and edge.node_to.value != start_node.value:
                cycle_found = True
            if not edge.node_to.visited:
                self.cycle_helper(cycle_found, edge.node_to)
        return cycle_found


def find_mst(G):
    """
    Given a graph represented by an adjacency list, returns a minimum spanning
    tree within the graph.

    The function will determine if the graph provided is an undirected graph.
    If the function detects a non-undirected or empty graph, the function will
    stop and return an empty dict.
    The function will start by creating a ordered list of unique edges by edge.
    It will then begin adding an edge and testing for cycles. If a cycle is
    created, the edge will be removed from the graph.

    Efficiency:
        Getting unique edges: O(n)
        Creating MST: O(|V|+|E|), Worst-case: O(|V|)

    Parameters:
    -----------
    g : dict
        An adjacency list representing an undirected graph structured as the
        following:
            {'A': [('B', 2), ('C', 8)],
             'B': [('A', 2), ('C', 5)],
             'C': [('A', 8), ('B', 5)]}

    Returns:
    --------
    mst : dict
        An empty dict or an adjacency list representing a minimum spanning tree
        structured as follows:
            {'A': [('B', 2)],
             'B': [('A', 2), ('C', 5)],
             'C': [('B', 5)]}
    """

    mst = MinimumSpanningTree()
    ordered_edge_list = mst.get_unique_edges(G)
    if ordered_edge_list:
        mst.insert_undirected_edges(ordered_edge_list)
        return mst.get_adjacency_list()
    else:
        return {}
