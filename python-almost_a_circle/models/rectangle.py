#!/usr/bin/python3
'''import of base class from base,py module'''
from models.base import Base
'''class'''


class Rectangle(Base):
    '''Defines the Rectangle class with attributes'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Get the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width of rectangle with validation'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        '''assignment'''
        self.__width = value

    @property
    def height(self):
        '''Get the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the height of rectangle with validation'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        '''assignment'''
        self.__height = value

    @property
    def x(self):
        '''Get the x coordinate of rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Set the coordinate of rectangle '''
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        '''assignment'''
        self.__x = value

    @property
    def y(self):
        '''Get the y coordinate of rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Set the y coordinate of rectangle'''
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        '''assignment'''
        self.__y = value

    '''method area'''
    def area(self):
        '''Calculate and return the area of rectangle'''
        return self.__width * self.__height

    '''method display'''
    def display(self):
        '''print y'''
        for j in range(self.__y):
            '''print position y'''
            print()
        '''diplay Rectangle'''
        for i in range(self.__height):
            '''print rectangle'''
            print(" " * self.__x + "#" * self.__width)

    '''method str'''
    def __str__(self):
        '''return'''
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

    '''method assignment'''
    def update(self, *args, **kwargs):
        '''iterates args'''
        for i in range(len(args)):
            '''assignment'''
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.__width = args[i]
            elif i == 2:
                self.__height = args[i]
            elif i == 3:
                self.__x = args[i]
            elif i == 4:
                self.__y = args[i]
        '''assignment key and value'''
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "width":
                self.__width = value
            elif key == "height":
                self.__height = value
            elif key == "x":
                self.__x = value
            elif key == "y":
                self.__y = value

    def to_dictionary(self):
        '''Return a dictionary representation of Rectangle'''
        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x,
                "y": self.__y}
