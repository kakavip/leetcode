#
# @lc app=leetcode id=2938 lang=python3
#
# [2938] Separate Black and White Balls
#

# @lc code=start
from typing import List


class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)

        real_idx: int = 0
        num_steps: int = 0
        for i in range(n):
            if s[i] == "0":
                num_steps += i - real_idx
                real_idx += 1

        return num_steps


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.minimumSteps("101") == 1)
    print(s.minimumSteps("100") == 2)
