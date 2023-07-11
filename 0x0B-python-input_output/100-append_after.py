#!/usr/bin/python3
"""
function that inserts a line of text to a file
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    look for a string in a line if present
    append new_string after it
    """
    if filename != "" or search_string != "" or new_string != "":
        with open(filename, mode="r", encoding="utf-8") as myfile:
            text = myfile.readlines()
        with open(filename, mode="w", encoding="utf-8") as myfile:
            for line in text:
                if search_string in line:
                    line = line + new_string
                myfile.write(line)
