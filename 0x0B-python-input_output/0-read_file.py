#!/usr/bin/python3
"""Module to read file"""


def read_file(filename=""):
    """Implementing module that reads file"""
    if filename is not None:
        with open(filename, "r", encoding="utf-8") as file1:
            content = file1.read()
            print(content, end="")
