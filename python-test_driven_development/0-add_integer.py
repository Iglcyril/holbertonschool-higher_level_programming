#!/usr/bin/python3
"""
Module pour l'addition d'entiers.

Ce module contient une fonction add_integer qui permet
d'additionner deux nombres (entiers ou floats).
"""


def add_integer(a, b=98):
    """
    Additionne deux entiers.

    Args:
        a (int, float): Premier nombre
        b (int, float): Deuxième nombre (défaut: 98)

    Returns:
        int: La somme de a et b

    Raises:
        TypeError: Si a ou b n'est pas un int ou float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
