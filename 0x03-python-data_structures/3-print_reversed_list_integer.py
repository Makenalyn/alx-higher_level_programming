#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    copy_list = my_list.copy()
    copy_list.reverse()
    for i in range(len(copy_list)):
        print('{}'.format(copy_list[i]))
