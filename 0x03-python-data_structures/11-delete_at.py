#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        if idx < 0 and idx >= len(my_list):
            return my_list
        else:
            for index, item in enumerate(my_list):
                if index == idx:
                    my_list.remove(item)
            return my_list
