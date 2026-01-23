#!/usr/bin/python3
"""
Module pour l'indentation de texte.

Ce module contient une fonction text_indentation qui formate
un texte en ajoutant des sauts de ligne après certains caractères.
"""


def text_indentation(text):
    """
    Affiche un texte avec 2 nouvelles lignes après . ? et :
    
    Args:
        text (str): Le texte à formatter
    
    Raises:
        TypeError: Si text n'est pas une string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    letter =0
    while letter < len(text):
        print(text[letter], end="")

        if text[letter] in ['.', '?', ':']:
            print("\n")
            letter += 1
            while letter < len(text) and text[letter] == ' ':
                letter += 1
            continue
        letter += 1

  
