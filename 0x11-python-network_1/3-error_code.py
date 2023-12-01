#!/usr/bin/python3
"""Handle Exceptions in HTTP Requests"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":

    url = argv[1]

    req = Request(url)

    try:
        with urlopen(req) as response:
            page = response.read().decode()
            print(page)

    except HTTPError as error:
        print(f"Error code: {error.code}")
