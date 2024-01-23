#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Represents a square with size attribute."""

    def __init__(self, size=0):
        """Initialize new instance of Square class with size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size attribute with type and value validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Compute and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare two squares based on area for equality."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare two squares based on area for inequality."""
        return not self == other

    def __lt__(self, other):
        """Compare two squares based on area for less than."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare two squares based on area for less than or equal."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare two squares based on area for greater than."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare two squares based on area for greater than or equal."""
        return self.area() >= other.area()
