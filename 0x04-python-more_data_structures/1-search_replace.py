#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res_list = []
    for i in my_list:
        if (i != search):
            res_list.append(i)
        else:
            res_list.append(replace)
    return (res_list)
