#!/usr/bin/python3
"""Class to inherit from list"""


class MyList(list):
    """Subclass of list that has inherited list attributes and instances"""

    def print_sorted(self):
        """Prints sorted lists on integers"""
        new_list = self.copy()
        n_list = sorted(new_list)
        print(n_list)
