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
    def test_normal_id(self):
        """Testeando casos normales correctos"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        r3 = Rectangle(1, 2, 3, 4, 15)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 15)
    
    def test_width_height(self):
        """testeando valores de width y height"""
        r1 = Rectangle(2, 2)
        r2 = Rectangle(4, 4)

        self.assertEqual(r1.width, 2)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 4)      

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

    """Chequeo privacidad de atributos"""
    def test_private_attr(self):
        """son nuestro atributos privados?"""
        self.assertFalse(hasattr(Rectangle, "__x"))
        self.assertFalse(hasattr(Rectangle, "__y"))
        self.assertFalse(hasattr(Rectangle, "__height"))
        self.assertFalse(hasattr(Rectangle, "__width"))

    """Funciones / Metodos"""
    def test_update(self):
        """check update function"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_print(self):
        """print of rectangle - heredado"""
        r = Rectangle(1, 2, 3, 4, 10)
        self.assertEqual(str(r), '[Rectangle] (10) 3/4 - 1/2') 

    def test_to_dictionary(self):
        """
        Test method: to_dictionary
        """
        dic = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertEqual(type(dic), dict)
        r2 = Rectangle(10, 10)
        r2.update(**dic)
        self.assertEqual(str(r2), '[Rectangle] (5) 3/4 - 1/2')

    """Test Errors"""
    def test_update_err(self):
        """casos de errror funcion update"""
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as e:
            r1.update('veinte')
        self.assertEqual("id must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r1.update(id='Naruto')
        self.assertEqual("id must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r1.update(height=5, x=5, width="hola")
        self.assertEqual("width must be an integer", str(e.exception))
    
    """Diferentes tests sobre atributos"""
    def test_inheritance(self):
        """chequeo de herencias"""
        r1 = Rectangle(7, 3)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))
        self.assertTrue(isinstance(r1, Base))

    def test_type_errors(self):
        """chequeo de errores de tipo"""
        with self.assertRaises(TypeError):
            test1 = Rectangle()
        with self.assertRaises(TypeError):
            test1 = Rectangle("Naruto")
        with self.assertRaises(TypeError):
            test1 = Rectangle([2, 4])
        with self.assertRaises(TypeError):
            test1 = Rectangle((2, 4))
        with self.assertRaises(TypeError):
            test1 = Rectangle(True)
        with self.assertRaises(TypeError):
            test1 = Rectangle(2, "Holaaa")
        with self.assertRaises(TypeError):
            test1 = Rectangle(5, [2, 3])
        with self.assertRaises(TypeError):
            test1 = Rectangle(5, (5, 5))
        with self.assertRaises(TypeError):
            test1 = Rectangle(5, False)
        with self.assertRaises(TypeError):
            test1 = Rectangle(5, {'hola': 4})
        with self.assertRaises(TypeError):
            test1 = Rectangle(2, 2, [2, 2])
