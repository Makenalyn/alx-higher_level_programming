#!/usr/bin/puthon3

def delete_at(my_list=[], idx=0):
    for i in my_list:
        if i > idx:
            return my_list
        del(my_list[idx])
