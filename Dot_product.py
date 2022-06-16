
#Tensors

l = [1, 5, 6, 2]
lol = [[1, 5, 6, 2], [3, 2, 1, 3]]
lolol = [[[1, 5, 6, 2], [3, 2, 1, 3]], [[5, 5, 2, 1, 2], [6, 4, 8, 4]], [[2, 8, 5, 3], [1, 1, 9, 4]]]

print(lolol)

#Dot Product and Vector Addition

a = [1, 2, 3]
b = [2, 3, 4]

dot_product = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
print(dot_product)


# import numpy as np
#
# inputs = [1.0, 2.0, 3.0, 2.5]
# weights = [0.2, 0.8, -0.5, 1.0]
# bias = 2.0

# outputs = np.dot(weights, inputs) + bias
# print(outputs)

#---simplification and optimization---
# import numpy as np
# inputs = [1.0, 2.0, 3.0, 2.5]
# weights = [[0.2, 0.8, -0.5, 1.0],
#            [0.5, -0.91, 0.26, -0.5],
#            [-0.26, -0.27, 0.17, 0.87]]
#
# biases = [2.0, 3.0, 0.5]
#
# layer_output = np.dot(weights, inputs) + biases
# print(layer_output)
# # >>> array([4.8   1.21  2.385])
