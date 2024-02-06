#!/usr/bin/python3
"""
Function to write an Object to a text file using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes the JSON representation of the given
    object to the specified file."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
