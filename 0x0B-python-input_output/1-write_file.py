#!/usr/bin/python3

""" file writer """


def write_file(filename="", text=""):
    """ wr a file """
    if filename == "":
        return
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
