#!/usr/bin/python3
"""
Advanced task 100 - create a class Myint
"""


class MyInt(int):
    """class with operators invertes"""
    def __eq__(self):
        return False

    def __ne__(self):
        return True
