#!/usr/bin/python3
"""Script that displays X-Request-Id variable"""

from urllib.request import Request, urlopen
from sys import argv

if __name__ == "__main__":

    url = argv[1]

    req = Request(url)

    with urlopen(req) as response:
        value = response.getheader("X-Request-Id")
        print(value)
