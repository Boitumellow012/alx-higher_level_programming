#!/usr/bin/python3
"""Define a  class with the name Square"""


class Square:
    """Defines an empty square."""
    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """int: Return area of square."""
        return self.__size * self.__size
