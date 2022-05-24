#!/usr/bin/python3
"""
Task 4 -> 5-text_indentation.py
space then especific characters
"""


def text_indentation(text):
    """add text /n when ',' or ':'"""
    if type(text) != str:
        raise TypeError("text must be a string")
    texto = ""
    elementos = [".", "?", ":"]
    for i in text:
        texto += i
        if i in elementos:
            print("{}\n".format(texto.strip()))
            texto = ""
    print("{}".format(texto.strip()))
