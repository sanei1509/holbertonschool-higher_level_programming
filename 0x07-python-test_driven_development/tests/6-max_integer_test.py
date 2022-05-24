#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define class"""
    def test_is_mayor(self):
        """Succes cases"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([2, 2]), 2)
        self.assertEqual(max_integer([[9, 1], [5, 6], [4, 8]]), [6, 1])        

    def test_is_none(self):
        """Case None"""
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer([None]))

if __name__ == "__main__":
    unittest.main()
