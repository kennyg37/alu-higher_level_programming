#!/usr/bin/python3
""" Module documented """


def write_file(filename="", text=""):
    """ define function 
    that includes the objects filename and text"""

    with open(filename, mode="w", encoding="UTF8") as c:
        print(c.read(), end=""
                return len(c.read()))
