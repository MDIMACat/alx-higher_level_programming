#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square

        Args:
            size (int): Size of the square
            position (tuple): Position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return self.size ** 2

    def my_print(self):
        """Print out the square"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
