#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    add = sum(int(args) for arg in args)
    print(add)
