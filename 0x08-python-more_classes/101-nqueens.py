#!/usr/bin/python3

import os

def getN():
    if len(os.sys.argv) == 2:
        n = os.sys.argv[1]
        if n.isdigit():
            n = int(n)
        else:
            print("N must be a number\n")
            exit(1)
        if n < 4:
            print("N must be at least 4")
            exit(1)
    else:
        print("Usage: nqueens N\n")
        exit(1)
getN()
