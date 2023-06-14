#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    elif not search or not replace:
        return (my_list)
    new_list = []
    for num in my_list:
        if num == search:
            new_list.append(replace)
        else:
            new_list.append(num)
    return new_list
