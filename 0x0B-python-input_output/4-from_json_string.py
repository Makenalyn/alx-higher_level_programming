#!/usr/bin/python3
""" functions returns ab object represented by a json string """
import json

def from_json_string(my_str):
    return json.loads(my_str) 
