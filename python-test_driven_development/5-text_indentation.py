#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    letter =0
    while letter < len(text):
        print(text[letter], end="")

        if text[letter] in ['.', '?', ':']:

            print("\n")
        letter += 1
    print(letter)
