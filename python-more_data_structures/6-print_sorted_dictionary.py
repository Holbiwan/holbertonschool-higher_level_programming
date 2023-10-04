#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = {k: a_dictionary[k] for k in sorted(a_dictionary)}
    print('\n'.join("{}: {}".format(k, v) for k, v in sorted_dict.items()))
    return sorted_dict
