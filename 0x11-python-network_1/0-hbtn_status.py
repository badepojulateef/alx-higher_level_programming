#!/usr/bin/python3
"""
A script that Displays the X-Request-Id header var
of a given req
"""
import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.arv[1]

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            x_request_id = dict(response.headers).get("X-Request-Id")
            if x_request_id is not None:
                print(x_request_id)

    except urllib.error.URLError as e:
        print("Error opening URL:", e.reason)
        sys.exit(1)
