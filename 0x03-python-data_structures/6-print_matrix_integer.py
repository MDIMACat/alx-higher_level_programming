#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for list in matrix:
        for elements in list:
            print("{:d}".format(elements), end=" ")
        print()
