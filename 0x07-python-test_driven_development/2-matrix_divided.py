#!/usr/bin/python3
"""Module that is used to divide
values in a matrix

example:

>>> matrix_divided([
... [1, 2, 3],
... [4, 5, 6],
... [7, 8, 9]
... ], 1)
[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]

"""


def matrix_divided(matrix, div):
    """
    matrix_divided : function prototype used for this module

    Parameters:
    matrix - a 2d matrix passed as first argument
    div - divisor value passed as second argument

    Returns:
    A new matrix with divided values

    Raises:
    TypeError:
        1. If matrix is not a list
        2. If rows in matrix aint a list
        3. If elements are not int's or float's

    ZeroDivisionError:
        If the Divisor is a zero
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("Each row in the matrix must be a list")

        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("Matrix elements must be integers or floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            new_row.append(round(x / div, 2))
        result_matrix.append(new_row)

    return result_matrix
