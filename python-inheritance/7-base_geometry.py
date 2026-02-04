#!/usr/bin/python3
"""
This module defines an empty BaseGeometry class.
"""


class BaseGeometry:
    """
    Base class for geometry objects.

    This class provides a foundation for geometry-related classes.
    """

    def area(self):
        """
        Calculate the area.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
