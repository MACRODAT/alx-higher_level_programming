#!/bin/python3

"""
    python file for storing data
"""

from base import Base


class Rectangle(Base):
    """ Class defining Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class initializer """
        super().__init__(id)
        self.width = (width)
        self.height = (height)
        self.x = (x)
        self.y = (y)

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns area """
        return (self.width * self.height)

    def display(self):
        """display rectangle"""
        y_ = self.y
        while y_:
            print()
            y_ = y_ - 1
        for _ in range(self.height):
            print(' ' * self.x,end='')
            for _ in range(self.width):
                print("#", end='')
            print()

    def __str__(self) -> str:
        """ override """
        return \
            f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ updates the rectangle """
        if args and len(args) > 0:
            _len = len(args) - 1
            if _len >= 0:
                self.id = args[0]
            if _len >= 1:
                self.width = args[1]
            if _len >= 2:
                self.height = args[2]
            if _len >= 3:
                self.x = args[3]
            if _len >= 4:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
