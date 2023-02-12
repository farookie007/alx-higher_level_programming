#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        a_dictionary = dict()
    a_dictionary.update({key: value})
