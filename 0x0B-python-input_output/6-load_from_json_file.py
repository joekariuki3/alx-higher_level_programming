#!/usr/bin/python3

"""
get json module
"""
import json

"""
function that creates an object from file
"""


def load_from_json_file(filename):
    """
    create object from file
    """
    if filename == "":
        raise FileNotFoundError("please provide a filename")
    else:
        with open(filename, mode='r', encoding="utf-8") as MyFile:
            return json.loads(MyFile.read())
