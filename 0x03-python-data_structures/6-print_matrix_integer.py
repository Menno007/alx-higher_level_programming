#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print()
    else:
        for row in matrix:
            for column in row:
                if column == row[-1]:
                    print("{:d}".format(column))
                else:
                    print("{:d} ".format(column), end='')
