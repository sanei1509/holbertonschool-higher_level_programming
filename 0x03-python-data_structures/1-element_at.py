#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0 or idx > len(my_list)):
        return None
    elif (type(my_list) is list):
        return int(my_list[idx])
