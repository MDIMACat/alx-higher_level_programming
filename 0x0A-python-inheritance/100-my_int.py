#!/usr/bin/python3
"""class int"""


class MyInt(int):
    """Implementing MyInt class"""
    def __ne__(self, other):
        return self.real == other

    def __eq__(self, other):
        return self.real != other
