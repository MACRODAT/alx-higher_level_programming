#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    p = 0
    while (i < x):
        try:
            print("{:d}".format(my_list[i]), end="")
            p += 1
        except (TypeError, ValueError):
            pass

        i += 1
    print()
    return p
