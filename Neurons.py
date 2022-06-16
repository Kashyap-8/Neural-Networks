'''
A single neuron ch1 to ch2
neural network from scratch
3/20/21
'''

#creating a single neuron
inputs = [1,2,3] #three inputs
weights = [0.2, 0.8, -0.5]
bias = 2 #we randomly select this value


output = (inputs[0]*weights[0] +
          inputs[1]*weights[1] +
          inputs[2]*weights[2] + bias)
print(output)

inputs = [1, 2, 3, 2.5] #four inputs
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2 #we randomly select this value


output =  [inputs[0]*weights[0] +
          inputs[1]*weights[1] +
          inputs[2]*weights[2] +
          inputs[3]*weights[3] +
          bias]
print(output)




