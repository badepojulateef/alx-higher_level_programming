#!/usr/bin/python3
""" Defines MyList class """


class MyList(list):
    """ Defines a subclass of class """

    def print_sorted(self):
        """ prints the a sorted list in an ascending sort """
        print(sorted(self))
