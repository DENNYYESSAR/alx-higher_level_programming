#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """
    A class that inherits from list and provides additional functionality.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
