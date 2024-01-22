#!/usr/bin/python3

def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: The function to be executed.
        *args: The arguments to be passed to the function.

    Returns:
        The result of the function, or None if an exception occurs.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return None
