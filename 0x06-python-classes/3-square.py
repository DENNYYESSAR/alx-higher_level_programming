#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize new instance of Square class with an optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Compute and return the area of the square."""
        return self.__size ** 2
