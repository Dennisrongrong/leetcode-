# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/9 13:56
@Auth ： 归去来兮
@File ：有序数组的平方.py
@IDE ：PyCharm
@Motto:花中自幼微风起
示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]
示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
"""
class Solution:
    def sortedSquares(self, nums) :
        l, r, i = 0, len(nums)-1, len(nums)-1
        res = [float('inf')] * len(nums) # 需要提前定义列表，存放结果
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2: # 左右边界进行对比，找出最大值
                res[i] = nums[r] ** 2
                r -= 1 # 右指针往左移动
            else:
                res[i] = nums[l] ** 2
                l += 1 # 左指针往右移动
            i -= 1 # 存放结果的指针需要往前平移一位
        return res

alg=Solution()
nums = [-4,-1,0,3,10]
res=alg.sortedSquares(nums)
print(res)