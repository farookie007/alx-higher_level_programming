#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    keys = a_dictionary.keys()
    for k in keys:
        if a_dictionary.get(k) == value:
            a_dictionary.pop(k)
