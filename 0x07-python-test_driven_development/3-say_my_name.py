#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    function to print name passed to it
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name == "":
        return "My name is " + first_name
    return "My name is " + first_name + " " + last_name
