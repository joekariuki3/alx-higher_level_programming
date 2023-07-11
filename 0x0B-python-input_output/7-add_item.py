#!/usr/bin/python3
"""
get os module
get save_to_json_file fucntion
get load_from_json_file function
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
"""
function to add all arguments to a list
"""


def addToList():
    if len(sys.argv) > 1:
        Mylist = []
        i = 1
        filename = "add_item.json"
        while i < len(sys.argv):
            Mylist.append(sys.argv[i])
            i += 1
        save_to_json_file(Mylist, filename)
        load_from_json_file(filename)


addToList()
