#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """
    A class representing a rebellious integer that inverts the == and != operators.
    """

    def __eq__(self, other):
        """
        Override the equality operator.

        Args:
        other: The object to compare with.

        Returns:
        bool: True if self is not equal to other, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator.

        Args:
        other: The object to compare with.

        Returns:
        bool: True if self is equal to other, False otherwise.
        """
        return super().__eq__(other)
