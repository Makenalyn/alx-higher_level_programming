#!/usr/bin/python3

def no_c(my_string):
    nw_str = my_string[:]
    for i in nw_str:
        if i == chr(67) or i == chr(99):
            continue
        return nw_str
