#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    """Prints an integer followed by a new line.

    Args:
        value: The value to be printed.

    Returns:
        True if value is an integer and has been correctly printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
