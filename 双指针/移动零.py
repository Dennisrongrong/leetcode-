# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/5 10:02
@Auth ： 归去来兮
@File ：移动零.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:
输入: nums = [0]
输出: [0]
"""
nums = [0,1,0,3,12]
n = len(nums)
j = 0
for i in range(n):
    if nums[i] != 0:
        nums[j] = nums[i]
        j += 1
while j < n:
    nums[j] = 0
    j += 1
print(nums)

