#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format())
        return True
    except Exception as err:
        write(sys.stderr, err)
        return False
