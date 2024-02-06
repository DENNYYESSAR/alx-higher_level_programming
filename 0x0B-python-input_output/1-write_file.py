#!/usr/bin/python3
"""
Function to write a string to a text file (UTF8) and
return the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes the given text to the specified file and
    returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
