#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    union = set.union(set_1, set_2)
    inter = set.intersection(set_1, set_2)
    return set.difference(union, inter)
