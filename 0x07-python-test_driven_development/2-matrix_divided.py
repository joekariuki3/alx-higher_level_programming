#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    funtion to divide each matrix number with div
    """
    row_size = 0
    if len(matrix) > 0 and isinstance(matrix, list):
        row_size = len(matrix[0])
    if isinstance(matrix, list):
        for row in matrix:
            if len(row) != row_size:
                raise TypeError("Each row of the matrix must have the same size")
            elif not isinstance(row, list):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            for num in row:
                if not isinstance(num, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return list(map(lambda row: list(map(lambda n: round((n / div), 2), row)), matrix))
