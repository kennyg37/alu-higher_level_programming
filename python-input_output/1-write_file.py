#!/usr/bin/python3
"""Defines a file-appending function."""


def write_file(filename="", text=""):
     """Appends a string to the end of a UTF8 text file.
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, 'w', encoding='UTF8') as c:
        return c.write(text)
