#!/usr/bin/python3
"""
MyList class that inherits from
another class list
"""


class MyList(list):
    """
    initialization of the class
    """
    def __init__(self):
        super().__init__()

    """
    fuction to print the list
    in assending order
    """
    def print_sorted(self):
        if not isinstance(self, list):
            raise TypeError("provide a list")
        elif self is None:
            raise TypeError("provide a list")
        print(sorted(self, reverse=False))
