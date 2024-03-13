#!/usr/bin/python3

def fizzbuzz():
    for i in range(0, 99):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print(f'Buzz')
        if i % 5 and i % 3:
            print("FizzBuzz")
