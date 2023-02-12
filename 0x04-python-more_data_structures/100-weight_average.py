#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_of_score = 0
    sum_of_weight = 0
    for score, weight in my_list:
        sum_of_score += weight * score
        sum_of_weight += weight
    return sum_of_score / sum_of_weight
