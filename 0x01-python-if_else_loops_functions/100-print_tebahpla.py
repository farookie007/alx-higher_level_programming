#!/usr/bin/python3

def uppercase(char):
    a = ord('a')
    A = ord('A')
    diff = a - A
    return chr(ord(char) - diff) if a <= ord(char) <= ord('z') else char


lower = True
for i in range(ord('z'), ord('a') - 1, -1):
    char = chr(i)
    print("{}".format(char if lower else uppercase(char)), end="")
    lower = not lower
