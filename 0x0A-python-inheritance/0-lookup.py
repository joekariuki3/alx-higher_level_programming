#!/usr/bin/python3
"""
lookup contets of a class
function to check available methods
and attributes of a class
"""


def lookup(obj):
    """
    returns a list of all the methods
    and atributes of class
    """
    return list(dir(obj))
