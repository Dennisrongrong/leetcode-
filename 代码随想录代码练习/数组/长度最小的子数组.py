# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/9 14:03
@Auth ： 归去来兮
@File ：长度最小的子数组.py
@IDE ：PyCharm
@Motto:花中自幼微风起

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
示例：
输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
"""
s ,nums =7, [2,3,1,2,4,3]


#滑动窗口模版
res=1000
cur_sum=0
i=0
for j in range(len(nums)):
    cur_sum+=nums[j]
    while cur_sum >= s :
        index = j - i + 1
        res = min (res,index)
        cur_sum -= nums[i]
        i = i + 1
print(res)

