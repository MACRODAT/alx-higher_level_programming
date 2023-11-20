#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for e in my_list:
        i += 1
        try:
            print(e)
        except Exception as e:
            break
        if i > x:
            break
