#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """
    Prints a square with the character # of the specified size.

    Parameters:
    - size (int): The size length of the square.

    Raises:
    - TypeError: If size is not an integer or if size is a float less than 0.
    - ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size.is_integer():
            size = int(size)
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
