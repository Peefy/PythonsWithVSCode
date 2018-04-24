
#python3 matplotlib_test.py
#python matplotlib_test.py

import math
import numpy as np
import matplotlib.pylab as mat
import matplotlib.pyplot as plt
from matplotlib.pyplot import * 
from numpy import *


## plot 画一个函数咯
X = np.linspace(0,100,200)
Y = [math.log(1 + math.e ** x) for x in X]
plot(X, Y); show()
print((math.sin(1) + 1) * 0.7)
print((math.sin(1) + 1) * 0.2)
print(2 ** 0.5 * math.sin(1 + math.pi / 4.0))


## 迭代法解方程
x1 = 0; x2 = 0
x1_pre,x2_pre = x1,x2
x1,x2 = 0.7 * math.sin(x1) + 0.2 * math.cos(x2),0.7 * math.cos(x1) - 0.2 * math.sin(x2)
i = 2
while abs(x1_pre - x1) + abs(x2_pre - x2) >= 0.5 * 0.0001:
    x1_pre,x2_pre = x1,x2
    x1,x2 = 0.7 * math.sin(x1) + 0.2 * math.cos(x2),0.7 * math.cos(x1) - 0.2 * math.sin(x2)
    i += 1
print(i)
print(x1, x2)

## 范数
#无穷范数相当于求向量中元素绝对值的最大值
print(np.linalg.norm([1, 2, 3, 4], ord=np.inf))

x = arange(1,100,0.5)
y = sin(x)
figure()
plot(x, y)
show()
# python matplotlib_test.py
# python3 matplotlib_test.py
