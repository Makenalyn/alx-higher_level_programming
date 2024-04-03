#!/usr/bin/python3

""" class square that defines a square """


class Square:
    """ protected attribute size """
    __size = None

    """ initializing the size attribute """
    def __init__(self, size=0):
        self.__size = size

    """ defining the attribute to get it """
    def size(self):
        return self.__size

    def size(self, value):
        self.value = value

    """ returns the area of a square """
    def area(self):
        return self.__size * self.__size

    def my_print(self):
        print('#{}'.format(self.__size * self.__size))
