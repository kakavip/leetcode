#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
from collections import deque
from typing import Deque


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack: Deque[int] = deque()
        counter: int = 0

        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if not stack:
                    counter += 1
                else:
                    stack.pop()

        return counter + len(stack)


# @lc code=end
