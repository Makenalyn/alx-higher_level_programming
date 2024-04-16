#!/usr/bin/python3

""" imports json module """

import json

""" function returns JSON representation of an object """


def to_json_string(my_obj):
    print(json.dumps([my_obj]))
