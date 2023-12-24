#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
import math


class Solution:
    def climbStairs(self, n: int) -> int:
        n_w = 0

        n_2 = n // 2
        for i in range(n_2 + 1):
            _n = i + n - 2 * i
            n_w += math.comb(_n, i)
        return n_w


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(3))
    print(s.climbStairs(2))