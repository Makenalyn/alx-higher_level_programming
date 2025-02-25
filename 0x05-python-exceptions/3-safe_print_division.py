#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        a / b
    except ZeroDivisionError as e:
        print("{}".format(e))
    finally:
        return a / b
