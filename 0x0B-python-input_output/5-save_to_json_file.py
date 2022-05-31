#!/usr/bin/python3
"""
task 5
- Guardar un objeto en un archivo
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function que mete un objeto en un archivo
    en un archivo determinado
    """
    with open(filename, "w") as f:
        """o tambien podria redireccionar con dumps"""
        f.write(json.dumps(my_obj))
