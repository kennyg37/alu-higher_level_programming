#!/usr/bin/python3
"""this module gives out an output to override a certain file

uses with function embedded in write_file

"""

def write_file(filename="", text=""):
    """define function 
    that includes the objects filename and text"""

    with open(filename, mode='w', encoding='UTF8') as c:
        print(c.read(), end=''
                return len(c.read()))
