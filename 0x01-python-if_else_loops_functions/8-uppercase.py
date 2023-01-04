#!/usr/bin/python3
def uppercase(str):
    a = ord('a')
    A = ord('A')
    diff = a - A
    print(''.join([chr(ord(char) - diff) if a <= ord(char) <= ord('z') else char for char in str]))
