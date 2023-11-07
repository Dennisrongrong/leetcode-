# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/5 10:21
@Auth ： 归去来兮
@File ：盛最多水的容器.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。
示例1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2：
输入：height = [1,1]
输出：1
思路
设两指针i,j，指向的水槽板高度分别为 h[i], h，此状态下水槽面积为 S(i,j)。由于可容纳水的高度由两板中的 短板 决定，因此可得如下 面积公式 ：
S(i,j)=min(h[i],h[j])×(j−i)S(i, j) = min(h[i], h[j]) × (j - i)
S(i,j)=min(h[i],h[j])×(j−i)
"""
height=[1,8,6,2,5,4,8,3,7]
i,j,res=0,len(height)-1,0
while i<j:
    if height[i]<height[j]:
        tmp=height[i]*(j-i)
        res=max(res,tmp)
        i=i+1
    if height[i]>=height[j]:
        tmp=height[j]*(j-i)
        res=max(res,tmp)
        j=j-1
print(res)
