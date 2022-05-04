#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for element in sorted(a_dictionary):
        print(f"{element}: {a_dictionary.get(element)}")
