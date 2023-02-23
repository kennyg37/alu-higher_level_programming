#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    a = 10
    b = 5
    def add(a, b):
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    def sub(a, b):
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    def mul(a, b):
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    def div(a, b):
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
