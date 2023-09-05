#!/usr/bin/python3
"""
Module that is used to print out a fullname

example:

>>> say_my_name("Tiff", "Johns")
My name is Tiff Johns

"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name - funtion prototype for the above function

    Parameters:
    first_name - string for first name passed in as first argument
    last_name - string for last name passed in as a second argument

    Returns:
    My name is <first name> <last name>

    Raises:
    TypeError:
        if both arguements are not string, error message is raised

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
