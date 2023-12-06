#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = [row[:] for row in matrix]

    # Iterate through the rows and columns of the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix

    """
    return list(map(lambda j: list(map(lambda x: x ** 2, j)), matrix))
    """


"""
sqr = matrix.copy()
    for i in range(len(matrix)):
        sqr[i] = list(map(lambda x: x ** 2, matrix[i]))
    return sqr
"""
