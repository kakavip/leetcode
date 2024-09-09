#
# @lc app=leetcode id=2326 lang=python3
#
# [2326] Spiral Matrix IV
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
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix: List[List[int]] = [[-1] * n for _ in range(m)]

        # pre_head: Optional[ListNode] = None
        for i in range(min(n, m)):
            x, y = i, i
            if matrix[y][x] != -1:
                break
            if not head:
                break

            # to right
            # pre_head = None
            while x < n - i and head and matrix[y][x] == -1:
                matrix[y][x] = head.val

                # pre_head = head
                head = head.next
                x += 1

            x = n - i - 1
            # head = pre_head
            y += 1

            # to down
            # pre_head = None
            while y < m - i and head and matrix[y][x] == -1:
                matrix[y][x] = head.val

                # pre_head = head
                head = head.next
                y += 1
            y = m - i - 1
            # head = pre_head
            x -= 1

            # to left
            # pre_head = None
            while x >= i and head and matrix[y][x] == -1:
                matrix[y][x] = head.val

                # pre_head = head
                head = head.next
                x -= 1

            x = i
            # head = pre_head
            y -= 1
            # to up
            # pre_head = None
            while y >= i and head and matrix[y][x] == -1:
                matrix[y][x] = head.val

                # pre_head = head
                head = head.next
                y -= 1
            y = i
            # head = pre_head

        return matrix


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(
        s.spiralMatrix(
            3,
            5,
            head=ListNode(
                3,
                ListNode(
                    0,
                    ListNode(
                        2,
                        ListNode(
                            6,
                            ListNode(
                                8,
                                ListNode(
                                    1,
                                    ListNode(
                                        7,
                                        ListNode(
                                            9,
                                            ListNode(
                                                4,
                                                ListNode(
                                                    2,
                                                    ListNode(
                                                        5, ListNode(5, ListNode(0))
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        )
        == [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]]
    )

    print(
        s.spiralMatrix(1, 4, ListNode(0, ListNode(1, ListNode(2)))) == [[0, 1, 2, -1]]
    )
