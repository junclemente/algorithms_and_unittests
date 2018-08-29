class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def get_value_from_end(self, position_from_end):
        """
        Creates a list of values from the LinkedList.

        Efficiency: O(n)

        Parameters
        ----------
        position_from_end : int

        Returns
        -------
        int
            Value of node mth from the end

        None
            None is returned if position_from_end is larger than
            LinkedList, 0, or negative.
        """
        node_list = []
        current = self.head
        while current:
            node_list.append(current.data)
            current = current.next
        if position_from_end > 0 and position_from_end <= len(node_list):
            index = (len(node_list)) - position_from_end
        # print "{} = {} - {}".format(index, len(node_list), position)
            return node_list[index]
        else:
            print("Error: {} is larger than the length of "
                  "the list.".format(position_from_end))
            return None


def make_linked_list(list_of_nodes):
    """ Creates a linked list from a provided list of node values.

    Efficiency: O(n)

    Parameters
    ----------
    list_of_nodes : list

    Returns
    -------
    linked_list
        Returns instance of Class LinkedList
    """
    linked_list = LinkedList()
    for n in list_of_nodes:
        node = Node(n)
        linked_list.append(node)

    return linked_list


def linked_list(ll, m):
    """ Returns mth value from the end of a linked list.

    Efficiency: O(n)

    Parameters
    ----------
    ll : linked list

    m : int
        Positive integer that represents mth number from end of linked list.

    Returns
    -------
    int
        Returns the value of the node that is mth from the end.
    None
        - Returned if m is larger than length of linked list.
        - Linked List is not provided.
    """
    if not isinstance(ll, LinkedList):
        print "A Linked List was not provided."
        return None
    if m < 0:
        print "Please provide a integer larger than 0."
        return None

    return ll.get_value_from_end(m)


