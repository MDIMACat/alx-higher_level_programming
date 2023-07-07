#!/usr/bin/python3
"""Defines a matrix_divided function"""


def matrix_divided(matrix, div):

    if not all(isinstance(row, list) and all(isinstance(element, (int, float))for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
