#!/usr/bin/python3

""" add item """


import sys, json
sv = __import__("5-save_to_json_file").save_to_json_file
ld = __import__("6-load_from_json_file").load_from_json_file


if __name__ == "__main__":
    try:
        data = ld("add_item.json")
        data_lst = json.loads(data)
    except:
        data_lst = []
    data_lst.extend(sys.argv)
    sv(json.dumps(data_lst), "add_item.json")
