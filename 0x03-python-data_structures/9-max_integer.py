#!/usr/bin/python3
def max_integer(my_list=[]):
    if(my_list == 0):
        return(None)
    else:
        big_value = my_list[0]
        for num in my_list:
            if (num > big_value):
                big_value = num
        return(big_value)
