#!/usr/bin/python3
"""
This module provides a function to list attributes and methods of an object.
"""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
        obj: Any Python object to inspect.

    Returns:
        list: A list containing all attributes and methods names.
    """
    return dir(obj)
