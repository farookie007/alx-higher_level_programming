#!/usr/bin/python3

def div(a, b):
    return a / b


def safe_print_division(a, b):
    result = None
    try:
        result = div(a, b)
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
        return result
