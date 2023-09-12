#!/usr/bin/python3
"""Module that takes json string to python obj"""
import json


def from_json_string(my_str):
    """Implementing module from json-str to python obj"""
    new_string = json.loads(my_str)
    return new_string
