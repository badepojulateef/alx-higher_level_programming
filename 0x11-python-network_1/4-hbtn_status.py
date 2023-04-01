#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status.

Usage: ./4-hbtn_status.py

Returns:
    The body of the response to the request, as a string.

Example:
    ./4-hbtn_status.py

Features:
    - Uses the Python requests library to make a GET
    request to a specified URL.
"""

import requests
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    # Make a GET request to the URL using the requests library
    r = requests.get(url)

    # Print out the response body
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
