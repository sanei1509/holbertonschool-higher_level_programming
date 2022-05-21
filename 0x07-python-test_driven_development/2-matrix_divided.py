#!/usr/bin/python3
"""
Task 1 - matrix_divided(matrix, div):
"""
def matrix_divided(matrix, div):
"""function that divide all the values of the matrix"""
    res = []
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) != len(matrix(1)):
        raise TypeError("Each row of the matrix must have the same size")
    if div = 0:
        raise ZeroDivisionError("division by zero")

    for listas_valores in matrix:
       for i in lista_valores:
           if type(i)) != int and type(i) != float:
               rais TypeError("matrix must be a matrix (list of lists) of integers/floats")
