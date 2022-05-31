#!/usr/bin/python3
"""
task 6
- Crear objeto desde un JSON
"""
import json


def load_from_json_file(filename):
    """
    function que crea un objeto desde un JSON file
    leo el JSON con load / loads lee string -> dict
    """
    with open(filename, "r") as f:
        return json.load(f)
