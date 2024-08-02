#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
from typing import Dict, List


class Solution:
    _cache: Dict[int, int] = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self._cache.clear()
        return self.solve([0] + cost, 0)

    def solve(self, cost: List[int], next_idx: int) -> int:
        if next_idx in self._cache:
            return self._cache[next_idx]

        if next_idx >= len(cost):
            return 0

        r = min(self.solve(cost, next_idx + 1), self.solve(cost, next_idx + 2))
        self._cache[next_idx] = cost[next_idx] + r
        return self._cache[next_idx]


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.minCostClimbingStairs([10, 15, 20]))
    print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
