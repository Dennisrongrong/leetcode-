# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/9 9:25
@Auth ： 归去来兮
@File ：重新规划路线.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""

"""
n 座城市，从 0 到 n-1 编号，其间共有 n-1 条路线。因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。
去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。
路线用 connections 表示，其中 connections[i] = [a, b] 表示从城市 a 到 b 的一条有向路线。
今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。
请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。
题目数据 保证 每个城市在重新规划路线方向后都能到达城市 0 。

输入：n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
输出：3
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。

输入：n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
输出：2
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。

基本思路：题目说路线会形成一颗树，并且重新规划路线后都可以到达顶点0，
那么深入的理解一下这些信息就是说，重新规划线路后，从城市0出发，可以到达所有其他的城市，换言之从顶点0出发遍历，可以把整个树遍历到。
再结合给出的边只有n-1个，也就是说没有多余的边，两个顶点之间要么是顺着连接，
要么是逆着连接，这里顺的意思是顺着从树根遍历（从0出发）的方向可达，逆也就是逆着从0出发的方向。那么只要统计出顺着的边的个数，
也就找到了题目的答案，也即是需要调整的路线数。
把图（树）变为一个无向图，然后把顺着的边的权重设置为1，把逆着的权重设置为0，然后从0开始做BFS，顺道累加权重，遍历完即得答案。

"""
from collections import  deque
n=6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

graph=[]
for i in range(n):
    graph.append([])
for u,v in connections:
    graph[u].append((v, 1))
    graph[v].append((u, 0))
print(graph)

res = 0
queue = deque()
queue.append(0)
visited = [False] * n
visited[0] = True
print(visited)
while len(queue) > 0:
    x = queue.popleft()
    for y, w in graph[x]:
        if visited[y]:
            continue
        visited[y] = True
        res += w
        queue.append(y)
print(res)



