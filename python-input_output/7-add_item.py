#!/usr/bin/python3
import sys
import os
from '5-save_to_json_file' import save_to_json_file
from '6-load_from_json_file' import load_from_json_file

args = sys.argv
filename = 'add_item.json'


def add_list():
    obj_list = []

    with open(filename, "a") as file:
        pass

    if os.stat(filename).st_size == 0:
        obj_list = []
    elif os.path.exists(filename):
        obj_list = load_from_json_file(filename)

    obj_list.extend(args[1:])
    save_to_json_file(obj_list, filename)


if __name__ == "__main__":
    add_list()
