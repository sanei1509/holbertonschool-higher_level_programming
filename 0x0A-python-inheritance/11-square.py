#!/usr/bin/python3
"""
Task 11 - inherit 9-rectangle, based on 10-base_geometry.py
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    class Square inherit of the rectangle
    (IMPORT) si quisiera importarlo -> __import__(9_rectangle).Rectangle
    """
    def __init__(self, size):
        """valido, inicializo"""
        self.__size = self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """reasigno __str__ con datos de square"""
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
