#!/usr/bin/python3
def no_c(my_string, C, c):
    if my_string is None or len(my_string) == 0:
        return None
    elif c in my_string:
        return my_string.remove(c)
    elif C in my_string:
        return my_string.remove(C)
    else:
        return None
