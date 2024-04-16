#!/usr/bin/python3

""" imports json module """

import json

""" function returns JSON representation of an object 


    parameters - any object to be converted to json format

    Return:

        string rep of json
"""


def to_json_string(my_obj):
    return json.dumps([my_obj])
