#!/usr/bin/python3
"""Defines an integer function"""


def add_integer(a, b=98):
    """Function returns an integer addition of the two variables

    if float is passed its typecasted into an int and then added

    Raises:
      TypeError: If either of a or b is a non-integer and non-float."""

    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
