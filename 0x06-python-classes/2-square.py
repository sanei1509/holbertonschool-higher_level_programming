#!/usr/bin/python3
"""
class Squar define a square for: 1-square.py
"""


class Square:
    """
    Instance attribute (private): size
    size: def __init__(self, new_size=0):
    """
    def __init__(self, new_size=0):
        self.__size = new_size
        if (type(self.__size) != int):
            raise TypeError("size must be an integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")
