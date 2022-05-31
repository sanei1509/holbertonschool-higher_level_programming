#!/usr/bin/python3
"""
task 3
- write a function that returns the JSON
"""
import json


def to_json_string(my_obj):
    """function that return the JSON representation"""
    return json.dumps(my_obj)
