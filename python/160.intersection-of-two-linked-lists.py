#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None
        super().__init__()


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNodeTmp:
    base: ListNode = None
    next: None

    def __init__(self, base: ListNode):
        self.base = base


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        if headA == headB:
            return headA

        reverse_node_a: ListNodeTmp = reverse_list_note(headA)
        reverse_node_b: ListNodeTmp = reverse_list_note(headB)

        current_intersect_node: ListNode = None
        while reverse_node_a.base == reverse_node_b.base:
            current_intersect_node = reverse_node_a.base
            
            reverse_node_a = reverse_node_a.next
            reverse_node_b = reverse_node_b.next
            
            if not reverse_node_a or not reverse_node_b:
                break

        return current_intersect_node


def reverse_list_note(head: ListNode) -> ListNodeTmp:
    node: ListNode = head
    new_head: ListNodeTmp = None

    while node:
        tmp_node = ListNodeTmp(node)

        # assigne node
        tmp_node.next = new_head
        new_head = tmp_node

        # next
        node = node.next
    return new_head


# @lc code=end

if __name__ == "__main__":
    pass
