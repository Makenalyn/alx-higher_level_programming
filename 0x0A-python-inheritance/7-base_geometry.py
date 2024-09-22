#!/usr/bin/python3

""" class BaseGeometry"""
class BaseGeometry:
    def area(self):
        raise Exception("area is not implemented")
    
    def integer_validator(self, name, value):
        try:
            isinstance(value, int)
        except TypeError:
            print("<name> must be an integer")
            raise

        if value <= 0:
            raise ValueError("<name> must be greater than 0")
