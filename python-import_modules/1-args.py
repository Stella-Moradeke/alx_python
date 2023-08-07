#!/usr/bin/python
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    args = sys.argv[1:]

    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, "s" if argc > 1 else ""))
        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))