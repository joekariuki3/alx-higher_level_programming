#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for pkey, pvalue in a_dictionary.items():
        if key == pkey:
            a_dictionary[pkey] = value
        else:
            a_dictionary[key] = value
