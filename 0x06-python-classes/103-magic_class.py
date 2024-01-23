#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided by Holberton."""


import math


class MagicClass:
    """Represents a magic class for geometric calculations."""

    def __init__(self, radius=0):
        """
        Initialize a new instance of the MagicClass with a radius.

        Args:
            radius (float): The radius of the circle. Defaults to 0.
        """
    self.__radius = 0

    if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Compute and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
    return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Compute and return the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
    return 2 * math.pi * self.__radius
