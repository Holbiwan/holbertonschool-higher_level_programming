#!/usr/bin/python3
'''class'''


class Rectangle:
    '''public attribute'''
    number_of_instances = 0
    '''method function'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    '''decorator'''
    @property
    def get_width(self):
        '''return  attribute'''
        return self.__width
    '''decorator'''
    @get_width.setter
    def width(self, value):
        '''validation'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        '''assign value'''
        self.__width = value
    '''decorator'''
    @property
    def get_height(self):
        '''return attribute'''
        return self.__height
    '''decorator'''
    @get_height.setter
    def height(self, value):
        '''validation'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        '''assign value'''
        self.__height = value
    '''function area'''
    def area(self):
        '''return area of rectangle'''
        return self.__width * self.__height
    '''function perimeter'''
    def perimeter(self):
        '''validation'''
        if self.__width == 0 or self.__height == 0:
            return 0
        '''return perimeter'''
        return 2 * (self.__width + self.__height)
    '''funtion str'''
    def __str__(self):
        rectangle = ""
        '''validation'''
        if self.__width == 0 or self.__height == 0:
            return rectangle
        '''created of rectangle'''
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
            if i < self.__height - 1:
                rectangle += '\n'
        '''return rectangle'''
        return rectangle
    '''function repr'''
    def __repr__(self):
        '''return new rectangle'''
        return "Rectangle(%d%d)" % (self.__height, self.__width)
    '''function del'''
    def __del__(self):
        '''Decremented'''
        Rectangle.number_of_instances -= 1
        '''delete and print a msg'''
    
    print("Bye rectangle...")
