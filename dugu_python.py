#!/usr/bin/python3
from sys import path
import math
import keyword
import random

#python利用缩进编程，句尾没有分号

print("hello word")
print(1.2 * 2.3)

print(math.sin(math.pi / 2))  #这是一条注释
#python基础语法
print(keyword.kwlist)
if True:
    print(True)
    print(1.1 / 2)
elif False:
    pass
else:
    pass

#续航符：\

items = ['one', 'two', 'three', 'four']
print('\n')
print(items)

# py中有四种数据类型：整数、长整数、浮点数和复数
# py中使用单引号和双引号完全相同

wordStr = '这是一个字符串\n'
print(wordStr)

#py可以在同一行中使用多条语句，语句之间使用分号(;)分隔，以下是一个简单的实例
x = 'dugu'
print(x)
#py不换行输出
print(x, end=' ')
print(x, end=' ')
print(path.count(1))
#print(max.__doc__)

#py变量就是变量，所说的类型是变量所指内存中对象的类型
#py中有六个标准的数据类型：Number(数字)、String(字符串)
#List(列表)、Tuple(元组)、Sets(集合)、Dictionary(字典)
a, b, c, d = 20, True, 3.3, 1+2j 
print(type(a), type(b), type(c), type(d))
#isinstance和type的区别
#type()不会认为子类和父类是一种类型
#isinstance()会认为子类是一种父类类型
del x   #删除对象;
#加法，减法，乘法，除法，除法求模，乘方
print(5 + 4, 4.3 - 2, 3 * 7, 2 / 4, 2 // 4, 2 ** 5)
#复数的两种方式
fu = complex(2, 3)
strDuGu = 'Runoob'
 
print(strDuGu)          # 输出字符串
print(strDuGu[0:-1])    # 输出第一个到倒数第二个的所有字符
print(strDuGu[0])       # 输出字符串第一个字符
print(strDuGu[2:5])     # 输出从第三个开始到第五个的字符
print(strDuGu[2:])      # 输出从第三个开始的后的所有字符
print(strDuGu * 2)      # 输出字符串两次
print(strDuGu + "TEST") # 连接字符串
#但是字符串索引取字符串是只读的，只能读不能写
#word[0] = 'm'会导致错误。 

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
 
print(list)            # 输出完整列表
print(list[0])         # 输出列表第一个元素
print(list[1:3])       # 从第二个开始输出到第三个元素
print(list[2:])        # 输出从第三个元素开始的所有元素
print(tinylist * 2)    # 输出两次列表
print(list + tinylist) # 连接列表

#与Python字符串不一样的是，列表中的元素是可以改变的：
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')
 
print(tuple)             # 输出完整元组
print(tuple[0])          # 输出元组的第一个元素
print(tuple[1:3])        # 输出从第二个元素开始到第三个元素
print(tuple[2:])         # 输出从第三个元素开始的所有元素
print(tinytuple * 2)     # 输出两次元组
print(tuple + tinytuple) # 连接元组

#string、list和tuple都属于sequence（序列）。

#集合
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
 
print(student)   # 输出集合，重复的元素被自动去掉
 
# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')
 
 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集 
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素

#字典
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
 
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
 
 
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

print({x: x**2 for x in (2, 4, 6)})

print(str(dict))
# 注意下面只输出两个元素1代表索引1的元素，也就是第2个元素；
# 3代表第三个元素
listDu = ['abcd', 786, 2.23, 'runoob', 70.2]
print(listDu[1:3])       # 从第二个开始输出到第三个元素
print(listDu[2:3])

flag = True
if flag:
    print('ssss')
else:
    pass
'''
python逻辑运算符 and or not
'''
test = 2
if test < 2 and test >= 0:
    print(test)
tests = (2, 3, 4)
if test in tests:
    print(str(test) + 'is in tests')

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b,end=',')
    a, b = b, a+b
print("")
#py条件控制
var1 = 100
if var1:
    print(var1)

if var1 >= 99:
    print(99.99)

print(5 == 6)

print(2 % 3)
print(4 & 4)
print(random.choice(range(100)))

# py循环语句
guess = 1
sum_dugu = 0
while guess < 100:
    sum_dugu += guess
    guess += 1
    if guess == 88:
        break
else:
    print("循环结束啦")
print("和为:",sum)
languages = ["c", "c++", "c#", "Python"]
for lan in languages:
    print(lan,end=' ')
    print("")
languages = {"c", "c++", "c#", "Python"}
for lan in languages:
    print(lan,end=' ')
    print("")
languages = ("c", "c++", "c#", "Python")
for lan in languages:
    print(lan,end=' ')
    print("")

for letter in "DuGu":
    if letter == 'u':
        continue
    print("the letter is", letter)

varNum = 10
while varNum > 0:
    print("now the num is ",varNum)
    varNum -= 1
    if varNum == 5:
        break

print("good bye")

#while语句和for循环语句都可以加else(另外加break)
cards = ["A", "B", "C", "D"]
for card in cards:
    if card == "C":
        print(card)
        break
    print("card is", card)
else:
    print("no card be found")
# range()函数
# 相当于matlab中的1:2:10
for j in range(1,10,2): 
    print("this num 1 is ", j)

#可以结合range函数和len函数遍历集合的索引
words = ["google", "microsoft", "facebook", "???", "??"]
for i in range(len(words)):
    print(i, words[i])

# 循环语句可以有 else 子句，它在穷尽列表(以for循环)
# 或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。 

# 查询质数的例子

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        print(n, '是质数')

# 使用 enumerate ,好使
dugustrs = ["?", "??", "???", "????"]
for i, o in enumerate(dugustrs):
    print(i, o)

## py3迭代器与生成器


        