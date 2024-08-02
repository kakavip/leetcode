#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

from typing import Dict, List


# @lc code=start
class Solution:
    _cache: Dict[int, int] = {}

    def rob(self, nums: List[int]) -> int:
        self._cache.clear()

        # print(self._cache)
        return max(self.solve(nums, 0), self.solve(nums, 1))

    def solve(self, nums: List[int], next_idx: int) -> int:
        if next_idx in self._cache:
            return self._cache[next_idx]

        if next_idx >= len(nums):
            return 0

        r = nums[next_idx] + max(
            self.solve(nums, next_idx + 2), self.solve(nums, next_idx + 3)
        )
        self._cache[next_idx] = r

        return r


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
    print(s.rob([2, 7, 9, 3, 1]))
