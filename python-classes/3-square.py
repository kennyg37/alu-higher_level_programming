#!/usr/bin/python3
""" Module documented"""


class Square:
    """ Class documented"""
    def __init__(sef, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size == 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size
    def area(self):
        return area
