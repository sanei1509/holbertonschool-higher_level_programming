#!/usr/bin/python3
"""
Task 10 - based on 9-base_geometry.py
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    create a class square que herede de Rectangle
    reasignando a sus valores correspondientes"""
    def __init__(self, size):
        """Inicialización y check con validator"""
        self.__size = self.integer_validator("size", size)
        """
        accedo a las inicializaciones heredadas
        y reasigno con valores correspondientes
        """
        super().__init__(self.__size, self.__size)
