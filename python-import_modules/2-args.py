#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    kk = len(sys.argv)
    if kk == 1:
        print("{} arguments.".format(kk - 1))
    else:
        print("{} arguments:".format(kk - 1))
    for c in range(1, kk):
        print("{}: {}".format(c, sys.argv[c]))
