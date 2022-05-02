#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for columna in range(len(matrix[0])):
        for fila in range(len(matrix[columna])):
            print(matrix[columna][fila], end="")
            if (fila < len(matrix[columna]) - 1):
                print(" ", end="")
        print()
