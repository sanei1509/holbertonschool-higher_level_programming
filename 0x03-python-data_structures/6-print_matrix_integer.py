#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for columna in matrix:
        len_col = len(columna)
        cont_fila = 0
        for fila in columna:
            print(f"{fila:d}", end='')
            if cont_fila < (len_col - 1):
                print(' ', end='')
            cont_fila += 1
        print("")
