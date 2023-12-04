#!/usr/bin/python3
"""BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Reusing BaseGeometry."""

    def __init__(self, width, height):
        """new rectangle
        using new geo
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[Rectangle] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
