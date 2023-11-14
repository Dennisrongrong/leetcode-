# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/9 9:17
@Auth ： 归去来兮
@File ：链表最大孪生和.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
"""
在一个大小为 n 且 n 为 偶数 的链表中，对于 0 <= i <= (n / 2) - 1 的 i ，第 i 个节点（下标从 0 开始）的孪生节点为第 (n-1-i) 个节点 。
比方说，n = 4 那么节点 0 是节点 3 的孪生节点，节点 1 是节点 2 的孪生节点。这是长度为 n = 4 的链表中所有的孪生节点。
孪生和 定义为一个节点和它孪生节点两者值之和。
给你一个长度为偶数的链表的头节点 head ，请你返回链表的 最大孪生和 。
输入：head = [5,4,2,1]
输出：6
解释：
节点 0 和节点 1 分别是节点 3 和 2 的孪生节点。孪生和都为 6 。
链表中没有其他孪生节点。
所以，链表的最大孪生和是 6 。
输入：head = [4,2,2,3]
输出：7
解释：
链表中的孪生节点为：
- 节点 0 是节点 3 的孪生节点，孪生和为 4 + 3 = 7 。
- 节点 1 是节点 2 的孪生节点，孪生和为 2 + 2 = 4 。
所以，最大孪生和为 max(7, 4) = 7 。
输入：head = [1,100000]
输出：100001
解释：
链表中只有一对孪生节点，孪生和为 1 + 100000 = 100001 。


思路：先使用快慢指针找到中间位置，然后反转后半部分的链表，这样就找到了孪生兄弟，然后依次顺序相加即可
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverselist(self, node):
#         pre = None
#         while node:
#             nxt = node.next
#             node.next = pre
#             pre = node
#             node = nxt
#         return pre
#
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         if not head or not head.next:
#             return 0
#         slow, fast = head, head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         second_half = self.reverselist(slow)
#
#         max_sum = float('-inf')
#         first, second = head, second_half
#         while second:
#             max_sum = max(max_sum, first.val + second.val)
#             first = first.next
#             second = second.next
#
#         return max_sum


