#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with a given letter.

Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""

import sys
import requests


if __name__ == "__main__":
    # Get the letter to search for from the command-line arguments,
    # if provided
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    # Construct the payload with the letter to search for
    payload = {"q": letter}

    # Send a POST request to the search_user endpoint with the payload
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        # Try to decode the response as JSON
        response = r.json()

        # If the response is empty, print "No result"
        if response == {}:
            print("No result")
        # If the response has an "id" and "name" field, print them
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        # If the response is not valid JSON, print "Not a valid JSON"
        print("Not a valid JSON")
