#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
module = number % 10
if module is > 5:
    print(f"Last digit of {number} is {module} and is greater than five")
if module == 0:
    print(f"Last digit of {number} is {module} and is zero")
if module < 6:
    print(f"Last digit of {number} is {module} and is less than size and not zero")
