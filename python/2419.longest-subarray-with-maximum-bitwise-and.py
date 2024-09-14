#
# @lc app=leetcode id=2419 lang=python3
#
# [2419] Longest Subarray With Maximum Bitwise AND
#

# @lc code=start
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums.append(0)
        _max = max(nums)
        n = len(nums)

        result: int = 1
        counter: int = 0
        for i in range(n):
            if nums[i] == _max:
                counter += 1
            else:
                if counter > 1:
                    result = max(result, counter)
                    counter = 0

        return result


# @lc code=end
