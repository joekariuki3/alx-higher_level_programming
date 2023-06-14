#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary.keys():
        x = {key: value}
        a_dictionary.update(x)
    else:
        a_dictionary = (key, value)
