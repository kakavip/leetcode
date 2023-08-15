#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
from dataclasses import dataclass
from typing import Any, List, Optional, Tuple


@dataclass
class ListNode:
    val: int = 0
    next: Optional[Any] = None


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def normalize_node_value(root: Optional[ListNode]) -> int:
    if root is None:
        return 10

    coef: int = normalize_node_value(root.next)
    root.val *= coef

    return coef * 10


def calc_two_node(
    n1: Optional[ListNode], n2: Optional[ListNode]
) -> Tuple[ListNode, int]:
    if n1 is None or n2 is None:
        return None, 0
    coef: int = 10 ** (max(len(str(n1.val)), len(str(n2.val))) - 1)
    n1.val = int(n1.val / coef)
    n2.val = int(n2.val / coef)

    _sum: int = n1.val + n2.val

    if n1.next is not None:
        n3, sur = calc_two_node(n1.next, n2.next)
        _sum += sur
        return ListNode(_sum % 10, n3), int(_sum / 10)

    return ListNode(_sum % 10, None), int(_sum / 10)


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        normalize_node_value(l1)
        normalize_node_value(l2)

        slide_s1, slide_s2 = l1, l2
        _len = abs(len(str(slide_s1.val)) - len(str(slide_s2.val)))
        if len(str(slide_s1)) > len(str(slide_s2)):
            for _ in range(_len):
                slide_s2 = ListNode(0, slide_s2)
        elif len(str(slide_s1)) < len(str(slide_s2)):
            for _ in range(_len):
                slide_s1 = ListNode(0, slide_s1)

        l3, sur = calc_two_node(slide_s1, slide_s2)
        if sur:
            l3 = ListNode(sur, l3)

        return l3

    def addTwoNumbers2(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        stack_1: List[int] = []
        stack_2: List[int] = []

        slide_l1: Optional[ListNode] = l1
        while slide_l1:
            stack_1.append(slide_l1.val)
            slide_l1 = slide_l1.next

        slide_l2: Optional[ListNode] = l2
        while slide_l2:
            stack_2.append(slide_l2.val)
            slide_l2 = slide_l2.next

        # stack_1, stack_2 = [7, 2, 4, 3], [5, 6, 4]
        # print(f"STACK 1: {stack_1}, STACK 2: {stack_2}")

        stack_1.reverse()
        stack_2.reverse()

        stack_3: List[int] = []
        sur: int = 0
        _len_s1, _len_s2 = len(stack_1), len(stack_2)
        for i in range(max(_len_s1, _len_s2)):
            a1 = 0 if i >= _len_s1 else stack_1[i]
            a2 = 0 if i >= _len_s2 else stack_2[i]

            _s = a1 + a2 + sur
            stack_3.append(_s % 10)
            sur = int(_s / 10)

        if sur:
            stack_3.append(sur)

        # print(stack_3)

        result: Optional[ListNode] = None
        for num in stack_3:
            result = ListNode(num, result)
        return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # s.addTwoNumbers(ListNode(0), ListNode(9))
    root = ListNode(7, ListNode(0))
    normalize_node_value(root)
    print(str(root))
