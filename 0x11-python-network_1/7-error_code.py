#!/usr/bin/python3
"""
Sends a request to a given URL and displays the response body.

Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""

import sys
import requests


if __name__ == "__main__":
    # Get URL from command-line arguments
    url = sys.argv[1]

    # Send a GET request to the specified URL
    r = requests.get(url)

    # Check if the response status code is an error code (>= 400)
    if r.status_code >= 400:
        # Print an error message with the status code
        print("Error code: {}".format(r.status_code))
    else:
        # Print the response body
        print(r.text)
