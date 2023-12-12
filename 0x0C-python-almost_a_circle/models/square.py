#!/bin/python3

"""
    python file for storing data
"""

from .rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ class init """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ return the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ set the size for value """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates the rectangle """
        if args and len(args) > 0:
            _len = len(args) - 1
            if _len >= 0:
                self.id = args[0]
            if _len >= 1:
                self.size = args[1]
            if _len >= 2:
                self.x = args[2]
            if _len >= 3:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """ dict repres """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y,
        }
