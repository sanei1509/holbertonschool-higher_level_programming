#!/usr/bin/python3
"""
Task 1 - matrix_divided(matrix, div):
"""
def matrix_divided(matrix, div):
    """function that divide all the values of the matrix"""
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    results_matrix = []
    for listas in matrix:
        if type(listas) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        c_resList = []
        for valor in listas:
           if type(valor) != int and type(valor) != float:
               raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
           c_resList.append(round(valor/div, 2))
        results_matrix.append(c_resList)
    return results_matrix
           




