#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argc = len(sys.argv)
    argv = sys.argv
    op = argv[2]

    if argc is not 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in operators:
	print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if op is "+":
             print(a, "+", b, "=", add(a, b))
	elif op is "-":
             print(a, "-", b, "=", sub(a, b))
	elif op is "*":
             print(a, "*", b, "=", mul(a, b))
	elif op is "/":
              print(a, "/", b, "=", div(a, b))
