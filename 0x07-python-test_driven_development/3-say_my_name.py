#!/usr/bin/python3
"""Defines a function say_my_name"""


def say_my_name(first_name, last_name=""):
    """Function returns a persons first and last name

    Args:
        first_name (str): this is the variable for first_name
        last_name(str): variable for last_name

    Return: First and last name

    Raises a TypeError if input isnt a string"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
