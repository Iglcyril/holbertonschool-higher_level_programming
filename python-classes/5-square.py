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
        self.size = size

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()

    def area(self):
        """
        Calculate and return the area of the square.
        Returns:
        int: The area of the square (size * size).
        """
        return self.__size * self.__size
