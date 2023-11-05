#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lst = []
    for i in my_list:
        lst += [i % 2]
    return lst
