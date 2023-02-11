#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    for i, j in enumerate(matrix):
        for x, y in enumerate(j):
            new_matrix[i][x] = y ** 2
    return new_matrix
