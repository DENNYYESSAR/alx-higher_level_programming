#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer with "{:d}" format.

    Args:
        value: The value to be printed.

    Returns:
        True if value is an integer and has been correctly printed, False otherwise.
    """
    try:
        print("{:d}".format(int(value)))
        return True
    except (ValueError, TypeError):
        return False
