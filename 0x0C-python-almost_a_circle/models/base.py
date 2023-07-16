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
        """ turn dictionary to json """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        jsonToSave = []
        jsonToSaveString = "["
        if list_objs is None:
            jsonToSave = []
        for obj in list_objs:
            dictionary = cls.to_dictionary(obj)
            jsonString = cls.to_json_string(dictionary)
            jsonToSave.append(jsonString)
            filename = cls.__name__+".json"
        for index, item in enumerate(jsonToSave):
            if index == 0:
                jsonToSaveString += item
            elif index != len(jsonToSave):
                jsonToSaveString += ", " + item
        with open(filename, mode='w', encoding='utf-8') as my_file:
            my_file.write(jsonToSaveString+"]")

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            class_ins = cls(cls.width, cls.height)
        elif cls.__name__ == "Square":
            class_ins = cls(cls.size)
        else:
            return
        class_ins.update(**dictionary)
        return class_ins
