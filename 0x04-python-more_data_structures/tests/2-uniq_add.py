#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    uni_nums = set(my_list)

    for num in uni_nums:
        res += num
    return(res)
