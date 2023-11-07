# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/5 10:29
@Auth ： 归去来兮
@File ：子数组最大平均数 I.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
"""
给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
任何误差小于 10-5 的答案都将被视为正确答案。

示例 1：
输入：nums = [1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
示例 2：
输入：nums = [5], k = 1
输出：5.00000
"""
nums,k= [1,12,-5,-6,50,3], 4
mx = sum(nums[:k])
cnt = 0
for i in range(k):
    cnt += nums[i]
for j in range(k, len(nums)):
    cnt = cnt - nums[j - k] + nums[j]
    mx = max(mx, cnt)
print(1.0*mx/k)
