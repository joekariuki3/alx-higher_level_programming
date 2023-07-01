#!/usr/bin/python3
def add_integer(a, b=98):
    """
    function to add two numbers

    if a is not a int or float raise TypeError
    if b is not a int or float raise TypeError
    if a is not a is float convert to int
    if b is not a is float convert to int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
