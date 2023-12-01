#!/usr/bin/python3
if __name__ == "__main__":
    """script that fetches from a given URL"""

    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError

    url = "https://alx-intranet.hbtn.io/status"

    req = Request(url)

    with urlopen(req) as response:
        page = response.read()
        print("Body response:")
        print(f"\t- type: {type(page)}")
        print(f"\t- content: {page}")
        print(f"\t- utf8 content: {page.decode()}")
