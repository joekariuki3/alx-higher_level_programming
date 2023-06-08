#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv)
    answer = 0
    i = 1
    while i < argc:
        answer = answer + int(argv[i])
        i = i + 1
    print("{:d}".format(answer))
