# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/16 18:30
@Auth ： 归去来兮
@File ：螺旋矩阵.py
@IDE ：PyCharm
@Motto:花中自幼微风起

https://leetcode.cn/problems/spiral-matrix-ii/description/
给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:
输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]
"""

n = 3
nums = [[0]*n for i in range(n)]
startx ,starty =0, 0
loop ,mid = n//2,n//2
cnt = 1
for  offset in range(1,loop+1):
    for i in range(starty,n-offset): ## 从左至右，左闭右开
        nums[startx][i] = cnt
        cnt += 1
    for i in range(startx ,n -offset):## 从上至下，上闭下开
        nums[i][n -offset] = cnt
        cnt += 1
    for i in range(n-offset ,starty, -1):## 从右至左，右闭左开
        nums[n-offset][i] = cnt
        cnt += 1
    for i in range(n-offset ,startx, -1):## 从下至上，下闭上开
        nums[i][starty] = cnt
        cnt += 1
    startx += 1
    starty += 1
if n % 2 != 0 :			# n为奇数时，填充中心点
    nums[mid][mid] = cnt
print(nums)


