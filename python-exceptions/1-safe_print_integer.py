#!/usr/bin/python3
def safe_print_integer(value):
    try:
        for x in value:
            print("{:d}".format(x))
    except IndexError:
        pass
    finally:
        print()
        return x
