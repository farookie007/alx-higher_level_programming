#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, col in enumerate(row, start=1):
            print("{:d}".format(col), end="\n" if i == len(row) else " ")

