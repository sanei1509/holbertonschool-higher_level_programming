#!/usr/bin/python3
"""
task 12
print a pascal triangle
"""


# Print Pascal's Triangle in Python

def pascal_triangle(n):
    new_list = []
    cont = 0

    if n <= 0:
        return []

    for i in range(1, n+1):
        print('[', end='')
        cont += 1
        for j in range(0, n-i+1):
            print(end='')

        C = 1

        for j in range(1, i+1):

            """el primer valor de la línea siempre es 1"""
            if C not in [1]:
                print('', end='')
            print(C, sep='', end='')
            """Coeficiente binomial"""
            C = C * (i - j) // j
            print(',', end="")
        print(']', end='')
        print()
    return[]
