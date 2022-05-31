#!/usr/bin/python3
"""
task 11
based on "10-student.py"
remplazar todos los atributos
de Student instance
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
                key: value for key, value in
                self.__dict__.items() if key in attrs
                }
        return self.__dict__

    def reload_from_json(self, json):
        """update all the attributtes of student"""
        for i in json:
            self.__dict__.update({i: json[i]})
