#!/usr/bin/python3
''' random stift
'''
import json


def save_to_json_file(my_obj, filename):
    ''' wedwedwwedwedewedwedwedw
    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
