#!/usr/bin/python3
"""
Tests for a class Square (square.py)
"""
import unittest
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class Test_case(unittest.TestCase):
    """clase para pruebas"""
    def test_normal(self):
        """size of Square"""
        s1 = Square(2)
        self.assertEqual(s1.size, 2)

    """test funciones / metodos"""
    def test_area(self):
        """test area method"""
        t1 = Square(3, 3)
        self.assertEqual(t1.area(), 9)

    def test_update_kwargs(self):
        """test a part of update"""
        t1 = Square(10, 10, 10, 10)
        t1.update(id = 5)
        self.assertEqual(str(t1), "[Square] (5) 10/10 - 10")

    def test_str_func(self):
        """Probando la función __str__"""
        t1 = Square(10)
        self.assertEqual(str(t1), "[Square] (3) 0/0 - 10")

        t1 = Square(10, 6)
        self.assertEqual(str(t1), "[Square] (4) 6/0 - 10")

        t1 = Square(10, 5, 9)
        self.assertEqual(str(t1), "[Square] (5) 5/9 - 10")

        t1 = Square(5, 10, 4, 14)
        self.assertEqual(str(t1), "[Square] (14) 10/4 - 5")

    """Error cases"""
    def test_type_errors(self):
        """checkear los casos errores de tipo"""
        with self.assertRaises(TypeError):
            test1 = Square()
        with self.assertRaises(TypeError):
            test1 = Square("Naruto")
        with self.assertRaises(TypeError):
            test1 = Square([2, 4])
        with self.assertRaises(TypeError):
            test1 = Square((2, 4))
        with self.assertRaises(TypeError):
            test1 = Square(True)
        with self.assertRaises(TypeError):
            test1 = Square(2, "Holaaa")
        with self.assertRaises(TypeError):
            test1 = Square(5, [2, 3])
        with self.assertRaises(TypeError):
            test1 = Square(5, (5, 5))
        with self.assertRaises(TypeError):
            test1 = Square(5, False)
        with self.assertRaises(TypeError):
            test1 = Square(5, {'hola': 4})
        with self.assertRaises(TypeError):
            test1 = Square(2, 2, [2, 2])
    
    def test_value_errors(self):
        """chequear los casos de value error"""
        with self.assertRaises(ValueError):
            test1 = Square(1, -10)
        with self.assertRaises(ValueError):
            test1 = Square(2, 2, -33)
        with self.assertRaises(ValueError):
            test1 = Square(0)
        with self.assertRaises(ValueError):
            test1 = Square(-20)             