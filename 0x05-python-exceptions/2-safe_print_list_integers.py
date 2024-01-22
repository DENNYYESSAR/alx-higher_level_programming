#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x integers of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to access.

    Returns:
        The real number of integers printed.
    """
    printed_integers = 0

    try:
        for i in range(x):
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                printed_integers += 1
    except (IndexError, ValueError, TypeError):
        raise

    print()
    return printed_integers
