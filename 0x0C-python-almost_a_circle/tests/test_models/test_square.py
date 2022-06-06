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