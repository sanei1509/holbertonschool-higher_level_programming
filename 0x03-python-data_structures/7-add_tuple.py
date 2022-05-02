#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res_tupla = ()

    len_tup1 = len(tuple_a)
    len_tup2 = len(tuple_b)
    suma1 = 0
    suma2 = 0
    if (len_tup1 < 2):
        while (len_tup1 < 2):
            tuple_a = tuple_a + (0,)
            len_tup1 += 1
    if (len_tup2 < 2):
        while (len_tup2 < 2):
            tuple_b += (0,)
            len_tup2 += 1

    suma1 = tuple_a[0] + tuple_b[0]
    res_tupla += (suma1,)
    suma2 = tuple_a[1] + tuple_b[1]
    res_tupla += (suma2,)
    return (res_tupla)
