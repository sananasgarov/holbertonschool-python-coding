#!/usr/bin/python3
"""
This module defines a Square class.
The class includes a private attribute and validation for size.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The side length of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter: Retrieves the private __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: validates data before updating __size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    def area(self):
        """
        Calculates the current square area.
        Retu
            int: The area of the square.
        """
        return self.__size**2
