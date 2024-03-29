#!/usr/bin/python3
"""A module that defines a class Rectangle"""
from module.base import Base



class Rectangle(Base):
    """A defination of class that defines a class Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constroctor"""
        super().__init__.(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter the size of the width

            Args:
                value: size to assign to the width

            Return:
                None
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
        self.__width = value

    # Getter and setter of height
    @property
    def height(self):
        """Getter the size of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter the size of height

        Args:
           value: Size to assign to the height

        Return:
           None

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

     # Getter and setter for x variable
    @property
    def x(self):
        """Getter of x variable"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of x variable

        Args:
           value: value to assign to x variable

        Return:
           None

        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    # Getter and setter for y variable
    @property
    def y(self):
        """Getter of y variable"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter of y variable

        Args:
           value: value to assign to y variable

        Return:
           None

        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

     def area(self):
        """Method that returns the area of the rectangle object

        Args:
           Not arguments

        Return:
           Area of the rectangle object

        """
        return self.width * self.height

    def display(self):
        """Method that prints to stdout
           Rectangle object with the character #

        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + self.width * '#')

     def __str__(self):
        """Method that override str method
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))



