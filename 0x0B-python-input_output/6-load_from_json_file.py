#!/usr/bin/python3
"""
Function to create an Object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """Creates an object from the JSON representation
    stored in the specified file."""
    with open(filename, "r") as file:
        return json.load(file)
