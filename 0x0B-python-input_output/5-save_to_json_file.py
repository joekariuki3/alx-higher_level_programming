#!/usr/bin/python3

"""
get json module
"""
import json

"""
fuction that writes json string to a file
"""


def save_to_json_file(my_obj, filename):
    """
    write jsom string to a file
    """
    if filename == "":
        raise FileNotFoundError("please provide a filename")
    elif my_obj is None:
        print("Please provide object to {}".format(filename))
        return
    else:
        with open(filename, mode='w', encoding="utf-8") as MyFile:
            return MyFile.write(json.dumps(my_obj))
