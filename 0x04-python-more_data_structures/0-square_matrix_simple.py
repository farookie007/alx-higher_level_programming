#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = list()
    for j in matrix:
        new_matrix.append([y ** 2 for y in j])
    return new_matrix
