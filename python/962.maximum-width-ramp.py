#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
from collections import deque
from typing import List


def monotonic_decreasing_stack(nums):
    stack = deque()
    for idx, num in enumerate(nums):
        if not stack or nums[stack[-1]] > num:
            stack.append(idx)

    return stack


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n: int = len(nums)
        _max: int = 0

        stack = monotonic_decreasing_stack(nums)

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                _max = max(_max, i - stack[-1])
                stack.pop()

        return _max


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.maxWidthRamp([6, 0, 8, 2, 1, 5]) == 4)
    print(s.maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7)
