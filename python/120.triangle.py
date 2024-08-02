#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        tri_min: List[List[int]] = [
            [float("inf")] * (i + 1) for i in range(len(triangle))
        ]

        tri_min[0][0] = triangle[0][0]
        for i in range(len(tri_min) - 1):
            for j in range(len(tri_min[i])):
                tri_min[i + 1][j] = min(
                    tri_min[i + 1][j], triangle[i + 1][j] + tri_min[i][j]
                )

                tri_min[i + 1][j + 1] = min(
                    tri_min[i + 1][j + 1], triangle[i + 1][j + 1] + tri_min[i][j]
                )

        return min(tri_min[-1])


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print(s.minimumTotal([[-10]]))
