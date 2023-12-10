#!/bin/python3

"""
    python file for storing data
"""
import json


class Base:
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """simple def
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json repre """
        if not list_dictionaries:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves things """
        with open(cls.__name__ + ".json", "w") as f:
            if not list_objs:
                f.write("[]")
            else:
                dct = []
                for o in list_objs:
                    dct.append([o.to_dictionary()])
                f.write(cls.to_json_string(dct))
