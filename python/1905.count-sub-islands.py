#
# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
#

# @lc code=start

from typing import Dict, List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if not grid1 or not [grid1[0]]:
            return 0
        m, n = len(grid1), len(grid1[0])
        # marks: List[int] = [0] * (m * n)
        # for i in range(m):
        #     for j in range(n):
        #         if grid1[i][j] == 1:
        #             marks[i * m + j] = 1

        def fill(i: int, j: int, m: int, n: int) -> bool:
            result: bool = True

            if grid1[i][j] != 1:
                result = False

            grid2[i][j] = 0
            if i > 0 and grid2[i - 1][j] == 1:
                result = fill(i - 1, j, m, n) and result
            if i < m - 1 and grid2[i + 1][j] == 1:
                result = fill(i + 1, j, m, n) and result

            if j > 0 and grid2[i][j - 1] == 1:
                result = fill(i, j - 1, m, n) and result
            if j < n - 1 and grid2[i][j + 1] == 1:
                result = fill(i, j + 1, m, n) and result
            return result

        counter: int = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if fill(i, j, m, n) is True:
                        # print("I: ", i, " J: ", j)
                        counter += 1

        return counter


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(
        s.countSubIslands(
            grid1=[
                [1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 1, 1],
            ],
            grid2=[
                [1, 1, 1, 0, 0],
                [0, 0, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [1, 0, 1, 1, 0],
                [0, 1, 0, 1, 0],
            ],
        )
        == 3
    )
    print(
        s.countSubIslands(
            grid1=[
                [1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [1, 0, 1, 0, 1],
            ],
            grid2=[
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [1, 0, 0, 0, 1],
            ],
        )
        == 2
    )
