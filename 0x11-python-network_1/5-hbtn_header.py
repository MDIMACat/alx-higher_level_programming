#!/usr/bin/python3
"""Script that displays X-Request-Id variable"""

from sys import argv
import requests

if __name__ == "__main__":

    url = argv[1]

    req = requests.get(url)
    head_dict = req.headers
    for key, value in head_dict.items():
        if key == "X-Request-Id":
            print(head_dict[key])
