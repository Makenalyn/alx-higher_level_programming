#!/usr/bin/python3
""" class base that will be base of other classes """


class Base:
    """ private attribute obj cont """
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = None

    if id is not None:
        id = id
    else:
        _nb_objects += 1
