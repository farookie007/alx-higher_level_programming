#!/usr/bin/python3
def print_last_digit(number):
    flag = -1 if number < 0 else 1
    l_digit = ((flag * number) % 10)
    print(f"{l_digit}", end="")
    return l_digit
