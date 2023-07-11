#!/usr/bin/python3
"""
Fuction that reads a file and prins its contents
"""


def read_file(filename=""):
    """
    read a file and print contents
    to stdout
    """
    if filename != "":
        with open(filename, encoding='utf-8') as MyFile:
            for line in MyFile:
                print("{}".format(line.rstrip()))
    else:
        raise FileNotFoundError("please provide a file name")
