#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_keys = sorted(a_dictionary.items())
    for key in sort_keys:
        print("{}: {}".format(key[0], key[1]))
