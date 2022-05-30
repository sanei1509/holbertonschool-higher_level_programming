#!/usr/bin/python3
"""
Task 6 - based on 5-base_geometry.py
"""


class BaseGeometry:
    """
    public instance method (def area(self):)
    """
    def area(self):
        """area definida sin implementar"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checkeo si es un entero valido"""
        if type(value) != int:
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
