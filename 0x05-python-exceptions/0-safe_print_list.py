#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]))
    except Error as e:
        print(e)
