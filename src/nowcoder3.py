
import sys

IS_TEST_DATA = True

if IS_TEST_DATA == True:
    datas = '15 10 4'
else:
    datas = sys.stdin.readline()

paras = datas.split()
n = int(paras[0])
k = int(paras[1])
m = int(paras[2])
q = [0] * (n + 1)
q[0] = 1
total = n
while total != 0:
    i = 0
    j = n + 1 

    kk = k
    for _ in range(0, kk):
        i = i + 1
        while q[i] == 1:
            i = i + 1
            if i >= n:
                i = 0
    mm = m
    for _ in range(0, mm):
        j = j - 1
        while q[j] != 0:
            j = j - 1     
            if j <= 1:
                j = n + 1
    q[i] = 1
    q[j] = 1
    if i == j:
        total = total - 1
    else:
        total = total - 2
    print(i, j)
