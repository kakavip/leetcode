#
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def check(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if head is None:
            return True

        if head and not root:
            return False

        if root.val != head.val:
            return False

        return self.check(head.next, root.left) or self.check(head.next, root.right)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True

        if head and not root:
            return False

        result: bool = False
        if root.val == head.val and self.check(head, root):
            return True

        result = self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

        return result


# @lc code=end
