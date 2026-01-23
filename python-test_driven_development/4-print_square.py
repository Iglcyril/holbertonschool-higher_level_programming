#!/usr/bin/python3
"""
Module pour afficher un carré de caractères.

Ce module contient une fonction print_square qui affiche
un carré composé du caractère #.
"""


def print_square(size):
    """
    Affiche un carré de taille size avec le caractère #.
    
    Args:
        size (int): La taille du carré
    
    Raises:
        TypeError: Si size n'est pas un entier
        ValueError: Si size est négatif
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
