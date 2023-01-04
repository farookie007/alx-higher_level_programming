#!/usr/bin/python3
def uppercase(str):
    a = ord('a')
    A = ord('A')
    diff = a - A
    for ch in [chr(ord(char) - diff) if a <= ord(char) <= ord('z') else char for char in str]:
        print("{}".format(ch))
