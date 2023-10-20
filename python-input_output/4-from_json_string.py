#!/usr/bin/python3
'''import'''
import json
'''return an object represented by a JSON'''


def from_json_string(my_str):
    '''return'''
    return json.loads(my_str)
