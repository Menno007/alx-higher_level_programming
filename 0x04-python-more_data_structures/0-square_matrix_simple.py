#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr = matrix.copy()
    for i in range(len(matrix)):
        sqr[i] = list(map(lambda x: x ** 2, matrix[i]))
    return sqr
