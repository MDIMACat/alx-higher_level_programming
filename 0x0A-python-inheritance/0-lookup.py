#!/usr/bin/python3
"""Defines the function to lookup available attributes"""


def lookup(obj):
    """Function to return a new_list for available attributes"""
    new_list = []
    for attribute in dir(obj):
        if not callable(getattr(obj, attribute) or attribute.startswith('__')):
            new_list.append(attribute)
    return new_list
