#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    max_ = 0
    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    romanNumbers = list(map(lambda c: nums[c], roman_string))
    for d in range(len(romanNumbers) - 1, -1, -1):
        if romanNumbers[d] < max_:
            romanNumbers[d] *= -1
        else:
            max_ = romanNumbers[d]
    return sum(romanNumbers)
