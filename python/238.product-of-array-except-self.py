#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul_temp1: List[int] = []
        mul_temp2: List[int] = []
        for idx, num in enumerate(nums):
            if not mul_temp1:
                mul_temp1.append(num)
            else:
                mul_temp1.append(mul_temp1[-1] * num)

            reverse_val = nums[-(idx + 1)]
            if not mul_temp2:
                mul_temp2.append(reverse_val)
            else:
                mul_temp2.append(mul_temp2[-1] * reverse_val)

        max_count: int = len(nums)
        result: List[int] = []
        for idx, num in enumerate(nums):
            idx1, idx2 = idx - 1, max_count - idx - 2
            val: int = 1
            if idx1 >= 0:
                val *= mul_temp1[idx1]
            if idx2 >= 0:
                val *= mul_temp2[idx2]
            # val: int = mul_temp1[idx1] * mul_temp2[idx2]

            result.append(val)

        return result


# @lc code=end
