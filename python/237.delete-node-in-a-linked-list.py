#
# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
#


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # print(f"{node.val} - {node.next}")

        slide_node: ListNode = node
        while slide_node.next:
            slide_next: ListNode = slide_node.next
            slide_node.val = slide_next.val

            if slide_next.next == None:
                slide_node.next = None
                break

            slide_node = slide_next


# @lc code=end
