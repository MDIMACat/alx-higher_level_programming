#!/usr/bin/python3
"""POST script that post email to server"""

from urllib.request import Request, urlopen
from urllib import parse
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    email = argv[2]
    info = {'email': email}

    data = parse.urlencode(info).encode('ascii')

    req = Request(url, data)
    with urlopen(req) as response:
        page = response.read().decode()
        print(page)
