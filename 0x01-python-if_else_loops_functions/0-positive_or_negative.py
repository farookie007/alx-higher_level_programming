#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(f"{number} is ", end="")
if number == 0:
    print("zero")
else:
    print(f"{'positive' if number > 0 else 'negative'}")
