#!/usr/bin/python3
""" import json module to represent the json module"""
import json
""" function returns a string rep of a JSON notation """


def to_json_string(my_obj):
    """
    return a string from the json object

    my_obj: object to return JSON representation from

    Return: string object
    """
    return json.dumps(my_obj)
