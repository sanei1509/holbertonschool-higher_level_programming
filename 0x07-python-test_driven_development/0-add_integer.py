#!/usr/bin/python3
"""
Task 0 - module add_integers(a, b)
"""


def add_integer(a, b=98):
    """function that return a( int/float ) + b( int/float )"""
    if type(a) != int or type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int or type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
