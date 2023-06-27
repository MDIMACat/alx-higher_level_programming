#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size(int): integer size square"""
        self.__size = 0
        self.size = size

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

    def area(self):
        """returns the area of square"""
        return self.__size ** 2
