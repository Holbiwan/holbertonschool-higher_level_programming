#!/usr/bin/python3
'''import'''
import json
import os.path
'''class'''


class Base:
    '''private attribute'''
    __nb_objects = 0
    '''method constructor'''
    def __init__(self, id=None):
        '''conditional'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
