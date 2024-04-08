#!/usr/bin/python3

class Rectangle:
    __width

    def width(self):
        return self.__width

    def width(self, value):
        self.value = value

        try:
           self.value is int
        except TypeError:
            print("width must be an integer")

        try:
            self.value < 0
        except ValueError:
            print("width must be >= 0")
            raise
    __height

    def height(self):
        return self.__height

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
            raise

    def __init__(self, width=0, height=0):
        self.width = 0
        self.height = 0

    def area(self):
        pass

    def perimeter(self):
        pass
