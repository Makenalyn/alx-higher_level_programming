#!/usr/bin/python3
""" imports from json file"""
import json
""" returns dict description with simple data structure """


def class_to_json(obj):
    return (dir(json.dumps(obj)))
