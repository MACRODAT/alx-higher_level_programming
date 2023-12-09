#!/bin/python3

"""
    python file for storing data
"""

from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ class init """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
