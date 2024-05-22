#!/usr/bin/python3
"""
Takes your GitHub credentials (username and personal access token)
and uses the GitHub API to display your id.
"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, password))

    try:
        user_info = response.json()
        print(user_info.get('id'))
    except ValueError:
        print(None)
