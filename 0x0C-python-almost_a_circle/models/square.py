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