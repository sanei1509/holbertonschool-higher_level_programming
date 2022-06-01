#!/usr/bin/python3
"""
task advanced 100
function que inserte una linea de texto
despúes de cada linea que contenga una específica
"""


def append_after(filename="", search_string="", new_string=""):
    """function insert line after search string received"""
    new_text = ""

    with open(filename, "r") as f:
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string

    with open(filename, "w") as f:
        f.write(new_text)
