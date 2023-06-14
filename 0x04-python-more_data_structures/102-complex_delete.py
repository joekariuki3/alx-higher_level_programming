#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delKeys = []
    if value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if value == v:
                delKeys.append(k)
        for key in delKeys:
            del a_dictionary[key]
    return a_dictionary
