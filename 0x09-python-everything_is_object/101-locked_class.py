#!/usr/bin/python3
"""Class to define Locked class"""


class LockedClass:
    """A class that prevents the user from dynamically creating new instance"""
    __slots__ = ["first_name"]
