#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_sum = set_1.union(set_2)
    set_common = set_1.intersection(set_2)
    set_diff = set_sum - set_common
    return(set_diff)
