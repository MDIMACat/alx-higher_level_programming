#!/usr/bin/python3
"""Module that writes to text file"""


def write_file(filename="", text=""):
    """Implementation of reading the text file"""
    char_count = 0
    with open(filename, "w", encoding="utf-8") as file1:
        char_count = file1.write(text)
    return char_count
