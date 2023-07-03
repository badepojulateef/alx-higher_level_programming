#!/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./5-hbtn_header.py <URL>
"""

import sys
import requests


if __name__ == "__main__":
    # Get URL from command-line arguments
    url = sys.argv[1]

    # Send a GET request to the URL using requests module
    res = requests.get(url)

    # Print the value of the X-Request-Id header in the response
    print(res.headers.get("X-Request-Id"))
