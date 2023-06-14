#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) or roman_string is None:
        return 0
    else:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for char in roman_string:
            if char in values.keys():
                result = result + values[char]
            else:
                result = result + 0
        return result
