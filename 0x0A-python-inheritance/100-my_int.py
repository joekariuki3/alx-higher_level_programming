#!/usr/bin/python3
"""
simple MyInt class it inherits from int
"""


class MyInt(int):
    """
    call super fuctions to be used with our
    custom functions
    """
    def __eq__(self, num):
        """ check for equality using super function"""
        return super().__eq__(num)

    def __ne__(self, num):
        """ checks for not equal to using super function """
        return super().__ne__(num)
