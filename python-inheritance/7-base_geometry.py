#!/usr/bin/python3
""" define an empty class."""


class BaseGeometry:
    """ an empty class"""

    def area(self):
        """Not done."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
