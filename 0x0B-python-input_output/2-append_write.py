#!/usr/bin/python3
"""
Function to append a string to the end of a text file (UTF8) and
return the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends the given text to the specified file and
    returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
