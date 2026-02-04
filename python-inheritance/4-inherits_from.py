#!/usr/bin/python3
"""
This module provides a function to check if an object inherits from a class.
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited from a_class.

    Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class, but NOT if obj is an
    instance of a_class itself.

    Args:
        obj: Any Python object to check.
        a_class: The class to check inheritance from.

    Returns:
        bool: True if obj inherits from a_class (but is not a direct
              instance of a_class), False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
