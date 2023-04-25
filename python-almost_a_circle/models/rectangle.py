#!/usr/bin/python3
""" Modules documented"""
from models.base import Base


class Rectangle(Base):
    """ documment and acquire class Base to class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.hight = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property

