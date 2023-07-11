#!/usr/bin/python3
"""
fuction that writes content to a file
"""


def write_file(filename="", text=""):
    """
    write text to filename if all not = ""
    """
    if filename == "":
        raise FileNotFoundError("please provide a filename")
    elif text == "":
        print("Please provide text to write to {}".format(filename))
        return
    else:
        with open(filename, mode='w', encoding="utf-8") as MyFile:
            return MyFile.write(text)
