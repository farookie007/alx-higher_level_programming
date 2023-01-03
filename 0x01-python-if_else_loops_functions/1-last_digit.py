#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# in order to get the absolute value of number is number is -ve
flag = -1 if number < 0 else 1
# converts the last digit to -ve if number was originally -ve
l_digit = ((flag * number) % 10) * flag
print(f"Last digit of {number} is {l_digit} and is ", end="")
if l_digit == 0:
    print(l_digit)
else:
    print(f"{'greater than 5' if l_digit > 5 else 'less than 6 and not 0'}")
