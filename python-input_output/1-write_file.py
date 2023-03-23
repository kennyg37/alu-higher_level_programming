#!/usr/bin/python3
"""
Defines a file-appending function.
"""


def write_file(filename="", text=""):
     """Appends a string to the end of a UTF8 text file"""
    with open(filename, "w", encoding="utf-8") as c:
        return c.write(text)
