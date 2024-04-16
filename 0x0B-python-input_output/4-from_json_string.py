#!/usr/bin/python3
""" functions returns ab object represented by a json string """
import json

def from_json_string(my_str):
    """

    return tan object represented by a json string

    my_str: object to return from the JSON format to object

    Return: object
    """
    return json.loads(my_str)
