#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    new_matrix = [[num * num for num in row] for row in matrix]
    return new_matrix
