#!/usr/bin/python3
"""GitHub API Script"""

import sys
import requests

if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.exit(1)
    else:
        username = sys.argv[1]
        password = sys.argv[2]

    url = "https://api.github.com/users"

    auth = (username, password)

    req = requests.get(url, auth=auth)

    if req.status_code == 200:
        user_data = req.json()
        user_id = user_data.get('id')

        print(user_id)
