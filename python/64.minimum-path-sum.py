#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
from typing import Dict, List, Tuple


class Solution:
    # _cache: Dict[Tuple[int, int], int] = {}

    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        # self._cache.clear()
        m = len(grid)
        n = len(grid[0])

        max_grid: List[List[int]] = [[0] * n for _ in range(m)]
        max_grid[0][0] = grid[0][0]
        for i in range(1, n):
            max_grid[0][i] = max_grid[0][i - 1] + grid[0][i]

        for i in range(1, m):
            max_grid[i][0] = max_grid[i - 1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                max_grid[i][j] = grid[i][j] + min(
                    max_grid[i][j - 1], max_grid[i - 1][j]
                )

        return max_grid[m - 1][n - 1]

    # def go(
    #     self, grid: List[List[int]], current: Tuple[int, int], finish: Tuple[int, int]
    # ) -> int:
    #     if current in self._cache:
    #         return self._cache[current]

    #     if current == finish:
    #         return grid[-1][-1]

    #     go_right = (current[0], current[1] + 1)
    #     go_bottom = (current[0] + 1, current[1])

    #     max_right = float("inf")
    #     max_bottom = float("inf")

    #     if go_right[1] <= finish[1]:
    #         max_right = self.go(grid, go_right, finish)
    #     if go_bottom[0] <= finish[0]:
    #         max_bottom = self.go(grid, go_bottom, finish)

    #     result: int = grid[current[0]][current[1]] + min(max_bottom, max_right)

    #     self._cache[current] = result
    #     return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(s.minPathSum([[1, 2, 3], [4, 5, 6]]))
