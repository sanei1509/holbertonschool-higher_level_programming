#!/usr/bin/python3
"""
task 2
- append a string to a textfile
"""


def append_write(filename="", text=""):
    """function that append a string to a file"""
    with open(filename, "a") as f:
        chars = f.write(text)
        return chars
