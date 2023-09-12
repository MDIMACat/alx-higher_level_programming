#!/usr/bin/python3
"""Module to convert python obj to json string"""
import json


def to_json_string(my_obj):
    """Implementation of json string"""
    new_string = json.dumps(my_obj)
    return new_string
