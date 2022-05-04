#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key_exist in a_dictionary:
        if(key_exist == key):
            a_dictionary[key] = value
            print(f"{key_exist}: {a_dictionary.get(key_exist)}")
        else:
            a_dictionary[key] = value
