#!/usr/bin/python3
"""
Uses the GitHub API to display a GitHub ID based on given credentials.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    # set the credentials for Basic Authentication
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    # send a GET request to the GitHub API with the credentials
    r = requests.get("https://api.github.com/user", auth=auth)

    # display the user ID of the authenticated user
    print(r.json().get("id"))
