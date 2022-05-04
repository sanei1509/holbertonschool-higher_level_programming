#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key_exist in a_dictionary:
        if(key_exist == key):
            a_dictionary[key] = value
        else:
            a_dictionary[key] = value
    return(a_dictionary)
