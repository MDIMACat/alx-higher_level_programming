#!/usr/bin/python3
"""
Module used to print out square (#)

example:
>>> print_square(3)
###
###
###
"""


def print_square(size):
    """
    print_square : function prototype for the module

    Parameters:
    size - is the size length of the square

    Returns:
    A printed square with # values

    Raises:
    TypeError:
        if Size isnt a int, error message will appear

    ValueError:
        if size is less than 0, error message will appear
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print("#", end=" ")
        print()
