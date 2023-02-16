#!/usr/bin/python3
"""Defines a `Square` class."""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """The constructor method for the `Square` class
        Args:
            size (int): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the value of the size of the `Square`"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and return the area of the `Square` object"""
        return self._Square__size ** 2i

    def __lt__(self, other):
        """Checks if the object is less than the other object based
        on their area"""
        return self.area < other.area

    def __gt__(self, other):
        """Checks if the object is greater than the other object
        based on their area"""
        return self.area > other.area

    def __eq__(self, other):
        """Checks if the object is equal to the other object
        based on their area"""
        return self.area == other.area

    def __le__(self, other):
        """Checks if the object is less than or equal to the 
        other object based on their area"""
        return self.area <= other.area

    def __ge__(self, other):
        """Checks if the object is greater than or equal to the other
        object based on their area"""
        return self.area >= other.area

    def __ne__(self, other):
        """Checks if the object is not equal to the other object based
        on their area"""
        return self.area != other.area