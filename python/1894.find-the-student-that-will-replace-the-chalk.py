#
# @lc app=leetcode id=1894 lang=python3
#
# [1894] Find the Student that Will Replace the Chalk
#

# @lc code=start
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        _sum: int = sum(chalk)
        n = len(chalk)

        k -= (k // _sum) * _sum
        for i in range(n):
            if k < chalk[i]:
                return i

            k -= chalk[i]

        return 0


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.chalkReplacer(chalk=[3, 4, 1, 2], k=25) == 1)
    print(s.chalkReplacer(chalk=[5, 1, 5], k=22) == 0)
