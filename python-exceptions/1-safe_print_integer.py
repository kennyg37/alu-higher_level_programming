#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".forma(value))
        return True
    except (ValueError, IndexError):
        return False
    finally:
        print()
        return x
