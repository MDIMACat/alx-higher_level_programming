#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size(int): The integer size of square"""
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
        """return the area of square"""
        return self.__size ** 2

    def my_print(self):
        """Prints out the square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
