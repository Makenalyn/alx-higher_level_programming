#!/usr/bin/python3
""" checks if an obj is an instance of class """


def inherits_from(obj, a_class):
    """ if it is, return True, else, False """
    if isinstance(obj, a_class):
        return True
    else:
        return False
