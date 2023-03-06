#!/usr/bin/python3
def safe_print_integer(value):
    try:
        for x in value:
            print("{:d}".format(x))
            if not isinstance(x, int):
                return True
    except IndexError:
        return False
    finally:
        print()
        return x
