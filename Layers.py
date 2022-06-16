
inputs = [1, 2, 3, 2.5]

weights1 = [0.2, 0.8, -0.5, 1]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

outputs = [
# Neuron 1:
inputs[0]*weights1[0] +
inputs[1]*weights1[1] +
inputs[2]*weights1[2] +
inputs[3]*weights1[3] + bias1,

# Neuron 2:
inputs[0]*weights2[0] +
inputs[1]*weights2[1] +
inputs[2]*weights2[2] +
inputs[3]*weights2[3] + bias2,

# Neuron 3:
inputs[0]*weights3[0] +
inputs[1]*weights3[1] +
inputs[2]*weights3[2] +
inputs[3]*weights3[3] + bias3]


print(outputs)


# import numpy as np
#
#
# inputs = [[1,2,3,2.5],[2., 5., -1., 2],[-1.5, 2.7, 3.3, -0.8]]
# weights = [[0.2, 0.8, -0.5, 1], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
# biases = [2, 3, 0.5]
# weights2 = [[0.1, -0.14, 0.5], [-0.5, 0.12, -0.33], [-0.44, 0.73, -0.13]]
# biases2 = [-1, 2, -0.5]
#
# layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
# layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2
# print(layer2_outputs)