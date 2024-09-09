#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        r = []
        head = self
        while head is not None:
            r.append(head.val)
            head = head.next

        return str(r)


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional


class Solution:
    def count(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        return 1 + self.count(head.next)

    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        n: int = self.count(head)

        mean_p: int = n // k
        result: List[Optional[ListNode]] = []
        for i in range(k):
            n_p = mean_p
            if n % (k - i) != 0:
                n_p = mean_p + 1

            n -= n_p

            r: Optional[ListNode] = head
            s_head: Optional[ListNode] = head
            pre_s: Optional[ListNode] = None
            while s_head is not None and n_p > 0:
                pre_s = s_head
                s_head = s_head.next
                n_p -= 1

            if pre_s is not None:
                head = pre_s.next
                pre_s.next = None
            else:
                head = None

            result.append(r)

        return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.splitListToParts(head=ListNode(1, ListNode(2, ListNode(3))), k=5))
    print(
        s.splitListToParts(
            head=ListNode(
                1,
                ListNode(
                    2,
                    ListNode(
                        3,
                        ListNode(
                            4,
                            ListNode(
                                5,
                                ListNode(
                                    6,
                                    ListNode(7, ListNode(8, ListNode(9, ListNode(10)))),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            k=3,
        )
    )
