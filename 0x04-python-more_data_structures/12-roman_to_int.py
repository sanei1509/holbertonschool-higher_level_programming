#!/usr/bin/python3

def symbols(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return 0


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    res = 0
    i = 0
    while (i < len(roman_string)):
        s1 = symbols(roman_string[i])
        if s1 == 0:
            return 0
        if (i + 1 < len(roman_string)):
            s2 = symbols(roman_string[i + 1])
            if (s1 >= s2):
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1

    return res
