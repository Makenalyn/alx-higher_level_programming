#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
module = number % 10
if module > 5:
    print(f"Last digit of {number} is {module} and is greater than 5")
if module == 0:
    print(f"Last digit of {number} is {module} and is 0")
if module < 6 and not 0:
    print(f"Last digit of {number} is {module} and is less than 6 and not 0")
