#!/usr/bin/python3
"""
Task 7 - based on 6-base_geometry.py
create function validator of integer
"""


class BaseGeometry:
    """
    public instance method (def area(self):)
    public instance method def integer_validator:
    (genero errores y por último devuelvo VALUE)
    """
    def area(self):
        """area definida sin implementar"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checkeo si es un entero valido"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value
