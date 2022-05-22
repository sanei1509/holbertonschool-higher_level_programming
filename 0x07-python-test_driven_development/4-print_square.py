#!/usr/bin/python3
def print_square(size):
    """print a square with the caracter '#' """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for altura in range(size):
        for ancho in range(size):
            print("#",  end="")
        print()
