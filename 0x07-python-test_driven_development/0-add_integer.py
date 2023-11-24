#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """add of a

    The addition operation for float values involves converting the floating 
    point numbers into integers prior to performing the calculation.

    Raises:
        In case one of the input arguments is not an integer or a float, a TypeError will be raised.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
