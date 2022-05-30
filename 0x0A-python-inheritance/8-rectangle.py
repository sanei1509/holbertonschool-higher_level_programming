#!/usr/bin/python3
"""
Task 8 - based on 7-base_geometry.py
"""


class BaseGeometry:
    """
    public instance method (def area(self):)
    public instance method (def integer_validator(self, name, value):)
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checkear si value es un entero"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    class Rectangle inherit things of BaseGeometry:
    - used public instance method integer_validator()
    """
    def __init__(self, width, height):
        self.__width = self.integer_validator("height", width)
        self.__height = self.integer_validator("width", height)
