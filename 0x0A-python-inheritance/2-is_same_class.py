#!/usr/bin/python3
"""
fuction that checks if object is instance of a class
or not
"""


def is_same_class(obj, a_class):
    """
    check if obj is instance of a_class
    """
    if obj is None or a_class is None:
        return False
    if isinstance(obj, a_class):
        return True
    if not isinstance(obj, a_class):
        return False
