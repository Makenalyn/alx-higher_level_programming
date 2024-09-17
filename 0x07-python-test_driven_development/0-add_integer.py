#!/usr/bin/python3

def add_integer(a, b=98):
    if a or b not int:
        raise TypeError("a must be an integer")
    if b not int:
        raise TypeError("b must be an integer")

    return a + b
