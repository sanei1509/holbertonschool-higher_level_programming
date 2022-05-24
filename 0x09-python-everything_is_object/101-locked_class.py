#!/usr/bin/python3
"""
Class LockedClass - solo permite crear una
instancia de atributo "first_name" al usuario
-> es el único caso permitido.
"""


class LockedClass:
    """
    CLase que controla la creación de atributos al usuario
    """
    __slots__ = ["first_name"]

    def __init__(self):
        pass
