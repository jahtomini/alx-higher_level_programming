#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for arr in matrix:
            for i in arr:
                print(str.format("{}", i), end=' ')
