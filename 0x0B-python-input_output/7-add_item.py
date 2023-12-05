#!/usr/bin/python3
""" add item """
import sys

if __name__ == "__main__":
    sv = __import__("5-save_to_json_file").save_to_json_file
    ld = __import__("6-load_from_json_file").load_from_json_file


    try:
        data_lst = ld("add_item.json")
    except FileNotFoundError:
        data_lst = []
    data_lst.extend(sys.argv[1:])
    sv(data_lst, "add_item.json")
