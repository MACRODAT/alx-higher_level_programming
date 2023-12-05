#!/usr/bin/python3
"""Student."""


class Student:
    """a student."""

    def __init__(self, first_name, last_name, age):
        """new Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """the Student.
        """
        if (type(attrs) is list):
            if (all(type(e) is str for e in attrs)):
                return {att: getattr(self, att)
                        for att in attrs if hasattr(self, att)}
        return self.__dict__
