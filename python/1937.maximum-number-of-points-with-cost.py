#
# @lc app=leetcode id=1937 lang=python3
#
# [1937] Maximum Number of Points with Cost
#

# @lc code=start
from typing import Dict, List, Tuple


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        prev = points[0]

        for i in range(1, m):
            left = [-float("inf")] * n
            right = [-float("inf")] * n

            left[0], right[n - 1] = prev[0], prev[n - 1]
            for k in range(1, n):
                left[k] = max(left[k - 1] - 1, prev[k])

                reverse_k: int = n - 1 - k
                right[reverse_k] = max(right[reverse_k + 1] - 1, prev[reverse_k])

            # print("LEFT: ", left)
            # print("RIGHT: ", right)

            for k in range(n):
                prev[k] = points[i][k] + max(right[k], left[k])

        # print(prev)
        return max(prev)


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maxPoints([[1, 2, 3], [1, 5, 1], [3, 1, 1]]) == 9)
    print(s.maxPoints([[1, 5], [2, 3], [4, 2]]) == 11)
    print(
        s.maxPoints(
            [
                [5, 4, 9, 4, 8, 0, 8],
                [3, 1, 3, 6, 7, 8, 3],
                [7, 10, 7, 7, 0, 1, 4],
                [3, 6, 3, 4, 10, 9, 5],
                [7, 8, 8, 5, 6, 8, 5],
                [5, 7, 4, 4, 4, 3, 1],
                [3, 5, 1, 8, 2, 3, 3],
            ]
        )
        == 49
    )

[
    [5, 4, 9, 4, 8, 0, 8],
    [3, 1, 3, 6, 7, 8, 3],
    [7, 10, 7, 7, 0, 1, 4],
    [3, 6, 3, 4, 10, 9, 5],
    [7, 8, 8, 5, 6, 8, 5],
    [5, 7, 4, 4, 4, 3, 1],
    [3, 5, 1, 8, 2, 3, 3],
]

[
    [5, 4, 9, 8, 8, 7, 8],
    [3, 2, 3, 6, 7, 8, 7],
    [7, 10, 9, 8, 7, 6, 5],
    [3, 6, 5, 4, 10, 9, 8],
    [7, 8, 8, 7, 6, 8, 7],
    [5, 7, 6, 5, 4, 3, 2],
    [3, 5, 4, 8, 7, 6, 5],
]

[
    [7, 8, 9, 7, 8, 7, 8],
    [3, 4, 5, 6, 7, 8, 3],
    [9, 10, 7, 7, 2, 3, 4],
    [6, 7, 8, 9, 10, 9, 5],
    [7, 8, 8, 6, 7, 8, 5],
    [6, 7, 4, 4, 4, 3, 1],
    [5, 6, 7, 8, 2, 3, 3],
]
