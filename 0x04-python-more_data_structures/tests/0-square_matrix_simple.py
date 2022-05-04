#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def elev(lista):
        list_ret = list(map(lambda x: x**2, lista))
        return(list_ret)
    res_lista = list(map(elev, matrix))
    return(res_lista)
