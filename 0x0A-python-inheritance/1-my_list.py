#!/usr/bin/python3
""" function inherits from another class """


class MyList(list):
    """ sorts a list provided """

    def print_sorted(self):
        self.sort()
        print(self)
