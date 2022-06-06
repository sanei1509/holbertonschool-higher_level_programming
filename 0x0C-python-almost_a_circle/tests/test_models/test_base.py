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

    """METODOS / FUNCIONES"""
    def test_convert_to_jsonStr(self):
        """convierte a json string nuestra funcion ?"""
        instance1 = Rectangle(7, 2, 8, 2, 10)
        dict_data = instance1.to_dictionary()
        in_json = Base.to_json_string([dict_data])
        self.assertEqual(type(in_json), str)

    def test_load_from_file(self):
        """
        convierte un texto a obj desde un archivo ?
        """
        if os.path.exists("Base.json"):
            os.remove("Base.json")

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        salida_rectangle = Rectangle.load_from_file()
        self.assertEqual(salida_rectangle, [])

        salida_square = Square.load_from_file()
        self.assertEqual(salida_square, [])

        error = "load_from_file() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            Rectangle.load_from_file('Naruto file')

        self.assertEqual(error, str(e.exception))

    def test_save_to_file(self):
        """test save_to_file function"""
        err = "'Base' object has no attribute 'to_dictionary'"

        with self.assertRaises(AttributeError) as e:
            Base.save_to_file([Base(2)])
        self.assertEqual(err, str(e.exception))

    def test_err_json_string(self):
        """to_json_string receive empty or none"""
        empty_list = []
        in_json = Base.to_json_string(empty_list)
        self.assertEqual(in_json, [])

        empty_list = None
        data_json = Base.to_json_string(empty_list)
        self.assertEqual(data_json, [])
