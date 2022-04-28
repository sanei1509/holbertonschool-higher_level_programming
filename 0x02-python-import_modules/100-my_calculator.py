#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argc = (len(sys.argv) - 1)
    argv = sys.argv
    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if (argc != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif (op != "+" and op != "-" and op != "*" and op != "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if (op == '+'):
            print(a, "+", b, "=", add(a, b))
        elif (op == '-'):
            print(a, "-", b, "=", sub(a, b))
        elif (op == '*'):
            print(a, '*', b, "=", mul(a, b))
        elif (op == '/'):
            print(a, "/", b, "=", div(a, b))
