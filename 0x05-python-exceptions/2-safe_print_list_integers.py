#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    for i in range(0, x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format())
        except ValueError:
            print("value is not an integer")
