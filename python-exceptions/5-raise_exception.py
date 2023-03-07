#!/usr/bin/python3
def raise_exception():
    x = int(input("Name?"))
    if isinstance(x, int):
        return x
    else:
        raise(TypeError("This is a type error"))
