#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """rectangle.
    Attributes:
        number_of_instances (int): nbr
        print_symbol (any): symb
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init.

        Args:
            width (i): The width.
            height (i): The height.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the w"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """G/s height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """printable repr"""
        if self.__width * self.__height == 0:
            return ("")

        rect = []
        for _ in range(self.__height):
            [rect.append(str(self.print_symbol)) for _ in range(self.__width)]
            rect.append("\n")
        rect = rect[:-1]
        return ("".join(rect))

    def __repr__(self):
        """string repr"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
