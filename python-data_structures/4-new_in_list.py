#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    else:
        my1_list = my_list.copy()
        my1_list[idx] = element
        return my1_list
