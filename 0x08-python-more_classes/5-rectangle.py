#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    __width = 0

    def width(self):
        self.__width = __width

    def width(self, value):
        self.value = value

    try:
        __width is int
    except TypeError:
        print("width must be an integer")

    try:
       __width < 0
    except ValueError:
        print("widthmust be >= 0")

    __height = 0

    def height(self):
        self.__height = __height

    def height(self, value):
        self.value = value

    try:
        __height is int
    except TypeError:
        print("height must be an integer")

    try:
        __height < 0
    except ValueError:
        print("height must be >= 0")

    def area(self):
        pass

    def perimeter(self):
        pass
