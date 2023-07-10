#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry():
    """
    initialize the class
    """
    def __init__(self):
        pass

    def area(self):
        """
        calculate area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates the value passed
        """
        if isinstance(name, string):
            if not isinstance(value, int):
                raise TypeError("{} must be an integer".format(name))
            if value < 1:
                raise ValueError("{} must be greater than 0".format(name))
        else:
            raise TypeError("name is required")
