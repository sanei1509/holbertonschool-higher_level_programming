#!/usr/bin/python3
"""
task 0
- reads a text file
"""


def read_file(filename=""):
    """function that read a file line per line"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
