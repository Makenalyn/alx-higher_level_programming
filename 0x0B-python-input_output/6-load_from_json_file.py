#!/usr/bin/python3
""" imports a json file to load from json"""
import json
from io import StringIO

""" from json to load """


def load_from_json_file(filename):
    with open(filename, encoding="utf-8") as f:
        obj = f.write(json.loads(filename))
