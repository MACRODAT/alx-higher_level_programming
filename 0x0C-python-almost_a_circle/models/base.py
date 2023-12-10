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
                    dct.append(o.to_dictionary())
                f.write(cls.to_json_string(dct))

    @staticmethod
    def from_json_string(json_string):
        """stuff
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ fcreates a class
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """jkggg uu
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
    
    @classmethod
    def load_from_file_csv(cls):
        """ get all [cls] """
        filename = str(cls.__name__) + ".csv"
        try:
            objs = []
            with open(filename, "r") as f:
                line = f.readline().strip()
                while line:
                    splits = [int(x) for x in line.split(',')]
                    if cls.__name__ == "Rectangle":
                        dummy = cls(1,1)
                    else:
                        dummy = cls(1)
                    dummy.update(*splits)
                    objs.append(dummy)
                    line = f.readline()
            return objs
        except IOError:
            return []

    @classmethod 
    def save_to_file_csv(cls, list_objs):
        """ file saver """
        filename = str(cls.__name__) + ".csv"
        try:
            s = ""
            for o in list_objs:
                s += f"{o.id},{o.width},{o.height},{o.x},{o.y}\n"
            s = s[:-1] 
            with open(filename, "w") as f:
                f.write(s)
        except IOError:
            return []
