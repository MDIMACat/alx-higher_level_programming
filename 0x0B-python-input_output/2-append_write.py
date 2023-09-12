#!/usr/bin/python3
"""Module to append to .txt file"""


def append_write(filename="", text=""):
    """Implementing an append module"""
    char_count = 0
    with open(filename, "a", encoding="utf-8") as file1:
        char_count = file1.write(text)
        return char_count
