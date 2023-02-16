#!/usr/bin/python3
"""Defines a `Square` class."""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """The constructor method for the `Square` class
        Args:
            size (int): the size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Returns the position of the top-left edge of the square"""
        return self.__position

    @position.setter
    def position(self, value: tuple):
        """Sets the value of the position attr of the class"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """String representation of the object"""
        return self._get_square_string()

    def area(self):
        """Calculates and return the area of the `Square` object"""
        return self.size ** 2

    def my_print(self):
        """Prints out the square to the stdout"""
        result = ""
        if self.size != 0:
            result = _get_square_string()
        print(result)

    def _get_square_string(self):
        """Protected function to return the equivalent string of a Square
        object."""
        result = ""
        result += "\n" * self.position[1]
        for i in range(self.size):
            result += " " * self.position[0]
            result += "#" * self.size
        return result
