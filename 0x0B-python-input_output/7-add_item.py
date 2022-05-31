#!/usr/bin/python3
"""
task 7
- Agregar todos los argumentos a una lista py
()
y guardarlos en un archivo.. con permisos suficientes
"""
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

args = list(sys.argv[1:])

try:
    load_from_json_file("add_item.json")

except FileNotFoundError:
    args_data = []

save_to_json_file(args_data + args, "add_item.json")
