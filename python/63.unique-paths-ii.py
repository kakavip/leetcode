#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#


# @lc code=start
from typing import Dict, List, Tuple


class Solution:
    _cache: Dict[Tuple[int, int], int] = {}
    _obstacle: Dict[Tuple[int, int], bool] = {}

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self._cache.clear()
        self._obstacle.clear()

        if not obstacleGrid:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    self._obstacle[(i, j)] = True

        return self.go((0, 0), (m - 1, n - 1)) + 1

    def go(self, current: Tuple[int, int], finish: Tuple[int, int]) -> int:
        if current == finish:
            return 0

        if current in self._cache:
            return self._cache[current]

        result = -1
        if (
            current[0] < finish[0]
            and (current[0] + 1, current[1]) not in self._obstacle
        ):
            result += 1
            result += self.go((current[0] + 1, current[1]), finish)
        if (
            current[1] < finish[1]
            and (current[0], current[1] + 1) not in self._obstacle
        ):
            result += 1
            result += self.go((current[0], current[1] + 1), finish)

        self._cache[current] = result

        return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(s.uniquePathsWithObstacles([[0, 1], [0, 0]]))
