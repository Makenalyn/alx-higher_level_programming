#!/usr/bin/python3
""" function returns true if an object is a ninstance"""


def is_same_class(obj, a_class):
    """ if True, return an affirmation """

    if isinstance(obj, type(a_class)):
        return True
    else:
        return False
