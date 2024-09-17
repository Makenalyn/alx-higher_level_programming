#!/usr/bin/python3

def add_integer(a, b=98):
    try:
        isinstance(a, int)
    except TypeError:
        print("a must be an integer")
    try:
        isinstance(b, int)
    except TypeError:
        print("b must be an int")
