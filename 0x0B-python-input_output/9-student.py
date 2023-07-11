#!/usr/bin/python3

"""
simple student class
"""


class Student():
    """ initiate the class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation of
        a Student instance
        """
        return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
