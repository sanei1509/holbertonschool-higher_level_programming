#!/usr/bin/python3
"""
Advanced task 100 - create a class Myint
"""


class MyInt(int):
    """class with operators inverted"""
    def __init__(self, value):
        """inicializo"""
        self.value = value

    def __eq__(self, value):
        """!="""
        return False

    def __ne__(self, value):
        """=="""
        return True
