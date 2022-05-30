#!/usr/bin/python3
"""
Task 4 - object isainstance of a subclass?
"""


def inherits_from(obj, a_class):
    """
    Checkeo si el objeto es una instancia de la subclase,
    no de la clase misma
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
