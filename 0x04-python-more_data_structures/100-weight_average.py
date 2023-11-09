#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        denom = 0
        for tss in my_list:
            num += (tss[0] * tss[1])
            denom += (tss[1])
        return (num/denom)
    return 0
