#!/usr/bin/python3
"""
Function to return an object represented by a JSON string.
"""


import json


def from_json_string(my_str):
    """Returns the object represented by the given JSON string."""
    return json.loads(my_str)
