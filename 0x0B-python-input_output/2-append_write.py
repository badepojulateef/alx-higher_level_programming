#!/usr/bin/python3
"""Defines a function that appends a string at the end 
of a text file (UTF8) and returns the number of characters.
"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file (UTF8) 
    and returns the number of characters.
    """
    with open(filename, "a") as f:
        return f.write(text)
