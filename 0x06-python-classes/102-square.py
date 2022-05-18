#!/usr/bin/python3
"""
class Square define a square for: 4-square.py
"""


class Square:
    """
    Instance attribute (private): size
    size: def __init__(self, new_size=0):
    @property def size(self): recuperar tamaño
    @size.setter def size(self, value): setear tamaño
    """

    def __init__(self, size=0):
        """Initialize the square"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        """return the area of the square"""
        return (self.__size * self.__size)

    def __eq__(self, o_square):
        """igual """
        return self.area() == o_square.area()
        """!igual"""
    def __ne__(self, o_square):
        return self.area() != o_square.area()
        """mayor que ->"""
    def __gt__(self, o_square):
        return self.area() > o_square.area()
        """mayor o igual que"""
    def __ge__(self, o_square):
        return self.area() >= o_square.area()
        """menor que ->"""
    def __lt__(self, o_square):
        return self.area() < o_square.area()
        """menor o igual que"""
    def __le__(self, o_square):
        return self.area() <= o_square.area()
