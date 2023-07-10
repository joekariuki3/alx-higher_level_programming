#!/usr/bin/python3
def lookup(obj):
    """
    function to check available methods
    and attributes of a class
    """
    return list(dir(obj))
