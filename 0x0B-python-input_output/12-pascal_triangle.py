#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """create pascal triangle
    """
    if n <= 0:
        return []

    liste = [[1]]
    while len(liste) != n:
        lst = liste[-1]
        new_tri = [1]
        for i in range(len(lst) - 1):
            new_tri.append(lst[i] + lst[i + 1])
        new_tri.append(1)
        liste.append(new_tri)
    return liste
