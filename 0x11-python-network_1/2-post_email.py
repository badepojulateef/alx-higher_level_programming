#!/usr/bin/python3
"""
Sends a POST request to a given URL with a given email and
displays the body of the response.

Usage: ./2-post_email.py <URL> <email>

Arguments:
    <URL>: The URL to which the POST request will be sent.
    <email>: The email address that will be sent as a parameter
    with the POST request.

Returns:
    The body of the response to the POST request, as a UTF-8 encoded string.

Example:
    ./2-post_email.py http://example.com/api/users/ john@example.com
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    # Retrieve URL and email address from command-line arguments
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    # Encode email address as a URL parameter
    data = urllib.parse.urlencode(value).encode("ascii")

    # Create request object with URL and encoded data
    request = urllib.request.Request(url, data)

    # Send HTTP POST request and retrieve response
    with urllib.request.urlopen(request) as response:
        # Decode response body as UTF-8 encoded string and print to console
        print(response.read().decode("utf-8"))
