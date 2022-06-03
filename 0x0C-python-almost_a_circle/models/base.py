#!/usr/bin/python3
"""
Task 1 :
private class attr, constructor, validate
"""
import json


class Base:
    __nb_objects = 0
    """
    Clase base
    I need access to my class to modify private clas
    """
    def __init__(self, id=None):
        """"initialize"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """transform object py to json string"""
        if type(list_dictionaries) == list:
            if len(list_dictionaries) != 0 and list_dictionaries is not None:
                return json.dumps(list_dictionaries)
            else:
                return []
