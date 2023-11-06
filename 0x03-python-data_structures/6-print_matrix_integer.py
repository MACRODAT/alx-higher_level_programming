#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for rr_ow in matrix:
        for _col in r_:
            if _col == r_[-1]:
                print('{:d}'.format(_col), end='')
            else:
                print('{:d}'.format(_col), end=' ')
        print()
