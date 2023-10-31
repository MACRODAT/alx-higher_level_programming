#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lst = number % -(10)
        print(-(lst), end='')
    else:
        lst = number % 10
        print(lst, end='')
    return abs(lst)
