#!/usr/bin/python3

def element_at(my_list, idx):
    for i in range(len(my_list)):
        if idx > i:
            return None
        elif idx < 0:
            return None
        else:
            return my_list[idx]

        
