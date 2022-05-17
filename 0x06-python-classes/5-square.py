#!/usr/bin/python3
"""
class Square define a square for: 4-square.py
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
        if (type(size) != int):
            raise TypeError("size must be a integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

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
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size < 0):
            print()
        else:
            for n in range(self.__size):
                for y in range(self.__size):
                    print('#', end="")
                print()
