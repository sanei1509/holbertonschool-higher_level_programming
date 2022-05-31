#!/usr/bin/python3
"""
task 7
- Agregar todos los argumentos a una lista py
()
y guardarlos en un archivo
"""
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

args = list(sys.argv[1:])

try:
    load_from_json_file("add_item.json")

except Exception:
    args_data = []

args_data.extend(args)
save_to_json_file(args_data, "add_item.json")
