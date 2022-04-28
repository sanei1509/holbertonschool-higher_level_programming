#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    if (argc == 0):
        print(argc, "arguments.")
    elif (argc == 1):
        print(argc, "argument:".format(sys.argv[0]))
    else:
        print(argc, "arguments:")
        for i in range(1, argc + 1):
            print("{}: {}".format(i, sys.argv[i]))
