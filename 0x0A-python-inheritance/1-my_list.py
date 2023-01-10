#!/usr/bin/python3
""" Defines MyList class """


class MyList(list):
    """ Defines a subclass of class """
    def __init__(self):
        """ Initializes the object """
        super().__init__

    def print_sorted(self):
        """ prints the a sorted list in an ascending sort """
        print(sorted(self))
