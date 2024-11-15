# -*- coding: utf-8 -*-
"""
@Time ： 2024/11/13 17:02
@Auth ： 归去来兮
@File ：给数组排序.py
@IDE ：PyCharm
@Motto:花中自幼微风起
题目大意
描述：给定一个非负整数数组 nums。

要求：重新排列数组中每个数的顺序，使之将数组中所有数字按顺序拼接起来所组成的整数最大。

说明：

。
。
示例：

输入：nums = [10,2]
输出："210"


输入：nums = [3,30,34,5,9]
输出："9534330"
Copy to clipboardErrorCopied
解题思路
思路 1：排序
本质上是给数组进行排序。假设 x、y 是数组 nums 中的两个元素。如果拼接字符串 x + y < y + x，则 y > x 。y 应该排在 x 前面。反之，则 y < x。

按照上述规则，对原数组进行排序即可。这里我们使用了 functools.cmp_to_key 自定义排序函数。

"""


import functools

class Solution:
    def largestNumber(self, nums) -> str:
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1
        nums_s = list(map(str, nums))
        nums_s.sort(key=functools.cmp_to_key(cmp), reverse=True)
        return str(int(''.join(nums_s)))
sol=Solution()
nums = [3,30,34,5,9]
res=sol.largestNumber(nums)
print(res)