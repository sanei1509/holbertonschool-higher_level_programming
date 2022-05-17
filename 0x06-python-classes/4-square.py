#!/usr/bin/python3
"""
class Squar define a square for: 3-square.py
"""


class Square:
    """
    Instance attribute (private): size
    size: def __init__(self, new_size=0):
    property def size(self): recuperar tamaño
    setter def size(self, value): setear tamaño
    """

    def __init__(self, size=0):
        self.__size = size
        if (type(self.__size) != int):
            raise TypeError("size must be a integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if (type(self.__size) != int):
            raise TypeError("size must be an integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size * self.__size)
