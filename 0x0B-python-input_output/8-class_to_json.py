#!/usr/bin/python3
"""
task 8 - de Clase a JSON
funcion que devuelve diccionario
"""


def class_to_json(obj):
    """
    function that return the dictionary
    for JSON serialization of an object
    """
    return obj.__dict__
