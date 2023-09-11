#!/usr/bin/python3
"""Module for object is an instance of a class that inherited from class"""


def inherits_from(obj, a_class):
    """
    inherits_from - Function prototype
    obj - object arguement
    a_class - class arguement
    Returns: True if is a instance of inherited class otherwise false
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
