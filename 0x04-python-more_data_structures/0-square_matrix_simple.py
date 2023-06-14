#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix2[i][j] = matrix[i][j] ** 2
    return matrix2
