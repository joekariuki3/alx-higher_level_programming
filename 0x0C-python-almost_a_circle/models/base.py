#!/usr/bin/python3
"""
class Base
"""
import json

class Base():
    """
    declare private class atribute
    """

    __nb_objects = 0

    """
    initiate class base
        Arguments
        @id: is int
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
          
