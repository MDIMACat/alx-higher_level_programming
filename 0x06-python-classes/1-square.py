#!/usr/bin/python3
"""Defining a class square by private instance attribute"""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """initialize the size of square

        Args:
            size (int): The integer size of the new square"""
        self.__size = size
