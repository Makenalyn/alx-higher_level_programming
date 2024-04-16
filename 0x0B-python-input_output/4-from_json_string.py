#!/usr/bin/python3
import json
""" functions returns ab object represented by a json string """


def from_json_string(my_str):
    """

    return tan object represented by a json string

    my_str: object to return from the JSON format to object

    Return: object
    """
    return json.loads(my_str)
