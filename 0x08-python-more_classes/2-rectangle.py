#!/usr/bin/python3
"""
Task 2-rectangle.py by (1-rectangle.py)
Create two private instances attributes:
"""


class Rectangle():
    """
    Attribute (private): width
    Attribute (private): height
    @property(height) - retrieve value
    @height.setter - set the value
    @property(width) - retrieve value
    @width.setter - set the value
    """

    def __init__(self, width=0, height=0):
        """Initialize"""
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__width = value

    def area(self):
        """return the rectangle area"""
        return(self.__height * self.__width)

    def perimeter(self):
        """return the rectangle perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (self.__width * 2 + self.__height * 2)
