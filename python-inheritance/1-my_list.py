#!/usr/bin/python3
"""
This module defines a MyList class that inherits from list.
"""


class MyList(list):
    """
    A class that inherits from list with additional functionality.
    
    Methods:
        print_sorted: Prints the list in ascending sorted order.
    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order.
        
        The original list remains unchanged.
        """
        print(sorted(self))
