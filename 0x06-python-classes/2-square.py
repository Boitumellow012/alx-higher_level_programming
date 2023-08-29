#!/usr/bin/python3
"""Define a class with the name Square"""

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

        try:
            self.__size = size
            if size < 0:
                raise ValueError
            if type(size) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
