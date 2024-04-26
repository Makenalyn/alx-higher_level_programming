#!/usr/bin/python3

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = None

    if id not None:
        self.id=id
    else:
        _nb_objects += 1
