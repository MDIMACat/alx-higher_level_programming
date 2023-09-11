#!/usr/bin/python3
"""Module to check if object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class -Function prototype
    obj - object arguement
    a_class - class arguement
    Return: True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
