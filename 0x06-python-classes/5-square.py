#!/usr/bin/python3
"""
This is a square module
it provides a simple square class
"""


class Square:
    """ class square has defination of it self
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer, otherwise raise a
    TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError
    exception with the message size must be >= 0
    Public instance method: def area(self):
    that returns the current square area
    Public instance method: def my_print(self):
    that prints in stdout the square with the character #:
    if size is equal to 0, print an empty line
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("\n")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
