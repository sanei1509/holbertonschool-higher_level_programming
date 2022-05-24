#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define class"""
    def test_is_mayor(self):
        """Succes cases"""
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([2, 2]), 2)
        self.assertEqual(max_integer([[9, 1], [5, 6], [4, 8]]), [9, 1])
        self.assertEqual(max_integer(["Naruto", "Neji"]), "Neji")
        self.assertEqual(max_integer(["abc", "zabc"]), "zabc")
        self.assertEqual(max_integer(["a", "b", "y"]), "y")
 
    def test_negative(self):
        "negative number"
        self.assertEqual(max_integer([-10, -7, 8]), 8)
        self.assertEqual(max_integer([-10, -7, -8]), -7)

    def test_error(self):
        "Test case of error"
        with self.assertRaises(TypeError):
            max_integer({1, 2})
        with self.assertRaises(TypeError):
            max_integer(2)

    def test_is_none(self):
        """Case None"""
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer([None]))



if __name__ == "__main__":
    unittest.main()
