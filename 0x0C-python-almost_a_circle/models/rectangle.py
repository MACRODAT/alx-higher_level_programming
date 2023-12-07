#!/bin/python3

"""
    python file for storing data
"""

Base = __import__("base.py").Base


class Rectangle(Base):
    """ Class defining Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class initializer """
        super(self, id)
        self.width(width)
        self.height(height)
        self.x(x)
        self.y(y)

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""

    @property
    def x(self):
        """x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        self.__x = value

    @property
    def y(self):
        """y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        self.__y = value
