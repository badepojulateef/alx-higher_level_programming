#!/usr/bin/python3
"""
A script that fetches https://intranet.hbtn.io/status
using urllib and displays the res body
"""


if __name__ == "__main__":
    from urllib.request import urlopen

    def getStatus(url):
        """ A function that fetches the content of a url
        and displays its res

        Args:
            url (str): The URL to fetch

        Returns:
            None: The function prints but not returns nothing

        """

        # Open the URL as a response object
        with urlopen(url) as res:

            # Read the contents of the response
            status = res.read()

            # Display the res
            print("Body response:")
            print("\t- type: {}".format(type(status)))
            print("\t- content: {}".format(status))
            print("\t- utf8 content: {}".format(status.decode('utf-8')))

    # URL to fetch
    url = "https://alx-intranet.hbtn.io/status"

    # Call the getStatus function with the URL
    getStatus(url)
