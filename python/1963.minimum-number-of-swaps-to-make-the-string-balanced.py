#
# @lc app=leetcode id=1963 lang=python3
#
# [1963] Minimum Number of Swaps to Make the String Balanced
#


# @lc code=start
from collections import deque


class Solution:
    def minSwaps(self, s: str) -> int:
        error_bracket: int = 0
        stack = deque()

        for c in s:
            if c == "[":
                stack.append(c)
            else:
                if not stack:
                    error_bracket += 1
                else:
                    stack.pop()

        return int((error_bracket + 1) / 2)


# @lc code=end
