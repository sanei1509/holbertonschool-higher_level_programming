#!/usr/bin/python3
"""
new Class that inherits from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    this inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(s):
        return (
            f"[Square] ({s.id}) {s.x}/{s.y} - {s.width}"
        )

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size to width and height"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """function to assing newly attrs"""
        i = 0
        if args is not None and len(args) != 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        else:
            if kwargs is not None and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    if key == "size":
                        self.width = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value
