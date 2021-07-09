"""
CSE212
(c) BYU-Idaho
07-Prove - Problems

It is a violation of BYU-Idaho Honor Code to post or share this code with others or
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""


class LinkedList:
    """
    Implement the LinkedList data structure.  The Node class below is an
    inner class.  An inner class means that its real name is related to
    the outer class.  To create a Node object, we will need to
    specify LinkedList.Node
    """

    class Node:
        """
        Each node of the linked list will have data and links to the
        previous and next node.
        """

        def __init__(self, data):
            """
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None

    def insert_head(self, value):
        """
        Insert a new node at the front (i.e. the head) of the
        linked list.
        """
        # Create the new node
        new_node = LinkedList.Node(value)

        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head  # Connect new node to the previous head
            self.head.prev = new_node  # Connect the previous head to the new node
            self.head = new_node  # Update the head to point to the new node

    def insert_tail(self, value):
        """
        Insert a new node at the back (i.e. the tail) of the
        linked list.
        """
        # Create a new node
        new_tail = LinkedList.Node(value)
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.tail is None:
            self.head = new_tail  # If the list is empty, then point both head and tail
            self.tail = new_tail  # to the new node.

            # If the list is not empty, then only self.tail will be
            # affected.
        else:
            new_tail.prev = self.tail  # Connect new node to the previous tail
            self.tail.next = new_tail  # Connect the previous tail to the new node
            self.tail = new_tail  # Update the tail to point to the new node

    def remove_head(self):
        """
        Remove the first node (i.e. the head) of the linked list.
        """
        # If the list has only one item in it, then set head and tail
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node

    def remove_tail(self):
        """
        Remove the last node (i.e. the tail) of the linked list.
        """
        # If there is only one item in linked list
        # set both head and tail to None
        if self.tail == self.head:
            self.head = None
            self.tail = None
        # If there is more than one item in the list
        # remove the last item
        elif self.tail is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def insert_after(self, value, new_value):
        """
        Insert 'new_value' after the first occurrence of 'value' in
        the linked list.
        """
        # Search for the node that matches 'value' by starting at the
        # head of the list.
        curr = self.head
        while curr is not None:
            if curr.data == value:
                # If the location of 'value' is at the end of the list,
                # then we can call insert_tail to add 'new_value'
                if curr == self.tail:
                    self.insert_tail(new_value)
                # For any other location of 'value', need to create a
                # new node and reconnect the links to insert.
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr  # Connect new node to the node containing 'value'
                    new_node.next = curr.next  # Connect new node to the node after 'value'
                    curr.next.prev = new_node  # Connect node after 'value' to the new node
                    curr.next = new_node  # Connect the node containing 'value' to the new node
                return  # We can exit the function after we insert
            curr = curr.next  # Go to the next node to search for 'value'

    def remove(self, value):
        """
        Remove the first node that contains 'value'.
        """
        # Search for the node that matches 'value' by starting at the
        # head of the list.
        curr = self.head
        while curr is not None:
            if curr.data == value:
                # If the value is contained in the head of the list, call the remove head function
                if curr == self.head:
                    self.remove_head()
                # If the value is contained in the tail of the list, call the remove tail function
                elif curr == self.tail:
                    self.remove_tail()
                # If the value is contained anywhere in the middle of the list, remove any pointers to it
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                # Once replaced, exit the function
                return
            curr = curr.next

    def replace(self, old_value, new_value):
        """
        Search for all instances of 'old_value' and replace the value
        to 'new_value'.
        """
        # Search for the node that matches 'value' by starting at the
        # head of the list.
        curr = self.head
        while curr is not None:
            # Once value is found, replace the old_value to the new_value
            if curr.data == old_value:
                curr.data = new_value
            # Makes sure to go through the entire list and replace all old_values
            curr = curr.next

    def __iter__(self):
        """
        Iterate forward through the Linked List
        """
        curr = self.head  # Start at the beginning since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next  # Go forward in the linked list

    def __reversed__(self):
        """
        Iterate backward through the Linked List
        """
        curr = self.tail  # Start at the end since this is a reverse iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.prev  # Go backward in the linked list

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output


# Sample Test Cases
ll = LinkedList()
# TODO: PROBLEM 1: We are wanting to create a linked list of the alphabet. For problem one, fix the code to implement
# TODO: the head and tail of the linked list.

ll.insert_tail('D')
ll.insert_head('C')
print(ll)  # [C, D]
ll.insert_head(5)
ll.insert_tail('f')
ll.insert_head('B')
ll.insert_tail('X')
print(ll)  # [B, 5, C, D, f, X]

# TODO: PROBLEM 2: The linked list is in alphabetical order at the moment except the 5 that made its way in the list.
# TODO: Fix the 'remove' function so that you can remove the 5 from the list.
ll.remove(5)
ll.replace('f', 'F')
ll.insert_head('A')
ll.insert_tail('Z')
print(ll)  # [A, B, C, D, F, X, Z]

#  TODO: PROBLEM 3: Implement the 'insert after' function to add the rest of the alphabet to the list so that the list
#  TODO: is in alphabetical order.

ll.insert_after('D', 'E')
ll.insert_after('F', 'I')
ll.insert_after('F', 'G')
ll.insert_after('G', 'H')
ll.insert_after('I', 'J')
ll.insert_after('J', 'K')
ll.insert_after('K', 'P')
ll.insert_after('K', 'O')
ll.insert_after('K', 'N')
ll.insert_after('K', 'L')
ll.insert_after('L', 'M')
ll.insert_after('X', 'Y')
print(ll)  # [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, X, Y, Z]
ll.insert_after('P', 'Q')
ll.insert_after('Q', 'R')
ll.insert_after('R', 'S')
ll.insert_tail('Next time won\'t you sing with me')
ll.insert_after('S', 'T')
ll.insert_after('T', 'U')
ll.insert_after('U', 'W')
ll.insert_after('U', 'V')
print(ll)  # [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z,
# Next time won't you sing with me]
