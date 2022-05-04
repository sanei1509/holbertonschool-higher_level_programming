#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for element in a_dictionary:
        new_dict[element] = int(a_dictionary[element])*2
    return(new_dict)
