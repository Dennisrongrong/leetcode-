# -*- coding: utf-8 -*-
"""
@Time ： 2024/11/13 16:43
@Auth ： 归去来兮
@File ：获取数组最多的元素.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
nums=[3,2,2,3,2]
numDict = dict()
for num in nums:
    if num in numDict:
        numDict[num] += 1
    else:
        numDict[num] = 1
max = float('-inf')
max_index = -1
for num in numDict:
    if numDict[num] > max:
        max = numDict[num]
        max_index = num
print(max_index)



