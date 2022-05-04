#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key_exist in a_dictionary:
        if(key_exist == key):
            a_dictionary.update({key: value})
            return(a_dictionary)        
    a_dictionary.update({key: value})
    return(a_dictionary)
