#!/usr/bin/python3
""" Modules documented"""


class Rectangle(Base):
    """ documment and acquire class Base to class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.hight = height
        self.x = x
        self.y = y
        super().__init__(id)
