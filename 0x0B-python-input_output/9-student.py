#!/usr/bin/python3
"""
task 9 -
- crear clase Student
-  instances : first_name, last_name, age
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

    def to_json(self):
        """
        function that return the dictionaryfor JSON serialization of an object
        """
        return obj.__dict__
