#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    if argc == 0:
        print("{:d} arguments.".format(argc))
    if argc >= 1:
        if argc == 1:
            print("{:d} argument:".format(argc))
        else:
            print("{:d} arguments:".format(argc))
        i = 1
        while i <= argc:
            print("{:d}: {}".format(i, argv[i]))
            i = i + 1
