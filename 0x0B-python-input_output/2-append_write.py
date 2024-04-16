#!/usr/bin/python3

""" appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """ attempts to open a file with with as it appends a string """
    with open(filename, "a", encoding="utf-8") as f:
        data = f.write(text)

    return data
