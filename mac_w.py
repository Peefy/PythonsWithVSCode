# python3 mac_w.py

import sys
import numpy.random as nmr
from collections import deque
import math
import mac_dugu_lib as dugu
import pickle
import pprint as ppr

## py3函数
def hello():
    print("hello world")

hello()
# 元组是值类型，列表，字典是引用类型
#可写函数说明
def printme( str = "dugu"):
   "打印任何传入的字符串"
   print (str);
   return;
 
#调用printme函数
printme( str = "hello me");
printme()

# 不定长参数
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;
 
# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, 60, 50 );

# lambda
sum = lambda arg1, arg2 : arg1 + arg2;
print(sum(12.3, 23.5))

X = int(2.7)
print(X)
# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域

total = 0; # 这是一个全局变量
# 可写函数说明
def sum2( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2; # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total;

#调用sum函数
total = sum2( 10, 20 );
print ("函数外是全局变量 : ", total)

# global 和 nonlocal关键字可以改变作用域

print(nmr.laplace(1.1))

## python3 数据结构
#列表list可以修改，tuple和字符串不行
A = [12,3,45.6]
print(A.count('str'))
A.append(17.9)
print(A)
A.sort(reverse=False)
print(A)
A.sort(reverse=True)
print(A)
queue_me = deque(['1', 'aeee', 'dugu'])
print(queue_me.popleft())
queue_me.append('ssss')
queue_me.append('sad')
print(queue_me)

#列表推导式
Y = [12, 23, 45]
print([[y, y ** 2] for y in Y]) 
wepon = [' sd   ', 'sss   ', '  assa']
print([[w, str(w).strip()] for w in wepon])
VET1 = [1, 2, 3]
VET2 = [4, 5, 6, 7]
print([[v1, v2] for v1 in VET1 for v2 in VET2])

#通过嵌套列表构成矩阵Matrix
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(M)

# del 删除语句
C = [1,2,3,4,'23','232',[1,2,3]]
del C[2]
print(C)

# 元组和序列
T = 12, 23, 45
U = 12,T
print(U)
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
dic_me = {str(x): x**2 for x in (2, 4, 6)} # 推导式创建字典
print(dic_me)
for k, v in dic_me.items():
    print(k, v)
i = 0
for k, v in enumerate(dic_me):
    print(i, k, v)
    i += 1
print('')
for k, v in enumerate(C):
    print(k, v)
print('')
for i in reversed(range(1, 10, 3)):
    print(i)
print('')
for i, j in zip(dic_me, C):
    print(i, j)

## python3 模块
for p in sys.argv:
    print(p)
print(sys.path)

dugu.print_func('dugu')

## python3 输入和输出
S = 'hello dugu\n'
print(repr(S))
print(str(S))
for i in range(1,11):
    print(repr(i).rjust(2), repr(i * i).rjust(3), end=' ')
    print(repr(i * i * i).rjust(4))
print('')
for i in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(i, i * i, i * i * i))
print('12'.zfill(5), '123456'.zfill(6))
print('{} {} {other}'.format(123, 345, other='1233333'))
#'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
PI = math.pi
print('{!a} {!s} {!r}'.format(PI, PI, PI))
print('the pi is %3.5f' % PI)
#键盘读入 input
#文件读入 open
myfile = open('file_test.txt','w')
myfile.write("123\n")
myfile.write("123\n")
print(myfile.write("'123444'\n"))
myfile.flush()
myfile.close()

dufile = open('file_test.txt','r')
print(dufile.readlines())
dufile.close()

# 相当于c#中的using
with open('file_test.txt', 'w') as f:
    f.write('1233333')
#pickle模块实现了对象的序列化和反序列化
data = {'key' : 123, 'value' : 'sdd'};
print(str(data))
with open('data.ini', 'wb') as wb:
    pickle.dump(data, wb)
with open('data.ini', 'rb') as rb:
    data_read = pickle.load(rb)
    ppr.pprint(data_read)
## pyhton3 OS


print()
