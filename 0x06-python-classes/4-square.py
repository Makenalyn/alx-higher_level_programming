#!/usr/bin/python3

""" class square that defines a square"""


class Square:

    """ private instance attribute"""
    __size = None

    """ initialization of the attribute size"""
    def __init__(self, size=0):
        self.__size = size

    def size(self):
        return self.__size

    def size(self, value):
        self.value = value

    def area(self):
        return self.__size * self.__size
