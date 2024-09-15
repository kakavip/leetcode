#
# @lc app=leetcode id=2807 lang=python3
#
# [2807] Insert Greatest Common Divisors in Linked List
#

import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        s_node: Optional[ListNode] = head
        while s_node and s_node.next:
            n_node: ListNode = ListNode(math.gcd(s_node.val, s_node.next.val))
            n_node.next = s_node.next
            s_node.next = n_node

            s_node = n_node.next

        return head


# @lc code=end
