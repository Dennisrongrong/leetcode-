# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/6 17:04
@Auth ： 归去来兮
@File ：二分查找.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
nums ,target = [-1,0,3,5,9,12],9
def search(nums,target):
    left=0
    right = len(nums) - 1
    while left <= right :
        middle = (left + right) // 2
        if nums[middle] > target:
            right=middle - 1
        elif nums[middle] < target:
            left=middle + 1
        else:
            return middle
middle=search(nums,target)
print(middle)
