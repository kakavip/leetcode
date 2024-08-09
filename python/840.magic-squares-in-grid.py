#
# @lc app=leetcode id=840 lang=python3
#
# [840] Magic Squares In Grid
#

# @lc code=start
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        if m < 3 or n < 3:
            return 0

        r = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if grid[i][j] >= 15:
                    continue

                a = [0] * 15
                a[grid[i][j] - 1] = 1
                a[grid[i][j + 1] - 1] = 1
                a[grid[i][j + 2] - 1] = 1
                a[grid[i + 1][j] - 1] = 1
                a[grid[i + 1][j + 1] - 1] = 1
                a[grid[i + 1][j + 2] - 1] = 1
                a[grid[i + 2][j] - 1] += 1
                a[grid[i + 2][j + 1] - 1] = 1
                a[grid[i + 2][j + 2] - 1] = 1
                if sum(a[:9]) < 9:
                    continue

                diagonal_1 = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
                diagonal_2 = grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2]

                col1 = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
                col2 = grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1]
                if (
                    sum(grid[i][j : j + 3]) == sum(grid[i + 1][j : j + 3]) == 15
                    and col1 == col2 == 15
                    and diagonal_1 == diagonal_2 == 15
                ):
                    r += 1

        return r


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # print(s.numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))
    # print(s.numMagicSquaresInside([[5, 5, 5], [5, 5, 5], [5, 5, 5]]))
    print(
        s.numMagicSquaresInside(
            [
                [8, 0, 7, 4, 3, 2],
                [1, 10, 4, 4, 3, 8],
                [8, 5, 2, 9, 5, 1],
                [6, 0, 9, 2, 7, 6],
                [9, 0, 6, 9, 5, 1],
                [4, 2, 1, 4, 3, 8],
            ]
        )
    )
