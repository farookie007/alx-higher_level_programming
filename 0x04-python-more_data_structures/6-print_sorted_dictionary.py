#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        a_dictionary = dict()
    sorted_keys = sorted(list(a_dictionary.keys()))
    for k in sorted_keys:
        print("{}: {}".format(k, a_dictionary.get(k)))
