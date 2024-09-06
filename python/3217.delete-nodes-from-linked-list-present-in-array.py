#
# @lc app=leetcode id=3217 lang=python3
#
# [3217] Delete Nodes From Linked List Present in Array
#

from typing import List, Optional


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
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if head is None:
            return None

        n: int = max(nums) + 1
        _cache: List[int] = [0] * (max(nums) + 1)
        for v in nums:
            _cache[v] = 1

        while head.val < n and _cache[head.val] == 1:
            head = head.next

        slice_node: Optional[ListNode] = head
        if slice_node is None:
            return None

        while slice_node.next is not None:
            next_node: Optional[ListNode] = slice_node.next
            if next_node.val < n and _cache[next_node.val] == 1:
                slice_node.next = next_node.next
            else:
                slice_node = next_node

        return head

    def modifiedList2(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        n: int = max(nums) + 1
        _cache: List[int] = [0] * (max(nums) + 1)
        for v in nums:
            _cache[v] = 1

        slice_node: Optional[ListNode] = head
        if slice_node is None:
            return None

        result: Optional[ListNode] = None
        slice_result: Optional[ListNode] = result

        while slice_node is not None:
            if slice_node.val >= n or not _cache[slice_node.val]:
                if not result:
                    result = ListNode(slice_node.val)
                    slice_result = result
                else:
                    slice_result.next = ListNode(slice_node.val)
                    slice_result = slice_result.next

            slice_node = slice_node.next

        return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    s.modifiedList(
        [1, 2, 3], ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    )
