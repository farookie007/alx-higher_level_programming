#!/usr/bin/python3
"""This module contains a class `Square` that defines a square"""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        """The constructor method for the `Square` class
        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and return the area of the `Square` object"""
        return self._Square__size ** 2
