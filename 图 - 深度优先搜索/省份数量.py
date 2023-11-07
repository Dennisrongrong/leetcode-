# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/6 10:38
@Auth ： 归去来兮
@File ：省份数量.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
"""
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，
而 isConnected[i][j] = 0 表示二者不直接相连。
返回矩阵中 省份 的数量。

输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2

输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3

"""
isConnected = [[1,1,0],[1,1,0],[0,0,1]]

def dfs(i: int):
    for j in range(cities):
        if isConnected[i][j] == 1 and j not in vis:
            vis.add(j)
            dfs(j)


provs = 0
cities = len(isConnected)
vis = set()

for i in range(cities):
    if i not in vis:
        dfs(i)
        provs += 1
print("一共有%d"%(provs)+"个")