# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/9 9:15
@Auth ： 归去来兮
@File ：反转链表.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         def recur(cur, pre):
#             if not cur: return pre  # 终止条件
#             res = recur(cur.next, cur)  # 递归后继节点
#             cur.next = pre  # 修改节点引用指向
#             return res  # 返回反转链表的头节点
#
#         return recur(head, None)  # 调用递归并返回
