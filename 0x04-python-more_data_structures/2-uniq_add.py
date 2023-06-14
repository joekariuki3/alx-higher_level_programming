#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return None
    new_list = set(my_list)
    answer = 0
    for i in new_list:
        answer = answer + i
    return answer
