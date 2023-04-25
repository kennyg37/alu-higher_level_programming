#!/usr/bin/python3
""" module being used is unidentifiable at begginig 


"""

class Base:
    """ Class Base is being used to define all objects and methods"""
    _nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
