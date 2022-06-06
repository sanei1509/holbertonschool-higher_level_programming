#!/usr/bin/python3
"""
Task 2:
-write a class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    class inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """validate and set the value width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """validate and set the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """validate and set value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """display the rectangle"""
        for pos_y in range(self.__y):
            print()
        for largo in range(self.__height):
            for pos_x in range(self.__x):
                print(" ", end="")
            for ancho in range(self.__width):
                print("#", end="")
            print()

    def __str__(s):
        """representation of rectangle"""
        return (
            f"[Rectangle] ({s.id}) {s.__x}/{s.__y} - {s.__width}/{s.__height}"
            )

    def update(self, *args, **kwargs):
        """function to assing newly attrs"""
        i = 0
        if args is not None and len(args) != 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.__width = arg
                if i == 2:
                    self.__height = arg
                if i == 3:
                    self.__x = arg
                if i == 4:
                    self.__y = arg
                i += 1
        else:
            if kwargs is not None and len(kwargs) != 0:
                for key, value in kwargs.items():
                    """print(f"{key}:{value}")"""
                    if key == "id":
                        self.id = value
                    if key == "width":
                        self.width = value
                    if key == "height":
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    def to_dictionary(self):
        """__dict__ representation of rectangle"""
        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x, "y": self.__y}
