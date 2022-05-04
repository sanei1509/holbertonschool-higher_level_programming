#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_mx = matrix.copy()
    for i in copy_mx:
        for j in i:
            print(copy_mx[0][0])
        return(copy_mx ** 2)
