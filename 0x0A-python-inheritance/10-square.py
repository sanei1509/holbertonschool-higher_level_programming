#!/usr/bin/python3
"""
Task 10 - based on 9-base_geometry.py
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle)
    """
    create a class square que herede de Rectangle
    reasignando a sus valores correspondientes
    """
    def __init__(self, size):
        """Inicializo"""
        self.size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
