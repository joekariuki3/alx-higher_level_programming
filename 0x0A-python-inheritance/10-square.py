#!/usr/bin/python3
"""
simple class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    initialize the class Square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        calculate area of Square
        """
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
