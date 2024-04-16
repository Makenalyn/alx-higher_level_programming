#!/usr/bin/python3
""" import json module to represent the json module"""
import json


def to_json_string(my_obj):
    """ return the JSON rep of a string object """
    return json.dumps([my_obj])
