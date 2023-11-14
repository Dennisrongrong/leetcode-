# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/9 9:07
@Auth ： 归去来兮
@File ：奇偶链表.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
"""
给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。

第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。

请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。

你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。
输入: head = [1,2,3,4,5]
输出: [1,3,5,2,4]

输入: head = [2,1,3,5,6,4,7]
输出: [2,3,6,7,1,5,4]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head :
#             return None
#         evenHead = head.next
#         odd, even = head, evenHead
#         while even and even.next:
#             odd.next = even.next
#             odd = odd.next
#             even.next = odd.next
#             even = even.next
#         odd.next = evenHead
#         return head


