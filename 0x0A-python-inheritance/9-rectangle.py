#!/usr/bin/python3
"""
Task 9 - based on 7-base_geometry.py
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
        self.__width = width
        self.__height = height

    def width(self):
        self.integer_validator("width", width)

    def height(self):
        self.integer_validator("height", height)

    def area(self):
        """calculate area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
