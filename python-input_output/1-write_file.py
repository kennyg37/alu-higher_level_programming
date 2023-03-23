#!/usr/bin/python3
"""this module gives out an output to override a certain file

uses with function embedded in write_file

"""

def write_file(filename="", text=""):
     """Appends a string to the end of a UTF8 text file.
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, mode='w', encoding='UTF8') as c:
        print(c.read(), end=''
                return len(c.read()))
