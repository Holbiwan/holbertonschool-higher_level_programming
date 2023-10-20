#!/usr/bin/python3

'''Class BaseGeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry

'''Class Rectangle inherits the class BaseGeometry'''
class Rectangle(BaseGeometry):
    '''Method'''
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    '''Method'''
    def area(self):
        '''Return area'''
        return self.__width * self.__height

    '''Method'''
    def __str__(self):
        '''Return print str'''
        name = str(self.__class__.__name__)
        return str("[{}] {}/{}".format(name, self.__width, self.__height))
