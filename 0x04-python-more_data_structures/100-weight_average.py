#!/usr/bin/python3
def weight_average(my_list=[]):
    if(my_list is None):
        return(0)
    else:
        numerador = 0
        denominador = 0
        for tup in my_list:
            numerador += tup[0] * tup[1]
            denominador += tup[1]
        return (numerador / denominador)
