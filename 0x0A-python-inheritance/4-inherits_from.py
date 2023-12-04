#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """something obnoxious
    and not that important
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
