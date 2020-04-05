
# python python/chnn.py
# python3 python/chnn.py

import numpy as np
import neurolab as nl
import pylab as pl
import matplotlib.pyplot as plt
# num of input layer
n = 9
# num of output layer
m = 3
# num of hidden layer
H = 3
# input and output data range min
data_min = 0
# input and output data range max
data_max = 1
# input and output data range 
input_range = [data_min, data_max]
# num of input layer data range array 
input_range_array = np.array(input_range)

# Create train samples
# input = np.random.uniform(-0.5, 0.5, (10, 9))
# target = (input[:, 0] + input[:, 1] + input[:, 2] + input[:, 4] + input[:, 5] + 
# input[:, 6] + input[:, 7] + input[:, 8]).reshape(10, 1)
# Create network with 9 inputs, 3 neurons in input layer and 3 in output layer
net = nl.net.newhop([[0, 1], [0, 1], [0, 1], [0, 1], [0, 1]
    , [0, 1], [0, 1], [0, 1], [0, 1]])
# print num of input layer
print(net.ci)

print(net.co)
# err = net.train(input, target, show=15)
x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.scatter(x, y, alpha=0.5)
plt.show()
# net.sim([[0.2, 0.1, 0.1, 0.2, 0.3, 0.4, 0.4, 0.34, 0.2]]) 