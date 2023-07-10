#!/usr/bon/python3
"""
returns True if the object is an instance of or
if the object is an instance of a class that inherited from,
"""


def is_kind_of_class(obj, a_class):
    """
    check if obj is an instance of a_class
    """
    return isinstance(obj, a_class)
