#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """
    Prints the text with 2 new lines after each occurrence of '.', '?' and ':'.

    Parameters:
    - text (str): The input text.

    Raises:
    - TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end="")
        if char in ['.', '?', ':']:
            print("\n")
