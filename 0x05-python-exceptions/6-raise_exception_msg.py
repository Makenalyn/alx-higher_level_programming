#!/usr/bin/python3

def raise_exception_msg(message=""):
    try:
        raise Exception(message)
        print(message)
    except Exception as e:
        print(e)
