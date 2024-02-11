#!/usr/bin/python3
"""
This script defines the Rectangle class inheriting from Base.
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle's position.
            y (int): y-coordinate of the rectangle's position.
            id (int): Identifier of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x attribute.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y attribute.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Prints the Rectangle instance with the character '#' taking
        into account x and y.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """Updates rectangle attributes based on positional and
        keyword arguments.

        Args:
            *args: Positional arguments for id (first only).
            **kwargs: Keyword arguments for any attribute.

        Raises:
            TypeError: If any non-ID argument is not an integer.
            ValueError: If width or height is not positive, or if x or
            y is less than 0.
        """

        # Process positional arguments (only for id)
        if len(args) >= 1:
            if not isinstance(args[0], int):
                raise TypeError("id must be an integer")
            self.id = args[0]

        # Process keyword arguments (override positional id if present)
        if "id" in kwargs:
            if not isinstance(kwargs["id"], int):
                raise TypeError("id must be an integer")
            self.id = kwargs["id"]
        if "width" in kwargs:
            if not isinstance(kwargs["width"], int):
                raise TypeError("width must be an integer")
            if kwargs["width"] <= 0:
                raise ValueError("width must be > 0")
            self.width = kwargs["width"]
        if "height" in kwargs:
            if not isinstance(kwargs["height"], int):
                raise TypeError("height must be an integer")
            if kwargs["height"] <= 0:
                raise ValueError("height must be > 0")
            self.height = kwargs["height"]
        if "x" in kwargs:
            if not isinstance(kwargs["x"], int):
                raise TypeError("x must be an integer")
            if kwargs["x"] < 0:
                raise ValueError("x must be >= 0")
            self.x = kwargs["x"]
        if "y" in kwargs:
            if not isinstance(kwargs["y"], int):
                raise TypeError("y must be an integer")
            if kwargs["y"] < 0:
                raise ValueError("y must be >= 0")
            self.y = kwargs["y"]

    def __str__(self):
        """
        Returns a string representation of the rectangle in a specific format.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)
    def to_dictionary(self):
        """
        Returns the dictionary representation of the rectangle.

        Returns:
            dict: Dictionary representation of the rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
