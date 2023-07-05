#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.

Usage:
    ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    # Construct the API endpoint for the given repository

    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])

    def getCommit(url):
        """
        A function that fetches the contents of a URL
        using urlopen and displays its contents.

        Args:
            url (str): The URL to fetch.

        Returns:
            None. The function only prints the contents of the URL.

        """
        url = "https://api.github.com/repos/{}/{}/commits".format(
                sys.argv[2], sys.argv[1])

        # Send a GET request to the API endpoint
        r = requests.get(url)

        # Parse the JSON response from the API into a list of commits
        commits = r.json()

        try:
            # Print the sha hash and author name for each of the 10 most
            for i in range(10):
                print("{}: {}".format(
                    commits[i].get("sha"),
                    commits[i].get("commit").get("author").get("name")))
        except IndexError:
            # If there are fewer than 10 commits, print as many as possible
            pass

    # Call the getStatus function with the URL
    getCommit(url)
