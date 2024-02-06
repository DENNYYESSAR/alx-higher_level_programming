#!/usr/bin/python3
"""
Function to read a text file (UTF8) and print its content to stdout.
"""


def read_file(filename=""):
    """Reads the content of the specified file and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        file_content = file.read()
        print(file_content)
