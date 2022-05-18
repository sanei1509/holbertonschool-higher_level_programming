#!/usr/bin/python3
"""
Task 6-rectangle.py by (5-rectangle.py)
Print a Rectangle
"""


class Rectangle:
    number_of_instances = 0
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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """print rectangle with str function"""
        string = ""
        if (self.__width == 0 or self.__height == 0):
            return string
        else:
            for largo in range(self.__height):
                for ancho in range(self.__width):
                    string += "#"
                string += "\n"
            return string[:-1]

    def __repr__(self):
        """return in stdout a rectangle"""
        return f"Rectangle({self.__height}, {self.__width})"

    def __del__(self):
        "print a message when delete a class"
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
