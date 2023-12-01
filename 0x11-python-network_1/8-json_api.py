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

    req = requests.post(url, json=json_payload)

    if req.status_code == 200:
        response_json = req.json()
        if response_json:
            user = response_json[0]
            print("[{}] {}".format(user.get('id'), user.get('name')))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
