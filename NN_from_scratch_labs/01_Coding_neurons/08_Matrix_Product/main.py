import numpy as np


matrix_a = [[0.49, 0.97, 0.53, 0.05],
            [0.33, 0.65, 0.62, 0.51],
            [1.00, 0.38, 0.61, 0.45],
            [0.74, 0.27, 0.64, 0.17],
            [0.36, 0.17, 0.96, 0.12]]

matrix_b = [[0.79, 0.32, 0.68, 0.90, 0.77],
            [0.18, 0.39, 0.12, 0.93, 0.09],
            [0.87, 0.42, 0.60, 0.71, 0.12],
            [0.45, 0.55, 0.40, 0.78, 0.81]]

full_matrix = []
products = []

for vector in matrix_a:
    col = 0

    while col < len(matrix_b[0]):
        row = 0
        product = 0

        for val in vector:
            product += val * matrix_b[row][col]
            row += 1
        
        products.append(product)
        col += 1

    full_matrix.append(products.copy())
    products.clear()    


    
print(np.round(np.array(full_matrix), 2))
print()

# numpy implementation 
matrix_numpy = np.round(np.dot(matrix_a, matrix_b), 2)
print(matrix_numpy)