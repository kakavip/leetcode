#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
from typing import List

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cached_list: List[int] = [0] * (len(nums) + 1)
        for num in nums:
            cached_list[num] += 1
        
        return cached_list.index(0)


# @lc code=end
