#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        print("{}".format(my_list[0:x]))
    except ValueError as e:
        print(e)
