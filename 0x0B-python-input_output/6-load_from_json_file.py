#!/usr/bin/python3
"""
Lorem ipsum dolor sit amet,
consectetuer adipiscing elit.
Aenean commodo
ligula eget dolor. Aenean massa.
Cum sociis natoque penatibus et magnis
dis parturient montes
"""
import json


def load_from_json_file(filename):
    """'Lorem ipsum dolor sit amet,
    consectetuer adipiscing elit.
    Aenean commodo ligula eget dolor. Aenean massa.
    Cum sociis natoque penatibus et magnis dis parturient montes,
    nascetur '"""
    with open(filename) as f:
        return json.load(f)
