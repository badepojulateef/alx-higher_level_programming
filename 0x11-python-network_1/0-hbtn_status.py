#!/usr/bin/python3
"""
A a Python script that fetches
https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    from urllib.request import urlopen

    def getStatus(url):
        with urlopen(url) as res:
            status = res.read()
            print("Body response:")
            print("\t- type: {}".format(type(status)))
            print("\t- content: {}".format(status))
            print("\t- utf8 content: {}".format(status.decode('utf-8')))

    url = "https://alx-intranet.hbtn.io/status"
    getStatus(url)

