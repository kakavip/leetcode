#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#
from typing import Dict, List


# @lc code=start
class Solution:
    _cache: Dict[int, int] = {}

    def deleteAndEarn(self, nums: List[int]) -> int:
        _max = max(nums)
        n = len(nums)

        fre_nums: List[int] = [0] * (_max + 1)
        for i in range(n):
            fre_nums[nums[i]] += 1

        self._cache.clear()
        return max(self.solve(fre_nums, 0), self.solve(fre_nums, 1))

    def solve(self, fre_nums: List[int], next_idx: int) -> int:
        if next_idx in self._cache:
            return self._cache[next_idx]

        if next_idx >= len(fre_nums):
            return 0

        r = next_idx * fre_nums[next_idx] + max(
            self.solve(fre_nums, next_idx + 2), self.solve(fre_nums, next_idx + 3)
        )

        self._cache[next_idx] = r
        return r


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.deleteAndEarn([3, 4, 2]))
    print(s.deleteAndEarn([2, 2, 3, 3, 3, 4]))
