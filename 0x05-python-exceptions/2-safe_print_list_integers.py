#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    for i in my_list:
        try:
            if i == int:
                print("{:d}".format())
        except ValueError:
            print("value is not an integer")
