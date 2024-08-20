#!/usr/bin/python3

def no_c(my_string):
    nw_str = my_string[:]
    for i in nw_str:
        if ord(i) == 67 or ord(i) == 99:
            continue
        else:
            return nw_str
