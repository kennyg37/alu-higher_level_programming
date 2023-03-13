#!/usr/bin/python3
""" Module not imported but documented, crazy, right?"""


class Square:
    """ Class documented"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < o:
            raise ValueError("size must be >= 0")
        else:
             self._Square__size= size



