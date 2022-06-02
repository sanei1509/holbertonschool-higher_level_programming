#!/usr/bin/python3
"""
Task 1 :
private class attr, constructor, validate
"""


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
