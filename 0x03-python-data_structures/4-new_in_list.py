#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        index = 0
        while index < len(my_list):
            new_list.append(my_list[index])
            index = index + 1
        new_list[idx] = element
        return new_list
