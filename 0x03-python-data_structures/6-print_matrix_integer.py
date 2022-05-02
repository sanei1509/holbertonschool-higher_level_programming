#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for columna in range(len(matrix[0])):
        for fila in range(len(matrix)):
            print(matrix[columna][fila], end=" ")
        print()
