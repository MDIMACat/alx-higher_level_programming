#!/usr/bin/python3
"""
Module to prints a text with 2 new lines after each of these characters:
., ? and :

example:

"""


def text_indentation(text):
    """
    text_indentation - Function prototype for module

    Parameters:
    text - string arguement passed in to module

    Returns:
    parsed text split at the following characters:
    ., ? and :

    Raises:
    TypeError:
        Is argument that isnt a string is passed -
        raise this error message

    """
    if not isinstance(text, str) or text == "":
        raise TypeError("text must be a string")

    char = [".", "?", ":"]
    lines = []
    current_line = ""

    for letter in text:
        current_line += letter
        if letter in char:
            lines.append(current_line.strip())
            current_line = ""

    if current_line:
        lines.append(current_line.strip())

    for line in lines:
        print(line)
