#!/usr/bin/python3
"""
Task 4 -> 5-text_indentation.py
space then especific characters
"""


def text_indentation(text):
    """add text /n when ',' or ':'"""
    if type(text) != str:
        raise TypeError("text must be a string")

    ind_text = text.replace(". ", ".\n\n")
    ind_text2 = ind_text.replace("? ", "?\n\n")
    last_text = ind_text2.replace(": ", ":\n\n")
    print(last_text, end="")
