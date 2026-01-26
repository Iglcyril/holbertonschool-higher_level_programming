#!/usr/bin/python3
"""
This module defines a Square class.

The Square class is used to represent square geometric shapes
and will be used for various calculations in future implementations.
"""


class Square:
    """
    This class represents a square with a validated size attribute.
    
    The size must be an integer >= 0, enforced during initialization.
    """


    def __init__(self, size=0):
        """
        Initialize a Square instance with size validation.
        
        Args:
            size (int, optional): The size of the square. Defaults to 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def area(self):
        """
        Calculate and return the area of the square.
        Returns:
        int: The area of the square (size * size).
        """
        return self.__size * self.__size

