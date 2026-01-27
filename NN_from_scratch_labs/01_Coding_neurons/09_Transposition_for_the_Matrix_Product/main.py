import numpy as np


# ---------------------------------------------
# Matrix with a single row. Different ways to implement.
# 1.
a = np.array([[1, 2, 3]])
# print(a)

# 2
b = [1, 2, 3]
# print(np.array([b]))

# 3
c = [1, 2, 3]
# print(np.expand_dims(np.array(c), axis=0)) # check this line 
# ---------------------------------------------


# Matrix product on a row vector and column vector
d = [1, 2, 3]
e = [2, 3, 4]

d = np.array([d])
e = np.array([e]).T # Numpy Matrix Transposition

# Outputs single value in a matrix
# print(np.dot(d, e)) 

matrix = [[0.49, 0.97, 0.53, 0.05],
            [0.33, 0.65, 0.62, 0.51],
            [1.00, 0.38, 0.61, 0.45],
            [0.74, 0.27, 0.64, 0.17],
            [0.36, 0.17, 0.96, 0.12]]

# transpose manual implementation 
matrix_transpose = []

for j in range(len(matrix[0])):
    row = []
    for i in range(len(matrix)):
        row.append(matrix[i][j])

    matrix_transpose.append(row.copy())

# print(np.array(matrix_transpose))

# Transpose manual pythonic implementation 
matrix_transpose_py = np.array(list(map(list, zip(*matrix))))
# print(matrix_transpose_py)

# Test the Zip Function 
# lst = [[1, 2, 3], [3, 4 ,5]]
# print(list(zip(*lst)))

#  Using numpy
matrix_transpose_numpy = np.array(matrix).T
# print(matrix_transpose_numpy)