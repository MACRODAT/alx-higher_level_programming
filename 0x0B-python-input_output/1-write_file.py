#!/usr/bin/python3

""" file writer """


def write_file(filename="", text=""):
    """ wr a file """
    if filename == "":
        return
    with open(filename, "w") as f:
        return f.write(text)
