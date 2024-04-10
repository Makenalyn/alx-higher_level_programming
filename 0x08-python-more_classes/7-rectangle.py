#!/usr/bin/python3

class Rectangle:
    __width = 0

    def width(self):
        self.__width = __width

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.value = value

    __height = 0

    def height(self):
        self.__height = __height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.value = value

    number_of_instances = 0

    print_symbol = '#'

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width * self.__height)

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

