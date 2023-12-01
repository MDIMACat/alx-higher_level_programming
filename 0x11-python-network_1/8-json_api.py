#!/usr/bin/python3
"""Handles a JSON content"""

from sys import argv
import requests

if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ''

    json_payload = {'q': letter}

    req = requests.post(url, json_payload)

    content = req.headers.get('Content-type')

    if (content == 'application/json'):
        json_file = eval(req.text)

        if json_file != {}:
            print(f"[{json_file.get('id')}] {json_file.get('name')}")
        else:
            print('No result')
    else:
        print('Not a valid JSON')
