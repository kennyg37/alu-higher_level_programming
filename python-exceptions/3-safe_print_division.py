#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError):
        return None
    else:
        return result
    finally:
        print("{} / {} = {}".format(a, b, result))