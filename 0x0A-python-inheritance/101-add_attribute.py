#!/usr/bin/python3
"""Module to add new attribute"""


def add_attribute(obj, name, values):
    """Add new attribute"""
    if hasattr(obj, '__dict__'):
        obj.__dict__[name] = values
    else:
        raise TypeError("can't add new attribute")
