#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argc = len(sys.argv) - 1
    argv = sys.argv

    if(argc != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if(argv[2] == "+"):
            print(a, "+", b, "=", add(a, b))
        elif(argv[2] == "-"):
            print(a, "-", b, "=", sub(a, b))
        elif(argv[2] == "*"):
            print(a, "*", b, "=", mul(a, b))
        elif(argv[2] == "/"):
            print(a, "/", b, "=", div(a, b))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
