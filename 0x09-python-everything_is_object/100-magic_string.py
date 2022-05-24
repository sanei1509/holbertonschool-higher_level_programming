#!/usr/bin/python3
def magic_string(cont=[0]):
    cont[0] += 1
    return str("BestSchool, " * (cont[0] - 1)) + "BestSchool"
