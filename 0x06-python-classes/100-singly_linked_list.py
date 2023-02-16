#!/usr/bin/python3
"""A class `Node` that defines a node of a singly linked list"""


class Node:
    """A representation of a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """A getter function for the `data` attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """A setter function for the `data` attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """A getter function for the `next_node` attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """A setter function for the `next_node` attribute"""
        if not((value is None) or (isinstance(value, Node))):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A representation of a singly linked list data structure"""

    def __init__(self):
        """The constructor for the class object"""
        self.__head = None

    def __str__(self):
        """String representation of the class using the `print()` function"""
        result = ""
        tmp = self.__head
        while tmp:
            result += str(tmp.data) + "\n"
            tmp = tmp.next_node
        return result[:-1]

    def sorted_insert(self, value):
        """Inserts a new Node into the SinglyLinkedList.

        A new Node is created from `value` and inserted into the correct
        sorted position in the list in an increasing order.

        Args:
            value (int): the new Node to be inserted in the list.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data >= value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
