#!/usr/bin/python3
"""
Sends a POST request to a given URL with a given email.

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import sys
import requests


if __name__ == "__main__":
    # Get URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Set the email data to be sent in the request
    data = {"email": email}

    # Send a POST request to the specified URL with the email data
    r = requests.post(url, data=data)

    # Print the response body
    print(r.text)
