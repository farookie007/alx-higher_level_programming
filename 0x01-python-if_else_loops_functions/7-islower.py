#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(str(c)) <= ord('z')

print(islower('c'))
print(islower("A"))
print(islower(9))
print(islower('9'))
