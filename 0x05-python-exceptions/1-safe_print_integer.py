#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer with "{:d}"format.

    Args:
    calue (int): The integer to prunt.

    Returns:
    If a TypeError or ValueError occurs - False.
    Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, valueError):
        return (False)
