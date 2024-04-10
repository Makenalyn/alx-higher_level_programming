#!/use/bin/python3

class Rectangle:
    __width = 0

    def width(self):
        self.__width = __width

    def width(self, value):
        self.value = value

    try:
        width is int
    except TypeError:
        print("width must be an integer")

    try:
        __width < 0
    except ValueError:
        print("width must be >= 0")


    __height = 0

    def height(self):
        self.__width = __width

    def height(self, value):
        self.value = value

    try:
        height is int
    except TypeError:
        print("height must be an integer")

    try:
        __height < 0
    except ValueError:
        print("height must be >= 0")

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = 0
        self.height = height

    def area(self):
        pass

    def perimeter(self):
        pass
