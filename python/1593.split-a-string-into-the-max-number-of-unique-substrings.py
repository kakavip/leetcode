#
# @lc app=leetcode id=1593 lang=python3
#
# [1593] Split a String Into the Max Number of Unique Substrings
#

# @lc code=start
from typing import List, Set


class Solution:
    result: float

    def maxUniqueSplit(self, s: str) -> int:
        self.result = -float("inf")

        def backtrack(sub_s: str, stack: Set[str]):
            if sub_s == "":
                self.result = max(self.result, len(stack))

            idx: int = 0
            for i in range(1, len(sub_s) + 1):
                if sub_s[idx:i] not in stack:
                    stack.add(sub_s[idx:i])
                    backtrack(sub_s[i:], stack)
                    stack.remove(sub_s[idx:i])

        backtrack(s, set())
        return self.result


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.maxUniqueSplit("ababccc") == 5)
    print(s.maxUniqueSplit("aba") == 2)
    print(s.maxUniqueSplit("aa") == 1)
    print(s.maxUniqueSplit("wwwzfvedwfvhsww") == 11)
