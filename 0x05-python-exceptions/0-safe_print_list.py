#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    for element in my_list:
        try:
            print(element, end='')
            len += 1
        except IndexError:
            break
    print()
    return len
