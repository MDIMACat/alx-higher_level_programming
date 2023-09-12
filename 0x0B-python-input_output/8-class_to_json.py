#!/usr/bin/python3
"""Module that gives __dict__ of simple data structure"""


def class_to_json(obj):
    """Implementation of the class_to_json module"""
    new_dict = obj.__dict__
    return new_dict
