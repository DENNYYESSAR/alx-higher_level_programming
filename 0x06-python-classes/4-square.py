#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize new instance of Square class with an optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size attribute with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Compute and return the area of the square."""
        return self.__size ** 2
