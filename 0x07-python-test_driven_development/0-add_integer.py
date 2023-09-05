#!/usr/bin/python3
"""
Modules that adds two integer values

for example
add_integer(2, 3)
5
"""


def add_integer(a, b=98):
    """
    add_integer: function prototype used for this module

    Parameters:
    a - first arguement to be passed to function (int or float)
    b - second arguement to be passed to function (int or float)

    Returns:
    Module is expected to return an int value

    Raises

    TypeError:
        Error message is displayed when a value that isn't an integer or float
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
