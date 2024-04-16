#!/usr/bin/python3

""" function reads a text from a file"""


def read_file(filename=""):
    """uses with to open file """

    with open(filename, encoding="utf-8") as f:
        write_data = f.read()
        print(write_data)
