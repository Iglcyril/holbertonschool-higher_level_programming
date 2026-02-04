#!/usr/bin/env python3
"""
This module defines an abstract Animal class and its subclasses.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    
    This class defines the interface that all animals must implement.
    """
    
    @abstractmethod
    def sound(self):
        """
        Abstract method that returns the sound an animal makes.
        
        Returns:
            str: The sound the animal makes.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.
    
    Represents a dog and implements the sound method.
    """
    
    def sound(self):
        """
        Return the sound a dog makes.
        
        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.
    
    Represents a cat and implements the sound method.
    """
    
    def sound(self):
        """
        Return the sound a cat makes.
        
        Returns:
            str: "Meow"
        """
        return "Meow"
