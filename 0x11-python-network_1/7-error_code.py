#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status.

Usage: ./7-error_code.py <URL>

Returns:
    The body of the response to the request, as a string.

Example:
    ./7-error_code.py

Features:
    - Uses the Python requests library to make a GET
    request to a specified URL.
"""

import sys
import requests


if __name == "__main__":
    # Get URL from command-line arguments
    url = sys.argv[1]

    # Send a GET request to the specified URL
    res = requests.get(url)

    # Check if the response status code is an error code (>= 400)
    if res.status_code >= 400:
        # Print an error message with the status code
        print("Error code: {}".format(res.status_code))

    else:
        # Print the response body
        print(res.text)
