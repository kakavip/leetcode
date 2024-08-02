#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#


# @lc code=start
from typing import Dict, List, Tuple


class Solution:
    _cache: Dict[Tuple[int, int], int] = {}

    def uniquePaths(self, m: int, n: int) -> int:
        self._cache.clear()
        return self.go((0, 0), (m - 1, n - 1)) + 1

    def go(self, current: Tuple[int, int], finish: Tuple[int, int]) -> int:
        if current == finish:
            return 0

        if current in self._cache:
            return self._cache[current]

        result = -1
        if current[0] < finish[0]:
            result += 1
            result += self.go((current[0] + 1, current[1]), finish)
        if current[1] < finish[1]:
            result += 1
            result += self.go((current[0], current[1] + 1), finish)

        self._cache[current] = result

        return result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 7))
    print(s.uniquePaths(3, 2))
    print(s.uniquePaths(23, 12))
