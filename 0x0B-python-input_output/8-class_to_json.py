#!/usr/bin/python3
"""
function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    class to json
    """

    if isinstance(obj, (str, int, bool)):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {class_to_json(key): class_to_json(value)
                for key, value in obj.items()}
    elif hasattr(obj, '__dict__'):
        return {key: class_to_json(value)
                for key, value in obj.__dict__.items()}
    else:
        return None
