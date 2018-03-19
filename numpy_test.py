# python3 numpy_test.py
# python numpy_test.py
import numpy as np
from numpy.random import rand
from numpy import *

X = np.array([2,3,45,1,23])
print(np.sort(X))
print([x ** 2 for x in X if x < 30 and x > 10]) 
a = np.array((1,2,3))
print(a)
print('')
A = matrix(zeros((3, 3)))
# matlab索引从1开始，python从0开始
A[1, 1] = 3
B = matrix(np.random.rand(3, 3))

B[2, 2] = 5
print(A)
print(B)
# 矩阵转置
print(B.T)
print(A + B)
print(A - B)
# 矩阵相乘
print(A * B)
# 矩阵点乘
print(multiply(A, B))
C = np.array([12,23,34])
print(C)
# python numpy_test.py
# python3 numpy_test.py
