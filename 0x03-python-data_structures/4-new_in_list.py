#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_cp = my_list.copy()
    if (idx < 0 or idx > len(my_list)):
        return my_list
    else:
        list_cp[idx] = element
        return list_cp
