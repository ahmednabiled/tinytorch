# List (1D array, Vector) - Shape is (4,) - 4 elements, 1 dimension.
l = [1, 5, 6, 2]

# List of lists (2D array, Matrix) - Shape is (2, 4) - 2 lists, 4 elements. 2 dimension.
lol = [[1, 5, 6, 2], [3, 2, 1, 3]] 

# List of lists of lists (3D array) - Shape is (3, 2, 4) - 3 lists of lists, 2 lists per list, 4 elements per list, 3 dimensions.
lolol = [
    [[1, 5, 6, 2], [3, 2, 1, 3]],
    [[5, 2, 1, 2], [6, 4, 8, 4]],
    [[2, 8, 5, 3], [1, 1, 9, 4]]
]

# This list cannot be an array due it not being "homologous" (having the same relation, relative position, or structure)
another_list_of_lists = [[4, 2, 3], [5, 1]]


# Matrix (2D array) - Shape is (3, 2), 3 lists, 2 elements per list. 2 dimensions.
list_matrix_array = [[4, 2],
                     [5, 1],
                     [8, 2]]