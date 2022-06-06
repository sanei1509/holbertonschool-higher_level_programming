#!/usr/bin/python3
"""
Tests for a class Rectangle (rectangle.py)
"""
import unittest
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class test_case(unittest.TestCase):
    """clase para pruebas"""

    """types"""
    def test_float(self):
        """width or height is float?"""
        Base.__nb_objects = 0
        with self.assertRaises(TypeError):
            Rectangle(2.1, 1, 2 , 5)

        with self.assertRaises(TypeError):
            Rectangle(2, 3.14, 4, 5)

    def test_Nan(self):
        """width or height is NaN"""
        Base.__nb_objects = 0
        with self.assertRaises(TypeError):
            Rectangle(float('NaN'), 1, 3, 5)

        with self.assertRaises(TypeError):
            Rectangle(2, float('NaN'), 2, 4)

    def test_dictionary(self):
        """check for dictionary"""
        r1 = Rectangle(5, 2, 1, 8)
        r1_dict = r1.to_dictionary()
        other_dict = {'x': 1, 'y': 8, 'id': 1, 'height': 2, 'width': 5}
        self.assertEqual(len(r1_dict), len(other_dict))
        self.assertEqual(type(r1_dict), dict)

    """AREA"""
    def test_area_values(self):
        """check area things"""
        r1 = Rectangle(2, 6)
        self.assertEqual(r1.area(), 12)
        r2 = Rectangle(12, 2)
        self.assertEqual(r2.area(), 24)
        r3 = Rectangle(5, 4, 1, 1, 10)
        self.assertEqual(r3.area(), 20)
        
    def test_arg_area(self):
        """error args"""
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, 6)

            r1.area("Holi")
        self.assertEqual("area() takes 1 positional argument but 2 were given", str(e.exception))

    