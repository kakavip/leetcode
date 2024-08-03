#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 0:
            return 0

        min_matrix: List[List[int]] = [[float("inf")] * n for _ in range(n)]
        min_matrix[0] = matrix[0].copy()

        for i in range(n - 1):
            for j in range(n):
                if j > 0:
                    min_matrix[i + 1][j - 1] = min(
                        min_matrix[i + 1][j - 1],
                        min_matrix[i][j] + matrix[i + 1][j - 1],
                    )
                min_matrix[i + 1][j] = min(
                    min_matrix[i + 1][j], min_matrix[i][j] + matrix[i + 1][j]
                )

                if j < n - 1:
                    min_matrix[i + 1][j + 1] = min(
                        min_matrix[i + 1][j + 1],
                        min_matrix[i][j] + matrix[i + 1][j + 1],
                    )

        return min(min_matrix[-1])


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
    print(s.minFallingPathSum([[-19, 57], [-40, -5]]))
