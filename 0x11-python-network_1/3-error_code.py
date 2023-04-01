#!/usr/bin/python3
"""
Sends a request to a given URL and displays the response body.

Usage: ./3-error_code.py <URL>

Arguments:
    <URL>: The URL to which the request will be sent.

Returns:
    The body of the response to the request, as an ASCII-encoded string.

Example:
    ./3-error_code.py http://example.com/api/users/

Features:
    - Handles HTTP errors.

"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    # Retrieve URL from command-line arguments
    url = sys.argv[1]

    # Create request object with URL
    request = urllib.request.Request(url)

    try:
        # Open URL and retrieve response
        with urllib.request.urlopen(request) as response:
            # Read response body and decode as ASCII-encoded string
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        # Handle HTTP error and print error code
        print("Error code: {}".format(e.code))
