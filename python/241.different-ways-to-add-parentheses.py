#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }

        @cache
        def dp(start: int, end: int) -> List[int]:
            """Evaluate expression[start:end+1], expression[start]...expression[end]"""
            ans = []

            # Base case
            if end - start <= 1:
                return [int(expression[start : end + 1])]

            for i in range(start, end + 1):
                char = expression[i]

                if char.isdigit():
                    continue

                left = dp(start, i - 1)
                right = dp(i + 1, end)

                for left_val in left:
                    for right_val in right:
                        val = operations[char](left_val, right_val)

                        ans.append(val)

            return ans

        return dp(0, n - 1)


# @lc code=end
