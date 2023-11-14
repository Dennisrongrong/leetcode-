# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/9 9:01
@Auth ： 归去来兮
@File ：删除链表的中间节点.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
"""
输入：head = [1,3,4,7,1,2,6]
输出：[1,3,4,1,2,6]
解释：
上图表示给出的链表。节点的下标分别标注在每个节点的下方。
由于 n = 7 ，值为 7 的节点 3 是中间节点，用红色标注。
返回结果为移除节点后的新链表。
输入：head = [1,2,3,4]
输出：[1,2,4]
解释：
上图表示给出的链表。
对于 n = 4 ，值为 3 的节点 2 是中间节点，用红色标注。 
输入：head = [2,1]
输出：[2]
解释：
上图表示给出的链表。
对于 n = 2 ，值为 1 的节点 1 是中间节点，用红色标注。
值为 2 的节点 0 是移除节点 1 后剩下的唯一一个节点。
"""
# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head.next is None:
#             return None
#         slow, fast, pre = head, head, None
#         while fast and fast.next:
#             fast = fast.next.next
#             pre = slow
#             slow = slow.next
#         pre.next = pre.next.next
#         return head



