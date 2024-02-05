#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible.

    Raises a TypeError if the object cannot have new attributes.

    Args:
    obj: The object to which the attribute should be added.
    attr: The name of the attribute to add.
    value: The value of the attribute to add.

    Raises:
    TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, '__dict__') and not isinstance(obj, type):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
