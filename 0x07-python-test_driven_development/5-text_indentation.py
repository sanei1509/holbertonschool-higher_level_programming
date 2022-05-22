#!/usr/bin/python3
""" 
Task 4 -> 5-text_indentation.py
space then especific characters
"""
def text_indentation(text):
    """add text /n when ',' or ':'"""
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if (text[i] == '.' and (i != 0 and i != len(text) - 1)):
            print("{}".format(text[i+1]), end="\n")
            print()
        if (text[i] == ':' and (i != 0 and i != len(text) - 1)):
            print("{}".format(text[i+1]), end="\n")
            print()
        if (text[i] == '?' and (i != 0 and i != len(text) - 1)):
            print("{}".format(text[i+1]), end="\n")
            print()
        else:
            print("{}".format(text[i]), end="")
