#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_val = max(a_dictionary.values())
    max_kay = ''
    for key, value in a_dictionary.items():
        if value == max_val:
            max_key = key
    return max_key
