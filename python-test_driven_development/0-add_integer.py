#!/usr/bin/python3
""" Module documented by Ken Ganza
This code creates a function that adds two integers and returns an error when one is of the parameters is not an integer
"""
def add_integer(a, b=98):
    """ This FUnction perfoms the task at hand"""
    if not isinstance(a, (int, float)): 
        raise TypeError("a must be an integer")
    elif not isinstance(a, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return int(a) + int(b)
