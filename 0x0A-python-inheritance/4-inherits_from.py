#!/usr/bin/python3
"""
Task 4 - object isainstance of a subclass?
"""


def inherits_from(obj, a_class):
    """checkear si es una instancia de una clase heredada"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
