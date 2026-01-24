import numpy as np

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]

bias = 2.0

# np.dot(weights, inputs)
output = np.array(inputs) @ np.array(weights) + bias
print(output)