# -*- coding: utf-8 -*-
"""
@Time ： 2024/11/13 16:54
@Auth ： 归去来兮
@File ：合并区间.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort(key=lambda x: x[0])
ans = []
for interval in intervals:
        if not ans or ans[-1][1] < interval[0]:
             ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])
print(ans)