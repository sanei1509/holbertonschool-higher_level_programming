#!/usr/bin/python3
"""
Module 1-square.py
Define a square with content
"""


class Square():
    """
    Instance attribute (private): size
    size: def __init__(self, new_size=0)
    """
    def __init__(self, new_size=0):
        self.__size = new_size
