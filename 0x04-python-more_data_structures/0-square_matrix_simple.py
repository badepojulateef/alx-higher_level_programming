def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    return [[col ** 2 for col in row] for row in new_matrix]
