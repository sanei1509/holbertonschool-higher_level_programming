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

    @classmethod
    def save_to_file(cls, list_objs):
        """save list of objs(json string) in afile with variable name"""
        name_of_file = f"{cls.__name__}.json"

        print(name_of_file)
        list_algo = []

        if list_objs is not None and len(list_objs) != 0:
            for algo in list_objs:
                list_algo += [algo.to_dictionary()]

        json_list = Base.to_json_string(list_algo)

        with open(name_of_file, "w", encoding="UTF-8") as f:
            f.write(json_list)

    def from_json_string(json_string):
        """convert json string to object python"""
        if json_string is not None and len(json_string) != 0:
            return json.loads(json_string)
        else:
            return []
