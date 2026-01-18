# inputs = [1.0, 2.0, 3.0, 2.5]

# weights1 = [0.2, 0.8, -0.5, 1.0]
# weights2 = [0.5, -0.91, 0.26, -0.5]
# weights3 = [-0.26, -0.27, 0.17, 0.87]

# bias1 = 2.0
# bias2 = 3.0
# bias3 = 0.5

# # using hard coding method

# outputs = [
#     # neuron 1
#     inputs[0] * weights1[0] +
#     inputs[1] * weights1[1] +
#     inputs[2] * weights1[2] +
#     inputs[3] * weights1[3] + bias1,

#     # neuron 2
#     inputs[0] * weights2[0] +
#     inputs[1] * weights2[1] +
#     inputs[2] * weights2[2] +
#     inputs[3] * weights2[3] + bias2,

#     # neuron 3
#     inputs[0] * weights3[0] +
#     inputs[1] * weights3[1] +
#     inputs[2] * weights3[2] +
#     inputs[3] * weights3[3] + bias3
# ]

# print(outputs)

# using for loop instead of hard coding every thing 
# we will need to turn weights into a 2d matrix 
# using more pythonic structrue is always prefered 

inputs = [1.0, 2.0, 3.0, 2.5]

weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
    
]

layer_outputs = []
biases = [2.0, 3.0, 0.5]

for neuron_weights, bias in zip(weights, biases):
    neuron_out = bias

    for input, weight in zip(inputs, neuron_weights):
        neuron_out += input * weight

    layer_outputs.append(neuron_out)



print(layer_outputs)

