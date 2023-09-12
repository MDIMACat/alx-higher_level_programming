#!/usr/bin/python3
"""Module that that creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """Implemention of module that creates object"""
    with open(filename, "w", encoding="utf-8") as file1:
        content = json.loads(file1.read())
        return content
