#!/usr/bin/python3
""" Finds a peak in a lst
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): lst
    Returns: pk of list_of_integers
    """
    sz = len(list_of_integers)
    middle = sz
    mid = sz // 2

    if sz == 0:
        return None

    while True:
        middle = middle // 2
        if (mid < sz - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if middle // 2 == 0:
                middle = 2
            mid = mid + middle // 2
        elif middle > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if middle // 2 == 0:
                middle = 2
            mid = mid - middle // 2
        else:
            return list_of_integers[mid]
