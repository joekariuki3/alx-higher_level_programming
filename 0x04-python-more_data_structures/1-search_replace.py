#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    return [replace if n == search  else n for n in my_list]
