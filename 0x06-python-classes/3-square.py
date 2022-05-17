#!/usr/bin/python3
"""
class Square define a square for: 2-square.py
"""


class Square:
    """
    Instance attribute (private): size
    size: def __init__(self, new_size=0):
    """
    def __init__(self, size=0):
        """Initialize the square"""
        self.__size = size

    def area(self):
        """return the area of the square"""
        return (self.__size * self.__size)
