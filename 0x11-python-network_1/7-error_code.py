#!/usr/bin/python3
"""Handle Exceptions in HTTP Requests"""

from sys import argv
import requests

if __name__ == "__main__":

    url = argv[1]

    try:
        req = requests.get(url)
        req.raise_for_status()
        print(req.text)
    except requests.exceptions.HTTPError as err:
        print(f"Error code: {err.response.status_code}")
