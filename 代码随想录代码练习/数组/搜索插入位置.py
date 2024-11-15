# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/6 18:46
@Auth ： 归去来兮
@File ：搜索插入位置.py
@IDE ：PyCharm
@Motto:花中自幼微风起
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
示例 1:
输入: [1,3,5,6], 5
输出: 2
示例 2:
输入: [1,3,5,6], 2
输出: 1
示例 3:
输入: [1,3,5,6], 7
输出: 4
示例 4:
输入: [1,3,5,6], 0
输出: 0
"""

nums,val = [1,3,5,6] ,2
def search(nums,val):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left+right)//2
        if nums[middle] > val:
            right = middle - 1
        elif nums[middle] < val:
            left = middle + 1
        else:
            return middle
    return right + 1

middle=search(nums,val)
print(middle)
