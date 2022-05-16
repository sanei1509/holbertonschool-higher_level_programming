#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list:
            print(i)
    except(ValueError, TypeError):
        print("Error de rango")
