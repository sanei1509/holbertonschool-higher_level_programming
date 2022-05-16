#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format())
        return True
    except (ValueError, TypeError):
        return False
