#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    add = 0
    if length == 1:
        add = 0
    else:
        for c in range(1, lengt):
            add += int(sys.argv[c])
    print(add)
