#!/usr/bin/python3
"""Class for student"""


class Student:
    """Implementing class for student"""
    def __init__(self, first_name, last_name, age):
        """
        Initialize a student instance.

        Args:
        first_name:
            The first name for the student
        last_name:
            The last name for the student
        age : integer
            The age for the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if attrs is None:
            return self.__dict__
        else:
            return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}

    def reload_from_json(self, json):
        
        for key, value in json.items():
            setattr(self, key, value)

