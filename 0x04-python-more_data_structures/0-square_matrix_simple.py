#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix
    for i in range(len(matrix)):
        for j in range(len(i)):
            new_matrix[i][j] = j ** 2
