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
        """declaro, valido, inicializo"""
        self.size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """reasigno __str__ con datos de square"""
        return f"[Square] {self.size}/{self.size}"
