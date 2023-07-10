#!/usr/bin/python3
"""
fuction to add atribute to an object
"""


def add_attribute(obj, attr_name, attr_value):
    """
    add atr to an object
    """

    if hasattr(obj, '__dict__'):
        obj.__setattr__(attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
