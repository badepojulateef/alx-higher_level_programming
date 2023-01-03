#!/usr/bin/python3
""" Defines a rectangle. """


class Rectangle:
    """ Defines a rectangle. """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initializes rectangle class. """

        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Get the width of the rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height of the reactangle. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the reactangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """  Returns the area of the rectangle. """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns the perimeter of the rectangle. """
        if self.__width == 0 or self.height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
