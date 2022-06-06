#!/usr/bin/python3
"""
Tests for a class Base (base.py)
"""
import unittest
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class test_case(unittest.TestCase):
    """clase para pruebas"""

    """types"""
    def test_lista(self):
        """id is a list?"""
        b1 = Base([1, 2])
        self.assertEqual(b1.id, [1, 2])

    def test_tupla(self):
        """id is a tuple?"""
        b1 = Base((1, 2))
        self.assertEqual(b1.id, (1, 2))

    def test_NotAnumber(self):
        """id is NaN?"""
        b1 = Base(float('NaN'))
        self.assertNotEqual(b1.id, float("NaN"))

    def test_dict(self):
        """id is a dictionary?"""
        b1 = Base({"uno": 1, "dos": 2})
        self.assertEqual(b1.id, {"uno": 1, "dos": 2})

    def test_negative(self):
        """id is negative ?"""
        b1 = Base(-2)
        self.assertEqual(b1.id, -2)
    
    def test_str(self):
        """id is a string ?"""
        b1 = Base("naruto")
        self.assertEqual(b1.id, "naruto")

    def test_bool(self):
        """id is TRUE || FALSE ? """
        b1 = Base(False)
        self.assertEqual(b1.id, False)


    """argumentos"""
    def test_2args(self):
        """id have two args?"""
        with self.assertRaises(TypeError):
            Base(1, 2)
 
    def test_none(self):
        """id no recibe argumentos?"""
        b1 = Base(None)
        self.assertEqual(b1.id, 2)

    """clase de instancia(BASE)"""
    def test_base_class(self):
        """es una instancia de Base?"""
        b1 = Base()
        self.assertEqual(type(b1), Base)
