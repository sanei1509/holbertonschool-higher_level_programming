#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy_dict = a_dictionary.copy()
    for element in copy_dict:
        if(copy_dict[element] == value):
            del a_dictionary[element]
    return(a_dictionary)
