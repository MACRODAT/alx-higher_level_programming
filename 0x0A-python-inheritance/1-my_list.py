#!/usr/bin/python3

""" base help """


class MyList(list):
    """a sub list"""
    def __init__(self):
        """ help here """
        super().__init__()

    def print_sorted(self):
        """ print sorted """
        print(sorted(self))
