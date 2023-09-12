#!/usr/bin/python3
"""Module to write objects to text files"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as file1:
        content = json.dumps(my_obj)
    return content
