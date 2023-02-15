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
        if all((isinstance(value, tuple),
                all(map(lambda x: isinstance(x, int), value)),
                value[0] >= 0, value[1] >= 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and return the area of the `Square` object"""
        return self.size ** 2

    def my_print(self):
        """Prints out the square to the stdout"""
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            self._print_square(self.position[0])

    def _print_square(self, h_pos=0):
        """Protected function to print a square starting at `h_pos`
        horizontal position"""
        for i in range(self.size):
            print(" " * h_pos, end="")
            print("#" * self.size)
