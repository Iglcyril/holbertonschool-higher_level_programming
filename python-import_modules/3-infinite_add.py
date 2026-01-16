#!/usr/bin/python3
import sys
if __name__ == "__main__":
    somme = 0
    for arg in sys.argv[1:]:
        somme += int(arg)
    print(somme)
