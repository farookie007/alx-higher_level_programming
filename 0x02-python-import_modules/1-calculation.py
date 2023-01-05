#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div


    a = 10
    b = 5
    for op in zip([add, sub, mul, div], ["+", "-", "*", "/"]):
        print("{} {} {} = {}".format(a, op[1], b, op[0](a, b)))
