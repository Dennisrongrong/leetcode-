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


基本思路：计算连通分量数的另一个方法是使用并查集。初始时，每个城市都属于不同的连通分量。
遍历矩阵 isConnected。如果两个城市之间有相连关系，则它们属于同一个连通分量，对它们进行合并。
遍历矩阵 isConnected 的全部元素之后，计算连通分量的总数，即为省份的总数。
"""
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
cities = len(isConnected)
parent = list(range(cities))

def find(index: int) -> int:
    if parent[index] != index:
        parent[index] = find(parent[index])
    return parent[index]

def union(index1: int, index2: int):
    parent[find(index1)] = find(index2)


for i in range(cities):
    for j in range(i + 1, cities):
        if isConnected[i][j] == 1:
            union(i, j)

provinces = sum(parent[i] == i for i in range(cities))
print("一共有%d"%(provinces)+"个")