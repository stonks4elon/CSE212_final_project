"""
CSE212
(c) BYU-Idaho
09-Prove - Problems

It is a violation of BYU-Idaho Honor Code to post or share this code with others or
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""


class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node
    class below is an inner class.  An inner class means that its real
    name is related to the outer class.  To create a Node object, we will
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the
        left and right sub-tree.
        """

        def __init__(self, data):
            """
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """

            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        elif data > node.data:
            # The data belongs on the right side.
            if node.right is None:
                # Code here
                pass

            else:
                # Code here
                pass

    def __contains__(self, data):
        """
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        """
        This function will search for a node that contains
        'data'.  The current sub-tree being search is
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        if node is None:
            return False
        elif data == node.data:
            return True
        else:
            if data < node.data:
                return self._contains(data, node.left)
            else:
                return self._contains(data, node.right)

    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root

    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will
        provide the data in the current node, and finally we will
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    def __reversed__(self):
        """
        Perform a formward traversal (in order traversal) starting from
        the root of the BST.  This function is called when a the
        reversed function is called and is frequently used with a for
        loop.

        for value in reversed(my_bst):
            print(value)

        """
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):
        """
        Does a backwards traversal (reverse in-order traversal) through the
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the right
        side (thus getting the larger numbers first), then we will
        provide the data in the current node, and finally we will
        traverse on the left side (thus getting the smaller numbers last).

        This function is intended to be called the first time by
        the __reversed__ function.
        """
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    def get_height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.

        If the tree is empty, then return 0.  Otherwise, call
        _get_height on the root which will recursively determine the
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    def _get_height(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree
        (represented by 'node') is 1 plus the height of either the
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by
        get_height.
        """
        # Base case if node is a leaf.
        if node is None:
            return 0
        else:
            # Find the max height of left and right subtrees.
            left = 1 + self._get_height(node.left)
            right = 1 + self._get_height(node.right)
            if left > right:
                return left
            else:
                return right


# Note: The following function is not part of the above class. It stands alone only for the recursion problem.
def compute_factorial(number):
    pass


# TODO: PROBLEM #1 Implement the compute_factorial function. Don't forget to define the needed base case(s).
print('__Problem 1 Test Cases__')
print(compute_factorial(5))   # 120
print(compute_factorial(10))  # 3628800
print(compute_factorial(7))   # 5040

# TODO: PROBLEM #2 look at the insert and _insert functions and finish the code to be able to correctly implement
#  inserting data into a binary tree
print("\n__Problem 2 Test Cases__")
tree = BST()
tree.insert(40)
tree.insert(34)
tree.insert(108)
tree.insert(12)
tree.insert(3)
tree.insert(65)
tree.insert(15)
tree.insert(76)

# Displays the tree.
for x in tree:
    print(x)    # 3, 12, 15, 34, 40, 65, 76, 108
