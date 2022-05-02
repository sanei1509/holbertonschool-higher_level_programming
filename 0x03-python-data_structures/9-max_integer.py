#!/usr/bin/python3
def max_integer(my_list=[]):
    if(my_list is None):
        return(None)

    big_value = 0
    for num in my_list:
        if (num > big_value):
            big_value = num
    return(big_value)
