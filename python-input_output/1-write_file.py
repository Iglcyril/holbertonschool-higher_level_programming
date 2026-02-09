#!/usr/bin/python3
"""Module that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns number of characters

    Args:
        filename: name of the file to write to
        text: text to write to the file

    Returns:
        Number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return len(text)	
