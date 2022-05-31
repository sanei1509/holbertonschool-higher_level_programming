#!/usr/bin/python3
"""
task 4
- From json to string Object
"""
import json


def from_json_string(my_str):
    """
    function que retorna un object python
    representado por una cadena JSON
    """
    return json.loads(my_str)
