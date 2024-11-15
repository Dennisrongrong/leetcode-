# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/6 17:13
@Auth ： 归去来兮
@File ：移除元素.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
nums ,val= [3,2,2,3], 3
def removeElement(nums,val):
    slowIndex = 0
    fastIndex = 0
    for fastIndex in range(len(nums)):
        if val != nums[fastIndex]:
            nums[slowIndex] = nums[fastIndex]
            slowIndex += 1
    return slowIndex

slowIndex=removeElement(nums,val)
print(slowIndex)
print(nums)