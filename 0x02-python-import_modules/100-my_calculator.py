#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(args[1])
    op = args[2]
    b = int(args[3])
    ops = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div
            }
    if op not in ops.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, op, b, ops[op](a, b)))
