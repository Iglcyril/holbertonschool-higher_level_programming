#!/usr/bin/env python3
"""
This module defines an abstract Shape class and its concrete implementations.
It demonstrates the concept of duck typing in Python.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    
    This class defines the interface that all shapes must implement.
    """
    
    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.
        
        Returns:
            float: The area of the shape.
        """
        pass
    
    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.
        
        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape.
    
    Represents a circle and implements area and perimeter calculations.
    """
    
    def __init__(self, radius):
        """
        Initialize a Circle instance.
        
        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate and return the area of the circle.
        
        Returns:
            float: The area (π * r²).
        """
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """
        Calculate and return the perimeter (circumference) of the circle.
        
        Returns:
            float: The perimeter (2 * π * r).
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.
    
    Represents a rectangle and implements area and perimeter calculations.
    """
    
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.
        
        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height
    
    def area(self):
        """
        Calculate and return the area of the rectangle.
        
        Returns:
            float: The area (width * height).
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        
        Returns:
            float: The perimeter (2 * (width + height)).
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.
    
    This function uses duck typing - it doesn't check the type of the shape,
    it just assumes the shape has area() and perimeter() methods.
    
    Args:
        shape: Any object that implements area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
