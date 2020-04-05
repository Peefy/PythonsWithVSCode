
from random import random as _random
from numpy import array as _np_array

font = {'family' : 'Times New Roman',    
        'size'   : 16,  
        }  

def build_rand_nparray(size):
    x = []
    for i in range(size):
        x.append(_random())
    return _np_array(x)

def build_rand_real_data(size, n):
    x = []
    for i in range(size):
        y = []
        for j in range(n):
            y.append(_random())
        x.append(y)
    return x

def cal_tar3(array):
    out_set = []
    size = len(array)
    for i in range(size):
        out_set.append(sum(array[i]) * 0.1)
    return out_set