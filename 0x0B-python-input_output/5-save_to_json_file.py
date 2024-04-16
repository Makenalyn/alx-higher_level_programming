#!/usr/bin/python3
""" import the JSON module """
import json
""" fucntion writes an Object to a text file using JSON representation """


def save_to_json_file(my_obj, filename):
    """using with to open file """
    with open(filename, "w", encoding="utf-8") as f:
        data = f.write(json.dumps(my_obj))
