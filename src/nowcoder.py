
import sys
import math

IS_TEST_DATA = True

if IS_TEST_DATA == True:
    datas = '11 22 33 44'
else:
    datas = sys.stdin.readlines()
    
lines = datas.split()
for i in range(len(lines)):
    lines[i] = int(lines[i])

print(type(lines[0]))
