# python3 numpy_test.py
# python numpy_test.py
import numpy as np
from numpy.random import rand
from numpy import *

import seaborn

def matrix_multiply(A, B):
    '''
    两个矩阵相乘
    '''
    rowA = shape(A)[0]
    colunmA = shape(A)[1]
    rowB = shape(B)[0]
    colunmB = shape(B)[1]
    C = ones([rowA, colunmB])
    if colunmA != rowA:
        raise Exception('incompatible dimensions')
    else:
        for i in range(rowA):
            for j in range(colunmB):
                C[i][j] = 0
                for k in range(colunmA):
                    C[i][j] = C[i][j] + A[i][k] * B[k][j]
        return C

seaborn.set_style('whitegrid')

A = array([[1, 2], [3, 4]])
# 相当于matlab中的点乘
print(A * A)
# 相当于matlab中的矩阵乘
print(matrix_multiply(A, A))
# 相当于matlab中的矩阵乘
print(dot(A, A))
A = matrix(A)
print(A * A)
print(multiply(A, A))

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
# !numpy的array具有与matlab向量同样的功能
a = np.array([[1,2],[3,4]])
b = np.array([[1,3],[5,6]])
print(a * b)

A = array([[1, 2], [3,4], [5, 6]])
print(A)
print(A * 2)
print(sin(A))
A = A[0:3, 1:2]
m = matrix(A)
print(m)
print(m.T)

# python numpy_test.py
# python3 numpy_test.py
