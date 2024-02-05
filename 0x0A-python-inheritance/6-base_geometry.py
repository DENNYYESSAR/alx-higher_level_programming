#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    A base class representing basic geometry.

    Attributes:
    None
    """

    def area(self):
        """
        Computes the area of the geometry.

        Raises:
        Exception: Indicates that the method is not implemented.
        """
        raise Exception("area() is not implemented")
