# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/5 9:53
@Auth ： 归去来兮
@File ：股票价格跨度.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
"""
设计一个算法收集某些股票的每日报价，并返回该股票当日价格的跨度 。
当日股票价格的 跨度 被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。
例如，如果未来 7 天股票的价格是 [100,80,60,70,60,75,85]，那么股票跨度将是 [1,1,1,2,1,4,6] 。
解释(java)：
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // 返回 1
stockSpanner.next(80);  // 返回 1
stockSpanner.next(60);  // 返回 1
stockSpanner.next(70);  // 返回 2
stockSpanner.next(60);  // 返回 1
stockSpanner.next(75);  // 返回 4 ，因为截至今天的最后 4 个股价 (包括今天的股价 75) 都小于或等于今天的股价。
stockSpanner.next(85);  // 返回 6
思路
栈的元素可以是股票价格的下标（即天数）和股票价格的二元数对，并且在栈中先插入一个最大值作为天数为 −1天的价格，
来保证栈不会为空。调用next时，先将栈中价格小于等于此时 price的元素都弹出，
直到遇到一个大于 price的值，并将 price入栈，计算下标差返回。
"""

import math
class StockSpanner:
    def __init__(self):
        self.stack = [(-1, math.inf)]
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1
        while price >= self.stack[-1][1]:
            self.stack.pop()
        self.stack.append((self.idx, price))
        return self.idx - self.stack[-2][0]

prices=[100, 80, 60, 70, 60, 75, 85]
obj = StockSpanner()
for price in prices:
    print(obj.next(price))


