#!/usr/bin/env python3
"""
This module defines a VerboseList class that extends the built-in list.
It provides notifications when items are added or removed.
"""


class VerboseList(list):
    """
    A list subclass that prints notifications when items are added or removed.
    
    This class extends the built-in list class and overrides methods to
    provide verbose feedback on list operations.
    """
    
    def append(self, item):
        """
        Append an item to the list and print a notification.
        
        Args:
            item: The item to append to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")
    
    def extend(self, iterable):
        """
        Extend the list with items from an iterable and print a notification.
        
        Args:
            iterable: An iterable containing items to add to the list.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")
    
    def remove(self, item):
        """
        Remove an item from the list and print a notification.
        
        Args:
            item: The item to remove from the list.
        
        Raises:
            ValueError: If the item is not in the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        """
        Remove and return an item at a given index and print a notification.
        
        Args:
            index (int, optional): The index of the item to pop. Defaults to -1 (last item).
        
        Returns:
            The item that was removed from the list.
        
        Raises:
            IndexError: If the list is empty or index is out of range.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
