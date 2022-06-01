#!/usr/bin/python3
"""
task 10
based on "9-student.py"
retornar solo los valores pasados en la lista
en un DICT
"""


class Student:
    """
    -Class student
    -intance three attributes
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        function that return the dictionaryfor JSON serialization of an object
        None - return all the dict

        """
        if attrs is not None:
            return {
                key: value for key, value
                in self.__dict__.items() if key in attrs
                }
        return self.__dict__
