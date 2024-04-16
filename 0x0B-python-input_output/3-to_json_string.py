#!/usr/bin/python3
import json

""" function returns JSON representation of an onject """


def to_json_string(my_obj):

    """ doesn't manage exceptions

    parameter: object needing to be repsented
    """
    return json.dumps(my_obj)
