#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    for c in my_list:
        if c % 2 == 0:
            return True
        else:
            return False
    return my_list
