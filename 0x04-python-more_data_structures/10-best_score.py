#!/usr/bin/python3

def best_score(a_dictionary):
    # if the dictionary is empty
    if len(a_dictionary) <= 0:
        return None
    # gets the maximum integer value in the dictionary
    max_value = max(a_dictionary.values())
    for k, v in a_dictionary.items():
        # if the value is equal to the max_value
        if v == max_value:
            return k
