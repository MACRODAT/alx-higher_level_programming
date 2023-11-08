#!/usr/bin/python3
def common_elements(set_1, set_2):
    s = set()
    s = s.union(set_1)
    s = s.intersection(set_2)
    return (s)
