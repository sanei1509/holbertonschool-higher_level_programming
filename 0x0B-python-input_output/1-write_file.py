#!/usr/bin/python3
"""
task 1
- create a file if not create and write
"""


def write_file(filename="", text=""):
    """function that write a file and return num of characters"""
    with open(filename, "w") as f:
        chars = f.write(text)
        return chars
