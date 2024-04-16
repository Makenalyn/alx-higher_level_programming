#!/usr/bin/python3

""" function writes a string into a text file"""


def write_file(filename="", text=""):
    """ using with to open the file"""

    with open(filename, 'r+', encoding="utf-8") as f:
        data = f.write(text)

    return data
