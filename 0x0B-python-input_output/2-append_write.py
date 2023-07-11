#!/usr/bin/python3
"""
fuction that appends content to a file
"""


def append_write(filename="", text=""):
    """
    append text to filename if all not = ""
    """
    if filename == "":
        raise FileNotFoundError("please provide a filename")
    elif text == "":
        print("Please provide text to append to {}".format(filename))
        return
    else:
        with open(filename, mode='a', encoding="utf-8") as MyFile:
            return MyFile.write(text)
