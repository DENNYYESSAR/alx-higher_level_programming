#!/usr/bin/python3
"""Defines a square class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the top-left corner
                of the square.Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner
                of the square.Defaults to 0.
            id (int, optional): The unique identifier of the square.
                Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square.

        Args:
            value (int): The new size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Updates attributes of the square.

        Args:
            *args: List of arguments. If provided, must follow the order
            : id, size, x, y.
            **kwargs: Dictionary of keyworded arguments, where each key
            represents an attribute.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the square.

        Returns:
            dict: Dictionary representation of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
