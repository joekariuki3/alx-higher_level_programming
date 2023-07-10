#!/usr/bin/python3
"""
function that returns True if the object is
an instance of a class that inherited
(directly or indirectly) from the specified class
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    true if is subclass else False
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
