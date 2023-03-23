#!/usr/bin/python3
""" Module documented"""


def append_write(filename="", text=""):
    """ Fynction documented"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
