import sys
IS_TEST_DATA = False
if IS_TEST_DATA == True:
    datas = '[2.2 1]'
else:
    datas = sys.stdin.readline()
if datas is not None and len(datas) > 2:
    datas = datas[1:len(datas) - 1]
    nums = datas.split()
    for i in range(len(nums)):
        if '.' not in nums[i]:
            nums[i] = int(nums[i])
        else:
            nums[i] = float(nums[i])
    snums = list(sorted(list(set(nums))))
    for snum in snums:
        print(snum, end=' ')



