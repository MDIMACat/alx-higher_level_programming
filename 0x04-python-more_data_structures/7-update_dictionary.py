#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key in range(len(a_dictionary)):
        if key in a_dictionary:
            a_dictionary["key"] = value
        else:
            a_dictionary["key"] = value
        return a_dictionary


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
