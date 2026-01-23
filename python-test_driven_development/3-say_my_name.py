#!/usr/bin/python3
"""
Module pour afficher un nom complet.

Ce module contient une fonction say_my_name qui affiche
le prénom et le nom de famille d'une personne.
"""


def say_my_name(first_name, last_name=""):
    """
    Affiche 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): Le prénom
        last_name (str): Le nom de famille (optionnel)

    Raises:
        TypeError: Si first_name n'est pas une string
        TypeError: Si last_name n'est pas une string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
