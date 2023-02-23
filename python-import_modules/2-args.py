#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv)
    if l == 1:
        print("{} argument.".format(l - 1))
    else:
        print("{} argument:".format(l - 1))
    for c in range(1, l):
        print("{}: {}".format(c, sys.argv(c)))
