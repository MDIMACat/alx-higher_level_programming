#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for list in matrix:
        print(" ".join("{:d}".format(j)for j in list))
