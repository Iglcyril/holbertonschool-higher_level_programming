#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ascii_code = ord(c)
        if ascii_code >= 97 and ascii_code <= 122:
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print()
