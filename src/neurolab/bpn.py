
# python python/bpn.py
# python3 python/bpn.py

import copy
import random
from copy import deepcopy
import numpy as np
from numpy import arange
import numpy.random as rand
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
from matplotlib.pyplot import figure
import neurolab as nl
import pylab as pl
if __name__ == '__main__':
    import dataset
else :
    from . import dataset
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
input_range_array = []
for i in range(n):
    input_range_array.append(input_range)
# create the feed forward fultilayer perceptron
net = nl.net.newff(input_range_array, [H, m])
# input data collection size
size = 500

# build expect input data collection
X = []
for i in range(n):
    X.append(dataset.build_rand_nparray(size))
inp = []
for i in range(size):
    inp.append([X[0][i], X[1][i], X[2][i], X[3][i], 
        X[4][i], X[5][i], X[6][i], X[7][i], X[8][i]])

tar_1 = X[0]
tar_2 = 0.2 * X[1]
tar_3 = 0.1 * (X[0] + X[1] + X[2] + X[3] + X[4] + X[5] + X[6] + X[7] + X[8])
target = []
for i in range(size):
    target.append([tar_1[i], tar_2[i], tar_3[i]])
print('start train')
err = net.train(inp, target, epochs=5000, show=100, goal=0.02)
real = abs(rand.randn(1, n) * 0.2)
print(real)
out = net.sim(real)
print(real[0][0])
print((real[0][0] + real[0][1]) * 0.2)
print(sum(real[0]) * 0.1)
print(out)
real_set = dataset.build_rand_real_data(100, n)
cal_set = dataset.cal_tar3(real_set)
out_set = net.sim(real_set)
print(cal_set)
print(out_set)
pl.plot(err)
ax = plt.gca()  
ax.set_xticks(np.linspace(0,1200,9))  
ax.set_xticklabels( ('0', '150', '300', '450', '600',  '750',  '900',  '1050', '1200'), fontdict=dataset.font)  
ax.set_yticks(np.linspace(0,32,9))  
ax.set_yticklabels( ('0', '4', '8', '12', '16','20','24','28', '32'), fontdict=dataset.font)  
ax.set_ylabel('Error', fontdict=dataset.font)  
ax.set_xlabel('Epochs', fontdict=dataset.font)
pl.show()


# python python/bpn.py
# python3 python/bpn.py