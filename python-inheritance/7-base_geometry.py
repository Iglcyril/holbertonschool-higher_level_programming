#!/usr/bin/python3
"""
This module defines a BaseGeometry class with validation.
"""


class BaseGeometry:
    """
    Base class for geometry objects.

    This class provides a foundation for geometry-related classes
    and includes validation methods.
    """

    def area(self):
        """
        Calculate the area.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
