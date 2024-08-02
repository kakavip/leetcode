#
# @lc app=leetcode id=2134 lang=python3
#
# [2134] Minimum Swaps to Group All 1's Together II
#

# @lc code=start
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        num_1s = sum(nums)
        n = len(nums)

        _sum = 0
        for i in range(0 - num_1s, 0):
            _sum += nums[i]

        _min = num_1s - _sum

        for i in range(0, n):
            _sum += nums[i] - nums[i - num_1s]

            if _min > num_1s - _sum:
                _min = num_1s - _sum

        return _min


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.minSwaps([0, 1, 0, 1, 1, 0, 0]) == 1, "Test 1"
    assert s.minSwaps([0, 1, 1, 1, 0, 0, 1, 1, 0]) == 2, "Test 2"
    assert s.minSwaps([1, 1, 0, 0, 1]) == 0, "Test 3"
