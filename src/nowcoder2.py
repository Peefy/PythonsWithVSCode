
import sys

IS_TEST_DATA = False

if IS_TEST_DATA == True:
    datas = '[1 1 3 3 2 2]'
else:
    datas = sys.stdin.readline()

datas = datas[1:len(datas) - 1]
nums = datas.split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
snums = sorted(set(nums))
for snum in snums:
    print(snum, end=' ')



