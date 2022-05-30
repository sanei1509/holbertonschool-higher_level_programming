#!/usr/bin/python3
"""
Task 8 - based on 7-base_geometry.py
instanciar (width) & (height) ya validados por nuestra function
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle inherit things of BaseGeometry:
    - used public instance method integer_validator()
    """
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
