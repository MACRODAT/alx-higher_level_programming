#!/usr/bin/python3

""" file reader """


def read_file(filename = ""):
    """ reads a file """
    with open(filename, "r", encoding="utf8") as f:
        print(f.read())
