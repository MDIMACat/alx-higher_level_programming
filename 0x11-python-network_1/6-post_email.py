#!/usr/bin/python3
"""POST script that post email to server"""

from sys import argv
import requests

if __name__ == "__main__":

    url = argv[1]
    email = argv[2]

    req = requests.post(url, data={'email': email})
    print(req.text)
